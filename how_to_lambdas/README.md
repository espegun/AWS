
# How to Lambda (and Serverless?)
Note - this README is about Lambdas in general. If you want to see how Lambda functions is handled for Origo Dataplatform, check the separate [repo](https://github.com/espegun/ok_dataplattform/tree/master/how_to_lambda_boilerplate) describing this.

## The purpose
AWS Lambda is useful to glue together many different AWS components. The functions automatically scale up to handle actual demand.

## How does it work?
Lambdas typically process events from some event source like S3, DynamoDB or an application. 
There are plenty of lambda blueprints (like `hello-world-python`)
You need to create an execution role which can be used to trigger the Lambda function.
You need to specify a handler function or method which will receive the event data as an input and will then start to process the event.
You may create a test event (JSON) to test the Lambda function.
You can monitor usage through [CloudWatch](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.html)

*Lambdas (may) belong to application.*

### Setup up simple function
You may create a function and a test event using the AWS Console.  
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


## Useful commands
`...`  ....  
`...`  ....  

## Useful links
[Lambdas Hello World (with further tutorials near the end)](https://aws.amazon.com/getting-started/hands-on/run-serverless-code/) **WIP**  
[Serverless and lambdas](https://www.serverless.com/aws-lambda)  
[Fredriks prezo fra JavaZone '19](https://github.com/fredriv/serverless-lambda-workshop)  
[AWS lambdas for data scientists](https://towardsdatascience.com/introduction-to-amazon-lambda-layers-and-boto3-using-python3-39bd390add17)  

