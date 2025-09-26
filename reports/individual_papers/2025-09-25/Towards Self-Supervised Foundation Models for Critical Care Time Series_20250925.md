---
keywords:
  - Transformer
  - Self-supervised Learning
  - Critical Care Time Series
  - Electronic Health Records
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19885
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:53:06.063613",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Self-supervised Learning",
    "Critical Care Time Series",
    "Electronic Health Records"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.8,
    "Self-supervised Learning": 0.85,
    "Critical Care Time Series": 0.7,
    "Electronic Health Records": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Bi-Axial Transformer",
        "canonical": "Transformer",
        "aliases": [
          "BAT"
        ],
        "category": "broad_technical",
        "rationale": "The Bi-Axial Transformer is a specific application of the Transformer architecture, relevant for linking with existing Transformer research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "self-supervised foundation models",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "self-supervised models"
        ],
        "category": "specific_connectable",
        "rationale": "Self-supervised foundation models are crucial for linking advancements in unsupervised learning techniques.",
        "novelty_score": 0.6,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "critical care time series",
        "canonical": "Critical Care Time Series",
        "aliases": [
          "critical care data"
        ],
        "category": "unique_technical",
        "rationale": "This is a specialized dataset type that is central to the paper's focus, offering unique insights into healthcare applications.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "electronic health record datasets",
        "canonical": "Electronic Health Records",
        "aliases": [
          "EHR datasets"
        ],
        "category": "specific_connectable",
        "rationale": "EHR datasets are a foundational element for healthcare-related machine learning models, facilitating connections to medical informatics.",
        "novelty_score": 0.5,
        "connectivity_score": 0.88,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "foundation models",
      "transfer learning",
      "mortality prediction"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Bi-Axial Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "self-supervised foundation models",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "critical care time series",
      "resolved_canonical": "Critical Care Time Series",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "electronic health record datasets",
      "resolved_canonical": "Electronic Health Records",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.88,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Towards Self-Supervised Foundation Models for Critical Care Time Series

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19885.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19885](https://arxiv.org/abs/2509.19885)

## 🔗 유사한 논문
- [[2025-09-23/MIRA_ Medical Time Series Foundation Model for Real-World Health Data_20250923|MIRA: Medical Time Series Foundation Model for Real-World Health Data]] (84.2% similar)
- [[2025-09-24/Early Prediction of In-Hospital ICU Mortality Using Innovative First-Day Data_ A Review_20250924|Early Prediction of In-Hospital ICU Mortality Using Innovative First-Day Data: A Review]] (82.2% similar)
- [[2025-09-24/Early Prediction of Multi-Label Care Escalation Triggers in the Intensive Care Unit Using Electronic Health Records_20250924|Early Prediction of Multi-Label Care Escalation Triggers in the Intensive Care Unit Using Electronic Health Records]] (82.1% similar)
- [[2025-09-23/Multi-View Contrastive Learning for Robust Domain Adaptation in Medical Time Series Analysis_20250923|Multi-View Contrastive Learning for Robust Domain Adaptation in Medical Time Series Analysis]] (82.0% similar)
- [[2025-09-22/Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture_20250922|Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture]] (81.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]], [[keywords/Electronic Health Records|Electronic Health Records]]
**⚡ Unique Technical**: [[keywords/Critical Care Time Series|Critical Care Time Series]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19885v1 Announce Type: cross 
Abstract: Domain-specific foundation models for healthcare have expanded rapidly in recent years, yet foundation models for critical care time series remain relatively underexplored due to the limited size and availability of datasets. In this work, we introduce an early-stage pre-trained foundation model for critical care time-series based on the Bi-Axial Transformer (BAT), trained on pooled electronic health record datasets. We demonstrate effective transfer learning by fine-tuning the model on a dataset distinct from the training sources for mortality prediction, where it outperforms supervised baselines, particularly for small datasets ($<5,000$). These contributions highlight the potential of self-supervised foundation models for critical care times series to support generalizable and robust clinical applications in resource-limited settings.

## 📝 요약

이 논문은 중환자 치료 시계열 데이터를 위한 초기 단계의 사전 학습된 기반 모델을 소개합니다. Bi-Axial Transformer(BAT)를 기반으로 전자의무기록 데이터를 활용해 모델을 개발하였으며, 다른 데이터셋에 대해 미세 조정을 통해 사망률 예측에서 우수한 성능을 보였습니다. 특히, 5,000개 미만의 작은 데이터셋에서 감독 학습 기반 모델을 능가했습니다. 이 연구는 자원 제한 환경에서 일반화 가능하고 견고한 임상 응용을 지원할 수 있는 자기 지도 기반 모델의 잠재력을 강조합니다.

## 🎯 주요 포인트

- 1. 의료 분야의 도메인 특화 기반 모델은 빠르게 확장되고 있으나, 중환자실 시계열 데이터에 대한 기반 모델은 데이터셋의 크기와 가용성의 제한으로 상대적으로 덜 탐구되었다.
- 2. 본 연구에서는 Bi-Axial Transformer(BAT)를 기반으로 한 중환자실 시계열 데이터의 초기 단계 사전 훈련 기반 모델을 소개하였다.
- 3. 본 모델은 훈련 소스와 다른 데이터셋에 대해 미세 조정하여 사망률 예측에서 감독 학습 기반 모델을 능가하는 성능을 보였다, 특히 작은 데이터셋($<5,000$)에서 두드러졌다.
- 4. 본 연구는 자가 지도 기반 모델이 자원이 제한된 환경에서 일반화 가능하고 견고한 임상 응용을 지원할 수 있는 잠재력을 강조한다.


---

*Generated on 2025-09-25 15:53:06*