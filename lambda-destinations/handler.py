import json
import logging
import os

import boto3

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

QUEUE_URL = os.getenv('QUEUE_URL')
SQS = boto3.client('sqs')

def main(event, context):
    for record in event['Records']:
        body = record["Sns"]["Message"]
        logger.info(f'Message body: {body}')
        if body == 'fail':
          raise Exception("failing as asked")
