"""Prompt templates for various AI tasks."""

from typing import Dict, Any
from pathlib import Path
import json
import yaml


class PromptTemplate:
    """프롬프트 템플릿 클래스"""
    
    def __init__(self, name: str, template: str, description: str = ""):
        self.name = name
        self.template = template
        self.description = description
    
    def format(self, **kwargs) -> str:
        """템플릿에 변수를 적용하여 프롬프트 생성"""
        try:
            return self.template.format(**kwargs)
        except KeyError as e:
            raise ValueError(f"Missing required variable for prompt '{self.name}': {e}")


class PromptManager:
    """프롬프트 관리자"""
    
    def __init__(self, templates_dir: Path = None):
        if templates_dir is None:
            templates_dir = Path(__file__).parent / "templates"
        
        self.templates_dir = templates_dir
        self.templates_dir.mkdir(exist_ok=True)
        
        self.templates: Dict[str, PromptTemplate] = {}
        self._load_default_templates()
        self._load_custom_templates()
    
    def _load_default_templates(self):
        """기본 프롬프트 템플릿 로드"""
        
        # 키워드 추출 프롬프트 (카테고리화된 트렌드 분석용)
        keyword_extraction_template = """
You are a keyword normalization & linking assistant for Obsidian graphs.

GOAL
- Propose a SMALL set of connectable, normalized keyword candidates from the paper's title+abstract.
- Fewer-but-stronger links are preferred.

INPUT
- Title: {title}
- Abstract: {abstract}
- Known Canonical Vocabulary (Optional): {controlled_vocab_json}   // 우리 사전 일부 (상위 500개)
- Recently Trending Candidates (Optional): {recent_trending_json} // 최근 30일 급증 키워드 100개

REQUIREMENTS
1) Output at most 6 candidates total (NOT per category).
2) For each candidate, provide:
   - surface: as appears in the paper
   - canonical: match an existing canonical from the provided vocab if similar (cosine≥0.85), else propose a new canonical
   - aliases: common synonyms/abbreviations
   - category: one of [broad_technical, specific_connectable, unique_technical, evolved_concepts]
   - rationale: one sentence on why it helps linking
   - scores: novelty(0-1), connectivity(0-1), specificity(0-1), link_intent(0-1)
3) Avoid overly generic or administrative terms (e.g., “method”, “experiment”, “performance”).
4) Prefer noun phrases; max 3–4 tokens unless it’s a well-known long form.
5) Use full names over acronyms unless the acronym is dominant (e.g., “GNN” as alias, canonical “Graph Neural Networks”).

DECISION HEURISTICS (APPLY BEFORE OUTPUT)
- Drop items with link_intent < 0.5
- For broad_technical, keep at most 1 item
- For unique_technical, include only if novelty ≥ 0.6
- If multiple variants map to the same canonical, keep the canonical once and list others in aliases

OUTPUT (JSON)
{{
  "candidates": [
    {{
      "surface": "...",
      "canonical": "...",
      "aliases": ["...", "..."],
      "category": "specific_connectable",
      "rationale": "...",
      "novelty_score": 0.62,
      "connectivity_score": 0.81,
      "specificity_score": 0.74,
      "link_intent_score": 0.76
    }}
  ],
  "ban_list_suggestions": ["...", "..."]
}}
"""

        # 요약 개선 프롬프트
        summary_template = """
당신은 학술 논문 요약 전문가입니다.

다음 논문의 초록을 한국어로 간결하고 명확하게 요약해주세요.

**논문 초록:** {abstract}

**요약 기준:**
1. 논문의 핵심 아이디어와 방법론을 포함
2. 주요 결과와 기여도를 명시
3. 200자 이내로 간결하게 작성
4. 전문 용어는 괄호 안에 영문 병기

**응답 형식:**
요약문만 제시해주세요.
"""

        # 주요 포인트 추출 프롬프트
        key_points_template = """
당신은 학술 논문 분석 전문가입니다.

다음 논문의 초록에서 주요 포인트 3-5개를 추출해주세요.

**논문 초록:** {abstract}

**추출 기준:**
1. 논문의 핵심 기여사항
2. 사용된 주요 방법론
3. 중요한 실험 결과
4. 실용적 응용 가능성

**응답 형식:**
각 포인트를 한 줄씩, 번호 없이 "- "로 시작하여 작성해주세요.

예시:
- 새로운 트랜스포머 아키텍처 제안으로 기존 모델 대비 30% 성능 향상
- 자기주의 메커니즘의 계산 복잡도를 O(n²)에서 O(n log n)으로 개선
- 다국어 번역 작업에서 BLEU 점수 2.5점 향상 달성
"""

        self.templates["keyword_extraction"] = PromptTemplate(
            name="keyword_extraction",
            template=keyword_extraction_template,
            description="논문에서 대표 키워드 3개 이내를 추출하는 프롬프트"
        )
        
        self.templates["summary"] = PromptTemplate(
            name="summary",
            template=summary_template,
            description="논문 초록을 한국어로 요약하는 프롬프트"
        )
        
        self.templates["key_points"] = PromptTemplate(
            name="key_points",
            template=key_points_template,
            description="논문의 주요 포인트를 추출하는 프롬프트"
        )
    
    def _load_custom_templates(self):
        """사용자 정의 프롬프트 템플릿 로드"""
        templates_file = self.templates_dir / "custom_templates.yaml"
        
        if templates_file.exists():
            try:
                with open(templates_file, 'r', encoding='utf-8') as f:
                    custom_templates = yaml.safe_load(f)
                
                for name, template_data in custom_templates.items():
                    self.templates[name] = PromptTemplate(
                        name=name,
                        template=template_data.get('template', ''),
                        description=template_data.get('description', '')
                    )
            except Exception as e:
                print(f"Warning: Failed to load custom templates: {e}")
    
    def save_custom_templates(self):
        """사용자 정의 템플릿을 파일에 저장"""
        custom_templates = {}
        
        # 기본 템플릿이 아닌 것들만 저장
        default_names = {"keyword_extraction", "summary", "key_points"}
        
        for name, template in self.templates.items():
            if name not in default_names:
                custom_templates[name] = {
                    'template': template.template,
                    'description': template.description
                }
        
        if custom_templates:
            templates_file = self.templates_dir / "custom_templates.yaml"
            with open(templates_file, 'w', encoding='utf-8') as f:
                yaml.dump(custom_templates, f, allow_unicode=True, default_flow_style=False)
    
    def get_template(self, name: str) -> PromptTemplate:
        """템플릿 조회"""
        if name not in self.templates:
            raise ValueError(f"Template '{name}' not found")
        return self.templates[name]
    
    def add_template(self, name: str, template: str, description: str = ""):
        """새 템플릿 추가"""
        self.templates[name] = PromptTemplate(name, template, description)
        self.save_custom_templates()
    
    def list_templates(self) -> Dict[str, str]:
        """모든 템플릿 목록 반환"""
        return {name: template.description for name, template in self.templates.items()}
    
    def generate_prompt(self, template_name: str, **kwargs) -> str:
        """프롬프트 생성"""
        template = self.get_template(template_name)
        return template.format(**kwargs)
