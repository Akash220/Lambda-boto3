#This code is used to take changes done in dynamodb from dynamodb stream and alerting it to users via email using lambda function.

import json
import boto3
sns = boto3.client('sns')
def lambda_handler(event, context):
    db = boto3.client('dynamodb')
    for record in event['Records']:
        if record['eventName'] == "INSERT":
            #insert function
            handler_insert(record)
        if record['eventName'] == "REMOVE":
           #delete function
           handler_delete(record)
          
def handler_insert(record):
    #Inserted image
    Inserted_image = record['dynamodb']['NewImage']['Message']['S']
    #Emailing via sns the inserted item
    response = sns.publish(TopicArn="arn:aws:sns:us-east-2:799914953831:dynamodb", 
               Message="The inserted item is " + Inserted_image)
    return response
    
def handler_delete(record):
    #Deleted image
    Deleted_image = record['dynamodb']['OldImage']['Message']['S']
    #Emailing via sns the deleted item
    response = sns.publish(TopicArn="arn:aws:sns:us-east-2:799914953831:dynamodb", 
               Message="The deleted item is " + Deleted_image)
    return response

    
            
            
    
