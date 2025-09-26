---
keywords:
  - End-to-End Autonomous Driving
  - Imitation Learning
  - Safety Direct Preference Optimization
  - Trajectory-Level Preference Alignment
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17940
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:13:05.258500",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "End-to-End Autonomous Driving",
    "Imitation Learning",
    "Safety Direct Preference Optimization",
    "Trajectory-Level Preference Alignment"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "End-to-End Autonomous Driving": 0.78,
    "Imitation Learning": 0.8,
    "Safety Direct Preference Optimization": 0.82,
    "Trajectory-Level Preference Alignment": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "End-to-end autonomous driving",
        "canonical": "End-to-End Autonomous Driving",
        "aliases": [
          "E2E autonomous driving"
        ],
        "category": "unique_technical",
        "rationale": "This represents a specific approach in autonomous vehicle technology, offering unique insights into direct policy learning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Imitation learning",
        "canonical": "Imitation Learning",
        "aliases": [
          "behavior cloning"
        ],
        "category": "specific_connectable",
        "rationale": "This is a key method in machine learning for training autonomous systems, facilitating connections to broader learning paradigms.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Safety Direct Preference Optimization",
        "canonical": "Safety Direct Preference Optimization",
        "aliases": [
          "Safety DPO"
        ],
        "category": "unique_technical",
        "rationale": "This novel framework is central to the paper's contribution, offering a new approach to policy learning with safety considerations.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Trajectory-level preference alignment",
        "canonical": "Trajectory-Level Preference Alignment",
        "aliases": [
          "trajectory preference alignment"
        ],
        "category": "unique_technical",
        "rationale": "This concept is crucial for understanding the optimization process in the proposed framework, linking to trajectory-based learning methods.",
        "novelty_score": 0.7,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
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
      "candidate_surface": "End-to-end autonomous driving",
      "resolved_canonical": "End-to-End Autonomous Driving",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Imitation learning",
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
      "candidate_surface": "Safety Direct Preference Optimization",
      "resolved_canonical": "Safety Direct Preference Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Trajectory-level preference alignment",
      "resolved_canonical": "Trajectory-Level Preference Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# DriveDPO: Policy Learning via Safety DPO For End-to-End Autonomous Driving

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17940.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17940](https://arxiv.org/abs/2509.17940)

## 🔗 유사한 논문
- [[2025-09-23/Safe Guaranteed Dynamics Exploration with Probabilistic Models_20250923|Safe Guaranteed Dynamics Exploration with Probabilistic Models]] (86.1% similar)
- [[2025-09-19/FlowDrive_ Energy Flow Field for End-to-End Autonomous Driving_20250919|FlowDrive: Energy Flow Field for End-to-End Autonomous Driving]] (85.7% similar)
- [[2025-09-17/MAP_ End-to-End Autonomous Driving with Map-Assisted Planning_20250917|MAP: End-to-End Autonomous Driving with Map-Assisted Planning]] (84.5% similar)
- [[2025-09-23/ReasonPlan_ Unified Scene Prediction and Decision Reasoning for Closed-loop Autonomous Driving_20250923|ReasonPlan: Unified Scene Prediction and Decision Reasoning for Closed-loop Autonomous Driving]] (84.2% similar)
- [[2025-09-19/Digital Twin-based Cooperative Autonomous Driving in Smart Intersections_ A Multi-Agent Reinforcement Learning Approach_20250919|Digital Twin-based Cooperative Autonomous Driving in Smart Intersections: A Multi-Agent Reinforcement Learning Approach]] (83.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Imitation Learning|Imitation Learning]]
**⚡ Unique Technical**: [[keywords/End-to-End Autonomous Driving|End-to-End Autonomous Driving]], [[keywords/Safety Direct Preference Optimization|Safety Direct Preference Optimization]], [[keywords/Trajectory-Level Preference Alignment|Trajectory-Level Preference Alignment]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17940v1 Announce Type: cross 
Abstract: End-to-end autonomous driving has substantially progressed by directly predicting future trajectories from raw perception inputs, which bypasses traditional modular pipelines. However, mainstream methods trained via imitation learning suffer from critical safety limitations, as they fail to distinguish between trajectories that appear human-like but are potentially unsafe. Some recent approaches attempt to address this by regressing multiple rule-driven scores but decoupling supervision from policy optimization, resulting in suboptimal performance. To tackle these challenges, we propose DriveDPO, a Safety Direct Preference Optimization Policy Learning framework. First, we distill a unified policy distribution from human imitation similarity and rule-based safety scores for direct policy optimization. Further, we introduce an iterative Direct Preference Optimization stage formulated as trajectory-level preference alignment. Extensive experiments on the NAVSIM benchmark demonstrate that DriveDPO achieves a new state-of-the-art PDMS of 90.0. Furthermore, qualitative results across diverse challenging scenarios highlight DriveDPO's ability to produce safer and more reliable driving behaviors.

## 📝 요약

이 논문은 자율주행의 안전성을 개선하기 위해 DriveDPO라는 새로운 정책 학습 프레임워크를 제안합니다. 기존의 모방 학습 기반 방법론은 인간과 유사한 경로를 예측하지만 안전성 측면에서 한계가 있었습니다. DriveDPO는 인간 모방 유사성과 규칙 기반 안전 점수를 결합하여 정책 최적화를 직접 수행하며, 경로 수준의 선호도 정렬을 통해 정책을 개선합니다. NAVSIM 벤치마크 실험 결과, DriveDPO는 90.0의 새로운 최첨단 PDMS를 달성했으며, 다양한 도전적인 시나리오에서 더 안전하고 신뢰할 수 있는 주행 행동을 보여주었습니다.

## 🎯 주요 포인트

- 1. End-to-end 자율 주행은 전통적인 모듈식 파이프라인을 우회하여 원시 인식 입력에서 직접 미래 경로를 예측함으로써 상당한 발전을 이루었습니다.
- 2. 모방 학습으로 훈련된 주류 방법은 인간처럼 보이지만 잠재적으로 안전하지 않은 경로를 구별하지 못해 안전성에 한계가 있습니다.
- 3. DriveDPO는 인간 모방 유사성과 규칙 기반 안전 점수를 결합하여 직접 정책 최적화를 위한 통합 정책 분포를 증류합니다.
- 4. DriveDPO는 NAVSIM 벤치마크에서 새로운 최첨단 PDMS 90.0을 달성하였으며, 다양한 도전적인 시나리오에서 더 안전하고 신뢰할 수 있는 주행 행동을 보여줍니다.
- 5. DriveDPO는 경로 수준의 선호도 정렬로 구성된 반복적인 Direct Preference Optimization 단계를 도입합니다.


---

*Generated on 2025-09-24 05:13:05*