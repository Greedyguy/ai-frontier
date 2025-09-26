---
keywords:
  - RawJPEG Adapter
  - JPEG Compression
  - Image Signal Processor
  - Digital Negative
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.19624
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:00:51.300009",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "RawJPEG Adapter",
    "JPEG Compression",
    "Image Signal Processor",
    "Digital Negative"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "RawJPEG Adapter": 0.88,
    "JPEG Compression": 0.8,
    "Image Signal Processor": 0.78,
    "Digital Negative": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "RawJPEG Adapter",
        "canonical": "RawJPEG Adapter",
        "aliases": [
          "Raw-JPEG Adapter"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel preprocessing pipeline for raw image compression using JPEG, which is central to the paper's contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "JPEG Compression",
        "canonical": "JPEG Compression",
        "aliases": [
          "JPEG"
        ],
        "category": "broad_technical",
        "rationale": "A widely used image compression standard, relevant for linking discussions on image processing and storage.",
        "novelty_score": 0.3,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Image Signal Processor",
        "canonical": "Image Signal Processor",
        "aliases": [
          "ISP"
        ],
        "category": "specific_connectable",
        "rationale": "Key component in digital cameras for converting raw data to display-ready images, important for linking to hardware and image processing topics.",
        "novelty_score": 0.45,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Digital Negative",
        "canonical": "Digital Negative",
        "aliases": [
          "DNG"
        ],
        "category": "specific_connectable",
        "rationale": "A raw image format that is relevant for discussions on image storage and editing.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
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
      "candidate_surface": "RawJPEG Adapter",
      "resolved_canonical": "RawJPEG Adapter",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "JPEG Compression",
      "resolved_canonical": "JPEG Compression",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Image Signal Processor",
      "resolved_canonical": "Image Signal Processor",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Digital Negative",
      "resolved_canonical": "Digital Negative",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Raw-JPEG Adapter: Efficient Raw Image Compression with JPEG

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19624.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.19624](https://arxiv.org/abs/2509.19624)

## 🔗 유사한 논문
- [[2025-09-22/Efficient RAW Image Deblurring with Adaptive Frequency Modulation_20250922|Efficient RAW Image Deblurring with Adaptive Frequency Modulation]] (82.3% similar)
- [[2025-09-19/HPGN_ Hybrid Priors-Guided Network for Compressed Low-Light Image Enhancement_20250919|HPGN: Hybrid Priors-Guided Network for Compressed Low-Light Image Enhancement]] (81.3% similar)
- [[2025-09-22/DSDNet_ Raw Domain Demoir\'eing via Dual Color-Space Synergy_20250922|DSDNet: Raw Domain Demoir\'eing via Dual Color-Space Synergy]] (80.6% similar)
- [[2025-09-18/Task-Aware Image Signal Processor for Advanced Visual Perception_20250918|Task-Aware Image Signal Processor for Advanced Visual Perception]] (80.5% similar)
- [[2025-09-23/Subjective Camera 1.0_ Bridging Human Cognition and Visual Reconstruction through Sequence-Aware Sketch-Guided Diffusion_20250923|Subjective Camera 1.0: Bridging Human Cognition and Visual Reconstruction through Sequence-Aware Sketch-Guided Diffusion]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/JPEG Compression|JPEG Compression]]
**🔗 Specific Connectable**: [[keywords/Image Signal Processor|Image Signal Processor]], [[keywords/Digital Negative|Digital Negative]]
**⚡ Unique Technical**: [[keywords/RawJPEG Adapter|RawJPEG Adapter]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19624v1 Announce Type: new 
Abstract: Digital cameras digitize scene light into linear raw representations, which the image signal processor (ISP) converts into display-ready outputs. While raw data preserves full sensor information--valuable for editing and vision tasks--formats such as Digital Negative (DNG) require large storage, making them impractical in constrained scenarios. In contrast, JPEG is a widely supported format, offering high compression efficiency and broad compatibility, but it is not well-suited for raw storage. This paper presents RawJPEG Adapter, a lightweight, learnable, and invertible preprocessing pipeline that adapts raw images for standard JPEG compression. Our method applies spatial and optional frequency-domain transforms, with compact parameters stored in the JPEG comment field, enabling accurate raw reconstruction. Experiments across multiple datasets show that our method achieves higher fidelity than direct JPEG storage, supports other codecs, and provides a favorable trade-off between compression ratio and reconstruction accuracy.

## 📝 요약

이 논문은 RawJPEG Adapter라는 새로운 방법론을 제안하여, 디지털 카메라의 원시(raw) 데이터를 JPEG 형식으로 효율적으로 저장할 수 있도록 합니다. RawJPEG Adapter는 가벼운 학습 가능한 전처리 파이프라인으로, 공간 및 주파수 변환을 통해 원시 이미지를 표준 JPEG 압축에 적합하게 변환합니다. JPEG의 주석 필드에 압축된 파라미터를 저장하여, 원시 데이터의 정확한 복원이 가능합니다. 여러 데이터셋을 통한 실험 결과, 이 방법은 직접적인 JPEG 저장보다 높은 충실도를 제공하며, 다른 코덱도 지원하고, 압축 비율과 복원 정확도 간의 균형을 잘 맞춥니다.

## 🎯 주요 포인트

- 1. RawJPEG Adapter는 원시(raw) 이미지를 표준 JPEG 압축에 적합하게 변환하는 경량의 학습 가능한 전처리 파이프라인입니다.
- 2. 이 방법은 공간 및 선택적 주파수 도메인 변환을 적용하며, JPEG 주석 필드에 압축된 파라미터를 저장하여 정확한 원시 데이터 복원을 가능하게 합니다.
- 3. 여러 데이터셋에 대한 실험 결과, RawJPEG Adapter는 직접적인 JPEG 저장보다 높은 충실도를 달성하고 다른 코덱도 지원하며, 압축 비율과 복원 정확도 간의 유리한 균형을 제공합니다.
- 4. JPEG는 높은 압축 효율성과 광범위한 호환성을 제공하지만 원시 데이터 저장에는 적합하지 않다는 점을 해결합니다.
- 5. RawJPEG Adapter는 제한된 저장 공간 시나리오에서 DNG와 같은 대용량 원시 데이터 포맷의 비실용성을 보완합니다.


---

*Generated on 2025-09-26 09:00:51*