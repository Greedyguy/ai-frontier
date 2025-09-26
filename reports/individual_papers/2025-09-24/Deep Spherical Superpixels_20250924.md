<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:26:10.133549",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Spherical Superpixels",
    "Spherical Convolutional Neural Networks",
    "Differentiable K-means Clustering",
    "Data Augmentation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Spherical Superpixels": 0.8,
    "Spherical Convolutional Neural Networks": 0.78,
    "Differentiable K-means Clustering": 0.72,
    "Data Augmentation": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Spherical Superpixels",
        "canonical": "Deep Spherical Superpixels",
        "aliases": [
          "DSS"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach specific to spherical image segmentation, enhancing connectivity in omnidirectional imaging research.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "spherical CNN architectures",
        "canonical": "Spherical Convolutional Neural Networks",
        "aliases": [
          "spherical CNNs"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to the broader field of CNN adaptations for non-Euclidean domains, relevant for spherical data processing.",
        "novelty_score": 0.7,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "differentiable K-means clustering",
        "canonical": "Differentiable K-means Clustering",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Represents an innovative adaptation of traditional clustering methods for deep learning frameworks.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "data augmentation techniques",
        "canonical": "Data Augmentation",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Essential for improving model training, especially in limited data scenarios, linking to general machine learning practices.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "superpixel segmentation",
      "omnidirectional images",
      "segmentation performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep Spherical Superpixels",
      "resolved_canonical": "Deep Spherical Superpixels",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "spherical CNN architectures",
      "resolved_canonical": "Spherical Convolutional Neural Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "differentiable K-means clustering",
      "resolved_canonical": "Differentiable K-means Clustering",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "data augmentation techniques",
      "resolved_canonical": "Data Augmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Deep Spherical Superpixels

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2407.17354.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2407.17354](https://arxiv.org/abs/2407.17354)

## 🔗 유사한 논문
- [[2025-09-23/Superpixel Graph Contrastive Clustering with Semantic-Invariant Augmentations for Hyperspectral Images_20250923|Superpixel Graph Contrastive Clustering with Semantic-Invariant Augmentations for Hyperspectral Images]] (82.5% similar)
- [[2025-09-24/A Single Image Is All You Need_ Zero-Shot Anomaly Localization Without Training Data_20250924|A Single Image Is All You Need: Zero-Shot Anomaly Localization Without Training Data]] (81.9% similar)
- [[2025-09-24/Reconstruction of Optical Coherence Tomography Images from Wavelength-space Using Deep-learning_20250924|Reconstruction of Optical Coherence Tomography Images from Wavelength-space Using Deep-learning]] (81.2% similar)
- [[2025-09-23/3D Cell Oversegmentation Correction via Geo-Wasserstein Divergence_20250923|3D Cell Oversegmentation Correction via Geo-Wasserstein Divergence]] (81.0% similar)
- [[2025-09-24/DeblurSplat_ SfM-free 3D Gaussian Splatting with Event Camera for Robust Deblurring_20250924|DeblurSplat: SfM-free 3D Gaussian Splatting with Event Camera for Robust Deblurring]] (81.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Data Augmentation|Data Augmentation]]
**🔗 Specific Connectable**: [[keywords/Spherical Convolutional Neural Networks|Spherical Convolutional Neural Networks]]
**⚡ Unique Technical**: [[keywords/Deep Spherical Superpixels|Deep Spherical Superpixels]], [[keywords/Differentiable K-means Clustering|Differentiable K-means Clustering]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2407.17354v2 Announce Type: replace 
Abstract: Over the years, the use of superpixel segmentation has become very popular in various applications, serving as a preprocessing step to reduce data size by adapting to the content of the image, regardless of its semantic content. While the superpixel segmentation of standard planar images, captured with a 90{\deg} field of view, has been extensively studied, there has been limited focus on dedicated methods to omnidirectional or spherical images, captured with a 360{\deg} field of view. In this study, we introduce the first deep learning-based superpixel segmentation approach tailored for omnidirectional images called DSS (for Deep Spherical Superpixels). Our methodology leverages on spherical CNN architectures and the differentiable K-means clustering paradigm for superpixels, to generate superpixels that follow the spherical geometry. Additionally, we propose to use data augmentation techniques specifically designed for 360{\deg} images, enabling our model to efficiently learn from a limited set of annotated omnidirectional data. Our extensive validation across two datasets demonstrates that taking into account the inherent circular geometry of such images into our framework improves the segmentation performance over traditional and deep learning-based superpixel methods. Our code is available online.

## 📝 요약

이 연구는 360도 전방위 이미지에 적합한 최초의 딥러닝 기반 초픽셀 분할 방법인 DSS(Deep Spherical Superpixels)를 제안합니다. 기존의 평면 이미지 초픽셀 분할에 비해, 구형 CNN 아키텍처와 미분 가능한 K-평균 클러스터링을 활용하여 구형 기하학을 따르는 초픽셀을 생성합니다. 또한, 360도 이미지에 특화된 데이터 증강 기법을 도입하여 제한된 주석 데이터로부터 효율적으로 학습할 수 있도록 합니다. 두 개의 데이터셋에 대한 검증 결과, 이러한 접근 방식이 전통적 및 기존 딥러닝 기반 방법보다 우수한 성능을 보였습니다. 연구의 코드는 온라인에서 제공됩니다.

## 🎯 주요 포인트

- 1. 본 연구는 360도 전방위 이미지를 위한 최초의 딥러닝 기반 초픽셀 분할 접근법인 DSS(Deep Spherical Superpixels)를 소개합니다.
- 2. DSS는 구형 CNN 아키텍처와 차별 가능한 K-평균 클러스터링을 활용하여 구형 기하학을 따르는 초픽셀을 생성합니다.
- 3. 360도 이미지에 특화된 데이터 증강 기법을 제안하여 제한된 주석 데이터로부터 효율적으로 학습할 수 있도록 합니다.
- 4. 두 개의 데이터셋에 걸친 광범위한 검증을 통해 구형 기하학을 고려한 프레임워크가 기존의 전통적 및 딥러닝 기반 초픽셀 방법보다 성능이 향상됨을 입증했습니다.
- 5. 연구의 코드는 온라인에서 공개되어 있습니다.


---

*Generated on 2025-09-24 16:26:10*