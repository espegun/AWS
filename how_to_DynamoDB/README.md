# How to DynamoDB

[AWS developer guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) This is really the go-to resource, with basic how-to's for various languages, integration guidelines and best development practices.

## The purpose
...

[Relational DBs vs NoSQL](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.WhyDynamoDB.html)  

## How does it work?

[How it works](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.html)  
* A *table* is a collection of *items*, which consists of a number of *attributes*.
* Each item has a *primary key* (one or more attributes), which distinguishes them from all other items. Except for the attributes in the primary key, the table is schemaless. 
* Attributes are normally scalars, but can also be *document types*. [Rules for naming and datatypes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html) - the most normal are *number*, *string*, *boolean*, *binary*, *null*, *lists* and *maps* (dictionaries). Keys can not be document types / nested, but must be a number, string, or binary.
* The primary keys consist of one *partition key* (hash function input, then distributed on the drive) and possibly one *sorting key* (sort by this in the partition group). 
* *Secondary indexes* can be created from attributes to query the items using other keys.
* A table can be associated with *DynamoDB Streams*, which then can trigger a lambda function when a table is updated.



DynamoDB is region specific. Two tables with similar names in different regions are not the same. It is however written to several locations in the region and propagation between these may take a second or so. Read operations can be *Eventually Consistent Reads* or *Strongly Consistent Reads*, which both have heir pros/cons.

...
**TBD: KeySchema**

Queries are much faster and should be used when you know the item keys, scan should be used otherwise. For more details, see [here](https://dynobase.dev/dynamodb-scan-vs-query/).

## boto3
See the attached example files for basic table initiatlization, adding, removing, modifying, delete and querying. It is all mostly taken for [these excellent examples](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html).  
[Conditions for query and scan](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/dynamodb.html#ref-dynamodb-conditions)  


## Useful links

[AWS: What is DynamoDB?](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)  
[Design patterns DynamoDB](https://www.youtube.com/watch?v=HaEPXoXVf2k) Se denne, visstnok veldig bra.  
