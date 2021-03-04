# Put up a lambda function which gets triggered by events in S3
## Deploy  
`sls deploy`  
## Test  
`aws s3 cp uploaded_file.txt s3://upload-data-here/`

The lambda must be given a suitable EXECUTION ROLE. 
https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html
Defined a policy `AWSLambdaS3Policy`:
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

Also created `lambda-s3-role` with the above `AWSLambdaS3Policy` attached.





Also see this example, where the lambda is given a role which has a policy which
also has the permissions required for the lambda to read and write to certain S3 buckets.

Se også Weber 76-84.  



