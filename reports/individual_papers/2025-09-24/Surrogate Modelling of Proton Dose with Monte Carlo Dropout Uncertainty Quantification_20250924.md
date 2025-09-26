<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:04:35.494445",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Monte Carlo Dropout",
    "Neural Network",
    "Predictive Uncertainty",
    "Robust Optimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Monte Carlo Dropout": 0.78,
    "Neural Network": 0.82,
    "Predictive Uncertainty": 0.79,
    "Robust Optimization": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Monte Carlo Dropout",
        "canonical": "Monte Carlo Dropout",
        "aliases": [
          "MC Dropout"
        ],
        "category": "unique_technical",
        "rationale": "Monte Carlo Dropout is a specific technique for uncertainty quantification in neural networks, relevant for linking to uncertainty-aware optimization in machine learning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Neural Surrogate",
        "canonical": "Neural Network",
        "aliases": [
          "Neural Surrogate Model"
        ],
        "category": "broad_technical",
        "rationale": "Neural Surrogate models are a subset of neural networks used for approximating complex functions, linking well with machine learning and optimization tasks.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Voxelwise Predictive Uncertainty",
        "canonical": "Predictive Uncertainty",
        "aliases": [
          "Voxelwise Uncertainty"
        ],
        "category": "specific_connectable",
        "rationale": "Predictive uncertainty is crucial for robust planning and adaptive workflows in medical applications, enhancing connections with uncertainty quantification.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      },
      {
        "surface": "Robust Planning",
        "canonical": "Robust Optimization",
        "aliases": [
          "Robust Planning"
        ],
        "category": "specific_connectable",
        "rationale": "Robust planning is a key application area for optimization under uncertainty, relevant for connecting to broader optimization frameworks.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "adaptive replanning",
      "probabilistic inference"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Monte Carlo Dropout",
      "resolved_canonical": "Monte Carlo Dropout",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Neural Surrogate",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Voxelwise Predictive Uncertainty",
      "resolved_canonical": "Predictive Uncertainty",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Robust Planning",
      "resolved_canonical": "Robust Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Surrogate Modelling of Proton Dose with Monte Carlo Dropout Uncertainty Quantification

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18155.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18155](https://arxiv.org/abs/2509.18155)

## 🔗 유사한 논문
- [[2025-09-23/Comparison of Deterministic and Probabilistic Machine Learning Algorithms for Precise Dimensional Control and Uncertainty Quantification in Additive Manufacturing_20250923|Comparison of Deterministic and Probabilistic Machine Learning Algorithms for Precise Dimensional Control and Uncertainty Quantification in Additive Manufacturing]] (81.2% similar)
- [[2025-09-23/Efficient Neural SDE Training using Wiener-Space Cubature_20250923|Efficient Neural SDE Training using Wiener-Space Cubature]] (80.8% similar)
- [[2025-09-22/Geometric Integration for Neural Control Variates_20250922|Geometric Integration for Neural Control Variates]] (80.7% similar)
- [[2025-09-23/Machine learning-driven conservative-to-primitive conversion in hybrid piecewise polytropic and tabulated equations of state_20250923|Machine learning-driven conservative-to-primitive conversion in hybrid piecewise polytropic and tabulated equations of state]] (80.6% similar)
- [[2025-09-24/Accounting for Uncertainty in Machine Learning Surrogates_ A Gauss-Hermite Quadrature Approach to Reliability Analysis_20250924|Accounting for Uncertainty in Machine Learning Surrogates: A Gauss-Hermite Quadrature Approach to Reliability Analysis]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Predictive Uncertainty|Predictive Uncertainty]], [[keywords/Robust Optimization|Robust Optimization]]
**⚡ Unique Technical**: [[keywords/Monte Carlo Dropout|Monte Carlo Dropout]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18155v1 Announce Type: cross 
Abstract: Accurate proton dose calculation using Monte Carlo (MC) is computationally demanding in workflows like robust optimisation, adaptive replanning, and probabilistic inference, which require repeated evaluations. To address this, we develop a neural surrogate that integrates Monte Carlo dropout to provide fast, differentiable dose predictions along with voxelwise predictive uncertainty. The method is validated through a series of experiments, starting with a one-dimensional analytic benchmark that establishes accuracy, convergence, and variance decomposition. Two-dimensional bone-water phantoms, generated using TOPAS Geant4, demonstrate the method's behavior under domain heterogeneity and beam uncertainty, while a three-dimensional water phantom confirms scalability for volumetric dose prediction. Across these settings, we separate epistemic (model) from parametric (input) contributions, showing that epistemic variance increases under distribution shift, while parametric variance dominates at material boundaries. The approach achieves significant speedups over MC while retaining uncertainty information, making it suitable for integration into robust planning, adaptive workflows, and uncertainty-aware optimisation in proton therapy.

## 📝 요약

이 논문은 몬테카를로(MC) 기반의 양성자 선량 계산의 계산 비용 문제를 해결하기 위해 신경망 대체 모델을 개발했습니다. 이 모델은 몬테카를로 드롭아웃을 통합하여 빠르고 미분 가능한 선량 예측과 함께 각 복셀의 예측 불확실성을 제공합니다. 1차원 분석 벤치마크 실험을 통해 정확성과 수렴성을 검증했으며, 2차원 및 3차원 팬텀 실험을 통해 이 방법이 도메인 이질성과 빔 불확실성 하에서도 효과적임을 확인했습니다. 특히, 분포 변화 시 모델 불확실성이 증가하고, 재료 경계에서는 입력 불확실성이 지배적임을 보여주었습니다. 이 방법은 MC에 비해 계산 속도를 크게 향상시키면서도 불확실성 정보를 유지하여, 양성자 치료의 강건한 계획, 적응적 워크플로우, 불확실성 인식 최적화에 적합합니다.

## 🎯 주요 포인트

- 1. 몬테카를로(MC) 기반의 프로톤 선량 계산은 반복 평가가 필요한 작업에서 계산 비용이 높다.
- 2. 본 연구에서는 몬테카를로 드롭아웃을 통합한 신경망 대체 모델을 개발하여 빠르고 미분 가능한 선량 예측과 예측 불확실성을 제공한다.
- 3. 다양한 실험을 통해 방법의 정확성, 수렴성, 분산 분해를 검증하였으며, 이차원 및 삼차원 팬텀을 통해 도메인 이질성과 빔 불확실성 하에서의 동작을 확인하였다.
- 4. 에피스테믹(모델) 분산과 파라메트릭(입력) 분산을 분리하여 에피스테믹 분산은 분포 변화 시 증가하고, 파라메트릭 분산은 물질 경계에서 지배적임을 보였다.
- 5. 제안된 방법은 MC 대비 속도 향상을 이루면서 불확실성 정보를 유지하여, 프로톤 치료의 강건한 계획, 적응적 워크플로우, 불확실성 인식 최적화에 적합하다.


---

*Generated on 2025-09-24 15:04:35*