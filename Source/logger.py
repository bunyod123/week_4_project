import logging
import os

def get_logger(name, log_file):
    os.makedirs("logs", exist_ok=True)
    path = os.path.join("logs", log_file)

    logging.basicConfig(
        filename=path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    return logging.getLogger(name)
