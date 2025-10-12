import pandas as pd

class data_load:

    def __init__(self, path : str):
        self.path = path

    def load(self):
        df = pd.read_csv(self.path)
        return df

#------------------------------------------------------
# import pandas as pd

# class DataLoader:
#     def __init__(self, path: str):
#         self.path = path

#     def load_data(self) -> pd.DataFrame:
#         """CSV faylni yuklash"""
#         try:
#             df = pd.read_csv(self.path)
#             print(f"[INFO] Dataset muvaffaqiyatli yuklandi: {self.path}")
#             return df
#         except Exception as e:
#             print(f"[ERROR] Fayl yuklanmadi: {e}")
#             return None