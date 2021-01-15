def lambda_handler(event, context):

    # See Weber, page 80
    if "body" in event:
        return {"response": event["body"] + "_Jalla!"}
    else:
        return {"response": "No body found."}

