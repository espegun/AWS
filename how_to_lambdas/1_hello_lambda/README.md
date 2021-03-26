This 

## Deploy to AWS
To be deploy a function to an AWS account, you need to be set up with valid data in `~/.aws/credentials` and `~/.aws/config`, in addition to matching `AWS_PROFILE` environment variable (could be `default`).  
`$ sls deploy` Must be run in the same directory as `serverless.yml`.  

## Test
Now use the AWS console that it or has been updated or simply invoke the function from the command line.  
`$ sls invoke -f my-function` Run the function deployed. 

https://www.serverless.com/framework/docs/providers/aws/examples/hello-world/python/




