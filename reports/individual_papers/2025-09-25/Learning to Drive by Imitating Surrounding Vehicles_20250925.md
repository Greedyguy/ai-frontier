---
keywords:
  - Imitation Learning
  - Autonomous Vehicles
  - Data Augmentation
  - Trajectory Data
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2503.05997
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:21:04.311360",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Imitation Learning",
    "Autonomous Vehicles",
    "Data Augmentation",
    "Trajectory Data"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Imitation Learning": 0.85,
    "Autonomous Vehicles": 0.8,
    "Data Augmentation": 0.78,
    "Trajectory Data": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Imitation Learning",
        "canonical": "Imitation Learning",
        "aliases": [
          "Behavior Cloning"
        ],
        "category": "specific_connectable",
        "rationale": "Imitation Learning is central to the paper's approach and connects to broader discussions in autonomous systems.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "Autonomous Vehicles",
        "canonical": "Autonomous Vehicles",
        "aliases": [
          "Self-Driving Cars",
          "AV"
        ],
        "category": "broad_technical",
        "rationale": "Autonomous Vehicles are the primary application domain of the study, linking to a wide range of related research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.92,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Data Augmentation",
        "canonical": "Data Augmentation",
        "aliases": [
          "Dataset Expansion"
        ],
        "category": "specific_connectable",
        "rationale": "Data Augmentation is a key technique used in the paper to improve learning outcomes, relevant to many ML applications.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.72,
        "link_intent_score": 0.78
      },
      {
        "surface": "Trajectory Data",
        "canonical": "Trajectory Data",
        "aliases": [
          "Motion Data",
          "Path Data"
        ],
        "category": "unique_technical",
        "rationale": "Trajectory Data is uniquely emphasized in the paper as a source of additional learning signals.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
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
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Autonomous Vehicles",
      "resolved_canonical": "Autonomous Vehicles",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.92,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Data Augmentation",
      "resolved_canonical": "Data Augmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.72,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Trajectory Data",
      "resolved_canonical": "Trajectory Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Learning to Drive by Imitating Surrounding Vehicles

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2503.05997.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2503.05997](https://arxiv.org/abs/2503.05997)

## 🔗 유사한 논문
- [[2025-09-23/Trajectory Prediction for Autonomous Driving_ Progress, Limitations, and Future Directions_20250923|Trajectory Prediction for Autonomous Driving: Progress, Limitations, and Future Directions]] (85.6% similar)
- [[2025-09-18/Occupancy-aware Trajectory Planning for Autonomous Valet Parking in Uncertain Dynamic Environments_20250918|Occupancy-aware Trajectory Planning for Autonomous Valet Parking in Uncertain Dynamic Environments]] (84.9% similar)
- [[2025-09-19/Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention_20250919|Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention]] (84.7% similar)
- [[2025-09-23/RIFT_ Group-Relative RL Fine-Tuning for Realistic and Controllable Traffic Simulation_20250923|RIFT: Group-Relative RL Fine-Tuning for Realistic and Controllable Traffic Simulation]] (83.8% similar)
- [[2025-09-25/RDAR_ Reward-Driven Agent Relevance Estimation for Autonomous Driving_20250925|RDAR: Reward-Driven Agent Relevance Estimation for Autonomous Driving]] (83.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Autonomous Vehicles|Autonomous Vehicles]]
**🔗 Specific Connectable**: [[keywords/Imitation Learning|Imitation Learning]], [[keywords/Data Augmentation|Data Augmentation]]
**⚡ Unique Technical**: [[keywords/Trajectory Data|Trajectory Data]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.05997v2 Announce Type: replace-cross 
Abstract: Imitation learning is a promising approach for training autonomous vehicles (AV) to navigate complex traffic environments by mimicking expert driver behaviors. While existing imitation learning frameworks focus on leveraging expert demonstrations, they often overlook the potential of additional complex driving data from surrounding traffic participants. In this paper, we study a data augmentation strategy that leverages the observed trajectories of nearby vehicles, captured by the AV's sensors, as additional demonstrations. We introduce a simple vehicle-selection sampling and filtering strategy that prioritizes informative and diverse driving behaviors, contributing to a richer dataset for training. We evaluate this idea with a representative learning-based planner on a large real-world dataset and demonstrate improved performance in complex driving scenarios. Specifically, the approach reduces collision rates and improves safety metrics compared to the baseline. Notably, even when using only 10 percent of the original dataset, the method matches or exceeds the performance of the full dataset. Through ablations, we analyze selection criteria and show that naive random selection can degrade performance. Our findings highlight the value of leveraging diverse real-world trajectory data in imitation learning and provide insights into data augmentation strategies for autonomous driving.

## 📝 요약

이 논문은 자율주행 차량의 모방 학습에서 주변 차량의 복잡한 주행 데이터를 활용한 데이터 증강 전략을 제안합니다. 기존 모방 학습은 전문가 시범에 집중하지만, 이 연구는 자율주행 차량 센서로 포착한 주변 차량의 주행 궤적을 추가 시범으로 활용합니다. 이를 위해 정보가 풍부하고 다양한 주행 행동을 우선시하는 차량 선택 및 필터링 전략을 도입하여 더 풍부한 학습 데이터를 제공합니다. 대규모 실제 데이터셋에서 이 방법을 평가한 결과, 충돌률 감소와 안전성 향상 등 복잡한 주행 시나리오에서 성능이 개선되었습니다. 특히, 원본 데이터셋의 10%만 사용해도 전체 데이터셋과 동등하거나 더 나은 성능을 보였습니다. 연구는 다양한 실제 궤적 데이터 활용의 가치를 강조하며, 자율주행을 위한 데이터 증강 전략에 대한 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. 모방 학습은 전문가 운전 행동을 모방하여 자율주행차를 훈련하는 유망한 접근 방식이다.
- 2. 기존 모방 학습은 전문가 시연에 집중하지만, 주변 교통 참여자의 복잡한 주행 데이터를 간과한다.
- 3. 본 연구는 자율주행차의 센서로 포착한 주변 차량의 궤적을 추가 시연으로 활용하는 데이터 증강 전략을 제안한다.
- 4. 제안된 방법은 충돌률 감소 및 안전성 지표 개선을 통해 복잡한 주행 시나리오에서 성능 향상을 보여준다.
- 5. 전체 데이터셋의 10%만 사용해도 기존 데이터셋의 성능을 맞추거나 초과할 수 있음을 입증한다.


---

*Generated on 2025-09-25 16:21:04*