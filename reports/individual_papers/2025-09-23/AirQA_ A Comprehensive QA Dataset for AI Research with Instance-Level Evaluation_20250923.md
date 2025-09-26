---
keywords:
  - Large Language Model
  - Multimodal Learning
  - ExTrActor Framework
  - AirQA Dataset
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16952
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:38:37.991469",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Multimodal Learning",
    "ExTrActor Framework",
    "AirQA Dataset"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Multimodal Learning": 0.82,
    "ExTrActor Framework": 0.78,
    "AirQA Dataset": 0.83
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
        "rationale": "Key technology enabling automated QA workflows, relevant for linking AI research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.89,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multimodal",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal"
        ],
        "category": "specific_connectable",
        "rationale": "Important for understanding the dataset's scope in handling diverse data types.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "ExTrActor",
        "canonical": "ExTrActor Framework",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A novel framework for data synthesis, crucial for dataset generation and evaluation.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "AirQA",
        "canonical": "AirQA Dataset",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Central to the paper, representing a new QA dataset for AI research.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.83
      }
    ],
    "ban_list_suggestions": [
      "question answering",
      "dataset",
      "evaluation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.89,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Multimodal",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "ExTrActor",
      "resolved_canonical": "ExTrActor Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "AirQA",
      "resolved_canonical": "AirQA Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.83
      }
    }
  ]
}
-->

# AirQA: A Comprehensive QA Dataset for AI Research with Instance-Level Evaluation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16952.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16952](https://arxiv.org/abs/2509.16952)

## 🔗 유사한 논문
- [[2025-09-19/SWE-QA_ Can Language Models Answer Repository-level Code Questions?_20250919|SWE-QA: Can Language Models Answer Repository-level Code Questions?]] (82.0% similar)
- [[2025-09-19/MovieCORE_ COgnitive REasoning in Movies_20250919|MovieCORE: COgnitive REasoning in Movies]] (81.8% similar)
- [[2025-09-19/OpenLens AI_ Fully Autonomous Research Agent for Health Infomatics_20250919|OpenLens AI: Fully Autonomous Research Agent for Health Infomatics]] (80.7% similar)
- [[2025-09-18/MAFA_ A multi-agent framework for annotation_20250918|MAFA: A multi-agent framework for annotation]] (80.3% similar)
- [[2025-09-18/Self-Guided Function Calling in Large Language Models via Stepwise Experience Recall_20250918|Self-Guided Function Calling in Large Language Models via Stepwise Experience Recall]] (80.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/ExTrActor Framework|ExTrActor Framework]], [[keywords/AirQA Dataset|AirQA Dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16952v1 Announce Type: cross 
Abstract: The growing volume of academic papers has made it increasingly difficult for researchers to efficiently extract key information. While large language models (LLMs) based agents are capable of automating question answering (QA) workflows for scientific papers, there still lacks a comprehensive and realistic benchmark to evaluate their capabilities. Moreover, training an interactive agent for this specific task is hindered by the shortage of high-quality interaction trajectories. In this work, we propose AirQA, a human-annotated comprehensive paper QA dataset in the field of artificial intelligence (AI), with 13,948 papers and 1,246 questions, that encompasses multi-task, multi-modal and instance-level evaluation. Furthermore, we propose ExTrActor, an automated framework for instruction data synthesis. With three LLM-based agents, ExTrActor can perform example generation and trajectory collection without human intervention. Evaluations of multiple open-source and proprietary models show that most models underperform on AirQA, demonstrating the quality of our dataset. Extensive experiments confirm that ExTrActor consistently improves the multi-turn tool-use capability of small models, enabling them to achieve performance comparable to larger ones.

## 📝 요약

이 논문은 연구자들이 학술 논문에서 핵심 정보를 효율적으로 추출하는 데 어려움을 겪고 있는 문제를 해결하기 위해, AI 분야의 논문에 대한 질문 응답(QA) 데이터셋인 AirQA를 제안합니다. AirQA는 13,948개의 논문과 1,246개의 질문으로 구성되어 있으며, 다중 작업, 다중 모드, 인스턴스 수준 평가를 포함합니다. 또한, ExTrActor라는 자동화된 프레임워크를 통해 예제 생성과 경로 수집을 인간의 개입 없이 수행할 수 있습니다. 여러 모델 평가 결과, 대부분의 모델이 AirQA에서 낮은 성능을 보였으며, 이는 데이터셋의 품질을 입증합니다. 실험 결과, ExTrActor는 작은 모델의 다중 턴 도구 사용 능력을 향상시켜, 더 큰 모델과 유사한 성능을 달성할 수 있음을 확인했습니다.

## 🎯 주요 포인트

- 1. 학술 논문의 증가로 인해 연구자들이 핵심 정보를 효율적으로 추출하는 것이 어려워지고 있다.
- 2. AirQA는 AI 분야의 13,948개 논문과 1,246개 질문을 포함한 인간 주석 기반의 포괄적인 논문 QA 데이터셋이다.
- 3. ExTrActor는 인간의 개입 없이 예제 생성과 경로 수집을 수행할 수 있는 자동화된 프레임워크이다.
- 4. AirQA 데이터셋을 통해 대부분의 모델이 성능이 부족함을 보여주며, 이는 데이터셋의 품질을 입증한다.
- 5. ExTrActor는 소형 모델의 다중 턴 도구 사용 능력을 향상시켜 대형 모델에 필적하는 성능을 달성하게 한다.


---

*Generated on 2025-09-23 23:38:37*