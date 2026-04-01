from fastapi import APIRouter
from pydantic import BaseModel
from models.fraud_model import FraudModel
from pipelines.feature_pipeline import build_features
from models.vector_store import VectorStore
from models.llm_explainer import LLMExplainer

router = APIRouter()

# Load once (important for performance)
model = FraudModel()
vector_store = VectorStore()
llm = LLMExplainer()


# Input schema
class Transaction(BaseModel):
    amount: float
    location: str = "US"


# Health check
@router.get("/")
def health():
    return {"message": "API running"}


# ✅ MAIN PREDICT API
@router.post("/predict")
async def predict(transaction: Transaction):

    # Step 1: Features
    features = build_features(transaction.dict())

    # Step 2: ML Prediction
    result = model.predict(features)

    # Step 3: Retrieval
    query_text = f"Transaction amount {features['amount']} from {features['location']}"
    retrieved_case = vector_store.search(query_text)

    # Step 4: LLM Explanation
    explanation = llm.generate_explanation(
        transaction.dict(),
        result,
        retrieved_case
    )

    # ✅ IMPORTANT RETURN (this was missing)
    return {
        "input": transaction.dict(),
        "prediction": result,
        "retrieved_case": retrieved_case,
        "llm_explanation": explanation if explanation else "Explanation not generated"
    }


# ✅ CHAT ENDPOINT (INTERACTIVE RAG)
class ChatRequest(BaseModel):
    user_query: str

@router.post("/chat")
async def chat(request: ChatRequest):
   # Try to extract amount from user query
    import re

    user_query = request.user_query
    match = re.search(r'\d+', user_query)
    amount = int(match.group()) if match else 0

    transaction = {
    "amount": amount,
    "location": "US"
    }

    features = build_features(transaction)
    result = model.predict(features)

    query_text = f"Transaction amount {features['amount']} from {features['location']}"
    retrieved_case = vector_store.search(query_text)

    explanation = llm.generate_explanation(
        transaction,
        result,
        retrieved_case
    )

    return {
        "user_query": user_query,
        "retrieved_case": retrieved_case,
        "response": explanation if explanation else "No explanation generated"
    }