# How to boto3

## The purpose
Connect to AWS-service using Python.

## How does it work?
...

## Setup
In the AWS console, go to IAM and create a user with *Programmatic access* and possible the *AdministratorAccess* existing policy. You now have the `Access key ID`(user id) and the `Secret access key`(password). 
Install boto3 according to the instructions at the [repo](https://github.com/boto/boto3). 
Setup credentials for the user with programmatic access in `~/.aws/credentials` og `~/.aws/config`.

## Useful commands
Read a text file from S3 (to memory)
```
S3_key = "something/something/log.txt"
bucket_name = "my_bucket_name"
s3 = boto3.resource('s3')
obj = s3.Object(bucket_name, S3_key)
filecontent = obj.get()['Body'].read().decode('utf-8')
````


**WIP below here**
`resource` is more high-level than `client`, use the former if possible.


RW S3
`s3 = boto3.resource("s3", region_name="eu-west-1")` Open a connection to S3  
`obj = s3.Object(bucket_name, key)`  Initiate a file object  
`obj.put(Body=content, ContentType='text/csv')` Populate the file object with a normal string 
`body = obj.get()["Body"].read()` Read binary string, alternatively add `.decode("utf-8")`  
```
with open("local_file.txt", "rw") as f:
    # .put with Body=f
```

Read S3 to memory (binary object):
```
with io.BytesIO(s3_res.Object(bu_name, key).get()["Body"].read()) as f:
    f.seek(0) # Rewind; arr = np.load(f, allow_pickle=True) # np-arrays
```

Write local binary file to S3:
```
with open("model.tar.gz", "rb") as data:
    s3.Bucket(BUCKET_NAME).put_object(Key=DST_KEY, Body=data)
```

Write a binary object (like an np-array) from memory to S3 (REWRITE):
```
s3_client = boto3.client("s3", region_name=region_name)
f = io.BytesIO()
pickle.dump(obj, f)
f.seek(0)
s3_client.upload_fileobj(f, bucket_name, new_dst_key)
```

Prøv dette:
```
bucket = boto3.resource("s3").Bucket(bucket)
objects = bucket.objects.filter(Prefix=prefix)
keys = [obj.key for obj in objects if obj.key.endswith(".json")]
```

## Useful links
[AWS at RealPython](https://realpython.com/lessons/python-boto3-aws-s3-overview/)
[Resource, client and session](https://stackoverflow.com/questions/42809096/difference-in-boto3-between-resource-client-and-session) <-- TBD!  
