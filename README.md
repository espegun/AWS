# AWS
[Private AWS login](https://espenpersonal.signin.aws.amazon.com/console), account 881179186002 / EspenPersonal, root login = espen.gunnarsen@gmail.com. TFA.  
[Origo AWS login](https://login.oslo.kommune.no/auth/realms/AD/protocol/saml/clients/amazon-aws)  

Remember that you have the moderately clever scripts to switch between accounts. These move `credentials` and `config` and updates  the `AWS_PROFILE` environment variable.   
`$ source ~/aws_config/origo_aws.sh`  
`$ source ~/aws_config/priv_aws.sh`  

Normally, you can log in to the `EspenPersonal` account with the `espen_daily` user.

## AWS Ramp up guides - by roles and topics
https://aws.amazon.com/training/ramp-up-guides/


## General
[ARNs](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) (Amazon Resource names) are resource identiers which are unique across all of  AWS, e.g. for users or policies. An example is `arn:aws:iam::881179186002:user/test_user` (the twelve digits are the account id).  

TBD i egen katalog: [Dynamo DB](https://link.medium.com/TmLpxi2h2cb) + [Docs og tutorial](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html)   
TBD i egen katalog: CloudFormation (equivalent with TerraForm, used with `sls deploy`)
Ikke AWS spesifikk, men les [Fundamentals of data architecture for data scientists](https://towardsdatascience.com/fundamentals-of-data-architecture-to-help-data-scientists-understand-architectural-diagrams-better-7bd26de41c66).  

## Debugging tips
* Minimize online debugging: Add plenty of tests, including for the handler.
* Look at the log from the failing process in **Step Functions** in the console.
* Remember that data may be available **DynamoDB**.
* 

## TBD!
* PostgresDB in AWS
* [SNS + SQS](https://medium.com/awesome-cloud/aws-difference-between-sqs-and-sns-61a397bf76c5#:~:text=SQS%20is%20mainly%20used%20to,application%20to%20several%20storage%20systems.) (including in lambda functions, Fredriks workshop)

## Nyttige lenker
* [AWS and Azure - Equivalent services](https://docs.microsoft.com/en-us/azure/architecture/aws-professional/services)  
