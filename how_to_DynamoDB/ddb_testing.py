# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html#using-an-existing-table

import random

import boto3
from boto3.dynamodb.conditions import Attr
import botocore


TABLE_NAME = "users"


def create_table():

    # Create the DynamoDB table.
    # Note that one the Keys are defined, not other content.
    table = dynamodb.create_table(
        TableName=TABLE_NAME,
        KeySchema=[
            {
                'AttributeName': 'username',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'last_name',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'username',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'last_name',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    print(f"Creating the table '{TABLE_NAME}', please wait....")
    table.meta.client.get_waiter('table_exists').wait(TableName=TABLE_NAME)
    print("Done.")

    return table


def add_random_item(table):

    username = "".join([random.choice(list("abcdefghiljklmnopqrstuvwxyz")) for _ in range(8)])

    print(f"Adding user {username}...")

    table.put_item(
        Item={"username": username,
              "first_name": "Jane",
              "last_name": "Doe",
              "age": random.randint(18, 65),
              "account_type": "standard_user"})

    # For more effective batch writing, see:
    # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html#batch-writing

    return username


def get_user(table, username):

    print(f"Getting user {username}")

    response = table.get_item(Key={"username": username, "last_name": "Doe"})
    print(response["Item"])


def users_above_age(table, age):

    # Note that querying by key is much faster than scanning/filtering by some value.
    # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html  # querying-and-scanning

    response = table.scan(
        FilterExpression=Attr('age').gt(age)
    )
    items = response['Items']
    for item in items:
        print(item)


def delete_user(table, username):

    print(f"Deleting user {username}...")

    table.delete_item(Key={"username": username,
                           "last_name": "Doe"})


if __name__ == "__main__":

    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')

    try:
        create_table()
    except Exception:
        # botocore.errorfactory.ResourceInUseException:
        print(f"Table {TABLE_NAME} already exists.")

    # Instantiate a table resource object without actually creating a DynamoDB table.
    table = dynamodb.Table(TABLE_NAME)
    print(table.creation_date_time)

    for i in range(20):
        username = add_random_item(table)

    get_user(table, username)

    print("Filtered data")
    users_above_age(table, 50)

    # Delete the last user added
    delete_user(table, username)

    print("Deleting table. Not sure it gets permanently removed from the console though....")
    table.delete()

    print("That was fun.")
