from app.services.ollama_service import OllamaService

service = OllamaService()

result = service.generate(
    "Say Hello from Ollama."
)

print(result)