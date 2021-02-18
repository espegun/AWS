https://www.serverless.com/framework/docs/providers/aws/examples/hello-world/python/
# How to deploy and test the minimum lambda
Step 2 - deploy  
`sls deploy`  
Then check that the function is available in the AWS console.  

Step 3 - Invoke deployed function  
`sls invoke -f my-function`  





OLD STUFF BELOW

# The minimum lambda
Deployed as described by Weber page 74-85.  
This example uses Origo's AWS account.

Write to this folder  
`ok-origo-dataplatform-dev/test/espeng-testing-bucket/simple_dataset/pre-lambda/`
Pick up by lambda and write to this folder.  
`ok-origo-dataplatform-dev/test/espeng-testing-bucket/simple_dataset/post-lambda/`

Create a local `handler.py` file. 
Zip it using `zip -r function.zip .`
Need to be logged in using `saml2aws login` or similar means.  
Copy the zippde lambda to S3:
`aws s3 cp simple_lambda.zip s3://ok-origo-dataplatform-dev/test/espeng-testing-bucket/simple_dataset/simple_lambda.zip`



BØR KUNNE DOCKER FØRST. DESSUTEN WEBER ER UTDATERT. BRUKER MEDIUM ELLER AWS DIREKTE
