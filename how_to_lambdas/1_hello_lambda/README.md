## serverless.yml
See the content of `serverless.yml` to understand how the function is defined and how it refers to the handler function in `handler.py`.
The lambda function does not need a role, since it does not use other AWS resources.

## Deploy to AWS
To deploy a lambda function to an AWS account, you need to do this with a user which have the sufficient permissions and programmatic access (valid `aws_access_key_id` and `aws_secret_access_key` specified in `~/.aws/credentials` and `~/.aws/config`), in addition to matching `AWS_PROFILE` environment variable (could be `default`).  

`$ sls deploy` Must be run in the same directory as `serverless.yml`.  

## Test
Now use the AWS console that it or has been updated or simply invoke the function from the command line.  
`$ sls invoke -f my-function` Run the function deployed. 

https://www.serverless.com/framework/docs/providers/aws/examples/hello-world/python/




