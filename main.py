import os
import requests
from dotenv import load_dotenv  # Add this import

# Load environment variables from .env file
load_dotenv()

# Get your Azure OpenAI endpoint and API key from environment variables
AZURE_OPENAI_ENDPOINT = os.getenv("ENDPOINT_URL")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
DEPLOYMENT_NAME = os.getenv("DEPLOYMENT_NAME")  # e.g., "gpt-35-turbo"

# Check for missing environment variables
if not AZURE_OPENAI_ENDPOINT or not AZURE_OPENAI_API_KEY or not DEPLOYMENT_NAME:
    raise EnvironmentError(
        "Missing one or more required environment variables: "
        "AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY, AZURE_OPENAI_DEPLOYMENT_NAME"
    )

def ask_azure_openai(prompt):
    url = f"{AZURE_OPENAI_ENDPOINT}openai/deployments/{DEPLOYMENT_NAME}/chat/completions?api-version=2024-02-15-preview"
    headers = {
        "api-key": AZURE_OPENAI_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

if __name__ == "__main__":
    prompt = "How do I cook spaghetti bolognese?"
    answer = ask_azure_openai(prompt)
    print("Azure OpenAI response:", answer)