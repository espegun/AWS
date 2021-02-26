# Put up a lambda function which gets triggered by events in S3
## Deploy  
`sls deploy`  
## Test  
`aws s3 cp uploaded_file.txt s3://aws-basics/`

The lambda must be given a suitable EXECUTION ROLE. 
https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html
Also see this example, where the lambda is given a role which has a policy which
also has the permissions required for the lambda to read and write to certain S3 buckets.



Se også Weber 76-84.  


### (old stuff below)
`$ curl https://07xnk0295b.execute-api.eu-west-1.amazonaws.com/dev/hello/Espen`  Use curl to send a GET request.  
`$ curl -d '{"name": "Espen"}' https://07xnk0295b.execute-api.eu-west-1.amazonaws.com/dev/hello` POST request, works.  
`$ curl -d 'name=Espen' https://07xnk0295b.execute-api.eu-west-1.amazonaws.com/dev/hello`  Attempted POST request, does NOT work. WHY?  
