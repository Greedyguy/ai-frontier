<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:26:49.454867",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Safe Reinforcement Learning",
    "Partially Observable Markov Decision Processes",
    "Privileged Information",
    "Asymmetric Actor-Critic Structure"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Safe Reinforcement Learning": 0.85,
    "Partially Observable Markov Decision Processes": 0.79,
    "Privileged Information": 0.81,
    "Asymmetric Actor-Critic Structure": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Safe Reinforcement Learning",
        "canonical": "Safe Reinforcement Learning",
        "aliases": [
          "Safe RL"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's contribution and connects to the broader topic of reinforcement learning with a focus on safety.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      },
      {
        "surface": "Partially Observable Markov Decision Processes",
        "canonical": "Partially Observable Markov Decision Processes",
        "aliases": [
          "POMDPs"
        ],
        "category": "specific_connectable",
        "rationale": "This is a key concept in reinforcement learning, particularly relevant to the challenges addressed in the paper.",
        "novelty_score": 0.58,
        "connectivity_score": 0.83,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      },
      {
        "surface": "Privileged Information",
        "canonical": "Privileged Information",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The concept of using privileged information is a novel approach in the context of this research, enhancing the model's safety and performance.",
        "novelty_score": 0.72,
        "connectivity_score": 0.68,
        "specificity_score": 0.76,
        "link_intent_score": 0.81
      },
      {
        "surface": "Asymmetric Actor-Critic Structure",
        "canonical": "Asymmetric Actor-Critic Structure",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This structure is a specific innovation in the paper that contributes to improved performance in Safe RL.",
        "novelty_score": 0.7,
        "connectivity_score": 0.64,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Safe Reinforcement Learning",
      "resolved_canonical": "Safe Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Partially Observable Markov Decision Processes",
      "resolved_canonical": "Partially Observable Markov Decision Processes",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.83,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Privileged Information",
      "resolved_canonical": "Privileged Information",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.68,
        "specificity": 0.76,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Asymmetric Actor-Critic Structure",
      "resolved_canonical": "Asymmetric Actor-Critic Structure",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.64,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# PIGDreamer: Privileged Information Guided World Models for Safe Partially Observable Reinforcement Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2508.02159.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2508.02159](https://arxiv.org/abs/2508.02159)

## 🔗 유사한 논문
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (83.9% similar)
- [[2025-09-24/SPiDR_ A Simple Approach for Zero-Shot Safety in Sim-to-Real Transfer_20250924|SPiDR: A Simple Approach for Zero-Shot Safety in Sim-to-Real Transfer]] (83.1% similar)
- [[2025-09-23/Rectified Robust Policy Optimization for Model-Uncertain Constrained Reinforcement Learning without Strong Duality_20250923|Rectified Robust Policy Optimization for Model-Uncertain Constrained Reinforcement Learning without Strong Duality]] (82.8% similar)
- [[2025-09-23/Robust Reinforcement Learning with Dynamic Distortion Risk Measures_20250923|Robust Reinforcement Learning with Dynamic Distortion Risk Measures]] (82.2% similar)
- [[2025-09-23/Safe Guaranteed Dynamics Exploration with Probabilistic Models_20250923|Safe Guaranteed Dynamics Exploration with Probabilistic Models]] (82.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Partially Observable Markov Decision Processes|Partially Observable Markov Decision Processes]]
**⚡ Unique Technical**: [[keywords/Safe Reinforcement Learning|Safe Reinforcement Learning]], [[keywords/Privileged Information|Privileged Information]], [[keywords/Asymmetric Actor-Critic Structure|Asymmetric Actor-Critic Structure]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.02159v2 Announce Type: replace 
Abstract: Partial observability presents a significant challenge for Safe Reinforcement Learning (Safe RL), as it impedes the identification of potential risks and rewards. Leveraging specific types of privileged information during training to mitigate the effects of partial observability has yielded notable empirical successes. In this paper, we propose Asymmetric Constrained Partially Observable Markov Decision Processes (ACPOMDPs) to theoretically examine the advantages of incorporating privileged information in Safe RL. Building upon ACPOMDPs, we propose the Privileged Information Guided Dreamer (PIGDreamer), a model-based RL approach that leverages privileged information to enhance the agent's safety and performance through privileged representation alignment and an asymmetric actor-critic structure. Our empirical results demonstrate that PIGDreamer significantly outperforms existing Safe RL methods. Furthermore, compared to alternative privileged RL methods, our approach exhibits enhanced performance, robustness, and efficiency. Codes are available at: https://github.com/hggforget/PIGDreamer.

## 📝 요약

이 논문은 안전 강화 학습(Safe RL)에서 부분 관찰 가능성이 잠재적 위험과 보상의 식별을 방해하는 문제를 다룹니다. 이를 해결하기 위해 특정 특권 정보를 활용하는 방법이 제안되었습니다. 저자들은 이론적으로 특권 정보의 이점을 분석하기 위해 비대칭 제약 부분 관찰 마르코프 결정 과정(ACPOMDPs)을 제안하고, 이를 기반으로 특권 정보 안내 드리머(PIGDreamer)라는 모델 기반 RL 접근법을 개발했습니다. PIGDreamer는 특권 정보 활용을 통해 에이전트의 안전성과 성능을 향상시키며, 비대칭 액터-크리틱 구조를 사용합니다. 실험 결과, PIGDreamer는 기존의 안전 RL 방법들보다 뛰어난 성능을 보였으며, 다른 특권 RL 방법들에 비해 성능, 견고성, 효율성 면에서 우수함을 입증했습니다.

## 🎯 주요 포인트

- 1. 부분 관측은 안전 강화 학습(Safe RL)에서 잠재적 위험과 보상을 식별하는 데 어려움을 초래합니다.
- 2. 훈련 중 특정 유형의 특권 정보를 활용하여 부분 관측의 영향을 완화하는 것이 실질적인 성공을 거두었습니다.
- 3. 본 논문에서는 Asymmetric Constrained Partially Observable Markov Decision Processes (ACPOMDPs)를 제안하여 Safe RL에서 특권 정보의 이점을 이론적으로 분석합니다.
- 4. 제안된 PIGDreamer는 특권 정보 활용을 통해 에이전트의 안전성과 성능을 향상시키며, 기존의 Safe RL 방법을 능가하는 성능을 보입니다.
- 5. PIGDreamer는 다른 특권 RL 방법에 비해 성능, 견고성 및 효율성이 향상되었습니다.


---

*Generated on 2025-09-24 15:26:49*