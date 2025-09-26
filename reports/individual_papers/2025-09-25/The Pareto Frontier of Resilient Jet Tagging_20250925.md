---
keywords:
  - Hadronic Jets
  - Resilient Jet Tagging
  - Classifier Performance
  - Model Uncertainty
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19431
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:53:41.629906",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Hadronic Jets",
    "Resilient Jet Tagging",
    "Classifier Performance",
    "Model Uncertainty"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Hadronic Jets": 0.78,
    "Resilient Jet Tagging": 0.82,
    "Classifier Performance": 0.7,
    "Model Uncertainty": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "hadronic jets",
        "canonical": "Hadronic Jets",
        "aliases": [
          "jets",
          "hadron jets"
        ],
        "category": "unique_technical",
        "rationale": "Hadronic jets are a specific concept in high-energy physics that can link to other studies on particle physics and collider experiments.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "resilient jet tagging",
        "canonical": "Resilient Jet Tagging",
        "aliases": [
          "jet tagging",
          "resilient tagging"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and represents a novel approach in jet classification, linking to resilience in machine learning models.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      },
      {
        "surface": "classifier performance",
        "canonical": "Classifier Performance",
        "aliases": [
          "performance metrics",
          "classifier metrics"
        ],
        "category": "broad_technical",
        "rationale": "Understanding classifier performance is crucial for linking to discussions on model evaluation and optimization strategies.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "model uncertainty",
        "canonical": "Model Uncertainty",
        "aliases": [
          "uncertainty in models",
          "model bias"
        ],
        "category": "specific_connectable",
        "rationale": "Model uncertainty is a key aspect in evaluating machine learning models, connecting to broader discussions on model reliability.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "accuracy",
      "AUC",
      "rejection rates"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "hadronic jets",
      "resolved_canonical": "Hadronic Jets",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "resilient jet tagging",
      "resolved_canonical": "Resilient Jet Tagging",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "classifier performance",
      "resolved_canonical": "Classifier Performance",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "model uncertainty",
      "resolved_canonical": "Model Uncertainty",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# The Pareto Frontier of Resilient Jet Tagging

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19431.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19431](https://arxiv.org/abs/2509.19431)

## 🔗 유사한 논문
- [[2025-09-23/ClusterRCA_ An End-to-End Approach for Network Fault Localization and Classification for HPC System_20250923|ClusterRCA: An End-to-End Approach for Network Fault Localization and Classification for HPC System]] (80.0% similar)
- [[2025-09-22/Inference Offloading for Cost-Sensitive Binary Classification at the Edge_20250922|Inference Offloading for Cost-Sensitive Binary Classification at the Edge]] (80.0% similar)
- [[2025-09-23/Fast, Accurate and Interpretable Graph Classification with Topological Kernels_20250923|Fast, Accurate and Interpretable Graph Classification with Topological Kernels]] (78.8% similar)
- [[2025-09-22/Interpretable Network-assisted Random Forest+_20250922|Interpretable Network-assisted Random Forest+]] (78.8% similar)
- [[2025-09-23/BiLCNet _ BiLSTM-Conformer Network for Encrypted Traffic Classification with 5G SA Physical Channel Records_20250923|BiLCNet : BiLSTM-Conformer Network for Encrypted Traffic Classification with 5G SA Physical Channel Records]] (78.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Classifier Performance|Classifier Performance]]
**🔗 Specific Connectable**: [[keywords/Model Uncertainty|Model Uncertainty]]
**⚡ Unique Technical**: [[keywords/Hadronic Jets|Hadronic Jets]], [[keywords/Resilient Jet Tagging|Resilient Jet Tagging]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19431v1 Announce Type: cross 
Abstract: Classifying hadronic jets using their constituents' kinematic information is a critical task in modern high-energy collider physics. Often, classifiers are designed by targeting the best performance using metrics such as accuracy, AUC, or rejection rates. However, the use of a single metric can lead to the use of architectures that are more model-dependent than competitive alternatives, leading to potential uncertainty and bias in analysis. We explore such trade-offs and demonstrate the consequences of using networks with high performance metrics but low resilience.

## 📝 요약

이 논문은 현대 고에너지 충돌 물리학에서 하드론 제트를 분류하는 데 있어 입자 구성 요소의 운동 정보를 활용하는 방법을 다룹니다. 전통적으로 분류기는 정확도, AUC, 거부율 등의 단일 성능 지표를 최대화하는 방향으로 설계되지만, 이는 모델 의존성을 높여 분석의 불확실성과 편향을 초래할 수 있습니다. 본 연구는 이러한 트레이드오프를 탐구하고, 높은 성능 지표를 가진 네트워크가 낮은 회복력을 가질 경우의 결과를 시연합니다.

## 🎯 주요 포인트

- 1. 하드론 제트를 분류하는 것은 현대 고에너지 충돌기 물리학에서 중요한 과제입니다.
- 2. 단일 성능 지표에 의존하는 것은 분석에서 불확실성과 편향을 초래할 수 있습니다.
- 3. 높은 성능 지표를 가진 네트워크가 낮은 탄력성을 가질 수 있음을 보여줍니다.
- 4. 성능 지표와 모델 의존성 간의 절충점을 탐구합니다.


---

*Generated on 2025-09-25 16:53:41*