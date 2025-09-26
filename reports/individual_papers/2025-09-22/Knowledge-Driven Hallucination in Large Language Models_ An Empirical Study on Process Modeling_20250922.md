---
keywords:
  - Large Language Model
  - Knowledge-Driven Hallucination
  - Business Process Management
  - Process Modeling
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15336
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T08:43:44.301837",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Knowledge-Driven Hallucination",
    "Business Process Management",
    "Process Modeling"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Knowledge-Driven Hallucination": 0.78,
    "Business Process Management": 0.8,
    "Process Modeling": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Language Model"
        ],
        "category": "broad_technical",
        "rationale": "Central to the study, providing a direct link to the broader field of language models.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "knowledge-driven hallucination",
        "canonical": "Knowledge-Driven Hallucination",
        "aliases": [
          "hallucination",
          "model hallucination"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel concept specific to the study of LLMs and their reliability.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Business Process Management",
        "canonical": "Business Process Management",
        "aliases": [
          "BPM"
        ],
        "category": "specific_connectable",
        "rationale": "Connects the study to the established domain of business processes, enhancing interdisciplinary links.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "process modeling",
        "canonical": "Process Modeling",
        "aliases": [
          "business process modeling"
        ],
        "category": "specific_connectable",
        "rationale": "Key task in the study, linking to methodologies in business and computational modeling.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "analytical tasks",
      "source artifact",
      "standardized patterns"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "knowledge-driven hallucination",
      "resolved_canonical": "Knowledge-Driven Hallucination",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Business Process Management",
      "resolved_canonical": "Business Process Management",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "process modeling",
      "resolved_canonical": "Process Modeling",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Knowledge-Driven Hallucination in Large Language Models: An Empirical Study on Process Modeling

**Korean Title:** 지식 기반 환각 현상: 프로세스 모델링에 관한 대형 언어 모델의 경험적 연구

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15336.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15336](https://arxiv.org/abs/2509.15336)

## 🔗 유사한 논문
- [[2025-09-17/Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (85.8% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (85.2% similar)
- [[2025-09-22/Quantifying Self-Awareness of Knowledge in Large Language Models_20250922|Quantifying Self-Awareness of Knowledge in Large Language Models]] (85.2% similar)
- [[2025-09-22/Natural Fingerprints of Large Language Models_20250922|Natural Fingerprints of Large Language Models]] (84.8% similar)
- [[2025-09-18/From Automation to Autonomy_ A Survey on Large Language Models in Scientific Discovery_20250918|From Automation to Autonomy: A Survey on Large Language Models in Scientific Discovery]] (84.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Business Process Management|Business Process Management]], [[keywords/Process Modeling|Process Modeling]]
**⚡ Unique Technical**: [[keywords/Knowledge-Driven Hallucination|Knowledge-Driven Hallucination]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15336v1 Announce Type: new 
Abstract: The utility of Large Language Models (LLMs) in analytical tasks is rooted in their vast pre-trained knowledge, which allows them to interpret ambiguous inputs and infer missing information. However, this same capability introduces a critical risk of what we term knowledge-driven hallucination: a phenomenon where the model's output contradicts explicit source evidence because it is overridden by the model's generalized internal knowledge. This paper investigates this phenomenon by evaluating LLMs on the task of automated process modeling, where the goal is to generate a formal business process model from a given source artifact. The domain of Business Process Management (BPM) provides an ideal context for this study, as many core business processes follow standardized patterns, making it likely that LLMs possess strong pre-trained schemas for them. We conduct a controlled experiment designed to create scenarios with deliberate conflict between provided evidence and the LLM's background knowledge. We use inputs describing both standard and deliberately atypical process structures to measure the LLM's fidelity to the provided evidence. Our work provides a methodology for assessing this critical reliability issue and raises awareness of the need for rigorous validation of AI-generated artifacts in any evidence-based domain.

## 🔍 Abstract (한글 번역)

arXiv:2509.15336v1 발표 유형: 신규  
초록: 대형 언어 모델(LLMs)의 분석 작업에서의 유용성은 방대한 사전 학습 지식에 기반하여 모호한 입력을 해석하고 누락된 정보를 추론할 수 있는 능력에 뿌리를 두고 있습니다. 그러나 이러한 능력은 모델의 일반화된 내부 지식에 의해 명시적인 출처 증거가 무시되어 모델의 출력이 이를 모순되게 하는 지식 기반 환각이라는 중요한 위험을 초래합니다. 본 논문은 주어진 소스 아티팩트로부터 형식적인 비즈니스 프로세스 모델을 생성하는 자동화된 프로세스 모델링 작업에서 LLM을 평가하여 이 현상을 조사합니다. 비즈니스 프로세스 관리(BPM) 분야는 많은 핵심 비즈니스 프로세스가 표준화된 패턴을 따르기 때문에 LLM이 이에 대한 강력한 사전 학습 스키마를 보유할 가능성이 높아 본 연구에 이상적인 맥락을 제공합니다. 우리는 제공된 증거와 LLM의 배경 지식 간에 의도적인 충돌을 일으키는 시나리오를 만들기 위해 설계된 통제된 실험을 수행합니다. 표준적이거나 의도적으로 비정형적인 프로세스 구조를 설명하는 입력을 사용하여 제공된 증거에 대한 LLM의 충실도를 측정합니다. 우리의 연구는 이 중요한 신뢰성 문제를 평가하기 위한 방법론을 제공하며, 증거 기반 도메인에서 AI 생성 아티팩트의 엄격한 검증 필요성에 대한 인식을 높입니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)이 분석 작업에서 유용하지만, 내재된 지식으로 인해 명시적 증거와 상충되는 출력을 생성하는 '지식 기반 환각' 현상을 초래할 수 있음을 다룹니다. 연구는 자동화된 프로세스 모델링 작업에서 LLM의 성능을 평가하며, 비즈니스 프로세스 관리(BPM) 분야를 대상으로 합니다. 실험을 통해 제공된 증거와 LLM의 배경 지식 간의 충돌을 의도적으로 조성하여, 모델이 증거에 얼마나 충실한지를 측정합니다. 이 연구는 AI 생성 결과물의 신뢰성을 평가하는 방법론을 제시하고, 증거 기반 분야에서의 엄격한 검증 필요성을 강조합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 지식 기반 환각 현상은 명시적 증거와 모순되는 출력을 생성하는 위험을 내포하고 있다.
- 2. 본 논문은 자동화된 프로세스 모델링 작업을 통해 LLM의 지식 기반 환각 현상을 조사한다.
- 3. 비즈니스 프로세스 관리(BPM) 분야는 많은 핵심 비즈니스 프로세스가 표준화된 패턴을 따르기 때문에 LLM의 사전 학습 스키마가 강력할 가능성이 높다.
- 4. 연구는 제공된 증거와 LLM의 배경 지식 간의 의도적인 충돌을 포함한 시나리오를 통해 LLM의 증거 충실도를 측정한다.
- 5. AI 생성 아티팩트의 엄격한 검증 필요성을 강조하며, 증거 기반 도메인에서의 신뢰성 문제를 평가하는 방법론을 제공한다.


---

*Generated on 2025-09-23 08:43:44*