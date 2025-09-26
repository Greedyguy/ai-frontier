---
keywords:
  - Otsu Thresholding
  - Bisection Method
  - Image Segmentation
  - Between-Class Variance
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.16179
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:30:36.359238",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Otsu Thresholding",
    "Bisection Method",
    "Image Segmentation",
    "Between-Class Variance"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Otsu Thresholding": 0.82,
    "Bisection Method": 0.78,
    "Image Segmentation": 0.8,
    "Between-Class Variance": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Otsu thresholding",
        "canonical": "Otsu Thresholding",
        "aliases": [
          "Otsu's method",
          "Otsu algorithm"
        ],
        "category": "unique_technical",
        "rationale": "A fundamental technique in image segmentation, crucial for linking to image processing topics.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "bisection method",
        "canonical": "Bisection Method",
        "aliases": [
          "bisection algorithm"
        ],
        "category": "unique_technical",
        "rationale": "An optimization technique that enhances computational efficiency, relevant for algorithmic discussions.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "image segmentation",
        "canonical": "Image Segmentation",
        "aliases": [
          "segmentation"
        ],
        "category": "broad_technical",
        "rationale": "A key application area in computer vision, facilitating connections to related image processing fields.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "between-class variance",
        "canonical": "Between-Class Variance",
        "aliases": [
          "inter-class variance"
        ],
        "category": "unique_technical",
        "rationale": "A critical concept in thresholding algorithms, connecting to statistical analysis in image processing.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "computational efficiency",
      "algorithmic iterations"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Otsu thresholding",
      "resolved_canonical": "Otsu Thresholding",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "bisection method",
      "resolved_canonical": "Bisection Method",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "image segmentation",
      "resolved_canonical": "Image Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "between-class variance",
      "resolved_canonical": "Between-Class Variance",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Fast OTSU Thresholding Using Bisection Method

**Korean Title:** 이분법을 이용한 빠른 OTSU 임계값 설정

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16179.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.16179](https://arxiv.org/abs/2509.16179)

## 🔗 유사한 논문
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (79.6% similar)
- [[2025-09-22/scSplit_ Bringing Severity Cognizance to Image Decomposition in Fluorescence Microscopy_20250922|scSplit: Bringing Severity Cognizance to Image Decomposition in Fluorescence Microscopy]] (79.3% similar)
- [[2025-09-19/DiffCut_ Catalyzing Zero-Shot Semantic Segmentation with Diffusion Features and Recursive Normalized Cut_20250919|DiffCut: Catalyzing Zero-Shot Semantic Segmentation with Diffusion Features and Recursive Normalized Cut]] (78.8% similar)
- [[2025-09-18/Semi-MoE_ Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation_20250918|Semi-MoE: Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation]] (78.4% similar)
- [[2025-09-18/A Novel Compression Framework for YOLOv8_ Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation_20250918|A Novel Compression Framework for YOLOv8: Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation]] (78.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Image Segmentation|Image Segmentation]]
**⚡ Unique Technical**: [[keywords/Otsu Thresholding|Otsu Thresholding]], [[keywords/Bisection Method|Bisection Method]], [[keywords/Between-Class Variance|Between-Class Variance]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16179v1 Announce Type: cross 
Abstract: The Otsu thresholding algorithm represents a fundamental technique in image segmentation, yet its computational efficiency is severely limited by exhaustive search requirements across all possible threshold values. This work presents an optimized implementation that leverages the bisection method to exploit the unimodal characteristics of the between-class variance function. Our approach reduces the computational complexity from O(L) to O(log L) evaluations while preserving segmentation accuracy. Experimental validation on 48 standard test images demonstrates a 91.63% reduction in variance computations and 97.21% reduction in algorithmic iterations compared to conventional exhaustive search. The bisection method achieves exact threshold matches in 66.67% of test cases, with 95.83% exhibiting deviations within 5 gray levels. The algorithm maintains universal convergence within theoretical logarithmic bounds while providing deterministic performance guarantees suitable for real-time applications. This optimization addresses critical computational bottlenecks in large-scale image processing systems without compromising the theoretical foundations or segmentation quality of the original Otsu method.

## 🔍 Abstract (한글 번역)

arXiv:2509.16179v1 발표 유형: 교차  
초록: 오츠 임계값 알고리즘은 이미지 분할에서 기본적인 기법을 나타내지만, 모든 가능한 임계값을 대상으로 한 철저한 탐색 요구로 인해 계산 효율성이 심각하게 제한됩니다. 본 연구는 클래스 간 분산 함수의 단봉 특성을 활용하기 위해 이분법을 활용한 최적화된 구현을 제시합니다. 우리의 접근 방식은 분할 정확도를 유지하면서 계산 복잡성을 O(L)에서 O(log L) 평가로 줄입니다. 48개의 표준 테스트 이미지에 대한 실험적 검증 결과, 기존의 철저한 탐색과 비교하여 분산 계산이 91.63% 감소하고 알고리즘 반복이 97.21% 감소함을 보여줍니다. 이분법은 테스트 사례의 66.67%에서 정확한 임계값 일치를 달성했으며, 95.83%는 5 그레이 레벨 이내의 편차를 보였습니다. 알고리즘은 이론적 로그 경계 내에서 보편적인 수렴성을 유지하면서 실시간 응용에 적합한 결정론적 성능 보장을 제공합니다. 이 최적화는 원래 오츠 방법의 이론적 기초나 분할 품질을 손상시키지 않으면서 대규모 이미지 처리 시스템의 중요한 계산 병목 현상을 해결합니다.

## 📝 요약

이 논문은 이미지 분할의 기본 기법인 Otsu 임계값 알고리즘의 계산 효율성을 개선한 연구를 소개합니다. 기존의 모든 가능한 임계값을 탐색하는 방식에서 벗어나, 본 연구는 클래스 간 분산 함수의 단봉 특성을 활용한 이분법을 적용하여 계산 복잡도를 O(L)에서 O(log L)로 줄였습니다. 48개의 표준 테스트 이미지 실험 결과, 분산 계산이 91.63% 감소하고 알고리즘 반복이 97.21% 감소했으며, 66.67%의 테스트 케이스에서 정확한 임계값을 찾았습니다. 이 방법은 대규모 이미지 처리 시스템에서 이론적 로그 범위 내에서 보편적인 수렴성을 유지하면서 실시간 응용에 적합한 성능을 보장합니다.

## 🎯 주요 포인트

- 1. Otsu 알고리즘의 계산 효율성을 개선하기 위해 이분법을 활용하여 계산 복잡도를 O(L)에서 O(log L)로 줄였습니다.
- 2. 실험 결과, 기존의 완전 탐색에 비해 분산 계산이 91.63% 감소하고 알고리즘 반복이 97.21% 감소했습니다.
- 3. 이분법을 사용한 최적화는 테스트 이미지의 66.67%에서 정확한 임계값을 찾았으며, 95.83%는 5 그레이 레벨 이내의 편차를 보였습니다.
- 4. 이 알고리즘은 이론적 로그 범위 내에서 보편적인 수렴성을 유지하며 실시간 응용에 적합한 성능 보장을 제공합니다.
- 5. 대규모 이미지 처리 시스템에서 Otsu 방법의 이론적 기초나 분할 품질을 손상시키지 않으면서 중요한 계산 병목 현상을 해결합니다.


---

*Generated on 2025-09-23 09:30:36*