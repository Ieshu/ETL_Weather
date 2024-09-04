import requests
from src.utils import log_message, read_config

def extract_data():
    config = read_config()
    url = config['api']['url']
    log_message("Starting data extraction...")
    response = requests.get(url)
    if response.status_code == 200:
        log_message("Data extracted successfully")
        return response.json()
    else:
        log_message("Failed to extract data", level="ERROR")
        return None
