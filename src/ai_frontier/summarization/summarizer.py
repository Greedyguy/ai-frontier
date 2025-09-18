"""AI-powered summarization service."""

from abc import ABC, abstractmethod
from typing import Optional, List
import openai
from anthropic import Anthropic
import os

class BaseSummarizer(ABC):
    """Base class for summarization services."""

    @abstractmethod
    def summarize(self, text: str, max_length: int = 200) -> str:
        """Summarize the given text."""
        pass

    @abstractmethod
    def summarize_key_points(self, text: str) -> List[str]:
        """Extract key points from the text."""
        pass

    @abstractmethod
    def summarize_text(self, text: str) -> str:
        """Summarize general text (not necessarily academic abstract)."""
        pass

class OpenAISummarizer(BaseSummarizer):
    """OpenAI-powered summarizer."""

    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4o"):
        api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError(
                "OpenAI API key is required. Please set OPENAI_API_KEY environment variable "
                "or pass api_key parameter."
            )
        self.client = openai.OpenAI(api_key=api_key)
        self.model = model

    def summarize(self, text: str, max_length: int = 200) -> str:
        """Summarize text using OpenAI API."""
        prompt = f"""
        다음 학술 논문 초록을 약 {max_length}자 내외로 한국어로 간결하게 요약해주세요.
        주요 기여도, 방법론, 핵심 발견사항에 중점을 두어주세요.

        초록:
        {text}
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=800
        )

        return response.choices[0].message.content.strip()

    def summarize_key_points(self, text: str) -> List[str]:
        """Extract key points from the abstract."""
        prompt = f"""
        다음 학술 논문 초록에서 3-5개의 핵심 포인트를 한국어로 추출해주세요.
        각 포인트는 한 줄로 작성해주세요.

        초록:
        {text}
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=600
        )

        content = response.choices[0].message.content.strip()
        # Split by lines and clean up bullet points
        points = [line.strip().lstrip('•-*').strip()
                 for line in content.split('\n')
                 if line.strip()]

        return points

    def summarize_text(self, text: str) -> str:
        """Summarize general text using OpenAI API."""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": text}],
            temperature=0.5,
            max_tokens=500
        )

        return response.choices[0].message.content.strip()

class ClaudeSummarizer(BaseSummarizer):
    """Claude-powered summarizer."""

    def __init__(self, api_key: Optional[str] = None, model: str = "claude-sonnet-4-20250514"):
        api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError(
                "Anthropic API key is required. Please set ANTHROPIC_API_KEY environment variable "
                "or pass api_key parameter."
            )
        self.client = Anthropic(api_key=api_key)
        self.model = model

    def summarize(self, text: str, max_length: int = 200) -> str:
        """Summarize text using Claude API."""
        prompt = f"""
        다음 학술 논문 초록을 약 {max_length}자 내외로 한국어로 간결하게 요약해주세요.
        주요 기여도, 방법론, 핵심 발견사항에 중점을 두어주세요.

        초록:
        {text}
        """

        response = self.client.messages.create(
            model=self.model,
            max_tokens=800,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text.strip()

    def summarize_key_points(self, text: str) -> List[str]:
        """Extract key points from the abstract."""
        prompt = f"""
        다음 학술 논문 초록에서 3-5개의 핵심 포인트를 한국어로 추출해주세요.
        각 포인트는 한 줄로 작성해주세요.

        초록:
        {text}
        """

        response = self.client.messages.create(
            model=self.model,
            max_tokens=600,
            messages=[{"role": "user", "content": prompt}]
        )

        content = response.content[0].text.strip()
        # Split by lines and clean up bullet points
        points = [line.strip().lstrip('•-*').strip()
                 for line in content.split('\n')
                 if line.strip()]

        return points

    def summarize_text(self, text: str) -> str:
        """Summarize general text using Claude API."""
        response = self.client.messages.create(
            model=self.model,
            max_tokens=500,
            messages=[{"role": "user", "content": text}]
        )

        return response.content[0].text.strip()

def get_summarizer(provider: str = "openai") -> BaseSummarizer:
    """Get summarizer instance based on provider."""
    if provider.lower() == "openai":
        return OpenAISummarizer()
    elif provider.lower() == "claude":
        return ClaudeSummarizer()
    else:
        raise ValueError(f"Unsupported summarization provider: {provider}")