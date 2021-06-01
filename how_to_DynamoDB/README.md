# How to DynamoDB

## The purpose
...

## How does it work?
[How it works](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.html)  
[Valid DynamoDB types](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/dynamodb.html#ref-valid-dynamodb-types)  
...
**TBD: KeySchema**


Queries are preferred and should be used when you know the item keys, scan should be used otherwise. See [here](https://dynobase.dev/dynamodb-scan-vs-query/).

## boto3
See the attached example files for basic table initiatlization, adding, removing, modifying, delete and querying. It is all mostly taken for [these excellent examples](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html).  
[Conditions for query and scan](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/dynamodb.html#ref-dynamodb-conditions)  


## Useful links
[AWS: What is DynamoDB?](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)  
[Design patterns DynamoDB](https://www.youtube.com/watch?v=HaEPXoXVf2k) Se denne, visstnok veldig bra.  
