# How to Cost Management, Billing and alarms

## The purpose
Monitor, raise alarms and avoid spending more than expected, especially as a result of unintended resource utilization.

*Interestingly, this folder was initiated shortly after the $812 cost occuring overnight in Feb 2021. Luckily creditted by AWS.* 

Learned: When your received a cost notification, *do not assume* it's an EC2 micro instance still running. But also - these alert does not happen in real time. Check usage stats after setting up a lambda or similar jobs.


## How does it work?
By default, only root users have cost access.

Quoted:  
*If you use the AWS Free Tier, Billing and Cost Management automatically provides AWS Free Tier usage alerts via AWS Budgets to track your free tier usage. Billing and Cost Management notifies you when you go over the free tier limits or are forecasted to go over the free tier limits. AWS sends these notifications to the email that you used to create your AWS account.* 

https://aws.amazon.com/support



WIP Creating alarms for anomaly detection, **Cloudwatch**.
Set alarms for usage of buckets and invocations of lambdas over a certain period.


## Useful commands
`...`  ....  

## Useful links
[AWS Billing and Cost Management - Getting started](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-getting-started.html)  
[Analyzing your costs with Cost Explorer](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-what-is.html)  
