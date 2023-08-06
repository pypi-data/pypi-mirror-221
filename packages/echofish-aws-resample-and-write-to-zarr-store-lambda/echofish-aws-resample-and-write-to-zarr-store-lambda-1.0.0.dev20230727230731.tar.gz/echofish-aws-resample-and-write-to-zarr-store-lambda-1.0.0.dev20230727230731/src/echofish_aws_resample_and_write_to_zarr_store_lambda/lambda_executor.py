# lambda_executor.py
import json
import os
import glob
import shutil
import s3fs
import zarr
from scipy import interpolate
import geopandas
from datetime import datetime
import boto3
from botocore.exceptions import ClientError
import numpy as np
import xarray as xr
import pandas as pd

TEMPDIR = "/tmp"

MAX_POOL_CONNECTIONS = 64
MAX_CONCURRENCY = 100
TILE_SIZE = 512

SYNCHRONIZER = None  # TODO

class LambdaExecutor:

    ############################################################################
    def __init__(
            self,
            s3_operations,
            s3fs_operations,
            dynamo_operations,
            sns_operations,
            output_bucket,
            table_name,
            output_bucket_access_key,
            output_bucket_secret_access_key,
            done_topic_arn,
    ):
        self.__s3 = s3_operations
        self.__s3fs = s3fs_operations
        self.__dynamo = dynamo_operations
        self.__sns_operations = sns_operations
        self.__output_bucket = output_bucket
        self.__table_name = table_name
        self.__output_bucket_access_key = output_bucket_access_key
        self.__output_bucket_secret_access_key = output_bucket_secret_access_key
        self.__done_topic_arn = done_topic_arn

    ############################################################################
    # def __delete_all_local_raw_and_zarr_files(self):  # good
    #     """Used to clean up any residual files from warm lambdas
    #     to keep the storage footprint below the 512 MB allocation.
    #
    #     Returns
    #     -------
    #     None : None
    #         No return value.
    #     """
    #     print('Deleting all local raw and zarr files')
    #     for i in ['*.raw*', '*.zarr']:
    #         for j in glob.glob(i):
    #             # print(f'Deleting {j}')
    #             if os.path.isdir(j):
    #                 shutil.rmtree(j, ignore_errors=True)
    #             elif os.path.isfile(j):
    #                 os.remove(j)

    ############################################################################
    # def __set_processing_status(
    #         self,
    #         ship_name: str,
    #         cruise_name: str,
    #         sensor_name: str,
    #         file_name: str,
    #         new_status: str
    # ):
    #     # Updates PIPELINE_STATUS via new_status value
    #     # HASH: FILE_NAME, RANGE: SENSOR_NAME
    #     self.__dynamo.put_item(
    #         table_name=self.__table_name,
    #         item={
    #             'FILE_NAME': {'S': file_name},  # HASH
    #             'SHIP_NAME': {'S': ship_name},
    #             'CRUISE_NAME': {'S': cruise_name},
    #             'SENSOR_NAME': {'S': sensor_name},  # RANGE
    #             'PIPELINE_TIME': {'S': datetime.now().isoformat(timespec="seconds") + "Z"},
    #             'PIPELINE_STATUS': {'S': new_status},
    #         }
    #     )

    ############################################################################
    # def __update_processing_status(
    #         self,
    #         cruise_name,
    #         file_name,
    #         new_status
    # ):
    #     self.__dynamo.update_item(
    #         table_name=self.__table_name,
    #         key={
    #             'FILE_NAME': {'S': file_name},  # Partition Key
    #             'CRUISE_NAME': {'S': cruise_name},  # Sort Key
    #         },
    #         expression='SET #PS = :ps',
    #         attribute_names={
    #             '#PS': 'PIPELINE_STATUS'
    #         },
    #         attribute_values={
    #             ':ps': {
    #                 'S': new_status
    #             }
    #         }
    #     )

    ############################################################################
    def __get_processing_status(
            self,
            file_name,
            cruise_name
    ):
        # HASH: FILE_NAME, RANGE: SENSOR_NAME
        item = self.__dynamo.get_item(
            TableName=self.__table_name,
            Key={
                'FILE_NAME': {'S': file_name},  # Partition Key
                'CRUISE_NAME': {'S': cruise_name},  # Sort Key
            })
        if item is None:
            return 'NONE'
        return item['PIPELINE_STATUS']['S']

    ############################################################################
    def __zarr_info_to_table(
            self,
            cruise_name,
            file_name,
            zarr_path,
            min_echo_range,
            max_echo_range,
            num_ping_time_dropna,
            start_time,
            end_time,
            frequencies,
            channels
    ):
        self.__dynamo.update_item(
            table_name=self.__table_name,
            key={
                'FILE_NAME': {'S': file_name},  # Partition Key
                'CRUISE_NAME': {'S': cruise_name},  # Sort Key # TODO: should be FILE_NAME & SENSOR_NAME so they are truely unique for when two sensors are processed within one cruise
            },
            expression='SET #ZB = :zb, #ZP = :zp, #MINER = :miner, #MAXER = :maxer, #P = :p, #ST = :st, #ET = :et, #F = :f, #C = :c',
            attribute_names={
                '#ZB': 'ZARR_BUCKET',
                '#ZP': 'ZARR_PATH',
                '#MINER': 'MIN_ECHO_RANGE',
                '#MAXER': 'MAX_ECHO_RANGE',
                '#P': 'NUM_PING_TIME_DROPNA',
                '#ST': 'START_TIME',
                '#ET': 'END_TIME',
                '#F': 'FREQUENCIES',
                '#C': 'CHANNELS',
                ### TODO: don't actually need to do with "update_item" operation ###
                # SHIP_NAME,SENSOR_NAME,PIPELINE_TIME,PIPELINE_STATUS
            },
            attribute_values={
                ':zb': {
                    'S': self.__output_bucket
                },
                ':zp': {
                    'S': zarr_path
                },
                ':miner': {
                    'N': str(np.round(min_echo_range, 4))
                },
                ':maxer': {
                    'N': str(np.round(max_echo_range, 4))
                },
                ':p': {
                    'N': str(num_ping_time_dropna)
                },
                ':st': {
                    'S': start_time
                },
                ':et': {
                    'S': end_time
                },
                ':f': {
                    'L': [{'N': str(i)} for i in frequencies]
                },
                ':c': {
                    'L': [{'S': i} for i in channels]
                }
            }
        )

    ############################################################################
    ############################################################################
    # def __write_geojson_to_file(
    #         self,
    #         store_name,
    #         data
    # ) -> None:
    #     """Write the GeoJSON file inside the Zarr store folder. Note that the
    #     file is not a technical part of the store, this is more of a hack
    #     to help pass the data along to the next processing step.
    #
    #     Parameters
    #     ----------
    #     path : str
    #         The path to a local Zarr store where the file will be written.
    #     data : str
    #         A GeoJSON Feature Collection to be written to output file.
    #
    #     Returns
    #     -------
    #     None : None
    #         No return value.
    #     """
    #     with open(os.path.join(store_name, 'geo.json'), "w") as outfile:
    #         outfile.write(data)

    ############################################################################
    ############################################################################
    # def __remove_existing_s3_objects(
    #         self,
    #         prefix
    # ):
    #     print(f'Removing existing s3 objects from: {self.__output_bucket} with prefix {prefix}')
    #     keys = self.__s3.list_objects(
    #         bucket_name=self.__output_bucket,
    #         prefix=prefix,
    #         access_key_id=self.__output_bucket_access_key,
    #         secret_access_key=self.__output_bucket_secret_access_key
    #     )
    #     for key in keys:
    #         self.__s3.delete_object(
    #             bucket_name=self.__output_bucket,
    #             key=key,
    #             access_key_id=self.__output_bucket_access_key,
    #             secret_access_key=self.__output_bucket_secret_access_key
    #         )
    #     print('Removing existing s3 objects done')

    ############################################################################
    # def __upload_files(
    #         self,
    #         local_directory,
    #         object_prefix
    # ):
    #     print('Upload files')
    #     for subdir, dirs, files in os.walk(local_directory):
    #         for file in files:
    #             local_path = os.path.join(subdir, file)
    #             # print(local_path)
    #             s3_key = os.path.join(object_prefix, local_path)
    #             self.__s3.upload_file(
    #                 file_name=local_path,
    #                 bucket_name=self.__output_bucket,
    #                 key=s3_key,
    #                 access_key_id=self.__output_bucket_access_key,
    #                 secret_access_key=self.__output_bucket_secret_access_key
    #             )
    #     # print('Done uploading files')

    ############################################################################
    #####################################################################

    def __get_table_as_dataframe(self) -> pd.DataFrame:
        print('get table as dataframe')
        session = boto3.Session()
        try:
            print(self.__table_name)
            #
            # table = self.__dynamo.Table(self.__table_name)
            table = self.__dynamo.get_table(table_name=self.__table_name)
            #
            # Note: table.scan() has 1 MB limit on results so pagination is used.
            response = table.scan()
            data = response['Items']
            while 'LastEvaluatedKey' in response:
                response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
                data.extend(response['Items'])
        except ClientError as err:
            print('Problem finding the dynamodb table')
            raise err
        df = pd.DataFrame(data)
        print(df.shape)
        # assert(  # TODO: need to assure that none are marked as processing still
        #     np.all(df['PIPELINE_STATUS'] == PIPELINE_STATUS.SUCCESS.value) # "POPULATING_CRUISE_ZARR"
        # ), "None of the status fields should still be processing."
        # df_success = df[df['PIPELINE_STATUS'] == PIPELINE_STATUS.SUCCESS.value]
        df_success = df[df['PIPELINE_STATUS'] == "POPULATING_CRUISE_ZARR"]
        if df_success.shape[0] == 0:
            raise
        return df_success.sort_values(by='START_TIME', ignore_index=True)


    ############################################################################
    # TODO: need to pass in key/secret as optionals
    def __get_s3_zarr_as_xr(
            self,
            zarr_path: str
    ) -> xr.core.dataset.Dataset:
        print('getting s3 zarr as xr')
        # path should be like: f's3://{input_zarr_bucket}/{input_zarr_path}'
        store = self.__s3fs.s3_map(
            s3_zarr_store_path=f"s3://{self.__output_bucket}/{zarr_path}",
            access_key_id=self.__output_bucket_access_key,
            secret_access_key=self.__output_bucket_secret_access_key,
        )
        # You are already using dask, this is assumed by open_zarr, not the same as open_dataset(engine=“zarr”)
        return xr.open_zarr(store=store, consolidated=None)  # synchronizer=SYNCHRONIZER

    ############################################################################
    ############################################################################
    def __interpolate_data(
            self,
            minimum_resolution: float,  # get from df
            maximum_cruise_depth_meters: float,  # get from df
            file_xr: xr.Dataset,  # need to figure out which time values are removed
            cruise_zarr: zarr.Group,
            start_ping_time_index: int,
            end_ping_time_index: int,
            indices: np.ndarray, # the file_xr ping_time and Sv indices that are not np.nan
    ) -> np.ndarray:
        # read remotely once to speed up
        #
        # Note: file_zarr dimensions are (frequency, time, depth)
        frequencies = file_xr.channel.shape[0]
        file_sv = file_xr.Sv.values  # (4, 9779, 1302)
        all_file_depth_values = file_xr.echo_range.values[:, :, :]  # TODO
        # Note: cruise_zarr dimensions are (depth, time, frequency)
        cruise_sv_subset = np.empty(shape=cruise_zarr.sv[:, start_ping_time_index:end_ping_time_index, :].shape)
        cruise_sv_subset[:, :, :] = np.nan # (5208, 9778, 4)
        # grid evenly spaced depths over the specified interval
        all_cruise_depth_values = np.linspace(
            start=0,
            stop=maximum_cruise_depth_meters,
            num=int(maximum_cruise_depth_meters / minimum_resolution) + 1,
            endpoint=True
        )  # 5208
        #
        for iii in range(frequencies):
            for jjj in range(len(indices)):
                y = file_sv[iii, indices[jjj], :]  # y.shape = (4, 4871, 5208) -> frequency, time, depth
                # all_Sv is inly 1302 depth measurements
                f = interpolate.interp1d(  # Interpolate a 1-D function.
                    x=all_file_depth_values[iii, indices[jjj], :],
                    y=y,  # Need to strip off unwanted timestamps
                    kind='nearest',
                    # axis=0,
                    bounds_error=False,
                    fill_value=np.nan
                )
                y_new = f(all_cruise_depth_values)  # y_new.shape = (4, 4871, 5208) --> (frequency, time, depth)
                # Note: dimensions are (depth, time, frequency)
                cruise_sv_subset[:, jjj, iii] = y_new #.transpose((2, 1, 0))  # (5208, 89911, 4)
        #
        return cruise_sv_subset

    ############################################################################

    def __s3_zarr(
            self,
            output_zarr_bucket: str,
            ship_name: str,
            cruise_name: str,
            sensor_name: str,
            # zarr_synchronizer: Union[str, None] = None,
    ):
        # Environment variables are optional parameters
        s3 = s3fs.S3FileSystem(
            key=os.getenv('ACCESS_KEY_ID'),
            secret=os.getenv('SECRET_ACCESS_KEY'),
        )
        root = f's3://{output_zarr_bucket}/level_2/{ship_name}/{cruise_name}/{sensor_name}/{cruise_name}.zarr'
        # TODO: check if directory exists
        store = s3fs.S3Map(root=root, s3=s3, check=True)
        # TODO: properly synchronize with efs mount
        # TODO: zarr.ThreadSynchronizer()
        # Note: 'r+' means read/write (store must already exist)
        cruise_zarr = zarr.open(store=store, mode="r+") #, zarr_synchronizer=zarr_synchronizer)
        return cruise_zarr


    ############################################################################
    def __get_spatiotemporal_indices(
            self,
            input_zarr_bucket: str,
            input_zarr_path: str,
    ) -> tuple:
        """
        Assumes that there is a GeoJSON file in the file-level Zarr store.

        :param str input_zarr_bucket: Input bucket where file-level Zarr store exists.
        :param str input_zarr_path: Input bucket path where file-level Zarr store exists.
        :return: (list, list, list): Returns the latitude, longitude, and epoch seconds
        needed to properly index the data.
        """
        s3 = s3fs.S3FileSystem(
            key=os.getenv('ACCESS_KEY_ID'),  # optional parameter
            secret=os.getenv('SECRET_ACCESS_KEY'),
        )
        geo_json_s3_path = f's3://{self.__output_bucket}/{input_zarr_path}/geo.json'
        assert(s3.exists(geo_json_s3_path)), "S3 GeoJSON file does not exist."
        geo_json = geopandas.read_file(
            filename=geo_json_s3_path,
            storage_options={
                "key": os.getenv('ACCESS_KEY_ID'),  # Optional values
                "secret": os.getenv('SECRET_ACCESS_KEY'),
            },
        )
        geo_json.id = pd.to_datetime(geo_json.id)
        geo_json.id.astype('datetime64[ns]')  # TODO: be careful with conversions for pandas >=2.0.0
        epoch_seconds = (
                                pd.to_datetime(geo_json.dropna().id, unit='s', origin='unix') - pd.Timestamp('1970-01-01')
                        ) / pd.Timedelta('1s')
        epoch_seconds = epoch_seconds.tolist()
        longitude = geo_json.dropna().longitude.tolist()
        latitude = geo_json.dropna().latitude.tolist()
        #
        return latitude, longitude, epoch_seconds


    ############################################################################
    def __read_s3_geo_json(
            self,
            input_zarr_path: str,
            access_key_id: str = None,
            secret_access_key: str = None,
    ) -> str:
        # reads geojson file from s3 bucket w boto3
        # session = boto3.Session()
        # s3 = boto3.resource(
        #     service_name='s3',
        #     aws_access_key_id=access_key_id,
        #     aws_secret_access_key=secret_access_key,
        # )
        content_object = self.__s3.get_object(
            self.__output_bucket,
            input_zarr_path,
            access_key_id=access_key_id,
            secret_access_key=secret_access_key
        )
        # content_object = s3.Object(self.__output_bucket, f'{input_zarr_path}/geo.json')
        file_content = content_object.get()['Body'].read().decode('utf-8')
        json_content = json.loads(file_content)
        return json_content


    ############################################################################
    def __publish_done_message(self, message):
        print("Sending done message")
        self.__sns_operations.publish(self.__done_topic_arn, json.dumps(message))


    ############################################################################
    def execute(self, message):
        # {"shipName":"Henry_B._Bigelow","cruiseName":"HB0707","sensorName":"EK60","fileName":"D20070711-T210709.raw"}
        ship_name = message['shipName']  # 'Henry_B._Bigelow'
        cruise_name = message['cruiseName']  # 'HB0707'
        sensor_name = message['sensorName']  # 'EK60'
        input_file_name = message['fileName']  # 'D20070711-T210709.raw'
        #
        file_stem = os.path.splitext(input_file_name)[0]
        input_zarr_path = f"level_1/{ship_name}/{cruise_name}/{sensor_name}/{file_stem}.zarr"
        #
        os.chdir(TEMPDIR)
        #
        ### COPY N PASTED IN BELOW #######################################################
        # [0] get dynamoDB table info
        df = self.__get_table_as_dataframe()
        # Zarr path is derived from DynamoDB
        ### ZARR_PATH ###
        assert(input_zarr_path in list(df['ZARR_PATH'])), "The Zarr path is not found in the database."
        #
        index = df.index[df['ZARR_PATH'] == input_zarr_path][0]  # index among all cruise files
        print(index)
        #
        file_info = df.iloc[index].to_dict()
        input_zarr_bucket = file_info['ZARR_BUCKET']
        input_zarr_path = file_info['ZARR_PATH']
        output_zarr_bucket = file_info['ZARR_BUCKET']
        #
        #################################################################
        # [1] read file-level Zarr store using xarray
        file_xr = self.__get_s3_zarr_as_xr(zarr_path=input_zarr_path)
        geo_json = self.__read_s3_geo_json(
            input_zarr_path=input_zarr_path,
            access_key_id=os.getenv('ACCESS_KEY_ID'),
            secret_access_key=os.getenv('SECRET_ACCESS_KEY')
        )
        #geo_json['features'][0]
        # {'id': '2007-07-12T15:24:16.032000000', 'type': 'Feature', 'properties': {'latitude': None, 'longitude': None}, 'geometry': None}
        # reads GeoJSON with the id as the index
        geospatial = geopandas.GeoDataFrame.from_features(geo_json['features']).set_index(pd.json_normalize(geo_json["features"])["id"].values)
        geospatial_index = geospatial.dropna().index.values.astype('datetime64[ns]')
        # find the indices where 'v' can be inserted into 'a'
        indices = np.searchsorted(a=file_xr.ping_time.values, v=geospatial_index)
        #
        # TODO: only need to read the geojson file once instead of twice here...
        #
        #########################################################################
        #########################################################################
        # [2] open cruise level zarr store for writing
        # output_zarr_path: str = f'',
        print('opening cruise zarr')
        cruise_zarr = self.__s3_zarr(
            output_zarr_bucket,
            ship_name,
            cruise_name,
            sensor_name,
            # zarr_synchronizer  # TODO:
        )
        #########################################################################
        # [3] Get needed indices
        # https://github.com/oftfrfbf/watercolumn/blob/8b7ed605d22f446e1d1f3087971c31b83f1b5f4c/scripts/scan_watercolumn_bucket_by_size.py#L138
        # Offset from start index to insert new data. Note that missing values are excluded.
        ping_time_cumsum = np.insert(
            np.cumsum(df['NUM_PING_TIME_DROPNA'].to_numpy(dtype=int)),
            obj=0,
            values=0
        )
        start_ping_time_index = ping_time_cumsum[index]
        end_ping_time_index = ping_time_cumsum[index + 1]
        #
        #########################################################################
        # [4] extract gps and time coordinate from file-level Zarr store,
        # write subset of ping_time to the larger zarr store
        # reference: https://osoceanacoustics.github.io/echopype-examples/echopype_tour.html
        latitude, longitude, epoch_seconds = self.__get_spatiotemporal_indices(input_zarr_bucket, input_zarr_path)
        assert(
                len(epoch_seconds) == len(cruise_zarr.time[start_ping_time_index:end_ping_time_index])
        ), "Number of the timestamps is not equivalent to indices given."
        cruise_zarr.time[start_ping_time_index:end_ping_time_index] = epoch_seconds
        #########################################################################
        # [5] write subset of latitude/longitude
        cruise_zarr.latitude[start_ping_time_index:end_ping_time_index] = latitude
        cruise_zarr.longitude[start_ping_time_index:end_ping_time_index] = longitude
        #########################################################################
        # [6] get interpolated Sv data
        filename = os.path.basename(input_zarr_path)
        print('interpolate_data')
        print(type(df['MIN_ECHO_RANGE']))
        print(df['MIN_ECHO_RANGE'])
        print(np.float32(df['MIN_ECHO_RANGE']))
        all_Sv_prototype = self.__interpolate_data(
            minimum_resolution = np.nanmin(np.float32(df['MIN_ECHO_RANGE'])),
            maximum_cruise_depth_meters = np.nanmax(np.float32(df['MAX_ECHO_RANGE'])),
            # num_ping_time_dropna = int(df.iloc[index]['NUM_PING_TIME_DROPNA']),
            file_xr=file_xr,
            cruise_zarr=cruise_zarr,
            start_ping_time_index=start_ping_time_index,
            end_ping_time_index=end_ping_time_index,
            indices=indices,
        )  # TODO:
        cruise_zarr.sv[:, start_ping_time_index:end_ping_time_index, :] = all_Sv_prototype
        #
        #np.nanmean(cruise_zarr.sv[:, start_ping_time_index:end_ping_time_index, :])
        #
        print(cruise_zarr.sv.info)
        print('done')
        # logger.info("Finishing lambda.")
        # TODO: Work on synchronizing the data as written
        self.__publish_done_message(message)
        print(f'Done processing {input_file_name}')
