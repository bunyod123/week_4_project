import logging
import os

def get_logger(name, log_file):
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_dir = os.path.join(base_dir, "logs")
    os.makedirs(log_dir, exist_ok=True)

    path = os.path.join(log_dir, log_file)

    logging.basicConfig(
        filename=path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    return logging.getLogger(name)
