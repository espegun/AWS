# AWS
[Private AWS login](https://espenpersonal.signin.aws.amazon.com/console)
[Origo AWS login](https://login.oslo.kommune.no/auth/realms/AD/protocol/saml/clients/amazon-aws)  




  
Ikke AWS spesifikk, men les [Fundamentals of data architecture for data scientists](https://towardsdatascience.com/fundamentals-of-data-architecture-to-help-data-scientists-understand-architectural-diagrams-better-7bd26de41c66)  

## Identitiy and Access Management (IAM)
- [Accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html): An account has a 12-digit ID and is also associated with a mail-adress and *root* user.
- [Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html): All accounts have a *root* user which have full access and should purely be used for administrative purposes. Normally, you should use *IAM users*, which represents a person or service which needs to interact with AWS, either by logging into the console or to make programmatic requests. A user has a name, a sign-in password and up to two keys that can be used to make programmatic requests. 
- [Groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html): A group has certain permission *policies* attached and has *IAM users* as members.
- Policies: A *policy* givens certain permissions, like access to a S3-bucket or to invoke a lambda function. The policy will normally be attached to a *group* or directly to a *user*.
- [Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html): Like an *user*, a *role* is an AWS identity with associated *policies* which determine what the identitiy can and can not do in AWS. However, a *role* doesn't have passwords or access keys, but can be assumed by anyone who needs it and give temporary security credentials for the role session (the normal permissions are not active during the session).  Roles can be assumed by IAM users in the same or a different AWS-*account*, or provided external users with some autentication method. Permissions to use the *role* is given in the *trust policy* from a *trusting account* to members of a *trusted account* which can assume the role. 

### A couple of examples
**TBD** Legg til et par konkrete eksempler etterhvert som du gjør de. F.eks. for Lambda funksjon som kjører mot S3.

## Useful links
[Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html)  
