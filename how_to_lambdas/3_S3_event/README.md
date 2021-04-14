# Put up a lambda function which gets triggered by events in S3
## Deploy  
`sls deploy` (must be run from the serverless directory, i.e. where `serverless.yml` is)   
## Test  
`aws s3 cp uploaded_file.txt s3://upload-data-here/`

The lambda must be given a suitable EXECUTION ROLE, as shown [here](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html).  
`serverless.yml` gave the lambda function the custom defined `lambda-s3-role`.
The custom *role* `lambda-s3-role` was created in the console with the below `AWSLambdaS3Policy` attached.
Defined a *policy* `AWSLambdaS3Policy` in the console:
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:PutLogEvents",
                "logs:CreateLogGroup",
                "logs:CreateLogStream"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::upload-data-here/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::write-logs-here/*"
        }
    ]
}
```
Meaning the lambda function now has the option to get objects from one bucket and write to another.

As defined in `serverless.yml`, the event `s3:ObjectCreated:*` in a bucket `upload-data-here` triggers the handler function defined in `handler.py`.

Se også Weber 76-84.  



