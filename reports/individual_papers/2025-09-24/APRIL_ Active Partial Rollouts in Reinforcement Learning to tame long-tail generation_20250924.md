<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:51:59.561392",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Active Partial Rollouts",
    "Large Language Model",
    "Rollout Generation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Reinforcement Learning": 0.85,
    "Active Partial Rollouts": 0.88,
    "Large Language Model": 0.82,
    "Rollout Generation": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is central to the paper's methodology and connects to a wide range of related research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Active Partial Rollouts in Reinforcement Learning",
        "canonical": "Active Partial Rollouts",
        "aliases": [
          "APRIL"
        ],
        "category": "unique_technical",
        "rationale": "APRIL is a novel method introduced in the paper, crucial for understanding its contributions to RL efficiency.",
        "novelty_score": 0.95,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are a key application area for the discussed RL techniques, providing strong connectivity to related fields.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Rollout Generation",
        "canonical": "Rollout Generation",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Rollout Generation is a critical process in RL discussed extensively in the paper, highlighting its computational challenges.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Active Partial Rollouts in Reinforcement Learning",
      "resolved_canonical": "Active Partial Rollouts",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Rollout Generation",
      "resolved_canonical": "Rollout Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# APRIL: Active Partial Rollouts in Reinforcement Learning to tame long-tail generation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18521.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18521](https://arxiv.org/abs/2509.18521)

## 🔗 유사한 논문
- [[2025-09-22/RLinf_ Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation_20250922|RLinf: Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation]] (88.0% similar)
- [[2025-09-23/Reinforcement Learning Meets Large Language Models_ A Survey of Advancements and Applications Across the LLM Lifecycle_20250923|Reinforcement Learning Meets Large Language Models: A Survey of Advancements and Applications Across the LLM Lifecycle]] (86.0% similar)
- [[2025-09-23/ConfClip_ Confidence-Weighted and Clipped Reward for Reinforcement Learning in LLMs_20250923|ConfClip: Confidence-Weighted and Clipped Reward for Reinforcement Learning in LLMs]] (85.6% similar)
- [[2025-09-23/Towards Sample-Efficiency and Generalization of Transfer and Inverse Reinforcement Learning_ A Comprehensive Literature Review_20250923|Towards Sample-Efficiency and Generalization of Transfer and Inverse Reinforcement Learning: A Comprehensive Literature Review]] (85.5% similar)
- [[2025-09-19/Zero-Shot LLMs in Human-in-the-Loop RL_ Replacing Human Feedback for Reward Shaping_20250919|Zero-Shot LLMs in Human-in-the-Loop RL: Replacing Human Feedback for Reward Shaping]] (85.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]], [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Active Partial Rollouts|Active Partial Rollouts]], [[keywords/Rollout Generation|Rollout Generation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18521v1 Announce Type: cross 
Abstract: Reinforcement learning (RL) has become a cornerstone in advancing large-scale pre-trained language models (LLMs). Successive generations, including GPT-o series, DeepSeek-R1, Kimi-K1.5, Grok 4, and GLM-4.5, have relied on large-scale RL training to enhance reasoning and coding capabilities. To meet the community's growing RL needs, numerous RL frameworks have been proposed. Most of these frameworks primarily rely on inference engines for rollout generation and training engines for policy updates. However, RL training remains computationally expensive, with rollout generation accounting for more than 90% of total runtime. In addition, its efficiency is often constrained by the long-tail distribution of rollout response lengths, where a few lengthy responses stall entire batches, leaving GPUs idle and underutilized. As model and rollout sizes continue to grow, this bottleneck increasingly limits scalability. To address this challenge, we propose Active Partial Rollouts in Reinforcement Learning (APRIL), which mitigates long-tail inefficiency. In the rollout phase, APRIL over-provisions rollout requests, terminates once the target number of responses is reached, and recycles incomplete responses for continuation in future steps. This strategy ensures that no rollouts are discarded while substantially reducing GPU idle time. Experiments show that APRIL improves rollout throughput by at most 44% across commonly used RL algorithms (GRPO, DAPO, GSPO), accelerates convergence, and achieves at most 8% higher final accuracy across tasks. Moreover, APRIL is both framework and hardware agnostic, already integrated into the slime RL framework, and deployable on NVIDIA and AMD GPUs alike. Taken together, this work unifies system-level and algorithmic considerations in proposing APRIL, with the aim of advancing RL training efficiency and inspiring further optimizations in RL systems.

## 📝 요약

강화 학습(RL)은 대규모 사전 학습 언어 모델(LLM)의 발전에 핵심 역할을 하고 있습니다. 그러나 RL 훈련은 계산 비용이 많이 들며, 롤아웃 생성이 전체 실행 시간의 90% 이상을 차지합니다. 이에 따라 롤아웃 응답 길이의 긴 꼬리 분포로 인해 효율성이 제한됩니다. 이를 해결하기 위해, 우리는 강화 학습에서의 능동적 부분 롤아웃(APRIL)을 제안합니다. APRIL은 롤아웃 요청을 초과할당하고 목표 응답 수에 도달하면 종료하며, 불완전한 응답을 재활용하여 GPU 유휴 시간을 줄입니다. 실험 결과, APRIL은 롤아웃 처리량을 최대 44% 개선하고, 수렴 속도를 가속화하며, 최종 정확도를 최대 8% 향상시킵니다. APRIL은 프레임워크 및 하드웨어에 구애받지 않으며, 슬라임 RL 프레임워크에 통합되어 NVIDIA 및 AMD GPU에서 사용할 수 있습니다. 이 연구는 RL 훈련 효율성을 높이고 추가 최적화를 위한 영감을 제공합니다.

## 🎯 주요 포인트

- 1. 강화 학습(RL)은 대규모 사전 학습된 언어 모델(LLMs)의 발전에 핵심적인 역할을 하고 있으며, 이를 통해 추론 및 코딩 능력을 향상시키고 있다.
- 2. RL 훈련은 계산 비용이 많이 들며, 롤아웃 생성이 전체 실행 시간의 90% 이상을 차지하여 병목 현상이 발생한다.
- 3. APRIL은 롤아웃 요청을 초과 할당하고 목표 응답 수에 도달하면 종료하며, 미완성 응답을 재활용하여 GPU 유휴 시간을 크게 줄인다.
- 4. APRIL은 일반적으로 사용되는 RL 알고리즘에서 롤아웃 처리량을 최대 44% 개선하고, 수렴 속도를 가속화하며, 최종 정확도를 최대 8% 향상시킨다.
- 5. APRIL은 프레임워크 및 하드웨어에 구애받지 않으며, 이미 슬라임 RL 프레임워크에 통합되어 NVIDIA 및 AMD GPU에서 배포 가능하다.


---

*Generated on 2025-09-24 13:51:59*