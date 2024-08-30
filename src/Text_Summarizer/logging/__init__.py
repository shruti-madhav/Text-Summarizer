import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(messages)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.mkdir(log_dir, exist_ok=True)


logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  # for logging in the logs file
        logging.StreamHandler(sys.stdout)   # for printing on the terminal
    ]
)

logger = logging.getLogger("Text_Summarizer_Logger")