#!/usr/bin/env python

import boto3

import constants

s3 = boto3.resource('s3')
bucket = s3.Bucket(constants.BUCKET_NAME)

# Create the bucket
bucket.create(
    ACL='private',
    CreateBucketConfiguration={
        'LocationConstraint':constants.BUCKET_REGION
    }
)

# Create some objects
for x in range(0, 2):
    # Create private objects
    bucket.put_object(
        ACL='private',
        Body=b'private!',
        Key=f"private-{x}"
    )

    # Create public objects
    bucket.put_object(
        ACL='public-read',
        Body=b'public-read!',
        Key=f"public-read-{x}"
    )