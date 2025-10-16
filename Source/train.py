import pandas as pd
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR

from logger import get_logger
logger = get_logger('model_training', 'training.log')


class ModelTrainer:
    def __init__(self, X, y, k_folds=6):
        self.X = X
        self.y = y
        self.k_folds = k_folds
        logger.info(f"Training boshlandi: X={X.shape}, y={y.shape}, K={k_folds}")

        self.models = {
            "Linear Regression": LinearRegression(),
            "Decision Tree": DecisionTreeRegressor(random_state=99),
            "Random Forest": RandomForestRegressor(random_state=88),
            "SVR": SVR(),
            "Gradient Boosting": GradientBoostingRegressor(random_state=77)
        }

    def train_all(self):
        try:
            X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=99)
            logger.info("Dataset train/testga ajratildi")

            kf = KFold(n_splits=self.k_folds, shuffle=True, random_state=99)
            results = []

            for name, model in self.models.items():
                logger.info(f"{name} modeli oqitilmoqda:")

                # Cross validation (R2 score)
                cv_scores = cross_val_score(model, X_train, y_train, cv=kf, scoring='r2')
                avg_cv_r2 = cv_scores.mean()

                model.fit(X_train, y_train)
                preds = model.predict(X_test)

                r2 = r2_score(y_test, preds)
                mae = mean_absolute_error(y_test, preds)

                results.append({
                    "Model": name,
                    "CV R2 (avg)": round(avg_cv_r2, 4),
                    "Test R2": round(r2, 4),
                    "Test MAE": round(mae, 4)
                })

                logger.info(
                    f"{name} -> CV R2(avg): {avg_cv_r2:.3f} | Test R2: {r2:.3f} | MAE: {mae:.3f}"
                )

            results_df = pd.DataFrame(results)
            logger.info("Barcha modellar K-Fold bilan baholandi.")
            return results_df

        except Exception as e:
            logger.error(f"Training jarayonida xatolik: {str(e)}")
            raise e
