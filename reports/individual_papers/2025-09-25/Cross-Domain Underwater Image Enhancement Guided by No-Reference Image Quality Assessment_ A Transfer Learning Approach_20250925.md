---
keywords:
  - Transfer Learning
  - No-Reference Image Quality Assessment
  - Underwater Image Enhancement
  - Pearson Correlation Loss
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2503.17937
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:24:05.351167",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transfer Learning",
    "No-Reference Image Quality Assessment",
    "Underwater Image Enhancement",
    "Pearson Correlation Loss"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transfer Learning": 0.85,
    "No-Reference Image Quality Assessment": 0.78,
    "Underwater Image Enhancement": 0.77,
    "Pearson Correlation Loss": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transfer Learning",
        "canonical": "Transfer Learning",
        "aliases": [
          "Domain Adaptation"
        ],
        "category": "broad_technical",
        "rationale": "Transfer Learning is a key concept in the paper, facilitating cross-domain image enhancement, and is widely applicable across machine learning tasks.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "No-Reference Image Quality Assessment",
        "canonical": "No-Reference Image Quality Assessment",
        "aliases": [
          "NR-IQA"
        ],
        "category": "unique_technical",
        "rationale": "This technique is central to the paper's approach, guiding the enhancement process without relying on reference images.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Underwater Image Enhancement",
        "canonical": "Underwater Image Enhancement",
        "aliases": [
          "UIE"
        ],
        "category": "unique_technical",
        "rationale": "The paper focuses on improving this specific type of image enhancement, which is a niche but important area in computer vision.",
        "novelty_score": 0.7,
        "connectivity_score": 0.55,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Pearson Correlation Loss",
        "canonical": "Pearson Correlation Loss",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This loss function is introduced to mitigate overfitting, representing a novel application in the context of the paper.",
        "novelty_score": 0.68,
        "connectivity_score": 0.5,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "Single underwater image enhancement",
      "reconstruction loss",
      "confirmation bias"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Transfer Learning",
      "resolved_canonical": "Transfer Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "No-Reference Image Quality Assessment",
      "resolved_canonical": "No-Reference Image Quality Assessment",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Underwater Image Enhancement",
      "resolved_canonical": "Underwater Image Enhancement",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.55,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Pearson Correlation Loss",
      "resolved_canonical": "Pearson Correlation Loss",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.5,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Cross-Domain Underwater Image Enhancement Guided by No-Reference Image Quality Assessment: A Transfer Learning Approach

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2503.17937.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2503.17937](https://arxiv.org/abs/2503.17937)

## 🔗 유사한 논문
- [[2025-09-22/Sea-ing Through Scattered Rays_ Revisiting the Image Formation Model for Realistic Underwater Image Generation_20250922|Sea-ing Through Scattered Rays: Revisiting the Image Formation Model for Realistic Underwater Image Generation]] (82.4% similar)
- [[2025-09-23/Revisiting Vision Language Foundations for No-Reference Image Quality Assessment_20250923|Revisiting Vision Language Foundations for No-Reference Image Quality Assessment]] (82.1% similar)
- [[2025-09-18/Sea-ing Through Scattered Rays_ Revisiting the Image Formation Model for Realistic Underwater Image Generation_20250918|Sea-ing Through Scattered Rays: Revisiting the Image Formation Model for Realistic Underwater Image Generation]] (81.3% similar)
- [[2025-09-22/Self-Supervised Cross-Modal Learning for Image-to-Point Cloud Registration_20250922|Self-Supervised Cross-Modal Learning for Image-to-Point Cloud Registration]] (80.9% similar)
- [[2025-09-25/Optical Ocean Recipes_ Creating Realistic Datasets to Facilitate Underwater Vision Research_20250925|Optical Ocean Recipes: Creating Realistic Datasets to Facilitate Underwater Vision Research]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transfer Learning|Transfer Learning]]
**⚡ Unique Technical**: [[keywords/No-Reference Image Quality Assessment|No-Reference Image Quality Assessment]], [[keywords/Underwater Image Enhancement|Underwater Image Enhancement]], [[keywords/Pearson Correlation Loss|Pearson Correlation Loss]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.17937v2 Announce Type: replace 
Abstract: Single underwater image enhancement (UIE) is a challenging ill-posed problem, but its development is hindered by two major issues: (1) The labels in underwater reference datasets are pseudo labels, relying on these pseudo ground truths in supervised learning leads to domain discrepancy. (2) Underwater reference datasets are scarce, making training on such small datasets prone to overfitting and distribution shift. To address these challenges, we propose Trans-UIE, a transfer learning-based UIE model that captures the fundamental paradigms of UIE through pretraining and utilizes a dataset composed of both reference and non-reference datasets for fine-tuning. However, fine-tuning the model using only reconstruction loss may introduce confirmation bias. To mitigate this, our method leverages no-reference image quality assessment (NR-IQA) metrics from above-water scenes to guide the transfer learning process across domains while generating enhanced images with the style of the above-water image domain. Additionally, to reduce the risk of overfitting during the pretraining stage, we introduce Pearson correlation loss. Experimental results on both full-reference and no-reference underwater benchmark datasets demonstrate that Trans-UIE significantly outperforms state-of-the-art methods.

## 📝 요약

이 논문은 단일 수중 이미지 향상(UIE)의 문제를 해결하기 위해 Trans-UIE라는 전이 학습 기반 모델을 제안합니다. 주요 기여는 두 가지 문제를 해결하는 데 있습니다. 첫째, 수중 참조 데이터셋의 가짜 레이블로 인한 도메인 불일치를 해결하고, 둘째, 데이터셋 부족으로 인한 과적합 문제를 완화합니다. 이를 위해 참조 및 비참조 데이터셋을 활용한 미세 조정을 수행하며, 수중 이미지의 품질 향상을 위해 무참조 이미지 품질 평가(NR-IQA) 지표를 사용합니다. 또한, 과적합을 줄이기 위해 Pearson 상관 손실을 도입했습니다. 실험 결과, Trans-UIE는 최신 기법들보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 단일 수중 이미지 향상(UIE)은 잘 정의되지 않은 문제로, 수중 참조 데이터셋의 레이블이 의사 레이블이기 때문에 도메인 불일치가 발생합니다.
- 2. 수중 참조 데이터셋이 부족하여 작은 데이터셋으로 훈련할 경우 과적합 및 분포 이동의 위험이 있습니다.
- 3. Trans-UIE는 전이 학습 기반의 UIE 모델로, 참조 및 비참조 데이터셋을 활용하여 미세 조정하며, NR-IQA 지표를 사용하여 도메인 간 전이 학습을 안내합니다.
- 4. 모델의 미세 조정 시 재구성 손실만 사용하면 확인 편향이 발생할 수 있어 Pearson 상관 손실을 도입하여 과적합 위험을 줄입니다.
- 5. 실험 결과, Trans-UIE는 최신 방법들보다 수중 벤치마크 데이터셋에서 뛰어난 성능을 보입니다.


---

*Generated on 2025-09-26 09:24:05*