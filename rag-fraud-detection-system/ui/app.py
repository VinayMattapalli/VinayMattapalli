import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000/chat"


def chat_fn(message, history):
    try:
        response = requests.post(API_URL, json={"user_query": message})
        data = response.json()
        return data.get("response", "No response from model")
    except:
        return "Error connecting to backend"


demo = gr.ChatInterface(
    fn=chat_fn,
    title="AI Fraud Detection Assistant",
    description="Ask about fraud patterns, transactions, or risk signals."
)

demo.launch()