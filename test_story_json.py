from app.prompts.story_prompt import SYSTEM_PROMPT, build_story_prompt
from app.services.ollama_service import OllamaService

service = OllamaService()

result = service.generate_json(
    SYSTEM_PROMPT,
    build_story_prompt(
        topic="Success Habit",
        duration=40,
        language="Hindi",
        audience="Kids"
    )
)

print(result)