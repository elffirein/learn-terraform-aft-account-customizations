import boto3

# http://boto3.readthedocs.io/en/latest/reference/services/ec2.html#service-resource

client = boto3.client('ec2', region_name='us-east-1')

# create VPC
vpc = client.create_vpc(CidrBlock='10.1.0.0/16')
