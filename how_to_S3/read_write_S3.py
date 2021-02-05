"""
Assuming the programmatic_access user credentials are used,
for the personal AWS account.
"""

import boto3

BUCKET_NAME = "boto3-practice"

s3 = boto3.resource("s3", region_name="eu-west-1")

#FILENAME = "text.txt"


print("Jalla")


