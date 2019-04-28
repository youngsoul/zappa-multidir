import boto3
import platform
from sqs_service import send_message_to_queue
import paramiko

"""
https://www.sftp.net/public-online-sftp-servers
"""
paramiko.util.log_to_file('/tmp/paramiko.log')


def recurring_event_handler(event, context):

    print("**** COMP1:  RecurringEvents.recurring_event_handler")
    my_kwargs = event.get('kwargs')
    print(f"***** kwargs: {my_kwargs}")

    return 'Done'


def every_2_mins(event, context):
    print("**** COMP1:  RecurringEvents.every_2_mins")
    my_kwargs = event.get('kwargs')
    print(f"***** kwargs: {my_kwargs}")

    queue_name = my_kwargs['queuename']
    msg_id, md5_of_msg = send_message_to_queue("***COMP1:  Hello Zappa SQS CloudWatch World...", queue_name)

    print("Notification sent with message id: %s" % msg_id)

    return 'Done'
