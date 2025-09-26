<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:46:48.596843",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Distributed Swarm Learning",
    "Multi-Worker Selection",
    "Non-IID Data",
    "Edge IoT"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Distributed Swarm Learning": 0.78,
    "Multi-Worker Selection": 0.77,
    "Non-IID Data": 0.8,
    "Edge IoT": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "distributed swarm learning",
        "canonical": "Distributed Swarm Learning",
        "aliases": [
          "DSL"
        ],
        "category": "unique_technical",
        "rationale": "This is a core concept of the paper, focusing on a novel learning paradigm that is central to the study.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "multi-worker selection",
        "canonical": "Multi-Worker Selection",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The paper introduces a new algorithm based on this concept, which is crucial for understanding the proposed method.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "non-i.i.d. data",
        "canonical": "Non-IID Data",
        "aliases": [
          "non-independent and identically distributed data"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding data heterogeneity is vital for the paper's context, linking to broader discussions on data distribution challenges.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "edge Internet of Things",
        "canonical": "Edge IoT",
        "aliases": [
          "Edge Internet of Things"
        ],
        "category": "broad_technical",
        "rationale": "This is a fundamental application domain for the discussed technologies, providing context for the paper's contributions.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "model scalability",
      "communication efficiency"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "distributed swarm learning",
      "resolved_canonical": "Distributed Swarm Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "multi-worker selection",
      "resolved_canonical": "Multi-Worker Selection",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "non-i.i.d. data",
      "resolved_canonical": "Non-IID Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "edge Internet of Things",
      "resolved_canonical": "Edge IoT",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Multi-Worker Selection based Distributed Swarm Learning for Edge IoT with Non-i.i.d. Data

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18367.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18367](https://arxiv.org/abs/2509.18367)

## 🔗 유사한 논문
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (80.6% similar)
- [[2025-09-19/Hierarchical Federated Learning for Social Network with Mobility_20250919|Hierarchical Federated Learning for Social Network with Mobility]] (80.3% similar)
- [[2025-09-23/(DEMO) Deep Reinforcement Learning Based Resource Allocation in Distributed IoT Systems_20250923|(DEMO) Deep Reinforcement Learning Based Resource Allocation in Distributed IoT Systems]] (80.3% similar)
- [[2025-09-23/LASER_ Stratified Selective Sampling for Instruction Tuning with Dedicated Scoring Strategy_20250923|LASER: Stratified Selective Sampling for Instruction Tuning with Dedicated Scoring Strategy]] (80.0% similar)
- [[2025-09-22/A method for improving multilingual quality and diversity of instruction fine-tuning datasets_20250922|A method for improving multilingual quality and diversity of instruction fine-tuning datasets]] (79.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Edge IoT|Edge IoT]]
**🔗 Specific Connectable**: [[keywords/Non-IID Data|Non-IID Data]]
**⚡ Unique Technical**: [[keywords/Distributed Swarm Learning|Distributed Swarm Learning]], [[keywords/Multi-Worker Selection|Multi-Worker Selection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18367v1 Announce Type: cross 
Abstract: Recent advances in distributed swarm learning (DSL) offer a promising paradigm for edge Internet of Things. Such advancements enhance data privacy, communication efficiency, energy saving, and model scalability. However, the presence of non-independent and identically distributed (non-i.i.d.) data pose a significant challenge for multi-access edge computing, degrading learning performance and diverging training behavior of vanilla DSL. Further, there still lacks theoretical guidance on how data heterogeneity affects model training accuracy, which requires thorough investigation. To fill the gap, this paper first study the data heterogeneity by measuring the impact of non-i.i.d. datasets under the DSL framework. This then motivates a new multi-worker selection design for DSL, termed M-DSL algorithm, which works effectively with distributed heterogeneous data. A new non-i.i.d. degree metric is introduced and defined in this work to formulate the statistical difference among local datasets, which builds a connection between the measure of data heterogeneity and the evaluation of DSL performance. In this way, our M-DSL guides effective selection of multiple works who make prominent contributions for global model updates. We also provide theoretical analysis on the convergence behavior of our M-DSL, followed by extensive experiments on different heterogeneous datasets and non-i.i.d. data settings. Numerical results verify performance improvement and network intelligence enhancement provided by our M-DSL beyond the benchmarks.

## 📝 요약

이 논문은 분산 스웜 학습(DSL)에서 비독립적이고 동일하게 분포되지 않은(non-i.i.d.) 데이터가 학습 성능을 저하시킨다는 문제를 다룹니다. 이를 해결하기 위해 새로운 M-DSL 알고리즘을 제안하며, 이는 분산된 이질적 데이터와 효과적으로 작동합니다. 논문에서는 비동질성 정도를 측정하는 새로운 지표를 도입하여 데이터 이질성과 DSL 성능 간의 관계를 규명합니다. M-DSL은 글로벌 모델 업데이트에 기여할 수 있는 작업자를 효과적으로 선택하도록 설계되었습니다. 이론적 수렴 분석과 다양한 실험을 통해 M-DSL의 성능 향상과 네트워크 지능 강화가 검증되었습니다.

## 🎯 주요 포인트

- 1. 분산 스웜 학습(DSL)은 데이터 프라이버시, 통신 효율성, 에너지 절약 및 모델 확장성을 향상시키는 유망한 패러다임을 제공합니다.
- 2. 비독립적이고 동일하게 분포되지 않은(non-i.i.d.) 데이터는 DSL의 학습 성능을 저하시킵니다.
- 3. 본 논문은 DSL 프레임워크에서 non-i.i.d. 데이터셋의 영향을 측정하여 데이터 이질성을 연구합니다.
- 4. M-DSL 알고리즘은 분산된 이질적 데이터와 효과적으로 작동하며, 글로벌 모델 업데이트에 기여하는 작업자를 효과적으로 선택합니다.
- 5. M-DSL의 수렴 행동에 대한 이론적 분석과 다양한 실험을 통해 성능 개선과 네트워크 지능 향상을 검증합니다.


---

*Generated on 2025-09-24 13:46:48*