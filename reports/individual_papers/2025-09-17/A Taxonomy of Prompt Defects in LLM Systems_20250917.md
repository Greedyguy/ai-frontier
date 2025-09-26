---
keywords:
  - Large Language Models
  - Prompt Defects Taxonomy
  - Prompt Engineering
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 23:02:53.260957",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Prompt Defects Taxonomy",
    "Prompt Engineering"
  ],
  "rejected_keywords": [
    "Natural Language Processing"
  ],
  "similarity_scores": {
    "Large Language Models": 0.9,
    "Prompt Defects Taxonomy": 0.88,
    "Prompt Engineering": 0.85
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# A Taxonomy of Prompt Defects in LLM Systems

**Korean Title:** LLM 시스템에서 프롬프트 결함의 분류학

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Prompt Defects Taxonomy|Taxonomy of Prompt Defects]], [[keywords/Prompt Engineering|Prompt Engineering]]
**🚀 Evolved Concepts**: [[keywords/Large Language Models|Large Language Models]]

## 🔗 유사한 논문
- [[Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (82.2% similar)
- [[From Capabilities to Performance_ Evaluating Key Functional Properties of LLM Architectures in Penetration Testing_20250919|From Capabilities to Performance Evaluating Key Functional Properties of LLM Architectures in Penetration Testing]] (81.7% similar)
- [[The Sum Leaks More Than Its Parts_ Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration_20250919|The Sum Leaks More Than Its Parts Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration]] (81.7% similar)
- [[A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks_20250919|A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks]] (81.5% similar)
- [[Controlling Language Difficulty in Dialogues with Linguistic Features_20250919|Controlling Language Difficulty in Dialogues with Linguistic Features]] (80.7% similar)

## 📋 저자 정보

**Authors:** Haoye Tian, Chong Wang, BoYang Yang, Lyuye Zhang, Yang Liu

## 📄 Abstract (원문)

Large Language Models (LLMs) have become key components of modern software,
with prompts acting as their de-facto programming interface. However, prompt
design remains largely empirical and small mistakes can cascade into
unreliable, insecure, or inefficient behavior. This paper presents the first
systematic survey and taxonomy of prompt defects, recurring ways that prompts
fail to elicit their intended behavior from LLMs. We organize defects along six
dimensions: (1) Specification and Intent, (2) Input and Content, (3) Structure
and Formatting, (4) Context and Memory, (5) Performance and Efficiency, and (6)
Maintainability and Engineering. Each dimension is refined into fine-grained
subtypes, illustrated with concrete examples and root cause analysis. Grounded
in software engineering principles, we show how these defects surface in real
development workflows and examine their downstream effects. For every subtype,
we distill mitigation strategies that span emerging prompt engineering
patterns, automated guardrails, testing harnesses, and evaluation frameworks.
We then summarize these strategies in a master taxonomy that links defect,
impact, and remedy. We conclude with open research challenges and a call for
rigorous engineering-oriented methodologies to ensure that LLM-driven systems
are dependable by design.

## 🔍 Abstract (한글 번역)

대형 언어 모델(LLM)은 현대 소프트웨어의 핵심 구성 요소가 되었으며, 프롬프트는 사실상의 프로그래밍 인터페이스로 작용하고 있습니다. 그러나 프롬프트 설계는 여전히 경험적이며, 작은 실수도 불안정하고, 안전하지 않거나 비효율적인 동작으로 이어질 수 있습니다. 본 논문은 LLM으로부터 의도한 동작을 이끌어내지 못하는 프롬프트 결함에 대한 최초의 체계적인 조사와 분류 체계를 제시합니다. 우리는 결함을 여섯 가지 차원으로 조직합니다: (1) 명세와 의도, (2) 입력과 내용, (3) 구조와 형식, (4) 문맥과 기억, (5) 성능과 효율성, (6) 유지보수성과 엔지니어링. 각 차원은 세부적인 하위 유형으로 세분화되며, 구체적인 예시와 근본 원인 분석을 통해 설명됩니다. 소프트웨어 공학 원칙에 기반하여, 이러한 결함이 실제 개발 워크플로우에서 어떻게 나타나는지 보여주고, 그로 인한 하류 효과를 검토합니다. 각 하위 유형에 대해, 우리는 신흥 프롬프트 엔지니어링 패턴, 자동화된 안전장치, 테스트 하니스, 평가 프레임워크를 아우르는 완화 전략을 도출합니다. 그런 다음, 결함, 영향, 해결책을 연결하는 마스터 분류 체계로 이러한 전략을 요약합니다. 마지막으로, LLM 기반 시스템이 설계상 신뢰할 수 있도록 보장하기 위한 엄격한 엔지니어링 지향 방법론의 필요성을 강조하며, 남아있는 연구 과제와 도전 과제를 제시합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 프롬프트 결함을 체계적으로 조사하고 분류한 최초의 연구를 제시합니다. 프롬프트 설계의 결함을 (1) 명세와 의도, (2) 입력과 내용, (3) 구조와 형식, (4) 문맥과 메모리, (5) 성능과 효율성, (6) 유지보수와 엔지니어링의 여섯 가지 차원으로 분류하고, 각 차원을 세부 유형으로 나누어 구체적인 예시와 근본 원인 분석을 제공합니다. 소프트웨어 엔지니어링 원칙에 기반하여 이러한 결함이 실제 개발 과정에서 어떻게 나타나는지와 그 영향을 분석하고, 각 유형에 대한 해결 전략을 제시합니다. 또한, 결함, 영향, 해결책을 연결하는 종합적인 분류 체계를 제안하며, LLM 기반 시스템의 신뢰성을 보장하기 위한 연구 과제를 제안합니다.

## 🎯 주요 포인트

- 1. 이 논문은 대형 언어 모델(LLM)의 프롬프트 결함에 대한 체계적인 조사와 분류를 최초로 제시합니다.

- 2. 프롬프트 결함은 여섯 가지 차원으로 분류되며, 각 차원은 세부 유형으로 세분화되어 구체적인 예시와 원인 분석을 통해 설명됩니다.

- 3. 소프트웨어 공학 원칙에 기반하여, 이러한 결함이 실제 개발 워크플로우에서 어떻게 나타나는지와 그로 인한 영향을 분석합니다.

- 4. 각 결함 유형에 대해 프롬프트 엔지니어링 패턴, 자동화된 안전장치, 테스트 하니스, 평가 프레임워크를 포함한 완화 전략을 제시합니다.

- 5. 논문은 LLM 기반 시스템의 신뢰성을 보장하기 위한 엄격한 공학적 방법론의 필요성을 강조하며, 이를 위한 연구 과제를 제시합니다.

---

*Generated on 2025-09-20 07:36:14*