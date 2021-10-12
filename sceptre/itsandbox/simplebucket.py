from troposphere import Output, Ref, Template
from troposphere.s3 import Bucket, PublicRead

def bucket(sceptre_user_data):
    template = Template()
    template.add_resource(
        Bucket(
            "S3Bucket",
            AccessControl=PublicRead,
        )
    )
    return template.to_yaml()

def sceptre_handler(sceptre_user_data):
    return bucket(sceptre_user_data)