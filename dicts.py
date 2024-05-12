import boto3

ec2_client = boto3.client('ec2', region_name="eu-west-3")

all_available_vpcs = ec2_client.describe_vpcs()
vpcs = all_available_vpcs["Vpcs"]

for vpc in vpcs: 
    print(vpc["VpcId"])
    cidr_block_assoc_sets = vpc["CidrBlockAssociationSet"]
    for assoc_set in cidr_block_assoc_sets:
        print(assoc_set["CidrBlockState"])

# will return: e.g.  
# vpc-0371c426ad8b0bb94
# {'State': 'associated'}
