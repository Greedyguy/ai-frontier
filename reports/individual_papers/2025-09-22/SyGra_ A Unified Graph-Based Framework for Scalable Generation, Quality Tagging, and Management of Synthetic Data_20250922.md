---
keywords:
  - Large Language Model
  - Supervised Fine-Tuning
  - Direct Preference Optimization
  - Synthetic Data Generation
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2508.15432
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:40:05.670254",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Supervised Fine-Tuning",
    "Direct Preference Optimization",
    "Synthetic Data Generation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Supervised Fine-Tuning": 0.8,
    "Direct Preference Optimization": 0.78,
    "Synthetic Data Generation": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Connects to a wide range of discussions on language model advancements and datasets.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Supervised Fine-Tuning",
        "canonical": "Supervised Fine-Tuning",
        "aliases": [
          "SFT"
        ],
        "category": "specific_connectable",
        "rationale": "Key process in adapting models, relevant to both existing and emerging techniques.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.8
      },
      {
        "surface": "Direct Preference Optimization",
        "canonical": "Direct Preference Optimization",
        "aliases": [
          "DPO"
        ],
        "category": "unique_technical",
        "rationale": "A specific alignment task that is critical for model performance tuning.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Synthetic Data Generation",
        "canonical": "Synthetic Data Generation",
        "aliases": [
          "Data Synthesis"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's framework, facilitating scalable data creation for model training.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "framework",
      "pipeline",
      "mechanism"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Supervised Fine-Tuning",
      "resolved_canonical": "Supervised Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Direct Preference Optimization",
      "resolved_canonical": "Direct Preference Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Synthetic Data Generation",
      "resolved_canonical": "Synthetic Data Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# SyGra: A Unified Graph-Based Framework for Scalable Generation, Quality Tagging, and Management of Synthetic Data

**Korean Title:** SyGra: 합성 데이터의 확장 가능한 생성, 품질 태깅 및 관리에 대한 통합 그래프 기반 프레임워크

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2508.15432.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2508.15432](https://arxiv.org/abs/2508.15432)

## 🔗 유사한 논문
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (86.8% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (85.6% similar)
- [[2025-09-17/Synthetic Data Generation for Screen Time and App Usage_20250917|Synthetic Data Generation for Screen Time and App Usage]] (83.9% similar)
- [[2025-09-22/LiteLong_ Resource-Efficient Long-Context Data Synthesis for LLMs_20250922|LiteLong: Resource-Efficient Long-Context Data Synthesis for LLMs]] (83.1% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (82.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Supervised Fine-Tuning|Supervised Fine-Tuning]]
**⚡ Unique Technical**: [[keywords/Direct Preference Optimization|Direct Preference Optimization]], [[keywords/Synthetic Data Generation|Synthetic Data Generation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.15432v2 Announce Type: replace 
Abstract: The advancement of large language models (LLMs) is critically dependent on the availability of high-quality datasets for Supervised Fine-Tuning (SFT), alignment tasks like Direct Preference Optimization (DPO), etc. In this work, we present a comprehensive synthetic data generation framework that facilitates scalable, configurable, and high-fidelity generation of synthetic data tailored for these training paradigms. Our approach employs a modular and configuration-based pipeline capable of modeling complex dialogue flows with minimal manual intervention. This framework uses a dual-stage quality tagging mechanism, combining heuristic rules and LLM-based evaluations, to automatically filter and score data extracted from OASST-formatted conversations, ensuring the curation of high-quality dialogue samples. The resulting datasets are structured under a flexible schema supporting both SFT and DPO use cases, enabling seamless integration into diverse training workflows. Together, these innovations offer a robust solution for generating and managing synthetic conversational data at scale, significantly reducing the overhead of data preparation in LLM training pipelines.

## 🔍 Abstract (한글 번역)

arXiv:2508.15432v2 발표 유형: 교체  
초록: 대형 언어 모델(LLM)의 발전은 감독된 미세 조정(SFT), 직접 선호 최적화(DPO)와 같은 정렬 작업을 위한 고품질 데이터셋의 가용성에 크게 의존합니다. 본 연구에서는 이러한 훈련 패러다임에 맞춘 합성 데이터를 확장 가능하고 구성 가능하며 높은 충실도로 생성할 수 있는 종합적인 합성 데이터 생성 프레임워크를 제시합니다. 우리의 접근법은 최소한의 수작업 개입으로 복잡한 대화 흐름을 모델링할 수 있는 모듈식 및 구성 기반 파이프라인을 사용합니다. 이 프레임워크는 휴리스틱 규칙과 LLM 기반 평가를 결합한 이중 단계 품질 태그 메커니즘을 사용하여 OASST 형식의 대화에서 추출한 데이터를 자동으로 필터링하고 점수를 매겨 고품질 대화 샘플을 선별합니다. 결과 데이터셋은 SFT 및 DPO 사용 사례 모두를 지원하는 유연한 스키마로 구조화되어 다양한 훈련 워크플로우에 원활하게 통합될 수 있습니다. 이러한 혁신은 대규모로 합성 대화 데이터를 생성하고 관리하기 위한 강력한 솔루션을 제공하여 LLM 훈련 파이프라인에서 데이터 준비의 부담을 크게 줄입니다.

## 📝 요약

이 논문은 대규모 언어 모델(LLM)의 발전을 위한 고품질 데이터셋 생성 프레임워크를 제안합니다. 이 프레임워크는 감독된 미세 조정(SFT)과 직접 선호 최적화(DPO)와 같은 작업에 적합한 합성 데이터를 대규모로 생성할 수 있습니다. 모듈형 및 구성 기반 파이프라인을 사용하여 복잡한 대화 흐름을 최소한의 수작업으로 모델링하며, 이중 단계 품질 태그 메커니즘을 통해 자동으로 데이터를 필터링하고 평가합니다. 결과적으로 생성된 데이터셋은 다양한 훈련 워크플로우에 쉽게 통합될 수 있는 유연한 구조를 가지며, LLM 훈련 과정에서 데이터 준비의 부담을 크게 줄입니다.

## 🎯 주요 포인트

- 1. 대규모 언어 모델(LLM)의 발전은 고품질 데이터셋의 가용성에 크게 의존합니다.
- 2. 본 연구는 대규모 언어 모델의 훈련을 위한 합성 데이터 생성 프레임워크를 제안합니다.
- 3. 제안된 프레임워크는 최소한의 수작업 개입으로 복잡한 대화 흐름을 모델링할 수 있는 모듈형 및 구성 기반 파이프라인을 사용합니다.
- 4. 이 프레임워크는 이중 단계 품질 태깅 메커니즘을 사용하여 고품질 대화 샘플을 자동으로 필터링하고 평가합니다.
- 5. 생성된 데이터셋은 다양한 훈련 워크플로우에 원활하게 통합될 수 있도록 유연한 스키마로 구조화됩니다.


---

*Generated on 2025-09-23 09:40:05*