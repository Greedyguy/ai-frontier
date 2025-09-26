---
keywords:
  - SMART-3D Algorithm
  - Adaptive Replanning
  - Dynamic Environments
  - Hot-Nodes
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16812
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:34:43.131430",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "SMART-3D Algorithm",
    "Adaptive Replanning",
    "Dynamic Environments",
    "Hot-Nodes"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "SMART-3D Algorithm": 0.8,
    "Adaptive Replanning": 0.75,
    "Dynamic Environments": 0.7,
    "Hot-Nodes": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "SMART-3D",
        "canonical": "SMART-3D Algorithm",
        "aliases": [
          "Three-Dimensional Self-Morphing Adaptive Replanning Tree"
        ],
        "category": "unique_technical",
        "rationale": "SMART-3D is a novel extension of the SMART algorithm specifically designed for dynamic 3D environments, making it a unique technical concept.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "adaptive replanning",
        "canonical": "Adaptive Replanning",
        "aliases": [
          "dynamic replanning"
        ],
        "category": "specific_connectable",
        "rationale": "Adaptive replanning is key to the algorithm's ability to handle dynamic environments, connecting to broader themes of real-time decision-making.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "dynamic environments",
        "canonical": "Dynamic Environments",
        "aliases": [
          "changing environments"
        ],
        "category": "broad_technical",
        "rationale": "Understanding dynamic environments is crucial for applications in robotics and AI, providing a broad technical context.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "hot-nodes",
        "canonical": "Hot-Nodes",
        "aliases": [
          "hot spots"
        ],
        "category": "unique_technical",
        "rationale": "Hot-nodes are a novel concept introduced in SMART-3D for efficient tree morphing, highlighting its technical uniqueness.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "algorithm",
      "performance",
      "simulations"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "SMART-3D",
      "resolved_canonical": "SMART-3D Algorithm",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "adaptive replanning",
      "resolved_canonical": "Adaptive Replanning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "dynamic environments",
      "resolved_canonical": "Dynamic Environments",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "hot-nodes",
      "resolved_canonical": "Hot-Nodes",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# SMART-3D: Three-Dimensional Self-Morphing Adaptive Replanning Tree

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16812.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16812](https://arxiv.org/abs/2509.16812)

## 🔗 유사한 논문
- [[2025-09-19/Multi-CAP_ A Multi-Robot Connectivity-Aware Hierarchical Coverage Path Planning Algorithm for Unknown Environments_20250919|Multi-CAP: A Multi-Robot Connectivity-Aware Hierarchical Coverage Path Planning Algorithm for Unknown Environments]] (80.8% similar)
- [[2025-09-22/GP3_ A 3D Geometry-Aware Policy with Multi-View Images for Robotic Manipulation_20250922|GP3: A 3D Geometry-Aware Policy with Multi-View Images for Robotic Manipulation]] (80.6% similar)
- [[2025-09-19/PA-MPPI_ Perception-Aware Model Predictive Path Integral Control for Quadrotor Navigation in Unknown Environments_20250919|PA-MPPI: Perception-Aware Model Predictive Path Integral Control for Quadrotor Navigation in Unknown Environments]] (79.7% similar)
- [[2025-09-23/Sycophancy Mitigation Through Reinforcement Learning with Uncertainty-Aware Adaptive Reasoning Trajectories_20250923|Sycophancy Mitigation Through Reinforcement Learning with Uncertainty-Aware Adaptive Reasoning Trajectories]] (79.5% similar)
- [[2025-09-23/Text-Scene_ A Scene-to-Language Parsing Framework for 3D Scene Understanding_20250923|Text-Scene: A Scene-to-Language Parsing Framework for 3D Scene Understanding]] (79.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Dynamic Environments|Dynamic Environments]]
**🔗 Specific Connectable**: [[keywords/Adaptive Replanning|Adaptive Replanning]]
**⚡ Unique Technical**: [[keywords/SMART-3D Algorithm|SMART-3D Algorithm]], [[keywords/Hot-Nodes|Hot-Nodes]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16812v1 Announce Type: cross 
Abstract: This paper presents SMART-3D, an extension of the SMART algorithm to 3D environments. SMART-3D is a tree-based adaptive replanning algorithm for dynamic environments with fast moving obstacles. SMART-3D morphs the underlying tree to find a new path in real-time whenever the current path is blocked by obstacles. SMART-3D removed the grid decomposition requirement of the SMART algorithm by replacing the concept of hot-spots with that of hot-nodes, thus making it computationally efficient and scalable to 3D environments. The hot-nodes are nodes which allow for efficient reconnections to morph the existing tree to find a new safe and reliable path. The performance of SMART-3D is evaluated by extensive simulations in 2D and 3D environments populated with randomly moving dynamic obstacles. The results show that SMART-3D achieves high success rates and low replanning times, thus highlighting its suitability for real-time onboard applications.

## 📝 요약

이 논문은 SMART 알고리즘을 3D 환경으로 확장한 SMART-3D를 소개합니다. SMART-3D는 빠르게 움직이는 장애물이 있는 동적 환경에서 실시간으로 경로를 재계획하는 트리 기반 알고리즘입니다. 기존 SMART 알고리즘의 격자 분해 요구 사항을 제거하고, '핫-노드' 개념을 도입하여 3D 환경에서도 효율적이고 확장 가능하게 만들었습니다. '핫-노드'는 기존 트리를 변형하여 새로운 안전 경로를 찾는 데 도움을 줍니다. 2D 및 3D 환경에서의 시뮬레이션 결과, SMART-3D는 높은 성공률과 짧은 재계획 시간을 보여 실시간 응용에 적합함을 입증했습니다.

## 🎯 주요 포인트

- 1. SMART-3D는 SMART 알고리즘을 3D 환경으로 확장한 알고리즘으로, 빠르게 움직이는 장애물이 있는 동적 환경에서의 적응형 재계획 알고리즘입니다.
- 2. SMART-3D는 기존 경로가 장애물에 의해 차단될 때마다 실시간으로 새로운 경로를 찾기 위해 트리를 변형합니다.
- 3. SMART-3D는 핫-노드 개념을 도입하여 그리드 분해 요구 사항을 제거함으로써 계산 효율성과 3D 환경에 대한 확장성을 높였습니다.
- 4. SMART-3D의 성능은 무작위로 움직이는 동적 장애물이 있는 2D 및 3D 환경에서의 광범위한 시뮬레이션을 통해 평가되었습니다.
- 5. 결과는 SMART-3D가 높은 성공률과 낮은 재계획 시간을 달성하여 실시간 온보드 애플리케이션에 적합함을 보여줍니다.


---

*Generated on 2025-09-23 23:34:43*