# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html#using-an-existing-table

import random

import boto3

from create_table import TABLE_NAME


def add_random_item(table):

    print("Adding user....")

    table.put_item(
        Item={"username": "".join([random.choice(list("abcdefghiljklmnopqrstuvwxyz")) for _ in range(8)]),
              "first_name": "Jane",
              "last_name": "Doe",
              "age": random.randint(18, 65),
              "account_type": "standard_user"})


if __name__ == "__main__":

    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')

    # Instantiate a table resource object without actually creating a DynamoDB table.
    table = dynamodb.Table(TABLE_NAME)
    print(table.creation_date_time)

    for i in range(3):
        add_random_item(table)

    # Print out some data about the table.
    print(f"The number of items in the table is {table.item_count}.")
    print("WHY DOES NOT THIS WORK?!")



    print("That was fun.")
