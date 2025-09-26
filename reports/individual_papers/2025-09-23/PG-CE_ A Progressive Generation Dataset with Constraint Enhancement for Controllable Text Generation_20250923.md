---
keywords:
  - Large Language Model
  - Controllable Text Generation
  - Constraint Enhancement
  - Progressive Generation
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.17669
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:31:00.328148",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Controllable Text Generation",
    "Constraint Enhancement",
    "Progressive Generation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Controllable Text Generation": 0.78,
    "Constraint Enhancement": 0.72,
    "Progressive Generation": 0.7
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
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "This term is central to the paper's focus on controllable text generation and aligns with existing vocabulary.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Controllable Text Generation",
        "canonical": "Controllable Text Generation",
        "aliases": [
          "CTG"
        ],
        "category": "unique_technical",
        "rationale": "This is a key concept in the paper, focusing on enhancing text generation control, which is novel in its approach.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Constraint Enhancement",
        "canonical": "Constraint Enhancement",
        "aliases": [
          "Constraint-based Generation"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel method proposed in the paper for improving text generation quality.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.77,
        "link_intent_score": 0.72
      },
      {
        "surface": "Progressive Generation",
        "canonical": "Progressive Generation",
        "aliases": [
          "PG"
        ],
        "category": "unique_technical",
        "rationale": "A novel approach introduced in the paper for decomposing CTG tasks, enhancing thematic relevance.",
        "novelty_score": 0.68,
        "connectivity_score": 0.55,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Controllable Text Generation",
      "resolved_canonical": "Controllable Text Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Constraint Enhancement",
      "resolved_canonical": "Constraint Enhancement",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.77,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Progressive Generation",
      "resolved_canonical": "Progressive Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.55,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# PG-CE: A Progressive Generation Dataset with Constraint Enhancement for Controllable Text Generation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17669.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.17669](https://arxiv.org/abs/2509.17669)

## 🔗 유사한 논문
- [[2025-09-18/AgentCTG_ Harnessing Multi-Agent Collaboration for Fine-Grained Precise Control in Text Generation_20250918|AgentCTG: Harnessing Multi-Agent Collaboration for Fine-Grained Precise Control in Text Generation]] (86.5% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (82.0% similar)
- [[2025-09-22/Creative Preference Optimization_20250922|Creative Preference Optimization]] (81.3% similar)
- [[2025-09-23/CIE_ Controlling Language Model Text Generations Using Continuous Signals_20250923|CIE: Controlling Language Model Text Generations Using Continuous Signals]] (80.9% similar)
- [[2025-09-22/SyGra_ A Unified Graph-Based Framework for Scalable Generation, Quality Tagging, and Management of Synthetic Data_20250922|SyGra: A Unified Graph-Based Framework for Scalable Generation, Quality Tagging, and Management of Synthetic Data]] (80.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Controllable Text Generation|Controllable Text Generation]], [[keywords/Constraint Enhancement|Constraint Enhancement]], [[keywords/Progressive Generation|Progressive Generation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17669v1 Announce Type: new 
Abstract: With the rapid development of Large Language Models (LLMs), Controllable Text Generation (CTG) has become a critical technology for enhancing system reliability and user experience. Addressing the limitations of traditional methods, this paper proposes the PG-CE (Progressive Generation with Constraint Enhancement) approach, which decomposes CTG tasks into three steps: type prediction, constraint construction, and guided generation. This method employs constraint generation models to dynamically build multi-dimensional constraints including tone, expression style, and thematic focus to guide output. Experiments demonstrate that PG-CE significantly improves generation quality across multiple scenarios while maintaining text controllability, thematic relevance, and response practicality. The research developed a dataset containing 90,000 constraint-text pairs (with an 8:2 ratio between daily and other topics), effectively reflecting real-world application requirements.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 발전에 따라 중요성이 커진 제어 가능한 텍스트 생성(CTG)을 개선하기 위해 PG-CE(제약 강화와 함께하는 점진적 생성) 방법을 제안합니다. PG-CE는 CTG 작업을 유형 예측, 제약 조건 구축, 안내된 생성의 세 단계로 나누어 수행합니다. 이 방법은 톤, 표현 스타일, 주제 집중과 같은 다차원 제약을 동적으로 생성하여 출력을 안내합니다. 실험 결과, PG-CE는 다양한 시나리오에서 생성 품질을 크게 향상시키며, 텍스트 제어 가능성, 주제 관련성, 실용성을 유지합니다. 연구는 일상 및 기타 주제에 대한 90,000개의 제약-텍스트 쌍을 포함하는 데이터셋을 개발하여 실제 응용 요구를 효과적으로 반영합니다.

## 🎯 주요 포인트

- 1. PG-CE 접근법은 CTG 작업을 유형 예측, 제약 조건 구성, 가이드 생성의 세 단계로 분해하여 수행합니다.
- 2. 이 방법은 톤, 표현 스타일, 주제 초점을 포함한 다차원 제약 조건을 동적으로 구축하여 출력을 안내합니다.
- 3. 실험 결과, PG-CE는 여러 시나리오에서 생성 품질을 크게 향상시키면서 텍스트 제어 가능성, 주제 관련성, 응답 실용성을 유지합니다.
- 4. 연구에서는 일상 및 기타 주제의 8:2 비율로 구성된 90,000개의 제약-텍스트 쌍을 포함하는 데이터셋을 개발하여 실제 응용 요구 사항을 효과적으로 반영합니다.


---

*Generated on 2025-09-24 03:31:00*