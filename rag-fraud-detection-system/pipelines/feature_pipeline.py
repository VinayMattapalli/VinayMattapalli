def build_features(transaction):

    amount = transaction.get("amount", 0)
    location = transaction.get("location", "US")

    # Simulated velocity feature
    velocity = 1 if amount < 1000 else 5

    return {
        "amount": amount,
        "location": location,
        "velocity": velocity
    }