RAG-Based Fraud Detection System

Overview

This project implements a real-time fraud detection system using a hybrid approach that combines machine learning with Retrieval-Augmented Generation (RAG). The system evaluates transaction data, generates a risk score, retrieves similar historical patterns using vector search, and produces an explainable decision output.

The goal is to simulate how modern fintech platforms detect and explain potentially fraudulent transactions in real time.

---

System Architecture

The system follows a modular pipeline:

- Data Ingestion  
  Accepts transaction input via REST API or chat interface  

- Feature Engineering  
  Transforms raw transaction data into model-ready features  

- Machine Learning Model  
  Uses a Random Forest classifier to generate fraud risk scores  

- Vector Search (FAISS)  
  Retrieves similar transaction patterns from a vector database  

- RAG Layer  
  Combines model output with retrieved context to generate explanations  

- API Layer  
  Exposes endpoints using FastAPI for prediction and chat-based interaction  

- UI Layer  
  Provides an interactive chat interface using Gradio  

---

Key Features

- Real-time fraud prediction using machine learning  
- Hybrid decision system combining ML and rule-based logic  
- Retrieval-based context using FAISS vector search  
- Dynamic, human-readable explanations for each prediction  
- Interactive chat interface for querying fraud scenarios  
- Modular and scalable architecture  

---

Tech Stack

- Python  
- FastAPI  
- Scikit-learn (Random Forest)  
- FAISS (Vector Search)  
- Sentence Transformers  
- Gradio (UI)  

---

API Endpoints

POST /predict  
Accepts transaction data and returns fraud prediction with explanation  

Example Request:
{
  "amount": 40000,
  "location": "US"
}

POST /chat  
Accepts natural language queries and returns fraud analysis  

Example Request:
{
  "user_query": "fraud pattern for 40000"
}

---

How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Start backend:
uvicorn main:app --reload

3. Run UI:
python ui/app.py

4. Open in browser:
http://127.0.0.1:7860

---

Example Output

- High-value transaction:
  Flagged as fraud with high risk score and matching historical pattern  

- Low-value transaction:
  Classified as safe with low risk score and normal behavior explanation  

---

Project Structure

rag-fraud-detection-system/
│
├── api/                 # API routes
├── models/              # ML model, vector store, explanation logic
├── pipelines/           # Feature engineering
├── ui/                  # Gradio interface
├── main.py              # FastAPI entry point
├── requirements.txt
└── README.md

---

Future Enhancements

- Integration with real transaction datasets  
- Real-time streaming using Kafka  
- Deployment using Docker and cloud platforms  
- Monitoring and logging for model performance  
- Advanced LLM-based explanations  

---

Summary

This project demonstrates a production-style fraud detection system by combining machine learning, vector search, and explainable AI techniques into a unified pipeline. It highlights how modern systems use both predictive models and contextual retrieval to improve decision-making and transparency.