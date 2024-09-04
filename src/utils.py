import yaml
import logging

def read_config():
    with open('config/config.yaml', 'r') as file:
        return yaml.safe_load(file)

def log_message(message, level="INFO"):
    logging.basicConfig(filename='logs/etl.log', level=logging.INFO)
    if level == "INFO":
        logging.info(message)
    elif level == "ERROR":
        logging.error(message)
