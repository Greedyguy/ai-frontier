---
keywords:
  - Kolmogorov-Arnold Networks
  - B-splines
  - Sobolev Spaces
  - Nonparametric Regression
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19830
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:50:08.760863",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Kolmogorov-Arnold Networks",
    "B-splines",
    "Sobolev Spaces",
    "Nonparametric Regression"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Kolmogorov-Arnold Networks": 0.8,
    "B-splines": 0.78,
    "Sobolev Spaces": 0.75,
    "Nonparametric Regression": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Kolmogorov-Arnold Networks",
        "canonical": "Kolmogorov-Arnold Networks",
        "aliases": [
          "KANs"
        ],
        "category": "unique_technical",
        "rationale": "Kolmogorov-Arnold Networks are central to the paper's contributions and represent a unique framework for function approximation.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "B-splines",
        "canonical": "B-splines",
        "aliases": [
          "B-spline basis"
        ],
        "category": "specific_connectable",
        "rationale": "B-splines are a key component in the paper's methodology, offering potential connections to other spline-based approximation techniques.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Sobolev spaces",
        "canonical": "Sobolev Spaces",
        "aliases": [
          "Sobolev space"
        ],
        "category": "specific_connectable",
        "rationale": "Sobolev spaces are crucial for understanding the mathematical framework of the convergence rates discussed in the paper.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "nonparametric regression",
        "canonical": "Nonparametric Regression",
        "aliases": [
          "non-parametric regression"
        ],
        "category": "broad_technical",
        "rationale": "Nonparametric regression is a broad technical area that connects the paper's findings to a wider field of study.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "convergence rate",
      "simulation studies"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Kolmogorov-Arnold Networks",
      "resolved_canonical": "Kolmogorov-Arnold Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "B-splines",
      "resolved_canonical": "B-splines",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Sobolev spaces",
      "resolved_canonical": "Sobolev Spaces",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "nonparametric regression",
      "resolved_canonical": "Nonparametric Regression",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# On the Rate of Convergence of Kolmogorov-Arnold Network Regression Estimators

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19830.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19830](https://arxiv.org/abs/2509.19830)

## 🔗 유사한 논문
- [[2025-09-23/Interpretable Clinical Classification with Kolgomorov-Arnold Networks_20250923|Interpretable Clinical Classification with Kolgomorov-Arnold Networks]] (84.9% similar)
- [[2025-09-24/Physics-informed time series analysis with Kolmogorov-Arnold Networks under Ehrenfest constraints_20250924|Physics-informed time series analysis with Kolmogorov-Arnold Networks under Ehrenfest constraints]] (84.8% similar)
- [[2025-09-18/Taylor-Series Expanded Kolmogorov-Arnold Network for Medical Imaging Classification_20250918|Taylor-Series Expanded Kolmogorov-Arnold Network for Medical Imaging Classification]] (83.7% similar)
- [[2025-09-23/KANO_ Kolmogorov-Arnold Neural Operator_20250923|KANO: Kolmogorov-Arnold Neural Operator]] (80.0% similar)
- [[2025-09-17/Quantum Variational Activation Functions Empower Kolmogorov-Arnold Networks_20250917|Quantum Variational Activation Functions Empower Kolmogorov-Arnold Networks]] (79.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Nonparametric Regression|Nonparametric Regression]]
**🔗 Specific Connectable**: [[keywords/B-splines|B-splines]], [[keywords/Sobolev Spaces|Sobolev Spaces]]
**⚡ Unique Technical**: [[keywords/Kolmogorov-Arnold Networks|Kolmogorov-Arnold Networks]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19830v1 Announce Type: cross 
Abstract: Kolmogorov-Arnold Networks (KANs) offer a structured and interpretable framework for multivariate function approximation by composing univariate transformations through additive or multiplicative aggregation. This paper establishes theoretical convergence guarantees for KANs when the univariate components are represented by B-splines. We prove that both additive and hybrid additive-multiplicative KANs attain the minimax-optimal convergence rate $O(n^{-2r/(2r+1)})$ for functions in Sobolev spaces of smoothness $r$. We further derive guidelines for selecting the optimal number of knots in the B-splines. The theory is supported by simulation studies that confirm the predicted convergence rates. These results provide a theoretical foundation for using KANs in nonparametric regression and highlight their potential as a structured alternative to existing methods.

## 📝 요약

Kolmogorov-Arnold Networks (KANs)는 다변수 함수 근사에 대한 구조적이고 해석 가능한 프레임워크를 제공합니다. 이 논문은 KANs가 B-스플라인으로 표현된 경우 이론적 수렴 보장을 확립합니다. 우리는 KANs가 Sobolev 공간의 함수에 대해 최소 극대 수렴 속도 $O(n^{-2r/(2r+1)})$를 달성함을 증명하였으며, B-스플라인의 최적 매듭 수를 선택하기 위한 지침을 도출했습니다. 시뮬레이션 연구를 통해 이론적 수렴 속도를 확인하였으며, 이는 비모수 회귀에서 KANs의 이론적 기반을 제공하고 기존 방법에 대한 구조적 대안으로서의 가능성을 강조합니다.

## 🎯 주요 포인트

- 1. Kolmogorov-Arnold Networks(KANs)는 다변수 함수 근사를 위한 구조적이고 해석 가능한 프레임워크를 제공합니다.
- 2. B-스플라인을 사용한 KANs의 수렴 보장이 이론적으로 확립되었습니다.
- 3. KANs는 Sobolev 공간의 함수에 대해 minimax-최적 수렴 속도 $O(n^{-2r/(2r+1)})$를 달성합니다.
- 4. B-스플라인의 최적 매듭 수 선택을 위한 지침이 도출되었습니다.
- 5. 시뮬레이션 연구가 예측된 수렴 속도를 확인하여 KANs의 이론적 기반을 제공합니다.


---

*Generated on 2025-09-25 15:50:08*