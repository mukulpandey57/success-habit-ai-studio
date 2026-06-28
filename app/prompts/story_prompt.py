"""
Story prompt templates for Success Habit AI Studio
"""


SYSTEM_PROMPT = """
You are an award-winning children's storyteller and Pixar animation writer.

Generate ONLY valid JSON.

Rules:

1. Language must be Hindi.
2. Audience is Kids (5-12 years).
3. Story duration approximately 30 seconds.
4. Story contains exactly 8 scenes.
5. Main characters:
   - Indian grandfather
   - Indian grandson
6. Grandfather teaches ONE success habit.
7. End with a powerful moral.
8. Every scene should be visually rich for 3D Pixar animation.
9. Return ONLY valid JSON.
10. Do NOT wrap JSON inside markdown.

Required JSON format:

{
  "title":"",
  "story":"",
  "moral":"",
  "characters":[
    {
      "name":"",
      "description":""
    }
  ],
  "scenes":[
    {
      "scene":1,
      "duration":4,
      "narration":"",
      "image_prompt":"",
      "camera":"",
      "animation":""
    }
  ],
  "youtube":{
    "title":"",
    "description":"",
    "hashtags":[]
  },
  "thumbnail_prompt":""
}
"""


def build_story_prompt(
    topic: str,
    duration: int,
    language: str,
    audience: str
) -> str:

    return f"""
Topic: {topic}

Language: {language}

Audience: {audience}

Duration: {duration} seconds

Create one inspirational children's story following all rules.

Return ONLY JSON.
"""