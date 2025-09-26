---
keywords:
  - Diffusion Models
  - Offline Reinforcement Learning
  - Inverse Dynamics Model
  - Temporal Difference Learning
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19538
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:38:27.478468",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Offline Reinforcement Learning",
    "Inverse Dynamics Model",
    "Temporal Difference Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diffusion Models": 0.82,
    "Offline Reinforcement Learning": 0.79,
    "Inverse Dynamics Model": 0.75,
    "Temporal Difference Learning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diffusion-based world models",
        "canonical": "Diffusion Models",
        "aliases": [
          "Diffusion-based models",
          "Diffusion world models"
        ],
        "category": "specific_connectable",
        "rationale": "Diffusion models are a key component in the proposed method, linking to advancements in model-based RL.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "Offline Reinforcement Learning",
        "canonical": "Offline Reinforcement Learning",
        "aliases": [
          "Offline RL"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus, connecting to a broad range of RL research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.68,
        "link_intent_score": 0.79
      },
      {
        "surface": "Inverse Dynamics Model",
        "canonical": "Inverse Dynamics Model",
        "aliases": [
          "IDM"
        ],
        "category": "unique_technical",
        "rationale": "A unique component of the proposed method, facilitating action inference.",
        "novelty_score": 0.71,
        "connectivity_score": 0.67,
        "specificity_score": 0.81,
        "link_intent_score": 0.75
      },
      {
        "surface": "Temporal Difference Learning",
        "canonical": "Temporal Difference Learning",
        "aliases": [
          "TD Learning"
        ],
        "category": "specific_connectable",
        "rationale": "Essential for understanding the compatibility with standard RL algorithms.",
        "novelty_score": 0.52,
        "connectivity_score": 0.83,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Diffusion-based world models",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Offline Reinforcement Learning",
      "resolved_canonical": "Offline Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.68,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Inverse Dynamics Model",
      "resolved_canonical": "Inverse Dynamics Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.71,
        "connectivity": 0.67,
        "specificity": 0.81,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Temporal Difference Learning",
      "resolved_canonical": "Temporal Difference Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.52,
        "connectivity": 0.83,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# DAWM: Diffusion Action World Models for Offline Reinforcement Learning via Action-Inferred Transitions

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19538.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19538](https://arxiv.org/abs/2509.19538)

## 🔗 유사한 논문
- [[2025-09-25/Wavelet Fourier Diffuser_ Frequency-Aware Diffusion Model for Reinforcement Learning_20250925|Wavelet Fourier Diffuser: Frequency-Aware Diffusion Model for Reinforcement Learning]] (86.5% similar)
- [[2025-09-22/DiffusionNFT_ Online Diffusion Reinforcement with Forward Process_20250922|DiffusionNFT: Online Diffusion Reinforcement with Forward Process]] (86.1% similar)
- [[2025-09-24/World4RL_ Diffusion World Models for Policy Refinement with Reinforcement Learning for Robotic Manipulation_20250924|World4RL: Diffusion World Models for Policy Refinement with Reinforcement Learning for Robotic Manipulation]] (85.1% similar)
- [[2025-09-18/TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (85.0% similar)
- [[2025-09-24/Diffusion Policies with Offline and Inverse Reinforcement Learning for Promoting Physical Activity in Older Adults Using Wearable Sensors_20250924|Diffusion Policies with Offline and Inverse Reinforcement Learning for Promoting Physical Activity in Older Adults Using Wearable Sensors]] (84.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Offline Reinforcement Learning|Offline Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Diffusion Models|Diffusion Models]], [[keywords/Temporal Difference Learning|Temporal Difference Learning]]
**⚡ Unique Technical**: [[keywords/Inverse Dynamics Model|Inverse Dynamics Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19538v1 Announce Type: cross 
Abstract: Diffusion-based world models have demonstrated strong capabilities in synthesizing realistic long-horizon trajectories for offline reinforcement learning (RL). However, many existing methods do not directly generate actions alongside states and rewards, limiting their compatibility with standard value-based offline RL algorithms that rely on one-step temporal difference (TD) learning. While prior work has explored joint modeling of states, rewards, and actions to address this issue, such formulations often lead to increased training complexity and reduced performance in practice. We propose \textbf{DAWM}, a diffusion-based world model that generates future state-reward trajectories conditioned on the current state, action, and return-to-go, paired with an inverse dynamics model (IDM) for efficient action inference. This modular design produces complete synthetic transitions suitable for one-step TD-based offline RL, enabling effective and computationally efficient training. Empirically, we show that conservative offline RL algorithms such as TD3BC and IQL benefit significantly from training on these augmented trajectories, consistently outperforming prior diffusion-based baselines across multiple tasks in the D4RL benchmark.

## 📝 요약

이 논문은 확산 기반 세계 모델인 DAWM을 제안하여 오프라인 강화 학습에서 현실적인 장기 궤적을 생성하는 데 중점을 둡니다. 기존 방법들은 상태와 보상만을 생성하여 일보차 시간차 학습을 사용하는 가치 기반 알고리즘과의 호환성이 떨어졌습니다. DAWM은 현재 상태, 행동, 목표 보상에 따라 미래 상태-보상 궤적을 생성하고, 역동학 모델(IDM)을 통해 효율적인 행동 추론을 가능하게 합니다. 이 모듈식 설계는 일보차 TD 기반 오프라인 강화 학습에 적합한 완전한 합성 전이를 제공합니다. 실험 결과, 보수적인 오프라인 강화 학습 알고리즘인 TD3BC와 IQL이 이러한 확장된 궤적을 활용하여 D4RL 벤치마크의 여러 작업에서 기존 확산 기반 모델을 능가하는 성능을 보였습니다.

## 🎯 주요 포인트

- 1. Diffusion 기반의 세계 모델은 오프라인 강화 학습에서 현실적인 장기 궤적을 합성하는 데 강력한 능력을 보여주었다.
- 2. 기존 방법들은 상태와 보상과 함께 행동을 직접 생성하지 않아, 표준 가치 기반 오프라인 강화 학습 알고리즘과의 호환성이 제한된다.
- 3. DAWM은 현재 상태, 행동, 그리고 반환 값에 조건화된 미래 상태-보상 궤적을 생성하며, 효율적인 행동 추론을 위한 역동학 모델(IDM)과 결합된다.
- 4. 이 모듈형 설계는 1단계 TD 기반 오프라인 강화 학습에 적합한 완전한 합성 전이를 생성하여 효과적이고 계산 효율적인 훈련을 가능하게 한다.
- 5. 보수적인 오프라인 강화 학습 알고리즘인 TD3BC와 IQL은 이러한 확장된 궤적을 활용한 훈련에서 상당한 성능 향상을 보이며, D4RL 벤치마크의 여러 작업에서 기존의 확산 기반 기준선을 일관되게 능가한다.


---

*Generated on 2025-09-25 15:38:27*