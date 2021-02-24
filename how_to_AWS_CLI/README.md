# How to AWS command line

## The purpose
Easy to move projects between different platforms.

## How does it work?
The [command structure](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-commandstructure.html) is straight forward:  
`$ aws <command> <subcommand> [options and parameters]`  

## Useful commands
`$ aws s3 ls s3://bucket_name/folder/` Read folder content.  
`$ aws s3 cp file.zip s3://bucket_name/folder/..../file.zip` Upload to S3.  
`$ aws s3 cp s3://bucket_name/.../file.zip .` Download from S3.  

## Links
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html
