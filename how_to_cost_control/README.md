# How to Cost Management, Billing and alarms

## The purpose
Monitor, raise alarms and avoid spending more than expected, especially as a result of unintended resource utilization.

*Interestingly, this folder was initiated shortly after the $812 cost occuring overnight in Feb 2021. Luckily creditted by AWS.* 

Learned: When your received a cost notification, *do not assume* it's an EC2 micro instance still running 


## How does it work?
By default, only root users have cost access.

Quoted:  
*If you use the AWS Free Tier, Billing and Cost Management automatically provides AWS Free Tier usage alerts via AWS Budgets to track your free tier usage. Billing and Cost Management notifies you when you go over the free tier limits or are forecasted to go over the free tier limits. AWS sends these notifications to the email that you used to create your AWS account.* 

## Useful commands
`...`  ....  

## Useful links
[AWS Billing and Cost Management - Getting started](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-getting-started.html)  
[Analyzing your costs with Cost Explorer](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-what-is.html)  



## Reminder

AWS Free Tier usage limit alerting via AWS Budgets 	02/24/2021

Dear AWS Customer,

Your AWS account 881179186002 has exceeded 85% of the usage limit for one or more AWS Free Tier-eligible services for the month of February.

Product 	AWS Free Tier Usage as of 02/24/2021 	Usage Limit 	AWS Free Tier Usage Limit
AWSLambda 	400000.0 seconds 	400000.0 seconds 	400,000 seconds of compute time per month for AWS Lambda
AWSLambda 	1000000.0 Requests 	1000000.0 Requests 	1,000,000 free requests per month for AWS Lambda
AmazonS3 	2000.0 Requests 	2000.0 Requests 	2,000 Put, Copy, Post or List Requests of Amazon S3

To learn more about your AWS Free Tier usage, please access the AWS Billing & Cost Management Dashboard. You can find more information on AWS Free Tier here.

This alert is provided by AWS Budgets. AWS automatically tracks your service usage and will alert you if you have reached 85% of the usage limit for one or more AWS Free Tier-eligible services. To unsubscribe from these alerts or to change the email address to which you would like your alerts to be sent, please visit the Cost Management Preferences.
