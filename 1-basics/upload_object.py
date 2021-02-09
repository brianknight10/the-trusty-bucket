#!/usr/bin/env python

import boto3

import constants

s3 = boto3.resource('s3')

# Upload the sandwich files to the bucket
for file in constants.SANDWICHES:
    s3.meta.client.upload_file(f"objects/{file}.jpeg",
                               constants.BUCKET_NAME,
                               f"{file}.jpeg")