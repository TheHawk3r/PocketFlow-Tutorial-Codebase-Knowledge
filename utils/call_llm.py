import requests
from termcolor import cprint
import json

# Configurează conexiunea către LM Studio local
local_api_url = "http://127.0.0.1:1234/v1/completions"  # Adresa corectă pentru serverul tău local
api_key = "gemma-3-27b-it"  # Dacă ai nevoie de un API key pentru acces

def call_llm(prompt: str, use_cache: bool = False):
    cprint("[Querying local LLM via LM Studio]", "cyan")
    try:
        # Setează datele pentru cererea POST
        data = {
            "model": "gemma-3-27b-it",  # Modelul specificat în LM Studio
            "prompt": prompt,
            "max_tokens": 100,  # Poți ajusta acest parametru
            "temperature": 0.7,  # Poți ajusta acest parametru
        }

        # Setează antetul pentru cererea POST
        headers = {
            "Authorization": f"Bearer {api_key}",  # Dacă API key-ul este necesar
            "Content-Type": "application/json"
        }

        # Trimite cererea POST către LM Studio local
        response = requests.post(local_api_url, headers=headers, data=json.dumps(data))

        # Verifică dacă cererea a avut succes
        if response.status_code == 200:
            result = response.json()
            response_text = result.get("choices")[0].get("text").strip()  # Extrage răspunsul din JSON
            return response_text
        else:
            cprint(f"[Error calling LM Studio] {response.status_code}: {response.text}", "red")
            return "[Error calling LLM]"

    except Exception as e:
        cprint(f"[Error calling LM Studio] {e}", "red")
        return "[Error calling LLM]"
