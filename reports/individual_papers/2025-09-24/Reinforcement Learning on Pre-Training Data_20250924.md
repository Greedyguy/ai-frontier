<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:16:59.258069",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning on Pre-Training Data",
    "Large Language Model",
    "Reinforcement Learning from Human Feedback",
    "Reinforcement Learning with Verifiable Rewards"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Reinforcement Learning on Pre-Training Data": 0.92,
    "Large Language Model": 0.85,
    "Reinforcement Learning from Human Feedback": 0.8,
    "Reinforcement Learning with Verifiable Rewards": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Reinforcement Learning on Pre-Training data",
        "canonical": "Reinforcement Learning on Pre-Training Data",
        "aliases": [
          "RLPT"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel training paradigm that extends reinforcement learning to pre-training data, offering unique insights and connections.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.92
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's discussion, linking to a broad range of topics in language model research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Reinforcement Learning from Human Feedback",
        "canonical": "Reinforcement Learning from Human Feedback",
        "aliases": [
          "RLHF"
        ],
        "category": "specific_connectable",
        "rationale": "A well-known strategy in reinforcement learning, providing a point of comparison for the novel RLPT approach.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Reinforcement Learning with Verifiable Rewards",
        "canonical": "Reinforcement Learning with Verifiable Rewards",
        "aliases": [
          "RLVR"
        ],
        "category": "specific_connectable",
        "rationale": "Another established method in reinforcement learning, relevant for contrasting with RLPT's approach.",
        "novelty_score": 0.45,
        "connectivity_score": 0.7,
        "specificity_score": 0.72,
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
      "candidate_surface": "Reinforcement Learning on Pre-Training data",
      "resolved_canonical": "Reinforcement Learning on Pre-Training Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.92
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Reinforcement Learning from Human Feedback",
      "resolved_canonical": "Reinforcement Learning from Human Feedback",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Reinforcement Learning with Verifiable Rewards",
      "resolved_canonical": "Reinforcement Learning with Verifiable Rewards",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.7,
        "specificity": 0.72,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Reinforcement Learning on Pre-Training Data

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19249.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.19249](https://arxiv.org/abs/2509.19249)

## 🔗 유사한 논문
- [[2025-09-23/Reinforcement Learning Meets Large Language Models_ A Survey of Advancements and Applications Across the LLM Lifecycle_20250923|Reinforcement Learning Meets Large Language Models: A Survey of Advancements and Applications Across the LLM Lifecycle]] (90.2% similar)
- [[2025-09-23/ConfClip_ Confidence-Weighted and Clipped Reward for Reinforcement Learning in LLMs_20250923|ConfClip: Confidence-Weighted and Clipped Reward for Reinforcement Learning in LLMs]] (87.6% similar)
- [[2025-09-22/Perception-R1_ Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward_20250922|Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward]] (87.5% similar)
- [[2025-09-23/Open Vision Reasoner_ Transferring Linguistic Cognitive Behavior for Visual Reasoning_20250923|Open Vision Reasoner: Transferring Linguistic Cognitive Behavior for Visual Reasoning]] (87.3% similar)
- [[2025-09-23/EvoCoT_ Overcoming the Exploration Bottleneck in Reinforcement Learning_20250923|EvoCoT: Overcoming the Exploration Bottleneck in Reinforcement Learning]] (86.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning from Human Feedback|Reinforcement Learning from Human Feedback]], [[keywords/Reinforcement Learning with Verifiable Rewards|Reinforcement Learning with Verifiable Rewards]]
**⚡ Unique Technical**: [[keywords/Reinforcement Learning on Pre-Training Data|Reinforcement Learning on Pre-Training Data]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19249v1 Announce Type: cross 
Abstract: The growing disparity between the exponential scaling of computational resources and the finite growth of high-quality text data now constrains conventional scaling approaches for large language models (LLMs). To address this challenge, we introduce Reinforcement Learning on Pre-Training data (RLPT), a new training-time scaling paradigm for optimizing LLMs. In contrast to prior approaches that scale training primarily through supervised learning, RLPT enables the policy to autonomously explore meaningful trajectories to learn from pre-training data and improve its capability through reinforcement learning (RL). While existing RL strategies such as reinforcement learning from human feedback (RLHF) and reinforcement learning with verifiable rewards (RLVR) rely on human annotation for reward construction, RLPT eliminates this dependency by deriving reward signals directly from pre-training data. Specifically, it adopts a next-segment reasoning objective, rewarding the policy for accurately predicting subsequent text segments conditioned on the preceding context. This formulation allows RL to be scaled on pre-training data, encouraging the exploration of richer trajectories across broader contexts and thereby fostering more generalizable reasoning skills. Extensive experiments on both general-domain and mathematical reasoning benchmarks across multiple models validate the effectiveness of RLPT. For example, when applied to Qwen3-4B-Base, RLPT yields absolute improvements of $3.0$, $5.1$, $8.1$, $6.0$, $6.6$, and $5.3$ on MMLU, MMLU-Pro, GPQA-Diamond, KOR-Bench, AIME24, and AIME25, respectively. The results further demonstrate favorable scaling behavior, suggesting strong potential for continued gains with more compute. In addition, RLPT provides a solid foundation, extending the reasoning boundaries of LLMs and enhancing RLVR performance.

## 📝 요약

이 논문은 대규모 언어 모델(LLM)의 학습 효율성을 높이기 위해 RLPT(Reinforcement Learning on Pre-Training data)라는 새로운 학습 패러다임을 제안합니다. 기존의 지도 학습 중심의 확장 방법과 달리, RLPT는 강화 학습(RL)을 통해 사전 학습 데이터에서 보상 신호를 직접 추출하여 모델이 자율적으로 학습할 수 있게 합니다. 이는 인간 주석에 의존하지 않고, 이전 문맥을 기반으로 다음 텍스트 세그먼트를 정확히 예측하는 목표를 설정하여 더 일반화된 추론 능력을 개발하도록 유도합니다. 다양한 모델과 벤치마크에서 실험한 결과, RLPT는 Qwen3-4B-Base 모델에서 MMLU, GPQA-Diamond 등 여러 평가 지표에서 성능 향상을 보였습니다. 이러한 결과는 RLPT가 LLM의 추론 능력을 확장하고, 더 많은 계산 자원을 활용할 경우 추가적인 성능 개선 가능성을 시사합니다.

## 🎯 주요 포인트

- 1. RLPT는 대규모 언어 모델(LLM)의 최적화를 위한 새로운 훈련 스케일링 패러다임으로, 강화 학습을 통해 사전 훈련 데이터를 탐색하고 학습합니다.
- 2. 기존의 RL 전략과 달리 RLPT는 보상 신호를 사전 훈련 데이터에서 직접 도출하여 인간 주석에 대한 의존성을 제거합니다.
- 3. RLPT는 다음 세그먼트 추론 목표를 채택하여 이전 맥락을 기반으로 후속 텍스트 세그먼트를 정확하게 예측하는 정책에 보상을 제공합니다.
- 4. 다양한 모델에 대한 일반 도메인 및 수학적 추론 벤치마크 실험에서 RLPT의 효과가 입증되었습니다.
- 5. RLPT는 LLM의 추론 경계를 확장하고 RLVR 성능을 향상시키며, 더 많은 컴퓨팅 자원을 통해 추가적인 성능 향상의 가능성을 시사합니다.


---

*Generated on 2025-09-24 14:16:59*