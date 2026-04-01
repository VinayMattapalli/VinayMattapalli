from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="RAG Fraud Detection System")

# include all routes from routes.py
app.include_router(router)

# root endpoint (just health check)
@app.get("/")
def root():
    return {"message": "RAG Fraud Detection System Running"}