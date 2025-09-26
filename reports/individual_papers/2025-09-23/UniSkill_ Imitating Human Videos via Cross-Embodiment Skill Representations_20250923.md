---
keywords:
  - Cross-Embodiment Skill Representations
  - Self-supervised Learning
  - Robot Policies
  - Imitation Learning
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2505.08787
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:35:00.033079",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Cross-Embodiment Skill Representations",
    "Self-supervised Learning",
    "Robot Policies",
    "Imitation Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Cross-Embodiment Skill Representations": 0.78,
    "Self-supervised Learning": 0.82,
    "Robot Policies": 0.75,
    "Imitation Learning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "cross-embodiment skill representations",
        "canonical": "Cross-Embodiment Skill Representations",
        "aliases": [
          "cross-embodiment skills",
          "skill transfer"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's contribution, focusing on transferring skills across different embodiments.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "self-supervised learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "SSL"
        ],
        "category": "specific_connectable",
        "rationale": "The paper leverages self-supervised learning to extract skills without labels, aligning with known concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "robot policies",
        "canonical": "Robot Policies",
        "aliases": [
          "robot control policies"
        ],
        "category": "unique_technical",
        "rationale": "This term is crucial for understanding how skills are applied in robotic systems.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "imitation learning",
        "canonical": "Imitation Learning",
        "aliases": [
          "mimicry learning"
        ],
        "category": "broad_technical",
        "rationale": "Imitation learning is a foundational concept in the paper, relevant for linking with broader AI learning strategies.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "human videos",
      "robot data",
      "video prompts"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "cross-embodiment skill representations",
      "resolved_canonical": "Cross-Embodiment Skill Representations",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "self-supervised learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "robot policies",
      "resolved_canonical": "Robot Policies",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "imitation learning",
      "resolved_canonical": "Imitation Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# UniSkill: Imitating Human Videos via Cross-Embodiment Skill Representations

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2505.08787.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2505.08787](https://arxiv.org/abs/2505.08787)

## 🔗 유사한 논문
- [[2025-09-18/\textsc{Gen2Real}_ Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video_20250918|\textsc{Gen2Real}: Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video]] (84.2% similar)
- [[2025-09-22/Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning_20250922|Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning]] (83.9% similar)
- [[2025-09-23/KungfuBot2_ Learning Versatile Motion Skills for Humanoid Whole-Body Control_20250923|KungfuBot2: Learning Versatile Motion Skills for Humanoid Whole-Body Control]] (83.7% similar)
- [[2025-09-18/TrajBooster_ Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning_20250918|TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning]] (82.2% similar)
- [[2025-09-22/Compose by Focus_ Scene Graph-based Atomic Skills_20250922|Compose by Focus: Scene Graph-based Atomic Skills]] (82.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Imitation Learning|Imitation Learning]]
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Cross-Embodiment Skill Representations|Cross-Embodiment Skill Representations]], [[keywords/Robot Policies|Robot Policies]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.08787v4 Announce Type: replace-cross 
Abstract: Mimicry is a fundamental learning mechanism in humans, enabling individuals to learn new tasks by observing and imitating experts. However, applying this ability to robots presents significant challenges due to the inherent differences between human and robot embodiments in both their visual appearance and physical capabilities. While previous methods bridge this gap using cross-embodiment datasets with shared scenes and tasks, collecting such aligned data between humans and robots at scale is not trivial. In this paper, we propose UniSkill, a novel framework that learns embodiment-agnostic skill representations from large-scale cross-embodiment video data without any labels, enabling skills extracted from human video prompts to effectively transfer to robot policies trained only on robot data. Our experiments in both simulation and real-world environments show that our cross-embodiment skills successfully guide robots in selecting appropriate actions, even with unseen video prompts. The project website can be found at: https://kimhanjung.github.io/UniSkill.

## 📝 요약

이 논문은 인간의 모방 학습 능력을 로봇에 적용하는 데 있어 발생하는 문제를 해결하기 위해 UniSkill이라는 새로운 프레임워크를 제안합니다. UniSkill은 대규모의 비디오 데이터를 활용하여 인간과 로봇 간의 구현 차이를 극복하고, 라벨 없이도 인간의 비디오에서 추출한 기술을 로봇 정책에 효과적으로 전이시킵니다. 실험 결과, 이 프레임워크는 시뮬레이션 및 실제 환경에서 로봇이 적절한 행동을 선택하도록 성공적으로 안내하며, 새로운 비디오 프롬프트에서도 유효함을 보여주었습니다.

## 🎯 주요 포인트

- 1. 모방은 인간의 기본적인 학습 메커니즘으로, 전문가를 관찰하고 모방하여 새로운 과제를 배우는 것을 가능하게 합니다.
- 2. 인간과 로봇의 외형 및 물리적 능력의 차이로 인해 로봇에 모방 학습을 적용하는 데에는 상당한 도전 과제가 존재합니다.
- 3. UniSkill이라는 새로운 프레임워크는 대규모의 크로스-임바디먼트 비디오 데이터로부터 레이블 없이 임바디먼트에 구애받지 않는 기술 표현을 학습합니다.
- 4. UniSkill은 인간 비디오 프롬프트에서 추출된 기술을 로봇 데이터로만 훈련된 로봇 정책에 효과적으로 전이시킵니다.
- 5. 실험 결과, 크로스-임바디먼트 기술은 보지 못한 비디오 프롬프트에서도 로봇이 적절한 행동을 선택하도록 성공적으로 안내합니다.


---

*Generated on 2025-09-24 05:35:00*