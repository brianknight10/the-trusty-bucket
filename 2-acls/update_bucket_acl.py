#!/usr/bin/env python

import boto3

import constants

s3 = boto3.resource('s3')
bucket = s3.Bucket(constants.BUCKET_NAME)

# Set bucket ACL to 'public-read'
bucket.Acl().put(ACL='public-read')

# Create object with default ACL
bucket.put_object(
    Body=b'default!',
    Key=f"default"
)