import boto3

eks_client_ny = boto3.client('eks') #, region_name='us-east-1')

clusters = eks_client_ny.list_clusters()
# print(clusters)
print(clusters['clusters'])

clusters = eks_client_ny.list_clusters()['clusters']

for cluster in clusters:
    response = eks_client_ny.describe_cluster(
        name=cluster
    )
    cluster_info = response['cluster']
    cluster_status = cluster_info['status']
    cluster_endpoint = cluster_info['endpoint']
    cluster_version = cluster_info['version']

    print(f"Cluster {cluster} status is {cluster_status}")
    print(f"Cluster endpoint: {cluster_endpoint}")
    print(f"Cluster version: {cluster_version}")
