<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:00:12.555082",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "MoCrop",
    "Video Action Recognition",
    "Motion Vectors",
    "ResNet",
    "Compressed Video Domain"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "MoCrop": 0.8,
    "Video Action Recognition": 0.85,
    "Motion Vectors": 0.7,
    "ResNet": 0.8,
    "Compressed Video Domain": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "MoCrop",
        "canonical": "MoCrop",
        "aliases": [
          "Motion Guided Cropping"
        ],
        "category": "unique_technical",
        "rationale": "MoCrop is a novel method introduced in the paper, making it a unique technical concept for linking.",
        "novelty_score": 0.9,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "video action recognition",
        "canonical": "Video Action Recognition",
        "aliases": [
          "action recognition in videos"
        ],
        "category": "broad_technical",
        "rationale": "Video Action Recognition is a key application area discussed in the paper, linking it to broader computer vision topics.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "motion vectors",
        "canonical": "Motion Vectors",
        "aliases": [
          "MV"
        ],
        "category": "specific_connectable",
        "rationale": "Motion Vectors are crucial for MoCrop's functionality, providing a specific technical link to video processing.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "ResNet-50",
        "canonical": "ResNet",
        "aliases": [
          "ResNet50"
        ],
        "category": "specific_connectable",
        "rationale": "ResNet-50 is a specific model used in the paper, linking it to deep learning architectures.",
        "novelty_score": 0.3,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "compressed domain",
        "canonical": "Compressed Video Domain",
        "aliases": [
          "video compression domain"
        ],
        "category": "specific_connectable",
        "rationale": "The compressed domain is a specific context for MoCrop's application, relevant for video processing discussions.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "training free",
      "efficient",
      "accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "MoCrop",
      "resolved_canonical": "MoCrop",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "video action recognition",
      "resolved_canonical": "Video Action Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "motion vectors",
      "resolved_canonical": "Motion Vectors",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "ResNet-50",
      "resolved_canonical": "ResNet",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "compressed domain",
      "resolved_canonical": "Compressed Video Domain",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# MoCrop: Training Free Motion Guided Cropping for Efficient Video Action Recognition

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18473.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18473](https://arxiv.org/abs/2509.18473)

## 🔗 유사한 논문
- [[2025-09-23/MoCLIP-Lite_ Efficient Video Recognition by Fusing CLIP with Motion Vectors_20250923|MoCLIP-Lite: Efficient Video Recognition by Fusing CLIP with Motion Vectors]] (87.7% similar)
- [[2025-09-23/A Unified Deep Learning Framework for Motion Correction in Medical Imaging_20250923|A Unified Deep Learning Framework for Motion Correction in Medical Imaging]] (83.1% similar)
- [[2025-09-23/4D-MoDe_ Towards Editable and Scalable Volumetric Streaming via Motion-Decoupled 4D Gaussian Compression_20250923|4D-MoDe: Towards Editable and Scalable Volumetric Streaming via Motion-Decoupled 4D Gaussian Compression]] (82.9% similar)
- [[2025-09-23/MO R-CNN_ Multispectral Oriented R-CNN for Object Detection in Remote Sensing Image_20250923|MO R-CNN: Multispectral Oriented R-CNN for Object Detection in Remote Sensing Image]] (82.8% similar)
- [[2025-09-24/MVP_ Motion Vector Propagation for Zero-Shot Video Object Detection_20250924|MVP: Motion Vector Propagation for Zero-Shot Video Object Detection]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Video Action Recognition|Video Action Recognition]]
**🔗 Specific Connectable**: [[keywords/Motion Vectors|Motion Vectors]], [[keywords/ResNet|ResNet]], [[keywords/Compressed Video Domain|Compressed Video Domain]]
**⚡ Unique Technical**: [[keywords/MoCrop|MoCrop]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18473v1 Announce Type: new 
Abstract: We introduce MoCrop, a motion-aware adaptive cropping module for efficient video action recognition in the compressed domain. MoCrop uses motion vectors that are available in H.264 video to locate motion-dense regions and produces a single clip-level crop that is applied to all I-frames at inference. The module is training free, adds no parameters, and can be plugged into diverse backbones. A lightweight pipeline that includes denoising & merge (DM), Monte Carlo sampling (MCS), and adaptive cropping (AC) via a motion-density submatrix search yields robust crops with negligible overhead. On UCF101, MoCrop improves accuracy or reduces compute. With ResNet-50, it delivers +3.5% Top-1 accuracy at equal FLOPs (attention setting), or +2.4% Top-1 accuracy with 26.5% fewer FLOPs (efficiency setting). Applied to CoViAR, it reaches 89.2% Top-1 accuracy at the original cost and 88.5% Top-1 accuracy while reducing compute from 11.6 to 8.5 GFLOPs. Consistent gains on MobileNet-V3, EfficientNet-B1, and Swin-B indicate strong generality and make MoCrop practical for real-time deployment in the compressed domain. Our code and models are available at https://github.com/microa/MoCrop.

## 📝 요약

MoCrop은 압축된 비디오에서 효율적인 동작 인식이 가능한 모션 인식 적응형 크롭 모듈입니다. H.264 비디오의 모션 벡터를 활용하여 동작이 많은 영역을 찾아내고, 모든 I-프레임에 동일한 클립 수준의 크롭을 적용합니다. 이 모듈은 학습이 필요 없고, 추가 매개변수가 없으며 다양한 백본에 쉽게 통합될 수 있습니다. MoCrop은 경량 파이프라인을 통해 강력한 크롭을 제공하며, UCF101 데이터셋에서 ResNet-50을 사용하여 동일한 FLOPs에서 3.5% 높은 Top-1 정확도를 달성하거나, 26.5% 적은 FLOPs로 2.4% 높은 정확도를 기록했습니다. CoViAR에 적용 시, 89.2%의 Top-1 정확도를 유지하면서 계산량을 줄였습니다. MobileNet-V3, EfficientNet-B1, Swin-B에서도 일관된 성능 향상을 보여, 실시간 압축 도메인에 실용적입니다. 코드와 모델은 GitHub에서 제공됩니다.

## 🎯 주요 포인트

- 1. MoCrop은 H.264 비디오의 모션 벡터를 활용하여 모션이 집중된 영역을 찾아내고, 모든 I-프레임에 적용되는 클립 수준의 크롭을 생성하는 모션 인식 적응형 크롭 모듈입니다.
- 2. MoCrop은 훈련이 필요 없고, 추가적인 파라미터 없이 다양한 백본에 플러그인 형태로 적용 가능합니다.
- 3. MoCrop은 UCF101 데이터셋에서 ResNet-50을 사용하여 동일한 FLOPs에서 Top-1 정확도를 3.5% 향상시키거나, 26.5% 적은 FLOPs로 2.4% 향상된 정확도를 제공합니다.
- 4. CoViAR에 적용 시, MoCrop은 11.6에서 8.5 GFLOPs로 연산량을 줄이면서도 89.2%의 Top-1 정확도를 유지합니다.
- 5. MobileNet-V3, EfficientNet-B1, Swin-B에서도 일관된 성능 향상을 보여 MoCrop은 실시간 압축 도메인 배포에 실용적입니다.


---

*Generated on 2025-09-24 16:00:12*