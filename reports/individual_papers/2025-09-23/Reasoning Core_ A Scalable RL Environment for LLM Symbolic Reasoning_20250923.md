---
keywords:
  - Large Language Model
  - Reinforcement Learning with Verifiable Rewards
  - Zero-Shot Learning
  - Symbolic Reasoning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.18083
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:05:33.566004",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Reinforcement Learning with Verifiable Rewards",
    "Zero-Shot Learning",
    "Symbolic Reasoning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Reinforcement Learning with Verifiable Rewards": 0.78,
    "Zero-Shot Learning": 0.77,
    "Symbolic Reasoning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's theme, linking to the broader context of language model advancements.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Reinforcement Learning with Verifiable Rewards",
        "canonical": "Reinforcement Learning with Verifiable Rewards",
        "aliases": [
          "RLVR"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel concept specific to the paper, enhancing understanding of its unique contributions.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Zero-Shot Evaluations",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the evaluation method used, connecting to broader zero-shot learning discussions.",
        "novelty_score": 0.4,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "Symbolic Reasoning",
        "canonical": "Symbolic Reasoning",
        "aliases": [
          "Symbolic Logic",
          "Formal Reasoning"
        ],
        "category": "unique_technical",
        "rationale": "Focuses on the paper's core contribution to reasoning capabilities in AI.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "environment",
      "problems",
      "tasks"
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
      "candidate_surface": "Reinforcement Learning with Verifiable Rewards",
      "resolved_canonical": "Reinforcement Learning with Verifiable Rewards",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Zero-Shot Evaluations",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Symbolic Reasoning",
      "resolved_canonical": "Symbolic Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Reasoning Core: A Scalable RL Environment for LLM Symbolic Reasoning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18083.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.18083](https://arxiv.org/abs/2509.18083)

## 🔗 유사한 논문
- [[2025-09-22/DivLogicEval_ A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models_20250922|DivLogicEval: A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models]] (85.3% similar)
- [[2025-09-23/Correlation or Causation_ Analyzing the Causal Structures of LLM and LRM Reasoning Process_20250923|Correlation or Causation: Analyzing the Causal Structures of LLM and LRM Reasoning Process]] (85.0% similar)
- [[2025-09-19/Understanding the Thinking Process of Reasoning Models_ A Perspective from Schoenfeld's Episode Theory_20250919|Understanding the Thinking Process of Reasoning Models: A Perspective from Schoenfeld's Episode Theory]] (85.0% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (84.8% similar)
- [[2025-09-22/Perception-R1_ Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward_20250922|Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward]] (84.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Reinforcement Learning with Verifiable Rewards|Reinforcement Learning with Verifiable Rewards]], [[keywords/Symbolic Reasoning|Symbolic Reasoning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18083v1 Announce Type: new 
Abstract: We introduce Reasoning Core, a new scalable environment for Reinforcement Learning with Verifiable Rewards (RLVR), designed to advance foundational symbolic reasoning in Large Language Models (LLMs). Unlike existing benchmarks that focus on games or isolated puzzles, Reasoning Core procedurally generates problems across core formal domains, including PDDL planning, first-order logic, context-free grammar parsing, causal reasoning, and system equation solving. The environment is built on key design principles of high-generality problem distributions, verification via external tools, and continuous difficulty control, which together provide a virtually infinite supply of novel training instances. Initial zero-shot evaluations with frontier LLMs confirm the difficulty of Reasoning Core's tasks, positioning it as a promising resource to improve the reasoning capabilities of future models.

## 📝 요약

Reasoning Core는 대규모 언어 모델(LLM)의 기초적인 상징적 추론을 발전시키기 위해 설계된 강화 학습 환경입니다. 기존의 게임이나 퍼즐 중심의 벤치마크와 달리, 이 환경은 PDDL 계획, 일차 논리, 문맥 자유 문법 파싱, 인과 추론, 시스템 방정식 해결 등 핵심 형식 영역에서 문제를 절차적으로 생성합니다. 높은 일반성의 문제 분포, 외부 도구를 통한 검증, 난이도 조절을 통해 무한한 훈련 사례를 제공합니다. 초기 평가 결과, Reasoning Core의 과제가 어려움을 확인했으며, 이는 향후 모델의 추론 능력을 향상시키는 유망한 자원이 될 것입니다.

## 🎯 주요 포인트

- 1. Reasoning Core는 대규모 언어 모델의 기초적인 상징적 추론을 발전시키기 위해 설계된 강화 학습 환경입니다.
- 2. 이 환경은 PDDL 계획, 일차 논리, 문맥 자유 문법 파싱, 인과 추론, 시스템 방정식 해결 등 핵심 형식 도메인에서 문제를 절차적으로 생성합니다.
- 3. 높은 일반성의 문제 분포, 외부 도구를 통한 검증, 지속적인 난이도 조절이라는 설계 원칙을 기반으로 무한한 새로운 학습 사례를 제공합니다.
- 4. 초기 제로샷 평가에서 Reasoning Core의 과제가 어려운 것으로 확인되어, 미래 모델의 추론 능력을 향상시키는 유망한 자원으로 자리매김하고 있습니다.


---

*Generated on 2025-09-23 23:05:33*