import boto3
import sys

client = boto3.client('elbv2', region_name='us-east-1')

response = client.deregister_targets(
    TargetGroupArn= str(sys.argv[1]),
    Targets=[
        {
            'Id': str(sys.argv[2]),
        },
    ]
)

print(response)
