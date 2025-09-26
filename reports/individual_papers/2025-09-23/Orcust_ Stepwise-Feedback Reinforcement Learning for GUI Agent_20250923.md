---
keywords:
  - Principle-Constrained Reward Modeling
  - Online VM-Grounded Trajectory Construction
  - Large Language Model
  - ScreenSpot
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17917
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:04:10.664108",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Principle-Constrained Reward Modeling",
    "Online VM-Grounded Trajectory Construction",
    "Large Language Model",
    "ScreenSpot"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Principle-Constrained Reward Modeling": 0.78,
    "Online VM-Grounded Trajectory Construction": 0.75,
    "Large Language Model": 0.8,
    "ScreenSpot": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Principle-Constrained Reward Modeling",
        "canonical": "Principle-Constrained Reward Modeling",
        "aliases": [
          "PCRM"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's novel approach to enhancing GUI agent performance and is not covered by existing canonical terms.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Online VM-Grounded Trajectory Construction",
        "canonical": "Online VM-Grounded Trajectory Construction",
        "aliases": [
          "OVTC"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique method introduced in the paper for generating GUI interaction trajectories, which is crucial for understanding the paper's contribution.",
        "novelty_score": 0.82,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.75
      },
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are integral to the paper's approach for deriving principles and enhancing reward modeling.",
        "novelty_score": 0.3,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "ScreenSpot",
        "canonical": "ScreenSpot",
        "aliases": [
          "ScreenSpot-Pro"
        ],
        "category": "unique_technical",
        "rationale": "ScreenSpot is a benchmark used to demonstrate the effectiveness of the proposed framework, highlighting its practical application.",
        "novelty_score": 0.7,
        "connectivity_score": 0.55,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "reward signals",
      "task execution"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Principle-Constrained Reward Modeling",
      "resolved_canonical": "Principle-Constrained Reward Modeling",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Online VM-Grounded Trajectory Construction",
      "resolved_canonical": "Online VM-Grounded Trajectory Construction",
      "decision": "linked",
      "scores": {
        "novelty": 0.82,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "ScreenSpot",
      "resolved_canonical": "ScreenSpot",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.55,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Orcust: Stepwise-Feedback Reinforcement Learning for GUI Agent

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17917.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17917](https://arxiv.org/abs/2509.17917)

## 🔗 유사한 논문
- [[2025-09-22/GUI-ARP_ Enhancing Grounding with Adaptive Region Perception for GUI Agents_20250922|GUI-ARP: Enhancing Grounding with Adaptive Region Perception for GUI Agents]] (86.4% similar)
- [[2025-09-22/GUI-ReWalk_ Massive Data Generation for GUI Agent via Stochastic Exploration and Intent-Aware Reasoning_20250922|GUI-ReWalk: Massive Data Generation for GUI Agent via Stochastic Exploration and Intent-Aware Reasoning]] (84.7% similar)
- [[2025-09-22/ORCA_ Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models_20250922|ORCA: Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models]] (83.3% similar)
- [[2025-09-22/BTL-UI_ Blink-Think-Link Reasoning Model for GUI Agent_20250922|BTL-UI: Blink-Think-Link Reasoning Model for GUI Agent]] (81.2% similar)
- [[2025-09-18/TGPO_ Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning_20250918|TGPO: Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Principle-Constrained Reward Modeling|Principle-Constrained Reward Modeling]], [[keywords/Online VM-Grounded Trajectory Construction|Online VM-Grounded Trajectory Construction]], [[keywords/ScreenSpot|ScreenSpot]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17917v1 Announce Type: new 
Abstract: Recent advances in GUI agents have achieved remarkable grounding and action-prediction performance, yet existing models struggle with unreliable reward signals and limited online trajectory generation. In this paper, we introduce Orcust, a framework that integrates Principle-Constrained Reward Modeling (PCRM) and Online VM-Grounded Trajectory Construction (OVTC) to enhance reasoning reliability and data efficiency in interactive GUI tasks. We leverages environment-verifiable and LLM-derived principle to enforce interpretable reward signals that constrain long chain-of-thought reasoning and rule-based feedback. OVTC spins up instrumented virtual machines to autonomously collect structured GUI interaction trajectories with explicit procedural and structural objectives, enabling the training of a stepwise reward model that robustly captures human preferences and adheres to task-specific constraints. Extensive experiments on standard GUI benchmarks covering perceptual grounding, foundational operations, and end-to-end task execution reveal that Orcust achieves state-of-the-art performance, improving by 22.2\% on ScreenSpot and 23.9\% on ScreenSpot-Pro over the base model (i.e. Qwen2.5-VL-7B). The results demonstrate Orcust's effectiveness in enhancing the reasoning, adaptability and scalability of GUI agents across various environments and task complexities.

## 📝 요약

Orcust는 GUI 에이전트의 신뢰성과 데이터 효율성을 높이기 위해 Principle-Constrained Reward Modeling(PCRM)과 Online VM-Grounded Trajectory Construction(OVTC)을 통합한 프레임워크입니다. 이 시스템은 해석 가능한 보상 신호를 통해 복잡한 추론과 규칙 기반 피드백을 강화하며, 가상 머신을 활용해 구조화된 GUI 상호작용 경로를 수집합니다. 이를 통해 인간의 선호를 반영하고 과제별 제약을 준수하는 보상 모델을 훈련합니다. 실험 결과, Orcust는 ScreenSpot과 ScreenSpot-Pro에서 각각 22.2%와 23.9% 성능 향상을 보여, 다양한 환경과 과제 복잡성에서 GUI 에이전트의 추론 능력과 적응성, 확장성을 크게 개선했습니다.

## 🎯 주요 포인트

- 1. Orcust는 Principle-Constrained Reward Modeling(PCRM)과 Online VM-Grounded Trajectory Construction(OVTC)을 통합하여 GUI 작업에서 추론 신뢰성과 데이터 효율성을 향상시킵니다.
- 2. 환경 검증 가능하고 LLM에서 파생된 원칙을 활용하여 해석 가능한 보상 신호를 강화하고, 장기적인 사고 과정을 제한하며 규칙 기반 피드백을 제공합니다.
- 3. OVTC는 가상 머신을 활용하여 명시적인 절차적 및 구조적 목표를 가진 GUI 상호작용 경로를 자동으로 수집하여 인간의 선호를 포착하고 작업별 제약을 준수하는 보상 모델을 훈련합니다.
- 4. Orcust는 표준 GUI 벤치마크에서 22.2% (ScreenSpot) 및 23.9% (ScreenSpot-Pro)의 성능 향상을 보여주며, GUI 에이전트의 추론, 적응성 및 확장성을 강화합니다.


---

*Generated on 2025-09-23 23:04:10*