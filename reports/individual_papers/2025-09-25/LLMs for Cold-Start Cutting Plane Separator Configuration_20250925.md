---
keywords:
  - Large Language Model
  - Mixed Integer Linear Programming
  - Cutting Plane Separator
  - Ensembling Strategy
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2412.12038
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T17:05:24.807300",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Mixed Integer Linear Programming",
    "Cutting Plane Separator",
    "Ensembling Strategy"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Mixed Integer Linear Programming": 0.8,
    "Cutting Plane Separator": 0.78,
    "Ensembling Strategy": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the proposed framework and connect to existing research on language models.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Mixed Integer Linear Programming",
        "canonical": "Mixed Integer Linear Programming",
        "aliases": [
          "MILP"
        ],
        "category": "unique_technical",
        "rationale": "MILP is a specific problem domain that the paper addresses, providing a unique connection point for optimization research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Cutting Plane Separator",
        "canonical": "Cutting Plane Separator",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a specific technique within MILP that the paper focuses on, offering a precise link to optimization methods.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Ensembling Strategy",
        "canonical": "Ensembling Strategy",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Ensembling strategies are widely used in machine learning, providing a connection to broader ML techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "solver",
      "configuration",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Mixed Integer Linear Programming",
      "resolved_canonical": "Mixed Integer Linear Programming",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Cutting Plane Separator",
      "resolved_canonical": "Cutting Plane Separator",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Ensembling Strategy",
      "resolved_canonical": "Ensembling Strategy",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# LLMs for Cold-Start Cutting Plane Separator Configuration

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2412.12038.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2412.12038](https://arxiv.org/abs/2412.12038)

## 🔗 유사한 논문
- [[2025-09-24/Prompting for Performance_ Exploring LLMs for Configuring Software_20250924|Prompting for Performance: Exploring LLMs for Configuring Software]] (85.5% similar)
- [[2025-09-23/Large Language Models as End-to-end Combinatorial Optimization Solvers_20250923|Large Language Models as End-to-end Combinatorial Optimization Solvers]] (83.3% similar)
- [[2025-09-22/Not All Parameters Are Created Equal_ Smart Isolation Boosts Fine-Tuning Performance_20250922|Not All Parameters Are Created Equal: Smart Isolation Boosts Fine-Tuning Performance]] (83.2% similar)
- [[2025-09-23/LASER_ Stratified Selective Sampling for Instruction Tuning with Dedicated Scoring Strategy_20250923|LASER: Stratified Selective Sampling for Instruction Tuning with Dedicated Scoring Strategy]] (82.7% similar)
- [[2025-09-22/Are LLMs Better Formalizers than Solvers on Complex Problems?_20250922|Are LLMs Better Formalizers than Solvers on Complex Problems?]] (82.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Ensembling Strategy|Ensembling Strategy]]
**⚡ Unique Technical**: [[keywords/Mixed Integer Linear Programming|Mixed Integer Linear Programming]], [[keywords/Cutting Plane Separator|Cutting Plane Separator]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2412.12038v2 Announce Type: replace 
Abstract: Mixed integer linear programming (MILP) solvers expose hundreds of parameters that have an outsized impact on performance but are difficult to configure for all but expert users. Existing machine learning (ML) approaches require training on thousands of related instances, generalize poorly and can be difficult to integrate into existing solver workflows. We propose a large language model (LLM)-based framework that configures cutting plane separators using problem descriptions and solver-specific separator summaries. To reduce variance in LLM outputs, we introduce an ensembling strategy that clusters and aggregates candidate configurations into a small portfolio of high-performing configurations. Our method requires no custom solver interface, generates configurations in seconds via simple API calls, and requires solving only a small number of instances. Extensive experiments on standard synthetic and real-world MILPs show our approach matches or outperforms state-of-the-art configuration methods with a fraction of the data and computation.

## 📝 요약

이 논문은 혼합 정수 선형 계획법(MILP) 해결기의 성능에 큰 영향을 미치는 매개변수 설정 문제를 해결하기 위해 대형 언어 모델(LLM) 기반 프레임워크를 제안합니다. 기존의 기계 학습 접근법은 많은 데이터가 필요하고 일반화가 어려운 반면, 제안된 방법은 문제 설명과 해결기별 요약을 활용하여 빠르게 설정을 생성합니다. 또한, 출력의 변동성을 줄이기 위해 후보 설정을 클러스터링하고 집계하는 방법을 도입하여 소수의 고성능 설정 포트폴리오를 만듭니다. 이 방법은 간단한 API 호출로 몇 초 만에 설정을 생성하며, 소수의 사례만 해결하면 됩니다. 실험 결과, 제안된 방법은 적은 데이터와 계산으로도 최신 설정 방법과 동등하거나 더 나은 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 혼합 정수 선형 계획법(MILP) 솔버의 성능에 큰 영향을 미치는 수백 개의 매개변수를 효과적으로 구성하기 위해 대형 언어 모델(LLM) 기반 프레임워크를 제안합니다.
- 2. 제안된 방법은 문제 설명과 솔버별 절단 평면 분리기 요약을 사용하여 절단 평면 분리기를 구성합니다.
- 3. LLM 출력의 변동성을 줄이기 위해 후보 구성들을 클러스터링하고 집계하여 고성능 구성의 작은 포트폴리오를 생성하는 앙상블 전략을 도입했습니다.
- 4. 이 방법은 맞춤형 솔버 인터페이스가 필요 없으며, 간단한 API 호출로 몇 초 만에 구성을 생성하고, 적은 수의 인스턴스만 해결하면 됩니다.
- 5. 표준 합성 및 실제 MILP에 대한 광범위한 실험에서 제안된 방법은 데이터와 계산의 일부만 사용하여 최첨단 구성 방법과 동등하거나 더 나은 성능을 보였습니다.


---

*Generated on 2025-09-25 17:05:24*