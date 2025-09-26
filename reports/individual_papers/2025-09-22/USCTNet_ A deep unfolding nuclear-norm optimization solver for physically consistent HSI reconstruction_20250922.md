---
keywords:
  - Hyperspectral Image Reconstruction
  - Deep Unfolding Solver
  - Nuclear Norm Optimization
  - Camera Spectral Sensitivity
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.10651
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:39:54.355472",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Hyperspectral Image Reconstruction",
    "Deep Unfolding Solver",
    "Nuclear Norm Optimization",
    "Camera Spectral Sensitivity"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Hyperspectral Image Reconstruction": 0.78,
    "Deep Unfolding Solver": 0.82,
    "Nuclear Norm Optimization": 0.8,
    "Camera Spectral Sensitivity": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "hyperspectral image reconstruction",
        "canonical": "Hyperspectral Image Reconstruction",
        "aliases": [
          "HSI reconstruction"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific task in computer vision that involves reconstructing detailed spectral information from limited data, which is central to the paper's contribution.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "deep unfolding solver",
        "canonical": "Deep Unfolding Solver",
        "aliases": [
          "unfolding network"
        ],
        "category": "unique_technical",
        "rationale": "The deep unfolding solver is a novel approach that combines deep learning with optimization techniques, which is a key innovation in the paper.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "nuclear norm optimization",
        "canonical": "Nuclear Norm Optimization",
        "aliases": [
          "nuclear norm",
          "nuclear-norm regularization"
        ],
        "category": "specific_connectable",
        "rationale": "This optimization technique is crucial for the paper's methodology, providing a regularization framework that ensures consistency in the reconstruction process.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "camera spectral sensitivity",
        "canonical": "Camera Spectral Sensitivity",
        "aliases": [
          "CSS"
        ],
        "category": "unique_technical",
        "rationale": "Understanding and estimating CSS is essential for accurate HSI reconstruction, making it a significant technical aspect of the study.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "RGB image",
      "scene illumination",
      "forward operator"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "hyperspectral image reconstruction",
      "resolved_canonical": "Hyperspectral Image Reconstruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "deep unfolding solver",
      "resolved_canonical": "Deep Unfolding Solver",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "nuclear norm optimization",
      "resolved_canonical": "Nuclear Norm Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "camera spectral sensitivity",
      "resolved_canonical": "Camera Spectral Sensitivity",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# USCTNet: A deep unfolding nuclear-norm optimization solver for physically consistent HSI reconstruction

**Korean Title:** USCTNet: 물리적으로 일관된 HSI 재구성을 위한 심층 전개 핵-노름 최적화 해법

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.10651.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.10651](https://arxiv.org/abs/2509.10651)

## 🔗 유사한 논문
- [[2025-09-22/MCGA_ Mixture of Codebooks Hyperspectral Reconstruction via Grayscale-Aware Attention_20250922|MCGA: Mixture of Codebooks Hyperspectral Reconstruction via Grayscale-Aware Attention]] (83.5% similar)
- [[2025-09-22/RGB-Only Supervised Camera Parameter Optimization in Dynamic Scenes_20250922|RGB-Only Supervised Camera Parameter Optimization in Dynamic Scenes]] (82.5% similar)
- [[2025-09-22/DSDNet_ Raw Domain Demoir\'eing via Dual Color-Space Synergy_20250922|DSDNet: Raw Domain Demoir\'eing via Dual Color-Space Synergy]] (81.6% similar)
- [[2025-09-22/DPC-QA Net_ A No-Reference Dual-Stream Perceptual and Cellular Quality Assessment Network for Histopathology Images_20250922|DPC-QA Net: A No-Reference Dual-Stream Perceptual and Cellular Quality Assessment Network for Histopathology Images]] (81.2% similar)
- [[2025-09-19/HPGN_ Hybrid Priors-Guided Network for Compressed Low-Light Image Enhancement_20250919|HPGN: Hybrid Priors-Guided Network for Compressed Low-Light Image Enhancement]] (80.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Nuclear Norm Optimization|Nuclear Norm Optimization]]
**⚡ Unique Technical**: [[keywords/Hyperspectral Image Reconstruction|Hyperspectral Image Reconstruction]], [[keywords/Deep Unfolding Solver|Deep Unfolding Solver]], [[keywords/Camera Spectral Sensitivity|Camera Spectral Sensitivity]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.10651v2 Announce Type: replace 
Abstract: Reconstructing hyperspectral images (HSIs) from a single RGB image is ill-posed and can become physically inconsistent when the camera spectral sensitivity (CSS) and scene illumination are misspecified. We formulate RGB-to-HSI reconstruction as a physics-grounded inverse problem regularized by a nuclear norm in a learnable transform domain, and we explicitly estimate CSS and illumination to define the forward operator embedded in each iteration, ensuring colorimetric consistency. To avoid the cost and instability of full singular-value decompositions (SVDs) required by singular-value thresholding (SVT), we introduce a data-adaptive low-rank subspace SVT operator. Building on these components, we develop USCTNet, a deep unfolding solver tailored to HSI that couples a parameter estimation module with learnable proximal updates. Extensive experiments on standard benchmarks show consistent improvements over state-of-the-art RGB-based methods in reconstruction accuracy. Code: https://github.com/psykheXX/USCTNet-Code-Implementation.git

## 🔍 Abstract (한글 번역)

arXiv:2509.10651v2 발표 유형: 교체  
초록: 단일 RGB 이미지로부터 초분광 이미지를 재구성하는 것은 부정확한 문제이며, 카메라 스펙트럼 감도(CSS)와 장면 조명이 잘못 지정되면 물리적으로 일관성이 없을 수 있습니다. 우리는 RGB에서 HSI로의 재구성을 학습 가능한 변환 도메인에서 핵 노름으로 정규화된 물리 기반의 역문제로 공식화하고, 각 반복에 내장된 전방 연산자를 정의하기 위해 CSS와 조명을 명시적으로 추정하여 색채계 일관성을 보장합니다. 특이값 임계(SVT)에 필요한 전체 특이값 분해(SVD)의 비용과 불안정을 피하기 위해, 우리는 데이터 적응형 저차원 부분공간 SVT 연산자를 도입합니다. 이러한 구성 요소를 기반으로, 우리는 매개변수 추정 모듈과 학습 가능한 근접 업데이트를 결합한 HSI에 맞춘 심층 전개 해법인 USCTNet을 개발합니다. 표준 벤치마크에서의 광범위한 실험은 재구성 정확도에서 최첨단 RGB 기반 방법들에 비해 일관된 개선을 보여줍니다. 코드: https://github.com/psykheXX/USCTNet-Code-Implementation.git

## 📝 요약

이 논문은 단일 RGB 이미지에서 초분광 이미지를 재구성하는 문제를 다룹니다. 카메라의 스펙트럼 감도(CSS)와 장면 조명이 잘못 지정될 경우 물리적으로 일관성이 없는 결과가 발생할 수 있습니다. 이를 해결하기 위해 물리 기반의 역문제를 학습 가능한 변환 도메인에서 핵심 노름으로 정규화하였으며, CSS와 조명을 명시적으로 추정하여 각 반복에 포함된 순방향 연산자를 정의함으로써 색채 일관성을 보장합니다. 또한, 전통적인 특이값 임계처리(SVT)의 비용과 불안정을 피하기 위해 데이터 적응형 저차원 부분공간 SVT 연산자를 도입했습니다. 이러한 요소를 기반으로, HSI에 특화된 심층 전개 해법인 USCTNet을 개발하여 매개변수 추정 모듈과 학습 가능한 근접 업데이트를 결합했습니다. 표준 벤치마크에서의 광범위한 실험 결과, 최첨단 RGB 기반 방법들에 비해 재구성 정확도가 일관되게 향상됨을 보여주었습니다.

## 🎯 주요 포인트

- 1. 단일 RGB 이미지에서 초분광 이미지를 재구성하는 문제를 물리적 기반의 역문제로 정식화하고, 학습 가능한 변환 도메인에서 핵심 노름으로 정규화하였습니다.
- 2. 카메라 스펙트럼 감도(CSS)와 장면 조명을 명시적으로 추정하여 각 반복에 포함된 순방향 연산자를 정의하고 색채 일관성을 보장합니다.
- 3. 전치 행렬 분해(SVD)의 비용과 불안정을 피하기 위해 데이터 적응형 저차원 부분공간 SVD 연산자를 도입하였습니다.
- 4. HSI에 특화된 심층 전개 해법인 USCTNet을 개발하여 매개변수 추정 모듈과 학습 가능한 근접 업데이트를 결합하였습니다.
- 5. 표준 벤치마크에서의 광범위한 실험을 통해 최첨단 RGB 기반 방법들보다 재구성 정확도에서 일관된 개선을 보여주었습니다.


---

*Generated on 2025-09-23 12:39:54*