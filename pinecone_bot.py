
from pinecone import Pinecone, ServerlessSpec
from pinecone_plugins.assistant.models.chat import Message
import os

# 🔑 Initialize Pinecone client
pc = Pinecone(api_key="pcsk_6EnhoS_BiziddFgAFadxbim2V5VLYtegi9ho28bCgjgcSfZrYBJUkkSuDfXFTBpL3DiXMg")  # replace with your Pinecone API key





# 🔹 Connect to your existing assistant
assistant = pc.assistant.Assistant(assistant_name="test")

# 💬 Ask a question
msg = Message(content="whats the education?")
resp = assistant.chat(messages=[msg])
print("Assistant Response:", resp["message"]["content"])

# 🔄 Streaming response
chunks = assistant.chat(messages=[msg], stream=True)
print("\nStreaming Response:")
for chunk in chunks:
    if chunk is None:
        continue
    # Check if 'message' key exists
    if "message" in chunk and "content" in chunk["message"]:
        print(chunk["message"]["content"], end="", flush=True)