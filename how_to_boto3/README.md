# How to boto3

## 
Note that this repo covers the stuff which is generic for boto3. For code which is specific to special technogies, check those repos.  
[boto3 with EC2](https://github.com/espegun/AWS/blob/main/how_to_EC2/README.md#boto3)  
boto3 with Lambda  
[boto3 with S3](https://github.com/espegun/AWS/tree/main/how_to_S3#boto3)  
[boto3 with DynamoDB](https://github.com/espegun/AWS/tree/main/how_to_DynamoDB#boto3)    

## The purpose
Connect to AWS-service using Python.

## How does it work?
...

`resource` is more high-level than `client`, use the former if possible.


## Setup
In the AWS console, go to IAM and create a user with *Programmatic access*, use the *AdministratorAccess* existing policy for full development, use *least privilige* rights for normal service users. You now have the `Access key ID`(user id) and the `Secret access key`(password).  
Install boto3 according to the instructions at the [repo](https://github.com/boto/boto3).  
Setup credentials for the user with programmatic access in `~/.aws/credentials` og `~/.aws/config`. **HOW**. 

## Useful links
[boto3 at readthedocs](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)  
[AWS at RealPython](https://realpython.com/lessons/python-boto3-aws-s3-overview/)  
[Resource, client and session](https://stackoverflow.com/questions/42809096/difference-in-boto3-between-resource-client-and-session) <-- TBD!  
