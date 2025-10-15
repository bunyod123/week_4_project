<<<<<<< HEAD
import logging
import os

def get_logger(name: str, log_file: str = "project.log"):
    # log fayllar uchun papka
    os.makedirs("logs", exist_ok=True)
    log_path = os.path.join("logs", log_file)

    # logging konfiguratsiyasi — faqat bir marta yaratiladi
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        handlers=[
            logging.FileHandler(log_path, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )

    # har bir modul uchun o‘z nomli logger
    logger = logging.getLogger(name)
    return logger
=======
import logging
import os

def get_logger(name: str, log_file: str = "project.log"):
    # log fayllar uchun papka
    os.makedirs("logs", exist_ok=True)
    log_path = os.path.join("logs", log_file)

    # logging konfiguratsiyasi — faqat bir marta yaratiladi
    logging.basicConfig(
        level=logging.INFO,

        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",

        handlers=[ logging.FileHandler(log_path, encoding='utf-8'),]
    )

    # har bir modul uchun o‘z nomli logger
    logger = logging.getLogger(name)
    return logger
>>>>>>> 42b013ea48d0025ff1955e22c1845b09becce627
