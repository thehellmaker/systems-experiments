import torch
import os
import logging
from transformers import BertForSequenceClassification, BertTokenizer
from ts.torch_handler.base_handler import BaseHandler

logger = logging.getLogger(__name__)

         
def list_model_files(directory):
    print(f"Model Directory: {directory}")
    print("\nFiles and subdirectories:")
    print(os.listdir(directory))

class TextClassifierHandler(BaseHandler):
    def initialize(self, context):
        """Loads the model and tokenizer"""
        properties = context.system_properties
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model_dir = properties.get("model_dir")  # Path where model artifacts are stored
        print(f"Model Directory: {model_dir}") 
        # Call the function
        list_model_files(model_dir)
                        
        model_path = os.path.join(model_dir, "pytorch_model.bin")
        config_path = os.path.join(model_dir, "config.json")
        tokenizer_path = os.path.join(model_dir, "vocab.txt")

        for path in [model_path, config_path, tokenizer_path]:
            if not os.path.exists(path):
                raise RuntimeError(f"Required file missing: {path}")

        # Load tokenizer and model
        self.tokenizer = BertTokenizer.from_pretrained(model_dir)
        self.model = BertForSequenceClassification.from_pretrained(model_dir)
        self.model.to(self.device)
        self.model.eval()

        logger.info("Model and tokenizer loaded successfully.")

    def preprocess(self, data):
        print("Preprocess", data)
        """Preprocesses the input text into tensors for inference."""
        texts = [item['text'] if 'text' in item else item['body']['text'] for item in data]
        print("preprocess1", texts)

        # Decode byte input if needed
        texts = [text.decode('utf-8') if isinstance(text, bytes) else text for text in texts]
        print("preprocess2", texts)

        inputs = self.tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
        inputs = {key: tensor.to(self.device) for key, tensor in inputs.items()}
        print("Processdone pre")
        return inputs

    def inference(self, inputs):
        print("Inference Start", inputs)
        """Runs the model on the preprocessed input."""
        with torch.no_grad():
            outputs = self.model(**inputs)
            predictions = torch.argmax(outputs.logits, dim=-1).tolist()
        print("Inference End",predictions)
        return predictions

    def postprocess(self, inference_output):
        print("Postprocess", inference_output)
        """Formats the model output for TorchServe response."""
        result = [{"prediction": pred} for pred in inference_output]
        print("Postprocess", result)
        return result

