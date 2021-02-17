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


ec2_client = boto3.client("ec2")

if True:

    print("Initiating EC2 instance.")
    id = launch_ec2_instance(ec2_client)
    list_of_id = [id]

    print("Starting instances")
    time.sleep(5)
    ec2_client.start_instances(InstanceIds=list_of_id)

    print("Stopping instances")
    time.sleep(60)  # Of course better to do this when confirmed running
    ec2_client.stop_instances(InstanceIds=list_of_id)

    print("Terminating instances")
    time.sleep(60)  # Of course better to do this when confirmed stopped
    resp = ec2_client.terminate_instances(InstanceIds=list_of_id)
    for instance in resp["TerminatingInstances"]:
        print(instance["InstanceId"])

    print("Describing instances")
    resp = ec2_client.describe_instances(InstanceIds=list_of_id)
    for res in resp["Reservations"]:
        for instance in res["Instances"]:
            print(instance["InstanceId"])

    print("Filtering instances")
    resp = ec2_client.describe_instances(Filters=[{"Name": "instance-state-name",
                                               "Values": ["terminated", "stopped"]}
                                          ]
                                 )
    # Instances may also be given named tags with values, you can then filter on "Name": "tag:Tag_name" with possible Values.


    for res in resp["Reservations"]:
        for instance in res["Instances"]:
            print(instance["InstanceId"])

print("\nUse collections")
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/collections.html
# A collection provides an iterable interface to a group of resources.
ec2_resource = boto3.resource("ec2") # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/collections.html
for instance in ec2_resource.instances.all():
    print(f"Instance id is {instance.instance_id} and Instance type is {instance.instance_type}.")
print("..")
for instance in ec2_resource.instances.filter(Filters=[{"Name": "availability-zone", "Values": ["eu-west-1"]}]):
    print(f"Instance id is {instance.instance_id} and Instance type is {instance.instance_type}.")
print("..")

print("Stop any running instances.")
ec2_resource.instances.filter(Filters=[{"Name": "instance-state-name", "Values": ["running"]}]).stop()


print("Husk å slette instanser! $$$$$$$$")
