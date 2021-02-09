#!/usr/bin/env python

import boto3

import constants

# Get the bucket resource
s3 = boto3.resource('s3')
bucket = s3.Bucket(name=constants.BUCKET_NAME)

# List all of the subresources for the bucket
for resource in bucket.get_available_subresources():
    print(resource)