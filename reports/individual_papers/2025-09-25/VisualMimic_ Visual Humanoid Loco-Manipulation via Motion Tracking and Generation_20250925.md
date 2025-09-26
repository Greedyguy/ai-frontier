---
keywords:
  - VisualMimic
  - Zero-Shot Learning
  - Egocentric Vision
  - Hierarchical Control
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.20322
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T17:03:42.404066",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "VisualMimic",
    "Zero-Shot Learning",
    "Egocentric Vision",
    "Hierarchical Control"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "VisualMimic": 0.85,
    "Zero-Shot Learning": 0.8,
    "Egocentric Vision": 0.78,
    "Hierarchical Control": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "VisualMimic",
        "canonical": "VisualMimic",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "VisualMimic is a novel framework specific to this paper, crucial for linking to its unique contributions in humanoid loco-manipulation.",
        "novelty_score": 0.95,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Zero-Shot Transfer",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot Transfer"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-shot transfer is a key concept in the paper, enabling the application of learned policies to real-world robots without retraining.",
        "novelty_score": 0.7,
        "connectivity_score": 0.88,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "Egocentric Vision",
        "canonical": "Egocentric Vision",
        "aliases": [
          "First-Person Vision"
        ],
        "category": "unique_technical",
        "rationale": "Egocentric vision is central to the framework's integration of perception and control, providing a unique perspective in robot vision.",
        "novelty_score": 0.78,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Hierarchical Whole-Body Control",
        "canonical": "Hierarchical Control",
        "aliases": [
          "Whole-Body Control"
        ],
        "category": "specific_connectable",
        "rationale": "Hierarchical control is essential for managing complex robot movements, linking to broader control strategies in robotics.",
        "novelty_score": 0.65,
        "connectivity_score": 0.83,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "motion capture systems",
      "task-agnostic",
      "task-specific"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "VisualMimic",
      "resolved_canonical": "VisualMimic",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Zero-Shot Transfer",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.88,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Egocentric Vision",
      "resolved_canonical": "Egocentric Vision",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Hierarchical Whole-Body Control",
      "resolved_canonical": "Hierarchical Control",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.83,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20322.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.20322](https://arxiv.org/abs/2509.20322)

## 🔗 유사한 논문
- [[2025-09-23/MaskedManipulator_ Versatile Whole-Body Manipulation_20250923|MaskedManipulator: Versatile Whole-Body Manipulation]] (87.7% similar)
- [[2025-09-22/Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning_20250922|Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning]] (87.1% similar)
- [[2025-09-23/KungfuBot2_ Learning Versatile Motion Skills for Humanoid Whole-Body Control_20250923|KungfuBot2: Learning Versatile Motion Skills for Humanoid Whole-Body Control]] (86.8% similar)
- [[2025-09-23/UniSkill_ Imitating Human Videos via Cross-Embodiment Skill Representations_20250923|UniSkill: Imitating Human Videos via Cross-Embodiment Skill Representations]] (84.9% similar)
- [[2025-09-24/MV-UMI_ A Scalable Multi-View Interface for Cross-Embodiment Learning_20250924|MV-UMI: A Scalable Multi-View Interface for Cross-Embodiment Learning]] (84.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]], [[keywords/Hierarchical Control|Hierarchical Control]]
**⚡ Unique Technical**: [[keywords/VisualMimic|VisualMimic]], [[keywords/Egocentric Vision|Egocentric Vision]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20322v1 Announce Type: cross 
Abstract: Humanoid loco-manipulation in unstructured environments demands tight integration of egocentric perception and whole-body control. However, existing approaches either depend on external motion capture systems or fail to generalize across diverse tasks. We introduce VisualMimic, a visual sim-to-real framework that unifies egocentric vision with hierarchical whole-body control for humanoid robots. VisualMimic combines a task-agnostic low-level keypoint tracker -- trained from human motion data via a teacher-student scheme -- with a task-specific high-level policy that generates keypoint commands from visual and proprioceptive input. To ensure stable training, we inject noise into the low-level policy and clip high-level actions using human motion statistics. VisualMimic enables zero-shot transfer of visuomotor policies trained in simulation to real humanoid robots, accomplishing a wide range of loco-manipulation tasks such as box lifting, pushing, football dribbling, and kicking. Beyond controlled laboratory settings, our policies also generalize robustly to outdoor environments. Videos are available at: https://visualmimic.github.io .

## 📝 요약

VisualMimic은 비정형 환경에서 인간형 로봇의 이동 및 조작을 위한 시각 기반 시뮬레이션-현실 전이 프레임워크입니다. 이 연구는 인간의 움직임 데이터를 활용한 교사-학생 방식의 키포인트 추적기와 시각 및 고유 수용 입력을 통해 키포인트 명령을 생성하는 정책을 결합하여, 외부 모션 캡처 시스템 없이 다양한 작업에 일반화할 수 있는 방법을 제안합니다. 안정적인 훈련을 위해 저수준 정책에 노이즈를 추가하고 고수준 행동을 인간 움직임 통계로 제한합니다. VisualMimic은 시뮬레이션에서 훈련된 시각-운동 정책을 실제 로봇에 제로샷 전이하여 박스 들어올리기, 밀기, 축구 드리블 및 차기와 같은 다양한 작업을 수행할 수 있으며, 실험실 외부 환경에서도 강력하게 일반화됩니다.

## 🎯 주요 포인트

- 1. VisualMimic은 인간형 로봇의 자아 중심 시각과 계층적 전신 제어를 통합하는 시뮬레이션-현실 전이 프레임워크입니다.
- 2. 이 시스템은 인간의 운동 데이터를 기반으로 훈련된 작업 비특이적 저수준 키포인트 추적기와 시각 및 고유 수용 입력으로부터 키포인트 명령을 생성하는 작업 특이적 고수준 정책을 결합합니다.
- 3. 안정적인 훈련을 위해 저수준 정책에 노이즈를 주입하고, 고수준 행동을 인간 운동 통계로 클립합니다.
- 4. VisualMimic은 시뮬레이션에서 훈련된 시각-운동 정책을 실제 인간형 로봇에 제로샷 전이하여 다양한 로코-조작 작업을 수행할 수 있게 합니다.
- 5. 이 정책은 통제된 실험실 환경을 넘어 실외 환경에서도 강력하게 일반화됩니다.


---

*Generated on 2025-09-25 17:03:42*