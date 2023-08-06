# s3fs_operations.py
import os
import s3fs


class S3FSOperations:
    #####################################################################
    def __get_s3_fs(
            self,
            access_key_id=None,
            secret_access_key=None
    ):
        if access_key_id:
            s3_fs = s3fs.S3FileSystem(
                key=access_key_id,
                secret=secret_access_key
            )
            print('NODD Authenticated w passed credentials')
        else:
            s3_fs = s3fs.S3FileSystem()
            print('NODD Authenticated wo passed credentials')
        return s3_fs

    #####################################################################
    def s3_map(
            self,
            s3_zarr_store_path,
            access_key_id=None,
            secret_access_key=None,
    ):
        s3_fs = self.__get_s3_fs(
            access_key_id=access_key_id,
            secret_access_key=secret_access_key
        )
        return s3fs.s3Map(root=s3_zarr_store_path, s3=s3_fs, check=True)

    #####################################################################
