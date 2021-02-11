#!/usr/bin/env python

import boto3

import constants

s3 = boto3.resource('s3')

# Get the bucket object
key = f"{constants.SANDWICHES[0]}.jpeg"
img = s3.Object(constants.BUCKET_NAME, key)

# List the attributes and actions for the object
attrs = ""
for attr in dir(img):
    if not attr.startswith("_"):
        attrs += f"'{attr}' "

print(attrs)