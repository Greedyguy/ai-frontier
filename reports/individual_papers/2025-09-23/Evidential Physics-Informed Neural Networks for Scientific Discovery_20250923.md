---
keywords:
  - Evidential Physics-Informed Neural Network
  - Uncertainty Estimation
  - Posterior Distribution
  - Deep Ensemble
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.14568
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:53:32.426112",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Evidential Physics-Informed Neural Network",
    "Uncertainty Estimation",
    "Posterior Distribution",
    "Deep Ensemble"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Evidential Physics-Informed Neural Network": 0.78,
    "Uncertainty Estimation": 0.75,
    "Posterior Distribution": 0.72,
    "Deep Ensemble": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Evidential Physics-Informed Neural Network",
        "canonical": "Evidential Physics-Informed Neural Network",
        "aliases": [
          "E-PINN"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach that combines evidential deep learning with physics-informed neural networks, offering a unique perspective in scientific discovery.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Uncertainty Estimation",
        "canonical": "Uncertainty Estimation",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Uncertainty estimation is crucial for validating model predictions and is a key feature of the E-PINN approach.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Posterior Distribution",
        "canonical": "Posterior Distribution",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Understanding posterior distributions is essential for inferring unknown parameters in probabilistic models like E-PINN.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.68,
        "link_intent_score": 0.72
      },
      {
        "surface": "Deep Ensemble",
        "canonical": "Deep Ensemble",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Deep ensembles are a well-known method for uncertainty estimation, providing a basis for comparison with E-PINN.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
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
      "candidate_surface": "Evidential Physics-Informed Neural Network",
      "resolved_canonical": "Evidential Physics-Informed Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Uncertainty Estimation",
      "resolved_canonical": "Uncertainty Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Posterior Distribution",
      "resolved_canonical": "Posterior Distribution",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.68,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Deep Ensemble",
      "resolved_canonical": "Deep Ensemble",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Evidential Physics-Informed Neural Networks for Scientific Discovery

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.14568.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.14568](https://arxiv.org/abs/2509.14568)

## 🔗 유사한 논문
- [[2025-09-22/Bayesian Physics Informed Neural Networks for Reliable Transformer Prognostics_20250922|Bayesian Physics Informed Neural Networks for Reliable Transformer Prognostics]] (88.0% similar)
- [[2025-09-17/A Conformal Prediction Framework for Uncertainty Quantification in Physics-Informed Neural Networks_20250917|A Conformal Prediction Framework for Uncertainty Quantification in Physics-Informed Neural Networks]] (85.0% similar)
- [[2025-09-22/PBPK-iPINNs_ Inverse Physics-Informed Neural Networks for Physiologically Based Pharmacokinetic Brain Models_20250922|PBPK-iPINNs: Inverse Physics-Informed Neural Networks for Physiologically Based Pharmacokinetic Brain Models]] (85.0% similar)
- [[2025-09-23/Physics-Informed Operator Learning for Hemodynamic Modeling_20250923|Physics-Informed Operator Learning for Hemodynamic Modeling]] (81.7% similar)
- [[2025-09-22/Gradient Alignment in Physics-informed Neural Networks_ A Second-Order Optimization Perspective_20250922|Gradient Alignment in Physics-informed Neural Networks: A Second-Order Optimization Perspective]] (79.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Ensemble|Deep Ensemble]]
**🔗 Specific Connectable**: [[keywords/Uncertainty Estimation|Uncertainty Estimation]], [[keywords/Posterior Distribution|Posterior Distribution]]
**⚡ Unique Technical**: [[keywords/Evidential Physics-Informed Neural Network|Evidential Physics-Informed Neural Network]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14568v2 Announce Type: replace 
Abstract: We present the fundamental theory and implementation guidelines underlying Evidential Physics-Informed Neural Network (E-PINN) -- a novel class of uncertainty-aware PINN. It leverages the marginal distribution loss function of evidential deep learning for estimating uncertainty of outputs, and infers unknown parameters of the PDE via a learned posterior distribution. Validating our model on two illustrative case studies -- the 1D Poisson equation with a Gaussian source and the 2D Fisher-KPP equation, we found that E-PINN generated empirical coverage probabilities that were calibrated significantly better than Bayesian PINN and Deep Ensemble methods. To demonstrate real-world applicability, we also present a brief case study on applying E-PINN to analyze clinical glucose-insulin datasets that have featured in medical research on diabetes pathophysiology.

## 📝 요약

E-PINN(Evidential Physics-Informed Neural Network)은 불확실성을 고려한 새로운 PINN 모델로, 증거 기반 딥러닝의 주변 분포 손실 함수를 활용하여 출력의 불확실성을 추정하고, 학습된 사후 분포를 통해 PDE의 미지 파라미터를 추론합니다. 1D 포아송 방정식과 2D Fisher-KPP 방정식 사례 연구를 통해 E-PINN이 Bayesian PINN 및 Deep Ensemble 방법보다 더 잘 보정된 경험적 커버리지 확률을 생성함을 확인했습니다. 또한, 당뇨병 병태생리에 관한 임상적 포도당-인슐린 데이터셋 분석을 통해 실제 적용 가능성을 입증했습니다.

## 🎯 주요 포인트

- 1. E-PINN은 불확실성을 고려한 새로운 유형의 PINN으로, 증거적 심층 학습의 주변 분포 손실 함수를 활용하여 출력의 불확실성을 추정합니다.
- 2. E-PINN은 학습된 사후 분포를 통해 PDE의 미지의 매개변수를 추론합니다.
- 3. 1D Poisson 방정식과 2D Fisher-KPP 방정식 사례 연구에서 E-PINN은 Bayesian PINN 및 Deep Ensemble 방법보다 더 잘 보정된 경험적 커버리지 확률을 생성했습니다.
- 4. E-PINN의 실제 적용 가능성을 보여주기 위해 당뇨병 병태생리학 연구에서 사용된 임상 포도당-인슐린 데이터셋 분석 사례 연구를 제시했습니다.


---

*Generated on 2025-09-24 02:53:32*