import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def sqs_listener(event, context):
    print("***COMP2:  SqsSubscriber.sqs_listener")
    print(f"event: {event}")
    print(f"context: {context}")
    print(f"Message Body: {event['Records'][0]['body']}")
    if 'messageAttributes' in event['Records'][0]:
        print(f"Message Attributes: {event['Records'][0]['messageAttributes']}")

    return "Done"
