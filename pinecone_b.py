import streamlit as st
from pinecone_plugins.assistant.models.chat import Message
from pinecone import Pinecone
import os

st.title("🤖 Pinecone Assistant")

# 🔑 Load Pinecone API key from Streamlit secrets
api_key = st.secrets["PINECONE_API_KEY"]
assistant_name = st.secrets["ASSISTANT_NAME"]

# Initialize Pinecone assistant
pc = Pinecone(api_key=api_key)
assistant = pc.assistant.Assistant(assistant_name=assistant_name)

# Text input for user query
query = st.text_input("Ask a question:")

if query:
    msg = Message(content=query)

    # Chat with assistant
    resp = assistant.chat(messages=[msg])
    st.write("**Assistant:**", resp["message"]["content"])

    # Optional: streaming response
    st.write("**Streaming response:**")
    chunks = assistant.chat(messages=[msg], stream=True)
    response_text = ""
    for chunk in chunks:
        if chunk and "message" in chunk and "content" in chunk["message"]:
            response_text += chunk["message"]["content"]
    st.write(response_text)
