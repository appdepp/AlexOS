import requests

from app.core.config import DEFAULT_MODEL, OLLAMA_URL, TEMPERATURE


class LLMManager:
    def __init__(self, model: str = DEFAULT_MODEL):
        self.model = model

    def chat(self, messages: list[dict]) -> str:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": self.model,
                "messages": messages,
                "stream": False,
                "options": {
                    "temperature": TEMPERATURE
                }
            },
            timeout=300
        )

        response.raise_for_status()
        return response.json()["message"]["content"]
