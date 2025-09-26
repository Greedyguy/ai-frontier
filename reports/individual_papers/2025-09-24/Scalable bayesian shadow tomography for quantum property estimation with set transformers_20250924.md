<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:11:32.595320",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Learning",
    "Quantum State Estimation",
    "Classical Shadows Protocol",
    "Transformer"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Learning": 0.78,
    "Quantum State Estimation": 0.8,
    "Classical Shadows Protocol": 0.82,
    "Transformer": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Bayesian machine learning",
        "canonical": "Machine Learning",
        "aliases": [
          "Bayesian ML"
        ],
        "category": "broad_technical",
        "rationale": "Connects to existing machine learning frameworks and techniques.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "quantum state estimation",
        "canonical": "Quantum State Estimation",
        "aliases": [
          "quantum estimation"
        ],
        "category": "unique_technical",
        "rationale": "Focuses on a specific application within quantum computing, enhancing domain-specific connections.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "classical shadows protocol",
        "canonical": "Classical Shadows Protocol",
        "aliases": [
          "classical shadows"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel method for quantum property estimation, relevant for cutting-edge research.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "set transformer architecture",
        "canonical": "Transformer",
        "aliases": [
          "set transformer"
        ],
        "category": "specific_connectable",
        "rationale": "Links to the broader transformer architecture, a key concept in modern machine learning.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "scalable",
      "estimator",
      "measurement outcomes",
      "baseline estimator"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Bayesian machine learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "quantum state estimation",
      "resolved_canonical": "Quantum State Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "classical shadows protocol",
      "resolved_canonical": "Classical Shadows Protocol",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "set transformer architecture",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Scalable bayesian shadow tomography for quantum property estimation with set transformers

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18674.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18674](https://arxiv.org/abs/2509.18674)

## 🔗 유사한 논문
- [[2025-09-23/Information Fusion Using Transferable Belief Functions Implemented on Quantum Circuits_20250923|Information Fusion Using Transferable Belief Functions Implemented on Quantum Circuits]] (83.2% similar)
- [[2025-09-23/Addressing the Inconsistency in Bayesian Deep Learning via Generalized Laplace Approximation_20250923|Addressing the Inconsistency in Bayesian Deep Learning via Generalized Laplace Approximation]] (82.3% similar)
- [[2025-09-17/Deconstructing Intraocular Pressure_ A Non-invasive Multi-Stage Probabilistic Inverse Framework_20250917|Deconstructing Intraocular Pressure: A Non-invasive Multi-Stage Probabilistic Inverse Framework]] (80.9% similar)
- [[2025-09-22/Gradient-Free Sequential Bayesian Experimental Design via Interacting Particle Systems_20250922|Gradient-Free Sequential Bayesian Experimental Design via Interacting Particle Systems]] (80.5% similar)
- [[2025-09-22/Bayesian Physics Informed Neural Networks for Reliable Transformer Prognostics_20250922|Bayesian Physics Informed Neural Networks for Reliable Transformer Prognostics]] (80.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**🔗 Specific Connectable**: [[keywords/Transformer|Transformer]]
**⚡ Unique Technical**: [[keywords/Quantum State Estimation|Quantum State Estimation]], [[keywords/Classical Shadows Protocol|Classical Shadows Protocol]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18674v1 Announce Type: cross 
Abstract: A scalable Bayesian machine learning framework is introduced for estimating scalar properties of an unknown quantum state from measurement data, which bypasses full density matrix reconstruction. This work is the first to integrate the classical shadows protocol with a permutation-invariant set transformer architecture, enabling the approach to predict and correct bias in existing estimators to approximate the true Bayesian posterior mean. Measurement outcomes are encoded as fixed-dimensional feature vectors, and the network outputs a residual correction to a baseline estimator. Scalability to large quantum systems is ensured by the polynomial dependence of input size on system size and number of measurements. On Greenberger-Horne-Zeilinger state fidelity and second-order R\'enyi entropy estimation tasks -- using random Pauli and random Clifford measurements -- this Bayesian estimator always achieves lower mean squared error than classical shadows alone, with more than a 99\% reduction in the few copy regime.

## 📝 요약

이 논문은 측정 데이터를 통해 미지의 양자 상태의 스칼라 속성을 추정하는 확장 가능한 베이지안 머신러닝 프레임워크를 제안합니다. 이 접근법은 밀도 행렬의 완전한 재구성을 우회하며, 클래식 섀도우 프로토콜과 순열 불변 집합 변환기 아키텍처를 통합하여 기존 추정기의 편향을 예측하고 수정하여 진정한 베이지안 사후 평균을 근사합니다. 측정 결과는 고정 차원의 특징 벡터로 인코딩되며, 네트워크는 기본 추정기에 대한 잔차 보정을 출력합니다. 이 방법은 시스템 크기와 측정 수에 대한 입력 크기의 다항식 의존성으로 인해 대규모 양자 시스템으로의 확장이 가능합니다. Greenberger-Horne-Zeilinger 상태 충실도와 2차 R\'enyi 엔트로피 추정 작업에서, 이 베이지안 추정기는 소수 복사 체제에서 99% 이상의 평균 제곱 오차 감소를 달성하며, 클래식 섀도우만 사용하는 경우보다 항상 더 낮은 평균 제곱 오차를 보입니다.

## 🎯 주요 포인트

- 1. 측정 데이터로부터 미지의 양자 상태의 스칼라 속성을 추정하기 위한 확장 가능한 베이지안 머신러닝 프레임워크가 도입되었습니다.
- 2. 이 연구는 고전적 그림자 프로토콜과 순열 불변 집합 변환기 아키텍처를 통합하여 기존 추정기의 편향을 예측하고 수정하는 접근 방식을 제시합니다.
- 3. 입력 크기가 시스템 크기와 측정 수에 대해 다항식적으로 의존하여 대규모 양자 시스템에 대한 확장성을 보장합니다.
- 4. 그린버거-호른-자일링거 상태 충실도 및 2차 레니 엔트로피 추정 작업에서, 이 베이지안 추정기는 고전적 그림자만을 사용할 때보다 항상 더 낮은 평균 제곱 오차를 달성합니다.
- 5. 특히 적은 복사본 체제에서 99% 이상의 오차 감소를 보여줍니다.


---

*Generated on 2025-09-24 15:11:32*