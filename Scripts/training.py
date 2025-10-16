#----------------------------------------------------------------------------------------
import sys,os
sys.path.append(r"C:\Users\bunyo\OneDrive\Desktop\git_project\4_week_project")

#----------------------------------------------------------------------------------------
from Source.train import ModelTrainer
import pandas as pd

#---------------------------------------------------------------------------------------

# Datasetni yuklash
df = pd.read_csv(r"C:\Users\bunyo\OneDrive\Desktop\git_project\4_week_project\Data\preprocessed_data\preprocessed_data.joblib")


X = df.drop('Score', axis=1)
y = df['Score']

trainer = ModelTrainer(X, y, k_folds=6)
results = trainer.train_all()

print(results)
