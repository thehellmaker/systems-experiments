# Use official Python base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install TorchServe
RUN pip install torchserve torch-model-archiver

# Copy application code
COPY app.py .
COPY entrypoint.sh .
COPY config.properties .
COPY model_store/ model_store/

# Expose required ports
EXPOSE 8000 8080

# Run entrypoint script
CMD ["bash", "entrypoint.sh"]
