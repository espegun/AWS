# How to test with moto

## The purpose
To test any function which uses `boto3` against an AWS-service, but during the test rather use an offline, simulated AWS instead of the real thing.

## How does it work?
...

## Useful commands
`from moto import mock_s3` Import it.  
`@mock_s3` Put this as a decorator around the `test_something` function to set up a new mocked s3 instance.  

When defining the mocked s3-instance in a fixture, rather do the below (no wrappers, since the instances will not be connected):
```
@pytest.fixture(scope="function")
def simulated_bucket(self, bucket_name, object_key):
        mock_s3().start()
        s3 = boto3.resource("s3", region_name="eu-west-1")
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={"LocationConstraint": "eu-west-1"},
        )
        yield

def test_workbook_in_s3(self, simulated_bucket):
    ...do some test...
```

`...`  ....  

## Useful links
[Pytest and moto (TO BE READ)](https://medium.com/@tensoriot/unit-testing-with-pytest-and-moto-e94fc2eefe7a)  
