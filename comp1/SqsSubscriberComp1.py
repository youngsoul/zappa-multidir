import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
from .sftp_client import test_sftp


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
