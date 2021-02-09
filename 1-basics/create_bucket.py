#!/usr/bin/env python

import boto3

import constants

client = boto3.client('s3')

# Create the bucket
response = client.create_bucket(
    Bucket=constants.BUCKET_NAME,
    CreateBucketConfiguration={
        'LocationConstraint':constants.BUCKET_REGION
    }
)

print('Created bucket', BUCKET_NAME, 'at', response['Location'])