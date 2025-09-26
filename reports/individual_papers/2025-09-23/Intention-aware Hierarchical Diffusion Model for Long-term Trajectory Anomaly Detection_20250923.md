---
keywords:
  - Intention-aware Hierarchical Diffusion Model
  - Inverse Q Learning
  - Trajectory Anomaly Detection
  - Diffusion Model
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17068
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T22:55:41.989456",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Intention-aware Hierarchical Diffusion Model",
    "Inverse Q Learning",
    "Trajectory Anomaly Detection",
    "Diffusion Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Intention-aware Hierarchical Diffusion Model": 0.88,
    "Inverse Q Learning": 0.8,
    "Trajectory Anomaly Detection": 0.75,
    "Diffusion Model": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Intention-aware Hierarchical Diffusion model",
        "canonical": "Intention-aware Hierarchical Diffusion Model",
        "aliases": [
          "IHiD"
        ],
        "category": "unique_technical",
        "rationale": "This is the primary novel method introduced in the paper, essential for linking the specific approach to trajectory anomaly detection.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "Inverse Q Learning",
        "canonical": "Inverse Q Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A specific learning approach used in the paper, important for understanding the high-level model's functionality.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "trajectory anomaly detection",
        "canonical": "Trajectory Anomaly Detection",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Central theme of the paper, connecting to broader discussions on anomaly detection in spatiotemporal data.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "diffusion model",
        "canonical": "Diffusion Model",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Key component of the low-level model in the proposed method, relevant for generating sub-trajectories.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.78,
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
      "candidate_surface": "Intention-aware Hierarchical Diffusion model",
      "resolved_canonical": "Intention-aware Hierarchical Diffusion Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Inverse Q Learning",
      "resolved_canonical": "Inverse Q Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "trajectory anomaly detection",
      "resolved_canonical": "Trajectory Anomaly Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "diffusion model",
      "resolved_canonical": "Diffusion Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Intention-aware Hierarchical Diffusion Model for Long-term Trajectory Anomaly Detection

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17068.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17068](https://arxiv.org/abs/2509.17068)

## 🔗 유사한 논문
- [[2025-09-18/AnoF-Diff_ One-Step Diffusion-Based Anomaly Detection for Forceful Tool Use_20250918|AnoF-Diff: One-Step Diffusion-Based Anomaly Detection for Forceful Tool Use]] (81.8% similar)
- [[2025-09-18/FlightDiffusion_ Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video_20250918|FlightDiffusion: Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video]] (80.6% similar)
- [[2025-09-18/Beyond Marginals_ Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection_20250918|Beyond Marginals: Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection]] (80.5% similar)
- [[2025-09-22/AdaSports-Traj_ Role- and Domain-Aware Adaptation for Multi-Agent Trajectory Modeling in Sports_20250922|AdaSports-Traj: Role- and Domain-Aware Adaptation for Multi-Agent Trajectory Modeling in Sports]] (79.8% similar)
- [[2025-09-22/G2D2_ Gradient-Guided Discrete Diffusion for Inverse Problem Solving_20250922|G2D2: Gradient-Guided Discrete Diffusion for Inverse Problem Solving]] (79.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Trajectory Anomaly Detection|Trajectory Anomaly Detection]]
**🔗 Specific Connectable**: [[keywords/Inverse Q Learning|Inverse Q Learning]], [[keywords/Diffusion Model|Diffusion Model]]
**⚡ Unique Technical**: [[keywords/Intention-aware Hierarchical Diffusion Model|Intention-aware Hierarchical Diffusion Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17068v1 Announce Type: new 
Abstract: Long-term trajectory anomaly detection is a challenging problem due to the diversity and complex spatiotemporal dependencies in trajectory data. Existing trajectory anomaly detection methods fail to simultaneously consider both the high-level intentions of agents as well as the low-level details of the agent's navigation when analysing an agent's trajectories. This limits their ability to capture the full diversity of normal trajectories. In this paper, we propose an unsupervised trajectory anomaly detection method named Intention-aware Hierarchical Diffusion model (IHiD), which detects anomalies through both high-level intent evaluation and low-level sub-trajectory analysis. Our approach leverages Inverse Q Learning as the high-level model to assess whether a selected subgoal aligns with an agent's intention based on predicted Q-values. Meanwhile, a diffusion model serves as the low-level model to generate sub-trajectories conditioned on subgoal information, with anomaly detection based on reconstruction error. By integrating both models, IHiD effectively utilises subgoal transition knowledge and is designed to capture the diverse distribution of normal trajectories. Our experiments show that the proposed method IHiD achieves up to 30.2% improvement in anomaly detection performance in terms of F1 score over state-of-the-art baselines.

## 📝 요약

이 논문은 장기 궤적 이상 탐지 문제를 다루며, 기존 방법들이 고수준의 의도와 저수준의 세부 내비게이션을 동시에 고려하지 못하는 한계를 극복하고자 합니다. 이를 위해, 저자들은 의도 인식 계층 확산 모델(IHiD)을 제안합니다. IHiD는 고수준 모델로 역 Q 학습을 활용하여 에이전트의 의도와 부합하는지 평가하고, 저수준 모델로 확산 모델을 사용하여 부궤적을 생성하며 재구성 오류를 기반으로 이상을 탐지합니다. 실험 결과, IHiD는 기존 최첨단 방법들에 비해 F1 점수 기준으로 최대 30.2%의 성능 향상을 보였습니다.

## 🎯 주요 포인트

- 1. 장기 궤적 이상 탐지는 궤적 데이터의 다양성과 복잡한 시공간 의존성 때문에 도전적인 문제입니다.
- 2. 기존 방법들은 에이전트의 고수준 의도와 저수준 내비게이션 세부사항을 동시에 고려하지 못해 정상 궤적의 다양성을 충분히 포착하지 못합니다.
- 3. 제안된 IHiD 모델은 고수준 의도 평가와 저수준 하위 궤적 분석을 통해 이상을 감지하는 비지도 학습 방법입니다.
- 4. IHiD는 역 Q 학습을 활용하여 에이전트의 의도에 부합하는 하위 목표를 평가하고, 확산 모델을 통해 하위 궤적을 생성하여 이상을 감지합니다.
- 5. 실험 결과, IHiD는 최첨단 기준 대비 F1 점수에서 최대 30.2%의 성능 향상을 달성했습니다.


---

*Generated on 2025-09-23 22:55:41*