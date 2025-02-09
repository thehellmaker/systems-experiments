import boto3
import os

sagemaker = boto3.client("sagemaker", region_name="us-east-1")

# Get AWS Account ID from environment variable
aws_account_id = os.getenv("AWS_ACCOUNT_ID")
tag = os.getenv("TAG")

if not aws_account_id:
    raise ValueError("AWS_ACCOUNT_ID environment variable is not set")

if not tag:
    raise ValueError("TAG environment variable is not set")

print(f"Using AWS Account ID: {aws_account_id}")

model_name=f"sagemaker-fastapi-torchserve-model-{tag}"
# Create the model
sagemaker.create_model(
    ModelName=model_name,
    PrimaryContainer={
        "Image": f"{aws_account_id}.dkr.ecr.us-east-1.amazonaws.com/sagemaker-fastapi-torchserve:{tag}",
        "ModelDataUrl": "<s3_path>",
        "Environment": {
            "SAGEMAKER_MODEL_SERVER_TIMEOUT": "3600",
            "SAGEMAKER_MODEL_SERVER_WORKERS": "1",
            "SAGEMAKER_DISABLE_CONTAINER_SUPPORT": "true"  # Prevents SageMaker from overriding the model path
        }
    },
    ExecutionRoleArn=f"arn:aws:iam::{aws_account_id}:role/service-role/AmazonSageMaker-ExecutionRole-20240308T062082"
)

endpoint_config_name=f"sagemaker-fastapi-torchserve-config-{tag}"

# Create an endpoint configuration
sagemaker.create_endpoint_config(
    EndpointConfigName=endpoint_config_name,
    ProductionVariants=[
        {
            "InstanceType": "ml.g4dn.xlarge",
            "InitialInstanceCount": 1,
            "ModelName": model_name,
            "VariantName": "AllTraffic",
        }
    ],
)

# Deploy the endpoint
sagemaker.create_endpoint(
    EndpointName=f"sagemaker-fastapi-torchserve-endpoint-{tag}",
    EndpointConfigName=endpoint_config_name,
)
