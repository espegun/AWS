# How to EC2

## The purpose
Like most cloud services, it's easy to get the power and scalability you need, and you pay for what you use.

## How does it work?
You need to generate and use a [key pair](https://eu-west-1.console.aws.amazon.com/ec2/v2/home?region=eu-west-1#KeyPairs:) to log in to your instance securely. First generate a private key, save it a safe place and `chmod 400 file.pem` so only you can read it.<br/>
Create a security group - with rules for inbound HTTP, HTTPS and SSH (your IP only), Jupyter (8888, custom TCP).<br/>
Launch an instance and add the security group and key pair already initiated.<br/>
ssh to the instance, refering to the locally stored key.
You may also SCP files there.

## Useful commands
`ssh -i ~/Desktop/Main/keys/EC2_test_instance.pem ec2-user@ec2-54-217-32-187.eu-west-1.compute.amazonaws.com` SSH to the instance. `ec2-user` is the default user @ the *Public IPv4 DNS*.<br/>



## Useful links
[Do this first: Set up for EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.html)<br/>
[Then: Tutorial EC2 setup](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)<br/>



