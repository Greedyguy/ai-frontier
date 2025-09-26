---
keywords:
  - Large Language Model
  - Approximate Bayesian Computation
  - Predictive Probability
  - Expected Calibration Error
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19375
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:32:27.897020",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Approximate Bayesian Computation",
    "Predictive Probability",
    "Expected Calibration Error"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Approximate Bayesian Computation": 0.8,
    "Predictive Probability": 0.78,
    "Expected Calibration Error": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus, linking to a well-established concept in AI.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Approximate Bayesian Computation",
        "canonical": "Approximate Bayesian Computation",
        "aliases": [
          "ABC"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach for uncertainty quantification in LLMs.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "predictive probabilities",
        "canonical": "Predictive Probability",
        "aliases": [
          "predictive probabilities"
        ],
        "category": "specific_connectable",
        "rationale": "Key concept for understanding the output of LLMs in this context.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "Expected Calibration Error",
        "canonical": "Expected Calibration Error",
        "aliases": [
          "ECE"
        ],
        "category": "specific_connectable",
        "rationale": "Important metric for evaluating model calibration, relevant to the paper's findings.",
        "novelty_score": 0.55,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "model logits",
      "elicited probabilities"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Approximate Bayesian Computation",
      "resolved_canonical": "Approximate Bayesian Computation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "predictive probabilities",
      "resolved_canonical": "Predictive Probability",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Expected Calibration Error",
      "resolved_canonical": "Expected Calibration Error",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Uncertainty Quantification of Large Language Models using Approximate Bayesian Computation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19375.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19375](https://arxiv.org/abs/2509.19375)

## 🔗 유사한 논문
- [[2025-09-22/Calibrating LLM Confidence by Probing Perturbed Representation Stability_20250922|Calibrating LLM Confidence by Probing Perturbed Representation Stability]] (86.9% similar)
- [[2025-09-22/Quantifying Self-Awareness of Knowledge in Large Language Models_20250922|Quantifying Self-Awareness of Knowledge in Large Language Models]] (85.9% similar)
- [[2025-09-17/Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (85.7% similar)
- [[2025-09-22/Quantifying Uncertainty in Natural Language Explanations of Large Language Models for Question Answering_20250922|Quantifying Uncertainty in Natural Language Explanations of Large Language Models for Question Answering]] (85.5% similar)
- [[2025-09-24/Advances in Large Language Models for Medicine_20250924|Advances in Large Language Models for Medicine]] (85.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Predictive Probability|Predictive Probability]], [[keywords/Expected Calibration Error|Expected Calibration Error]]
**⚡ Unique Technical**: [[keywords/Approximate Bayesian Computation|Approximate Bayesian Computation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19375v1 Announce Type: cross 
Abstract: Despite their widespread applications, Large Language Models (LLMs) often struggle to express uncertainty, posing a challenge for reliable deployment in high stakes and safety critical domains like clinical diagnostics. Existing standard baseline methods such as model logits and elicited probabilities produce overconfident and poorly calibrated estimates. In this work, we propose Approximate Bayesian Computation (ABC), a likelihood-free Bayesian inference, based approach that treats LLMs as a stochastic simulator to infer posterior distributions over predictive probabilities. We evaluate our ABC approach on two clinically relevant benchmarks: a synthetic oral lesion diagnosis dataset and the publicly available GretelAI symptom-to-diagnosis dataset. Compared to standard baselines, our approach improves accuracy by up to 46.9\%, reduces Brier scores by 74.4\%, and enhances calibration as measured by Expected Calibration Error (ECE) and predictive entropy.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 불확실성 표현 문제를 해결하기 위해 Approximate Bayesian Computation (ABC) 방법론을 제안합니다. 기존의 모델 로그잇 및 확률 추정 방식은 과신하고 보정이 잘 안 되는 문제를 가지고 있습니다. ABC는 LLM을 확률적 시뮬레이터로 간주하여 예측 확률의 사후 분포를 추론하는 접근법입니다. 이 방법은 구강 병변 진단 데이터셋과 GretelAI 증상-진단 데이터셋에서 평가되었으며, 기존 방법에 비해 정확도를 최대 46.9% 향상시키고, Brier 점수를 74.4% 감소시키며, 보정 오류(ECE)와 예측 엔트로피 측면에서 개선을 보였습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)은 불확실성을 표현하는 데 어려움을 겪어 신뢰성 있는 배포에 도전 과제를 제기합니다.
- 2. 기존의 모델 로짓 및 확률 추정 방법은 과신하고 잘못된 보정을 초래합니다.
- 3. 본 연구에서는 LLMs를 확률적 시뮬레이터로 취급하여 예측 확률의 사후 분포를 추론하는 ABC 접근법을 제안합니다.
- 4. 제안된 ABC 접근법은 두 가지 임상적으로 관련된 벤치마크에서 기존 방법보다 정확성을 최대 46.9% 향상시킵니다.
- 5. Brier 점수를 74.4% 감소시키고, ECE 및 예측 엔트로피로 측정한 보정 능력을 향상시킵니다.


---

*Generated on 2025-09-25 15:32:27*