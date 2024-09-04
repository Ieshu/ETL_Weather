from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data
from src.validation import validate_data
from src.monitoring import monitor_pipeline
from src.parallel_processing import parallel_process_data

def run_pipeline():
    data = extract_data()
    if not data:
        monitor_pipeline(success=False)
        return

    transformed_data = transform_data(data)
    
    if not validate_data(transformed_data):
        monitor_pipeline(success=False)
        return
    
    chunks = [transformed_data]  # For parallel processing example
    processed_chunks = parallel_process_data(chunks)
    
    for chunk in processed_chunks:
        load_data(chunk, stage="processed")

    load_data(transformed_data, stage="final")
    monitor_pipeline(success=True)
