import json

# Make a simple GET call by pasting the URL in the browser like e.g.:
# https://07xnk0295b.execute-api.eu-west-1.amazonaws.com/dev/hello/Espen 

def hello_get(event, context):

    name = event["pathParameters"]["name"]  # name is specified as a parameter in serverless.yml

    response = {"greeting": f"Hello, {name}"}

    return {"statusCode": 200,
            "body": json.dumps(response),
            "headers": {"Content-type": "application/json"}
            }



def hello_post(event, context):
    return {"msg": "Work in progress...."}

