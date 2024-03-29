# How to Identitiy and Access Management (IAM)

## The purpose
Any entity which should use any AWS resource, needs to have a authenticated *user* with assigned *permissions*.

*Authentication* identifies who you are, typically by using login credentials and MFA.
*Authorization* handles the policies assigned to an idenity.  

## How does it work?
- [Accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html): An account has a 12-digit ID and is also associated with a mail-adress and *root* user.
- [Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html): All accounts have a *root* user which have full access and should purely be used for administrative purposes. Normally, you should use *IAM users*, which represents a person or service which needs to interact with AWS, having the right to log into the console (requiring password) and/or to make programmatic requests from outside AWS (requiring a generated key, can be regenerated if lost). 
- Permissions: Grants access to actions and resources in AWS. E.g. one permission may be `{"Service": "S3", "Access level": "Full access", "Resource": "All resources"}`. Each such permission may also come with more detailed constraints like a specified list of buckets.
- Policies: A *policy* consists one or more *permissions*. Policies can be pre-built or custom built from available services/resources. E.g. the pre-built `AmazonS3FullAccess` policy gives the entity which has it the permissions to access S3. A policy can be assigned to a *user*, *group* or *role*.  *Example: A Lambda function should be given the 
- [Groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html): A group has certain permission *policies* attached. *IAM users* may be attached as members of the group and will be given the *permission policies* as defined for the *group* (in addition to the *user's* own *permission policies*).
- [Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html): Like an *user*, a *role* is an AWS identity which har certain *policies*. A *role* does not have passwords or access keys, but can be temporarily given to someone who needs it for a session (the user's normal permissions are not active during the session). Roles can be assumed by IAM users in the same or a different AWS-account, or provided external users with some autentication method. Permissions to use the *role* is given in the *trust policy* from a *trusting account* to members of a *trusted account* which can assume the role. **TBD Example** 

Some examples:  
- A lambda function needs to be given a *role* which has the `AWSLambdaBasicExecutionRole` *policy* which has the *permissions* that the function needs to write logs to CloudWatch Logs.  Also see [this example](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html), where the lambda is given a *role* which has a *policy* which also has the *permissions* required for the lambda to read and write to certain S3 buckets.
- ...

To login using programmatic access, see the instructions in [how_to_boto3](../how_to_boto3/README.md)

## Useful commands
`...`  ....  
`...`  ....  

## Useful links
[Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
