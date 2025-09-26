<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:34:34.856185",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Temporal Conformal Prediction",
    "Robbins-Monro Offset",
    "Quantile Regression",
    "Distribution Shift"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Temporal Conformal Prediction": 0.8,
    "Robbins-Monro Offset": 0.75,
    "Quantile Regression": 0.7,
    "Distribution Shift": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Temporal Conformal Prediction",
        "canonical": "Temporal Conformal Prediction",
        "aliases": [
          "TCP"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel framework introduced in the paper, providing a unique approach to risk forecasting.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Robbins-Monro offset",
        "canonical": "Robbins-Monro Offset",
        "aliases": [
          "RM offset"
        ],
        "category": "unique_technical",
        "rationale": "The RM offset is a specific technique used within TCP to improve calibration, which is unique to this framework.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "Quantile Regression",
        "canonical": "Quantile Regression",
        "aliases": [
          "QR"
        ],
        "category": "broad_technical",
        "rationale": "Quantile Regression is a key baseline method used for comparison, linking statistical methods with machine learning.",
        "novelty_score": 0.3,
        "connectivity_score": 0.8,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "distribution shift",
        "canonical": "Distribution Shift",
        "aliases": [
          "nonstationary time series"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding distribution shift is crucial for adaptive risk forecasting, connecting statistical inference with machine learning.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
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
      "candidate_surface": "Temporal Conformal Prediction",
      "resolved_canonical": "Temporal Conformal Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Robbins-Monro offset",
      "resolved_canonical": "Robbins-Monro Offset",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Quantile Regression",
      "resolved_canonical": "Quantile Regression",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.8,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "distribution shift",
      "resolved_canonical": "Distribution Shift",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Temporal Conformal Prediction (TCP): A Distribution-Free Statistical and Machine Learning Framework for Adaptive Risk Forecasting

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2507.05470.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2507.05470](https://arxiv.org/abs/2507.05470)

## 🔗 유사한 논문
- [[2025-09-23/Conformal Prediction with Upper and Lower Bound Models_20250923|Conformal Prediction with Upper and Lower Bound Models]] (81.4% similar)
- [[2025-09-22/Probabilistic Conformal Coverage Guarantees in Small-Data Settings_20250922|Probabilistic Conformal Coverage Guarantees in Small-Data Settings]] (80.2% similar)
- [[2025-09-18/From Patterns to Predictions_ A Shapelet-Based Framework for Directional Forecasting in Noisy Financial Markets_20250918|From Patterns to Predictions: A Shapelet-Based Framework for Directional Forecasting in Noisy Financial Markets]] (79.0% similar)
- [[2025-09-17/A Conformal Prediction Framework for Uncertainty Quantification in Physics-Informed Neural Networks_20250917|A Conformal Prediction Framework for Uncertainty Quantification in Physics-Informed Neural Networks]] (79.0% similar)
- [[2025-09-24/On Multi-entity, Multivariate Quickest Change Point Detection_20250924|On Multi-entity, Multivariate Quickest Change Point Detection]] (78.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Quantile Regression|Quantile Regression]]
**🔗 Specific Connectable**: [[keywords/Distribution Shift|Distribution Shift]]
**⚡ Unique Technical**: [[keywords/Temporal Conformal Prediction|Temporal Conformal Prediction]], [[keywords/Robbins-Monro Offset|Robbins-Monro Offset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.05470v3 Announce Type: replace-cross 
Abstract: We propose Temporal Conformal Prediction (TCP), a distribution-free framework for constructing well-calibrated prediction intervals in nonstationary time series. TCP combines a quantile forecaster with split-conformal calibration on a rolling window and, in its TCP-RM variant, augments the conformal threshold with a Robbins-Monro (RM) offset to steer coverage toward a target level in real time. We benchmark TCP against GARCH, Historical Simulation, and a rolling Quantile Regression (QR) baseline across equities (S&amp;P500), cryptocurrency (Bitcoin), and commodities (Gold). Three consistent findings emerge. First, rolling QR produces the sharpest intervals but is materially under-calibrated (e.g., S&amp;P500: 86.3% vs. 95% target). Second, TCP and TCP-RM achieve near-nominal coverage while delivering substantially narrower intervals than Historical Simulation (e.g., S&amp;P500: 29% reduction in width). Third, the RM update improves calibration with negligible width cost. Crisis-window visualizations around March 2020 show TCP/TCP-RM expanding and contracting intervals promptly as volatility spikes and recedes, with red dots marking days of miscoverage. A sensitivity study confirms robustness to window size and step-size choices. Overall, TCP provides a practical, theoretically grounded solution for calibrated uncertainty quantification under distribution shift, bridging statistical inference and machine learning for risk forecasting.

## 📝 요약

이 논문에서는 비정상 시계열에서 잘 보정된 예측 구간을 구성하기 위한 분포 자유 프레임워크인 Temporal Conformal Prediction(TCP)을 제안합니다. TCP는 분할 적합 보정을 통해 롤링 윈도우에서 퀀타일 예측기를 결합하며, TCP-RM 변형에서는 Robbins-Monro 오프셋을 추가하여 실시간으로 목표 수준을 향해 커버리지를 조정합니다. S&P500, 비트코인, 금과 같은 자산을 대상으로 GARCH, Historical Simulation, 롤링 퀀타일 회귀(QR)와 비교한 결과, QR은 가장 날카로운 구간을 제공하지만 보정이 부족하고, TCP와 TCP-RM은 목표 커버리지를 거의 달성하면서도 Historical Simulation보다 구간 폭이 좁습니다. 특히, RM 업데이트는 보정 개선에 기여하면서도 구간 폭에 거의 영향을 미치지 않습니다. 2020년 3월 위기 시각화에서는 변동성이 급등하고 감소할 때 TCP/TCP-RM이 구간을 신속히 조정하는 것을 보여줍니다. 전반적으로 TCP는 분포 변화 하에서 보정된 불확실성 정량화를 위한 실용적이고 이론적으로 근거 있는 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. Temporal Conformal Prediction (TCP)는 비정상 시계열에서 잘 보정된 예측 구간을 제공하는 분포 무관 프레임워크입니다.
- 2. TCP는 롤링 윈도우에서의 분할 적합 보정과 결합하여 목표 수준으로 실시간 커버리지를 조정합니다.
- 3. TCP와 TCP-RM은 역사적 시뮬레이션보다 더 좁은 구간을 제공하면서도 명목 커버리지에 근접한 결과를 달성합니다.
- 4. RM 업데이트는 구간 너비에 거의 영향을 미치지 않으면서 보정을 향상시킵니다.
- 5. TCP는 분포 변화 하에서 보정된 불확실성 정량화를 위한 실용적이고 이론적으로 근거 있는 솔루션을 제공합니다.


---

*Generated on 2025-09-24 15:34:34*