# How to Identitiy and Access Management (IAM)

## The purpose
...

## How does it work?
- [Accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html): An account has a 12-digit ID and is also associated with a mail-adress and *root* user.
- [Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html): All accounts have a *root* user which have full access and should purely be used for administrative purposes. Normally, you should use *IAM users*, which represents a person or service which needs to interact with AWS, having the right to log into the console (requiring password) and/or to make programmatic requests (requiring a generated key). 
- Permissions: Grants access to actions and resources in AWS. E.g. one permission may be `{"Service": "S3", "Access level": "Full access", "Resource": "All resources"}`. Each such permission may also come with more detailed constraints like a specified list of buckets.
- Policies: A *policy* consists one or more *permissions*. Policies can be pre-built or custom built from available services/resources. E.g. the pre-built `AmazonS3FullAccess` policy gives the entity which has it the permissions to access S3. A policy can be assigned to a *user*, *group* or *role*.
- [Groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html): A group has certain permission *policies* attached. *IAM users* may be attached as members of the group and will be given the *permission policies* as defined for the *group* (in addition to the *user's* own *permission policies*).
- [Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html): Like an *user*, a *role* is an AWS identity which har certain *policies*. A *role* does not have passwords or access keys, but can be temporarily given to someone who needs it for a session (the user's normal permissions are not active during the session). Roles can be assumed by IAM users in the same or a different AWS-account, or provided external users with some autentication method. Permissions to use the *role* is given in the *trust policy* from a *trusting account* to members of a *trusted account* which can assume the role. **TBD Example** 

**TBD** Legg til et par konkrete eksempler etterhvert som du gjør de. F.eks. for Lambda funksjon som kjører mot S3.

## Useful commands
`...`  ....  
`...`  ....  

## Useful links
[Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html)  



