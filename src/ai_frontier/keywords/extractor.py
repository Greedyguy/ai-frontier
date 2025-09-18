"""Keyword extraction service using LLM."""

import os
import logging
import json
from typing import List, Dict, Any, Optional
import openai
from openai import OpenAI

from ..prompts.templates import PromptManager


class KeywordExtractor:
    """LLM을 이용한 카테고리화된 키워드 추출 서비스"""

    def __init__(self, provider: str = "openai", model: str = None):
        self.provider = provider.lower()
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.prompt_manager = PromptManager()

        if self.provider == "openai":
            self.api_key = os.getenv("OPENAI_API_KEY")
            if not self.api_key:
                raise ValueError("OPENAI_API_KEY environment variable is required")

            self.client = OpenAI(api_key=self.api_key)
            self.model = model or "gpt-4o"

        else:
            raise ValueError(f"Unsupported provider: {provider}")

        self.logger.info(f"KeywordExtractor initialized with provider: {provider}, model: {self.model}")

    def extract_keywords(self, title: str, abstract: str) -> Dict[str, List[str]]:
        """논문 제목과 초록에서 카테고리화된 키워드를 추출합니다.

        Returns:
            Dict with categorized keywords:
            {
                "broad_technical": ["LLM", "RAG"],
                "specific_connectable": ["Multimodal RAG"],
                "unique_technical": ["ColPali"],
                "evolved_concepts": ["Multi-agent RAG"]
            }
        """
        try:
            self.logger.debug(f"카테고리화된 키워드 추출 시작 - 제목: {title[:50]}...")

            # 프롬프트 생성
            prompt = self.prompt_manager.generate_prompt(
                "keyword_extraction",
                title=title,
                abstract=abstract
            )

            # LLM 호출
            if self.provider == "openai":
                keywords = self._extract_with_openai(prompt)
            else:
                raise ValueError(f"Unsupported provider: {self.provider}")

            self.logger.debug(f"카테고리화된 키워드 추출 완료: {keywords}")
            return keywords

        except Exception as e:
            self.logger.error(f"키워드 추출 실패: {str(e)}")
            # 실패 시 기본 키워드 반환
            return self._extract_fallback_keywords(title, abstract)

    def extract_keywords_legacy(self, title: str, abstract: str) -> List[str]:
        """레거시 지원을 위한 평면 키워드 리스트 반환"""
        categorized = self.extract_keywords(title, abstract)

        # 모든 카테고리의 키워드를 평면 리스트로 변환
        all_keywords = []
        for category_keywords in categorized.values():
            all_keywords.extend(category_keywords)

        return all_keywords[:5]  # 최대 5개로 제한

    def _extract_with_openai(self, prompt: str) -> Dict[str, List[str]]:
        """OpenAI API를 이용한 카테고리화된 키워드 추출"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "당신은 연구 트렌드 분석을 위한 키워드 추출 전문가입니다. 정확한 JSON 형태로만 응답해주세요. 특수문자나 백슬래시를 사용하지 말고, 키워드에는 영문자, 숫자, 공백, 하이픈만 사용해주세요."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                max_tokens=300,
                temperature=0.2,
                top_p=1.0
            )

            keywords_text = response.choices[0].message.content.strip()
            self.logger.debug(f"Raw API response: {keywords_text}")

            # JSON 파싱하여 카테고리화된 키워드 추출
            keywords = self._parse_categorized_keywords(keywords_text)

            return keywords

        except Exception as e:
            self.logger.error(f"OpenAI API 호출 실패: {str(e)}")
            raise

    def _parse_categorized_keywords(self, keywords_text: str) -> Dict[str, List[str]]:
        """JSON 형태의 카테고리화된 키워드 텍스트를 파싱"""
        try:
            # JSON 파싱 전 전처리 - 잘못된 escape 문자 정리
            cleaned_text = self._preprocess_json_text(keywords_text)

            # JSON 파싱 시도
            keywords_json = json.loads(cleaned_text)

            # 예상 카테고리 키 검증
            expected_keys = {"broad_technical", "specific_connectable", "unique_technical", "evolved_concepts"}

            result = {}
            total_keywords = 0

            for key in expected_keys:
                if key in keywords_json and isinstance(keywords_json[key], list):
                    # 키워드 정리 및 제한
                    cleaned = self._clean_keyword_list(keywords_json[key])
                    # 각 카테고리당 최대 2개
                    result[key] = cleaned[:2]
                    total_keywords += len(result[key])
                else:
                    result[key] = []

            # 전체 키워드 수가 5개를 초과하면 조정
            if total_keywords > 5:
                result = self._limit_total_keywords(result, 5)

            self.logger.debug(f"Parsed categorized keywords: {result}")
            return result

        except json.JSONDecodeError as e:
            self.logger.warning(f"JSON 파싱 실패, 대체 파싱 시도: {e}")
            self.logger.debug(f"Failed JSON text: {repr(cleaned_text)}")
            return self._parse_keywords_fallback(keywords_text)

    def _preprocess_json_text(self, text: str) -> str:
        """JSON 파싱 전 텍스트 전처리"""
        import re

        # 잘못된 escape 문자 수정
        # \n, \t, \\, \", \' 등 유효한 escape는 유지하고 잘못된 것만 수정

        # 1. 먼저 유효한 JSON 부분만 추출 (```json 블록이 있는 경우)
        json_match = re.search(r'```json\s*(.*?)\s*```', text, re.DOTALL)
        if json_match:
            text = json_match.group(1)

        # 2. 또는 중괄호로 둘러싸인 JSON 부분만 추출
        elif '{' in text and '}' in text:
            start = text.find('{')
            end = text.rfind('}')
            if start != -1 and end != -1 and end > start:
                text = text[start:end+1]

        # 3. 잘못된 escape 문자 처리
        # 유효하지 않은 \문자 앞에 추가 \를 붙여서 올바른 escape로 만들기
        # 단, 이미 유효한 escape 문자(\n, \t, \\, \", \/, \b, \f, \r, \u)는 유지

        # 유효한 escape 문자를 임시로 치환
        text = text.replace('\\n', '\x00NEWLINE\x00')
        text = text.replace('\\t', '\x00TAB\x00')
        text = text.replace('\\\\', '\x00BACKSLASH\x00')
        text = text.replace('\\"', '\x00QUOTE\x00')
        text = text.replace('\\/', '\x00SLASH\x00')
        text = text.replace('\\b', '\x00BACKSPACE\x00')
        text = text.replace('\\f', '\x00FORMFEED\x00')
        text = text.replace('\\r', '\x00CARRIAGE\x00')

        # 유니코드 escape (\uXXXX) 처리
        text = re.sub(r'\\u[0-9a-fA-F]{4}', lambda m: m.group(0).replace('\\', '\x00UNICODE\x00'), text)

        # 남은 모든 \ 문자를 \\로 교체
        text = text.replace('\\', '\\\\')

        # 임시 치환한 것들을 원래대로 복원
        text = text.replace('\x00NEWLINE\x00', '\\n')
        text = text.replace('\x00TAB\x00', '\\t')
        text = text.replace('\x00BACKSLASH\x00', '\\\\')
        text = text.replace('\x00QUOTE\x00', '\\"')
        text = text.replace('\x00SLASH\x00', '\\/')
        text = text.replace('\x00BACKSPACE\x00', '\\b')
        text = text.replace('\x00FORMFEED\x00', '\\f')
        text = text.replace('\x00CARRIAGE\x00', '\\r')
        text = text.replace('\x00UNICODE\x00', '\\')

        return text.strip()

    def _clean_keyword_list(self, keywords: List[str]) -> List[str]:
        """키워드 리스트 정리"""
        cleaned = []
        for kw in keywords:
            if isinstance(kw, str):
                # 앞뒤 공백 및 불필요한 문자 제거
                kw = kw.strip('\'".,;()[]{}!')
                if kw and len(kw) > 1:  # 1글자 키워드는 제외
                    cleaned.append(kw)
        return cleaned

    def _limit_total_keywords(self, keywords_dict: Dict[str, List[str]], max_total: int) -> Dict[str, List[str]]:
        """전체 키워드 수를 제한"""
        # 우선순위: broad_technical > specific_connectable > unique_technical > evolved_concepts
        priority_order = ["broad_technical", "specific_connectable", "unique_technical", "evolved_concepts"]

        result = {key: [] for key in keywords_dict.keys()}
        total_count = 0

        for category in priority_order:
            if category in keywords_dict:
                available_slots = max_total - total_count
                if available_slots <= 0:
                    break

                # 이 카테고리에서 가져올 수 있는 키워드 수
                take_count = min(len(keywords_dict[category]), available_slots)
                result[category] = keywords_dict[category][:take_count]
                total_count += take_count

        return result

    def _parse_keywords_fallback(self, keywords_text: str) -> Dict[str, List[str]]:
        """JSON 파싱 실패 시 대체 파싱 방법"""
        self.logger.warning("JSON 파싱 실패, 텍스트 기반 파싱 사용")

        # 단순히 쉼표로 구분된 키워드를 broad_technical로 분류
        keywords = [kw.strip() for kw in keywords_text.split(',')]
        cleaned_keywords = self._clean_keyword_list(keywords)

        return {
            "broad_technical": cleaned_keywords[:2],
            "specific_connectable": cleaned_keywords[2:3] if len(cleaned_keywords) > 2 else [],
            "unique_technical": cleaned_keywords[3:4] if len(cleaned_keywords) > 3 else [],
            "evolved_concepts": cleaned_keywords[4:5] if len(cleaned_keywords) > 4 else []
        }

    def _extract_fallback_keywords(self, title: str, abstract: str) -> Dict[str, List[str]]:
        """LLM 실패 시 대체 키워드 추출 (간단한 규칙 기반)"""
        self.logger.warning("LLM 키워드 추출 실패, 규칙 기반 대체 방법 사용")

        text = (title + " " + abstract).lower()

        # 카테고리별 키워드 매칭
        broad_keywords = []
        specific_keywords = []

        # 광범위 기술 키워드 매칭
        broad_terms = {
            "machine learning": "Machine Learning",
            "deep learning": "Deep Learning",
            "neural network": "Neural Network",
            "transformer": "Transformer",
            "natural language processing": "Natural Language Processing",
            "computer vision": "Computer Vision",
            "artificial intelligence": "Artificial Intelligence",
            "llm": "LLM",
            "rag": "RAG"
        }

        for term, keyword in broad_terms.items():
            if term in text and keyword not in broad_keywords:
                broad_keywords.append(keyword)
                if len(broad_keywords) >= 2:
                    break

        # 세부 연결 키워드 매칭
        specific_terms = {
            "multimodal": "Multimodal Learning",
            "few-shot": "Few-shot Learning",
            "attention": "Attention Mechanism",
            "graph neural": "Graph Neural Network",
            "reinforcement learning": "Reinforcement Learning"
        }

        for term, keyword in specific_terms.items():
            if term in text and keyword not in specific_keywords:
                specific_keywords.append(keyword)
                if len(specific_keywords) >= 2:
                    break

        # 기본 키워드 부족시 카테고리 기반 추가
        if not broad_keywords:
            if "cs.ai" in text:
                broad_keywords.append("Artificial Intelligence")
            elif "cs.lg" in text:
                broad_keywords.append("Machine Learning")
            elif "cs.cl" in text:
                broad_keywords.append("Natural Language Processing")
            elif "cs.cv" in text:
                broad_keywords.append("Computer Vision")

        return {
            "broad_technical": broad_keywords[:2],
            "specific_connectable": specific_keywords[:2],
            "unique_technical": [],
            "evolved_concepts": []
        }


def get_keyword_extractor(provider: str = "openai", model: str = None) -> KeywordExtractor:
    """키워드 추출기 팩토리 함수"""
    return KeywordExtractor(provider=provider, model=model)