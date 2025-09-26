---
keywords:
  - Gaussian Process Regression
  - Neural Network
  - Additive Manufacturing
  - Uncertainty Quantification
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16233
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:33:21.786092",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Gaussian Process Regression",
    "Neural Network",
    "Additive Manufacturing",
    "Uncertainty Quantification"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Gaussian Process Regression": 0.82,
    "Neural Network": 0.79,
    "Additive Manufacturing": 0.81,
    "Uncertainty Quantification": 0.84
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Gaussian Process Regression",
        "canonical": "Gaussian Process Regression",
        "aliases": [
          "GPR"
        ],
        "category": "specific_connectable",
        "rationale": "GPR is a key probabilistic method for uncertainty quantification, linking well with existing probabilistic models.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Bayesian Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "BNNs"
        ],
        "category": "broad_technical",
        "rationale": "BNNs are a specialized form of neural networks, enhancing the link to existing neural network studies.",
        "novelty_score": 0.48,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.79
      },
      {
        "surface": "Additive Manufacturing",
        "canonical": "Additive Manufacturing",
        "aliases": [
          "3D Printing"
        ],
        "category": "unique_technical",
        "rationale": "Additive Manufacturing is a unique technical domain crucial for linking to manufacturing and design strategies.",
        "novelty_score": 0.72,
        "connectivity_score": 0.76,
        "specificity_score": 0.85,
        "link_intent_score": 0.81
      },
      {
        "surface": "Uncertainty Quantification",
        "canonical": "Uncertainty Quantification",
        "aliases": [
          "UQ"
        ],
        "category": "specific_connectable",
        "rationale": "Uncertainty Quantification is central to the paper's methodology, providing a strong link to risk assessment techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.83,
        "specificity_score": 0.8,
        "link_intent_score": 0.84
      }
    ],
    "ban_list_suggestions": [
      "Difference from Target",
      "design features",
      "process repeatability"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Gaussian Process Regression",
      "resolved_canonical": "Gaussian Process Regression",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Bayesian Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.48,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Additive Manufacturing",
      "resolved_canonical": "Additive Manufacturing",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.76,
        "specificity": 0.85,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Uncertainty Quantification",
      "resolved_canonical": "Uncertainty Quantification",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.83,
        "specificity": 0.8,
        "link_intent": 0.84
      }
    }
  ]
}
-->

# Comparison of Deterministic and Probabilistic Machine Learning Algorithms for Precise Dimensional Control and Uncertainty Quantification in Additive Manufacturing

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16233.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16233](https://arxiv.org/abs/2509.16233)

## 🔗 유사한 논문
- [[2025-09-22/Learning to Optimize Capacity Planning in Semiconductor Manufacturing_20250922|Learning to Optimize Capacity Planning in Semiconductor Manufacturing]] (83.6% similar)
- [[2025-09-23/Proactive Statistical Process Control Using AI_ A Time Series Forecasting Approach for Semiconductor Manufacturing_20250923|Proactive Statistical Process Control Using AI: A Time Series Forecasting Approach for Semiconductor Manufacturing]] (82.8% similar)
- [[2025-09-22/Deep Gaussian Process-based Cost-Aware Batch Bayesian Optimization for Complex Materials Design Campaigns_20250922|Deep Gaussian Process-based Cost-Aware Batch Bayesian Optimization for Complex Materials Design Campaigns]] (82.2% similar)
- [[2025-09-17/Physics-based deep kernel learning for parameter estimation in high dimensional PDEs_20250917|Physics-based deep kernel learning for parameter estimation in high dimensional PDEs]] (80.4% similar)
- [[2025-09-22/Kernel Model Validation_ How To Do It, And Why You Should Care_20250922|Kernel Model Validation: How To Do It, And Why You Should Care]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Gaussian Process Regression|Gaussian Process Regression]], [[keywords/Uncertainty Quantification|Uncertainty Quantification]]
**⚡ Unique Technical**: [[keywords/Additive Manufacturing|Additive Manufacturing]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16233v1 Announce Type: new 
Abstract: We present a probabilistic framework to accurately estimate dimensions of additively manufactured components. Using a dataset of 405 parts from nine production runs involving two machines, three polymer materials, and two-part configurations, we examine five key design features. To capture both design information and manufacturing variability, we employ models integrating continuous and categorical factors. For predicting Difference from Target (DFT) values, we test deterministic and probabilistic machine learning methods. Deterministic models, trained on 80% of the dataset, provide precise point estimates, with Support Vector Regression (SVR) achieving accuracy close to process repeatability. To address systematic deviations, we adopt Gaussian Process Regression (GPR) and Bayesian Neural Networks (BNNs). GPR delivers strong predictive performance and interpretability, while BNNs capture both aleatoric and epistemic uncertainties. We investigate two BNN approaches: one balancing accuracy and uncertainty capture, and another offering richer uncertainty decomposition but with lower dimensional accuracy. Our results underscore the importance of quantifying epistemic uncertainty for robust decision-making, risk assessment, and model improvement. We discuss trade-offs between GPR and BNNs in terms of predictive power, interpretability, and computational efficiency, noting that model choice depends on analytical needs. By combining deterministic precision with probabilistic uncertainty quantification, our study provides a rigorous foundation for uncertainty-aware predictive modeling in AM. This approach not only enhances dimensional accuracy but also supports reliable, risk-informed design strategies, thereby advancing data-driven manufacturing methodologies.

## 📝 요약

이 논문은 적층 제조 부품의 치수를 정확하게 추정하기 위한 확률적 프레임워크를 제시합니다. 두 대의 기계, 세 가지 폴리머 소재, 두 가지 부품 구성에서 405개의 부품 데이터를 사용하여 설계 정보와 제조 변동성을 포착합니다. 차이값(DFT)을 예측하기 위해 결정론적 및 확률적 기계 학습 방법을 테스트했으며, 서포트 벡터 회귀(SVR)는 높은 정확도를 보였습니다. 체계적 편차를 해결하기 위해 가우시안 프로세스 회귀(GPR)와 베이지안 신경망(BNN)을 사용했습니다. GPR은 예측 성능과 해석 가능성이 뛰어나며, BNN은 불확실성을 포착합니다. 연구 결과는 불확실성을 정량화하는 것이 의사 결정과 위험 평가에 중요함을 강조합니다. GPR과 BNN의 예측력, 해석 가능성, 계산 효율성 간의 균형을 논의하며, 모델 선택은 분석 요구에 따라 달라진다고 결론짓습니다. 이 연구는 결정론적 정밀도와 확률적 불확실성 정량화를 결합하여 데이터 기반 제조 방법론을 발전시킵니다.

## 🎯 주요 포인트

- 1. 본 연구는 적층 제조 부품의 치수를 정확하게 추정하기 위한 확률적 프레임워크를 제시합니다.
- 2. 405개의 부품 데이터셋을 사용하여 설계 정보와 제조 변동성을 포착하기 위해 연속적 및 범주형 요소를 통합한 모델을 사용합니다.
- 3. 결정론적 모델과 확률론적 기계 학습 방법을 테스트하여 목표 차이(Difference from Target, DFT) 값을 예측합니다.
- 4. Gaussian Process Regression(GPR)과 Bayesian Neural Networks(BNNs)를 사용하여 체계적인 편차를 해결하고, BNNs는 불확실성을 포착합니다.
- 5. GPR과 BNNs의 예측력, 해석 가능성, 계산 효율성 간의 균형을 논의하며, 모델 선택은 분석적 필요에 따라 달라집니다.


---

*Generated on 2025-09-24 01:33:21*