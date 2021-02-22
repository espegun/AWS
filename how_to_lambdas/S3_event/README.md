# Put up a lambda function which gets triggered by events in S3
## Deploy  
`sls deploy`  
## Test  
...

The current setup in `code` may be correct, but the Lambda does not have access to RW S3.  
https://aws.amazon.com/premiumsupport/knowledge-center/lambda-execution-role-s3-bucket/  
Bruk gjerne noen templater i konsollen for å finne ut hvilke policy og sånn som må til.  
Se også Weber 76-84.  


### (old stuff below)
`$ curl https://07xnk0295b.execute-api.eu-west-1.amazonaws.com/dev/hello/Espen`  Use curl to send a GET request.  
`$ curl -d '{"name": "Espen"}' https://07xnk0295b.execute-api.eu-west-1.amazonaws.com/dev/hello` POST request, works.  
`$ curl -d 'name=Espen' https://07xnk0295b.execute-api.eu-west-1.amazonaws.com/dev/hello`  Attempted POST request, does NOT work. WHY?  
