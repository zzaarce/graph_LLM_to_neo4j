import requests
from config import AZURE_OPENAI_API_KEY

def get_azure_openai_response(prompt):
    url = "https://YOUR_AZURE_OPENAI_ENDPOINT/openai/deployments/YOUR_DEPLOYMENT_ID/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AZURE_OPENAI_API_KEY}"
    }
    data = {
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 100,
        "temperature": 0.5
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error in Azure API call:", response.status_code, response.text)
        return None
