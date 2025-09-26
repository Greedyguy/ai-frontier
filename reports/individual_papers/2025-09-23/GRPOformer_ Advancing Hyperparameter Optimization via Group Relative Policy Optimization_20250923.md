---
keywords:
  - Hyperparameter Optimization
  - Group Relative Policy Optimization
  - Policy Churn Regularization
  - Reinforcement Learning
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17105
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:47:05.400481",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Hyperparameter Optimization",
    "Group Relative Policy Optimization",
    "Policy Churn Regularization",
    "Reinforcement Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Hyperparameter Optimization": 0.72,
    "Group Relative Policy Optimization": 0.81,
    "Policy Churn Regularization": 0.77,
    "Reinforcement Learning": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Hyperparameter Optimization",
        "canonical": "Hyperparameter Optimization",
        "aliases": [
          "HPO"
        ],
        "category": "broad_technical",
        "rationale": "Hyperparameter Optimization is a fundamental concept in machine learning, facilitating connections to various optimization techniques.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      },
      {
        "surface": "Group Relative Policy Optimization",
        "canonical": "Group Relative Policy Optimization",
        "aliases": [
          "GRPO"
        ],
        "category": "unique_technical",
        "rationale": "GRPO is a novel approach in the context of reinforcement learning, offering unique insights into optimization strategies.",
        "novelty_score": 0.78,
        "connectivity_score": 0.67,
        "specificity_score": 0.82,
        "link_intent_score": 0.81
      },
      {
        "surface": "Policy Churn Regularization",
        "canonical": "Policy Churn Regularization",
        "aliases": [
          "PCR"
        ],
        "category": "unique_technical",
        "rationale": "Policy Churn Regularization is a specific technique introduced to enhance training stability, relevant for advanced RL discussions.",
        "novelty_score": 0.72,
        "connectivity_score": 0.64,
        "specificity_score": 0.79,
        "link_intent_score": 0.77
      },
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is a key area in AI, crucial for linking to various learning and optimization frameworks.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "model performance",
      "experimental results",
      "baseline methods"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Hyperparameter Optimization",
      "resolved_canonical": "Hyperparameter Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Group Relative Policy Optimization",
      "resolved_canonical": "Group Relative Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.67,
        "specificity": 0.82,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Policy Churn Regularization",
      "resolved_canonical": "Policy Churn Regularization",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.64,
        "specificity": 0.79,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# GRPOformer: Advancing Hyperparameter Optimization via Group Relative Policy Optimization

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17105.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17105](https://arxiv.org/abs/2509.17105)

## 🔗 유사한 논문
- [[2025-09-19/Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (85.6% similar)
- [[2025-09-22/PVPO_ Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning_20250922|PVPO: Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning]] (83.6% similar)
- [[2025-09-23/Advancing Speech Understanding in Speech-Aware Language Models with GRPO_20250923|Advancing Speech Understanding in Speech-Aware Language Models with GRPO]] (82.8% similar)
- [[2025-09-23/GPO_ Learning from Critical Steps to Improve LLM Reasoning_20250923|GPO: Learning from Critical Steps to Improve LLM Reasoning]] (82.7% similar)
- [[2025-09-23/GEPO_ Group Expectation Policy Optimization for Stable Heterogeneous Reinforcement Learning_20250923|GEPO: Group Expectation Policy Optimization for Stable Heterogeneous Reinforcement Learning]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Hyperparameter Optimization|Hyperparameter Optimization]], [[keywords/Reinforcement Learning|Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Group Relative Policy Optimization|Group Relative Policy Optimization]], [[keywords/Policy Churn Regularization|Policy Churn Regularization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17105v1 Announce Type: new 
Abstract: Hyperparameter optimization (HPO) plays a critical role in improving model performance. Transformer-based HPO methods have shown great potential; however, existing approaches rely heavily on large-scale historical optimization trajectories and lack effective reinforcement learning (RL) techniques, thereby limiting their efficiency and performance improvements. Inspired by the success of Group Relative Policy Optimization (GRPO) in large language models (LLMs), we propose GRPOformer -- a novel hyperparameter optimization framework that integrates reinforcement learning (RL) with Transformers. In GRPOformer, Transformers are employed to generate new hyperparameter configurations from historical optimization trajectories, while GRPO enables rapid trajectory construction and optimization strategy learning from scratch. Moreover, we introduce Policy Churn Regularization (PCR) to enhance the stability of GRPO training. Experimental results on OpenML demonstrate that GRPOformer consistently outperforms baseline methods across diverse tasks, offering new insights into the application of RL for HPO.

## 📝 요약

이 논문은 하이퍼파라미터 최적화(HPO)의 성능을 향상시키기 위해 제안된 GRPOformer라는 새로운 프레임워크를 소개합니다. 기존의 Transformer 기반 HPO 방법들은 대규모의 과거 최적화 경로에 의존하고 강화 학습(RL) 기술이 부족하다는 한계가 있습니다. GRPOformer는 Transformer와 RL을 결합하여 이러한 문제를 해결합니다. Transformer는 과거 경로에서 새로운 하이퍼파라미터 구성을 생성하고, GRPO는 빠른 경로 구축과 최적화 전략 학습을 지원합니다. 또한, 정책 변동 규제(PCR)를 도입하여 GRPO 훈련의 안정성을 높였습니다. OpenML에서의 실험 결과, GRPOformer는 다양한 작업에서 기존 방법들을 능가하는 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 하이퍼파라미터 최적화(HPO)는 모델 성능 향상에 중요한 역할을 한다.
- 2. 기존의 Transformer 기반 HPO 방법은 대규모의 과거 최적화 경로에 의존하며, 강화 학습(RL) 기법이 부족하여 효율성과 성능 개선에 한계가 있다.
- 3. GRPOformer는 강화 학습과 Transformers를 통합하여 새로운 하이퍼파라미터 최적화 프레임워크를 제안한다.
- 4. GRPOformer는 OpenML 실험 결과에서 다양한 작업에서 기존 방법보다 일관되게 우수한 성능을 보였다.
- 5. Policy Churn Regularization(PCR)을 도입하여 GRPO 훈련의 안정성을 향상시켰다.


---

*Generated on 2025-09-24 01:47:05*