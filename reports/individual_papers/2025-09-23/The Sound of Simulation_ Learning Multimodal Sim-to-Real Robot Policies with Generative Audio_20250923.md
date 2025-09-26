---
keywords:
  - Multimodal Sim-to-Real Transfer
  - Generative Audio
  - Multimodal Learning
  - Zero-Shot Learning
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2507.02864
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:36:07.485368",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Sim-to-Real Transfer",
    "Generative Audio",
    "Multimodal Learning",
    "Zero-Shot Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Sim-to-Real Transfer": 0.88,
    "Generative Audio": 0.84,
    "Multimodal Learning": 0.91,
    "Zero-Shot Learning": 0.87
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal Sim-to-Real Transfer",
        "canonical": "Multimodal Sim-to-Real Transfer",
        "aliases": [
          "Multimodal Transfer",
          "Sim-to-Real Transfer"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's contribution and connects to ongoing research in transferring simulated learning to real-world applications.",
        "novelty_score": 0.85,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.88
      },
      {
        "surface": "Generative Audio",
        "canonical": "Generative Audio",
        "aliases": [
          "Audio Synthesis",
          "Sound Generation"
        ],
        "category": "unique_technical",
        "rationale": "This term highlights the novel use of audio generation in robotics, which is a less explored modality compared to vision.",
        "novelty_score": 0.78,
        "connectivity_score": 0.65,
        "specificity_score": 0.81,
        "link_intent_score": 0.84
      },
      {
        "surface": "Multimodal Learning",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multisensory Learning"
        ],
        "category": "specific_connectable",
        "rationale": "This connects to the broader field of integrating multiple sensory inputs, which is crucial for the paper's approach.",
        "novelty_score": 0.55,
        "connectivity_score": 0.89,
        "specificity_score": 0.77,
        "link_intent_score": 0.91
      },
      {
        "surface": "Zero-Shot Transfer",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot Transfer"
        ],
        "category": "specific_connectable",
        "rationale": "The paper demonstrates zero-shot transfer capabilities, which is a significant aspect of its contribution to sim-to-real learning.",
        "novelty_score": 0.6,
        "connectivity_score": 0.83,
        "specificity_score": 0.79,
        "link_intent_score": 0.87
      }
    ],
    "ban_list_suggestions": [
      "robot",
      "simulation",
      "framework"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal Sim-to-Real Transfer",
      "resolved_canonical": "Multimodal Sim-to-Real Transfer",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Generative Audio",
      "resolved_canonical": "Generative Audio",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.65,
        "specificity": 0.81,
        "link_intent": 0.84
      }
    },
    {
      "candidate_surface": "Multimodal Learning",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.89,
        "specificity": 0.77,
        "link_intent": 0.91
      }
    },
    {
      "candidate_surface": "Zero-Shot Transfer",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.83,
        "specificity": 0.79,
        "link_intent": 0.87
      }
    }
  ]
}
-->

# The Sound of Simulation: Learning Multimodal Sim-to-Real Robot Policies with Generative Audio

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2507.02864.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2507.02864](https://arxiv.org/abs/2507.02864)

## 🔗 유사한 논문
- [[2025-09-18/\textsc{Gen2Real}_ Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video_20250918|\textsc{Gen2Real}: Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video]] (85.8% similar)
- [[2025-09-22/Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning_20250922|Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning]] (83.7% similar)
- [[2025-09-23/Latent Policy Steering with Embodiment-Agnostic Pretrained World Models_20250923|Latent Policy Steering with Embodiment-Agnostic Pretrained World Models]] (82.8% similar)
- [[2025-09-23/KungfuBot2_ Learning Versatile Motion Skills for Humanoid Whole-Body Control_20250923|KungfuBot2: Learning Versatile Motion Skills for Humanoid Whole-Body Control]] (82.5% similar)
- [[2025-09-23/UniSkill_ Imitating Human Videos via Cross-Embodiment Skill Representations_20250923|UniSkill: Imitating Human Videos via Cross-Embodiment Skill Representations]] (82.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Multimodal Sim-to-Real Transfer|Multimodal Sim-to-Real Transfer]], [[keywords/Generative Audio|Generative Audio]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.02864v2 Announce Type: replace-cross 
Abstract: Robots must integrate multiple sensory modalities to act effectively in the real world. Yet, learning such multimodal policies at scale remains challenging. Simulation offers a viable solution, but while vision has benefited from high-fidelity simulators, other modalities (e.g. sound) can be notoriously difficult to simulate. As a result, sim-to-real transfer has succeeded primarily in vision-based tasks, with multimodal transfer still largely unrealized. In this work, we tackle these challenges by introducing MultiGen, a framework that integrates large-scale generative models into traditional physics simulators, enabling multisensory simulation. We showcase our framework on the dynamic task of robot pouring, which inherently relies on multimodal feedback. By synthesizing realistic audio conditioned on simulation video, our method enables training on rich audiovisual trajectories -- without any real robot data. We demonstrate effective zero-shot transfer to real-world pouring with novel containers and liquids, highlighting the potential of generative modeling to both simulate hard-to-model modalities and close the multimodal sim-to-real gap.

## 📝 요약

이 논문은 로봇이 현실 세계에서 효과적으로 작동하기 위해 여러 감각 모달리티를 통합해야 한다는 점을 다루고 있습니다. 특히, 시뮬레이션을 통해 이러한 멀티모달 정책을 학습하는 데 어려움이 있으며, 시각 기반 작업에서는 성공을 거두었으나 다른 모달리티에서는 여전히 도전 과제가 남아 있습니다. 이를 해결하기 위해, 본 연구는 MultiGen이라는 프레임워크를 도입하여 대규모 생성 모델을 전통적인 물리 시뮬레이터에 통합하여 멀티센서리 시뮬레이션을 가능하게 합니다. 로봇이 액체를 붓는 동적 작업을 통해, 시뮬레이션 비디오에 기반한 현실적인 오디오를 합성하여 풍부한 오디오비주얼 경로를 학습할 수 있게 하였습니다. 이 방법은 실제 로봇 데이터를 사용하지 않고도 새로운 용기와 액체를 사용하는 실제 환경으로의 효과적인 제로샷 전이를 입증하였습니다. 이는 생성 모델링이 어려운 모달리티를 시뮬레이션하고 멀티모달 시뮬레이션-현실 전이의 격차를 줄일 수 있는 잠재력을 보여줍니다.

## 🎯 주요 포인트

- 1. 로봇이 여러 감각 모달리티를 통합하여 효과적으로 작동하는 것이 중요하지만, 대규모로 이러한 멀티모달 정책을 학습하는 것은 여전히 도전적입니다.
- 2. MultiGen이라는 프레임워크를 도입하여 전통적인 물리 시뮬레이터에 대규모 생성 모델을 통합함으로써 멀티센서리 시뮬레이션을 가능하게 합니다.
- 3. 시뮬레이션 비디오에 조건화된 현실적인 오디오를 합성하여, 실제 로봇 데이터 없이도 풍부한 오디오비주얼 궤적에 대한 훈련을 가능하게 합니다.
- 4. 새로운 용기와 액체를 사용한 실제 로봇 붓기 작업에서 효과적인 제로샷 전이를 입증하여, 생성 모델링이 어려운 모달리티를 시뮬레이션하고 멀티모달 시뮬레이션-현실 간의 격차를 줄일 수 있는 잠재력을 강조합니다.


---

*Generated on 2025-09-24 05:36:07*