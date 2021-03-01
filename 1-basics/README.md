## S3 Basics

These scripts support the topics covered in the [basics blog post](https://blog.ippon.tech/the-trusty-bucket-introduction-and-basics/).

### Script List and Order

Run the scripts in the following order to follow along with the blog post. You
can configure your bucket name and region by changing the `constants.py` file.

- `create_bucket.py`: Create a new S3 bucket in you AWS account
- `describe_bucket.py`: Examine the list of attributes for the S3 bucket
- `upload_object.py`: Uploads three objects to the S3 bucket
- `describe_object.py`: Examine the attributes and actions for an S3 object
- `cleanup.py`: Delete the objects and the S3 bucket