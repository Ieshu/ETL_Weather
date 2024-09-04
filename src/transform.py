from src.utils import log_message

def transform_data(data):
    log_message("Starting data transformation...")
    transformed_data = {
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'weather': data['weather'][0]['description'],
        'city': data['name'],
        'timestamp': data['dt']
    }
    log_message("Data transformation complete")
    return transformed_data
