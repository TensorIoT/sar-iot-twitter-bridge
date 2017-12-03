from time import sleep
import boto3, json, os, uuid, logging, random, string

from twitter import *

token = os.environ['TOKEN']
tokenSecret = os.environ['TOKEN_SECRET']
consumerKey = os.environ['CONSUMER_KEY']
consumerSecret = os.environ['CONSUMER_SECRET']

t = Twitter(
    auth=OAuth(token, tokenSecret, consumerKey, consumerSecret))

def lambda_handler(event, context):
    print(event)
    if 'deviceID' not in event:
        print("Missing DeviceID")
        return "Error"

    if 'incomingText' not in event:
        print("Missing IncomingText")
        return "Error"

    print(event['deviceID'])
    print(event['incomingText'])

    try:
        t.statuses.update(
            status="Message from "+event['deviceID']+" : "+event['incomingText'])
        return "Success"
    except Exception as e:
        print(e)
        return "Error"
