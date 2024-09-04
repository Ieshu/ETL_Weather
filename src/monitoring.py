from src.utils import log_message

def monitor_pipeline(success):
    if success:
        log_message("ETL Pipeline ran successfully")
    else:
        log_message("ETL Pipeline failed", level="ERROR")
