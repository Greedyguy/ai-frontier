<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:12:36.675309",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Fraud Detection",
    "Multi-arm Bandit",
    "Thompson Sampling",
    "Randomized Selection Strategy"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Fraud Detection": 0.85,
    "Multi-arm Bandit": 0.8,
    "Thompson Sampling": 0.78,
    "Randomized Selection Strategy": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Fraud Detection",
        "canonical": "Fraud Detection",
        "aliases": [
          "Fraud Identification",
          "Fraud Analysis"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's focus, providing a specific context for linking related research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multi-arm Bandit",
        "canonical": "Multi-arm Bandit",
        "aliases": [
          "MAB",
          "Bandit Problem"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to a well-known problem in decision-making and learning, relevant for linking to related strategies.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Thompson Sampling",
        "canonical": "Thompson Sampling",
        "aliases": [
          "TS",
          "Bayesian Bandit"
        ],
        "category": "specific_connectable",
        "rationale": "A specific strategy within the multi-arm bandit framework, useful for linking to probabilistic methods.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "Randomized Selection Strategy",
        "canonical": "Randomized Selection Strategy",
        "aliases": [
          "Randomized Strategy",
          "Random Selection"
        ],
        "category": "unique_technical",
        "rationale": "Proposed as a novel approach in the paper, offering a unique angle for linking to selection strategies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "Selection Strategies",
      "Prediction Model",
      "Parameter Estimates"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Fraud Detection",
      "resolved_canonical": "Fraud Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Multi-arm Bandit",
      "resolved_canonical": "Multi-arm Bandit",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Thompson Sampling",
      "resolved_canonical": "Thompson Sampling",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Randomized Selection Strategy",
      "resolved_canonical": "Randomized Selection Strategy",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Consistency of Selection Strategies for Fraud Detection

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18739.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18739](https://arxiv.org/abs/2509.18739)

## 🔗 유사한 논문
- [[2025-09-19/Evaluating Supervised Learning Models for Fraud Detection_ A Comparative Study of Classical and Deep Architectures on Imbalanced Transaction Data_20250919|Evaluating Supervised Learning Models for Fraud Detection: A Comparative Study of Classical and Deep Architectures on Imbalanced Transaction Data]] (83.0% similar)
- [[2025-09-23/Statistical Inference for Misspecified Contextual Bandits_20250923|Statistical Inference for Misspecified Contextual Bandits]] (81.1% similar)
- [[2025-09-23/Robust Reinforcement Learning with Dynamic Distortion Risk Measures_20250923|Robust Reinforcement Learning with Dynamic Distortion Risk Measures]] (80.4% similar)
- [[2025-09-23/A Comprehensive Performance Comparison of Traditional and Ensemble Machine Learning Models for Online Fraud Detection_20250923|A Comprehensive Performance Comparison of Traditional and Ensemble Machine Learning Models for Online Fraud Detection]] (80.3% similar)
- [[2025-09-22/Nonconvex Regularization for Feature Selection in Reinforcement Learning_20250922|Nonconvex Regularization for Feature Selection in Reinforcement Learning]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multi-arm Bandit|Multi-arm Bandit]], [[keywords/Thompson Sampling|Thompson Sampling]]
**⚡ Unique Technical**: [[keywords/Fraud Detection|Fraud Detection]], [[keywords/Randomized Selection Strategy|Randomized Selection Strategy]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18739v1 Announce Type: cross 
Abstract: This paper studies how insurers can chose which claims to investigate for fraud. Given a prediction model, typically only claims with the highest predicted propability of being fraudulent are investigated. We argue that this can lead to inconsistent learning and propose a randomized alternative. More generally, we draw a parallel with the multi-arm bandit literature and argue that, in the presence of selection, the obtained observations are not iid. Hence, dependence on past observations should be accounted for when updating parameter estimates. We formalize selection in a binary regression framework and show that model updating and maximum-likelihood estimation can be implemented as if claims were investigated at random. Then, we define consistency of selection strategies and conjecture sufficient conditions for consistency. Our simulations suggest that the often-used selection strategy can be inconsistent while the proposed randomized alternative is consistent. Finally, we compare our randomized selection strategy with Thompson sampling, a standard multi-arm bandit heuristic. Our simulations suggest that the latter can be inefficient in learning low fraud probabilities.

## 📝 요약

이 논문은 보험사가 사기 가능성이 있는 청구를 조사할 때 사용하는 전략에 대해 연구합니다. 기존에는 사기 가능성이 높은 청구만을 조사했으나, 이는 일관되지 않은 학습을 초래할 수 있음을 지적하며 무작위 대안을 제안합니다. 다중 팔 밴딧 문제와 유사성을 제시하며, 선택된 관찰이 독립적이지 않음을 강조하고, 과거 관찰에 의존하여 매개변수 추정을 업데이트해야 함을 설명합니다. 이진 회귀 프레임워크를 통해 선택을 형식화하고, 무작위로 청구를 조사하는 것처럼 모델 업데이트와 최대 우도 추정을 구현할 수 있음을 보여줍니다. 시뮬레이션 결과, 기존의 선택 전략은 일관성이 없을 수 있지만, 제안된 무작위 대안은 일관성이 있음을 시사합니다. 또한, 제안된 무작위 선택 전략과 다중 팔 밴딧 휴리스틱인 톰슨 샘플링을 비교하며, 후자는 낮은 사기 확률 학습에 비효율적일 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. 보험사들이 사기 가능성이 높은 청구 건만 조사하는 기존 방식은 일관되지 않은 학습을 초래할 수 있다.
- 2. 선택된 관측값이 독립적이지 않기 때문에 과거 관측값에 의존하여 매개변수 추정을 업데이트해야 한다.
- 3. 이진 회귀 프레임워크에서 무작위로 청구 건을 조사하는 것처럼 모델 업데이트와 최대우도 추정을 구현할 수 있다.
- 4. 기존의 선택 전략은 일관성이 없을 수 있으며, 제안된 무작위 대안은 일관성이 있다.
- 5. 제안된 무작위 선택 전략은 낮은 사기 확률을 학습하는 데 비효율적인 톰슨 샘플링보다 효과적이다.


---

*Generated on 2025-09-24 15:12:36*