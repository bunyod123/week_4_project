import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
scaler = MinMaxScaler()
#-----------------------------------------------------------------------------

# logging qilishni sozlaymiz
from logger import get_logger
logger = get_logger('preprocessing jarayoni', 'preprocessing.log')

#---------------------------------------------------------------------------    
# class yaratamiz
class Preprocessing:
    def __init__(self, df):
        self.df = df.copy()
        self.encoder = LabelEncoder()
        self.scaler = MinMaxScaler()
        logger.info(f"Data Preprocessing boshlandi: {self.df.shape}")

#------------------------------------------------------------------------------
    # toliq Nan bolgan ustunni tashlab yuboramiz
    def dropColumn(self, column_name):
        try:
            if column_name in self.df.columns:
                self.df = self.df.drop(columns=[column_name],axis=1)
                logger.info(f"'{column_name}' ustuni tashlab yuborildi.")
            else:
                logger.warning(f"{column_name} ustuni topilmadi, tashlab yuborilmadi.")
            return self
        except Exception as e:
            logger.error(f"Ustunni ochirishda xatolik: {e}")
            raise e
    
#--------------------------------------------------------------------------------
    # Nan qiymatlarni toldirish
    def fillMissingValues(self):
        try:
            num_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
            lab_cols = self.df.select_dtypes(exclude=[np.number]).columns.tolist()
            
            # Imputer yaratamiz
            num_imputer = SimpleImputer(strategy='mean')
            lab_imputer = SimpleImputer(strategy='most_frequent')
            
            self.df[num_cols] = num_imputer.fit_transform(self.df[num_cols])
            self.df[lab_cols] = lab_imputer.fit_transform(self.df[lab_cols])
          
            logger.info("Nan qiymatlar toldirildi")
            return self
        except Exception as e:
            logger.error(f"Xatolik yuz berdi {e}")
    
#------------------------------------------------------------------------------
    # Encoding qilish
    def encoding(self):
        try:
            for col in self.df.columns:
                if self.df[col].dtype == 'object':
                    if self.df[col].nunique() <= 5:
                        dummies = pd.get_dummies(self.df[col], prefix=col, dtype=int)
                        self.df = pd.concat([self.df.drop(columns=[col]), dummies], axis=1)
                    else:
                        self.df[col] = self.encoder.fit_transform(self.df[col])
            logger.info("Encoding qilindi")
            return self
        except Exception as e:
            logger.error(f"Xatolikbor encoding qilishda {e}")
            raise e
    
#----------------------------------------------------------------------------------
    # Scaling qilish
    def scaling(self):
        try:

            num_cols = self.df.select_dtypes(include=[np.numbers]).columns.drop('Score').tolist()
            self.df[num_cols] = self.scaler.fit_transform(self.df[num_cols])

            logger.info("Scaling qilindi")
            return self
        
        except Exception as e:
            logger.error("Scaling qilishda muammo boldi")
            raise e
        
#-------------------------------------------------------------------------------
    # Log transforming
    def logTransformation(self):
        try:
            skewness = self.df.skew()
            features_log = skewness[skewness >= 0.5].index.tolist()
            for col in features_log:
                if (self.df[col] > 0).all():
                    self.df[col] = np.log1p(self.df[col])
            logger.info("Log transforming qilindi")
            return self
        except Exception as e:
            logger.error("Log tranform qilish da xatolik boldi")
            raise e
        
#-------------------------------------------------------------------------------        
    # Final data ni olish
    def getDataset(self):
        return self.df