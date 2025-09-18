"""AI-powered translation service."""

from abc import ABC, abstractmethod
from typing import Optional
import openai
from anthropic import Anthropic
import os

class BaseTranslator(ABC):
    """Base class for translation services."""

    @abstractmethod
    def translate(self, text: str, target_language: str = "ko") -> str:
        """Translate text to target language."""
        pass

class OpenAITranslator(BaseTranslator):
    """OpenAI-powered translator."""

    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4o"):
        api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError(
                "OpenAI API key is required. Please set OPENAI_API_KEY environment variable "
                "or pass api_key parameter."
            )
        self.client = openai.OpenAI(api_key=api_key)
        self.model = model

    def translate(self, text: str, target_language: str = "ko") -> str:
        """Translate text using OpenAI API."""
        language_map = {
            "ko": "Korean",
            "en": "English",
            "ja": "Japanese",
            "zh": "Chinese"
        }

        target_lang_name = language_map.get(target_language, target_language)

        prompt = f"""
        Please translate the following text to {target_lang_name}.
        Maintain the academic tone and technical terminology appropriately.

        Text to translate:
        {text}
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        return response.choices[0].message.content.strip()

class ClaudeTranslator(BaseTranslator):
    """Claude-powered translator."""

    def __init__(self, api_key: Optional[str] = None, model: str = "claude-sonnet-4-20250514"):
        api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError(
                "Anthropic API key is required. Please set ANTHROPIC_API_KEY environment variable "
                "or pass api_key parameter."
            )
        self.client = Anthropic(api_key=api_key)
        self.model = model

    def translate(self, text: str, target_language: str = "ko") -> str:
        """Translate text using Claude API."""
        language_map = {
            "ko": "Korean",
            "en": "English",
            "ja": "Japanese",
            "zh": "Chinese"
        }

        target_lang_name = language_map.get(target_language, target_language)

        prompt = f"""
        Please translate the following academic text to {target_lang_name}.
        Maintain the academic tone and preserve technical terminology appropriately.

        Text to translate:
        {text}
        """

        response = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text.strip()

def get_translator(provider: str = "openai") -> BaseTranslator:
    """Get translator instance based on provider."""
    if provider.lower() == "openai":
        return OpenAITranslator()
    elif provider.lower() == "claude":
        return ClaudeTranslator()
    else:
        raise ValueError(f"Unsupported translation provider: {provider}")