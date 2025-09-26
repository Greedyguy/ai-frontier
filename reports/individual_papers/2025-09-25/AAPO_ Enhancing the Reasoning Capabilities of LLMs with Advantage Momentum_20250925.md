---
keywords:
  - Large Language Model
  - Reinforcement Learning
  - Advantage-Augmented Policy Optimization
  - Group Relative Policy Optimization
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2505.14264
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T17:07:40.848835",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Reinforcement Learning",
    "Advantage-Augmented Policy Optimization",
    "Group Relative Policy Optimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Reinforcement Learning": 0.8,
    "Advantage-Augmented Policy Optimization": 0.78,
    "Group Relative Policy Optimization": 0.72
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
        "rationale": "Large Language Models are central to the paper's focus on enhancing reasoning capabilities, providing a strong link to related works in NLP.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is a key method used in the paper, connecting it to a broad range of machine learning literature.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "Advantage-Augmented Policy Optimization",
        "canonical": "Advantage-Augmented Policy Optimization",
        "aliases": [
          "AAPO"
        ],
        "category": "unique_technical",
        "rationale": "AAPO is a novel algorithm introduced in the paper, providing a unique contribution to the field of RL-based optimization methods.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Group Relative Policy Optimization",
        "canonical": "Group Relative Policy Optimization",
        "aliases": [
          "GRPO"
        ],
        "category": "unique_technical",
        "rationale": "GRPO is discussed as a comparative method, linking the paper to existing RL optimization techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "chain-of-thought",
      "cross-entropy loss"
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
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Advantage-Augmented Policy Optimization",
      "resolved_canonical": "Advantage-Augmented Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Group Relative Policy Optimization",
      "resolved_canonical": "Group Relative Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# AAPO: Enhancing the Reasoning Capabilities of LLMs with Advantage Momentum

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2505.14264.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2505.14264](https://arxiv.org/abs/2505.14264)

## 🔗 유사한 논문
- [[2025-09-25/Kalman Filter Enhanced GRPO for Reinforcement Learning-Based Language Model Reasoning_20250925|Kalman Filter Enhanced GRPO for Reinforcement Learning-Based Language Model Reasoning]] (90.0% similar)
- [[2025-09-23/GPO_ Learning from Critical Steps to Improve LLM Reasoning_20250923|GPO: Learning from Critical Steps to Improve LLM Reasoning]] (89.6% similar)
- [[2025-09-24/NGRPO_ Negative-enhanced Group Relative Policy Optimization_20250924|NGRPO: Negative-enhanced Group Relative Policy Optimization]] (89.4% similar)
- [[2025-09-23/GRPO-LEAD_ A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models_20250923|GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models]] (88.9% similar)
- [[2025-09-25/Stepwise Guided Policy Optimization_ Coloring your Incorrect Reasoning in GRPO_20250925|Stepwise Guided Policy Optimization: Coloring your Incorrect Reasoning in GRPO]] (88.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]], [[keywords/Reinforcement Learning|Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Advantage-Augmented Policy Optimization|Advantage-Augmented Policy Optimization]], [[keywords/Group Relative Policy Optimization|Group Relative Policy Optimization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.14264v2 Announce Type: replace 
Abstract: Reinforcement learning (RL) has emerged as an effective approach for enhancing the reasoning capabilities of large language models (LLMs), especially in scenarios where supervised fine-tuning (SFT) falls short due to limited chain-of-thought (CoT) data. Among RL-based post-training methods, group relative advantage estimation, as exemplified by Group Relative Policy Optimization (GRPO), has attracted considerable attention for eliminating the dependency on the value model, thereby simplifying training compared to traditional approaches like Proximal Policy Optimization (PPO). However, we observe that exsiting group relative advantage estimation method still suffers from training inefficiencies, particularly when the estimated advantage approaches zero. To address this limitation, we propose Advantage-Augmented Policy Optimization (AAPO), a novel RL algorithm that optimizes the cross-entropy (CE) loss using advantages enhanced through a momentum-based estimation scheme. This approach effectively mitigates the inefficiencies associated with group relative advantage estimation. Experimental results on multiple mathematical reasoning benchmarks demonstrate the superior performance of AAPO.

## 📝 요약

이 논문은 강화 학습(RL)을 통해 대형 언어 모델(LLM)의 추론 능력을 향상시키는 방법을 제시합니다. 기존의 감독 학습(SFT)이 제한된 사고 과정 데이터로 인해 한계를 보일 때, RL 기반의 후속 학습 방법이 효과적임을 강조합니다. 특히, 그룹 상대 이점 추정 방식을 사용하는 Group Relative Policy Optimization (GRPO)이 가치 모델에 대한 의존성을 제거하여 전통적인 방법보다 훈련을 단순화하지만, 이점 추정치가 0에 가까워질 때 훈련 비효율성이 발생하는 문제를 지적합니다. 이를 해결하기 위해, 이 논문은 모멘텀 기반 추정 방식을 통해 이점을 강화하여 교차 엔트로피 손실을 최적화하는 새로운 RL 알고리즘인 Advantage-Augmented Policy Optimization (AAPO)을 제안합니다. 실험 결과, AAPO가 여러 수학적 추론 벤치마크에서 우수한 성능을 보임을 입증했습니다.

## 🎯 주요 포인트

- 1. 강화 학습(RL)은 대형 언어 모델(LLM)의 추론 능력을 향상시키는 효과적인 방법으로 부상하고 있습니다.
- 2. Group Relative Policy Optimization (GRPO)은 가치 모델에 대한 의존성을 제거하여 전통적인 방법보다 훈련을 단순화합니다.
- 3. 기존의 그룹 상대적 이점 추정 방법은 훈련 비효율성 문제를 겪고 있으며, 이를 해결하기 위해 Advantage-Augmented Policy Optimization (AAPO)을 제안합니다.
- 4. AAPO는 모멘텀 기반 추정 방식을 통해 이점을 강화하여 교차 엔트로피(CE) 손실을 최적화하는 새로운 RL 알고리즘입니다.
- 5. 여러 수학적 추론 벤치마크에서 AAPO의 우수한 성능이 실험 결과로 입증되었습니다.


---

*Generated on 2025-09-25 17:07:40*