import os
import joblib
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)


class ModelTrainer:

    def __init__(self):

        self.models = {

            "Logistic Regression": LogisticRegression(
                max_iter=1000,
                random_state=42
            ),

            "Random Forest": RandomForestClassifier(
                n_estimators=200,
                random_state=42
            )

        }

    def train(
        self,
        X_train,
        y_train,
        X_test,
        y_test
    ):

        results = []

        best_auc = 0

        best_model = None

        best_model_name = None

        for name, model in self.models.items():

            model.fit(X_train, y_train)

            predictions = model.predict(X_test)

            probabilities = model.predict_proba(X_test)[:, 1]

            accuracy = accuracy_score(
                y_test,
                predictions
            )

            precision = precision_score(
                y_test,
                predictions
            )

            recall = recall_score(
                y_test,
                predictions
            )

            f1 = f1_score(
                y_test,
                predictions
            )

            roc_auc = roc_auc_score(
                y_test,
                probabilities
            )

            results.append({

                "Model": name,
                "Accuracy": round(accuracy, 4),
                "Precision": round(precision, 4),
                "Recall": round(recall, 4),
                "F1 Score": round(f1, 4),
                "ROC AUC": round(roc_auc, 4)

            })

            if roc_auc > best_auc:

                best_auc = roc_auc
                best_model = model
                best_model_name = name

        os.makedirs("models", exist_ok=True)

        joblib.dump(
            best_model,
            "models/best_model.pkl"
        )

        return {

            "results": pd.DataFrame(results),

            "best_model": best_model_name,

            "best_auc": round(best_auc, 4)

        }