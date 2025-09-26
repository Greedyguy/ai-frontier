---
keywords:
  - Spatial Enhanced Manipulation
  - 3D Geometric Context
  - Robot State Encoder
  - Graph-Based Modeling
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2505.16196
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:25:48.571167",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Spatial Enhanced Manipulation",
    "3D Geometric Context",
    "Robot State Encoder",
    "Graph-Based Modeling"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Spatial Enhanced Manipulation": 0.8,
    "3D Geometric Context": 0.85,
    "Robot State Encoder": 0.78,
    "Graph-Based Modeling": 0.83
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Spatial Enhanced Manipulation",
        "canonical": "Spatial Enhanced Manipulation",
        "aliases": [
          "SEM"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel framework introduced in the paper, crucial for linking specific advancements in robot manipulation.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "3D geometric context",
        "canonical": "3D Geometric Context",
        "aliases": [
          "3D geometry"
        ],
        "category": "specific_connectable",
        "rationale": "Enhancing spatial understanding with 3D context is a key contribution, linking to spatial reasoning in robotics.",
        "novelty_score": 0.7,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      },
      {
        "surface": "robot state encoder",
        "canonical": "Robot State Encoder",
        "aliases": [
          "state encoder"
        ],
        "category": "unique_technical",
        "rationale": "Captures embodiment-aware structure, crucial for understanding robot manipulation dynamics.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "graph-based modeling",
        "canonical": "Graph-Based Modeling",
        "aliases": [
          "graph modeling"
        ],
        "category": "specific_connectable",
        "rationale": "Links to the use of graph structures in capturing dependencies, relevant to Graph Neural Networks.",
        "novelty_score": 0.68,
        "connectivity_score": 0.82,
        "specificity_score": 0.8,
        "link_intent_score": 0.83
      }
    ],
    "ban_list_suggestions": [
      "robot manipulation",
      "policy models",
      "visual representations"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Spatial Enhanced Manipulation",
      "resolved_canonical": "Spatial Enhanced Manipulation",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "3D geometric context",
      "resolved_canonical": "3D Geometric Context",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "robot state encoder",
      "resolved_canonical": "Robot State Encoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "graph-based modeling",
      "resolved_canonical": "Graph-Based Modeling",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.82,
        "specificity": 0.8,
        "link_intent": 0.83
      }
    }
  ]
}
-->

# SEM: Enhancing Spatial Understanding for Robust Robot Manipulation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.16196.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2505.16196](https://arxiv.org/abs/2505.16196)

## 🔗 유사한 논문
- [[2025-09-22/GP3_ A 3D Geometry-Aware Policy with Multi-View Images for Robotic Manipulation_20250922|GP3: A 3D Geometry-Aware Policy with Multi-View Images for Robotic Manipulation]] (85.9% similar)
- [[2025-09-24/PEEK_ Guiding and Minimal Image Representations for Zero-Shot Generalization of Robot Manipulation Policies_20250924|PEEK: Guiding and Minimal Image Representations for Zero-Shot Generalization of Robot Manipulation Policies]] (84.9% similar)
- [[2025-09-22/Spatial Understanding from Videos_ Structured Prompts Meet Simulation Data_20250922|Spatial Understanding from Videos: Structured Prompts Meet Simulation Data]] (84.2% similar)
- [[2025-09-23/A Modular Robotic System for Autonomous Exploration and Semantic Updating in Large-Scale Indoor Environments_20250923|A Modular Robotic System for Autonomous Exploration and Semantic Updating in Large-Scale Indoor Environments]] (83.7% similar)
- [[2025-09-24/Do You Need Proprioceptive States in Visuomotor Policies?_20250924|Do You Need Proprioceptive States in Visuomotor Policies?]] (83.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/3D Geometric Context|3D Geometric Context]], [[keywords/Graph-Based Modeling|Graph-Based Modeling]]
**⚡ Unique Technical**: [[keywords/Spatial Enhanced Manipulation|Spatial Enhanced Manipulation]], [[keywords/Robot State Encoder|Robot State Encoder]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.16196v3 Announce Type: replace-cross 
Abstract: A key challenge in robot manipulation lies in developing policy models with strong spatial understanding, the ability to reason about 3D geometry, object relations, and robot embodiment. Existing methods often fall short: 3D point cloud models lack semantic abstraction, while 2D image encoders struggle with spatial reasoning. To address this, we propose SEM (Spatial Enhanced Manipulation model), a novel diffusion-based policy framework that explicitly enhances spatial understanding from two complementary perspectives. A spatial enhancer augments visual representations with 3D geometric context, while a robot state encoder captures embodiment-aware structure through graphbased modeling of joint dependencies. By integrating these modules, SEM significantly improves spatial understanding, leading to robust and generalizable manipulation across diverse tasks that outperform existing baselines.

## 📝 요약

로봇 조작에서 공간 이해를 강화하기 위해 SEM(Spatial Enhanced Manipulation) 모델을 제안합니다. 이 모델은 3D 기하학 및 객체 관계를 이해하는 데 중점을 둡니다. 기존의 3D 포인트 클라우드 모델과 2D 이미지 인코더의 한계를 극복하기 위해, SEM은 시각적 표현에 3D 기하학적 맥락을 추가하는 공간 향상기와 로봇 상태 인코더를 사용하여 조인트 의존성을 그래프 기반으로 모델링합니다. 이를 통해 다양한 작업에서 기존 모델보다 뛰어난 성능을 보이며, 강력하고 일반화 가능한 조작을 가능하게 합니다.

## 🎯 주요 포인트

- 1. 로봇 조작의 주요 과제는 3D 기하학, 객체 관계 및 로봇 구현에 대한 공간 이해 능력을 갖춘 정책 모델 개발이다.
- 2. 기존의 3D 포인트 클라우드 모델과 2D 이미지 인코더는 각각 의미적 추상화와 공간 추론에서 한계를 보인다.
- 3. 제안된 SEM 모델은 공간 이해를 강화하기 위해 시각적 표현에 3D 기하학적 맥락을 추가하는 공간 강화기와 로봇 상태 인코더를 통합한다.
- 4. SEM은 다양한 작업에서 기존의 기준선을 능가하는 강력하고 일반화 가능한 조작을 가능하게 한다.


---

*Generated on 2025-09-25 16:25:48*