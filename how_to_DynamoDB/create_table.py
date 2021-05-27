# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html#creating-a-new-table

import boto3

TABLE_NAME = "users"

if __name__ == "__main__":

    # Get the service resource.
    dynamodb = boto3.resource("dynamodb")

    # Create the DynamoDB table.
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

    # Print out some data about the table.
    print(f"The number of items in the table is {table.item_count}.")
