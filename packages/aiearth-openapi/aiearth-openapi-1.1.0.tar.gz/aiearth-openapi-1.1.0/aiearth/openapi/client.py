import os
from urllib import parse

from aiearth.core.client import Endpoints
from aiearth.core.client.client import BaseClient

from aiearth import core
from aiearth.openapi.enums import DataType
from aiearth.openapi.enums import RasterFileType


def __get_host__() -> str:
    host = Endpoints.HOST
    data_host = os.getenv("DATA_CLIENT_HOST")
    return data_host if (data_host is not None and len(data_host) > 0) else host


def __get_sts_token__(file_ext: str, data_type: DataType, prev_file_name: str = None):
    url = __get_host__() + f"/mariana/openapi/oss/getStsToken?client=aiearthopenapi&data_type={data_type.name}&file_ext={file_ext}"
    if prev_file_name:
        url = url + f"&prev_file_name={parse.quote(prev_file_name)}"
    resp = BaseClient.get(url, {})
    return resp.content.decode(encoding='utf-8')


def __publish_vector__(name: str,
                       oss_file_key: str):
    url = f'{__get_host__()}/mariana/openapi/shape/v2/batchPublish?client=aiearthopenapi'
    resp = BaseClient.post(url, {}, data=[{
        'name': name,
        'fileUrl': oss_file_key
    }])
    return resp.content.decode(encoding='utf-8')


def __publish_raster__(name: str,
                       file_type: RasterFileType,
                       attach_file_type: RasterFileType = None,
                       oss_file_key: str = None,
                       attach_oss_file_key: str = None,
                       acquisition_date: int = None,
                       download_url: str = None,
                       attach_download_url: str = None):
    url = __get_host__() + "/mariana/openapi/tiff/v2/batchPublish?client=aiearthopenapi"
    resp = BaseClient.post(url, {}, data=[{
        "file_type": file_type.value,
        "attach_file_type": attach_file_type.value if attach_file_type else None,
        "tiff_date": acquisition_date,
        "name": name,
        "file_url": oss_file_key,
        "attach_file_url": attach_oss_file_key,
        "download_url": download_url,
        "attach_download_url": attach_download_url
    }])
    return resp.content.decode(encoding="utf-8")


def __get_token__() -> str:
    return core.g_var.get_var(core.g_var.GVarKey.Authenticate.TOKEN) or None
