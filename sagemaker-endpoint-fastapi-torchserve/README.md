
## Install all required dependencies
```bash
pip install -r requirements.txt
```

## Download BERT Classification Model
```bash
# Download pytorch_model.bin
curl -L https://huggingface.co/bert-base-uncased/resolve/main/pytorch_model.bin -o ./bert-base-uncased/pytorch_model.bin
# Download config.json
curl -L https://huggingface.co/bert-base-uncased/resolve/main/config.json -o ./bert-base-uncased/config.json
# Download tokenizer.json
curl -L https://huggingface.co/bert-base-uncased/resolve/main/tokenizer.json -o ./bert-base-uncased/tokenizer.json
# Download tokenizer_config.json
curl -L https://huggingface.co/bert-base-uncased/resolve/main/tokenizer_config.json -o ./bert-base-uncased/tokenizer_config.json
```

## Model Archive
```bash
torch-model-archiver -f --model-name bert_classifier \
    --version 1.0 \
    --serialized-file bert-base-uncased/pytorch_model.bin \
    --handler text_classifier.py \
    --extra-files "bert-base-uncased/config.json,bert-base-uncased/tokenizer.json,bert-base-uncased/tokenizer_config.json,bert-base-uncased/vocab.txt" \
    --export-path model_store
tar -czvf model.tar.gz model_store
aws s3 cp model.tar.gz <s3_path>
```

## Build Docker
```bash
export TAG=latest
docker build --no-cache -t sagemaker-fastapi-torchserve:$TAG .
```

## Run Docker
```bash
docker run -p 8080:8080 sagemaker-fastapi-torchserve
```

## Test with CURL
```bash
# Health Check
curl -X GET "http://localhost:8080/ping"

# Inference Request
curl -X POST "http://localhost:8080/invocations" -H "Content-Type: application/json" -d '{"text": "I love AI"}'
```


## Sagemaker
### Deploy the docker to Sagemaker Endpoint
```bash
export TAG=latest
./buildAndDeployDocker.sh
```

### Invoke SM Endpoint
```bash
python invoke.py
```


### Cleanup SM Resources
```bash
aws sagemaker delete-endpoint --endpoint-name sagemaker-fastapi-torchserve-endpoint
aws sagemaker delete-endpoint-config --endpoint-config-name sagemaker-fastapi-torchserve-config
aws sagemaker delete-model --model-name sagemaker-fastapi-torchserve-model
```