import json

# Make a simple GET call by pasting the URL in the browser like e.g.:
# https://07xnk0295b.execute-api.eu-west-1.amazonaws.com/dev/hello/Espen 


def hello_get(event, context):

    """
    Test:
    curl https://07xnk0295b.execute-api.eu-west-1.amazonaws.com/dev/hello/Espen
    """

    name = event["pathParameters"]["name"]  # name is specified as a parameter in serverless.yml

    response = {"greeting": f"Hello, {name}! (Reply after GET)"}

    return {"statusCode": 200,
            "headers": {"Content-type": "application/json"},
            "body": json.dumps(response)
            }


def hello_post(event, context):

    """
    Test (https://medium.com/100-days-of-linux/10-curl-commands-that-you-should-know-ee3d032eb351)
    curl -d '{"name": "Espen"}' https://07xnk0295b.execute-api.eu-west-1.amazonaws.com/dev/hello  # This works
    curl -d 'name=Espen' https://07xnk0295b.execute-api.eu-west-1.amazonaws.com/dev/hello  # This does NOT work. WHY?

    """
    name = json.loads(event["body"])["name"]
    response = {"greeting": f"Hello, {name}! (Reply after POST)"}

    return {"statusCode": 200,
            "headers": {"Content-type": "application/json"},
            "body": json.dumps(response)
            }
