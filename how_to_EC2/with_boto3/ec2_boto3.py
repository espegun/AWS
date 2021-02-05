# boto3.readthedocs.io
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-examples.html
import time

import boto3


def launch_ec2_instance(client):

    # Launch an instance
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html  # EC2.Client.run_instances
    # ImageId needs to be fetched from the console. E.g. from previously created instances.
    resp = client.run_instances(ImageId="ami-0bb3fad3c0286ebd5",
                                InstanceType="t2.micro",
                                MinCount=1,
                                MaxCount=1)

    for instance in resp["Instances"]:
        print(f"InstanceId: {instance['InstanceId']}")
        return instance["InstanceId"]  # Only one instanciated anyway


client = boto3.client("ec2")

print("Initiating EC2 instance.")
id = launch_ec2_instance(client)
list_of_id = [id]

print("Starting instances")
time.sleep(5)
client.start_instances(InstanceIds=list_of_id)

print("Stopping instances")
time.sleep(60)  # Of course better to do this when confirmed running
client.stop_instances(InstanceIds=list_of_id)

print("Terminating instances")
time.sleep(60)  # Of course better to do this when confirmed stopped
resp = client.terminate_instances(InstanceIds=list_of_id)
for instance in resp["TerminatingInstances"]:
    print(instance["InstanceId"])

print("Husk å slette instanser! $$$$$$$$")
