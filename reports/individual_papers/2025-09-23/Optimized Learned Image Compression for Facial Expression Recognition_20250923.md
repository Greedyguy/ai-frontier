---
keywords:
  - Facial Expression Recognition
  - Image Compression
  - End-to-End Model
  - Custom Loss Function
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17262
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:48:10.880693",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Facial Expression Recognition",
    "Image Compression",
    "End-to-End Model",
    "Custom Loss Function"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Facial Expression Recognition": 0.78,
    "Image Compression": 0.7,
    "End-to-End Model": 0.75,
    "Custom Loss Function": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Facial Expression Recognition",
        "canonical": "Facial Expression Recognition",
        "aliases": [
          "FER"
        ],
        "category": "unique_technical",
        "rationale": "Facial Expression Recognition is a specific application area that connects to both computer vision and emotion analysis.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Image Compression",
        "canonical": "Image Compression",
        "aliases": [
          "Visual Data Compression"
        ],
        "category": "broad_technical",
        "rationale": "Image Compression is a fundamental concept in computer vision and data management, linking to storage and transmission efficiency.",
        "novelty_score": 0.55,
        "connectivity_score": 0.72,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      },
      {
        "surface": "End-to-End Model",
        "canonical": "End-to-End Model",
        "aliases": [
          "E2E Model"
        ],
        "category": "unique_technical",
        "rationale": "End-to-End Models are crucial for understanding integrated systems in machine learning, especially in tasks requiring holistic optimization.",
        "novelty_score": 0.62,
        "connectivity_score": 0.77,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Custom Loss Function",
        "canonical": "Custom Loss Function",
        "aliases": [
          "Tailored Loss Function"
        ],
        "category": "unique_technical",
        "rationale": "Custom Loss Functions are pivotal in optimizing machine learning models for specific tasks, enhancing both performance and adaptability.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "Efficient Data Compression",
      "Feature Degradation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Facial Expression Recognition",
      "resolved_canonical": "Facial Expression Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Image Compression",
      "resolved_canonical": "Image Compression",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.72,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "End-to-End Model",
      "resolved_canonical": "End-to-End Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.62,
        "connectivity": 0.77,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Custom Loss Function",
      "resolved_canonical": "Custom Loss Function",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Optimized Learned Image Compression for Facial Expression Recognition

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17262.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17262](https://arxiv.org/abs/2509.17262)

## 🔗 유사한 논문
- [[2025-09-23/Unified Framework for Pre-trained Neural Network Compression via Decomposition and Optimized Rank Selection_20250923|Unified Framework for Pre-trained Neural Network Compression via Decomposition and Optimized Rank Selection]] (81.9% similar)
- [[2025-09-23/Interpretability-Aware Pruning for Efficient Medical Image Analysis_20250923|Interpretability-Aware Pruning for Efficient Medical Image Analysis]] (81.8% similar)
- [[2025-09-19/Controllable Localized Face Anonymization Via Diffusion Inpainting_20250919|Controllable Localized Face Anonymization Via Diffusion Inpainting]] (81.6% similar)
- [[2025-09-19/HPGN_ Hybrid Priors-Guided Network for Compressed Low-Light Image Enhancement_20250919|HPGN: Hybrid Priors-Guided Network for Compressed Low-Light Image Enhancement]] (81.4% similar)
- [[2025-09-22/Prostate Capsule Segmentation from Micro-Ultrasound Images using Adaptive Focal Loss_20250922|Prostate Capsule Segmentation from Micro-Ultrasound Images using Adaptive Focal Loss]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Image Compression|Image Compression]]
**⚡ Unique Technical**: [[keywords/Facial Expression Recognition|Facial Expression Recognition]], [[keywords/End-to-End Model|End-to-End Model]], [[keywords/Custom Loss Function|Custom Loss Function]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17262v1 Announce Type: new 
Abstract: Efficient data compression is crucial for the storage and transmission of visual data. However, in facial expression recognition (FER) tasks, lossy compression often leads to feature degradation and reduced accuracy. To address these challenges, this study proposes an end-to-end model designed to preserve critical features and enhance both compression and recognition performance. A custom loss function is introduced to optimize the model, tailored to balance compression and recognition performance effectively. This study also examines the influence of varying loss term weights on this balance. Experimental results indicate that fine-tuning the compression model alone improves classification accuracy by 0.71% and compression efficiency by 49.32%, while joint optimization achieves significant gains of 4.04% in accuracy and 89.12% in efficiency. Moreover, the findings demonstrate that the jointly optimized classification model maintains high accuracy on both compressed and uncompressed data, while the compression model reliably preserves image details, even at high compression rates.

## 📝 요약

이 연구는 얼굴 표정 인식(FER) 작업에서 손실 압축으로 인한 특징 손실과 정확도 저하 문제를 해결하기 위해, 중요한 특징을 보존하면서 압축 및 인식 성능을 향상시키는 종단 간 모델을 제안합니다. 맞춤형 손실 함수를 도입하여 압축과 인식 성능 간의 균형을 최적화하였으며, 손실 항목 가중치의 영향을 분석했습니다. 실험 결과, 압축 모델의 미세 조정만으로도 분류 정확도가 0.71% 향상되고 압축 효율성이 49.32% 증가했으며, 공동 최적화 시 정확도는 4.04%, 효율성은 89.12% 크게 향상되었습니다. 또한, 공동 최적화된 분류 모델은 압축 및 비압축 데이터 모두에서 높은 정확도를 유지하고, 압축 모델은 높은 압축률에서도 이미지 세부 사항을 잘 보존함을 보여줍니다.

## 🎯 주요 포인트

- 1. 얼굴 표정 인식 작업에서 손실 압축은 특징 저하와 정확도 감소를 초래할 수 있다.
- 2. 본 연구는 중요한 특징을 보존하고 압축 및 인식 성능을 향상시키기 위한 엔드 투 엔드 모델을 제안한다.
- 3. 커스텀 손실 함수를 도입하여 압축과 인식 성능의 균형을 효과적으로 최적화한다.
- 4. 실험 결과, 압축 모델의 미세 조정만으로도 분류 정확도가 0.71% 향상되고 압축 효율성이 49.32% 증가한다.
- 5. 공동 최적화는 정확도 4.04% 및 효율성 89.12%의 상당한 향상을 달성하며, 압축 모델은 높은 압축률에서도 이미지 세부 사항을 잘 보존한다.


---

*Generated on 2025-09-24 04:48:10*