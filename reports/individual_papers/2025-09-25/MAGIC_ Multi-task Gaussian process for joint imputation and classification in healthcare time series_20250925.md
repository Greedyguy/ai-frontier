---
keywords:
  - Multi-task Gaussian Process
  - Functional Logistic Regression
  - Taylor Expansion Approximations
  - EM Algorithm
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19577
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:56:20.892857",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-task Gaussian Process",
    "Functional Logistic Regression",
    "Taylor Expansion Approximations",
    "EM Algorithm"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multi-task Gaussian Process": 0.78,
    "Functional Logistic Regression": 0.72,
    "Taylor Expansion Approximations": 0.68,
    "EM Algorithm": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multi-task Gaussian Process",
        "canonical": "Multi-task Gaussian Process",
        "aliases": [
          "MAGIC"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach combining imputation and classification, which is central to the paper's contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Functional Logistic Regression",
        "canonical": "Functional Logistic Regression",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This technique is integral to the proposed framework, enhancing its specificity and application in healthcare.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "Taylor Expansion Approximations",
        "canonical": "Taylor Expansion Approximations",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "This mathematical technique is crucial for handling intractable likelihood components in the model.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.65,
        "link_intent_score": 0.68
      },
      {
        "surface": "EM Algorithm",
        "canonical": "EM Algorithm",
        "aliases": [
          "Expectation-Maximization Algorithm"
        ],
        "category": "broad_technical",
        "rationale": "A well-known algorithm used for parameter estimation, enhancing the model's robustness.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "time series analysis",
      "healthcare applications",
      "prediction",
      "imputation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multi-task Gaussian Process",
      "resolved_canonical": "Multi-task Gaussian Process",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Functional Logistic Regression",
      "resolved_canonical": "Functional Logistic Regression",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Taylor Expansion Approximations",
      "resolved_canonical": "Taylor Expansion Approximations",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.65,
        "link_intent": 0.68
      }
    },
    {
      "candidate_surface": "EM Algorithm",
      "resolved_canonical": "EM Algorithm",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# MAGIC: Multi-task Gaussian process for joint imputation and classification in healthcare time series

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19577.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19577](https://arxiv.org/abs/2509.19577)

## 🔗 유사한 논문
- [[2025-09-23/MIRA_ Medical Time Series Foundation Model for Real-World Health Data_20250923|MIRA: Medical Time Series Foundation Model for Real-World Health Data]] (84.3% similar)
- [[2025-09-24/Early Prediction of Multi-Label Care Escalation Triggers in the Intensive Care Unit Using Electronic Health Records_20250924|Early Prediction of Multi-Label Care Escalation Triggers in the Intensive Care Unit Using Electronic Health Records]] (83.4% similar)
- [[2025-09-23/Estimating Clinical Lab Test Result Trajectories from PPG using Physiological Foundation Model and Patient-Aware State Space Model -- a UNIPHY+ Approach_20250923|Estimating Clinical Lab Test Result Trajectories from PPG using Physiological Foundation Model and Patient-Aware State Space Model -- a UNIPHY+ Approach]] (82.7% similar)
- [[2025-09-23/TS-P$^2$CL_ Plug-and-Play Dual Contrastive Learning for Vision-Guided Medical Time Series Classification_20250923|TS-P$^2$CL: Plug-and-Play Dual Contrastive Learning for Vision-Guided Medical Time Series Classification]] (82.4% similar)
- [[2025-09-23/Multi-View Contrastive Learning for Robust Domain Adaptation in Medical Time Series Analysis_20250923|Multi-View Contrastive Learning for Robust Domain Adaptation in Medical Time Series Analysis]] (82.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Taylor Expansion Approximations|Taylor Expansion Approximations]], [[keywords/EM Algorithm|EM Algorithm]]
**⚡ Unique Technical**: [[keywords/Multi-task Gaussian Process|Multi-task Gaussian Process]], [[keywords/Functional Logistic Regression|Functional Logistic Regression]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19577v1 Announce Type: cross 
Abstract: Time series analysis has emerged as an important tool for improving patient diagnosis and management in healthcare applications. However, these applications commonly face two critical challenges: time misalignment and data sparsity. Traditional approaches address these issues through a two-step process of imputation followed by prediction. We propose MAGIC (Multi-tAsk Gaussian Process for Imputation and Classification), a novel unified framework that simultaneously performs class-informed missing value imputation and label prediction within a hierarchical multi-task Gaussian process coupled with functional logistic regression. To handle intractable likelihood components, MAGIC employs Taylor expansion approximations with bounded error analysis, and parameter estimation is performed using EM algorithm with block coordinate optimization supported by convergence analysis. We validate MAGIC through two healthcare applications: prediction of post-traumatic headache improvement following mild traumatic brain injury and prediction of in-hospital mortality within 48 hours after ICU admission. In both applications, MAGIC achieves superior predictive accuracy compared to existing methods. The ability to generate real-time and accurate predictions with limited samples facilitates early clinical assessment and treatment planning, enabling healthcare providers to make more informed treatment decisions.

## 📝 요약

이 논문은 의료 분야에서 환자 진단 및 관리를 개선하기 위한 시계열 분석의 중요성을 다루며, 시간 불일치와 데이터 희소성이라는 두 가지 주요 문제를 해결하는 새로운 방법론을 제안합니다. 제안된 MAGIC(Multi-tAsk Gaussian Process for Imputation and Classification) 프레임워크는 계층적 다중 작업 가우시안 프로세스와 기능적 로지스틱 회귀를 결합하여 클래스 정보를 활용한 결측값 보완과 라벨 예측을 동시에 수행합니다. MAGIC은 테일러 전개 근사와 EM 알고리즘을 사용하여 매개변수 추정을 수행하며, 두 가지 의료 응용 사례에서 기존 방법보다 우수한 예측 정확성을 입증했습니다. 이를 통해 제한된 샘플로도 실시간 정확한 예측이 가능해져 조기 임상 평가와 치료 계획 수립에 기여합니다.

## 🎯 주요 포인트

- 1. 시계열 분석은 의료 분야에서 환자 진단 및 관리 개선을 위한 중요한 도구로 부상하고 있다.
- 2. MAGIC은 클래스 정보를 활용한 결측값 보완과 레이블 예측을 동시에 수행하는 통합 프레임워크이다.
- 3. MAGIC은 테일러 전개 근사와 EM 알고리즘을 사용하여 복잡한 가능도 구성 요소를 처리하고 매개변수 추정을 수행한다.
- 4. 두 가지 의료 응용 사례에서 MAGIC은 기존 방법보다 우수한 예측 정확도를 달성하였다.
- 5. 제한된 샘플로 실시간 정확한 예측을 생성하여 조기 임상 평가와 치료 계획을 가능하게 한다.


---

*Generated on 2025-09-25 16:56:20*