---
keywords:
  - Machine Learning
  - Model Uncertainty
  - Input Uncertainty
  - Joint Distribution
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16663
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:12:34.317115",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Learning",
    "Model Uncertainty",
    "Input Uncertainty",
    "Joint Distribution"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Learning": 0.8,
    "Model Uncertainty": 0.7,
    "Input Uncertainty": 0.65,
    "Joint Distribution": 0.6
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Machine Learning Models",
        "canonical": "Machine Learning",
        "aliases": [
          "ML Models",
          "Machine Learning Systems"
        ],
        "category": "broad_technical",
        "rationale": "Machine Learning is a foundational concept that connects to a wide range of technical topics.",
        "novelty_score": 0.2,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.8
      },
      {
        "surface": "Model Uncertainty",
        "canonical": "Model Uncertainty",
        "aliases": [
          "Uncertainty Quantification",
          "Prediction Uncertainty"
        ],
        "category": "unique_technical",
        "rationale": "Model Uncertainty is crucial for understanding and improving ML model predictions.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Input Uncertainty",
        "canonical": "Input Uncertainty",
        "aliases": [
          "Data Uncertainty",
          "Input Variability"
        ],
        "category": "unique_technical",
        "rationale": "Input Uncertainty is important for assessing the reliability of ML model inputs.",
        "novelty_score": 0.65,
        "connectivity_score": 0.55,
        "specificity_score": 0.75,
        "link_intent_score": 0.65
      },
      {
        "surface": "Joint Distribution",
        "canonical": "Joint Distribution",
        "aliases": [
          "Joint Probability Distribution",
          "Multivariate Distribution"
        ],
        "category": "unique_technical",
        "rationale": "Understanding joint distributions is key to modeling dependencies in ML predictions.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.7,
        "link_intent_score": 0.6
      }
    ],
    "ban_list_suggestions": [
      "theoretical framework",
      "decision-making",
      "design"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Machine Learning Models",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.2,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Model Uncertainty",
      "resolved_canonical": "Model Uncertainty",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Input Uncertainty",
      "resolved_canonical": "Input Uncertainty",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.55,
        "specificity": 0.75,
        "link_intent": 0.65
      }
    },
    {
      "candidate_surface": "Joint Distribution",
      "resolved_canonical": "Joint Distribution",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.7,
        "link_intent": 0.6
      }
    }
  ]
}
-->

# System-Level Uncertainty Quantification with Multiple Machine Learning Models: A Theoretical Framework

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16663.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16663](https://arxiv.org/abs/2509.16663)

## 🔗 유사한 논문
- [[2025-09-18/Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning_20250918|Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning]] (83.1% similar)
- [[2025-09-22/Quantifying Uncertainty in Natural Language Explanations of Large Language Models for Question Answering_20250922|Quantifying Uncertainty in Natural Language Explanations of Large Language Models for Question Answering]] (82.7% similar)
- [[2025-09-22/Boosting Active Learning with Knowledge Transfer_20250922|Boosting Active Learning with Knowledge Transfer]] (82.0% similar)
- [[2025-09-23/Both Text and Images Leaked! A Systematic Analysis of Data Contamination in Multimodal LLM_20250923|Both Text and Images Leaked! A Systematic Analysis of Data Contamination in Multimodal LLM]] (81.9% similar)
- [[2025-09-23/Causal Fuzzing for Verifying Machine Unlearning_20250923|Causal Fuzzing for Verifying Machine Unlearning]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**⚡ Unique Technical**: [[keywords/Model Uncertainty|Model Uncertainty]], [[keywords/Input Uncertainty|Input Uncertainty]], [[keywords/Joint Distribution|Joint Distribution]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16663v1 Announce Type: cross 
Abstract: ML models have errors when used for predictions. The errors are unknown but can be quantified by model uncertainty. When multiple ML models are trained using the same training points, their model uncertainties may be statistically dependent. In reality, model inputs are also random with input uncertainty. The effects of these types of uncertainty must be considered in decision-making and design. This study develops a theoretical framework that generates the joint distribution of multiple ML predictions given the joint distribution of model uncertainties and the joint distribution of model inputs. The strategy is to decouple the coupling between the two types of uncertainty and transform them as independent random variables. The framework lays a foundation for numerical algorithm development for various specific applications.

## 📝 요약

이 연구는 다중 기계 학습(ML) 모델의 예측 시 발생하는 오류와 관련된 불확실성을 다루는 이론적 프레임워크를 제시합니다. 모델 불확실성과 입력 불확실성이 통계적으로 의존적일 수 있음을 고려하여, 이 두 불확실성을 독립적인 확률 변수로 변환하는 전략을 사용합니다. 이를 통해 다중 ML 예측의 결합 분포를 생성하는 방법을 개발하였으며, 이는 다양한 응용 분야에서 수치 알고리즘 개발의 기초를 제공합니다. 주요 기여는 불확실성의 영향을 고려한 의사결정 및 설계에 대한 새로운 접근법을 제시한 것입니다.

## 🎯 주요 포인트

- 1. ML 모델의 예측 오류는 모델 불확실성으로 정량화할 수 있다.
- 2. 동일한 학습 데이터를 사용한 여러 ML 모델의 불확실성은 통계적으로 의존적일 수 있다.
- 3. 모델 입력도 불확실성을 가지며, 이는 의사결정 및 설계에 고려되어야 한다.
- 4. 본 연구는 모델 불확실성과 입력 불확실성의 결합을 독립적인 확률 변수로 변환하는 이론적 프레임워크를 개발하였다.
- 5. 이 프레임워크는 다양한 특정 응용을 위한 수치 알고리즘 개발의 기초를 마련한다.


---

*Generated on 2025-09-24 02:12:34*