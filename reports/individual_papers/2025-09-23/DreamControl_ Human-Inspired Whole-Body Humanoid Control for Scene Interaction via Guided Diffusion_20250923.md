---
keywords:
  - DreamControl
  - Diffusion Models
  - Reinforcement Learning
  - Sim-to-Real Transfer
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.14353
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:31:58.034742",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "DreamControl",
    "Diffusion Models",
    "Reinforcement Learning",
    "Sim-to-Real Transfer"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "DreamControl": 0.8,
    "Diffusion Models": 0.78,
    "Reinforcement Learning": 0.8,
    "Sim-to-Real Transfer": 0.85
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "DreamControl",
        "canonical": "DreamControl",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "DreamControl is a novel methodology combining diffusion models and reinforcement learning for humanoid control, offering unique insights into sim-to-real transfer.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "diffusion models",
        "canonical": "Diffusion Models",
        "aliases": [
          "diffusion prior"
        ],
        "category": "broad_technical",
        "rationale": "Diffusion models are central to the methodology, facilitating natural motion generation and sim-to-real transfer.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is a key component of DreamControl, guiding humanoid tasks in simulation.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "sim-to-real transfer",
        "canonical": "Sim-to-Real Transfer",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Sim-to-real transfer is crucial for applying simulated learning to real-world humanoid robots.",
        "novelty_score": 0.7,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.85
      }
    ],
    "ban_list_suggestions": [
      "whole-body humanoid skills",
      "human motion data",
      "object interaction"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "DreamControl",
      "resolved_canonical": "DreamControl",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "diffusion models",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "sim-to-real transfer",
      "resolved_canonical": "Sim-to-Real Transfer",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.85
      }
    }
  ]
}
-->

# DreamControl: Human-Inspired Whole-Body Humanoid Control for Scene Interaction via Guided Diffusion

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.14353.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.14353](https://arxiv.org/abs/2509.14353)

## 🔗 유사한 논문
- [[2025-09-18/Embracing Bulky Objects with Humanoid Robots_ Whole-Body Manipulation with Reinforcement Learning_20250918|Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning]] (84.1% similar)
- [[2025-09-23/MaskedManipulator_ Versatile Whole-Body Manipulation_20250923|MaskedManipulator: Versatile Whole-Body Manipulation]] (83.4% similar)
- [[2025-09-23/HuMam_ Humanoid Motion Control via End-to-End Deep Reinforcement Learning with Mamba_20250923|HuMam: Humanoid Motion Control via End-to-End Deep Reinforcement Learning with Mamba]] (82.9% similar)
- [[2025-09-18/TrajBooster_ Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning_20250918|TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning]] (82.4% similar)
- [[2025-09-22/Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning_20250922|Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning]] (82.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Diffusion Models|Diffusion Models]], [[keywords/Reinforcement Learning|Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Sim-to-Real Transfer|Sim-to-Real Transfer]]
**⚡ Unique Technical**: [[keywords/DreamControl|DreamControl]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14353v2 Announce Type: replace-cross 
Abstract: We introduce DreamControl, a novel methodology for learning autonomous whole-body humanoid skills. DreamControl leverages the strengths of diffusion models and Reinforcement Learning (RL): our core innovation is the use of a diffusion prior trained on human motion data, which subsequently guides an RL policy in simulation to complete specific tasks of interest (e.g., opening a drawer or picking up an object). We demonstrate that this human motion-informed prior allows RL to discover solutions unattainable by direct RL, and that diffusion models inherently promote natural looking motions, aiding in sim-to-real transfer. We validate DreamControl's effectiveness on a Unitree G1 robot across a diverse set of challenging tasks involving simultaneous lower and upper body control and object interaction.

## 📝 요약

DreamControl은 인간형 로봇의 자율적인 전신 기술 학습을 위한 새로운 방법론입니다. 이 방법론은 확산 모델과 강화 학습(RL)의 장점을 결합하여, 인간 동작 데이터로 훈련된 확산 사전 모델을 사용해 RL 정책이 특정 작업(예: 서랍 열기, 물건 집기)을 수행하도록 안내합니다. 이를 통해 직접적인 RL로는 불가능한 솔루션을 발견할 수 있으며, 자연스러운 동작을 촉진하여 시뮬레이션에서 현실로의 전환을 돕습니다. DreamControl의 효과는 Unitree G1 로봇을 통해 다양한 복잡한 작업에서 검증되었습니다.

## 🎯 주요 포인트

- 1. DreamControl은 인간 모션 데이터를 기반으로 학습된 확산 사전(prior)을 활용하여 강화 학습(RL) 정책을 안내하는 새로운 방법론입니다.
- 2. DreamControl은 서랍 열기나 물건 집기와 같은 특정 과제를 완료하기 위해 시뮬레이션에서 RL 정책을 안내합니다.
- 3. 인간 모션 정보를 활용한 사전은 직접 RL로는 불가능한 솔루션을 발견할 수 있게 하며, 자연스러운 모션을 촉진하여 시뮬레이션에서 실제로의 전환을 돕습니다.
- 4. DreamControl은 Unitree G1 로봇을 사용하여 하체와 상체의 동시 제어 및 물체 상호작용을 포함한 다양한 도전 과제에서 그 효과가 입증되었습니다.


---

*Generated on 2025-09-24 01:31:58*