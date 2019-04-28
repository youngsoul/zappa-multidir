import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
import paramiko
from .sftp_client import test_sftp

"""
{'Records': 
    [
        {'messageId': '7d84d03c-0ef1-4d01-bf51-bae14572691f', 
         'receiptHandle': 'AQEBpGfpye//yFo+Z5lMy2zY+i5HV6rTd6os+Uc1ICT47sJebs0y3KyLwpSApsrom3/oXMT3s/LPt5CYpps60n6nCuS2cUdSUAUcPwcgOTb3mWzMBBTz2TND/J4dE8+cgbKI+wZ6IfWqeBM1LxlPq9XaqgEgLhR/MIOBjD+lqKN0Otc0nUtKNKbVbrXUOLnjIeSlteom9ujg+Na1YHKjjbm/ZbNvQ9GTEC3buykbbgVXqZm14eAezjaurXuNYrTJrArgqN1sLZ7YgPQs6rWqnvbd5PDN+n/h+srf1/+K+fpR76kk/7LqSCGredEU+I/vGUv9LQITZYqR5cly/3TnZC8K43CnSNCwfMNM5AwOzRyN8F8A6iQ4JL29y/nX3ZXKn7MQ1+QKUju89pNWyjRR9dXCrQ==', 
         'body': 'This is a test message', 
         'attributes': {
            'ApproximateReceiveCount': '1', 
            'SentTimestamp': '1539567381670', 
            'SenderId': 'AIDAIPR4RVWVANBX5X2R4', 
            'ApproximateFirstReceiveTimestamp': '1539567381686'}, 
         'messageAttributes': {
            'attr2': {
                'stringValue': '42', 
                'stringListValues': [], 
                'binaryListValues': [], 
                'dataType': 'Number'}, 
            'attr1': {
                'stringValue': 'value1', 
                'stringListValues': [], 
                'binaryListValues': [], 
                'dataType': 'String'}
         }, 
         'md5OfBody': 'fafb00f5732ab283681e124bf8747ed1', 'md5OfMessageAttributes': 'b4c762a206809fcd8eaad92a0eacfe1d', 'eventSource': 'aws:sqs', 'eventSourceARN': 'arn:aws:sqs:us-east-1:485071734737:zappa-test-queue', 'awsRegion': 'us-east-1'}]}"""


def sqs_listener(event, context):
    print("***COMP1:  SqsSubscriber.sqs_listener")
    print(f"event: {event}")
    print(f"context: {context}")
    print(f"Message Body: {event['Records'][0]['body']}")
    if 'messageAttributes' in event['Records'][0]:
        print(f"Message Attributes: {event['Records'][0]['messageAttributes']}")

    results = test_sftp()
    print(f"*** SFTP results: {results}")

    return "Done"
