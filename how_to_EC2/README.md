# How to <something>

## The purpose
...Easy to move projects between different platforms.

## How does it work?
You need to generate and use a [key pair](https://eu-west-1.console.aws.amazon.com/ec2/v2/home?region=eu-west-1#KeyPairs:) to log in to your instance securely. First generate a private key, save it a safe place and `chmod 400 file.pem` so only you can read it.<br/>
Create a security group - with rules for inbound HTTP, HTTPS and SSH (your IP only).<br/>
Launch an instance and add the security group and key pair already initiated.<br/>

## Useful commands
`$ ...` Some comment<br/>

## Useful links
[Do this first: Set up for EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.html)<br/>
[Then: Tutorial EC2 setup](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)<br/>



