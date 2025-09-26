---
keywords:
  - Transformer
  - Foveated Vision
  - Machine Learning
  - Human Gaze
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2507.15833
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:14:30.193612",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Foveated Vision",
    "Machine Learning",
    "Human Gaze"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Foveated Vision": 0.8,
    "Machine Learning": 0.7,
    "Human Gaze": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision Transformers",
        "canonical": "Transformer",
        "aliases": [
          "ViTs"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational model in machine learning and are directly applicable to the discussed foveated vision approach.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "foveated vision",
        "canonical": "Foveated Vision",
        "aliases": [
          "foveated processing"
        ],
        "category": "unique_technical",
        "rationale": "Foveated vision is a unique approach to visual processing that mirrors human vision and is central to the paper's methodology.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "robot learning",
        "canonical": "Machine Learning",
        "aliases": [
          "robotic learning"
        ],
        "category": "broad_technical",
        "rationale": "Machine learning is the broader category under which robot learning falls, linking to a wide range of related research.",
        "novelty_score": 0.2,
        "connectivity_score": 0.88,
        "specificity_score": 0.5,
        "link_intent_score": 0.7
      },
      {
        "surface": "human gaze",
        "canonical": "Human Gaze",
        "aliases": [
          "gaze tracking"
        ],
        "category": "unique_technical",
        "rationale": "Human gaze is a specific aspect of the study that informs the robot's visual processing, offering a novel approach to vision systems.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "robot vision system",
      "simulation benchmark"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision Transformers",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "foveated vision",
      "resolved_canonical": "Foveated Vision",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "robot learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.2,
        "connectivity": 0.88,
        "specificity": 0.5,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "human gaze",
      "resolved_canonical": "Human Gaze",
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

# Look, Focus, Act: Efficient and Robust Robot Learning via Human Gaze and Foveated Vision Transformers

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2507.15833.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2507.15833](https://arxiv.org/abs/2507.15833)

## 🔗 유사한 논문
- [[2025-09-19/Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring_20250919|Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring]] (84.7% similar)
- [[2025-09-19/GAF_ Gaussian Action Field as a Dynamic World Model for Robotic Manipulation_20250919|GAF: Gaussian Action Field as a Dynamic World Model for Robotic Manipulation]] (84.4% similar)
- [[2025-09-23/KungfuBot2_ Learning Versatile Motion Skills for Humanoid Whole-Body Control_20250923|KungfuBot2: Learning Versatile Motion Skills for Humanoid Whole-Body Control]] (84.3% similar)
- [[2025-09-22/A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning_20250922|A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning]] (83.9% similar)
- [[2025-09-22/Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception_20250922|Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception]] (83.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]], [[keywords/Machine Learning|Machine Learning]]
**⚡ Unique Technical**: [[keywords/Foveated Vision|Foveated Vision]], [[keywords/Human Gaze|Human Gaze]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.15833v2 Announce Type: replace-cross 
Abstract: Human vision is a highly active process driven by gaze, which directs attention to task-relevant regions through foveation, dramatically reducing visual processing. In contrast, robot learning systems typically rely on passive, uniform processing of raw camera images. In this work, we explore how incorporating human-like active gaze into robotic policies can enhance efficiency and robustness. We develop GIAVA (Gaze Integrated Active-Vision ALOHA), a robot vision system that emulates human head and neck movement, and gaze adjustment for foveated processing. Extending the AV-ALOHA robot platform, we introduce a framework for simultaneously collecting eye-tracking, perspective control, and robot manipulation demonstration data from a human operator. We also open-source a simulation benchmark and dataset for training robot policies that incorporate human gaze. Inspired by recent work in foveated image segmentation and given the widespread use of Vision Transformers (ViTs) in robot learning, we integrate gaze information into ViTs using a foveated patch tokenization scheme. Compared to uniform patch tokenization, this significantly reduces the number of tokens, and thus computation. Our results show that our method for foveated robot vision drastically reduces computational overhead, and enhances robustness to background distractors. Notably, on certain high-precision tasks, foveated vision also improves performance, as reflected in higher success rates. Together, these findings suggest that human-inspired foveated visual processing offers untapped potential and should be further considered as a useful inductive bias in robotic vision systems. https://ian-chuang.github.io/gaze-av-aloha/

## 📝 요약

이 논문은 인간의 시각적 주의 메커니즘을 로봇 비전 시스템에 적용하여 효율성과 견고성을 향상시키는 방법을 제안합니다. 연구팀은 인간의 시선 조절을 모방한 GIAVA 시스템을 개발하여, AV-ALOHA 플랫폼을 확장했습니다. 이 시스템은 인간의 시선 추적 데이터를 활용하여 로봇 정책을 훈련할 수 있는 시뮬레이션 벤치마크와 데이터셋을 공개했습니다. 또한, Vision Transformers(ViTs)에 시선 정보를 통합하여 계산량을 줄이고, 배경 방해 요소에 대한 견고성을 높였습니다. 실험 결과, 이 방법은 고정밀 작업에서 성공률을 높이며, 인간의 시각 처리 방식이 로봇 비전 시스템에 유용한 귀납적 편향으로 작용할 수 있음을 시사합니다.

## 🎯 주요 포인트

- 1. 인간의 시선 기반 능동적 시각 처리를 로봇 정책에 통합하여 효율성과 견고성을 향상시킬 수 있음을 탐구했습니다.
- 2. 인간의 머리와 목 움직임, 시선 조정을 모방하는 로봇 비전 시스템 GIAVA를 개발했습니다.
- 3. 인간 시선을 통합한 Vision Transformers(ViTs)를 사용하여 계산량을 크게 줄이고, 배경 방해 요소에 대한 견고성을 강화했습니다.
- 4. 특정 고정밀 작업에서 시선 기반 시각 처리가 성능을 향상시켜 성공률을 높였습니다.
- 5. 인간 영감을 받은 시선 기반 시각 처리가 로봇 비전 시스템에서 유용한 귀납적 편향으로 고려되어야 함을 시사합니다.


---

*Generated on 2025-09-24 01:14:30*