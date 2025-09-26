---
keywords:
  - Local Differential Privacy
  - Wavelet Expansion
  - Distribution Estimation
  - Wasserstein Distance
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19661
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:39:00.286474",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Local Differential Privacy",
    "Wavelet Expansion",
    "Distribution Estimation",
    "Wasserstein Distance"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Local Differential Privacy": 0.8,
    "Wavelet Expansion": 0.75,
    "Distribution Estimation": 0.7,
    "Wasserstein Distance": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Local Differential Privacy",
        "canonical": "Local Differential Privacy",
        "aliases": [
          "LDP"
        ],
        "category": "unique_technical",
        "rationale": "Local Differential Privacy is a key concept in privacy-preserving data analysis, crucial for linking privacy-focused research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Wavelet Expansion",
        "canonical": "Wavelet Expansion",
        "aliases": [
          "Wavelet Transform"
        ],
        "category": "unique_technical",
        "rationale": "Wavelet Expansion is a specific mathematical technique used in the paper, providing a unique angle for connecting related mathematical methods.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Distribution Estimation",
        "canonical": "Distribution Estimation",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Distribution Estimation is a fundamental task in statistics and machine learning, linking to a broad range of estimation techniques.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.7
      },
      {
        "surface": "Wasserstein Distance",
        "canonical": "Wasserstein Distance",
        "aliases": [
          "Earth Mover's Distance"
        ],
        "category": "specific_connectable",
        "rationale": "Wasserstein Distance is a specific metric for measuring distribution similarity, useful for linking to other metric-based research.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Local Differential Privacy",
      "resolved_canonical": "Local Differential Privacy",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Wavelet Expansion",
      "resolved_canonical": "Wavelet Expansion",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Distribution Estimation",
      "resolved_canonical": "Distribution Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Wasserstein Distance",
      "resolved_canonical": "Wasserstein Distance",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Consistent Estimation of Numerical Distributions under Local Differential Privacy by Wavelet Expansion

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19661.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19661](https://arxiv.org/abs/2509.19661)

## 🔗 유사한 논문
- [[2025-09-23/Differential Privacy for Euclidean Jordan Algebra with Applications to Private Symmetric Cone Programming_20250923|Differential Privacy for Euclidean Jordan Algebra with Applications to Private Symmetric Cone Programming]] (80.6% similar)
- [[2025-09-23/Discrete Diffusion Models_ Novel Analysis and New Sampler Guarantees_20250923|Discrete Diffusion Models: Novel Analysis and New Sampler Guarantees]] (80.5% similar)
- [[2025-09-22/Query-Efficient Locally Private Hypothesis Selection via the Scheffe Graph_20250922|Query-Efficient Locally Private Hypothesis Selection via the Scheffe Graph]] (80.4% similar)
- [[2025-09-24/A Weighted Gradient Tracking Privacy-Preserving Method for Distributed Optimization_20250924|A Weighted Gradient Tracking Privacy-Preserving Method for Distributed Optimization]] (80.3% similar)
- [[2025-09-24/Long-Range Graph Wavelet Networks_20250924|Long-Range Graph Wavelet Networks]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Distribution Estimation|Distribution Estimation]], [[keywords/Wasserstein Distance|Wasserstein Distance]]
**⚡ Unique Technical**: [[keywords/Local Differential Privacy|Local Differential Privacy]], [[keywords/Wavelet Expansion|Wavelet Expansion]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19661v1 Announce Type: new 
Abstract: Distribution estimation under local differential privacy (LDP) is a fundamental and challenging task. Significant progresses have been made on categorical data. However, due to different evaluation metrics, these methods do not work well when transferred to numerical data. In particular, we need to prevent the probability mass from being misplaced far away. In this paper, we propose a new approach that express the sample distribution using wavelet expansions. The coefficients of wavelet series are estimated under LDP. Our method prioritizes the estimation of low-order coefficients, in order to ensure accurate estimation at macroscopic level. Therefore, the probability mass is prevented from being misplaced too far away from its ground truth. We establish theoretical guarantees for our methods. Experiments show that our wavelet expansion method significantly outperforms existing solutions under Wasserstein and KS distances.

## 📝 요약

이 논문은 지역 차분 프라이버시(LDP) 하에서의 분포 추정 문제를 다룹니다. 기존의 범주형 데이터에 대한 방법들은 수치형 데이터에 잘 적용되지 않는 문제를 해결하기 위해, 저자들은 샘플 분포를 웨이블릿 확장으로 표현하는 새로운 접근법을 제안했습니다. 이 방법은 저차 계수를 우선적으로 추정하여, 확률 질량이 실제 값에서 멀리 벗어나는 것을 방지합니다. 이론적 보장을 제공하며, 실험 결과 웨이블릿 확장 방법이 Wasserstein 거리와 KS 거리 측면에서 기존 솔루션보다 뛰어남을 보여줍니다.

## 🎯 주요 포인트

- 1. 본 논문은 지역적 차등 프라이버시(LDP) 하에서의 분포 추정을 다루며, 특히 수치 데이터에 대한 새로운 접근 방식을 제안합니다.
- 2. 제안된 방법은 웨이블릿 확장을 사용하여 샘플 분포를 표현하고, LDP 하에서 웨이블릿 계수를 추정합니다.
- 3. 저차 계수의 정확한 추정을 우선시하여 확률 질량이 실제 값에서 멀리 벗어나지 않도록 합니다.
- 4. 제안된 방법은 이론적 보장을 제공하며, 실험 결과 Wasserstein 및 KS 거리에서 기존 솔루션보다 성능이 뛰어남을 보여줍니다.


---

*Generated on 2025-09-25 16:39:00*