---
keywords:
  - Large Language Model
  - Entity Matching
  - Temperature Scaling
  - Monte Carlo Dropout
  - Ensemble Methods
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19557
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:55:39.538749",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Entity Matching",
    "Temperature Scaling",
    "Monte Carlo Dropout",
    "Ensemble Methods"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Entity Matching": 0.78,
    "Temperature Scaling": 0.77,
    "Monte Carlo Dropout": 0.8,
    "Ensemble Methods": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the study and connect well with existing research in NLP and AI.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Entity Matching",
        "canonical": "Entity Matching",
        "aliases": [
          "Record Linkage"
        ],
        "category": "unique_technical",
        "rationale": "Entity Matching is a specialized task in data integration, crucial for understanding the paper's focus.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Temperature Scaling",
        "canonical": "Temperature Scaling",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Temperature Scaling is a key technique for confidence calibration, linking to broader machine learning calibration methods.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "Monte Carlo Dropout",
        "canonical": "Monte Carlo Dropout",
        "aliases": [
          "MC Dropout"
        ],
        "category": "specific_connectable",
        "rationale": "Monte Carlo Dropout is a probabilistic method for uncertainty estimation, relevant to the study's calibration focus.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Ensembles",
        "canonical": "Ensemble Methods",
        "aliases": [
          "Ensemble Learning"
        ],
        "category": "specific_connectable",
        "rationale": "Ensemble Methods are widely used for improving model robustness and are directly applied in the study.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.68,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "baseline",
      "datasets",
      "findings"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Entity Matching",
      "resolved_canonical": "Entity Matching",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Temperature Scaling",
      "resolved_canonical": "Temperature Scaling",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Monte Carlo Dropout",
      "resolved_canonical": "Monte Carlo Dropout",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Ensembles",
      "resolved_canonical": "Ensemble Methods",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.68,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Confidence Calibration in Large Language Model-Based Entity Matching

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19557.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19557](https://arxiv.org/abs/2509.19557)

## 🔗 유사한 논문
- [[2025-09-22/Calibrating LLM Confidence by Probing Perturbed Representation Stability_20250922|Calibrating LLM Confidence by Probing Perturbed Representation Stability]] (83.1% similar)
- [[2025-09-25/Uncertainty Quantification of Large Language Models using Approximate Bayesian Computation_20250925|Uncertainty Quantification of Large Language Models using Approximate Bayesian Computation]] (82.8% similar)
- [[2025-09-23/Decoding Uncertainty_ The Impact of Decoding Strategies for Uncertainty Estimation in Large Language Models_20250923|Decoding Uncertainty: The Impact of Decoding Strategies for Uncertainty Estimation in Large Language Models]] (80.7% similar)
- [[2025-09-18/Calibrating LLMs for Text-to-SQL Parsing by Leveraging Sub-clause Frequencies_20250918|Calibrating LLMs for Text-to-SQL Parsing by Leveraging Sub-clause Frequencies]] (80.2% similar)
- [[2025-09-23/Post-hoc Reward Calibration_ A Case Study on Length Bias_20250923|Post-hoc Reward Calibration: A Case Study on Length Bias]] (79.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Temperature Scaling|Temperature Scaling]], [[keywords/Monte Carlo Dropout|Monte Carlo Dropout]], [[keywords/Ensemble Methods|Ensemble Methods]]
**⚡ Unique Technical**: [[keywords/Entity Matching|Entity Matching]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19557v1 Announce Type: cross 
Abstract: This research aims to explore the intersection of Large Language Models and confidence calibration in Entity Matching. To this end, we perform an empirical study to compare baseline RoBERTa confidences for an Entity Matching task against confidences that are calibrated using Temperature Scaling, Monte Carlo Dropout and Ensembles. We use the Abt-Buy, DBLP-ACM, iTunes-Amazon and Company datasets. The findings indicate that the proposed modified RoBERTa model exhibits a slight overconfidence, with Expected Calibration Error scores ranging from 0.0043 to 0.0552 across datasets. We find that this overconfidence can be mitigated using Temperature Scaling, reducing Expected Calibration Error scores by up to 23.83%.

## 📝 요약

이 연구는 대형 언어 모델과 신뢰도 보정의 교차점에서 엔티티 매칭을 탐구합니다. RoBERTa 모델의 기본 신뢰도를 온도 조정, 몬테카를로 드롭아웃, 앙상블 기법으로 보정하여 비교하는 실증 연구를 수행했습니다. Abt-Buy, DBLP-ACM, iTunes-Amazon, Company 데이터셋을 사용한 결과, 수정된 RoBERTa 모델이 약간의 과신을 보였으며, 데이터셋 전반에서 기대 보정 오류 점수가 0.0043에서 0.0552로 나타났습니다. 온도 조정을 통해 과신을 최대 23.83%까지 줄일 수 있음을 발견했습니다.

## 🎯 주요 포인트

- 1. 본 연구는 대형 언어 모델과 신뢰도 보정의 교차점을 탐구하는 것을 목표로 합니다.
- 2. RoBERTa 모델의 신뢰도를 Temperature Scaling, Monte Carlo Dropout, Ensembles 기법으로 보정하여 비교 연구를 수행했습니다.
- 3. 사용된 데이터셋은 Abt-Buy, DBLP-ACM, iTunes-Amazon, Company입니다.
- 4. 수정된 RoBERTa 모델은 약간의 과신을 보이며, 데이터셋에 따라 기대 보정 오류 점수가 0.0043에서 0.0552 사이로 나타났습니다.
- 5. Temperature Scaling을 사용하여 과신 문제를 완화할 수 있으며, 기대 보정 오류 점수를 최대 23.83%까지 감소시킬 수 있음을 발견했습니다.


---

*Generated on 2025-09-25 16:55:39*