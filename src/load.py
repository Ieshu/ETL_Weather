import json
import os
from src.utils import log_message, read_config

def load_data(data, stage="final"):
    log_message(f"Starting data load to {stage} stage...")
    config = read_config()
    file_path = config['file_paths'][f'{stage}_data']
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        json.dump(data, f)
    log_message(f"Data loaded successfully to {file_path}")
