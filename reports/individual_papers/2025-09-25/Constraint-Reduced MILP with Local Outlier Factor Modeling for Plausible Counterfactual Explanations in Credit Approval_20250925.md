---
keywords:
  - Counterfactual Explanation
  - Mixed-Integer Linear Programming
  - Local Outlier Factor
  - Support Vector Machine
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19504
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:36:27.179342",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Counterfactual Explanation",
    "Mixed-Integer Linear Programming",
    "Local Outlier Factor",
    "Support Vector Machine"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Counterfactual Explanation": 0.85,
    "Mixed-Integer Linear Programming": 0.78,
    "Local Outlier Factor": 0.81,
    "Support Vector Machine": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Counterfactual Explanation",
        "canonical": "Counterfactual Explanation",
        "aliases": [
          "CE"
        ],
        "category": "unique_technical",
        "rationale": "Counterfactual explanations are crucial for interpretability in machine learning, linking to broader discussions on model transparency.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      },
      {
        "surface": "Mixed-Integer Linear Programming",
        "canonical": "Mixed-Integer Linear Programming",
        "aliases": [
          "MILP"
        ],
        "category": "broad_technical",
        "rationale": "MILP is a fundamental optimization technique relevant across various computational fields, enhancing connectivity with optimization literature.",
        "novelty_score": 0.45,
        "connectivity_score": 0.87,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Local Outlier Factor",
        "canonical": "Local Outlier Factor",
        "aliases": [
          "LOF"
        ],
        "category": "specific_connectable",
        "rationale": "LOF is a key method in anomaly detection, connecting to broader topics in data science and machine learning.",
        "novelty_score": 0.58,
        "connectivity_score": 0.83,
        "specificity_score": 0.79,
        "link_intent_score": 0.81
      },
      {
        "surface": "Linear SVM Classifier",
        "canonical": "Support Vector Machine",
        "aliases": [
          "SVM",
          "Linear SVM"
        ],
        "category": "broad_technical",
        "rationale": "Support Vector Machines are a classic machine learning model, providing strong connectivity to foundational ML concepts.",
        "novelty_score": 0.4,
        "connectivity_score": 0.89,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "optimization model",
      "data distribution characteristics",
      "experimental results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Counterfactual Explanation",
      "resolved_canonical": "Counterfactual Explanation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Mixed-Integer Linear Programming",
      "resolved_canonical": "Mixed-Integer Linear Programming",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.87,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Local Outlier Factor",
      "resolved_canonical": "Local Outlier Factor",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.83,
        "specificity": 0.79,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Linear SVM Classifier",
      "resolved_canonical": "Support Vector Machine",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.89,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Constraint-Reduced MILP with Local Outlier Factor Modeling for Plausible Counterfactual Explanations in Credit Approval

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19504.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19504](https://arxiv.org/abs/2509.19504)

## 🔗 유사한 논문
- [[2025-09-24/Can LLMs Explain Themselves Counterfactually?_20250924|Can LLMs Explain Themselves Counterfactually?]] (82.9% similar)
- [[2025-09-24/LD-ViCE_ Latent Diffusion Model for Video Counterfactual Explanations_20250924|LD-ViCE: Latent Diffusion Model for Video Counterfactual Explanations]] (81.8% similar)
- [[2025-09-17/An Exhaustive DPLL Approach to Model Counting over Integer Linear Constraints with Simplification Techniques_20250917|An Exhaustive DPLL Approach to Model Counting over Integer Linear Constraints with Simplification Techniques]] (81.8% similar)
- [[2025-09-24/From latent factors to language_ a user study on LLM-generated explanations for an inherently interpretable matrix-based recommender system_20250924|From latent factors to language: a user study on LLM-generated explanations for an inherently interpretable matrix-based recommender system]] (81.3% similar)
- [[2025-09-23/Intrinsic Meets Extrinsic Fairness_ Assessing the Downstream Impact of Bias Mitigation in Large Language Models_20250923|Intrinsic Meets Extrinsic Fairness: Assessing the Downstream Impact of Bias Mitigation in Large Language Models]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Mixed-Integer Linear Programming|Mixed-Integer Linear Programming]], [[keywords/Support Vector Machine|Support Vector Machine]]
**🔗 Specific Connectable**: [[keywords/Local Outlier Factor|Local Outlier Factor]]
**⚡ Unique Technical**: [[keywords/Counterfactual Explanation|Counterfactual Explanation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19504v1 Announce Type: new 
Abstract: Counterfactual explanation (CE) is a widely used post-hoc method that provides individuals with actionable changes to alter an unfavorable prediction from a machine learning model. Plausible CE methods improve realism by considering data distribution characteristics, but their optimization models introduce a large number of constraints, leading to high computational cost. In this work, we revisit the DACE framework and propose a refined Mixed-Integer Linear Programming (MILP) formulation that significantly reduces the number of constraints in the local outlier factor (LOF) objective component. We also apply the method to a linear SVM classifier with standard scaler. The experimental results show that our approach achieves faster solving times while maintaining explanation quality. These results demonstrate the promise of more efficient LOF modeling in counterfactual explanation and data science applications.

## 📝 요약

이 논문은 반사실적 설명(Counterfactual Explanation, CE) 방법론의 효율성을 개선하는 연구를 다룹니다. 기존의 CE 방법은 데이터 분포를 고려하여 현실성을 높이지만, 많은 제약 조건으로 인해 계산 비용이 높습니다. 본 연구에서는 DACE 프레임워크를 재검토하고, 혼합 정수 선형 계획법(MILP)을 활용하여 지역 외부 요인(LOF) 목표 구성 요소의 제약 조건을 줄였습니다. 이를 통해 선형 SVM 분류기에 적용한 결과, 설명의 품질을 유지하면서도 계산 속도가 빨라졌습니다. 이 연구는 CE와 데이터 과학 응용에서 더 효율적인 LOF 모델링의 가능성을 보여줍니다.

## 🎯 주요 포인트

- 1. 반사실적 설명(CE)은 머신러닝 모델의 불리한 예측을 변경하기 위한 실행 가능한 변경 사항을 제공하는 사후 방법이다.
- 2. 현실성을 개선하는 CE 방법은 데이터 분포 특성을 고려하지만, 최적화 모델에 많은 제약 조건을 도입하여 높은 계산 비용을 초래한다.
- 3. 본 연구에서는 DACE 프레임워크를 재검토하고, 제약 조건 수를 크게 줄인 혼합 정수 선형 프로그래밍(MILP) 공식을 제안하였다.
- 4. 제안된 방법을 표준 스케일러를 사용한 선형 SVM 분류기에 적용하여 설명 품질을 유지하면서 해결 시간을 단축하였다.
- 5. 실험 결과는 반사실적 설명 및 데이터 과학 응용에서 더 효율적인 LOF 모델링의 가능성을 보여준다.


---

*Generated on 2025-09-25 16:36:27*