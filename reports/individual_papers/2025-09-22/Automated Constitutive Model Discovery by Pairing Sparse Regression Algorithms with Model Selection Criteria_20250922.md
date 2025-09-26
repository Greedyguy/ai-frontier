---
keywords:
  - Sparse Regression
  - Model Selection
  - Constitutive Model Discovery
  - Hyperelasticity
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.16040
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:40:59.487617",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Sparse Regression",
    "Model Selection",
    "Constitutive Model Discovery",
    "Hyperelasticity"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Sparse Regression": 0.82,
    "Model Selection": 0.79,
    "Constitutive Model Discovery": 0.77,
    "Hyperelasticity": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Sparse Regression Algorithms",
        "canonical": "Sparse Regression",
        "aliases": [
          "LASSO",
          "LARS",
          "OMP"
        ],
        "category": "specific_connectable",
        "rationale": "Sparse regression is central to the paper's methodology and links to broader machine learning techniques.",
        "novelty_score": 0.58,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Model Selection Criteria",
        "canonical": "Model Selection",
        "aliases": [
          "AIC",
          "BIC",
          "K-fold CV"
        ],
        "category": "specific_connectable",
        "rationale": "Model selection criteria are crucial for evaluating the algorithms and connect to statistical model evaluation.",
        "novelty_score": 0.55,
        "connectivity_score": 0.83,
        "specificity_score": 0.72,
        "link_intent_score": 0.79
      },
      {
        "surface": "Constitutive Model Discovery",
        "canonical": "Constitutive Model Discovery",
        "aliases": [
          "Model Discovery"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique application area of the framework presented in the paper.",
        "novelty_score": 0.72,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Hyperelasticity",
        "canonical": "Hyperelasticity",
        "aliases": [
          "Isotropic Hyperelasticity",
          "Anisotropic Hyperelasticity"
        ],
        "category": "specific_connectable",
        "rationale": "Hyperelasticity is a key application domain for the algorithms discussed, linking to materials science.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "framework",
      "datasets",
      "results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Sparse Regression Algorithms",
      "resolved_canonical": "Sparse Regression",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Model Selection Criteria",
      "resolved_canonical": "Model Selection",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.83,
        "specificity": 0.72,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Constitutive Model Discovery",
      "resolved_canonical": "Constitutive Model Discovery",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Hyperelasticity",
      "resolved_canonical": "Hyperelasticity",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Automated Constitutive Model Discovery by Pairing Sparse Regression Algorithms with Model Selection Criteria

**Korean Title:** 희소 회귀 알고리즘과 모델 선택 기준을 결합한 자동화된 구성 모델 발견

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16040.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.16040](https://arxiv.org/abs/2509.16040)

## 🔗 유사한 논문
- [[2025-09-22/An Equivariant Graph Network for Interpretable Nanoporous Materials Design_20250922|An Equivariant Graph Network for Interpretable Nanoporous Materials Design]] (79.7% similar)
- [[2025-09-19/MOLE_ Metadata Extraction and Validation in Scientific Papers Using LLMs_20250919|MOLE: Metadata Extraction and Validation in Scientific Papers Using LLMs]] (79.2% similar)
- [[2025-09-22/Deep Gaussian Process-based Cost-Aware Batch Bayesian Optimization for Complex Materials Design Campaigns_20250922|Deep Gaussian Process-based Cost-Aware Batch Bayesian Optimization for Complex Materials Design Campaigns]] (78.8% similar)
- [[2025-09-22/Spatio-temporal, multi-field deep learning of shock propagation in meso-structured media_20250922|Spatio-temporal, multi-field deep learning of shock propagation in meso-structured media]] (78.5% similar)
- [[2025-09-18/Towards universal property prediction in Cartesian space_ TACE is all you need_20250918|Towards universal property prediction in Cartesian space: TACE is all you need]] (78.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Sparse Regression|Sparse Regression]], [[keywords/Model Selection|Model Selection]], [[keywords/Hyperelasticity|Hyperelasticity]]
**⚡ Unique Technical**: [[keywords/Constitutive Model Discovery|Constitutive Model Discovery]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16040v1 Announce Type: new 
Abstract: The automated discovery of constitutive models from data has recently emerged as a promising alternative to the traditional model calibration paradigm. In this work, we present a fully automated framework for constitutive model discovery that systematically pairs three sparse regression algorithms (Least Absolute Shrinkage and Selection Operator (LASSO), Least Angle Regression (LARS), and Orthogonal Matching Pursuit (OMP)) with three model selection criteria: $K$-fold cross-validation (CV), Akaike Information Criterion (AIC), and Bayesian Information Criterion (BIC). This pairing yields nine distinct algorithms for model discovery and enables a systematic exploration of the trade-off between sparsity, predictive performance, and computational cost. While LARS serves as an efficient path-based solver for the $\ell_1$-constrained problem, OMP is introduced as a tractable heuristic for $\ell_0$-regularized selection. The framework is applied to both isotropic and anisotropic hyperelasticity, utilizing both synthetic and experimental datasets. Results reveal that all nine algorithm-criterion combinations perform consistently well for the discovery of isotropic and anisotropic materials, yielding highly accurate constitutive models. These findings broaden the range of viable discovery algorithms beyond $\ell_1$-based approaches such as LASSO.

## 🔍 Abstract (한글 번역)

arXiv:2509.16040v1 발표 유형: 신규  
초록: 데이터로부터 구성 모델을 자동으로 발견하는 방법은 최근 전통적인 모델 보정 패러다임에 대한 유망한 대안으로 부상하고 있습니다. 본 연구에서는 세 가지 희소 회귀 알고리즘(최소 절대 수축 및 선택 연산자(LASSO), 최소 각도 회귀(LARS), 직교 매칭 추구(OMP))와 세 가지 모델 선택 기준($K$-겹 교차 검증(CV), Akaike 정보 기준(AIC), 베이지안 정보 기준(BIC))을 체계적으로 결합한 완전 자동화된 구성 모델 발견 프레임워크를 제시합니다. 이러한 결합은 모델 발견을 위한 아홉 가지 독특한 알고리즘을 제공하며, 희소성, 예측 성능, 계산 비용 간의 절충을 체계적으로 탐구할 수 있게 합니다. LARS는 $\ell_1$ 제약 문제에 대한 효율적인 경로 기반 해법으로 작용하는 반면, OMP는 $\ell_0$ 정규화 선택에 대한 실용적인 휴리스틱으로 도입됩니다. 이 프레임워크는 합성 및 실험 데이터셋을 활용하여 등방성 및 이방성 초탄성에 적용됩니다. 결과는 아홉 가지 알고리즘-기준 조합 모두가 등방성 및 이방성 재료 발견에 대해 일관되게 우수한 성능을 발휘하며, 매우 정확한 구성 모델을 산출함을 보여줍니다. 이러한 발견은 LASSO와 같은 $\ell_1$ 기반 접근법을 넘어서는 다양한 유망한 발견 알고리즘의 범위를 확장합니다.

## 📝 요약

이 연구는 데이터 기반의 구성 모델 자동 발견을 위한 완전 자동화된 프레임워크를 제안합니다. LASSO, LARS, OMP 세 가지 희소 회귀 알고리즘과 $K$-겹 교차 검증, AIC, BIC 세 가지 모델 선택 기준을 조합하여 총 아홉 가지 알고리즘을 개발했습니다. 이 프레임워크는 희소성, 예측 성능, 계산 비용 간의 균형을 체계적으로 탐색합니다. 연구는 등방성 및 이방성 초탄성 재료에 적용되었으며, 모든 알고리즘이 높은 정확도의 구성 모델을 발견하는 데 일관된 성능을 보였습니다. 이로써 LASSO와 같은 $\ell_1$ 기반 접근법을 넘어 다양한 발견 알고리즘의 가능성을 확장했습니다.

## 🎯 주요 포인트

- 1. 데이터 기반의 구성 모델 자동 발견이 전통적인 모델 보정 패러다임의 유망한 대안으로 부상하고 있습니다.
- 2. 본 연구는 LASSO, LARS, OMP와 같은 희소 회귀 알고리즘과 CV, AIC, BIC 모델 선택 기준을 체계적으로 결합한 자동화된 구성 모델 발견 프레임워크를 제시합니다.
- 3. 제안된 프레임워크는 희소성, 예측 성능, 계산 비용 간의 절충을 체계적으로 탐색할 수 있는 아홉 가지 알고리즘을 제공합니다.
- 4. 이 프레임워크는 등방성 및 비등방성 초탄성에 적용되어, 합성 및 실험 데이터 세트를 활용하여 높은 정확도의 구성 모델을 발견합니다.
- 5. 연구 결과는 LASSO와 같은 $\ell_1$ 기반 접근법을 넘어 다양한 발견 알고리즘의 가능성을 확장합니다.


---

*Generated on 2025-09-23 10:40:59*