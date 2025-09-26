---
keywords:
  - Imitation Learning
  - Motion Retargeting
  - Humanoid Robot
  - Whole-body Controller
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15443
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T08:58:25.705078",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Imitation Learning",
    "Motion Retargeting",
    "Humanoid Robot",
    "Whole-body Controller"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Imitation Learning": 0.85,
    "Motion Retargeting": 0.82,
    "Humanoid Robot": 0.78,
    "Whole-body Controller": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Imitation Learning",
        "canonical": "Imitation Learning",
        "aliases": [
          "Behavioral Cloning"
        ],
        "category": "specific_connectable",
        "rationale": "Imitation Learning is a key concept in robotics and connects well with existing frameworks in machine learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.85
      },
      {
        "surface": "Motion Retargeting",
        "canonical": "Motion Retargeting",
        "aliases": [
          "Motion Transfer"
        ],
        "category": "unique_technical",
        "rationale": "This is a specialized technique in robotics crucial for translating human motion to robots.",
        "novelty_score": 0.78,
        "connectivity_score": 0.67,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Humanoid Robot",
        "canonical": "Humanoid Robot",
        "aliases": [
          "Bipedal Robot"
        ],
        "category": "specific_connectable",
        "rationale": "Humanoid robots are a specific type of robot that are central to the study of human-like motion.",
        "novelty_score": 0.5,
        "connectivity_score": 0.79,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Whole-body Controller",
        "canonical": "Whole-body Controller",
        "aliases": [
          "Full-body Controller"
        ],
        "category": "unique_technical",
        "rationale": "This is a specialized control system in robotics that manages complex movements.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
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
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Motion Retargeting",
      "resolved_canonical": "Motion Retargeting",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.67,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Humanoid Robot",
      "resolved_canonical": "Humanoid Robot",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.79,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Whole-body Controller",
      "resolved_canonical": "Whole-body Controller",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning

**Korean Title:** 인간에서 휴머노이드로의 모방 학습을 위한 암묵적 키노다이내믹 모션 리타게팅

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15443.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15443](https://arxiv.org/abs/2509.15443)

## 🔗 유사한 논문
- [[2025-09-18/Embracing Bulky Objects with Humanoid Robots_ Whole-Body Manipulation with Reinforcement Learning_20250918|Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning]] (86.3% similar)
- [[2025-09-18/TrajBooster_ Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning_20250918|TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning]] (84.7% similar)
- [[2025-09-18/Motion Adaptation Across Users and Tasks for Exoskeletons via Meta-Learning_20250918|Motion Adaptation Across Users and Tasks for Exoskeletons via Meta-Learning]] (84.5% similar)
- [[2025-09-18/\textsc{Gen2Real}_ Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video_20250918|\textsc{Gen2Real}: Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video]] (83.6% similar)
- [[2025-09-17/Prompt2Auto_ From Motion Prompt to Automated Control via Geometry-Invariant One-Shot Gaussian Process Learning_20250917|Prompt2Auto: From Motion Prompt to Automated Control via Geometry-Invariant One-Shot Gaussian Process Learning]] (83.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Imitation Learning|Imitation Learning]], [[keywords/Humanoid Robot|Humanoid Robot]]
**⚡ Unique Technical**: [[keywords/Motion Retargeting|Motion Retargeting]], [[keywords/Whole-body Controller|Whole-body Controller]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15443v1 Announce Type: cross 
Abstract: Human-to-humanoid imitation learning aims to learn a humanoid whole-body controller from human motion. Motion retargeting is a crucial step in enabling robots to acquire reference trajectories when exploring locomotion skills. However, current methods focus on motion retargeting frame by frame, which lacks scalability. Could we directly convert large-scale human motion into robot-executable motion through a more efficient approach? To address this issue, we propose Implicit Kinodynamic Motion Retargeting (IKMR), a novel efficient and scalable retargeting framework that considers both kinematics and dynamics. In kinematics, IKMR pretrains motion topology feature representation and a dual encoder-decoder architecture to learn a motion domain mapping. In dynamics, IKMR integrates imitation learning with the motion retargeting network to refine motion into physically feasible trajectories. After fine-tuning using the tracking results, IKMR can achieve large-scale physically feasible motion retargeting in real time, and a whole-body controller could be directly trained and deployed for tracking its retargeted trajectories. We conduct our experiments both in the simulator and the real robot on a full-size humanoid robot. Extensive experiments and evaluation results verify the effectiveness of our proposed framework.

## 🔍 Abstract (한글 번역)

arXiv:2509.15443v1 발표 유형: 교차  
초록: 인간에서 휴머노이드로의 모방 학습은 인간의 움직임으로부터 휴머노이드 전신 제어기를 학습하는 것을 목표로 합니다. 모션 리타게팅은 로봇이 이동 기술을 탐색할 때 참조 궤적을 획득할 수 있도록 하는 중요한 단계입니다. 그러나 현재의 방법들은 프레임별로 모션 리타게팅에 집중하고 있으며, 이는 확장성이 부족합니다. 대규모 인간의 움직임을 보다 효율적인 방법으로 로봇이 실행 가능한 움직임으로 직접 변환할 수 있을까요? 이 문제를 해결하기 위해, 우리는 암묵적 운동역학 모션 리타게팅(Implicit Kinodynamic Motion Retargeting, IKMR)을 제안합니다. 이는 운동학과 동역학을 모두 고려한 새로운 효율적이고 확장 가능한 리타게팅 프레임워크입니다. 운동학에서 IKMR은 모션 토폴로지 특징 표현과 이중 인코더-디코더 아키텍처를 사전 훈련하여 모션 도메인 매핑을 학습합니다. 동역학에서 IKMR은 모방 학습을 모션 리타게팅 네트워크와 통합하여 물리적으로 실행 가능한 궤적으로 모션을 정제합니다. 추적 결과를 사용하여 미세 조정한 후, IKMR은 실시간으로 대규모 물리적으로 실행 가능한 모션 리타게팅을 달성할 수 있으며, 전신 제어기는 리타게팅된 궤적을 추적하기 위해 직접 훈련되고 배포될 수 있습니다. 우리는 실물 크기의 휴머노이드 로봇에서 시뮬레이터와 실제 로봇 모두에서 실험을 수행했습니다. 광범위한 실험과 평가 결과는 우리가 제안한 프레임워크의 효과성을 검증합니다.

## 📝 요약

이 논문은 인간의 움직임을 휴머노이드 로봇이 모방할 수 있도록 하는 학습 방법을 제안합니다. 기존의 모션 리타게팅 방법은 프레임 단위로 처리하여 확장성이 부족한 문제를 가지고 있습니다. 이를 해결하기 위해, 저자들은 IKMR(Implicit Kinodynamic Motion Retargeting)이라는 새로운 프레임워크를 제안합니다. IKMR은 운동학적 및 동역학적 요소를 모두 고려하여, 대규모 인간의 움직임을 로봇이 실행 가능한 형태로 변환합니다. 운동학적으로는 모션 토폴로지 특징을 사전 학습하고, 이중 인코더-디코더 구조를 통해 모션 도메인 매핑을 학습합니다. 동역학적으로는 모방 학습을 통합하여 물리적으로 실행 가능한 궤적을 생성합니다. 실험 결과, IKMR은 대규모 모션 리타게팅을 실시간으로 수행할 수 있으며, 실제 로봇에서도 효과적임이 검증되었습니다.

## 🎯 주요 포인트

- 1. 인간의 움직임을 로봇이 실행 가능한 동작으로 변환하는 효율적인 방법을 제안합니다.
- 2. IKMR은 운동학과 동역학을 모두 고려하여 대규모 동작 리타겟팅을 가능하게 합니다.
- 3. IKMR은 모션 토폴로지 특징 표현과 이중 인코더-디코더 구조를 사전 학습하여 모션 도메인 매핑을 학습합니다.
- 4. 모방 학습과 모션 리타겟팅 네트워크를 통합하여 물리적으로 실현 가능한 궤적을 생성합니다.
- 5. 시뮬레이터와 실제 로봇 실험을 통해 IKMR의 효과성을 검증하였습니다.


---

*Generated on 2025-09-23 08:58:25*