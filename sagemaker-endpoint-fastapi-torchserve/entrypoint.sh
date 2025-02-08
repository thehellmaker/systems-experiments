#!/bin/bash
# Start TorchServe in the background
torchserve --start --ncs --model-store /app/model_store --models bert_classifier.mar --ts-config /app/config.properties &

# Start FastAPI
uvicorn app:app --host 0.0.0.0 --port 8000