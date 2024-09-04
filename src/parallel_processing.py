from concurrent.futures import ThreadPoolExecutor
from src.utils import log_message

def parallel_process_data(data_chunks):
    log_message("Starting parallel processing...")
    with ThreadPoolExecutor(max_workers=4) as executor:
        processed_chunks = list(executor.map(process_chunk, data_chunks))
    log_message("Parallel processing complete")
    return processed_chunks

def process_chunk(chunk):
    # Example processing logic for a data chunk
    return {k: v for k, v in chunk.items()}
