#----------------------------------------------------------------------------------------
import sys,os
sys.path.append(r"C:\Users\bunyo\OneDrive\Desktop\git_project\4_week_project")

#----------------------------------------------------------------------------------------
from Source.train import ModelTrainer
import pandas as pd

#---------------------------------------------------------------------------------------

# Datasetni yuklash
df = pd.read_csv('data/preprocessed/preprocessed_house_price_prediction.csv')

# target ustunni belgilang
X = df.drop('target', axis=1)
y = df['target']

trainer = ModelTrainer(X, y, k_folds=6)
results = trainer.train_all()

print(results)
