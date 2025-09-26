---
keywords:
  - Multimodal Learning
  - Prostate Cancer Prediction
  - Cox Regression
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.14051
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:32:27.399895",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Prostate Cancer Prediction",
    "Cox Regression"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.85,
    "Prostate Cancer Prediction": 0.78,
    "Cox Regression": 0.68
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "fused multi-modal embeddings",
        "canonical": "Multimodal Learning",
        "aliases": [
          "multi-modal embeddings",
          "fused embeddings"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Learning is a trending area that connects various data types, enhancing the prediction capabilities in medical applications.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.79,
        "link_intent_score": 0.85
      },
      {
        "surface": "prostate cancer biochemical recurrence prediction",
        "canonical": "Prostate Cancer Prediction",
        "aliases": [
          "PCa BCR prediction",
          "biochemical recurrence prediction"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application of predictive modeling in healthcare, focusing on a critical aspect of prostate cancer management.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Cox Proportional Hazard regressors",
        "canonical": "Cox Regression",
        "aliases": [
          "Cox model",
          "Proportional Hazard model"
        ],
        "category": "broad_technical",
        "rationale": "Cox Regression is a fundamental statistical technique for survival analysis, relevant across various research domains.",
        "novelty_score": 0.45,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.68
      }
    ],
    "ban_list_suggestions": [
      "radical prostatectomy",
      "prostate specific antigen"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "fused multi-modal embeddings",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.79,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "prostate cancer biochemical recurrence prediction",
      "resolved_canonical": "Prostate Cancer Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Cox Proportional Hazard regressors",
      "resolved_canonical": "Cox Regression",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.68
      }
    }
  ]
}
-->

# PROFUSEme: PROstate Cancer Biochemical Recurrence Prediction via FUSEd Multi-modal Embeddings

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.14051.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.14051](https://arxiv.org/abs/2509.14051)

## 🔗 유사한 논문
- [[2025-09-23/ME-Mamba_ Multi-Expert Mamba with Efficient Knowledge Capture and Fusion for Multimodal Survival Analysis_20250923|ME-Mamba: Multi-Expert Mamba with Efficient Knowledge Capture and Fusion for Multimodal Survival Analysis]] (82.1% similar)
- [[2025-09-22/NeuroRAD-FM_ A Foundation Model for Neuro-Oncology with Distributionally Robust Training_20250922|NeuroRAD-FM: A Foundation Model for Neuro-Oncology with Distributionally Robust Training]] (81.6% similar)
- [[2025-09-23/Block-Fused Attention-Driven Adaptively-Pooled ResNet Model for Improved Cervical Cancer Classification_20250923|Block-Fused Attention-Driven Adaptively-Pooled ResNet Model for Improved Cervical Cancer Classification]] (81.5% similar)
- [[2025-09-19/Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2_ Atypical Mitosis Classification_20250919|Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2: Atypical Mitosis Classification]] (81.4% similar)
- [[2025-09-23/Unified Multimodal Coherent Field_ Synchronous Semantic-Spatial-Vision Fusion for Brain Tumor Segmentation_20250923|Unified Multimodal Coherent Field: Synchronous Semantic-Spatial-Vision Fusion for Brain Tumor Segmentation]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Cox Regression|Cox Regression]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Prostate Cancer Prediction|Prostate Cancer Prediction]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14051v2 Announce Type: replace 
Abstract: Almost 30% of prostate cancer (PCa) patients undergoing radical prostatectomy (RP) experience biochemical recurrence (BCR), characterized by increased prostate specific antigen (PSA) and associated with increased mortality. Accurate early prediction of BCR, at the time of RP, would contribute to prompt adaptive clinical decision-making and improved patient outcomes. In this work, we propose prostate cancer BCR prediction via fused multi-modal embeddings (PROFUSEme), which learns cross-modal interactions of clinical, radiology, and pathology data, following an intermediate fusion configuration in combination with Cox Proportional Hazard regressors. Quantitative evaluation of our proposed approach reveals superior performance, when compared with late fusion configurations, yielding a mean C-index of 0.861 ($\sigma=0.112$) on the internal 5-fold nested cross-validation framework, and a C-index of 0.7107 on the hold out data of CHIMERA 2025 challenge validation leaderboard.

## 📝 요약

이 논문은 전립선암 환자의 생화학적 재발(BCR)을 조기에 예측하기 위한 방법을 제안합니다. 연구에서는 임상, 방사선, 병리 데이터를 융합하여 다중 모달 임베딩을 학습하는 PROFUSEme 모델을 개발했습니다. 이 모델은 Cox 비례 위험 회귀를 사용하여 중간 융합 구성에서 데이터를 분석합니다. 제안된 방법은 내부 5겹 교차 검증에서 평균 C-지수 0.861을 기록하며, CHIMERA 2025 챌린지 검증 데이터에서는 C-지수 0.7107을 보여 기존의 후기 융합 구성보다 우수한 성능을 나타냈습니다. 이를 통해 조기 예측이 가능해져 임상적 의사결정과 환자 결과 개선에 기여할 수 있습니다.

## 🎯 주요 포인트

- 1. 전립선암 환자의 생화학적 재발(BCR)을 조기에 예측하는 것은 임상적 의사 결정과 환자 결과 개선에 기여할 수 있습니다.
- 2. 본 연구에서는 임상, 방사선, 병리 데이터를 융합하여 BCR을 예측하는 다중 모달 임베딩 기법(PROFUSEme)을 제안합니다.
- 3. 제안된 방법은 Cox 비례 위험 회귀 모델과 결합하여 중간 융합 구성을 따르며, 후기 융합 구성보다 우수한 성능을 보입니다.
- 4. 내부 5겹 중첩 교차 검증에서 평균 C-지수 0.861을 기록하였으며, CHIMERA 2025 챌린지 검증 리더보드의 홀드 아웃 데이터에서 C-지수 0.7107을 기록했습니다.


---

*Generated on 2025-09-24 05:32:27*