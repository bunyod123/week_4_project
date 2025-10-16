import sys,os
import pandas as pd
from Source.preprocessing import Preprocessing
from Source.logger import get_logger
#----------------------------------------------------------------------------------------------

sys.path.append(r"C:\Users\bunyo\OneDrive\Desktop\git_project\4_week_project")
logger = get_logger('use_preprocessing', 'preprocessing.log')

#------------------------------------------------------------------------------------------------
# Dataset yuklash
df = pd.read_csv('data/dataset.csv')
logger.info(f"Dataset yuklandi: {df.shape}")


#--------------------------------------------------------------------------------------------------
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


logger.info(f"Preprocessing tugadi. Shape: {df_clean.shape}")

#--------------------------------------------------------------------------------------------------
# faylni saqlaymiz
path = r"C:\Users\bunyo\OneDrive\Desktop\git_project\4_week_project\Data\preprocessed_data"
output_dir = os.path.join(path, "preprocessed")
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "cleaned_dataset.csv")
df_clean.to_csv(output_path, index=False)

logger.info(f"Tozalangan dataset saqlandi: {output_path}")
print(f"Fayl saqlandi: {output_path}")
#----------------------------------------------------------------------------------------------------