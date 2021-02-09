# How to EC2

## The purpose
Like most cloud services, it's easy to get the power and scalability you need, and you pay for what you use.
Use it to host a website, an API or train models.

## How does it work?
The [instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) defines the hardware used for the instance. The [AMI (Amazon Machine Image)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html) defines the OS and software.

You need to generate and use a [key pair](https://eu-west-1.console.aws.amazon.com/ec2/v2/home?region=eu-west-1#KeyPairs:) to log in to your instance securely. First generate a private key, save it a safe place and `chmod 400 file.pem` so only you can read it.<br/>
Create a security group - with rules for inbound HTTP, HTTPS and SSH (your IP only), Jupyter (8888, custom TCP).<br/>
Launch an instance and add the key pair and security group (may be modified) already initiated.<br/>
`ssh` to the instance, refering to the locally stored key.

## Useful commands

### SSH to the instance
`ssh -i /folder/EC2_test_instance.pem ec2-user@54.123.123.123` SSH to the instance. `ec2-user` is the default user @ the *Public IPv4*.<br/>

### File transfer using SCP
`scp -i /folder/EC2_test_instance.pem testing.py ec2-user@54.123.123.123:~/upload_dir/` How to upload something to the instance.<br/>
`scp -i /folder/EC2_test_instance.pem ec2-user@54.216.85.67:~/source_dir/* .` How to download something from the instance.<br/>

### Setup various stuff on the instance
To update Python, install Jupyter, see Weber p11-12.<br/>
`jupyter notebook --ip <private IPv4>`   Set the instance running, it will return a token. Replace the private with public IP and paste in the browser (port 8888 must be open for inbound traffic).<br/>
To set up a Flask API, simply run the `flaski_api.py`file (port 5000 must be open for inbound traffic).<br/>

## Boto3
[Boto3 EC2 docs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html)  
[Examples](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-examples.html)  

`client = boto3.client("ec2")`

Launch an instance. Find or generate a suitable AMI (`ImageId`) in the console.  
`resp = client.run_instances(ImageId="ami-0bb3fad3c0286ebd5", InstanceType="t2.micro", MinCount=1, MaxCount=1)`

Useful functions for the instances. Check documentation [here](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#client).
```
client.start_instances(InstanceIds=list_of_id)
resp = client.describe_instances(InstanceIds=list_of_id)
client.stop_instances(InstanceIds=list_of_id)
client.terminate_instances(InstanceIds=list_of_id)
```

## Useful links
[First: Set up key pair and possibly create a security group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.html)<br/>
[Then: Set up and connect to an EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)<br/>



