<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:29:36.071661",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Dual Data Alignment",
    "AI-Generated Image Detector",
    "Frequency-Level Misalignment",
    "Generative Reconstruction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Dual Data Alignment": 0.78,
    "AI-Generated Image Detector": 0.75,
    "Frequency-Level Misalignment": 0.7,
    "Generative Reconstruction": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Dual Data Alignment",
        "canonical": "Dual Data Alignment",
        "aliases": [
          "DDA"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel method for aligning both pixel and frequency domains, crucial for improving detector generalizability.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "AI-Generated Image Detector",
        "canonical": "AI-Generated Image Detector",
        "aliases": [
          "synthetic image detector"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's focus on improving detector performance across diverse datasets.",
        "novelty_score": 0.58,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Frequency-Level Misalignment",
        "canonical": "Frequency-Level Misalignment",
        "aliases": [
          "frequency misalignment"
        ],
        "category": "unique_technical",
        "rationale": "Highlights a specific challenge in image alignment that the proposed method addresses.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.7
      },
      {
        "surface": "Generative Reconstruction",
        "canonical": "Generative Reconstruction",
        "aliases": [
          "image reconstruction"
        ],
        "category": "specific_connectable",
        "rationale": "A common technique revisited in the paper for aligning real and synthetic images.",
        "novelty_score": 0.55,
        "connectivity_score": 0.68,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "dataset alignment",
      "JPEG compression",
      "performance degradation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Dual Data Alignment",
      "resolved_canonical": "Dual Data Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "AI-Generated Image Detector",
      "resolved_canonical": "AI-Generated Image Detector",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Frequency-Level Misalignment",
      "resolved_canonical": "Frequency-Level Misalignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Generative Reconstruction",
      "resolved_canonical": "Generative Reconstruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.68,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Dual Data Alignment Makes AI-Generated Image Detector Easier Generalizable

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2505.14359.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2505.14359](https://arxiv.org/abs/2505.14359)

## 🔗 유사한 논문
- [[2025-09-22/Efficient Multimodal Dataset Distillation via Generative Models_20250922|Efficient Multimodal Dataset Distillation via Generative Models]] (84.7% similar)
- [[2025-09-23/AlignedGen_ Aligning Style Across Generated Images_20250923|AlignedGen: Aligning Style Across Generated Images]] (84.2% similar)
- [[2025-09-23/Depth Edge Alignment Loss_ DEALing with Depth in Weakly Supervised Semantic Segmentation_20250923|Depth Edge Alignment Loss: DEALing with Depth in Weakly Supervised Semantic Segmentation]] (84.0% similar)
- [[2025-09-17/Class-invariant Test-Time Augmentation for Domain Generalization_20250917|Class-invariant Test-Time Augmentation for Domain Generalization]] (83.5% similar)
- [[2025-09-24/A Single Image Is All You Need_ Zero-Shot Anomaly Localization Without Training Data_20250924|A Single Image Is All You Need: Zero-Shot Anomaly Localization Without Training Data]] (83.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/AI-Generated Image Detector|AI-Generated Image Detector]], [[keywords/Generative Reconstruction|Generative Reconstruction]]
**⚡ Unique Technical**: [[keywords/Dual Data Alignment|Dual Data Alignment]], [[keywords/Frequency-Level Misalignment|Frequency-Level Misalignment]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.14359v5 Announce Type: replace 
Abstract: Existing detectors are often trained on biased datasets, leading to the possibility of overfitting on non-causal image attributes that are spuriously correlated with real/synthetic labels. While these biased features enhance performance on the training data, they result in substantial performance degradation when applied to unbiased datasets. One common solution is to perform dataset alignment through generative reconstruction, matching the semantic content between real and synthetic images. However, we revisit this approach and show that pixel-level alignment alone is insufficient. The reconstructed images still suffer from frequency-level misalignment, which can perpetuate spurious correlations. To illustrate, we observe that reconstruction models tend to restore the high-frequency details lost in real images (possibly due to JPEG compression), inadvertently creating a frequency-level misalignment, where synthetic images appear to have richer high-frequency content than real ones. This misalignment leads to models associating high-frequency features with synthetic labels, further reinforcing biased cues. To resolve this, we propose Dual Data Alignment (DDA), which aligns both the pixel and frequency domains. Moreover, we introduce two new test sets: DDA-COCO, containing DDA-aligned synthetic images for testing detector performance on the most aligned dataset, and EvalGEN, featuring the latest generative models for assessing detectors under new generative architectures such as visual auto-regressive generators. Finally, our extensive evaluations demonstrate that a detector trained exclusively on DDA-aligned MSCOCO could improve across 8 diverse benchmarks by a non-trivial margin, showing a +7.2% on in-the-wild benchmarks, highlighting the improved generalizability of unbiased detectors. Our code is available at: https://github.com/roy-ch/Dual-Data-Alignment.

## 📝 요약

이 논문은 기존 탐지기가 편향된 데이터셋으로 훈련되어 비본질적인 이미지 속성에 과적합되는 문제를 다룹니다. 이를 해결하기 위해 제안된 'Dual Data Alignment (DDA)' 방법론은 픽셀 및 주파수 도메인에서의 정렬을 통해 비본질적 상관관계를 줄입니다. 기존의 픽셀 정렬만으로는 주파수 불일치가 발생하여 편향을 강화할 수 있음을 지적하며, DDA는 이를 개선합니다. 또한, 새로운 테스트 세트인 DDA-COCO와 EvalGEN을 도입하여 다양한 생성 모델 하에서 탐지기의 성능을 평가합니다. DDA를 적용한 MSCOCO로 훈련된 탐지기는 8개의 다양한 벤치마크에서 성능이 향상되었으며, 특히 자연 환경 벤치마크에서 +7.2%의 성능 향상을 보여줍니다.

## 🎯 주요 포인트

- 1. 기존 탐지기는 편향된 데이터셋으로 훈련되어 비인과적 이미지 속성에 과적합될 가능성이 있습니다.
- 2. 픽셀 수준의 정렬만으로는 충분하지 않으며, 주파수 수준의 불일치가 발생할 수 있습니다.
- 3. Dual Data Alignment(DDA)는 픽셀과 주파수 도메인을 모두 정렬하여 편향된 단서를 해결합니다.
- 4. DDA-COCO와 EvalGEN 테스트 세트를 도입하여 새로운 생성 아키텍처에서 탐지기를 평가합니다.
- 5. DDA로 정렬된 MSCOCO로 훈련된 탐지기는 8개의 다양한 벤치마크에서 성능을 향상시켰습니다.


---

*Generated on 2025-09-24 16:29:36*