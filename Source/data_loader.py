from logger import get_logger
logger = get_logger("data loader", "data_loading.log")

logger.info("Data yuklash boshqlandi.")


import pandas as pd

class data_load:

    def __init__(self, path : str):
        self.path = path

    def load(self):
        try:
            df = pd.read_csv(self.path)
            logger.info("Dataset yuklandi")
            return df
        except Exception as e:
            logger.info(f"Data yuklanmadi {e}")