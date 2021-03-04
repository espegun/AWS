import json
import time

import boto3

# https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html
# Also see this example, where the lambda is given a role which has a policy which
# also has the permissions required for the lambda to read and write to certain S3 buckets.


def react_to_file_event(event, context):

    BUCKET = "aws-basics"

    print("Running reach_to_file_event.")

    s3 = boto3.resource("s3", region_name="eu-west-1")
    obj = s3.Object(BUCKET, "dump.txt")
    obj.put(Body=f"File object created at {time.time()}", ContentType="text/csv")

    # response = "Great success!"

    # return {"statusCode": 200,
    #         "headers": {"Content-type": "application/json"},
    #         "body": json.dumps(response)
    #          }
