import boto3
import sys
client = boto3.client('elbv2', region_name='us-east-1')

response = client.register_targets(
    TargetGroupArn= sys.argv[1],
    Targets=[
        {
            'Id': sys.argv[2],
        },
    ]
)

print(response)