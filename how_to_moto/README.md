# How to test with moto

## The purpose
To test any function which uses `boto3` against an AWS-service, but during the test rather use an offline, simulated AWS instead of the real thing.

## How does it work?
...

## Useful commands
`from moto import mock_s3` Import it.  
`@mock_s3` Put this as a decorator around the `test_something` function.   
`...`  ....  

## Useful links
[Pytest and moto (TO BE READ)](https://medium.com/@tensoriot/unit-testing-with-pytest-and-moto-e94fc2eefe7a)  
