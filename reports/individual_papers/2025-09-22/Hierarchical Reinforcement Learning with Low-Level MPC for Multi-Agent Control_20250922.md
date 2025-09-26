---
keywords:
  - Hierarchical Reinforcement Learning
  - Model Predictive Control
  - Multi-Agent Systems
  - Structured Regions of Interest
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15799
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:13:54.990414",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Hierarchical Reinforcement Learning",
    "Model Predictive Control",
    "Multi-Agent Systems",
    "Structured Regions of Interest"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Hierarchical Reinforcement Learning": 0.78,
    "Model Predictive Control": 0.82,
    "Multi-Agent Systems": 0.8,
    "Structured Regions of Interest": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Hierarchical Reinforcement Learning",
        "canonical": "Hierarchical Reinforcement Learning",
        "aliases": [
          "HRL"
        ],
        "category": "unique_technical",
        "rationale": "Hierarchical Reinforcement Learning is a distinct approach that enhances connectivity by bridging high-level decision-making with low-level execution.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Model Predictive Control",
        "canonical": "Model Predictive Control",
        "aliases": [
          "MPC"
        ],
        "category": "specific_connectable",
        "rationale": "Model Predictive Control is a well-established technique that ensures safe and feasible motion, connecting structured learning with control systems.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Multi-Agent Systems",
        "canonical": "Multi-Agent Systems",
        "aliases": [
          "MAS"
        ],
        "category": "specific_connectable",
        "rationale": "Multi-Agent Systems are crucial for understanding interactions in complex environments, enhancing connectivity with other multi-agent frameworks.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      },
      {
        "surface": "Structured Regions of Interest",
        "canonical": "Structured Regions of Interest",
        "aliases": [
          "ROIs"
        ],
        "category": "unique_technical",
        "rationale": "Structured Regions of Interest are key to high-level policy selection, providing a unique perspective on spatial decision-making.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "end-to-end learning",
      "sample efficiency",
      "reward",
      "safety",
      "consistency"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Hierarchical Reinforcement Learning",
      "resolved_canonical": "Hierarchical Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Model Predictive Control",
      "resolved_canonical": "Model Predictive Control",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Multi-Agent Systems",
      "resolved_canonical": "Multi-Agent Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Structured Regions of Interest",
      "resolved_canonical": "Structured Regions of Interest",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control

**Korean Title:** 다중 에이전트 제어를 위한 저수준 MPC를 활용한 계층적 강화 학습

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15799.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15799](https://arxiv.org/abs/2509.15799)

## 🔗 유사한 논문
- [[2025-09-22/Explainable AI-Enhanced Supervisory Control for Robust Multi-Agent Robotic Systems_20250922|Explainable AI-Enhanced Supervisory Control for Robust Multi-Agent Robotic Systems]] (84.9% similar)
- [[2025-09-19/Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (84.7% similar)
- [[2025-09-19/Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning_20250919|Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning]] (84.6% similar)
- [[2025-09-19/Local-Canonicalization Equivariant Graph Neural Networks for Sample-Efficient and Generalizable Swarm Robot Control_20250919|Local-Canonicalization Equivariant Graph Neural Networks for Sample-Efficient and Generalizable Swarm Robot Control]] (84.3% similar)
- [[2025-09-19/ActivePusher_ Active Learning and Planning with Residual Physics for Nonprehensile Manipulation_20250919|ActivePusher: Active Learning and Planning with Residual Physics for Nonprehensile Manipulation]] (84.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Model Predictive Control|Model Predictive Control]], [[keywords/Multi-Agent Systems|Multi-Agent Systems]]
**⚡ Unique Technical**: [[keywords/Hierarchical Reinforcement Learning|Hierarchical Reinforcement Learning]], [[keywords/Structured Regions of Interest|Structured Regions of Interest]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15799v1 Announce Type: cross 
Abstract: Achieving safe and coordinated behavior in dynamic, constraint-rich environments remains a major challenge for learning-based control. Pure end-to-end learning often suffers from poor sample efficiency and limited reliability, while model-based methods depend on predefined references and struggle to generalize. We propose a hierarchical framework that combines tactical decision-making via reinforcement learning (RL) with low-level execution through Model Predictive Control (MPC). For the case of multi-agent systems this means that high-level policies select abstract targets from structured regions of interest (ROIs), while MPC ensures dynamically feasible and safe motion. Tested on a predator-prey benchmark, our approach outperforms end-to-end and shielding-based RL baselines in terms of reward, safety, and consistency, underscoring the benefits of combining structured learning with model-based control.

## 🔍 Abstract (한글 번역)

arXiv:2509.15799v1 발표 유형: 교차  
초록: 동적이고 제약이 많은 환경에서 안전하고 조정된 행동을 달성하는 것은 학습 기반 제어에 있어 여전히 주요 과제입니다. 순수한 종단 간 학습은 샘플 효율성이 낮고 신뢰성이 제한적이며, 모델 기반 방법은 사전에 정의된 참조에 의존하고 일반화에 어려움을 겪습니다. 우리는 강화 학습(RL)을 통한 전술적 의사 결정과 모델 예측 제어(MPC)를 통한 저수준 실행을 결합한 계층적 프레임워크를 제안합니다. 다중 에이전트 시스템의 경우, 이는 고수준 정책이 관심 영역(ROIs)의 구조화된 영역에서 추상적인 목표를 선택하는 반면, MPC는 동적으로 실현 가능하고 안전한 움직임을 보장한다는 것을 의미합니다. 포식자-피식자 벤치마크에서 테스트한 결과, 우리의 접근 방식은 보상, 안전성 및 일관성 측면에서 종단 간 및 차폐 기반 RL 기준선을 능가하여 구조화된 학습과 모델 기반 제어를 결합한 이점을 강조합니다.

## 📝 요약

이 논문은 동적이고 제약이 많은 환경에서 안전하고 조정된 행동을 달성하기 위한 학습 기반 제어의 도전 과제를 다룹니다. 저자들은 강화학습(RL)을 통한 전술적 의사결정과 모델 예측 제어(MPC)를 통한 저수준 실행을 결합한 계층적 프레임워크를 제안합니다. 다중 에이전트 시스템의 경우, 고수준 정책은 구조화된 관심 영역(ROIs)에서 추상적인 목표를 선택하고, MPC는 동적으로 실행 가능한 안전한 움직임을 보장합니다. 포식자-피식자 벤치마크에서 이 접근법은 보상, 안전성, 일관성 측면에서 기존의 RL 기반 방법을 능가하며, 구조화된 학습과 모델 기반 제어의 결합이 가져오는 이점을 강조합니다.

## 🎯 주요 포인트

- 1. 학습 기반 제어에서 안전하고 조정된 행동을 달성하는 것은 여전히 주요 과제입니다.
- 2. 순수한 종단 간 학습은 샘플 효율성과 신뢰성이 부족한 반면, 모델 기반 방법은 일반화에 어려움을 겪습니다.
- 3. 강화 학습을 통한 전술적 의사 결정과 모델 예측 제어를 통한 저수준 실행을 결합한 계층적 프레임워크를 제안합니다.
- 4. 다중 에이전트 시스템에서는 고수준 정책이 관심 영역에서 추상적 목표를 선택하고, MPC가 동적으로 실행 가능한 안전한 움직임을 보장합니다.
- 5. 포식자-피식자 벤치마크에서 제안된 방법이 보상, 안전성, 일관성 측면에서 기존 방법들을 능가했습니다.


---

*Generated on 2025-09-23 09:13:54*