---
keywords:
  - Loss of Trainability
  - Gradient Noise
  - Curvature Volatility
  - Wasserstein Regularization
  - L2 Weight Decay
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19698
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:45:21.742803",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Loss of Trainability",
    "Gradient Noise",
    "Curvature Volatility",
    "Wasserstein Regularization",
    "L2 Weight Decay"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Loss of Trainability": 0.78,
    "Gradient Noise": 0.8,
    "Curvature Volatility": 0.75,
    "Wasserstein Regularization": 0.79,
    "L2 Weight Decay": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Loss of Trainability",
        "canonical": "Loss of Trainability",
        "aliases": [
          "LoT"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's analysis and represents a specific challenge in continual learning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Gradient Noise",
        "canonical": "Gradient Noise",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Gradient noise is a key factor in the proposed predictive threshold for trainability.",
        "novelty_score": 0.55,
        "connectivity_score": 0.72,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Curvature Volatility",
        "canonical": "Curvature Volatility",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a novel concept introduced in the paper to control trainability through a predictive threshold.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      },
      {
        "surface": "Wasserstein Regularization",
        "canonical": "Wasserstein Regularization",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Wasserstein regularization is used in the paper's experiments to stabilize training.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.77,
        "link_intent_score": 0.79
      },
      {
        "surface": "L2 Weight Decay",
        "canonical": "L2 Weight Decay",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "L2 weight decay is a common technique referenced in the paper to improve accuracy.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "optimization lens",
      "adequate capacity",
      "supervision"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Loss of Trainability",
      "resolved_canonical": "Loss of Trainability",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Gradient Noise",
      "resolved_canonical": "Gradient Noise",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.72,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Curvature Volatility",
      "resolved_canonical": "Curvature Volatility",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Wasserstein Regularization",
      "resolved_canonical": "Wasserstein Regularization",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.77,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "L2 Weight Decay",
      "resolved_canonical": "L2 Weight Decay",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# A Unified Noise-Curvature View of Loss of Trainability

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19698.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19698](https://arxiv.org/abs/2509.19698)

## 🔗 유사한 논문
- [[2025-09-22/Flavors of Margin_ Implicit Bias of Steepest Descent in Homogeneous Neural Networks_20250922|Flavors of Margin: Implicit Bias of Steepest Descent in Homogeneous Neural Networks]] (82.6% similar)
- [[2025-09-23/Stabilizing Information Flow Entropy_ Regularization for Safe and Interpretable Autonomous Driving Perception_20250923|Stabilizing Information Flow Entropy: Regularization for Safe and Interpretable Autonomous Driving Perception]] (81.6% similar)
- [[2025-09-24/Stability and Generalization of Adversarial Diffusion Training_20250924|Stability and Generalization of Adversarial Diffusion Training]] (81.5% similar)
- [[2025-09-18/HAM_ Hierarchical Adapter Merging for Scalable Continual Learning_20250918|HAM: Hierarchical Adapter Merging for Scalable Continual Learning]] (81.5% similar)
- [[2025-09-23/On the $O(\frac{\sqrt{d}}{K^{1/4}})$ Convergence Rate of AdamW Measured by $\ell_1$ Norm_20250923|On the $O(\frac{\sqrt{d}}{K^{1/4}})$ Convergence Rate of AdamW Measured by $\ell_1$ Norm]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Gradient Noise|Gradient Noise]], [[keywords/Wasserstein Regularization|Wasserstein Regularization]], [[keywords/L2 Weight Decay|L2 Weight Decay]]
**⚡ Unique Technical**: [[keywords/Loss of Trainability|Loss of Trainability]], [[keywords/Curvature Volatility|Curvature Volatility]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19698v1 Announce Type: cross 
Abstract: Loss of trainability (LoT) in continual learning occurs when gradient steps no longer yield improvement as tasks evolve, so accuracy stalls or degrades despite adequate capacity and supervision. We analyze LoT incurred with Adam through an optimization lens and find that single indicators such as Hessian rank, sharpness level, weight or gradient norms, gradient-to-parameter ratios, and unit-sign entropy are not reliable predictors. Instead we introduce two complementary criteria: a batch-size-aware gradient-noise bound and a curvature volatility-controlled bound that combine into a per-layer predictive threshold that anticipates trainability behavior. Using this threshold, we build a simple per-layer scheduler that keeps each layers effective step below a safe limit, stabilizing training and improving accuracy across concatenated ReLU (CReLU), Wasserstein regularization, and L2 weight decay, with learned learning-rate trajectories that mirror canonical decay.

## 📝 요약

이 논문은 지속 학습에서 발생하는 학습 가능성 상실(LoT) 문제를 다룹니다. Adam 최적화 관점에서 LoT를 분석한 결과, 헤시안 랭크, 샤프니스 수준, 가중치 또는 그래디언트 노름, 그래디언트-매개변수 비율, 유닛-사인 엔트로피와 같은 단일 지표는 신뢰할 수 없는 예측자임을 발견했습니다. 대신, 배치 크기를 고려한 그래디언트 노이즈 경계와 곡률 변동 제어 경계를 결합한 레이어별 예측 임계값을 제안합니다. 이를 통해 각 레이어의 효과적인 스텝을 안전한 한도 내로 유지하는 스케줄러를 구축하여, CReLU, Wasserstein 정규화, L2 가중치 감소에서의 훈련 안정성과 정확성을 향상시킵니다.

## 🎯 주요 포인트

- 1. 지속 학습에서의 학습 가능성 상실(LoT)은 과제의 진화로 인해 기울기 단계가 더 이상 개선을 가져오지 않을 때 발생하며, 이는 충분한 용량과 감독에도 불구하고 정확도가 정체되거나 저하되는 현상이다.
- 2. Adam 최적화 관점에서 LoT를 분석한 결과, 헤시안 랭크, 샤프니스 수준, 가중치 또는 기울기 노름, 기울기 대 파라미터 비율, 단위 부호 엔트로피와 같은 단일 지표는 신뢰할 수 있는 예측자가 아님을 발견했다.
- 3. 대신, 배치 크기 인식 기울기-노이즈 경계와 곡률 변동 제어 경계를 도입하여 계층별 예측 임계값을 설정하고, 이를 통해 학습 가능성 행동을 예측한다.
- 4. 이 임계값을 사용하여 각 계층의 효과적인 단계를 안전한 한도 내로 유지하는 간단한 계층별 스케줄러를 구축하여, CReLU, Wasserstein 정규화, L2 가중치 감쇠에서 학습률 궤적을 학습하여 훈련을 안정화하고 정확도를 향상시킨다.


---

*Generated on 2025-09-25 15:45:21*