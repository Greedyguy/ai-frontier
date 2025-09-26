<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:20:32.390804",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Unlearning",
    "Shapley Value",
    "Large Language Model",
    "Data Valuation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Unlearning": 0.78,
    "Shapley Value": 0.85,
    "Large Language Model": 0.82,
    "Data Valuation": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Machine Unlearning",
        "canonical": "Machine Unlearning",
        "aliases": [
          "Data Forgetting"
        ],
        "category": "unique_technical",
        "rationale": "Machine Unlearning is a novel concept that enhances data privacy and valuation, making it a key topic for linking in modern AI discussions.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Shapley Value",
        "canonical": "Shapley Value",
        "aliases": [
          "Game-Theoretic Value"
        ],
        "category": "broad_technical",
        "rationale": "Shapley Value is a fundamental concept in data valuation and game theory, providing a strong link to discussions on data contribution and fairness.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Large Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large AI Models"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to current AI research, offering extensive connections to topics like scalability and efficiency.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.68,
        "link_intent_score": 0.82
      },
      {
        "surface": "Data Valuation",
        "canonical": "Data Valuation",
        "aliases": [
          "Data Contribution Assessment"
        ],
        "category": "specific_connectable",
        "rationale": "Data Valuation is crucial for understanding the impact of individual data points, linking to broader themes of data markets and AI ethics.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.77,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "proliferation",
      "traditional approaches"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Machine Unlearning",
      "resolved_canonical": "Machine Unlearning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Shapley Value",
      "resolved_canonical": "Shapley Value",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Large Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.68,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Data Valuation",
      "resolved_canonical": "Data Valuation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.77,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Losing is for Cherishing: Data Valuation Based on Machine Unlearning and Shapley Value

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.16147.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2505.16147](https://arxiv.org/abs/2505.16147)

## 🔗 유사한 논문
- [[2025-09-24/Data Valuation and Selection in a Federated Model Marketplace_20250924|Data Valuation and Selection in a Federated Model Marketplace]] (82.4% similar)
- [[2025-09-18/Reveal and Release_ Iterative LLM Unlearning with Self-generated Data_20250918|Reveal and Release: Iterative LLM Unlearning with Self-generated Data]] (81.3% similar)
- [[2025-09-22/Estimating Model Performance Under Covariate Shift Without Labels_20250922|Estimating Model Performance Under Covariate Shift Without Labels]] (80.5% similar)
- [[2025-09-22/PVPO_ Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning_20250922|PVPO: Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning]] (80.3% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Shapley Value|Shapley Value]], [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Data Valuation|Data Valuation]]
**⚡ Unique Technical**: [[keywords/Machine Unlearning|Machine Unlearning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.16147v2 Announce Type: replace 
Abstract: The proliferation of large models has intensified the need for efficient data valuation methods to quantify the contribution of individual data providers. Traditional approaches, such as game-theory-based Shapley value and influence-function-based techniques, face prohibitive computational costs or require access to full data and model training details, making them hardly achieve partial data valuation. To address this, we propose Unlearning Shapley, a novel framework that leverages machine unlearning to estimate data values efficiently. By unlearning target data from a pretrained model and measuring performance shifts on a reachable test set, our method computes Shapley values via Monte Carlo sampling, avoiding retraining and eliminating dependence on full data. Crucially, Unlearning Shapley supports both full and partial data valuation, making it scalable for large models (e.g., LLMs) and practical for data markets. Experiments on benchmark datasets and large-scale text corpora demonstrate that our approach matches the accuracy of state-of-the-art methods while reducing computational overhead by orders of magnitude. Further analysis confirms a strong correlation between estimated values and the true impact of data subsets, validating its reliability in real-world scenarios. This work bridges the gap between data valuation theory and practical deployment, offering a scalable, privacy-compliant solution for modern AI ecosystems.

## 📝 요약

대형 모델의 확산으로 인해 개별 데이터 제공자의 기여도를 효율적으로 평가하는 방법이 필요해졌습니다. 기존의 게임 이론 기반 Shapley 값이나 영향 함수 기반 기술은 계산 비용이 높거나 전체 데이터와 모델 훈련 세부 정보에 대한 접근이 필요하여 부분 데이터 평가가 어렵습니다. 이를 해결하기 위해 우리는 기계 학습 해제를 활용한 새로운 프레임워크인 Unlearning Shapley를 제안합니다. 이 방법은 사전 훈련된 모델에서 목표 데이터를 제거하고 테스트 세트에서 성능 변화를 측정하여 Monte Carlo 샘플링을 통해 Shapley 값을 계산합니다. 이로써 재훈련 없이 전체 데이터에 대한 의존을 제거하고, 대형 모델과 데이터 시장에 적합한 확장성을 제공합니다. 벤치마크 데이터셋과 대규모 텍스트 코퍼스 실험 결과, 최신 방법과 유사한 정확성을 유지하면서도 계산 부담을 크게 줄였습니다. 추가 분석에서는 추정된 값과 데이터 부분집합의 실제 영향 간 강한 상관관계를 확인하여 실용성을 입증했습니다. 이 연구는 데이터 평가 이론과 실제 적용 간의 간극을 메우며, 현대 AI 생태계에 적합한 확장 가능하고 프라이버시를 준수하는 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. 대규모 모델의 증가로 인해 개별 데이터 제공자의 기여도를 정량화하는 효율적인 데이터 평가 방법의 필요성이 증가하고 있습니다.
- 2. 기존의 게임 이론 기반 Shapley 값 및 영향 함수 기반 기법은 높은 계산 비용이 들거나 전체 데이터 및 모델 훈련 세부 정보에 대한 접근이 필요하여 부분 데이터 평가를 거의 달성하지 못합니다.
- 3. Unlearning Shapley는 사전 훈련된 모델에서 목표 데이터를 제거하고 성능 변화를 측정하여 데이터 가치를 효율적으로 추정하는 새로운 프레임워크입니다.
- 4. 이 방법은 전체 데이터에 의존하지 않고 몬테카를로 샘플링을 통해 Shapley 값을 계산하여 재훈련을 피하고 대규모 모델 및 데이터 시장에 적합합니다.
- 5. 실험 결과, 제안된 방법은 최신 기법의 정확성을 유지하면서 계산 비용을 크게 줄이며, 데이터 하위 집합의 실제 영향과의 강한 상관관계를 보여 신뢰성을 입증합니다.


---

*Generated on 2025-09-24 14:20:32*