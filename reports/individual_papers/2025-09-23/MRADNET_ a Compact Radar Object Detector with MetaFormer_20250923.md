---
keywords:
  - MetaFormer
  - U-net Architecture
  - FMCW Radar
  - Attention Mechanism
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.16223
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:09:36.316226",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "MetaFormer",
    "U-net Architecture",
    "FMCW Radar",
    "Attention Mechanism"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "MetaFormer": 0.82,
    "U-net Architecture": 0.79,
    "FMCW Radar": 0.77,
    "Attention Mechanism": 0.85
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "MetaFormer",
        "canonical": "MetaFormer",
        "aliases": [
          "MetaFormer blocks"
        ],
        "category": "unique_technical",
        "rationale": "MetaFormer represents a novel architectural component that enhances radar object detection, offering a unique link to advanced model design.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "U-net style architecture",
        "canonical": "U-net Architecture",
        "aliases": [
          "U-net"
        ],
        "category": "specific_connectable",
        "rationale": "U-net is a well-known architecture in computer vision, providing a strong link to image processing techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.87,
        "specificity_score": 0.72,
        "link_intent_score": 0.79
      },
      {
        "surface": "Frequency-modulated continuous wave radars",
        "canonical": "FMCW Radar",
        "aliases": [
          "Frequency-modulated continuous wave radar"
        ],
        "category": "unique_technical",
        "rationale": "FMCW Radar is a specific technology crucial for automotive applications, linking to radar-based detection systems.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Attention token mixers",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Attention mixers"
        ],
        "category": "specific_connectable",
        "rationale": "Attention mechanisms are fundamental in modern neural networks, facilitating connections to various machine learning models.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.75,
        "link_intent_score": 0.85
      }
    ],
    "ban_list_suggestions": [
      "compactness",
      "efficiency",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "MetaFormer",
      "resolved_canonical": "MetaFormer",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "U-net style architecture",
      "resolved_canonical": "U-net Architecture",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.87,
        "specificity": 0.72,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Frequency-modulated continuous wave radars",
      "resolved_canonical": "FMCW Radar",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Attention token mixers",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.75,
        "link_intent": 0.85
      }
    }
  ]
}
-->

# MRADNET: a Compact Radar Object Detector with MetaFormer

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16223.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.16223](https://arxiv.org/abs/2509.16223)

## 🔗 유사한 논문
- [[2025-09-22/PAN_ Pillars-Attention-Based Network for 3D Object Detection_20250922|PAN: Pillars-Attention-Based Network for 3D Object Detection]] (83.7% similar)
- [[2025-09-23/MO R-CNN_ Multispectral Oriented R-CNN for Object Detection in Remote Sensing Image_20250923|MO R-CNN: Multispectral Oriented R-CNN for Object Detection in Remote Sensing Image]] (83.3% similar)
- [[2025-09-23/PMRT_ A Training Recipe for Fast, 3D High-Resolution Aerodynamic Prediction_20250923|PMRT: A Training Recipe for Fast, 3D High-Resolution Aerodynamic Prediction]] (82.3% similar)
- [[2025-09-22/RadarGaussianDet3D_ An Efficient and Effective Gaussian-based 3D Detector with 4D Automotive Radars_20250922|RadarGaussianDet3D: An Efficient and Effective Gaussian-based 3D Detector with 4D Automotive Radars]] (82.0% similar)
- [[2025-09-22/Cross-Resolution SAR Target Detection Using Structural Hierarchy Adaptation and Reliable Adjacency Alignment_20250922|Cross-Resolution SAR Target Detection Using Structural Hierarchy Adaptation and Reliable Adjacency Alignment]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/U-net Architecture|U-net Architecture]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/MetaFormer|MetaFormer]], [[keywords/FMCW Radar|FMCW Radar]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16223v1 Announce Type: cross 
Abstract: Frequency-modulated continuous wave radars have gained increasing popularity in the automotive industry. Its robustness against adverse weather conditions makes it a suitable choice for radar object detection in advanced driver assistance systems. These real-time embedded systems have requirements for the compactness and efficiency of the model, which have been largely overlooked in previous work. In this work, we propose mRadNet, a novel radar object detection model with compactness in mind. mRadNet employs a U-net style architecture with MetaFormer blocks, in which separable convolution and attention token mixers are used to capture both local and global features effectively. More efficient token embedding and merging strategies are introduced to further facilitate the lightweight design of the model. The performance of mRadNet is validated on the CRUW dataset, improving state-of-the-art performance.

## 📝 요약

이 논문에서는 자동차 산업에서 주목받고 있는 주파수 변조 연속파 레이더를 위한 새로운 객체 탐지 모델인 mRadNet을 제안합니다. mRadNet은 U-net 스타일의 아키텍처와 MetaFormer 블록을 사용하여 지역 및 전역 특징을 효과적으로 포착합니다. 또한, 더 효율적인 토큰 임베딩 및 병합 전략을 도입하여 모델의 경량화를 달성합니다. CRUW 데이터셋에서 mRadNet의 성능을 검증한 결과, 기존 최첨단 성능을 개선하였습니다. 이 연구는 모델의 컴팩트함과 효율성을 중시하여 실시간 임베디드 시스템의 요구를 충족시킵니다.

## 🎯 주요 포인트

- 1. 주파수 변조 연속파 레이더는 악천후에서도 강력한 성능을 발휘하여 자동차 산업에서 인기를 얻고 있습니다.
- 2. mRadNet은 U-net 스타일 아키텍처와 MetaFormer 블록을 사용하여 컴팩트한 설계를 목표로 하는 새로운 레이더 객체 탐지 모델입니다.
- 3. mRadNet은 분리 가능한 합성곱과 주의 토큰 믹서를 사용하여 지역 및 전역 특징을 효과적으로 포착합니다.
- 4. 더 효율적인 토큰 임베딩 및 병합 전략을 도입하여 모델의 경량화를 촉진합니다.
- 5. mRadNet은 CRUW 데이터셋에서 검증되었으며, 기존의 최첨단 성능을 개선했습니다.


---

*Generated on 2025-09-24 05:09:36*