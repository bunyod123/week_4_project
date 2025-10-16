import sys
sys.path.append(r"C:\Users\bunyo\OneDrive\Desktop\git_project\4_week_project")

from Source.data_loader import data_load
from Source.logger import get_logger



#----------------------------------------------------------------------------------------------
logger = get_logger("data_loading", 'data_loading.log')
path = r"C:\Users\bunyo\OneDrive\Desktop\git_project\4_week_project\Data\raw_data\cwur_2025_rankings.csv"


#---------------------------------------------------------------------------------------------------
try:
    df = data_load(path)
    logger.info('Data set script file orqali yuklandi')
except: 
    # Exception as e:
    logger.info("Muammo bor data yuklashda")
