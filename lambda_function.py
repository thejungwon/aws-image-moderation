#python 3.7
from __future__ import print_function

import boto3
from decimal import Decimal
import json
import urllib.parse


rekognition = boto3.client('rekognition')
dynamodb    = boto3.client('dynamodb')
s3          = boto3.resource('s3')
TABLE_NAME     = "image_table"
def moderate_image(bucket, key):

    client=boto3.client('rekognition')

    response = client.detect_moderation_labels(Image={'S3Object':{'Bucket':bucket,'Name':key}})

    print('Detected labels for ' + key)
    for label in response['ModerationLabels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))
        print (label['ParentName'])
    return response



def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    region = event['Records'][0]['awsRegion']

    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    try:
        response = moderate_image(bucket, key)

        isSensitive = len(response['ModerationLabels']) != 0
        name = key.split(".")[0].split("/")[1]
        url = "https://{}.s3.{}.amazonaws.com/{}".format(bucket,region,key)
        dynamodb.put_item(TableName=TABLE_NAME, Item={'id':{'S':name},'url':{'S':url}, 'isSensitive':{'BOOL':isSensitive}})
        object = s3.Object(bucket, "logs/"+name+".json")
        object.put(Body=json.dumps(response).encode())
        return response
    except Exception as e:
        print(e)
        print("Error processing object {} from bucket {}. ".format(key, bucket) +
              "Make sure your object and bucket exist and your bucket is in the same region as this function.")
        raise e
