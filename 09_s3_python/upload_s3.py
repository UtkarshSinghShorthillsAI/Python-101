import os
import boto3

# instantitate the s3 client
session = boto3.Session(profile_name='s3_dev')
client = session.client('s3')


# set variable
bucket = 'utkarshfirsts3'
cur_path = os.getcwd()
file = 'data.csv'
filename = os.path.join(cur_path, 'data', file)


# open the file
data = open(filename, 'rb') #rb = read binary


# load data into s3

client.upload_file(filename, bucket, 'data_in_s3.csv')


