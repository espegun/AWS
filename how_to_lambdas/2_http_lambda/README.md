# Put up a lambda function as a simple HTTP-endpoint
## Deploy  
`sls deploy`  
## Test  
`$ curl https://07xnk0295b.execute-api.eu-west-1.amazonaws.com/dev/hello/Espen`  Use curl to send a GET request.  
`$ curl -d '{"name": "Espen"}' https://07xnk0295b.execute-api.eu-west-1.amazonaws.com/dev/hello` POST request, works.  
`$ curl -d 'name=Espen' https://07xnk0295b.execute-api.eu-west-1.amazonaws.com/dev/hello`  Attempted POST request, does NOT work. WHY?  
