# How to DynamoDB

[AWS developer guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) This is really the go-to resource for almost everything, with basic how-to's for various languages, CLI, console, integration guidelines and best development practices.  
For info about DynamoDB with Python, see further down.

## The purpose
[Relational DBs vs NoSQL](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.WhyDynamoDB.html)  

## How does it work?
[How it works](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.html)  
[Core concepts](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html)  

* A *table* is a collection of *items*, which consists of a number of *attributes*.
* Each item has a *primary key* (one or more attributes), which distinguishes them from all other items. Except for the attributes in the primary key, the table is schemaless. 
* Attributes are normally scalars, but can also be *document types*. [Rules for naming and datatypes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html) - the most normal are *number*, *string*, *boolean*, *binary*, *null*, *lists* and *maps* (dictionaries). Keys can not be document types / nested, but must be a number, string, or binary.
* The primary keys consist of one *partition key (HASH)* (hash function input, then distributed on the drive) and possibly one *sorting key (RANGE)* (sort by this in the partition group). Read [this](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.ServiceResource.create_table) to understand how keys are defined (this example is in boto3, but the principles are general). 
* *Secondary indexes* can be created from attributes to query the items using other keys.
* A table can be associated with *DynamoDB Streams*, which then can trigger a lambda function when a table is updated.

DynamoDB is region specific. Two tables with similar names in different regions are not the same. It is however written to several locations in the region and propagation between these may take a second or so. Read operations can be *Eventually Consistent Reads* or *Strongly Consistent Reads*, which both have heir pros/cons.

Queries are much faster and should be used when you know the item keys, scan should be used otherwise. For more details, see [here](https://dynobase.dev/dynamodb-scan-vs-query/).

## boto3 (DynamoDB with Python)
See the attached example files for basic table initiatlization, adding, removing, modifying, delete and querying. It is all mostly taken for the excellent examples of [DynamoDB with Python](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html). 

Official and practical example of setting up and deploying a [DynamoDB database with boto3](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TicTacToe.html) in production.

## Useful links
[AWS: What is DynamoDB?](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)  
[Design patterns DynamoDB](https://www.youtube.com/watch?v=HaEPXoXVf2k) Se denne, visstnok veldig bra.
[Serie om data modelling i DynamoDB **IKKE LEST**](https://medium.com/expedia-group-tech/dynamodb-data-modeling-c4b02729ac08)    
