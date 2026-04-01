from transformers import pipeline


class LLMExplainer:

    def __init__(self):
        pass

    def generate_explanation(self, transaction, prediction, retrieved_case):

        amount = transaction["amount"]
        location = transaction["location"]
        risk = prediction["risk_score"]
        is_fraud = prediction["is_fraud"]

        # FRAUD CASE
        if is_fraud:
            return (
                f"This transaction is flagged as risky because it involves a high amount of ${amount} "
                f"from {location}, with a risk score of {risk}. It matches known fraud patterns such as: "
                f"{retrieved_case}."
            )

        # SAFE CASE
        else:
            return (
                f"This transaction appears normal because the amount of ${amount} is relatively low "
                f"and does not match known fraud patterns. The risk score is {risk}, indicating low risk."
            )