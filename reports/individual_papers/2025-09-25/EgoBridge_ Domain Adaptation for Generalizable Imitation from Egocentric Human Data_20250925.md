---
keywords:
  - EgoBridge
  - Domain Adaptation
  - Optimal Transport
  - Egocentric Human Data
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19626
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:57:08.267368",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "EgoBridge",
    "Domain Adaptation",
    "Optimal Transport",
    "Egocentric Human Data"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "EgoBridge": 0.85,
    "Domain Adaptation": 0.8,
    "Optimal Transport": 0.78,
    "Egocentric Human Data": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "EgoBridge",
        "canonical": "EgoBridge",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "EgoBridge is a novel framework introduced in the paper, crucial for domain adaptation in imitation learning.",
        "novelty_score": 0.95,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Domain Adaptation",
        "canonical": "Domain Adaptation",
        "aliases": [
          "Domain Transfer"
        ],
        "category": "specific_connectable",
        "rationale": "Domain adaptation is a key concept in aligning human and robot data, enhancing connectivity with related works.",
        "novelty_score": 0.5,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Optimal Transport",
        "canonical": "Optimal Transport",
        "aliases": [
          "OT"
        ],
        "category": "specific_connectable",
        "rationale": "Optimal Transport is used to measure discrepancy in policy latent features, linking to mathematical methods in learning.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Egocentric Human Data",
        "canonical": "Egocentric Human Data",
        "aliases": [
          "First-Person Human Data"
        ],
        "category": "unique_technical",
        "rationale": "Egocentric data is central to the paper's approach, offering a unique perspective in imitation learning.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "robot",
      "human",
      "task"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "EgoBridge",
      "resolved_canonical": "EgoBridge",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Domain Adaptation",
      "resolved_canonical": "Domain Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Optimal Transport",
      "resolved_canonical": "Optimal Transport",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Egocentric Human Data",
      "resolved_canonical": "Egocentric Human Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# EgoBridge: Domain Adaptation for Generalizable Imitation from Egocentric Human Data

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19626.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19626](https://arxiv.org/abs/2509.19626)

## 🔗 유사한 논문
- [[2025-09-24/Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training_20250924|Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training]] (85.8% similar)
- [[2025-09-18/TrajBooster_ Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning_20250918|TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning]] (83.8% similar)
- [[2025-09-25/ROPA_ Synthetic Robot Pose Generation for RGB-D Bimanual Data Augmentation_20250925|ROPA: Synthetic Robot Pose Generation for RGB-D Bimanual Data Augmentation]] (83.5% similar)
- [[2025-09-24/MV-UMI_ A Scalable Multi-View Interface for Cross-Embodiment Learning_20250924|MV-UMI: A Scalable Multi-View Interface for Cross-Embodiment Learning]] (83.5% similar)
- [[2025-09-23/UniSkill_ Imitating Human Videos via Cross-Embodiment Skill Representations_20250923|UniSkill: Imitating Human Videos via Cross-Embodiment Skill Representations]] (83.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Domain Adaptation|Domain Adaptation]], [[keywords/Optimal Transport|Optimal Transport]]
**⚡ Unique Technical**: [[keywords/EgoBridge|EgoBridge]], [[keywords/Egocentric Human Data|Egocentric Human Data]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19626v1 Announce Type: cross 
Abstract: Egocentric human experience data presents a vast resource for scaling up end-to-end imitation learning for robotic manipulation. However, significant domain gaps in visual appearance, sensor modalities, and kinematics between human and robot impede knowledge transfer. This paper presents EgoBridge, a unified co-training framework that explicitly aligns the policy latent spaces between human and robot data using domain adaptation. Through a measure of discrepancy on the joint policy latent features and actions based on Optimal Transport (OT), we learn observation representations that not only align between the human and robot domain but also preserve the action-relevant information critical for policy learning. EgoBridge achieves a significant absolute policy success rate improvement by 44% over human-augmented cross-embodiment baselines in three real-world single-arm and bimanual manipulation tasks. EgoBridge also generalizes to new objects, scenes, and tasks seen only in human data, where baselines fail entirely. Videos and additional information can be found at https://ego-bridge.github.io

## 📝 요약

EgoBridge는 인간과 로봇 간의 도메인 차이를 극복하여 로봇 조작을 위한 모방 학습을 향상시키는 통합 공동 학습 프레임워크입니다. 이 연구는 Optimal Transport(OT)를 기반으로 한 정책 잠재 공간의 불일치를 측정하여 인간과 로봇 데이터 간의 정책 잠재 공간을 명시적으로 정렬합니다. 이를 통해 관찰 표현을 학습하여 인간과 로봇 도메인 간 정렬을 이루고, 정책 학습에 중요한 행동 관련 정보를 보존합니다. EgoBridge는 세 가지 실제 조작 작업에서 인간 보강 크로스-구현 기준선 대비 44%의 절대적인 정책 성공률 향상을 달성했으며, 인간 데이터에서만 본 새로운 객체, 장면, 작업에도 일반화합니다.

## 🎯 주요 포인트

- 1. EgoBridge는 인간과 로봇 데이터 간의 정책 잠재 공간을 명시적으로 정렬하여 도메인 적응을 통한 통합 공동 학습 프레임워크를 제시합니다.
- 2. 최적 수송(Optimal Transport, OT)을 기반으로 한 공동 정책 잠재 특징 및 행동의 불일치 측정을 통해 관찰 표현을 학습하여 인간과 로봇 도메인을 정렬하고 정책 학습에 중요한 행동 관련 정보를 보존합니다.
- 3. EgoBridge는 세 가지 실제 단일 팔 및 양손 조작 작업에서 인간 보강 교차 구현 기준선보다 절대 정책 성공률을 44% 향상시킵니다.
- 4. EgoBridge는 기준선이 완전히 실패하는 새로운 물체, 장면 및 인간 데이터에서만 본 작업에 일반화됩니다.
- 5. 추가 정보와 비디오는 https://ego-bridge.github.io에서 확인할 수 있습니다.


---

*Generated on 2025-09-25 16:57:08*