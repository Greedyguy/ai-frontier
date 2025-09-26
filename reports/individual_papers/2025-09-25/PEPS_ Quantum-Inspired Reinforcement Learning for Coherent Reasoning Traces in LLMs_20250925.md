---
keywords:
  - Large Language Model
  - Projected Entangled Pair States
  - Proximal Policy Optimization
  - Quantum-Inspired Learning
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.20105
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:19:33.421638",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Projected Entangled Pair States",
    "Proximal Policy Optimization",
    "Quantum-Inspired Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Projected Entangled Pair States": 0.8,
    "Proximal Policy Optimization": 0.82,
    "Quantum-Inspired Learning": 0.78
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
        "rationale": "A foundational concept in the paper, linking to a broad range of NLP research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Projected Entangled Pair States",
        "canonical": "Projected Entangled Pair States",
        "aliases": [
          "PEPS"
        ],
        "category": "unique_technical",
        "rationale": "A unique quantum concept applied in the paper, offering novel insights into coherence in reasoning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Proximal Policy Optimization",
        "canonical": "Proximal Policy Optimization",
        "aliases": [
          "PPO"
        ],
        "category": "specific_connectable",
        "rationale": "A key reinforcement learning algorithm used in the methodology, relevant for linking to RL research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "quantum-inspired approach",
        "canonical": "Quantum-Inspired Learning",
        "aliases": [
          "quantum-inspired method"
        ],
        "category": "evolved_concepts",
        "rationale": "Represents a novel intersection of quantum mechanics and machine learning, fostering interdisciplinary links.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "method",
      "approach",
      "framework"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Projected Entangled Pair States",
      "resolved_canonical": "Projected Entangled Pair States",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Proximal Policy Optimization",
      "resolved_canonical": "Proximal Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "quantum-inspired approach",
      "resolved_canonical": "Quantum-Inspired Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# PEPS: Quantum-Inspired Reinforcement Learning for Coherent Reasoning Traces in LLMs

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20105.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.20105](https://arxiv.org/abs/2509.20105)

## 🔗 유사한 논문
- [[2025-09-23/How Can Quantum Deep Learning Improve Large Language Models?_20250923|How Can Quantum Deep Learning Improve Large Language Models?]] (86.0% similar)
- [[2025-09-23/EvoCoT_ Overcoming the Exploration Bottleneck in Reinforcement Learning_20250923|EvoCoT: Overcoming the Exploration Bottleneck in Reinforcement Learning]] (85.5% similar)
- [[2025-09-24/Reinforcement Learning on Pre-Training Data_20250924|Reinforcement Learning on Pre-Training Data]] (85.0% similar)
- [[2025-09-24/ReSearch_ Learning to Reason with Search for LLMs via Reinforcement Learning_20250924|ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning]] (84.8% similar)
- [[2025-09-23/GPO_ Learning from Critical Steps to Improve LLM Reasoning_20250923|GPO: Learning from Critical Steps to Improve LLM Reasoning]] (84.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Proximal Policy Optimization|Proximal Policy Optimization]]
**⚡ Unique Technical**: [[keywords/Projected Entangled Pair States|Projected Entangled Pair States]]
**🚀 Evolved Concepts**: [[keywords/Quantum-Inspired Learning|Quantum-Inspired Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20105v1 Announce Type: new 
Abstract: Large Language Models (LLMs) often struggle with maintaining coherent multi-step reasoning traces, particularly in tasks that require a structured logical flow. This work introduces a quantum-inspired approach to address the challenge by incorporating a fidelity-based reward derived from Projected Entangled Pair States (PEPS) into Proximal Policy Optimization. Unlike prior approaches that use direct supervision or contrastive objectives, the proposed method guides learning through structural consistency, offering a novel approach to enforce global coherence in generated reasoning traces. The proposed framework is evaluated using multiple coherence-determining metrics on diverse datasets such as GSM8K, StrategyQA, and EntailmentBank spanning arithmetic, intuitive, and entailment-based reasoning. Results show that the proposed quantum-inspired approach offers significant improvements over supervised, contrastive, and pretrained baseline approaches, highlighting the effectiveness of quantum-inspired fidelity as a foundation to improve reasoning trace coherence in LLMs.

## 📝 요약

이 연구는 대형 언어 모델(LLM)이 여러 단계의 추론 과정에서 일관성을 유지하는 데 어려움을 겪는 문제를 해결하기 위해 양자 영감을 받은 접근 방식을 제안합니다. Projected Entangled Pair States(PEPS)에서 파생된 충실도 기반 보상을 Proximal Policy Optimization에 통합하여 구조적 일관성을 통해 학습을 유도합니다. 이 방법은 GSM8K, StrategyQA, EntailmentBank와 같은 다양한 데이터셋에서 평가되었으며, 산술, 직관, 함의 기반 추론에서 기존의 감독 학습 및 대조적 목표보다 뛰어난 성능을 보였습니다. 연구 결과는 양자 영감 충실도가 LLM의 추론 일관성을 개선하는 데 효과적임을 강조합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)은 다단계 추론에서 일관성을 유지하는 데 어려움을 겪는다.
- 2. 본 연구는 양자 영감을 받은 접근 방식을 통해 Projected Entangled Pair States(PEPS)에서 유도된 충실도 기반 보상을 Proximal Policy Optimization에 통합하여 이 문제를 해결한다.
- 3. 제안된 방법은 구조적 일관성을 통해 학습을 유도하며, 생성된 추론 과정의 전반적인 일관성을 강화하는 새로운 접근 방식을 제공한다.
- 4. 다양한 데이터셋(GSM8K, StrategyQA, EntailmentBank)을 사용한 평가 결과, 제안된 양자 영감 접근 방식이 기존의 지도 학습, 대조 목표, 사전 학습된 기준 접근 방식보다 유의미한 개선을 보였다.
- 5. 양자 영감 충실도가 LLM의 추론 과정 일관성을 향상시키는 기초로서 효과적임을 강조한다.


---

*Generated on 2025-09-25 15:19:33*