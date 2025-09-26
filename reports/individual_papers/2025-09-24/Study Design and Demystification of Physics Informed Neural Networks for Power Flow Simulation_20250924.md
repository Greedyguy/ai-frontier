<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:02:28.498259",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Physics-Informed Neural Networks",
    "Power Flow Simulation",
    "Graph Neural Network",
    "Hybrid Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Physics-Informed Neural Networks": 0.88,
    "Power Flow Simulation": 0.8,
    "Graph Neural Network": 0.84,
    "Hybrid Models": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Physics Informed Neural Networks",
        "canonical": "Physics-Informed Neural Networks",
        "aliases": [
          "PINNs"
        ],
        "category": "specific_connectable",
        "rationale": "Physics-Informed Neural Networks are crucial for linking machine learning with physical systems, enhancing model accuracy and compliance.",
        "novelty_score": 0.68,
        "connectivity_score": 0.85,
        "specificity_score": 0.82,
        "link_intent_score": 0.88
      },
      {
        "surface": "Power Flow Simulation",
        "canonical": "Power Flow Simulation",
        "aliases": [
          "Power Flow Analysis"
        ],
        "category": "unique_technical",
        "rationale": "This term is specific to electrical engineering and energy systems, providing a unique link to studies on grid stability.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.79,
        "link_intent_score": 0.8
      },
      {
        "surface": "Graph-Based Networks",
        "canonical": "Graph Neural Network",
        "aliases": [
          "Graph-Based Models"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Neural Networks are essential for modeling complex systems and are directly relevant to the paper's exploration of model architectures.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.76,
        "link_intent_score": 0.84
      },
      {
        "surface": "Hybrid Models",
        "canonical": "Hybrid Models",
        "aliases": [
          "Hybridization Strategies"
        ],
        "category": "broad_technical",
        "rationale": "Hybrid models bridge traditional and machine learning approaches, offering a broad technical link across disciplines.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "energy transition",
      "grid stability",
      "physical compliance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Physics Informed Neural Networks",
      "resolved_canonical": "Physics-Informed Neural Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.85,
        "specificity": 0.82,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Power Flow Simulation",
      "resolved_canonical": "Power Flow Simulation",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.79,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Graph-Based Networks",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.76,
        "link_intent": 0.84
      }
    },
    {
      "candidate_surface": "Hybrid Models",
      "resolved_canonical": "Hybrid Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Study Design and Demystification of Physics Informed Neural Networks for Power Flow Simulation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19233.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.19233](https://arxiv.org/abs/2509.19233)

## 🔗 유사한 논문
- [[2025-09-22/Bayesian Physics Informed Neural Networks for Reliable Transformer Prognostics_20250922|Bayesian Physics Informed Neural Networks for Reliable Transformer Prognostics]] (84.8% similar)
- [[2025-09-18/Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers_20250918|Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers]] (84.1% similar)
- [[2025-09-23/Physics-Informed Operator Learning for Hemodynamic Modeling_20250923|Physics-Informed Operator Learning for Hemodynamic Modeling]] (84.0% similar)
- [[2025-09-23/Machine learning-driven conservative-to-primitive conversion in hybrid piecewise polytropic and tabulated equations of state_20250923|Machine learning-driven conservative-to-primitive conversion in hybrid piecewise polytropic and tabulated equations of state]] (83.6% similar)
- [[2025-09-22/PBPK-iPINNs_ Inverse Physics-Informed Neural Networks for Physiologically Based Pharmacokinetic Brain Models_20250922|PBPK-iPINNs: Inverse Physics-Informed Neural Networks for Physiologically Based Pharmacokinetic Brain Models]] (83.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Hybrid Models|Hybrid Models]]
**🔗 Specific Connectable**: [[keywords/Physics-Informed Neural Networks|Physics-Informed Neural Networks]], [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Power Flow Simulation|Power Flow Simulation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19233v1 Announce Type: new 
Abstract: In the context of the energy transition, with increasing integration of renewable sources and cross-border electricity exchanges, power grids are encountering greater uncertainty and operational risk. Maintaining grid stability under varying conditions is a complex task, and power flow simulators are commonly used to support operators by evaluating potential actions before implementation. However, traditional physical solvers, while accurate, are often too slow for near real-time use. Machine learning models have emerged as fast surrogates, and to improve their adherence to physical laws (e.g., Kirchhoff's laws), they are often trained with embedded constraints which are also known as physics-informed or hybrid models. This paper presents an ablation study to demystify hybridization strategies, ranging from incorporating physical constraints as regularization terms or unsupervised losses, and exploring model architectures from simple multilayer perceptrons to advanced graph-based networks enabling the direct optimization of physics equations. Using our custom benchmarking pipeline for hybrid models called LIPS, we evaluate these models across four dimensions: accuracy, physical compliance, industrial readiness, and out-of-distribution generalization. The results highlight how integrating physical knowledge impacts performance across these criteria. All the implementations are reproducible and provided in the corresponding Github page.

## 📝 요약

이 논문은 에너지 전환 과정에서 재생 가능 에너지원과 국경 간 전력 교환의 증가로 인해 전력망이 직면하는 불확실성과 운영 위험을 다룹니다. 전력 흐름 시뮬레이터는 운영자가 조치를 시행하기 전에 평가하는 데 사용되지만, 전통적인 물리 기반 솔버는 실시간 사용에 비해 속도가 느립니다. 이를 해결하기 위해 물리 법칙을 내재화한 하이브리드 머신러닝 모델이 제안되었습니다. 본 연구는 물리적 제약을 규제 항목이나 비지도 학습 손실로 통합하는 다양한 하이브리드화 전략을 탐구하고, 단순한 다층 퍼셉트론부터 고급 그래프 기반 네트워크까지 다양한 모델 아키텍처를 평가합니다. LIPS라는 맞춤형 벤치마크 파이프라인을 통해 정확성, 물리적 준수, 산업적 준비성, 분포 외 일반화 등 네 가지 차원에서 모델을 평가한 결과, 물리적 지식의 통합이 성능에 미치는 영향을 강조합니다. 모든 구현은 재현 가능하며, 관련 Github 페이지에서 제공됩니다.

## 🎯 주요 포인트

- 1. 에너지 전환과 재생 가능 에너지원의 증가로 전력망의 불확실성과 운영 리스크가 커지고 있다.
- 2. 전통적인 물리적 해석기는 정확하지만 실시간 사용에는 속도가 느리다는 단점이 있다.
- 3. 물리 법칙을 반영한 하이브리드 머신러닝 모델이 전력 흐름 시뮬레이션에서 빠른 대안으로 주목받고 있다.
- 4. 본 논문은 물리적 제약을 정규화 항이나 비지도 학습 손실로 통합하는 하이브리드화 전략을 분석한다.
- 5. LIPS 벤치마킹 파이프라인을 통해 하이브리드 모델의 정확성, 물리적 준수, 산업적 준비성, 분포 외 일반화 능력을 평가한다.


---

*Generated on 2025-09-24 15:02:28*