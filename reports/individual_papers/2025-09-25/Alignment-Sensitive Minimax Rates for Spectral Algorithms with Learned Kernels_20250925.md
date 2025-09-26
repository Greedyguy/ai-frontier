---
keywords:
  - Spectral Algorithms
  - Effective Span Dimension
  - Learned Kernels
  - RKHS Regression
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.20294
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:48:09.297557",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Spectral Algorithms",
    "Effective Span Dimension",
    "Learned Kernels",
    "RKHS Regression"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Spectral Algorithms": 0.78,
    "Effective Span Dimension": 0.8,
    "Learned Kernels": 0.77,
    "RKHS Regression": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "spectral algorithms",
        "canonical": "Spectral Algorithms",
        "aliases": [
          "spectral methods"
        ],
        "category": "broad_technical",
        "rationale": "Spectral algorithms are a foundational concept in machine learning and connect well with various other techniques.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "effective span dimension",
        "canonical": "Effective Span Dimension",
        "aliases": [
          "ESD"
        ],
        "category": "unique_technical",
        "rationale": "The effective span dimension is a novel concept introduced in this paper, offering a new perspective on complexity measures.",
        "novelty_score": 0.95,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "learned kernels",
        "canonical": "Learned Kernels",
        "aliases": [
          "adaptive kernels"
        ],
        "category": "specific_connectable",
        "rationale": "Learned kernels are crucial for understanding adaptive feature learning and its impact on generalization.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      },
      {
        "surface": "RKHS regression",
        "canonical": "RKHS Regression",
        "aliases": [
          "Reproducing Kernel Hilbert Space regression"
        ],
        "category": "specific_connectable",
        "rationale": "RKHS regression is a specialized technique that connects well with kernel methods and spectral algorithms.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "sequence models",
      "numerical experiments"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "spectral algorithms",
      "resolved_canonical": "Spectral Algorithms",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "effective span dimension",
      "resolved_canonical": "Effective Span Dimension",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "learned kernels",
      "resolved_canonical": "Learned Kernels",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "RKHS regression",
      "resolved_canonical": "RKHS Regression",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Alignment-Sensitive Minimax Rates for Spectral Algorithms with Learned Kernels

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20294.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.20294](https://arxiv.org/abs/2509.20294)

## 🔗 유사한 논문
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (81.0% similar)
- [[2025-09-23/Regularizing Extrapolation in Causal Inference_20250923|Regularizing Extrapolation in Causal Inference]] (80.5% similar)
- [[2025-09-22/Accelerated Gradient Methods with Biased Gradient Estimates_ Risk Sensitivity, High-Probability Guarantees, and Large Deviation Bounds_20250922|Accelerated Gradient Methods with Biased Gradient Estimates: Risk Sensitivity, High-Probability Guarantees, and Large Deviation Bounds]] (80.3% similar)
- [[2025-09-22/Permutation recovery of spikes in noisy high-dimensional tensor estimation_20250922|Permutation recovery of spikes in noisy high-dimensional tensor estimation]] (80.3% similar)
- [[2025-09-22/Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization_20250922|Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization]] (80.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Spectral Algorithms|Spectral Algorithms]]
**🔗 Specific Connectable**: [[keywords/Learned Kernels|Learned Kernels]], [[keywords/RKHS Regression|RKHS Regression]]
**⚡ Unique Technical**: [[keywords/Effective Span Dimension|Effective Span Dimension]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20294v1 Announce Type: new 
Abstract: We study spectral algorithms in the setting where kernels are learned from data. We introduce the effective span dimension (ESD), an alignment-sensitive complexity measure that depends jointly on the signal, spectrum, and noise level $\sigma^2$. The ESD is well-defined for arbitrary kernels and signals without requiring eigen-decay conditions or source conditions. We prove that for sequence models whose ESD is at most $K$, the minimax excess risk scales as $\sigma^2 K$. Furthermore, we analyze over-parameterized gradient flow and prove that it can reduce the ESD. This finding establishes a connection between adaptive feature learning and provable improvements in generalization of spectral algorithms. We demonstrate the generality of the ESD framework by extending it to linear models and RKHS regression, and we support the theory with numerical experiments. This framework provides a novel perspective on generalization beyond traditional fixed-kernel theories.

## 📝 요약

이 논문은 데이터로부터 학습된 커널을 사용하는 스펙트럼 알고리즘을 연구하며, 효과적 스팬 차원(ESD)을 도입합니다. ESD는 신호, 스펙트럼, 노이즈 수준에 따라 결정되는 복잡도 측정으로, 임의의 커널과 신호에 대해 정의됩니다. ESD가 최대 K인 모델의 경우, 미니맥스 초과 위험이 $\sigma^2 K$로 스케일링됨을 증명합니다. 또한, 과매개화된 그래디언트 흐름이 ESD를 감소시킬 수 있음을 보여주어, 적응적 특징 학습과 스펙트럼 알고리즘의 일반화 개선 간의 연결을 제시합니다. 이 프레임워크는 선형 모델과 RKHS 회귀로 확장 가능하며, 수치 실험을 통해 이론을 뒷받침합니다. 이는 전통적 고정 커널 이론을 넘어선 일반화에 대한 새로운 관점을 제공합니다.

## 🎯 주요 포인트

- 1. 효과적 스팬 차원(ESD)은 신호, 스펙트럼, 노이즈 수준에 따라 달라지는 정렬 민감 복잡도 측정치로 도입되었습니다.
- 2. ESD가 최대 K인 시퀀스 모델의 경우, 미니맥스 초과 위험은 $\sigma^2 K$로 스케일링됩니다.
- 3. 과매개변수화된 그래디언트 흐름은 ESD를 감소시킬 수 있으며, 이는 적응적 특징 학습과 스펙트럼 알고리즘의 일반화 개선 간의 연결을 확립합니다.
- 4. ESD 프레임워크는 선형 모델과 RKHS 회귀로 확장 가능하며, 이는 전통적인 고정 커널 이론을 넘어서는 일반화에 대한 새로운 관점을 제공합니다.
- 5. 이론적 주장을 뒷받침하기 위해 수치 실험이 수행되었습니다.


---

*Generated on 2025-09-25 16:48:09*