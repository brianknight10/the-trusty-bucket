#!/usr/bin/env python

import boto3

import constants

client = boto3.client('s3')

client.put_public_access_block(
    Bucket=constants.BUCKET_NAME,
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': True,
        'IgnorePublicAcls': True
    }
)