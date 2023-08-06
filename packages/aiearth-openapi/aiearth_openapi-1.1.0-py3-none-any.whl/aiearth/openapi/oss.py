class StsToken(object):

    def __init__(self, json_object: dict):

        self.access_key_id = json_object['accessKeyId']
        self.access_key_secret = json_object['accessKeySecret']
        self.bucket = json_object['bucket']
        self.expiration = json_object['expiration']
        self.file_key = json_object['fileKey']
        self.file_name = json_object['fileName']
        self.region = json_object['region']
        self.security_token = json_object['securityToken']
        self.endpoint = json_object['endpoint']
