import sys

sys.path.append(r"C:\Users\bunyo\OneDrive\Desktop\git_project\4_week_project")


import pandas as pd
from Source.preprocessing import Preprocessing
from Source.logger import get_logger

logger = get_logger('use_preprocessing', 'preprocessing.log')

# Dataset yuklash
df = pd.read_csv('data/dataset.csv')
logger.info(f"Dataset yuklandi: {df.shape}")

# Preprocessing obyekt yaratish
pre = Preprocessing(df)

df_clean = (
    pre.dropColumn('World Rank')    
       .fillMissingValues()
       .encoding()
       .scaling()
       .logTransformation()
       .getDataset()
)