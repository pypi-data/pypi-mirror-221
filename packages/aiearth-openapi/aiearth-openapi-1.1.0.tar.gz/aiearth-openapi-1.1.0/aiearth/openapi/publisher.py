import json
import os
from abc import abstractmethod, ABC

from alibabacloud_aiearth_engine20220609.client import Client
from aiearth.openapi.models import PublishLocalTiffRequest, PublishLocalTiffResponse, PublishLocalImgRequest, \
    PublishLocalImgResponse, PublishLocalImgIgeResponse, PublishLocalImgIgeRequest, PublishLocalTiffRpcRequest, \
    PublishLocalTiffRpcResponse, PublishLocalTiffRpbRequest, PublishLocalTiffRpbResponse, PublishLocalTiffTfwRequest, \
    PublishLocalTiffTfwResponse, BasePublishLocalResponseBody, PublishLocalShapefileRequest, \
    PublishLocalShapefileResponse

from aiearth.openapi import client
from aiearth.openapi.oss import StsToken
from aiearth.openapi.enums import DataType, RasterFileType, AttachRasterFileType
from oss2 import Bucket, StsAuth
from tqdm import tqdm
from datetime import datetime
from aiearth.core import env, g_var

import logging

logger = logging.getLogger(__name__)

log_lvl = 'INFO'
if g_var.has_var(g_var.GVarKey.Log.LOG_LEVEL):
    log_lvl = g_var.get_var(g_var.GVarKey.Log.LOG_LEVEL).upper()

logging.basicConfig(level=log_lvl)

AIE_AUTH_TOKEN = "x-aie-auth-token"


class ExtClient(Client):

    def publish_local_tiff(self, request: PublishLocalTiffRequest) -> PublishLocalTiffResponse:
        tiff_publisher: TiffPublisher = TiffPublisher(request.local_file_path, request.name, request.acquisition_date)
        resp = tiff_publisher.publish()
        body = BasePublishLocalResponseBody(resp['dataId'], resp['name'])
        return PublishLocalTiffResponse({}, 200, body)

    def publish_local_img(self, request: PublishLocalImgRequest) -> PublishLocalImgResponse:
        img_publisher = ImgPublisher(request.local_file_path, request.name, request.acquisition_date)
        resp = img_publisher.publish()
        body = BasePublishLocalResponseBody(resp['dataId'], resp['name'])
        return PublishLocalImgResponse({}, 200, body)

    def publish_local_img_ige(self, request: PublishLocalImgIgeRequest) -> PublishLocalImgIgeResponse:
        img_ige_publisher = ImgIgePublisher(request.main_file_path, request.attach_file_path, request.name,
                                            request.acquisition_date)
        resp = img_ige_publisher.publish()
        body = BasePublishLocalResponseBody(resp['dataId'], resp['name'])
        return PublishLocalImgIgeResponse({}, 200, body)

    def publish_local_tiff_rpc(self, request: PublishLocalTiffRpcRequest) -> PublishLocalTiffRpcResponse:
        tiff_rpc_publisher = TiffRpcPublisher(request.main_file_path, request.attach_file_path, request.name,
                                              request.acquisition_date)
        resp = tiff_rpc_publisher.publish()
        body = BasePublishLocalResponseBody(resp['dataId'], resp['name'])
        return PublishLocalTiffRpcResponse({}, 200, body)

    def publish_local_tiff_rpb(self, request: PublishLocalTiffRpbRequest) -> PublishLocalTiffRpbResponse:
        tiff_rpb_publisher = TiffRpbPublisher(request.main_file_path, request.attach_file_path, request.name,
                                              request.acquisition_date)
        resp = tiff_rpb_publisher.publish()
        body = BasePublishLocalResponseBody(resp['dataId'], resp['name'])
        return PublishLocalTiffRpbResponse({}, 200, body)

    def publish_local_tiff_tfw(self, request: PublishLocalTiffTfwRequest) -> PublishLocalTiffTfwResponse:
        tiff_tfw_publisher = TiffTfwPublisher(request.main_file_path, request.attach_file_path, request.name,
                                              request.acquisition_date)
        resp = tiff_tfw_publisher.publish()
        body = BasePublishLocalResponseBody(resp['dataId'], resp['name'])
        return PublishLocalTiffTfwResponse({}, 200, body)

    def publish_local_shapefile(self, request: PublishLocalShapefileRequest) -> PublishLocalShapefileResponse:
        if request.name is None or len(request.name.strip()) == 0:
            raise ValueError(f"不合法的影像名称 {request.name}")

        resp = client.__get_sts_token__('zip', data_type=DataType.VECTOR)
        logger.debug(f"get_sts_token for zip get {resp}")
        sts_token = StsToken(json.loads(resp)['module'])

        auth = StsAuth(sts_token.access_key_id, sts_token.access_key_secret, sts_token.security_token)
        bucket = Bucket(auth, endpoint=sts_token.endpoint, bucket_name=sts_token.bucket)
        logger.debug(f"uploading {request.local_file_path} to {sts_token.bucket}/{sts_token.file_key}")
        with TqdmUpTo(desc=f"Uploading {request.local_file_path}") as t:
            bucket.put_object_from_file(sts_token.file_key, request.local_file_path, progress_callback=t.update_to)
            t.total = t.n

        resp = client.__publish_vector__(request.name,
                                         oss_file_key=f"oss://{sts_token.bucket}/{sts_token.file_key}")
        module = json.loads(resp)['module']
        vector_id = module[0]['vectorId']
        name = module[0]['vectorName']
        return PublishLocalShapefileResponse({}, 200, BasePublishLocalResponseBody(vector_id, name))


class TqdmUpTo(tqdm):
    """Provides `update_to(n)` which uses `tqdm.update(delta_n)`."""

    def __init__(self, desc: str = None):
        super().__init__(unit='B', unit_divisor=1024, miniters=1, unit_scale=True, desc=desc)

    def update_to(self, byte_consumed, total_bytes):
        if total_bytes is not None:
            self.total = total_bytes
        return self.update(byte_consumed - self.n)  # also sets self.n = b * bsize


class BaseDoubleFilePublisher(ABC):

    def __init__(self, main_file_path: str, attach_file_path: str,
                 name: str, acquisition_date: str = None):
        self.__main_file_path = main_file_path
        self.__attach_file_path = attach_file_path
        if name is None or len(name.strip()) == 0:
            raise ValueError(f"不合法的影像名称 {name}")
        self.__name = name
        self.__acquisition_date_dt = datetime.strptime(acquisition_date, "%Y%m%d") if acquisition_date else None

    def __get_sts_token__(self):
        resp = client.__get_sts_token__(self.__exts__()[0], data_type=DataType.RASTER)
        logger.debug(f"get_sts_token for {self.__exts__()[0]} get {resp}")
        self.__sts_token = StsToken(json.loads(resp)['module'])

        prev_file_name = os.path.basename(self.__sts_token.file_key)
        resp_ige = client.__get_sts_token__(self.__exts__()[1], data_type=DataType.RASTER,
                                            prev_file_name=prev_file_name)
        logger.debug(f"get_sts_token for {self.__exts__()[1]} with {self.__sts_token.file_key} get {resp_ige}")
        self.__sts_token_attach = StsToken(json.loads(resp_ige)['module'])

    @abstractmethod
    def __exts__(self):
        pass

    def __upload_file_to_oss__(self):
        auth = StsAuth(self.__sts_token.access_key_id, self.__sts_token.access_key_secret,
                       self.__sts_token.security_token)
        bucket = Bucket(auth, endpoint=self.__sts_token.endpoint, bucket_name=self.__sts_token.bucket)

        # upload main file
        logger.debug(f"uploading {self.__main_file_path} to {self.__sts_token.bucket}/{self.__sts_token.file_key}")
        with TqdmUpTo(desc=f"Uploading {self.__main_file_path}") as t:
            bucket.put_object_from_file(self.__sts_token.file_key, self.__main_file_path,
                                        progress_callback=t.update_to)
            t.total = t.n

        # upload attach file
        auth = StsAuth(self.__sts_token_attach.access_key_id, self.__sts_token_attach.access_key_secret,
                       self.__sts_token_attach.security_token)
        bucket = Bucket(auth, endpoint=self.__sts_token_attach.endpoint, bucket_name=self.__sts_token_attach.bucket)
        logger.debug(
            f"uploading {self.__attach_file_path} to {self.__sts_token_attach.bucket}/{self.__sts_token_attach.file_key}")
        with TqdmUpTo(desc=f"Uploading {self.__attach_file_path}") as t:
            bucket.put_object_from_file(self.__sts_token_attach.file_key, self.__attach_file_path,
                                        progress_callback=t.update_to)
            t.total = t.n

    def __publish_file(self):
        acquisition_date = int(self.__acquisition_date_dt.timestamp() * 1000) if self.__acquisition_date_dt else None
        resp = client.__publish_raster__(self.__name,
                                         file_type=self.__file_types__()[0],
                                         attach_file_type=self.__file_types__()[1],
                                         oss_file_key=f"oss://{self.__sts_token.bucket}/{self.__sts_token.file_key}",
                                         attach_oss_file_key=f'oss://{self.__sts_token_attach.bucket}/{self.__sts_token_attach.file_key}',
                                         acquisition_date=acquisition_date)
        module: dict = json.loads(resp)['module']
        return [{'dataId': a['stacId'], 'name': a['tiffName']} for a in module][0]

    @abstractmethod
    def __file_types__(self):
        pass

    def publish(self):
        self.__get_sts_token__()
        self.__upload_file_to_oss__()
        return self.__publish_file()


class TiffTfwPublisher(BaseDoubleFilePublisher):

    def __exts__(self):
        return "tif", "tfw"

    def __file_types__(self):
        return RasterFileType.TIFF, AttachRasterFileType.TFW


class TiffRpcPublisher(BaseDoubleFilePublisher):
    def __exts__(self):
        return "tif", "_rpc.txt"

    def __file_types__(self):
        return RasterFileType.TIFF, AttachRasterFileType.RPC


class TiffRpbPublisher(BaseDoubleFilePublisher):
    def __exts__(self):
        return 'tif', 'rpb'

    def __file_types__(self):
        return RasterFileType.TIFF, AttachRasterFileType.RPB


class ImgIgePublisher(BaseDoubleFilePublisher):

    def __exts__(self):
        return 'img', 'ige'

    def __file_types__(self):
        return RasterFileType.IMG, AttachRasterFileType.IGE


class BaseSingleFilePublisher(ABC):

    def __init__(self,
                 local_file_path: str,
                 name: str,
                 acquisition_date: str = None):
        """
        EN: publish local file to AI Earth;
        1. upload local file to oss
        2. publish this file
        :param local_file_path: accepts tif / img file 接收 tif / img 影像
        :param name: the published resource name 发布的影像资源的名称
        :param acquisition_date: the date (in %y%m%d format) this image acquired 该影响的获取时间
        """
        self.__local_file_path__ = local_file_path
        if name is None or len(name.strip()) == 0:
            raise ValueError(f"不合法的影像名称 {name}")
        self.__raster_name__ = name

        # parse acquisition date
        self.__acquisition_date_dt = datetime.strptime(acquisition_date, '%Y%m%d') if acquisition_date else None

    def __get_sts_token__(self):
        resp = client.__get_sts_token__(self.__file_ext__(), data_type=DataType.RASTER)
        logger.debug(f"get_sts_token: {resp}")
        self.__sts_token = StsToken(json.loads(resp)['module'])

    def __upload_file_to_oss__(self):
        auth = StsAuth(self.__sts_token.access_key_id, self.__sts_token.access_key_secret,
                       self.__sts_token.security_token)
        bucket = Bucket(auth, endpoint=self.__sts_token.endpoint, bucket_name=self.__sts_token.bucket)

        logger.debug(f"uploading {self.__local_file_path__} to {self.__sts_token.bucket}/{self.__sts_token.file_key}")

        with TqdmUpTo(desc=f"Uploading {self.__local_file_path__}") as t:
            bucket.put_object_from_file(self.__sts_token.file_key, self.__local_file_path__,
                                        progress_callback=t.update_to)
            t.total = t.n

    def __publish_file(self):
        acquisition_date = int(self.__acquisition_date_dt.timestamp() * 1000) if self.__acquisition_date_dt else None
        resp = client.__publish_raster__(self.__raster_name__, file_type=self.__file_type__(),
                                         oss_file_key=f"oss://{self.__sts_token.bucket}/{self.__sts_token.file_key}",
                                         acquisition_date=acquisition_date)
        module: dict = json.loads(resp)['module']
        return [{'dataId': a['stacId'], 'name': a['tiffName']} for a in module][0]

    def publish(self):
        self.__get_sts_token__()
        self.__upload_file_to_oss__()
        return self.__publish_file()

    @abstractmethod
    def __file_ext__(self):
        pass

    @abstractmethod
    def __file_type__(self):
        pass


class ImgPublisher(BaseSingleFilePublisher):

    def __file_ext__(self):
        return "img"

    def __file_type__(self):
        return RasterFileType.IMG


class TiffPublisher(BaseSingleFilePublisher):

    def __file_ext__(self):
        return "tif"

    def __file_type__(self):
        return RasterFileType.TIFF
