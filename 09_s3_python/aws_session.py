import boto3
import pandas as pd


session = boto3.Session(profile_name='s3_dev')
dev_s3_client = session.client('s3')

print(dev_s3_client.list_buckets()) #list buckets

