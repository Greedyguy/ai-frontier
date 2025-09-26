---
keywords:
  - Large Language Model
  - VORTEX Framework
  - Pareto-optimal Trade-offs
  - Human-AI Collaborative Optimization
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16399
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T22:48:52.073019",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "VORTEX Framework",
    "Pareto-optimal Trade-offs",
    "Human-AI Collaborative Optimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.88,
    "VORTEX Framework": 0.85,
    "Pareto-optimal Trade-offs": 0.78,
    "Human-AI Collaborative Optimization": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the reward shaping framework discussed, linking to broader AI and NLP topics.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.88
      },
      {
        "surface": "VORTEX",
        "canonical": "VORTEX Framework",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "VORTEX is a novel framework introduced in the paper, crucial for understanding the proposed method.",
        "novelty_score": 0.95,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Pareto-optimal trade-offs",
        "canonical": "Pareto-optimal Trade-offs",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Pareto-optimal trade-offs are key to the optimization goals of the framework, linking to multi-objective optimization concepts.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Human-AI collaborative optimization",
        "canonical": "Human-AI Collaborative Optimization",
        "aliases": [],
        "category": "evolved_concepts",
        "rationale": "This concept represents a growing area of research in AI, emphasizing collaboration between human preferences and AI systems.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "solver",
      "preference descriptions",
      "real-world allocation tasks"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "VORTEX",
      "resolved_canonical": "VORTEX Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Pareto-optimal trade-offs",
      "resolved_canonical": "Pareto-optimal Trade-offs",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Human-AI collaborative optimization",
      "resolved_canonical": "Human-AI Collaborative Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# VORTEX: Aligning Task Utility and Human Preferences through LLM-Guided Reward Shaping

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16399.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16399](https://arxiv.org/abs/2509.16399)

## 🔗 유사한 논문
- [[2025-09-19/Ask-to-Clarify_ Resolving Instruction Ambiguity through Multi-turn Dialogue_20250919|Ask-to-Clarify: Resolving Instruction Ambiguity through Multi-turn Dialogue]] (83.6% similar)
- [[2025-09-22/A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning_20250922|A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning]] (82.8% similar)
- [[2025-09-19/Zero-Shot LLMs in Human-in-the-Loop RL_ Replacing Human Feedback for Reward Shaping_20250919|Zero-Shot LLMs in Human-in-the-Loop RL: Replacing Human Feedback for Reward Shaping]] (82.5% similar)
- [[2025-09-19/Emergent Alignment via Competition_20250919|Emergent Alignment via Competition]] (81.8% similar)
- [[2025-09-19/CollabVLA_ Self-Reflective Vision-Language-Action Model Dreaming Together with Human_20250919|CollabVLA: Self-Reflective Vision-Language-Action Model Dreaming Together with Human]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Pareto-optimal Trade-offs|Pareto-optimal Trade-offs]]
**⚡ Unique Technical**: [[keywords/VORTEX Framework|VORTEX Framework]]
**🚀 Evolved Concepts**: [[keywords/Human-AI Collaborative Optimization|Human-AI Collaborative Optimization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16399v1 Announce Type: new 
Abstract: In social impact optimization, AI decision systems often rely on solvers that optimize well-calibrated mathematical objectives. However, these solvers cannot directly accommodate evolving human preferences, typically expressed in natural language rather than formal constraints. Recent approaches address this by using large language models (LLMs) to generate new reward functions from preference descriptions. While flexible, they risk sacrificing the system's core utility guarantees. In this paper, we propose \texttt{VORTEX}, a language-guided reward shaping framework that preserves established optimization goals while adaptively incorporating human feedback. By formalizing the problem as multi-objective optimization, we use LLMs to iteratively generate shaping rewards based on verbal reinforcement and text-gradient prompt updates. This allows stakeholders to steer decision behavior via natural language without modifying solvers or specifying trade-off weights. We provide theoretical guarantees that \texttt{VORTEX} converges to Pareto-optimal trade-offs between utility and preference satisfaction. Empirical results in real-world allocation tasks demonstrate that \texttt{VORTEX} outperforms baselines in satisfying human-aligned coverage goals while maintaining high task performance. This work introduces a practical and theoretically grounded paradigm for human-AI collaborative optimization guided by natural language.

## 📝 요약

이 논문에서는 인간의 선호를 자연어로 표현하여 AI 의사결정 시스템에 통합하는 새로운 프레임워크 \texttt{VORTEX}를 제안합니다. 기존의 최적화 목표를 유지하면서도 인간의 피드백을 적응적으로 반영할 수 있도록 설계되었습니다. \texttt{VORTEX}는 다목적 최적화 문제로 공식화하여, 대형 언어 모델(LLM)을 활용해 언어적 강화와 텍스트-그래디언트 프롬프트 업데이트를 통해 보상 함수를 생성합니다. 이 접근법은 솔버를 수정하거나 가중치를 지정하지 않고도 자연어로 의사결정 행동을 조정할 수 있게 합니다. 이론적으로는 유틸리티와 선호 만족 간의 파레토 최적 해에 수렴함을 보장하며, 실제 할당 작업에서 인간의 목표를 잘 반영하면서도 높은 성능을 유지하는 것을 실증적으로 입증했습니다. 이는 자연어로 인간과 AI가 협력하여 최적화를 수행하는 실용적이고 이론적으로 기반이 있는 새로운 패러다임을 제시합니다.

## 🎯 주요 포인트

- 1. \texttt{VORTEX}는 인간의 피드백을 적응적으로 반영하면서 기존 최적화 목표를 유지하는 언어 기반 보상 조정 프레임워크입니다.
- 2. 이 연구는 다목적 최적화 문제로 문제를 공식화하여, LLM을 사용해 언어적 강화와 텍스트-그래디언트 프롬프트 업데이트를 통해 보상을 생성합니다.
- 3. \texttt{VORTEX}는 자연어를 통해 이해관계자가 의사결정 행동을 조정할 수 있게 하며, 이 과정에서 솔버를 수정하거나 상충 가중치를 지정할 필요가 없습니다.
- 4. 이론적 보장을 통해 \texttt{VORTEX}가 효용성과 선호 만족 간의 파레토 최적 교환에 수렴함을 증명합니다.
- 5. 실제 할당 작업에서 \texttt{VORTEX}는 인간 정렬 커버리지 목표를 만족시키면서 높은 작업 성능을 유지하며 기존 기준을 능가하는 성과를 보였습니다.


---

*Generated on 2025-09-23 22:48:52*