# Use official PyTorch base image with CUDA support
FROM pytorch/pytorch:2.6.0-cuda11.8-cudnn9-devel

# Set working directory for SageMaker
WORKDIR /opt/ml/code

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    unzip \
    openjdk-17-jdk \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /opt/ml/code/
RUN pip install --no-cache-dir -r /opt/ml/code/requirements.txt

# Copy application code and required files
COPY app.py /opt/ml/code/
COPY serve /opt/ml/code
COPY config.properties /opt/ml/code
COPY model_store/ /opt/ml/model

# Ensure proper permissions for scripts
RUN chmod +x /opt/ml/code/serve

# Set SageMaker environment variables
ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PYTHONPATH /opt/ml/code
ENV PATH="/opt/ml/code/:${PATH}"

# Expose TorchServe and SageMaker default ports
EXPOSE 8080

