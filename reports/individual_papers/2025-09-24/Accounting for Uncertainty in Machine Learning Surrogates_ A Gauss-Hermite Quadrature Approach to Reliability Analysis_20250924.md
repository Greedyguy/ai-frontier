<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:46:29.853528",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Learning Surrogates",
    "Gauss-Hermite Quadrature",
    "Reliability Analysis",
    "Epistemic Uncertainty",
    "Aleatory Uncertainty"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Learning Surrogates": 0.75,
    "Gauss-Hermite Quadrature": 0.7,
    "Reliability Analysis": 0.65,
    "Epistemic Uncertainty": 0.8,
    "Aleatory Uncertainty": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Machine Learning Surrogates",
        "canonical": "Machine Learning Surrogates",
        "aliases": [
          "ML Surrogates"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's focus on replacing computational models and is specific to the study's context.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Gauss-Hermite Quadrature",
        "canonical": "Gauss-Hermite Quadrature",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a specific mathematical approach used in the study, crucial for the proposed method.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Reliability Analysis",
        "canonical": "Reliability Analysis",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "A key aspect of the study, linking to broader technical discussions on model reliability.",
        "novelty_score": 0.4,
        "connectivity_score": 0.7,
        "specificity_score": 0.6,
        "link_intent_score": 0.65
      },
      {
        "surface": "Epistemic Uncertainty",
        "canonical": "Epistemic Uncertainty",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This type of uncertainty is critical to the paper's discussion on model approximation errors.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Aleatory Uncertainty",
        "canonical": "Aleatory Uncertainty",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Understanding this uncertainty is essential for the paper's proposed method.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "example",
      "probability"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Machine Learning Surrogates",
      "resolved_canonical": "Machine Learning Surrogates",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Gauss-Hermite Quadrature",
      "resolved_canonical": "Gauss-Hermite Quadrature",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Reliability Analysis",
      "resolved_canonical": "Reliability Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.7,
        "specificity": 0.6,
        "link_intent": 0.65
      }
    },
    {
      "candidate_surface": "Epistemic Uncertainty",
      "resolved_canonical": "Epistemic Uncertainty",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Aleatory Uncertainty",
      "resolved_canonical": "Aleatory Uncertainty",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Accounting for Uncertainty in Machine Learning Surrogates: A Gauss-Hermite Quadrature Approach to Reliability Analysis

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18128.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18128](https://arxiv.org/abs/2509.18128)

## 🔗 유사한 논문
- [[2025-09-23/System-Level Uncertainty Quantification with Multiple Machine Learning Models_ A Theoretical Framework_20250923|System-Level Uncertainty Quantification with Multiple Machine Learning Models: A Theoretical Framework]] (85.2% similar)
- [[2025-09-22/Kernel Model Validation_ How To Do It, And Why You Should Care_20250922|Kernel Model Validation: How To Do It, And Why You Should Care]] (81.9% similar)
- [[2025-09-23/Loss-Complexity Landscape and Model Structure Functions_20250923|Loss-Complexity Landscape and Model Structure Functions]] (81.4% similar)
- [[2025-09-22/Boosting Active Learning with Knowledge Transfer_20250922|Boosting Active Learning with Knowledge Transfer]] (81.1% similar)
- [[2025-09-18/Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning_20250918|Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reliability Analysis|Reliability Analysis]]
**🔗 Specific Connectable**: [[keywords/Epistemic Uncertainty|Epistemic Uncertainty]], [[keywords/Aleatory Uncertainty|Aleatory Uncertainty]]
**⚡ Unique Technical**: [[keywords/Machine Learning Surrogates|Machine Learning Surrogates]], [[keywords/Gauss-Hermite Quadrature|Gauss-Hermite Quadrature]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18128v1 Announce Type: new 
Abstract: Machine learning surrogates are increasingly employed to replace expensive computational models for physics-based reliability analysis. However, their use introduces epistemic uncertainty from model approximation errors, which couples with aleatory uncertainty in model inputs, potentially compromising the accuracy of reliability predictions. This study proposes a Gauss-Hermite quadrature approach to decouple these nested uncertainties and enable more accurate reliability analysis. The method evaluates conditional failure probabilities under aleatory uncertainty using First and Second Order Reliability Methods and then integrates these probabilities across realizations of epistemic uncertainty. Three examples demonstrate that the proposed approach maintains computational efficiency while yielding more trustworthy predictions than traditional methods that ignore model uncertainty.

## 📝 요약

이 연구는 물리 기반 신뢰성 분석에서 고비용 계산 모델을 대체하기 위해 사용되는 기계 학습 대리 모델의 불확실성을 다루고자 합니다. 모델 근사 오류로 인한 인식적 불확실성과 입력의 변동성에 따른 불확실성을 분리하기 위해 Gauss-Hermite 사중적분 방법을 제안합니다. 이 방법은 1차 및 2차 신뢰성 방법을 사용하여 조건부 실패 확률을 평가하고, 이를 인식적 불확실성의 실현에 걸쳐 통합합니다. 세 가지 예제를 통해 제안된 접근법이 전통적인 방법보다 더 신뢰할 수 있는 예측을 제공하면서도 계산 효율성을 유지함을 보여줍니다.

## 🎯 주요 포인트

- 1. 기계 학습 대체 모델은 물리 기반 신뢰성 분석에서 비용이 많이 드는 계산 모델을 대체하기 위해 점점 더 많이 사용되고 있습니다.
- 2. 모델 근사 오류로 인한 인식론적 불확실성이 모델 입력의 우연적 불확실성과 결합되어 신뢰성 예측의 정확성을 저하시킬 수 있습니다.
- 3. 본 연구는 Gauss-Hermite 사중법을 제안하여 이러한 중첩된 불확실성을 분리하고 더 정확한 신뢰성 분석을 가능하게 합니다.
- 4. 제안된 방법은 우연적 불확실성 하에서의 조건부 고장 확률을 평가하고, 이를 인식론적 불확실성의 실현에 걸쳐 통합합니다.
- 5. 세 가지 예시를 통해 제안된 접근법이 모델 불확실성을 무시하는 전통적인 방법보다 더 신뢰할 수 있는 예측을 제공하면서도 계산 효율성을 유지함을 보여줍니다.


---

*Generated on 2025-09-24 14:46:29*