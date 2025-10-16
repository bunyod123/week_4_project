import pandas as pd
import sys,os
sys.path.append(r"C:\Users\bunyo\OneDrive\Desktop\git_project\4_week_project")

#-----------------------------------------------------------------------------------------
from Source.logger import get_logger
logger = get_logger("data loader", "data_loading.log")

logger.info("Data yuklash boshqlandi.")


#------------------------------------------------------------------------------------------
# data koad uchun class yaratamiz
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
#-----------------------------------------------------------------------------------------