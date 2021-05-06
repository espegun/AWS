
# How to Lambda
Note - this README is about Lambdas in general. If you want to see how Lambda functions is handled for Origo Dataplatform, check the separate [repo](https://github.com/espegun/ok_dataplattform/tree/master/how_to_lambda_boilerplate) describing this.

## The purpose
AWS Lambda is useful to glue together many different AWS components. The functions automatically scale up to handle actual demand.

## How does it work?
Lambdas typically process events from some event source like S3, DynamoDB or an application.  
There are plenty of lambda blueprints (like `hello-world-python`). 
You need to create an execution role which can be used to trigger the Lambda function.  
You need to specify a handler function which will receive the `event` data as an input and will then start to process the event.
You may create a test event (JSON) in the console to test the Lambda function.  
You can monitor usage through [CloudWatch](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.html).  

*Lambda functions* are possibly assigned to *Lambda applications* and *Step Functions* (see under console).  

https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html

## Giving an execution role
A Lambda function needs to be assigned an *execution role* which enables it to use other AWS services as needed. The *role* need to have the necessary *policies* with the required *permissions*. The roles can be premade templates or custom roles, or defined as the lambda is initiated. Note that the execution is *for the lambda* to use other resources, which other permissions have to be set for other resources to access the lambda.
* [Example 1](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html). The lambda is given a *role* which has a *policy* which also has the *permissions* required for the lambda to read and write to certain S3 buckets.  
* [Example 2](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html) Creating a custom role  `lambda-s3-role` with the existing `AWSLambdaS3Policy` attached.  

*Unclear: Do we need to define a user with programmatic access? (for the execution role)*

Some managed roles typical roles used: NOT FOUND YET.   
Some managed policies typically used with Lambdas, see [this](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html#permissions-executionrole-features).  

General description for [Lambda permissions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-permissions.html).  

### Execution role: In the console
A lambda function may be given any such role.
* Default role (upload logs to CloudWatch).  
* Use a custom role created in IAM, as shown [here](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html#permissions-executionrole-console).  
* Use an AWS policy template.  
To check this for a lambda function, go to the **Lambda function**, go to **Configuration** and then choose **Permissions**.

### Execution role: Define in `serverless.yml`
...

Defined a policy `AWSLambdaS3Policy`:
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:PutLogEvents",
                "logs:CreateLogGroup",
                "logs:CreateLogStream"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::upload-data-here/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::write-logs-here/*"
        }
    ]
}
```




## Creating an handler function
The handler function can be written directly in the console or deployed in a number of ways which will be discussed further down. This section discusses only the structure of the handler function and surrounding code.  
The `event` is the actual function input, while `context` gives descriptions about the environment. Create a test case, this is normally done by specifying a dict-like object which is passed as the `event`. In the end return a dict-like object, preferably with a `statusCode` and a `body`. In some cases (when?), the value of `body` element should be converted to JSON, using `json.dumps(body)`.
```
import json

def lambda_handler(event, context):
    
    intro = f"Hello, {event['name']}!"
    
    if event["age"] > 40:
        body = f"{intro} You are really an old sod now!"
    else:
        body = f"{intro} Still young and promissing!"

    return {
        'statusCode': 200,
        'body': body
    }
```
*The example above is take from the lambda function `espen_test` in Dataplatform, dev.* 
The test event is  
```
{
  "name": "Espen",
  "age": 31
}
```









## Deployment
There are a number of ways to write and deploy a lambda function to AWS.

### Deploy: From the console
[console](https://docs.aws.amazon.com/lambda/latest/dg/getting-started-create-function.html)

### Deploy: Using the Serverless framework
This is the method used in several of the examples further up.
**TBD**

### Deploy: From a zip archive
**TBD**
https://docs.aws.amazon.com/lambda/latest/dg/python-package.html

### Deploy from container image
**TBD**
https://docs.aws.amazon.com/lambda/latest/dg/python-image.html



### Setup up hello world lambda function
[Building Lambda functions with Python](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html)
[Blank python lambda template](https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/blank-python)  
A Lambda function needs to be assigned an *execution role* which enables it to use other AWS services. Before creating the lambda function; go to IAM, create a role, add one or more *(permission) policies* like `AWSLambdaBasicExecutionRole`  and give the role a name, e.g. `lambda-role`.

Then create the lambda, in the console or otherwise, and set `existing role` to the one created above.

### Triggering a lambda function from S3
[Tutorial](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html)  


### Deploying a lambda function (old notes below)

*Not finished stuff**

However, this approach doesn't enable version control or continuous deployment. When setup up this for Origo, use the lambda_boilerplate repo. 
Initiate (or modify) `serverless.yaml` in the top directory, which configures the lambda function. Enter (or replace) the content of `service_name` to the name of the lambda function. Enter (or replace) the content of `functions` and include the `handler` function. 

To the Origo dataplatform - deploy it (to dev) using `make deploy`.

Send an S3-key as content of and `event` to the handler function, e.g. `test/espeng-testing-bucket/opening-hours/Åpningstider (eksempel).xlsx`  

```
{
  "s3_src": "test/espeng-testing-bucket/opening-hours/Åpningstider (eksempel).xlsx",
  "s3_dst": "test/espeng-testing-bucket/opening-hours/output.json",
}
```




[Deploy a Lambda function](https://medium.com/better-programming/deploy-your-first-lambda-function-4f7e54f75001)

### Deploy a ML model to a Lambda function (and expose it through an API Gateway)
As done in Weber pages 76-85. It's not CD, but useful to go through.    
Copy the ML model from `how_to_EC2`.
`cp ../how_to_EC2/ml_model/model.pkl .`
`cp ../how_to_EC2/ml_model/train_predict_iris.py .`









**TBD**  

How to trigger events from S3? --> WIP  
How to upload Lambda functions from local .py files?

**To be done! Serverless and lambdas (ref Simen prat 2020-11-02)**  
S3-path sent to function in the handler in the event.  
Example (see line 38, def copy):  
https://github.oslo.kommune.no/origo-dataplatform/s3-writer/blob/master/handlers/s3_writer.py  
Register the function using the `serverless.yml` file (replace `get_boilerplate`).  


Setting up a pipeline can be done with TerraForm - (and/or AWS Step Functions).

## Debugging
After having deployed a lambda function, you may check failure messages in StepFunctions and press failed step (if a step function sequence is established) or CloudWatch (or within Origo, use the link in `#dataplattform-alerts` after crashes).


### Getting started with lambdas
https://docs.aws.amazon.com/lambda/latest/dg/welcome.html



## Useful commands
`...`  ....  
`...`  ....  

## Useful links
[Lambdas Hello World (with further tutorials near the end)](https://aws.amazon.com/getting-started/hands-on/run-serverless-code/) **WIP**  
[Lambda triggered by upload to S3](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html)  
[Lambda developer guide with code repo](https://github.com/awsdocs/aws-lambda-developer-guide)    

[Serverless and lambdas](https://www.serverless.com/aws-lambda)  
[Spec serverless.yml for AWS](https://www.serverless.com/framework/docs/providers/aws/guide/serverless.yml/)  
[Deply Python package on AWS lambda](https://medium.com/swlh/tips-to-deploy-python-package-on-aws-lambda-fbf4bed4dc87)  
[Fredriks prezo fra JavaZone '19](https://github.com/fredriv/serverless-lambda-workshop)  
[AWS lambdas for data scientists](https://towardsdatascience.com/introduction-to-amazon-lambda-layers-and-boto3-using-python3-39bd390add17)  

