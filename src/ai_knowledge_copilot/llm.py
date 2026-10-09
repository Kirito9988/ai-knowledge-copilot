from google import genai
from google.genai import types

from ai_knowledge_copilot.config import get_settings


SYSTEM_INSTRUCTIONS = """
You are an AI knowledge assistant.

Your job is to give accurate, concise, and useful answers.

When you are unsure about something, clearly say that you are unsure.
Do not invent facts.
"""


class LLMService:
    def __init__(self) -> None:
        settings = get_settings()

        self.client = genai.Client(
            api_key=settings.gemini_api_key,
        )

        self.model = settings.model_name

    def generate(self, user_message: str) -> str:
        if not user_message.strip():
            raise ValueError("User message cannot be empty.")

        response = self.client.models.generate_content(
            model=self.model,
            contents=user_message,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTIONS,
            ),
        )

        if not response.text:
            raise RuntimeError("The model returned an empty response.")

        return response.text.strip()