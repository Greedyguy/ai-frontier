<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:11:50.326820",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "MoiréNet",
    "Neural Network",
    "Directional Frequency-Spatial Encoder",
    "Frequency-Spatial Adaptive Selector"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "MoiréNet": 0.8,
    "Neural Network": 0.85,
    "Directional Frequency-Spatial Encoder": 0.75,
    "Frequency-Spatial Adaptive Selector": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "MoiréNet",
        "canonical": "MoiréNet",
        "aliases": [
          "MoireNet",
          "Moire Net"
        ],
        "category": "unique_technical",
        "rationale": "MoiréNet is a novel framework specifically designed for image demoiréing, representing a unique contribution to the field.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "convolutional neural U-Net-based framework",
        "canonical": "Neural Network",
        "aliases": [
          "U-Net",
          "convolutional neural network"
        ],
        "category": "broad_technical",
        "rationale": "The U-Net architecture is a well-known neural network model, facilitating connections within the broader neural network research community.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Directional Frequency-Spatial Encoder",
        "canonical": "Directional Frequency-Spatial Encoder",
        "aliases": [
          "DFSE"
        ],
        "category": "unique_technical",
        "rationale": "This component is a novel approach to discerning moiré orientation, offering a unique technical contribution.",
        "novelty_score": 0.78,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "Frequency-Spatial Adaptive Selector",
        "canonical": "Frequency-Spatial Adaptive Selector",
        "aliases": [
          "FSAS"
        ],
        "category": "unique_technical",
        "rationale": "FSAS is a specific innovation for feature-adaptive suppression in image processing, adding unique value to the field.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "parameter-efficient",
      "state-of-the-art",
      "extensive experiments"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "MoiréNet",
      "resolved_canonical": "MoiréNet",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "convolutional neural U-Net-based framework",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Directional Frequency-Spatial Encoder",
      "resolved_canonical": "Directional Frequency-Spatial Encoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Frequency-Spatial Adaptive Selector",
      "resolved_canonical": "Frequency-Spatial Adaptive Selector",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Moir\'eNet: A Compact Dual-Domain Network for Image Demoir\'eing

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18910.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18910](https://arxiv.org/abs/2509.18910)

## 🔗 유사한 논문
- [[2025-09-22/DSDNet_ Raw Domain Demoir\'eing via Dual Color-Space Synergy_20250922|DSDNet: Raw Domain Demoir\'eing via Dual Color-Space Synergy]] (86.3% similar)
- [[2025-09-23/MO R-CNN_ Multispectral Oriented R-CNN for Object Detection in Remote Sensing Image_20250923|MO R-CNN: Multispectral Oriented R-CNN for Object Detection in Remote Sensing Image]] (84.3% similar)
- [[2025-09-24/MoCrop_ Training Free Motion Guided Cropping for Efficient Video Action Recognition_20250924|MoCrop: Training Free Motion Guided Cropping for Efficient Video Action Recognition]] (82.4% similar)
- [[2025-09-22/Efficient RAW Image Deblurring with Adaptive Frequency Modulation_20250922|Efficient RAW Image Deblurring with Adaptive Frequency Modulation]] (82.0% similar)
- [[2025-09-23/A Unified Deep Learning Framework for Motion Correction in Medical Imaging_20250923|A Unified Deep Learning Framework for Motion Correction in Medical Imaging]] (81.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**⚡ Unique Technical**: [[keywords/MoiréNet|MoiréNet]], [[keywords/Directional Frequency-Spatial Encoder|Directional Frequency-Spatial Encoder]], [[keywords/Frequency-Spatial Adaptive Selector|Frequency-Spatial Adaptive Selector]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18910v1 Announce Type: new 
Abstract: Moir\'e patterns arise from spectral aliasing between display pixel lattices and camera sensor grids, manifesting as anisotropic, multi-scale artifacts that pose significant challenges for digital image demoir\'eing. We propose Moir\'eNet, a convolutional neural U-Net-based framework that synergistically integrates frequency and spatial domain features for effective artifact removal. Moir\'eNet introduces two key components: a Directional Frequency-Spatial Encoder (DFSE) that discerns moir\'e orientation via directional difference convolution, and a Frequency-Spatial Adaptive Selector (FSAS) that enables precise, feature-adaptive suppression. Extensive experiments demonstrate that Moir\'eNet achieves state-of-the-art performance on public and actively used datasets while being highly parameter-efficient. With only 5.513M parameters, representing a 48% reduction compared to ESDNet-L, Moir\'eNet combines superior restoration quality with parameter efficiency, making it well-suited for resource-constrained applications including smartphone photography, industrial imaging, and augmented reality.

## 📝 요약

MoiréNet은 디스플레이 픽셀 격자와 카메라 센서 그리드 간의 스펙트럼 에일리어싱으로 발생하는 모아레 패턴을 효과적으로 제거하기 위한 U-Net 기반의 컨볼루션 신경망 프레임워크입니다. 이 모델은 방향성 차이 합성을 통해 모아레 방향을 식별하는 방향성 주파수-공간 인코더(DFSE)와 특징 적응적 억제를 가능하게 하는 주파수-공간 적응 선택기(FSAS)를 도입합니다. MoiréNet은 공공 및 널리 사용되는 데이터셋에서 최첨단 성능을 달성하며, 5.513M 파라미터로 ESDNet-L 대비 48% 파라미터를 줄여 자원 제약이 있는 환경에서도 뛰어난 복원 품질을 제공합니다.

## 🎯 주요 포인트

- 1. MoiréNet은 주파수 및 공간 도메인 특징을 통합하여 효과적인 모아레 패턴 제거를 수행하는 U-Net 기반 프레임워크입니다.
- 2. MoiréNet은 방향 차이 합성곱을 통해 모아레 방향을 식별하는 DFSE와 특징 적응형 억제를 가능하게 하는 FSAS를 도입합니다.
- 3. MoiréNet은 공공 및 널리 사용되는 데이터셋에서 최첨단 성능을 달성하며, 5.513M 파라미터로 ESDNet-L 대비 48% 파라미터를 절감합니다.
- 4. MoiréNet은 스마트폰 사진 촬영, 산업 이미지 처리, 증강 현실 등 자원 제약이 있는 응용 분야에 적합합니다.


---

*Generated on 2025-09-24 16:11:50*