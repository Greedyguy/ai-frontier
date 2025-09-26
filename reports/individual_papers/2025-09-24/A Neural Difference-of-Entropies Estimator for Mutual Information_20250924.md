<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:32:14.926559",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Mutual Information",
    "Normalizing Flows",
    "Deep Learning",
    "Block Autoregressive Structure"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Mutual Information": 0.8,
    "Normalizing Flows": 0.78,
    "Deep Learning": 0.75,
    "Block Autoregressive Structure": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Mutual Information",
        "canonical": "Mutual Information",
        "aliases": [
          "MI"
        ],
        "category": "unique_technical",
        "rationale": "Mutual Information is a central concept in information theory and is crucial for linking studies on dependence measures.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Normalizing Flows",
        "canonical": "Normalizing Flows",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Normalizing Flows are a popular deep learning model that can connect to various generative modeling studies.",
        "novelty_score": 0.7,
        "connectivity_score": 0.82,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Deep Generative Model",
        "canonical": "Deep Learning",
        "aliases": [
          "DGM"
        ],
        "category": "broad_technical",
        "rationale": "Deep Generative Models are a subset of deep learning, providing a broad connection to the field.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      },
      {
        "surface": "Block Autoregressive Structure",
        "canonical": "Block Autoregressive Structure",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This structure is specific to the proposed method, offering unique insights into model architecture.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "Estimator",
      "Benchmark Tasks",
      "Bias-Variance Trade-offs"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Mutual Information",
      "resolved_canonical": "Mutual Information",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Normalizing Flows",
      "resolved_canonical": "Normalizing Flows",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.82,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Deep Generative Model",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Block Autoregressive Structure",
      "resolved_canonical": "Block Autoregressive Structure",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# A Neural Difference-of-Entropies Estimator for Mutual Information

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2502.13085.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2502.13085](https://arxiv.org/abs/2502.13085)

## 🔗 유사한 논문
- [[2025-09-22/Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows_20250922|Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows]] (79.6% similar)
- [[2025-09-23/A Generative Conditional Distribution Equality Testing Framework and Its Minimax Analysis_20250923|A Generative Conditional Distribution Equality Testing Framework and Its Minimax Analysis]] (78.5% similar)
- [[2025-09-22/Manifold Dimension Estimation_ An Empirical Study_20250922|Manifold Dimension Estimation: An Empirical Study]] (78.4% similar)
- [[2025-09-23/Loss-Complexity Landscape and Model Structure Functions_20250923|Loss-Complexity Landscape and Model Structure Functions]] (78.1% similar)
- [[2025-09-23/Stabilizing Information Flow Entropy_ Regularization for Safe and Interpretable Autonomous Driving Perception_20250923|Stabilizing Information Flow Entropy: Regularization for Safe and Interpretable Autonomous Driving Perception]] (77.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Normalizing Flows|Normalizing Flows]]
**⚡ Unique Technical**: [[keywords/Mutual Information|Mutual Information]], [[keywords/Block Autoregressive Structure|Block Autoregressive Structure]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.13085v2 Announce Type: replace-cross 
Abstract: Estimating Mutual Information (MI), a key measure of dependence of random quantities without specific modelling assumptions, is a challenging problem in high dimensions. We propose a novel mutual information estimator based on parametrizing conditional densities using normalizing flows, a deep generative model that has gained popularity in recent years. This estimator leverages a block autoregressive structure to achieve improved bias-variance trade-offs on standard benchmark tasks.

## 📝 요약

이 논문은 고차원에서의 상호 정보량(MI) 추정을 다루며, 이를 위해 정상화 흐름(normalizing flows)을 활용한 새로운 추정 방법을 제안합니다. 정상화 흐름은 최근 인기를 얻고 있는 심층 생성 모델로, 조건부 밀도를 매개변수화하는 데 사용됩니다. 제안된 추정기는 블록 자기회귀 구조를 활용하여 표준 벤치마크 작업에서 편향-분산 균형을 개선합니다. 주요 기여는 고차원 데이터에서의 상호 정보량 추정의 정확성을 높인 점입니다.

## 🎯 주요 포인트

- 1. 고차원에서의 상호 정보(MI) 추정은 특정 모델링 가정 없이 무작위 변수의 의존성을 측정하는 데 중요한 문제입니다.
- 2. 본 연구는 정상화 흐름(normalizing flows)을 사용하여 조건부 밀도를 매개변수화하는 새로운 상호 정보 추정기를 제안합니다.
- 3. 제안된 추정기는 블록 자기회귀 구조를 활용하여 표준 벤치마크 작업에서 편향-분산 절충을 개선합니다.


---

*Generated on 2025-09-24 15:32:14*