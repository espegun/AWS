
# How to Lambda (and Serverless?)

**To be done! Serverless and lambdas (ref Simen prat 2020-11-02)**  
S3-path sent to function in the handler in the event.  
Example (see line 38, def copy):  
https://github.oslo.kommune.no/origo-dataplatform/s3-writer/blob/master/handlers/s3_writer.py  
Register the function using the `serverless.yml` file (replace `get_boilerplate`).  

## The purpose
...  

## How does it work?
Lambdas typically process events from some event source like S3, DynamoDB or an application.
There are plenty of lambda blueprints (like `hello-world-python`)
You need to create an execution role which can be used to trigger the Lambda function.
You need to specify a handler function or method which will receive the event data as an input and will then start to process the event.
You may create a test event (JSON) to test the Lambda function.
You can monitor usage through [CloudWatch](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.html)

TBD  
**How to trigger events from S3?** --> WIP  
**How to upload Lambda functions from local .py files?**


## Useful commands
`...`  ....  
`...`  ....  

## Useful links
[Lambdas Hello World (with further tutorials near the end)](https://aws.amazon.com/getting-started/hands-on/run-serverless-code/) **WIP**  
[Serverless and lambdas](https://www.serverless.com/aws-lambda)  
[Fredriks prezo fra JavaZone '19](https://github.com/fredriv/serverless-lambda-workshop)  
[AWS lambdas for data scientists](https://towardsdatascience.com/introduction-to-amazon-lambda-layers-and-boto3-using-python3-39bd390add17)  

