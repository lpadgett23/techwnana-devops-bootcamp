import boto3
from operator import itemgetter

ec2_client = boto3.client('ec2', region_name='us-east-1')
ec2_resource = boto3.resource('ec2', region_name='us-east-1')

instance_id = ''

volumes = ec2_client.describe_volumes()

my_instance_volume = volumes['Volumes'][0]

snapshots = ec2_client.describe_snapshots()

latest_snapshot = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)[0]
print(latest_snapshot['StartTime'])

new_volume = ec2_client.create_volume()

while True:
  vol = ec2_resource.Volume(new_volume['VolumeId'])
  print(vol.state)
  if vol.state == 'available':
    ec2_resource.Instance(instance_id).attach_volume()
    break
