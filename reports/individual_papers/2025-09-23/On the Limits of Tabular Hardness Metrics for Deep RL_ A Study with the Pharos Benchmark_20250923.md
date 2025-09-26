---
keywords:
  - Deep Learning
  - Representation Hardness
  - Pharos Benchmark
  - Tabular Hardness Metrics
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17092
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:46:53.979362",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Representation Hardness",
    "Pharos Benchmark",
    "Tabular Hardness Metrics"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Representation Hardness": 0.78,
    "Pharos Benchmark": 0.82,
    "Tabular Hardness Metrics": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "deep reinforcement learning",
        "canonical": "Deep Learning",
        "aliases": [
          "deep RL"
        ],
        "category": "broad_technical",
        "rationale": "Deep reinforcement learning is a subfield of deep learning, providing a strong link to broader technical discussions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "representation hardness",
        "canonical": "Representation Hardness",
        "aliases": [
          "representation difficulty"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's argument about the limitations of tabular metrics in non-tabular settings.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Pharos Benchmark",
        "canonical": "Pharos Benchmark",
        "aliases": [
          "pharos"
        ],
        "category": "unique_technical",
        "rationale": "Pharos Benchmark is a newly introduced tool, crucial for linking discussions on principled RL benchmarking.",
        "novelty_score": 0.8,
        "connectivity_score": 0.55,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "tabular hardness metrics",
        "canonical": "Tabular Hardness Metrics",
        "aliases": [
          "tabular metrics"
        ],
        "category": "unique_technical",
        "rationale": "These metrics are a key point of comparison in the paper, highlighting their limitations in deep RL contexts.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "MDP diameter",
      "suboptimality gaps"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "deep reinforcement learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "representation hardness",
      "resolved_canonical": "Representation Hardness",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Pharos Benchmark",
      "resolved_canonical": "Pharos Benchmark",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.55,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "tabular hardness metrics",
      "resolved_canonical": "Tabular Hardness Metrics",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# On the Limits of Tabular Hardness Metrics for Deep RL: A Study with the Pharos Benchmark

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17092.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17092](https://arxiv.org/abs/2509.17092)

## 🔗 유사한 논문
- [[2025-09-23/Synthetic POMDPs to Challenge Memory-Augmented RL_ Memory Demand Structure Modeling_20250923|Synthetic POMDPs to Challenge Memory-Augmented RL: Memory Demand Structure Modeling]] (81.5% similar)
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (81.3% similar)
- [[2025-09-22/Enhancing Interpretability in Deep Reinforcement Learning through Semantic Clustering_20250922|Enhancing Interpretability in Deep Reinforcement Learning through Semantic Clustering]] (80.9% similar)
- [[2025-09-23/Reasoning Core_ A Scalable RL Environment for LLM Symbolic Reasoning_20250923|Reasoning Core: A Scalable RL Environment for LLM Symbolic Reasoning]] (80.8% similar)
- [[2025-09-22/Perception-R1_ Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward_20250922|Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward]] (80.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**⚡ Unique Technical**: [[keywords/Representation Hardness|Representation Hardness]], [[keywords/Pharos Benchmark|Pharos Benchmark]], [[keywords/Tabular Hardness Metrics|Tabular Hardness Metrics]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17092v1 Announce Type: new 
Abstract: Principled evaluation is critical for progress in deep reinforcement learning (RL), yet it lags behind the theory-driven benchmarks of tabular RL. While tabular settings benefit from well-understood hardness measures like MDP diameter and suboptimality gaps, deep RL benchmarks are often chosen based on intuition and popularity. This raises a critical question: can tabular hardness metrics be adapted to guide non-tabular benchmarking? We investigate this question and reveal a fundamental gap. Our primary contribution is demonstrating that the difficulty of non-tabular environments is dominated by a factor that tabular metrics ignore: representation hardness. The same underlying MDP can pose vastly different challenges depending on whether the agent receives state vectors or pixel-based observations. To enable this analysis, we introduce \texttt{pharos}, a new open-source library for principled RL benchmarking that allows for systematic control over both environment structure and agent representations. Our extensive case study using \texttt{pharos} shows that while tabular metrics offer some insight, they are poor predictors of deep RL agent performance on their own. This work highlights the urgent need for new, representation-aware hardness measures and positions \texttt{pharos} as a key tool for developing them.

## 📝 요약

이 논문은 심층 강화 학습(RL)의 평가 기준이 이론 중심의 표 형식 RL 벤치마크에 비해 뒤처져 있다는 문제를 다룹니다. 표 형식의 난이도 측정 기준은 MDP 직경과 비최적성 간격과 같은 잘 이해된 지표를 사용하지만, 심층 RL 벤치마크는 직관과 인기에 의해 선택됩니다. 저자들은 표 형식의 난이도 측정 기준이 비표 형식 환경의 난이도를 충분히 설명하지 못하며, 특히 표현의 난이도가 중요한 요소임을 발견했습니다. 이를 분석하기 위해 \texttt{pharos}라는 새로운 오픈 소스 라이브러리를 소개하여 환경 구조와 에이전트 표현을 체계적으로 제어할 수 있게 했습니다. 연구 결과, 표 형식 지표는 일부 통찰력을 제공하지만 심층 RL 에이전트 성능을 예측하는 데 한계가 있음을 보여주었습니다. 이 연구는 표현을 고려한 새로운 난이도 측정 기준의 필요성을 강조하며, \texttt{pharos}가 이를 개발하는 데 중요한 도구가 될 것임을 제시합니다.

## 🎯 주요 포인트

- 1. 심층 강화 학습의 평가 기준은 이론 기반의 표 형식 RL 벤치마크에 비해 뒤처져 있다.
- 2. 비표 형식 환경의 난이도는 표현의 어려움에 의해 크게 좌우된다.
- 3. 동일한 MDP도 상태 벡터나 픽셀 기반 관측에 따라 매우 다른 도전 과제를 제시할 수 있다.
- 4. 새로운 오픈 소스 라이브러리 \texttt{pharos}는 환경 구조와 에이전트 표현을 체계적으로 제어할 수 있는 RL 벤치마킹 도구이다.
- 5. 새로운 표현 인식 난이도 측정이 필요하며, \texttt{pharos}는 이를 개발하는 데 중요한 도구로 자리매김한다.


---

*Generated on 2025-09-24 01:46:53*