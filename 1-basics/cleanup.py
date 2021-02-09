#!/usr/bin/env python

import boto3

import constants

s3 = boto3.resource('s3')
bucket = s3.Bucket(name=constants.BUCKET_NAME)

# Remove the images from the bucket
print('Emptying bucket', constants.BUCKET_NAME)
response = bucket.delete_objects(
    Delete={
        'Objects': [
            { 'Key': f"{constants.SANDWICHES[0]}.jpeg" },
            { 'Key': f"{constants.SANDWICHES[1]}.jpeg" },
            { 'Key': f"{constants.SANDWICHES[2]}.jpeg" }
        ]
    }
)

# Delete the bucket
bucket.delete()
print('Bucket', constants.BUCKET_NAME, 'deleted.')
