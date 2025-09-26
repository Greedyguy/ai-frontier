---
keywords:
  - Imitation Learning
  - ReSET Algorithm
  - Teleoperation Data
  - Diffusion Policies
  - Human Videos
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.18043
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:30:06.683387",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Imitation Learning",
    "ReSET Algorithm",
    "Teleoperation Data",
    "Diffusion Policies",
    "Human Videos"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Imitation Learning": 0.8,
    "ReSET Algorithm": 0.88,
    "Teleoperation Data": 0.78,
    "Diffusion Policies": 0.77,
    "Human Videos": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Imitation Learning",
        "canonical": "Imitation Learning",
        "aliases": [
          "IL"
        ],
        "category": "specific_connectable",
        "rationale": "Imitation Learning is central to the paper's approach and connects to a wide range of learning methods.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "ReSET algorithm",
        "canonical": "ReSET Algorithm",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "ReSET is a novel algorithm introduced in the paper, crucial for understanding the proposed method.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "Teleoperation data",
        "canonical": "Teleoperation Data",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Teleoperation data is a key component in training the algorithm, linking to data collection techniques.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.72,
        "link_intent_score": 0.78
      },
      {
        "surface": "Diffusion policies",
        "canonical": "Diffusion Policies",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Diffusion policies are compared against the proposed method, providing context for evaluation.",
        "novelty_score": 0.58,
        "connectivity_score": 0.7,
        "specificity_score": 0.68,
        "link_intent_score": 0.77
      },
      {
        "surface": "Human videos",
        "canonical": "Human Videos",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Human videos are used for action prediction, linking to human-robot interaction studies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.71,
        "link_intent_score": 0.79
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
      "candidate_surface": "Imitation Learning",
      "resolved_canonical": "Imitation Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "ReSET algorithm",
      "resolved_canonical": "ReSET Algorithm",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Teleoperation data",
      "resolved_canonical": "Teleoperation Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.72,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Diffusion policies",
      "resolved_canonical": "Diffusion Policies",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.7,
        "specificity": 0.68,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Human videos",
      "resolved_canonical": "Human Videos",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.71,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Prepare Before You Act: Learning From Humans to Rearrange Initial States

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18043.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.18043](https://arxiv.org/abs/2509.18043)

## 🔗 유사한 논문
- [[2025-09-23/Latent Policy Steering with Embodiment-Agnostic Pretrained World Models_20250923|Latent Policy Steering with Embodiment-Agnostic Pretrained World Models]] (84.6% similar)
- [[2025-09-23/Look, Focus, Act_ Efficient and Robust Robot Learning via Human Gaze and Foveated Vision Transformers_20250923|Look, Focus, Act: Efficient and Robust Robot Learning via Human Gaze and Foveated Vision Transformers]] (82.6% similar)
- [[2025-09-18/Robot Control Stack_ A Lean Ecosystem for Robot Learning at Scale_20250918|Robot Control Stack: A Lean Ecosystem for Robot Learning at Scale]] (82.6% similar)
- [[2025-09-22/Uncertainty-Based Smooth Policy Regularisation for Reinforcement Learning with Few Demonstrations_20250922|Uncertainty-Based Smooth Policy Regularisation for Reinforcement Learning with Few Demonstrations]] (82.5% similar)
- [[2025-09-19/Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring_20250919|Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring]] (82.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Imitation Learning|Imitation Learning]], [[keywords/Teleoperation Data|Teleoperation Data]], [[keywords/Diffusion Policies|Diffusion Policies]], [[keywords/Human Videos|Human Videos]]
**⚡ Unique Technical**: [[keywords/ReSET Algorithm|ReSET Algorithm]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18043v1 Announce Type: cross 
Abstract: Imitation learning (IL) has proven effective across a wide range of manipulation tasks. However, IL policies often struggle when faced with out-of-distribution observations; for instance, when the target object is in a previously unseen position or occluded by other objects. In these cases, extensive demonstrations are needed for current IL methods to reach robust and generalizable behaviors. But when humans are faced with these sorts of atypical initial states, we often rearrange the environment for more favorable task execution. For example, a person might rotate a coffee cup so that it is easier to grasp the handle, or push a box out of the way so they can directly grasp their target object. In this work we seek to equip robot learners with the same capability: enabling robots to prepare the environment before executing their given policy. We propose ReSET, an algorithm that takes initial states -- which are outside the policy's distribution -- and autonomously modifies object poses so that the restructured scene is similar to training data. Theoretically, we show that this two step process (rearranging the environment before rolling out the given policy) reduces the generalization gap. Practically, our ReSET algorithm combines action-agnostic human videos with task-agnostic teleoperation data to i) decide when to modify the scene, ii) predict what simplifying actions a human would take, and iii) map those predictions into robot action primitives. Comparisons with diffusion policies, VLAs, and other baselines show that using ReSET to prepare the environment enables more robust task execution with equal amounts of total training data. See videos at our project website: https://reset2025paper.github.io/

## 📝 요약

이 논문은 로봇 학습에서 환경을 사전에 준비하는 능력을 부여하는 ReSET 알고리즘을 제안합니다. 기존 모방 학습은 관찰이 분포 밖에 있을 때 어려움을 겪지만, ReSET은 초기 상태를 조정하여 훈련 데이터와 유사하게 만듭니다. 이 과정은 일반화 격차를 줄이며, 인간의 비디오와 원격 조작 데이터를 활용해 장면 수정 시점과 간소화 행동을 예측합니다. 실험 결과, ReSET은 환경 준비를 통해 더 강력한 작업 수행을 가능하게 합니다.

## 🎯 주요 포인트

- 1. 모방 학습(IL)은 다양한 조작 작업에서 효과적이지만, 분포 밖의 관측에 직면했을 때 어려움을 겪습니다.
- 2. 인간은 비정상적인 초기 상태에서 환경을 재배치하여 작업을 더 쉽게 수행하는 경향이 있습니다.
- 3. ReSET 알고리즘은 로봇이 정책 실행 전에 환경을 준비할 수 있도록 하여 일반화 격차를 줄입니다.
- 4. ReSET은 인간의 비디오와 원격 조작 데이터를 결합하여 장면 수정 시점과 단순화 행동을 예측하고 이를 로봇 행동으로 변환합니다.
- 5. ReSET을 사용하면 동일한 양의 훈련 데이터로 더 견고한 작업 수행이 가능합니다.


---

*Generated on 2025-09-24 02:30:06*