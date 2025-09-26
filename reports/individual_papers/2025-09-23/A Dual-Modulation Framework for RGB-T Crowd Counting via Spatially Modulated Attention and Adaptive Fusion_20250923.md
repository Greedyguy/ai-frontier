---
keywords:
  - Attention Mechanism
  - Multimodal Learning
  - Multimodal Learning
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17079
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:44:24.408004",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Attention Mechanism",
    "Multimodal Learning",
    "Multimodal Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Attention Mechanism": 0.82,
    "Multimodal Learning": 0.85
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Spatially Modulated Attention",
        "canonical": "Attention Mechanism",
        "aliases": [
          "SMA"
        ],
        "category": "specific_connectable",
        "rationale": "This concept enhances the existing Attention Mechanism by incorporating spatial modulation, which is crucial for precise crowd localization.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Adaptive Fusion Modulation",
        "canonical": "Multimodal Learning",
        "aliases": [
          "AFM"
        ],
        "category": "specific_connectable",
        "rationale": "AFM represents a dynamic approach to multimodal learning, optimizing cross-modal fusion which is key in RGB-T crowd counting.",
        "novelty_score": 0.68,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.84
      },
      {
        "surface": "RGB-Thermal Crowd Counting",
        "canonical": "Multimodal Learning",
        "aliases": [
          "RGB-T Crowd Counting"
        ],
        "category": "specific_connectable",
        "rationale": "This task exemplifies the application of multimodal learning, integrating RGB and thermal data for enhanced crowd analysis.",
        "novelty_score": 0.7,
        "connectivity_score": 0.83,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      }
    ],
    "ban_list_suggestions": [
      "Transformer-based methods",
      "public safety",
      "dynamic gating mechanism"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Spatially Modulated Attention",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Adaptive Fusion Modulation",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.84
      }
    },
    {
      "candidate_surface": "RGB-Thermal Crowd Counting",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.83,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    }
  ]
}
-->

# A Dual-Modulation Framework for RGB-T Crowd Counting via Spatially Modulated Attention and Adaptive Fusion

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17079.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17079](https://arxiv.org/abs/2509.17079)

## 🔗 유사한 논문
- [[2025-09-22/MCGA_ Mixture of Codebooks Hyperspectral Reconstruction via Grayscale-Aware Attention_20250922|MCGA: Mixture of Codebooks Hyperspectral Reconstruction via Grayscale-Aware Attention]] (81.6% similar)
- [[2025-09-23/MO R-CNN_ Multispectral Oriented R-CNN for Object Detection in Remote Sensing Image_20250923|MO R-CNN: Multispectral Oriented R-CNN for Object Detection in Remote Sensing Image]] (81.2% similar)
- [[2025-09-22/RGB-Only Supervised Camera Parameter Optimization in Dynamic Scenes_20250922|RGB-Only Supervised Camera Parameter Optimization in Dynamic Scenes]] (81.1% similar)
- [[2025-09-18/MCGS-SLAM_ A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping_20250918|MCGS-SLAM: A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping]] (80.2% similar)
- [[2025-09-23/Efficient Rectified Flow for Image Fusion_20250923|Efficient Rectified Flow for Image Fusion]] (79.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]], [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Multimodal Learning|Multimodal Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17079v1 Announce Type: new 
Abstract: Accurate RGB-Thermal (RGB-T) crowd counting is crucial for public safety in challenging conditions. While recent Transformer-based methods excel at capturing global context, their inherent lack of spatial inductive bias causes attention to spread to irrelevant background regions, compromising crowd localization precision. Furthermore, effectively bridging the gap between these distinct modalities remains a major hurdle. To tackle this, we propose the Dual Modulation Framework, comprising two modules: Spatially Modulated Attention (SMA), which improves crowd localization by using a learnable Spatial Decay Mask to penalize attention between distant tokens and prevent focus from spreading to the background; and Adaptive Fusion Modulation (AFM), which implements a dynamic gating mechanism to prioritize the most reliable modality for adaptive cross-modal fusion. Extensive experiments on RGB-T crowd counting datasets demonstrate the superior performance of our method compared to previous works. Code available at https://github.com/Cht2924/RGBT-Crowd-Counting.

## 📝 요약

이 논문은 RGB-열화상(RGB-T) 군중 수 계산의 정확성을 높이기 위해 제안된 Dual Modulation Framework에 대해 설명합니다. 주요 기여는 두 가지 모듈로 구성됩니다. 첫째, Spatially Modulated Attention(SMA)는 학습 가능한 공간 감쇠 마스크를 사용하여 주의가 배경으로 확산되는 것을 방지하고 군중 위치 정확성을 향상시킵니다. 둘째, Adaptive Fusion Modulation(AFM)은 동적 게이팅 메커니즘을 통해 가장 신뢰할 수 있는 모달리티를 우선시하여 적응형 모달리티 융합을 구현합니다. 실험 결과, 제안된 방법이 기존 방법들보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. RGB-T 군중 계수의 정확성은 어려운 조건에서 공공 안전을 위해 중요합니다.
- 2. 최근 Transformer 기반 방법은 전역 문맥을 잘 포착하지만, 공간 유도 편향 부족으로 인해 주의가 불필요한 배경 영역으로 확산되어 군중 위치 정확도가 저하됩니다.
- 3. Dual Modulation Framework는 Spatially Modulated Attention(SMA)과 Adaptive Fusion Modulation(AFM)이라는 두 모듈로 구성되어 이러한 문제를 해결합니다.
- 4. SMA는 학습 가능한 공간 감쇠 마스크를 사용하여 멀리 떨어진 토큰 간의 주의를 벌주고 배경으로의 확산을 방지하여 군중 위치를 개선합니다.
- 5. AFM은 동적 게이팅 메커니즘을 구현하여 가장 신뢰할 수 있는 모달리티를 우선시하여 적응형 교차 모달 융합을 수행합니다.


---

*Generated on 2025-09-24 04:44:24*