---
keywords:
  - Uncertainty Estimation
  - Evidential Segmentation
  - Self-supervised Learning
  - Out-of-Distribution Generalization
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17098
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:19:30.899533",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Uncertainty Estimation",
    "Evidential Segmentation",
    "Self-supervised Learning",
    "Out-of-Distribution Generalization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Uncertainty Estimation": 0.75,
    "Evidential Segmentation": 0.7,
    "Self-supervised Learning": 0.8,
    "Out-of-Distribution Generalization": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Uncertainty Estimation",
        "canonical": "Uncertainty Estimation",
        "aliases": [
          "Uncertainty Quantification"
        ],
        "category": "unique_technical",
        "rationale": "Key focus of the paper, enhancing interpretability and robustness in segmentation.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Evidential Segmentation",
        "canonical": "Evidential Segmentation",
        "aliases": [
          "Evidential Image Segmentation"
        ],
        "category": "unique_technical",
        "rationale": "Central method proposed in the paper, distinct from traditional segmentation techniques.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Self-supervised Approach",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "Self-supervised Method"
        ],
        "category": "specific_connectable",
        "rationale": "The paper introduces a self-supervised method for uncertainty guidance, linking to existing concepts.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Out-of-Distribution Scenarios",
        "canonical": "Out-of-Distribution Generalization",
        "aliases": [
          "OOD Scenarios"
        ],
        "category": "specific_connectable",
        "rationale": "Addresses robustness in novel scenarios, a key challenge in machine learning.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
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
      "candidate_surface": "Uncertainty Estimation",
      "resolved_canonical": "Uncertainty Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Evidential Segmentation",
      "resolved_canonical": "Evidential Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Self-supervised Approach",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Out-of-Distribution Scenarios",
      "resolved_canonical": "Out-of-Distribution Generalization",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Uncertainty-Supervised Interpretable and Robust Evidential Segmentation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17098.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17098](https://arxiv.org/abs/2509.17098)

## 🔗 유사한 논문
- [[2025-09-22/Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images_20250922|Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images]] (82.1% similar)
- [[2025-09-22/Towards Sharper Object Boundaries in Self-Supervised Depth Estimation_20250922|Towards Sharper Object Boundaries in Self-Supervised Depth Estimation]] (81.9% similar)
- [[2025-09-23/Ambiguous Medical Image Segmentation Using Diffusion Schr\"{o}dinger Bridge_20250923|Ambiguous Medical Image Segmentation Using Diffusion Schr\"{o}dinger Bridge]] (81.8% similar)
- [[2025-09-18/Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning_20250918|Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning]] (81.4% similar)
- [[2025-09-22/Boosting Active Learning with Knowledge Transfer_20250922|Boosting Active Learning with Knowledge Transfer]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]], [[keywords/Out-of-Distribution Generalization|Out-of-Distribution Generalization]]
**⚡ Unique Technical**: [[keywords/Uncertainty Estimation|Uncertainty Estimation]], [[keywords/Evidential Segmentation|Evidential Segmentation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17098v1 Announce Type: cross 
Abstract: Uncertainty estimation has been widely studied in medical image segmentation as a tool to provide reliability, particularly in deep learning approaches. However, previous methods generally lack effective supervision in uncertainty estimation, leading to low interpretability and robustness of the predictions. In this work, we propose a self-supervised approach to guide the learning of uncertainty. Specifically, we introduce three principles about the relationships between the uncertainty and the image gradients around boundaries and noise. Based on these principles, two uncertainty supervision losses are designed. These losses enhance the alignment between model predictions and human interpretation. Accordingly, we introduce novel quantitative metrics for evaluating the interpretability and robustness of uncertainty. Experimental results demonstrate that compared to state-of-the-art approaches, the proposed method can achieve competitive segmentation performance and superior results in out-of-distribution (OOD) scenarios while significantly improving the interpretability and robustness of uncertainty estimation. Code is available via https://github.com/suiannaius/SURE.

## 📝 요약

이 논문은 의료 영상 분할에서 불확실성 추정을 개선하기 위한 자기 지도 학습 방법을 제안합니다. 기존 방법들은 불확실성 추정에 효과적인 감독이 부족하여 예측의 해석 가능성과 견고성이 낮았습니다. 본 연구에서는 이미지 경계와 노이즈 주변의 불확실성과 이미지 그래디언트 간의 관계에 관한 세 가지 원칙을 도입하고, 이를 기반으로 두 가지 불확실성 감독 손실을 설계했습니다. 이러한 손실은 모델 예측과 인간 해석 간의 정렬을 강화합니다. 또한, 불확실성의 해석 가능성과 견고성을 평가하기 위한 새로운 정량적 지표를 제안했습니다. 실험 결과, 제안된 방법이 최첨단 접근법과 비교하여 경쟁력 있는 분할 성능을 보이며, 분포 외 시나리오에서 우수한 결과를 나타내고, 불확실성 추정의 해석 가능성과 견고성을 크게 향상시킴을 보여줍니다. 코드: https://github.com/suiannaius/SURE.

## 🎯 주요 포인트

- 1. 본 연구는 의료 영상 분할에서 불확실성 추정을 위한 자기 지도 학습 접근법을 제안합니다.
- 2. 이미지 경계와 노이즈 주변의 불확실성과 관련된 세 가지 원칙을 도입하여 불확실성 학습을 지도합니다.
- 3. 제안된 불확실성 지도 손실은 모델 예측과 인간 해석 간의 정렬을 강화합니다.
- 4. 새로운 정량적 지표를 통해 불확실성의 해석 가능성과 견고성을 평가합니다.
- 5. 제안된 방법은 최첨단 접근법과 비교하여 경쟁력 있는 분할 성능과 OOD 시나리오에서 우수한 결과를 보여줍니다.


---

*Generated on 2025-09-24 02:19:30*