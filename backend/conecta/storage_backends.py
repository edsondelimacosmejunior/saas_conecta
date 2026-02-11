from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = "static"
    default_acl = "public-read"


class PublicMediaStorage(S3Boto3Storage):
    location = "media"
    file_overwrite = False


class TemporaryMediaStorage(S3Boto3Storage):
    location = "tmp"
    file_overwrite = (
        False  # Para evitar que arquivos com o mesmo nome sejam sobrescritos
    )
