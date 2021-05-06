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


## Setup (outside the AWS-environment)
In the AWS console, go to IAM and create a user with *Programmatic access*, use the *AdministratorAccess* existing policy for full development, use *least privilige* rights for normal service users. You now have the `Access key ID`(user id) and the `Secret access key`(password) associated with one specific role with certain priviliges.  
Install boto3 according to the instructions at the [repo](https://github.com/boto/boto3).  
Setup credentials for the user with programmatic access in `~/.aws/credentials` og `~/.aws/config` as described [here](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration), i.e. by using `aws configure` or manually modifying the files.
The files may contain several entries for different profile names, which is given in the brackets, like `[my_profile_name]`. The environment variable `AWS_PROFILE` is read, trying to find a matching name and if no match, uses the `[default]` specification.


~/.aws/credentiasls :
```
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```
~/.aws/config:
```
[default]
region=eu-west-1
```
With these keys in place in the environment which is connecting to AWS using `boto3`, no further login should be required and the connecting entity has a defined role.  
[saml2aws](https://github.com/Versent/saml2aws) is useful when you have several accounts, several clients or need time limited login sessions.  

## Useful links
[boto3 at readthedocs](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)  
[AWS at RealPython](https://realpython.com/lessons/python-boto3-aws-s3-overview/)  
[Resource, client and session](https://stackoverflow.com/questions/42809096/difference-in-boto3-between-resource-client-and-session) <-- TBD!  
