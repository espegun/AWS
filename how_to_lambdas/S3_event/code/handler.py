import json
import time

import boto3


def read_and_write_filesize(event, context):

    BUCKET = "aws-basics"

    s3 = boto3.resource("s3", region_name="eu-west-1")
    obj = s3.Object(BUCKET, "dump.txt")
    obj.put(Body=f"File object created at {time.time()}", ContentType="text/csv")

    # response = "Great success!"

    # return {"statusCode": 200,
    #         "headers": {"Content-type": "application/json"},
    #         "body": json.dumps(response)
    #          }
