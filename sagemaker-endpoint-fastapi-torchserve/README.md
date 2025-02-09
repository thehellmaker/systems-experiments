# SageMaker FastAPI TorchServe Integration

This repository provides a template for deploying a custom Docker container on Amazon SageMaker that integrates FastAPI with TorchServe. This architecture allows for advanced customization at the FastAPI layer, enabling features such as:

- Request/Response customization
- Caching mechanisms
- Request batching
- Custom middleware implementation
- Additional API endpoints

## Architecture Overview

```
Client Request → SageMaker Endpoint → FastAPI → TorchServe → BERT Model
```

## Prerequisites

- AWS CLI configured with appropriate permissions
- Docker installed
- Python 3.7+
- Access to Amazon SageMaker

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Download BERT Model Assets
Download the required BERT model files from Hugging Face:
```bash
# Create model directory
mkdir -p bert-base-uncased

# Download model files
curl -L https://huggingface.co/bert-base-uncased/resolve/main/pytorch_model.bin -o ./bert-base-uncased/pytorch_model.bin
curl -L https://huggingface.co/bert-base-uncased/resolve/main/config.json -o ./bert-base-uncased/config.json
curl -L https://huggingface.co/bert-base-uncased/resolve/main/tokenizer.json -o ./bert-base-uncased/tokenizer.json
curl -L https://huggingface.co/bert-base-uncased/resolve/main/tokenizer_config.json -o ./bert-base-uncased/tokenizer_config.json
```

### 3. Create Model Archive
Package the model files for TorchServe:
```bash
torch-model-archiver -f --model-name bert_classifier \
    --version 1.0 \
    --serialized-file bert-base-uncased/pytorch_model.bin \
    --handler text_classifier.py \
    --extra-files "bert-base-uncased/config.json,bert-base-uncased/tokenizer.json,bert-base-uncased/tokenizer_config.json,bert-base-uncased/vocab.txt" \
    --export-path model_store

# Upload to S3 (replace <s3_path> with your bucket path)
tar -czvf model.tar.gz model_store
aws s3 cp model.tar.gz <s3_path>
```

### 4. Build and Test Docker Image Locally

Build the Docker image:
```bash
export TAG=latest
docker build --no-cache -t sagemaker-fastapi-torchserve:$TAG .
```

Run the container locally:
```bash
docker run -p 8080:8080 sagemaker-fastapi-torchserve
```

Test the endpoints:
```bash
# Health check
curl -X GET "http://localhost:8080/ping"

# Test inference
curl -X POST "http://localhost:8080/invocations" \
    -H "Content-Type: application/json" \
    -d '{"text": "I love AI"}'
```

## SageMaker Deployment

### Deploy to SageMaker
```bash
export TAG=latest
./buildAndDeployDocker.sh
```

### Test SageMaker Endpoint
```bash
python invoke.py
```

### Cleanup Resources
When you're done, clean up your SageMaker resources:
```bash
aws sagemaker delete-endpoint --endpoint-name sagemaker-fastapi-torchserve-endpoint
aws sagemaker delete-endpoint-config --endpoint-config-name sagemaker-fastapi-torchserve-config
aws sagemaker delete-model --model-name sagemaker-fastapi-torchserve-model
```

## Customization

The FastAPI layer (`app.py`) can be modified to add:
- Custom preprocessing/postprocessing logic
- Caching mechanisms
- Request batching
- Additional API endpoints
- Authentication/Authorization
- Custom middleware

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the Apache License, Version 2.0 - see below for details:

```
Copyright 2024 

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

