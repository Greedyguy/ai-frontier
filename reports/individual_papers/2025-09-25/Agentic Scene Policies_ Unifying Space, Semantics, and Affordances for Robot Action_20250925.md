---
keywords:
  - Agentic Scene Policies
  - Vision-Language Model
  - Zero-Shot Learning
  - Object Affordances
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.19571
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:17:38.279110",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Agentic Scene Policies",
    "Vision-Language Model",
    "Zero-Shot Learning",
    "Object Affordances"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Agentic Scene Policies": 0.78,
    "Vision-Language Model": 0.82,
    "Zero-Shot Learning": 0.85,
    "Object Affordances": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Agentic Scene Policies",
        "canonical": "Agentic Scene Policies",
        "aliases": [
          "ASP"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel framework for robot action using scene representations, which is central to the paper's contributions.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Vision-Language-Actions models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLA"
        ],
        "category": "evolved_concepts",
        "rationale": "Connects to the growing field of integrating vision and language for robotic actions, enhancing cross-domain linking.",
        "novelty_score": 0.7,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Zero-shot manner",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-shot"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the capability of executing tasks without prior examples, a key aspect of modern AI models.",
        "novelty_score": 0.65,
        "connectivity_score": 0.9,
        "specificity_score": 0.75,
        "link_intent_score": 0.85
      },
      {
        "surface": "Object affordances",
        "canonical": "Object Affordances",
        "aliases": [
          "Affordances"
        ],
        "category": "specific_connectable",
        "rationale": "Essential for understanding how objects can be interacted with, crucial for robotic manipulation tasks.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "robot",
      "scene representation",
      "language-conditioned"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Agentic Scene Policies",
      "resolved_canonical": "Agentic Scene Policies",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Vision-Language-Actions models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Zero-shot manner",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.9,
        "specificity": 0.75,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Object affordances",
      "resolved_canonical": "Object Affordances",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Agentic Scene Policies: Unifying Space, Semantics, and Affordances for Robot Action

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19571.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.19571](https://arxiv.org/abs/2509.19571)

## 🔗 유사한 논문
- [[2025-09-24/PEEK_ Guiding and Minimal Image Representations for Zero-Shot Generalization of Robot Manipulation Policies_20250924|PEEK: Guiding and Minimal Image Representations for Zero-Shot Generalization of Robot Manipulation Policies]] (84.0% similar)
- [[2025-09-18/Robot Control Stack_ A Lean Ecosystem for Robot Learning at Scale_20250918|Robot Control Stack: A Lean Ecosystem for Robot Learning at Scale]] (83.3% similar)
- [[2025-09-24/Pure Vision Language Action (VLA) Models_ A Comprehensive Survey_20250924|Pure Vision Language Action (VLA) Models: A Comprehensive Survey]] (83.3% similar)
- [[2025-09-23/Evo-0_ Vision-Language-Action Model with Implicit Spatial Understanding_20250923|Evo-0: Vision-Language-Action Model with Implicit Spatial Understanding]] (82.7% similar)
- [[2025-09-22/A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning_20250922|A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning]] (82.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]], [[keywords/Object Affordances|Object Affordances]]
**⚡ Unique Technical**: [[keywords/Agentic Scene Policies|Agentic Scene Policies]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19571v1 Announce Type: cross 
Abstract: Executing open-ended natural language queries is a core problem in robotics. While recent advances in imitation learning and vision-language-actions models (VLAs) have enabled promising end-to-end policies, these models struggle when faced with complex instructions and new scenes. An alternative is to design an explicit scene representation as a queryable interface between the robot and the world, using query results to guide downstream motion planning. In this work, we present Agentic Scene Policies (ASP), an agentic framework that leverages the advanced semantic, spatial, and affordance-based querying capabilities of modern scene representations to implement a capable language-conditioned robot policy. ASP can execute open-vocabulary queries in a zero-shot manner by explicitly reasoning about object affordances in the case of more complex skills. Through extensive experiments, we compare ASP with VLAs on tabletop manipulation problems and showcase how ASP can tackle room-level queries through affordance-guided navigation, and a scaled-up scene representation. (Project page: https://montrealrobotics.ca/agentic-scene-policies.github.io/)

## 📝 요약

이 논문은 로봇이 복잡한 자연어 질의를 처리하는 문제를 다룹니다. 기존의 모방 학습과 비전-언어-행동(VLA) 모델은 복잡한 지시와 새로운 장면에서 어려움을 겪습니다. 이에 대한 대안으로, 로봇과 세계 사이의 질의 가능한 인터페이스로 명시적인 장면 표현을 설계하고, 이를 통해 모션 계획을 안내하는 방법을 제안합니다. 본 연구에서는 Agentic Scene Policies (ASP)라는 프레임워크를 소개하며, 이는 현대 장면 표현의 고급 의미적, 공간적, 기능적 질의 능력을 활용하여 언어 조건에 맞는 로봇 정책을 구현합니다. ASP는 객체의 기능을 명시적으로 추론하여 복잡한 기술을 무작위로 수행할 수 있으며, 실험을 통해 ASP가 VLA 모델과 비교하여 테이블탑 조작 문제와 방 수준의 질의를 해결하는 능력을 입증합니다.

## 🎯 주요 포인트

- 1. Agentic Scene Policies (ASP)는 현대의 장면 표현의 고급 의미적, 공간적, 사용 가능성 기반 쿼리 기능을 활용하여 언어 조건 로봇 정책을 구현하는 프레임워크입니다.
- 2. ASP는 객체의 사용 가능성을 명시적으로 추론하여 복잡한 기술에서도 개방형 어휘 쿼리를 제로샷 방식으로 실행할 수 있습니다.
- 3. 실험을 통해 ASP는 테이블탑 조작 문제에서 VLAs와 비교하여 우수한 성능을 보였으며, 사용 가능성 기반 내비게이션과 확장된 장면 표현을 통해 방 수준의 쿼리를 처리할 수 있음을 입증했습니다.
- 4. ASP는 로봇과 세계 사이의 쿼리 가능한 인터페이스로 명시적인 장면 표현을 설계하여 복잡한 지시와 새로운 장면에서의 문제를 해결합니다.


---

*Generated on 2025-09-26 09:17:38*