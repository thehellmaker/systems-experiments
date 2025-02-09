export AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>
export AWS_ACCOUNT_ID=<AWS_ACCOUNT_ID>
torch-model-archiver -f --model-name bert_classifier \
    --version 1.0 \
    --serialized-file bert-base-uncased/pytorch_model.bin \
    --handler text_classifier.py \
    --extra-files "bert-base-uncased/config.json,bert-base-uncased/tokenizer.json,bert-base-uncased/tokenizer_config.json,bert-base-uncased/vocab.txt" \
    --export-path model_store
tar -czvf model.tar.gz model_store
aws s3 cp model.tar.gz <s3_path>
docker build -t sagemaker-fastapi-torchserve:$TAG .


aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com

# Create an ECR repository
aws ecr create-repository --repository-name sagemaker-fastapi-torchserve --region us-east-1

# Tag the Docker image
docker tag sagemaker-fastapi-torchserve:$TAG $AWS_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/sagemaker-fastapi-torchserve:$TAG

# Push the image to ECR
docker push $AWS_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/sagemaker-fastapi-torchserve:$TAG

python deploy.py