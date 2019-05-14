'''
This is a sample that connects Lambda with IFTTT Maker channel. The event is
sent in this format: <serialNumber>-<clickType>.

The following JSON template shows what is sent as the payload:
{
    "serialNumber": "GXXXXXXXXXXXXXXXXX",
    "batteryVoltage": "xxmV",
    "clickType": "SINGLE" | "DOUBLE" | "LONG"
}

A "LONG" clickType is sent if the first press lasts longer than 1.5 seconds.
"SINGLE" and "DOUBLE" clickType payloads are sent for short clicks.

For more documentation, follow the link below.
http://docs.aws.amazon.com/iot/latest/developerguide/iot-lambda-rule.html
'''

from __future__ import print_function

import boto3
import json
import logging
import urllib2

logger = logging.getLogger()
logger.setLevel(logging.INFO)

maker_key = 'XXXXXX'  # change it to your Maker key
aws_sns = boto3.client('sns')
aws_lambda = boto3.client('lambda')
phone_number = '+86XXXXX'  # change it to your phone number


def lambda_handler(event, context):
    logger.info('Received event: ' + json.dumps(event))
    # make sure you created a receipe for event <serialNumber>-<clickType>
    maker_event = '%s-%s' % (event['serialNumber'], event['clickType'])
    logger.info('Maker event: ' + maker_event)


    if event['serialNumber'] == 'G030MD048506E9X4':
        # Zitong's Button
        if event['clickType'] == 'SINGLE':
            # Single Click, invoke IMissYou
            response = aws_lambda.invoke(
                FunctionName='IMissYou',
                InvocationType='Event',
                LogType='None',
                ClientContext='',
                Payload=b'')
            return
        if event['clickType'] == 'DOUBLE':
                url = 'https://maker.ifttt.com/trigger/%s/with/key/%s' % (maker_event, maker_key)
                f = urllib2.urlopen(url)
                response = f.read()
                f.close()
                logger.info('Event has been sent to IFTTT Maker channel')
                message = 'Hello from your IoT Button %s. Here is the full event: %s' % (
                event['serialNumber'], json.dumps(event))
                aws_sns.publish(PhoneNumber=phone_number, Message=message)
        if event['clickType'] == 'LONG':
            url = 'https://maker.ifttt.com/trigger/%s/with/key/%s' % (maker_event, maker_key)
            f = urllib2.urlopen(url)
            response = f.read()
            f.close()
            logger.info('Event has been sent to IFTTT Maker channel')
            message = 'Hello from your IoT Button %s. Here is the full event: %s' % (
            event['serialNumber'], json.dumps(event))
            aws_sns.publish(PhoneNumber=phone_number, Message=message)

    return response
