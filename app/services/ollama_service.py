import json
import httpx

from app.core.settings import settings


class OllamaService:

    def __init__(self):
        self.base_url = settings.OLLAMA_URL
        self.model = settings.OLLAMA_MODEL

    def generate_json(self, system_prompt: str, user_prompt: str):

        payload = {
            "model": self.model,
            "format": "json",
            "stream": False,
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        }

        response = httpx.post(
            f"{self.base_url}/api/chat",
            json=payload,
            timeout=300
        )

        response.raise_for_status()

        content = response.json()["message"]["content"]

        return json.loads(content)