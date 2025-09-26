---
keywords:
  - Preference-based Reinforcement Learning
  - Diffusion Classifier
  - Conditional Diffusion Reward
  - Reinforcement Learning
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2503.01143
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T17:06:26.676580",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Preference-based Reinforcement Learning",
    "Diffusion Classifier",
    "Conditional Diffusion Reward",
    "Reinforcement Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Preference-based Reinforcement Learning": 0.75,
    "Diffusion Classifier": 0.7,
    "Conditional Diffusion Reward": 0.65,
    "Reinforcement Learning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Offline Preference-based Reinforcement Learning",
        "canonical": "Preference-based Reinforcement Learning",
        "aliases": [
          "PbRL"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and represents a specific approach within reinforcement learning, facilitating connections to related works.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Diffusion Classifier",
        "canonical": "Diffusion Classifier",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Introduces a novel classification method that is pivotal to the paper's methodology, offering potential links to diffusion models.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Conditional Diffusion Preference-based Reward",
        "canonical": "Conditional Diffusion Reward",
        "aliases": [
          "C-DPR"
        ],
        "category": "unique_technical",
        "rationale": "Represents an advanced method proposed in the paper, enhancing the diffusion-based approach with conditional elements.",
        "novelty_score": 0.75,
        "connectivity_score": 0.55,
        "specificity_score": 0.9,
        "link_intent_score": 0.65
      },
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "A foundational concept that underpins the entire study, essential for linking to the broader field of machine learning.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "trajectory-wise preferences",
      "step-wise reward"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Offline Preference-based Reinforcement Learning",
      "resolved_canonical": "Preference-based Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Diffusion Classifier",
      "resolved_canonical": "Diffusion Classifier",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Conditional Diffusion Preference-based Reward",
      "resolved_canonical": "Conditional Diffusion Reward",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.55,
        "specificity": 0.9,
        "link_intent": 0.65
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
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Diffusion Classifier-Driven Reward for Offline Preference-based Reinforcement Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2503.01143.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2503.01143](https://arxiv.org/abs/2503.01143)

## 🔗 유사한 논문
- [[2025-09-18/TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (85.2% similar)
- [[2025-09-25/DAWM_ Diffusion Action World Models for Offline Reinforcement Learning via Action-Inferred Transitions_20250925|DAWM: Diffusion Action World Models for Offline Reinforcement Learning via Action-Inferred Transitions]] (84.9% similar)
- [[2025-09-24/Online Process Reward Leanring for Agentic Reinforcement Learning_20250924|Online Process Reward Leanring for Agentic Reinforcement Learning]] (84.8% similar)
- [[2025-09-24/MiCRo_ Mixture Modeling and Context-aware Routing for Personalized Preference Learning_20250924|MiCRo: Mixture Modeling and Context-aware Routing for Personalized Preference Learning]] (84.3% similar)
- [[2025-09-25/Wavelet Fourier Diffuser_ Frequency-Aware Diffusion Model for Reinforcement Learning_20250925|Wavelet Fourier Diffuser: Frequency-Aware Diffusion Model for Reinforcement Learning]] (84.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Preference-based Reinforcement Learning|Preference-based Reinforcement Learning]], [[keywords/Diffusion Classifier|Diffusion Classifier]], [[keywords/Conditional Diffusion Reward|Conditional Diffusion Reward]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.01143v3 Announce Type: replace 
Abstract: Offline preference-based reinforcement learning (PbRL) mitigates the need for reward definition, aligning with human preferences via preference-driven reward feedback without interacting with the environment. However, trajectory-wise preference labels are difficult to meet the precise learning of step-wise reward, thereby affecting the performance of downstream algorithms. To alleviate the insufficient step-wise reward caused by trajectory-wise preferences, we propose a novel preference-based reward acquisition method: Diffusion Preference-based Reward (DPR). DPR directly treats step-wise preference-based reward acquisition as a binary classification and utilizes the robustness of diffusion classifiers to infer step-wise rewards discriminatively. In addition, to further utilize trajectory-wise preference information, we propose Conditional Diffusion Preference-based Reward (C-DPR), which conditions on trajectory-wise preference labels to enhance reward inference. We apply the above methods to existing offline RL algorithms, and a series of experimental results demonstrate that the diffusion classifier-driven reward outperforms the previous reward acquisition method with the Bradley-Terry model.

## 📝 요약

이 논문은 오프라인 선호 기반 강화 학습(PbRL)에서 경로 단위의 선호 레이블이 단계별 보상 학습에 어려움을 주는 문제를 해결하기 위해 새로운 보상 획득 방법인 확산 선호 기반 보상(DPR)을 제안합니다. DPR은 단계별 보상 획득을 이진 분류로 처리하여 확산 분류기의 강력함을 활용해 보상을 추론합니다. 또한, 경로 단위의 선호 정보를 활용하기 위해 조건부 확산 선호 기반 보상(C-DPR)을 제안하여 보상 추론을 강화합니다. 실험 결과, 확산 분류기를 활용한 보상이 기존의 Bradley-Terry 모델 기반 보상 획득 방법보다 우수함을 보여줍니다.

## 🎯 주요 포인트

- 1. 오프라인 선호 기반 강화 학습(PbRL)은 환경과의 상호작용 없이 선호 기반 보상 피드백을 통해 인간의 선호와 일치하는 보상을 정의하는 문제를 해결합니다.
- 2. 궤적 기반 선호 레이블은 단계별 보상의 정확한 학습을 충족시키기 어려워, 다운스트림 알고리즘의 성능에 영향을 미칩니다.
- 3. Diffusion Preference-based Reward (DPR)은 단계별 선호 기반 보상 획득을 이진 분류로 처리하여, 확산 분류기의 강건성을 활용해 단계별 보상을 판별적으로 추론합니다.
- 4. Conditional Diffusion Preference-based Reward (C-DPR)은 궤적 기반 선호 레이블을 조건으로 하여 보상 추론을 강화합니다.
- 5. 실험 결과, 확산 분류기 기반 보상이 Bradley-Terry 모델을 사용한 이전 보상 획득 방법보다 뛰어난 성능을 보였습니다.


---

*Generated on 2025-09-25 17:06:26*