# Put up a lambda function which gets triggered by events in S3
## Deploy  
`sls deploy`  
## Test  
...
WIP (old stuff below)
`$ curl https://07xnk0295b.execute-api.eu-west-1.amazonaws.com/dev/hello/Espen`  Use curl to send a GET request.  
`$ curl -d '{"name": "Espen"}' https://07xnk0295b.execute-api.eu-west-1.amazonaws.com/dev/hello` POST request, works.  
`$ curl -d 'name=Espen' https://07xnk0295b.execute-api.eu-west-1.amazonaws.com/dev/hello`  Attempted POST request, does NOT work. WHY?  
