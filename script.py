# Load environment variables
import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

# Add OpenAI import
import openai

# Set OpenAI configuration settings
openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OAI_ENDPOINT")
openai.api_version = "2023-03-15-preview"
openai.api_key = os.getenv("AZURE_OAI_KEY")

prompt = ""

# build the messages
session_chats = [
    { "role": "system", "content": "You are a helpful assistant. Summarize the following text in 60 words or less." },
]

while prompt!="exit":
    prompt = input("Prompt: ")
    session_chats.append({ "role": "user", "content": prompt })
    # Send request to Azure OpenAI model
    try:
        print("\n\nSending request for summary to Azure OpenAI endpoint...")
        response = openai.ChatCompletion.create(
            engine=os.getenv("AZURE_OAI_MODEL"),
            temperature=0.7,
            max_tokens=120,
            messages=session_chats
        )
        print("Response: " + response.choices[0].message.content + "\n")
        session_chats.append({ "role": "assistant", "content": response.choices[0].message.content })
    except ValueError:
        print("Oops! Something went wrong!")