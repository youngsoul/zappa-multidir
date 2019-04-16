import boto3
"""
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs.html
"""
_sqs = None

def _get_sqs():
    global _sqs

    if not _sqs:
        _sqs = boto3.resource('sqs')

    return _sqs

def send_message_to_queue(msg, queue_name):
    """
    Put a message on the queue
    :param msg: String formatted message
    :param queue_name: name of sqs quue
    :return: MessageId, MD5 hash of Message body
    """
    # Get the queue. This returns an SQS.Queue instance
    try:
        queue = _get_sqs().get_queue_by_name(QueueName=queue_name)

        response = queue.send_message(MessageBody=msg)

        return response.get('MessageId'), response.get('MD5OfMessageBody')
    except Exception as exc:
        print(f"Error sending message to queue: {queue_name}.  Exc: {exc}")

def read_messages_from_queue_url(queue_name, num_messages = 1):
    queue = _get_sqs().get_queue_by_name(QueueName=queue_name)
    messages = queue.receive_messages(MaxNumberOfMessages=num_messages)

    return messages

def delete_message_from_queue(queue_message):
    try:
        queue_message.delete()
    except Exception as exc:
        print(f"Error deleting message: {exc}.  Queue Message Type: {type(queue_message)}.  Queue Mesage: {queue_message}")
