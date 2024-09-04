from src.utils import log_message

def validate_data(data):
    log_message("Starting data validation...")
    if data and 'temperature' in data and 'humidity' in data:
        log_message("Data validation successful")
        return True
    else:
        log_message("Data validation failed", level="ERROR")
        return False
