## S3 ACLs

These scripts support the topics covered in the [ACLs blog post](https://blog.ippon.tech/the-trusty-bucket-access-control-lists/).

### Script List and Order

Run the scripts in the following order to follow along with the blog post. You
can configure your bucket name and region by changing the `constants.py` file.

- `setup.py`: Create a new S3 bucket in your AWS account along with several objects
- `update_bucket_acl.py`: Update the ACL on the S3 bucket
- `public_access_block.py`: Block public access to the S3 bucket via ACLs
- `cleanup.py`: Delete the objects and the S3 bucket
