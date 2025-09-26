---
keywords:
  - Multicalibration
  - Distance to Calibration Framework
  - Intersectional Fairness
  - Auditability
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16930
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:45:01.430239",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multicalibration",
    "Distance to Calibration Framework",
    "Intersectional Fairness",
    "Auditability"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multicalibration": 0.78,
    "Distance to Calibration Framework": 0.7,
    "Intersectional Fairness": 0.72,
    "Auditability": 0.68
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multicalibration",
        "canonical": "Multicalibration",
        "aliases": [
          "Multi-calibration"
        ],
        "category": "unique_technical",
        "rationale": "Multicalibration is a key concept in the paper, offering a unique perspective on calibration across multiple subgroups.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Distance to Calibration Framework",
        "canonical": "Distance to Calibration Framework",
        "aliases": [
          "dCE Framework"
        ],
        "category": "unique_technical",
        "rationale": "This framework is central to understanding the calibration metrics discussed in the paper.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Intersectional Fairness",
        "canonical": "Intersectional Fairness",
        "aliases": [
          "Intersectional Equity"
        ],
        "category": "evolved_concepts",
        "rationale": "Intersectional fairness is crucial for understanding the fairness implications of multicalibration.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      },
      {
        "surface": "Auditability",
        "canonical": "Auditability",
        "aliases": [
          "Auditable"
        ],
        "category": "broad_technical",
        "rationale": "Auditability is a significant aspect of the paper, linking to the reliability of multicalibration metrics.",
        "novelty_score": 0.5,
        "connectivity_score": 0.6,
        "specificity_score": 0.7,
        "link_intent_score": 0.68
      }
    ],
    "ban_list_suggestions": [
      "Calibration",
      "Predictor"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multicalibration",
      "resolved_canonical": "Multicalibration",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Distance to Calibration Framework",
      "resolved_canonical": "Distance to Calibration Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Intersectional Fairness",
      "resolved_canonical": "Intersectional Fairness",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Auditability",
      "resolved_canonical": "Auditability",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.6,
        "specificity": 0.7,
        "link_intent": 0.68
      }
    }
  ]
}
-->

# Auditability and the Landscape of Distance to Multicalibration

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16930.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16930](https://arxiv.org/abs/2509.16930)

## 🔗 유사한 논문
- [[2025-09-22/Calibrating LLM Confidence by Probing Perturbed Representation Stability_20250922|Calibrating LLM Confidence by Probing Perturbed Representation Stability]] (79.9% similar)
- [[2025-09-22/A re-calibration method for object detection with multi-modal alignment bias in autonomous driving_20250922|A re-calibration method for object detection with multi-modal alignment bias in autonomous driving]] (79.8% similar)
- [[2025-09-22/MoCA_ Multi-modal Cross-masked Autoencoder for Digital Health Measurements_20250922|MoCA: Multi-modal Cross-masked Autoencoder for Digital Health Measurements]] (79.6% similar)
- [[2025-09-19/Disproving the Feasibility of Learned Confidence Calibration Under Binary Supervision_ An Information-Theoretic Impossibility_20250919|Disproving the Feasibility of Learned Confidence Calibration Under Binary Supervision: An Information-Theoretic Impossibility]] (79.5% similar)
- [[2025-09-19/A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation_20250919|A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation]] (79.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Auditability|Auditability]]
**⚡ Unique Technical**: [[keywords/Multicalibration|Multicalibration]], [[keywords/Distance to Calibration Framework|Distance to Calibration Framework]]
**🚀 Evolved Concepts**: [[keywords/Intersectional Fairness|Intersectional Fairness]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16930v1 Announce Type: new 
Abstract: Calibration is a critical property for establishing the trustworthiness of predictors that provide uncertainty estimates. Multicalibration is a strengthening of calibration which requires that predictors be calibrated on a potentially overlapping collection of subsets of the domain. As multicalibration grows in popularity with practitioners, an essential question is: how do we measure how multicalibrated a predictor is? B{\l}asiok et al. (2023) considered this question for standard calibration by introducing the distance to calibration framework (dCE) to understand how calibration metrics relate to each other and the ground truth. Building on the dCE framework, we consider the auditability of the distance to multicalibration of a predictor $f$.
  We begin by considering two natural generalizations of dCE to multiple subgroups: worst group dCE (wdMC), and distance to multicalibration (dMC). We argue that there are two essential properties of any multicalibration error metric: 1) the metric should capture how much $f$ would need to be modified in order to be perfectly multicalibrated; and 2) the metric should be auditable in an information theoretic sense. We show that wdMC and dMC each fail to satisfy one of these two properties, and that similar barriers arise when considering the auditability of general distance to multigroup fairness notions. We then propose two (equivalent) multicalibration metrics which do satisfy these requirements: 1) a continuized variant of dMC; and 2) a distance to intersection multicalibration, which leans on intersectional fairness desiderata. Along the way, we shed light on the loss-landscape of distance to multicalibration and the geometry of the set of perfectly multicalibrated predictors. Our findings may have implications for the development of stronger multicalibration algorithms as well as multigroup auditing more generally.

## 📝 요약

이 논문은 예측 모델의 신뢰성을 높이기 위한 다중 보정(multicalibration)의 측정 방법을 제안합니다. 기존의 보정 측정 프레임워크인 dCE를 확장하여, 다중 보정의 거리 측정 방법인 wdMC와 dMC를 소개하지만, 이들은 각각 완벽한 다중 보정을 위한 수정 정도와 정보 이론적 감사 가능성을 충족하지 못합니다. 이를 해결하기 위해, 두 가지 새로운 다중 보정 측정 방법을 제안합니다: 연속화된 dMC와 교차 다중 보정 거리. 이 연구는 다중 보정 알고리즘과 다중 그룹 감사의 발전에 기여할 수 있습니다.

## 🎯 주요 포인트

- 1. 멀티캘리브레이션은 예측기의 신뢰성을 높이기 위해 중요한 속성으로, 여러 하위 그룹에 대해 캘리브레이션이 이루어져야 한다.
- 2. 기존의 dCE 프레임워크를 기반으로, 예측기의 멀티캘리브레이션 거리 측정 가능성을 연구하였다.
- 3. wdMC와 dMC는 각각 멀티캘리브레이션 오류 측정의 필수 속성을 충족하지 못하며, 일반적인 멀티그룹 공정성 거리 측정에서도 유사한 문제가 발생한다.
- 4. 두 가지 새로운 멀티캘리브레이션 측정 방법을 제안하였으며, 이는 정보 이론적 감사 가능성을 만족한다.
- 5. 연구 결과는 더 강력한 멀티캘리브레이션 알고리즘 개발과 멀티그룹 감사에 대한 일반적인 이해를 발전시킬 수 있다.


---

*Generated on 2025-09-24 01:45:01*