# AWS
[Private AWS login](https://espenpersonal.signin.aws.amazon.com/console), account 881179186002, root login = espen.gunnarsen@gmail.com. TFA.  
[Origo AWS login](https://login.oslo.kommune.no/auth/realms/AD/protocol/saml/clients/amazon-aws)  

Remember that you have the moderately clever scripts to switch between accounts.  
`$ ~/aws_config/origo_aws.sh`  
`$ ~/aws_config/priv_aws.sh`  

## General
[ARNs](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) (Amazon Resource names) are resource identiers which are unique across all of  AWS, e.g. for users or policies. An example is `arn:aws:iam::881179186002:user/test_user` (the twelve digits are the account id).  

TBD i egen katalog: [Dynamo DB](https://link.medium.com/TmLpxi2h2cb) + [Docs og tutorial](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html)   

Ikke AWS spesifikk, men les [Fundamentals of data architecture for data scientists](https://towardsdatascience.com/fundamentals-of-data-architecture-to-help-data-scientists-understand-architectural-diagrams-better-7bd26de41c66).  


