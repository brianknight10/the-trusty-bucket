#!/usr/bin/env python

import boto3

import constants

s3 = boto3.resource('s3')
bucket = s3.Bucket(name=constants.BUCKET_NAME)

# Remove the objects from the bucket
print('Emptying bucket', constants.BUCKET_NAME)
for x in range(0, 2):
    bucket.delete_objects(
        Delete={
            'Objects': [
                { 'Key': f"private-{x}" },
                { 'Key': f"public-read-{x}" },
                { 'Key': "default" }
            ]
        }
    )

# Delete the bucket
bucket.delete()
print('Bucket', constants.BUCKET_NAME, 'deleted.')
