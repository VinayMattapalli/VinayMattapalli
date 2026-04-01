import numpy as np
from sklearn.ensemble import RandomForestClassifier


class FraudModel:

    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100)
        self._train_model()

    def _train_model(self):
        np.random.seed(42)

        data = []
        labels = []

        # NORMAL TRANSACTIONS
        for _ in range(500):
            amount = np.random.randint(1, 1000)
            location = 0  # US
            velocity = np.random.randint(1, 3)

            data.append([amount, location, velocity])
            labels.append(0)

        # FRAUD TRANSACTIONS
        for _ in range(500):
            amount = np.random.randint(2000, 10000)
            location = np.random.choice([0, 1])  # US or international
            velocity = np.random.randint(3, 10)

            data.append([amount, location, velocity])
            labels.append(1)

        X = np.array(data)
        y = np.array(labels)

        self.model.fit(X, y)

    def predict(self, features):

        amount = features["amount"]
        location = 1 if features["location"] != "US" else 0
        velocity = features.get("velocity", 1)

        data = np.array([[amount, location, velocity]])

        probability = self.model.predict_proba(data)[0][1]

        # HYBRID LOGIC (ML + RULES)
        is_fraud = probability > 0.7

        # Business rule override
        if amount < 100:
            is_fraud = False

        return {
            "risk_score": round(float(probability), 2),
            "is_fraud": bool(is_fraud)
        }