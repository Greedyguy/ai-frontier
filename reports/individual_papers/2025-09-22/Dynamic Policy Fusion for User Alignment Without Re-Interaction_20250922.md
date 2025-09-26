---
keywords:
  - Deep Learning
  - Dynamic Policy Fusion
  - Zero-Shot Learning
  - Human Feedback
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2409.20016
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:33:18.178090",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Dynamic Policy Fusion",
    "Zero-Shot Learning",
    "Human Feedback"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.7,
    "Dynamic Policy Fusion": 0.78,
    "Zero-Shot Learning": 0.82,
    "Human Feedback": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep reinforcement learning",
        "canonical": "Deep Learning",
        "aliases": [
          "Deep RL"
        ],
        "category": "broad_technical",
        "rationale": "Deep Learning is a foundational technology for reinforcement learning, enhancing connectivity with other machine learning concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Dynamic policy fusion",
        "canonical": "Dynamic Policy Fusion",
        "aliases": [
          "Policy Fusion"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach proposed in the paper, crucial for understanding user alignment without re-interaction.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Zero-shot approach",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-Shot Learning is a trending concept that aligns with the paper's approach of not requiring additional interactions.",
        "novelty_score": 0.55,
        "connectivity_score": 0.9,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "Human feedback",
        "canonical": "Human Feedback",
        "aliases": [
          "User Feedback"
        ],
        "category": "unique_technical",
        "rationale": "Human Feedback is central to adapting policies to user-specific needs, enhancing the paper's methodology.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "task policy",
      "user-specific needs"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep reinforcement learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Dynamic policy fusion",
      "resolved_canonical": "Dynamic Policy Fusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Zero-shot approach",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.9,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Human feedback",
      "resolved_canonical": "Human Feedback",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Dynamic Policy Fusion for User Alignment Without Re-Interaction

**Korean Title:** 사용자 정렬을 위한 동적 정책 융합: 재상호작용 없이

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2409.20016.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2409.20016](https://arxiv.org/abs/2409.20016)

## 🔗 유사한 논문
- [[2025-09-19/Online Learning of Deceptive Policies under Intermittent Observation_20250919|Online Learning of Deceptive Policies under Intermittent Observation]] (83.4% similar)
- [[2025-09-19/Zero-Shot LLMs in Human-in-the-Loop RL_ Replacing Human Feedback for Reward Shaping_20250919|Zero-Shot LLMs in Human-in-the-Loop RL: Replacing Human Feedback for Reward Shaping]] (82.5% similar)
- [[2025-09-19/Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (81.9% similar)
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (81.7% similar)
- [[2025-09-19/Emergent Alignment via Competition_20250919|Emergent Alignment via Competition]] (81.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Dynamic Policy Fusion|Dynamic Policy Fusion]], [[keywords/Human Feedback|Human Feedback]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2409.20016v4 Announce Type: replace 
Abstract: Deep reinforcement learning (RL) policies, although optimal in terms of task rewards, may not align with the personal preferences of human users. To ensure this alignment, a naive solution would be to retrain the agent using a reward function that encodes the user's specific preferences. However, such a reward function is typically not readily available, and as such, retraining the agent from scratch can be prohibitively expensive. We propose a more practical approach - to adapt the already trained policy to user-specific needs with the help of human feedback. To this end, we infer the user's intent through trajectory-level feedback and combine it with the trained task policy via a theoretically grounded dynamic policy fusion approach. As our approach collects human feedback on the very same trajectories used to learn the task policy, it does not require any additional interactions with the environment, making it a zero-shot approach. We empirically demonstrate in a number of environments that our proposed dynamic policy fusion approach consistently achieves the intended task while simultaneously adhering to user-specific needs.

## 🔍 Abstract (한글 번역)

arXiv:2409.20016v4 발표 유형: 교체  
초록: 심층 강화 학습(RL) 정책은 과제 보상 측면에서 최적일 수 있지만, 인간 사용자의 개인적 선호와 일치하지 않을 수 있습니다. 이러한 일치를 보장하기 위한 단순한 해결책은 사용자의 특정 선호를 암호화하는 보상 함수를 사용하여 에이전트를 재학습하는 것입니다. 그러나 이러한 보상 함수는 일반적으로 쉽게 구할 수 없으며, 따라서 에이전트를 처음부터 재학습하는 것은 비용이 많이 들 수 있습니다. 우리는 보다 실용적인 접근법을 제안합니다. 이미 학습된 정책을 인간의 피드백을 통해 사용자별 요구에 맞게 조정하는 것입니다. 이를 위해 우리는 궤적 수준의 피드백을 통해 사용자의 의도를 추론하고, 이 정보를 이론적으로 기반을 둔 동적 정책 융합 접근법을 통해 학습된 과제 정책과 결합합니다. 우리의 접근법은 과제 정책을 학습하는 데 사용된 동일한 궤적에서 인간의 피드백을 수집하므로 환경과의 추가적인 상호작용이 필요하지 않으며, 이는 제로샷 접근법입니다. 우리는 여러 환경에서 제안된 동적 정책 융합 접근법이 의도된 과제를 일관되게 달성하면서 동시에 사용자별 요구를 충족시키는 것을 실증적으로 입증합니다.

## 📝 요약

이 논문은 심층 강화 학습(RL) 정책이 사용자 개인의 선호와 일치하지 않을 수 있음을 지적하며, 이를 해결하기 위해 사용자 피드백을 활용한 정책 적응 방법을 제안합니다. 기존의 정책을 사용자 요구에 맞게 조정하기 위해 경로 수준의 피드백을 통해 사용자의 의도를 추론하고, 이 정보를 이론적으로 기반한 동적 정책 융합 접근법으로 결합합니다. 이 방법은 추가적인 환경 상호작용 없이 기존 경로에서 피드백을 수집하여 제로샷 방식으로 작동합니다. 여러 환경에서 실험을 통해 제안된 방법이 사용자 요구를 충족하면서도 과제를 효과적으로 수행함을 입증했습니다.

## 🎯 주요 포인트

- 1. 심층 강화 학습 정책은 인간 사용자의 개인적 선호와 일치하지 않을 수 있다.
- 2. 사용자 선호를 반영하기 위해 에이전트를 처음부터 재훈련하는 것은 비용이 많이 들 수 있다.
- 3. 제안된 방법은 이미 훈련된 정책을 사용자 요구에 맞게 인간 피드백을 통해 적응시키는 것이다.
- 4. 경로 수준의 피드백을 통해 사용자의 의도를 추론하고, 이를 이론적으로 기반한 동적 정책 융합 접근법으로 결합한다.
- 5. 제안된 방법은 환경과의 추가 상호작용 없이 사용자 요구를 충족시키면서도 의도된 작업을 달성한다.


---

*Generated on 2025-09-23 09:33:18*