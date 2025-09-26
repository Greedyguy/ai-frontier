<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:52:56.552548",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Kolmogorov Arnold Networks",
    "Ehrenfest Theorems",
    "Physics-Informed Learning",
    "Chain of Kolmogorov Arnold Networks"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Kolmogorov Arnold Networks": 0.85,
    "Ehrenfest Theorems": 0.8,
    "Physics-Informed Learning": 0.78,
    "Chain of Kolmogorov Arnold Networks": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Kolmogorov Arnold Networks",
        "canonical": "Kolmogorov Arnold Networks",
        "aliases": [
          "KANs"
        ],
        "category": "unique_technical",
        "rationale": "This novel neural architecture is central to the paper's contribution and offers a new approach to quantum dynamics modeling.",
        "novelty_score": 0.95,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Ehrenfest constraints",
        "canonical": "Ehrenfest Theorems",
        "aliases": [
          "Ehrenfest constraints"
        ],
        "category": "specific_connectable",
        "rationale": "The use of Ehrenfest theorems as constraints is a key aspect of the model's physics-informed approach.",
        "novelty_score": 0.7,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "physics-informed loss functions",
        "canonical": "Physics-Informed Learning",
        "aliases": [
          "physics-informed loss"
        ],
        "category": "evolved_concepts",
        "rationale": "This concept bridges physics and machine learning, enhancing model interpretability and accuracy.",
        "novelty_score": 0.68,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "Chain of KANs",
        "canonical": "Chain of Kolmogorov Arnold Networks",
        "aliases": [
          "Chain of KANs"
        ],
        "category": "unique_technical",
        "rationale": "This architecture embeds temporal causality, making it a unique contribution to time series modeling.",
        "novelty_score": 0.92,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "time series",
      "quantum systems",
      "neural architectures"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Kolmogorov Arnold Networks",
      "resolved_canonical": "Kolmogorov Arnold Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Ehrenfest constraints",
      "resolved_canonical": "Ehrenfest Theorems",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "physics-informed loss functions",
      "resolved_canonical": "Physics-Informed Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Chain of KANs",
      "resolved_canonical": "Chain of Kolmogorov Arnold Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Physics-informed time series analysis with Kolmogorov-Arnold Networks under Ehrenfest constraints

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18483.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18483](https://arxiv.org/abs/2509.18483)

## 🔗 유사한 논문
- [[2025-09-23/Interpretable Clinical Classification with Kolgomorov-Arnold Networks_20250923|Interpretable Clinical Classification with Kolgomorov-Arnold Networks]] (84.2% similar)
- [[2025-09-17/Quantum Variational Activation Functions Empower Kolmogorov-Arnold Networks_20250917|Quantum Variational Activation Functions Empower Kolmogorov-Arnold Networks]] (82.2% similar)
- [[2025-09-23/KANO_ Kolmogorov-Arnold Neural Operator_20250923|KANO: Kolmogorov-Arnold Neural Operator]] (81.7% similar)
- [[2025-09-23/Full-History Graphs with Edge-Type Decoupled Networks for Temporal Reasoning_20250923|Full-History Graphs with Edge-Type Decoupled Networks for Temporal Reasoning]] (80.9% similar)
- [[2025-09-23/Comprehensive Review of Neural Differential Equations for Time Series Analysis_20250923|Comprehensive Review of Neural Differential Equations for Time Series Analysis]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Ehrenfest Theorems|Ehrenfest Theorems]]
**⚡ Unique Technical**: [[keywords/Kolmogorov Arnold Networks|Kolmogorov Arnold Networks]], [[keywords/Chain of Kolmogorov Arnold Networks|Chain of Kolmogorov Arnold Networks]]
**🚀 Evolved Concepts**: [[keywords/Physics-Informed Learning|Physics-Informed Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18483v1 Announce Type: new 
Abstract: The prediction of quantum dynamical responses lies at the heart of modern physics. Yet, modeling these time-dependent behaviors remains a formidable challenge because quantum systems evolve in high-dimensional Hilbert spaces, often rendering traditional numerical methods computationally prohibitive. While large language models have achieved remarkable success in sequential prediction, quantum dynamics presents a fundamentally different challenge: forecasting the entire temporal evolution of quantum systems rather than merely the next element in a sequence. Existing neural architectures such as recurrent and convolutional networks often require vast training datasets and suffer from spurious oscillations that compromise physical interpretability. In this work, we introduce a fundamentally new approach: Kolmogorov Arnold Networks (KANs) augmented with physics-informed loss functions that enforce the Ehrenfest theorems. Our method achieves superior accuracy with significantly less training data: it requires only 5.4 percent of the samples (200) compared to Temporal Convolution Networks (3,700). We further introduce the Chain of KANs, a novel architecture that embeds temporal causality directly into the model design, making it particularly well-suited for time series modeling. Our results demonstrate that physics-informed KANs offer a compelling advantage over conventional black-box models, maintaining both mathematical rigor and physical consistency while dramatically reducing data requirements.

## 📝 요약

이 논문은 양자 역학적 동적 반응 예측의 어려움을 해결하기 위해 Kolmogorov Arnold Networks(KANs)를 제안합니다. 기존의 신경망 구조는 많은 데이터가 필요하고 물리적 해석을 저해하는 문제를 겪습니다. KANs는 Ehrenfest 정리를 반영한 물리 기반 손실 함수를 도입하여, 기존 방법보다 적은 데이터(5.4%에 해당하는 200개의 샘플)로도 높은 정확도를 달성합니다. 또한, 시간적 인과성을 모델 설계에 직접 포함한 'Chain of KANs' 구조를 제안하여 시계열 모델링에 적합함을 보입니다. 이 연구는 수학적 엄밀성과 물리적 일관성을 유지하면서 데이터 요구량을 크게 줄이는 데 기여합니다.

## 🎯 주요 포인트

- 1. 양자 역학적 동적 반응의 예측은 현대 물리학의 핵심 과제이다.
- 2. 전통적인 수치 해법은 양자 시스템의 고차원 힐베르트 공간에서의 진화로 인해 계산적으로 부담이 크다.
- 3. Kolmogorov Arnold Networks (KANs)를 물리학적 손실 함수와 결합하여 에렌페스트 정리를 적용한 새로운 접근법을 제안한다.
- 4. 제안된 방법은 Temporal Convolution Networks보다 훨씬 적은 데이터(5.4%의 샘플)로 높은 정확도를 달성한다.
- 5. KANs의 체인 구조는 시간적 인과성을 모델 설계에 직접적으로 내장하여 시계열 모델링에 적합하다.


---

*Generated on 2025-09-24 14:52:56*