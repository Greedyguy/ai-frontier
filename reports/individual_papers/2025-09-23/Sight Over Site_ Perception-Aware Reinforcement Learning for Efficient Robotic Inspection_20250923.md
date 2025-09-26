---
keywords:
  - Perception-Aware Reinforcement Learning
  - Autonomous Inspection
  - Machine Learning
  - Target Visibility
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17877
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:12:51.091759",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Perception-Aware Reinforcement Learning",
    "Autonomous Inspection",
    "Machine Learning",
    "Target Visibility"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Perception-Aware Reinforcement Learning": 0.78,
    "Autonomous Inspection": 0.77,
    "Machine Learning": 0.7,
    "Target Visibility": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Perception-Aware Reinforcement Learning",
        "canonical": "Perception-Aware Reinforcement Learning",
        "aliases": [
          "Perception-Driven Reinforcement Learning"
        ],
        "category": "unique_technical",
        "rationale": "This concept integrates perception into reinforcement learning, which is central to the paper's approach and novel in its application to robotic inspection.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Autonomous Inspection",
        "canonical": "Autonomous Inspection",
        "aliases": [
          "Automated Inspection"
        ],
        "category": "unique_technical",
        "rationale": "This term encapsulates the primary application domain of the research, linking it to broader robotics and automation contexts.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Reinforcement Learning",
        "canonical": "Machine Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement learning is a fundamental machine learning approach used in the paper, connecting it to a broad range of AI research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Target Visibility",
        "canonical": "Target Visibility",
        "aliases": [
          "Visibility of Target"
        ],
        "category": "unique_technical",
        "rationale": "This is a key concept in the paper's methodology, focusing on the visibility aspect of inspection tasks.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "navigation tasks",
      "real-world environments",
      "simulation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Perception-Aware Reinforcement Learning",
      "resolved_canonical": "Perception-Aware Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Autonomous Inspection",
      "resolved_canonical": "Autonomous Inspection",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Target Visibility",
      "resolved_canonical": "Target Visibility",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Sight Over Site: Perception-Aware Reinforcement Learning for Efficient Robotic Inspection

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17877.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17877](https://arxiv.org/abs/2509.17877)

## 🔗 유사한 논문
- [[2025-09-19/Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion_20250919|Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion]] (85.4% similar)
- [[2025-09-22/Dynamic Neural Curiosity Enhances Learning Flexibility for Autonomous Goal Discovery_20250922|Dynamic Neural Curiosity Enhances Learning Flexibility for Autonomous Goal Discovery]] (84.6% similar)
- [[2025-09-19/Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring_20250919|Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring]] (84.1% similar)
- [[2025-09-18/Reinforcement Learning for Autonomous Point-to-Point UAV Navigation_20250918|Reinforcement Learning for Autonomous Point-to-Point UAV Navigation]] (83.3% similar)
- [[2025-09-19/Digital Twin-based Cooperative Autonomous Driving in Smart Intersections_ A Multi-Agent Reinforcement Learning Approach_20250919|Digital Twin-based Cooperative Autonomous Driving in Smart Intersections: A Multi-Agent Reinforcement Learning Approach]] (83.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**⚡ Unique Technical**: [[keywords/Perception-Aware Reinforcement Learning|Perception-Aware Reinforcement Learning]], [[keywords/Autonomous Inspection|Autonomous Inspection]], [[keywords/Target Visibility|Target Visibility]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17877v1 Announce Type: cross 
Abstract: Autonomous inspection is a central problem in robotics, with applications ranging from industrial monitoring to search-and-rescue. Traditionally, inspection has often been reduced to navigation tasks, where the objective is to reach a predefined location while avoiding obstacles. However, this formulation captures only part of the real inspection problem. In real-world environments, the inspection targets may become visible well before their exact coordinates are reached, making further movement both redundant and inefficient. What matters more for inspection is not simply arriving at the target's position, but positioning the robot at a viewpoint from which the target becomes observable. In this work, we revisit inspection from a perception-aware perspective. We propose an end-to-end reinforcement learning framework that explicitly incorporates target visibility as the primary objective, enabling the robot to find the shortest trajectory that guarantees visual contact with the target without relying on a map. The learned policy leverages both perceptual and proprioceptive sensing and is trained entirely in simulation, before being deployed to a real-world robot. We further develop an algorithm to compute ground-truth shortest inspection paths, which provides a reference for evaluation. Through extensive experiments, we show that our method outperforms existing classical and learning-based navigation approaches, yielding more efficient inspection trajectories in both simulated and real-world settings. The project is avialable at https://sight-over-site.github.io/

## 📝 요약

이 논문은 자율 로봇의 검사 문제를 새로운 시각에서 접근하여, 목표물의 가시성을 최우선으로 고려하는 강화 학습 프레임워크를 제안합니다. 전통적인 탐색 방식은 목표 지점에 도달하는 것을 중시하지만, 이 연구는 목표물이 보이는 최적의 위치를 찾는 것이 더 중요하다고 주장합니다. 제안된 방법은 지도 없이도 목표물과의 시각적 접촉을 보장하는 최단 경로를 찾도록 설계되었습니다. 이를 위해 시뮬레이션 환경에서 학습된 정책을 실제 로봇에 적용하였고, 실험 결과 기존의 탐색 방법들보다 더 효율적인 경로를 제공함을 입증했습니다.

## 🎯 주요 포인트

- 1. 자율 검사 문제는 전통적으로 목표 지점에 도달하는 내비게이션 문제로 간주되었으나, 실제로는 목표를 관찰할 수 있는 위치에 로봇을 배치하는 것이 중요하다.
- 2. 본 연구는 목표 가시성을 주요 목표로 하는 강화 학습 프레임워크를 제안하여, 지도 없이도 목표를 시각적으로 관찰할 수 있는 최단 경로를 찾도록 한다.
- 3. 제안된 정책은 지각 및 고유 감각을 활용하며, 시뮬레이션에서 훈련된 후 실제 로봇에 적용된다.
- 4. 본 연구는 최단 검사 경로를 계산하는 알고리즘을 개발하여 평가 기준을 제공한다.
- 5. 실험 결과, 제안된 방법은 기존의 내비게이션 접근 방식을 능가하여 더 효율적인 검사 경로를 제공한다.


---

*Generated on 2025-09-24 05:12:51*