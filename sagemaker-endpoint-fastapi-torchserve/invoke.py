import boto3
import json

runtime = boto3.client("sagemaker-runtime", region_name="us-east-1")

import os

tag = os.getenv("TAG")

if not tag:
    raise ValueError("TAG environment variable is not set")

response = runtime.invoke_endpoint(
    EndpointName=f"sagemaker-fastapi-torchserve-endpoint-{tag}",
    ContentType="application/json",
    Body=json.dumps({"text": "SageMaker is awesome!"}),
)

result = json.loads(response["Body"].read().decode())
print(result)
