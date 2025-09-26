---
keywords:
  - Deep Learning
  - Symbolic Dependence Graph
  - Temporal Dimensions
  - Recurrent Tensors
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2501.05408
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:42:52.799262",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Symbolic Dependence Graph",
    "Temporal Dimensions",
    "Recurrent Tensors"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Symbolic Dependence Graph": 0.8,
    "Temporal Dimensions": 0.78,
    "Recurrent Tensors": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [
          "DL"
        ],
        "category": "broad_technical",
        "rationale": "Deep Learning is a foundational concept that connects various aspects of the paper's methodology.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "symbolic dependence graph",
        "canonical": "Symbolic Dependence Graph",
        "aliases": [
          "SDG"
        ],
        "category": "unique_technical",
        "rationale": "The symbolic dependence graph is a unique technical concept introduced in the paper that underpins its novel approach.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "temporal dimensions",
        "canonical": "Temporal Dimensions",
        "aliases": [
          "time dimensions"
        ],
        "category": "specific_connectable",
        "rationale": "Temporal dimensions are crucial for understanding dynamic dependencies in the proposed system.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "recurrent tensors",
        "canonical": "Recurrent Tensors",
        "aliases": [
          "recurrent tensor structures"
        ],
        "category": "unique_technical",
        "rationale": "Recurrent tensors are a novel concept in the paper that enable dynamic execution.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "eager execution",
      "graph-based systems",
      "whole-program optimizations"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "symbolic dependence graph",
      "resolved_canonical": "Symbolic Dependence Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "temporal dimensions",
      "resolved_canonical": "Temporal Dimensions",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "recurrent tensors",
      "resolved_canonical": "Recurrent Tensors",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Tempo: Compiled Dynamic Deep Learning with Symbolic Dependence Graphs

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2501.05408.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2501.05408](https://arxiv.org/abs/2501.05408)

## 🔗 유사한 논문
- [[2025-09-19/(P)rior(D)yna(F)low_ A Priori Dynamic Workflow Construction via Multi-Agent Collaboration_20250919|(P)rior(D)yna(F)low: A Priori Dynamic Workflow Construction via Multi-Agent Collaboration]] (79.6% similar)
- [[2025-09-22/DebFlow_ Automating Agent Creation via Agent Debate_20250922|DebFlow: Automating Agent Creation via Agent Debate]] (79.6% similar)
- [[2025-09-22/ChronoForge-RL_ Chronological Forging through Reinforcement Learning for Enhanced Video Understanding_20250922|ChronoForge-RL: Chronological Forging through Reinforcement Learning for Enhanced Video Understanding]] (79.4% similar)
- [[2025-09-23/LightCode_ Compiling LLM Inference for Photonic-Electronic Systems_20250923|LightCode: Compiling LLM Inference for Photonic-Electronic Systems]] (79.1% similar)
- [[2025-09-23/Adaptive Overclocking_ Dynamic Control of Thinking Path Length via Real-Time Reasoning Signals_20250923|Adaptive Overclocking: Dynamic Control of Thinking Path Length via Real-Time Reasoning Signals]] (78.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Temporal Dimensions|Temporal Dimensions]]
**⚡ Unique Technical**: [[keywords/Symbolic Dependence Graph|Symbolic Dependence Graph]], [[keywords/Recurrent Tensors|Recurrent Tensors]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.05408v2 Announce Type: replace-cross 
Abstract: Deep learning (DL) algorithms are often defined in terms of \emph{temporal relationships}: a tensor at one timestep may depend on tensors from earlier or later timesteps. Such \emph{dynamic} dependencies (and corresponding dynamic tensor shapes) are difficult to express and optimize: while \emph{eager} DL systems support such dynamism, they cannot apply compiler-based optimizations; \emph{graph-based} systems require static tensor shapes, which forces users to pad tensors or break-up programs into multiple static graphs.
  We describe Tempo, a new DL system that combines the dynamism of eager execution with the whole-program optimizations of graph-based compilation. Tempo achieves this through a declarative programming model with \emph{recurrent tensors}, which include explicit \emph{temporal dimensions}. Temporal dimensions can be indexed using \emph{symbolic expressions} to express dynamic dependencies on past and future tensors. Based on this, Tempo constructs a \emph{symbolic dependence graph}, which concisely encodes dynamic dependencies between operators, and applies whole-program optimizations, such as algebraic simplifications, vectorization, tiling, and fusion. By tiling dynamic dependencies into static-size blocks, Tempo can also reuse existing static code-generators. It then uses a polyhedral model to find a feasible execution schedule, which includes memory management operations. We show that Tempo achieves a 7$\times$ speedup over JAX for Llama-3.2-3B decoding; for reinforcement learning algorithms, Tempo achieves a 54$\times$ speedup, with 16$\times$ lower peak memory usage.

## 📝 요약

Tempo는 딥러닝 시스템으로, 즉시 실행의 유연성과 그래프 기반 컴파일의 최적화를 결합합니다. 이는 명령형 프로그래밍 모델과 명시적 시간 차원을 포함하는 재귀 텐서를 통해 구현됩니다. Tempo는 동적 의존성을 상징적 표현으로 나타내어, 연산자 간의 의존성을 효율적으로 인코딩하고, 전역 최적화를 수행합니다. 이를 통해 Tempo는 기존의 정적 코드 생성기를 재활용하며, 메모리 관리 등을 포함한 실행 일정을 최적화합니다. 실험 결과, Tempo는 JAX 대비 Llama-3.2-3B 디코딩에서 7배, 강화 학습 알고리즘에서 54배의 속도 향상과 16배의 메모리 사용 감소를 달성했습니다.

## 🎯 주요 포인트

- 1. Tempo는 동적 실행의 유연성과 그래프 기반 컴파일의 전체 프로그램 최적화를 결합한 새로운 딥러닝 시스템입니다.
- 2. Tempo는 명시적인 시간 차원을 포함한 재귀 텐서를 사용하여 동적 의존성을 표현하고 최적화합니다.
- 3. Tempo는 연산자 간의 동적 의존성을 간결하게 인코딩하는 상징적 의존 그래프를 구축하고, 전역 프로그램 최적화를 수행합니다.
- 4. Tempo는 동적 의존성을 정적 크기의 블록으로 타일링하여 기존의 정적 코드 생성기를 재사용할 수 있습니다.
- 5. Tempo는 Llama-3.2-3B 디코딩에서 JAX 대비 7배, 강화 학습 알고리즘에서 54배의 속도 향상과 16배 낮은 메모리 사용량을 달성했습니다.


---

*Generated on 2025-09-24 00:42:52*