---
keywords:
  - Evaluation-Aware Reinforcement Learning
  - Policy Evaluation
  - Reinforcement Learning
  - Value Prediction Scheme
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19464
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:14:14.117255",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Evaluation-Aware Reinforcement Learning",
    "Policy Evaluation",
    "Reinforcement Learning",
    "Value Prediction Scheme"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Evaluation-Aware Reinforcement Learning": 0.88,
    "Policy Evaluation": 0.8,
    "Reinforcement Learning": 0.85,
    "Value Prediction Scheme": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Evaluation-Aware Reinforcement Learning",
        "canonical": "Evaluation-Aware Reinforcement Learning",
        "aliases": [
          "EvA-RL"
        ],
        "category": "unique_technical",
        "rationale": "This concept introduces a novel approach to reinforcement learning by integrating evaluation as a core component, which is central to the paper's contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "Policy Evaluation",
        "canonical": "Policy Evaluation",
        "aliases": [
          "Policy Assessment"
        ],
        "category": "specific_connectable",
        "rationale": "Policy evaluation is a critical component in reinforcement learning, providing a direct link to the paper's focus on evaluation-aware methods.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      },
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is the foundational framework within which the paper's proposed method operates, ensuring broad connectivity.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "Value Prediction Scheme",
        "canonical": "Value Prediction Scheme",
        "aliases": [
          "Value Estimation Method"
        ],
        "category": "unique_technical",
        "rationale": "This term is crucial for understanding the evaluation mechanism proposed in the paper and its impact on policy training.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "system"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Evaluation-Aware Reinforcement Learning",
      "resolved_canonical": "Evaluation-Aware Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Policy Evaluation",
      "resolved_canonical": "Policy Evaluation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Value Prediction Scheme",
      "resolved_canonical": "Value Prediction Scheme",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Evaluation-Aware Reinforcement Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19464.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19464](https://arxiv.org/abs/2509.19464)

## 🔗 유사한 논문
- [[2025-09-22/PVPO_ Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning_20250922|PVPO: Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning]] (84.7% similar)
- [[2025-09-23/ConfClip_ Confidence-Weighted and Clipped Reward for Reinforcement Learning in LLMs_20250923|ConfClip: Confidence-Weighted and Clipped Reward for Reinforcement Learning in LLMs]] (84.4% similar)
- [[2025-09-19/Online Learning of Deceptive Policies under Intermittent Observation_20250919|Online Learning of Deceptive Policies under Intermittent Observation]] (83.6% similar)
- [[2025-09-19/Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning_20250919|Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning]] (83.4% similar)
- [[2025-09-24/Online Process Reward Leanring for Agentic Reinforcement Learning_20250924|Online Process Reward Leanring for Agentic Reinforcement Learning]] (83.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Policy Evaluation|Policy Evaluation]]
**⚡ Unique Technical**: [[keywords/Evaluation-Aware Reinforcement Learning|Evaluation-Aware Reinforcement Learning]], [[keywords/Value Prediction Scheme|Value Prediction Scheme]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19464v1 Announce Type: new 
Abstract: Policy evaluation is often a prerequisite for deploying safety- and performance-critical systems. Existing evaluation approaches frequently suffer from high variance due to limited data and long-horizon tasks, or high bias due to unequal support or inaccurate environmental models. We posit that these challenges arise, in part, from the standard reinforcement learning (RL) paradigm of policy learning without explicit consideration of evaluation. As an alternative, we propose evaluation-aware reinforcement learning (EvA-RL), in which a policy is trained to maximize expected return while simultaneously minimizing expected evaluation error under a given value prediction scheme -- in other words, being "easy" to evaluate. We formalize a framework for EvA-RL and design an instantiation that enables accurate policy evaluation, conditioned on a small number of rollouts in an assessment environment that can be different than the deployment environment. However, our theoretical analysis and empirical results show that there is often a tradeoff between evaluation accuracy and policy performance when using a fixed value-prediction scheme within EvA-RL. To mitigate this tradeoff, we extend our approach to co-learn an assessment-conditioned state-value predictor alongside the policy. Empirical results across diverse discrete and continuous action domains demonstrate that EvA-RL can substantially reduce evaluation error while maintaining competitive returns. This work lays the foundation for a broad new class of RL methods that treat reliable evaluation as a first-class principle during training.

## 📝 요약

이 논문은 정책 평가의 중요성을 강조하며, 기존 강화 학습(RL) 방법론의 한계를 지적합니다. 기존 방법론은 데이터 부족과 긴 시간대 과제로 인해 높은 분산을 겪거나, 환경 모델의 부정확성으로 인해 높은 편향을 겪습니다. 이를 해결하기 위해, 저자들은 평가를 명시적으로 고려하는 평가 인식 강화 학습(EvA-RL)을 제안합니다. EvA-RL은 정책이 기대 수익을 최대화하면서 동시에 평가 오류를 최소화하도록 훈련됩니다. 이 방법론은 평가 환경에서 소수의 롤아웃으로 정확한 정책 평가를 가능하게 합니다. 그러나 고정된 가치 예측 체계 내에서는 평가 정확도와 정책 성능 간의 절충이 발생할 수 있습니다. 이를 완화하기 위해, 저자들은 정책과 함께 평가 환경에 맞춘 상태-가치 예측기를 공동 학습하는 접근법을 확장합니다. 다양한 행동 영역에서의 실험 결과는 EvA-RL이 평가 오류를 크게 줄이면서도 경쟁력 있는 수익을 유지할 수 있음을 보여줍니다. 이 연구는 신뢰할 수 있는 평가를 훈련의 핵심 원칙으로 삼는 새로운 RL 방법론의 기초를 마련합니다.

## 🎯 주요 포인트

- 1. 정책 평가의 중요성을 강조하며, 기존의 평가 방법들이 데이터 부족과 장기 과제 때문에 높은 분산을 겪거나, 불균형한 지원 및 부정확한 환경 모델로 인해 높은 편향을 겪는 문제를 지적합니다.
- 2. 평가를 명시적으로 고려하지 않는 기존 강화 학습 패러다임의 한계를 극복하기 위해, 평가를 고려한 강화 학습(EvA-RL)을 제안합니다.
- 3. EvA-RL은 주어진 가치 예측 체계 하에서 기대 평가 오류를 최소화하면서 기대 수익을 극대화하도록 정책을 훈련합니다.
- 4. 이론적 분석과 실증 결과는 EvA-RL 내에서 고정된 가치 예측 체계를 사용할 때 평가 정확도와 정책 성능 간의 상충 관계가 존재함을 보여줍니다.
- 5. 다양한 이산 및 연속 행동 도메인에서 EvA-RL은 평가 오류를 크게 줄이면서도 경쟁력 있는 수익을 유지할 수 있음을 실증적으로 입증합니다.


---

*Generated on 2025-09-25 15:14:14*