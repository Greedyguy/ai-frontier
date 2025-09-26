---
keywords:
  - 3D Medical Image Segmentation
  - SegResNet
  - Attention Mechanism
  - Positional Encoding
  - Muon Optimizer
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15874
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:13:22.419743",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Medical Image Segmentation",
    "SegResNet",
    "Attention Mechanism",
    "Positional Encoding",
    "Muon Optimizer"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Medical Image Segmentation": 0.78,
    "SegResNet": 0.72,
    "Attention Mechanism": 0.81,
    "Positional Encoding": 0.79,
    "Muon Optimizer": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "3D medical image segmentation",
        "canonical": "3D Medical Image Segmentation",
        "aliases": [
          "3D image segmentation",
          "medical image segmentation"
        ],
        "category": "specific_connectable",
        "rationale": "This is a specific application area that connects with various medical imaging and segmentation techniques.",
        "novelty_score": 0.58,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "SegResNet-based encoder",
        "canonical": "SegResNet",
        "aliases": [
          "SegResNet encoder"
        ],
        "category": "unique_technical",
        "rationale": "SegResNet is a specific neural network architecture used in the model, providing a unique technical detail.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.72
      },
      {
        "surface": "latent cross-attention",
        "canonical": "Attention Mechanism",
        "aliases": [
          "cross-attention"
        ],
        "category": "specific_connectable",
        "rationale": "Attention mechanisms are crucial in neural networks, and cross-attention is a specific variant that enhances connectivity.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.77,
        "link_intent_score": 0.81
      },
      {
        "surface": "relative positional encoding",
        "canonical": "Positional Encoding",
        "aliases": [
          "relative encoding"
        ],
        "category": "specific_connectable",
        "rationale": "Positional encoding is a key concept in transformer models, relevant for linking with other encoding techniques.",
        "novelty_score": 0.6,
        "connectivity_score": 0.82,
        "specificity_score": 0.75,
        "link_intent_score": 0.79
      },
      {
        "surface": "Muon optimizer",
        "canonical": "Muon Optimizer",
        "aliases": [
          "Muon"
        ],
        "category": "unique_technical",
        "rationale": "The Muon optimizer is a unique technical component that improves model training efficiency.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "foundation model",
      "interactive segmentation",
      "hidden test set"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "3D medical image segmentation",
      "resolved_canonical": "3D Medical Image Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "SegResNet-based encoder",
      "resolved_canonical": "SegResNet",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "latent cross-attention",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.77,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "relative positional encoding",
      "resolved_canonical": "Positional Encoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.82,
        "specificity": 0.75,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Muon optimizer",
      "resolved_canonical": "Muon Optimizer",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# ENSAM: an efficient foundation model for interactive segmentation of 3D medical images

**Korean Title:** ENSAM: 3D 의료 영상의 상호작용적 분할을 위한 효율적인 기초 모델

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15874.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15874](https://arxiv.org/abs/2509.15874)

## 🔗 유사한 논문
- [[2025-09-22/pFedSAM_ Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation_20250922|pFedSAM: Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation]] (83.9% similar)
- [[2025-09-22/TASAM_ Terrain-and-Aware Segment Anything Model for Temporal-Scale Remote Sensing Segmentation_20250922|TASAM: Terrain-and-Aware Segment Anything Model for Temporal-Scale Remote Sensing Segmentation]] (83.3% similar)
- [[2025-09-22/FMD-TransUNet_ Abdominal Multi-Organ Segmentation Based on Frequency Domain Multi-Axis Representation Learning and Dual Attention Mechanisms_20250922|FMD-TransUNet: Abdominal Multi-Organ Segmentation Based on Frequency Domain Multi-Axis Representation Learning and Dual Attention Mechanisms]] (82.0% similar)
- [[2025-09-22/Screener_ Self-supervised Pathology Segmentation in Medical CT Images_20250922|Screener: Self-supervised Pathology Segmentation in Medical CT Images]] (81.5% similar)
- [[2025-09-17/Consistent View Alignment Improves Foundation Models for 3D Medical Image Segmentation_20250917|Consistent View Alignment Improves Foundation Models for 3D Medical Image Segmentation]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/3D Medical Image Segmentation|3D Medical Image Segmentation]], [[keywords/Attention Mechanism|Attention Mechanism]], [[keywords/Positional Encoding|Positional Encoding]]
**⚡ Unique Technical**: [[keywords/SegResNet|SegResNet]], [[keywords/Muon Optimizer|Muon Optimizer]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15874v1 Announce Type: new 
Abstract: We present ENSAM (Equivariant, Normalized, Segment Anything Model), a lightweight and promptable model for universal 3D medical image segmentation. ENSAM combines a SegResNet-based encoder with a prompt encoder and mask decoder in a U-Net-style architecture, using latent cross-attention, relative positional encoding, normalized attention, and the Muon optimizer for training. ENSAM is designed to achieve good performance under limited data and computational budgets, and is trained from scratch on under 5,000 volumes from multiple modalities (CT, MRI, PET, ultrasound, microscopy) on a single 32 GB GPU in 6 hours. As part of the CVPR 2025 Foundation Models for Interactive 3D Biomedical Image Segmentation Challenge, ENSAM was evaluated on hidden test set with multimodal 3D medical images, obtaining a DSC AUC of 2.404, NSD AUC of 2.266, final DSC of 0.627, and final NSD of 0.597, outperforming two previously published baseline models (VISTA3D, SAM-Med3D) and matching the third (SegVol), surpassing its performance in final DSC but trailing behind in the other three metrics. In the coreset track of the challenge, ENSAM ranks 5th of 10 overall and best among the approaches not utilizing pretrained weights. Ablation studies confirm that our use of relative positional encodings and the Muon optimizer each substantially speed up convergence and improve segmentation quality.

## 🔍 Abstract (한글 번역)

arXiv:2509.15874v1 발표 유형: 신규  
초록: 우리는 보편적인 3D 의료 이미지 분할을 위한 경량의 프롬프트 가능한 모델인 ENSAM(Equivariant, Normalized, Segment Anything Model)을 소개합니다. ENSAM은 SegResNet 기반의 인코더와 프롬프트 인코더 및 마스크 디코더를 U-Net 스타일의 아키텍처로 결합하여 잠재적 교차 주의(attention), 상대적 위치 인코딩, 정규화된 주의(attention), Muon 옵티마이저를 사용하여 학습합니다. ENSAM은 제한된 데이터와 계산 자원 하에서 우수한 성능을 달성하도록 설계되었으며, 단일 32GB GPU에서 6시간 동안 여러 모달리티(CT, MRI, PET, 초음파, 현미경)의 5,000개 미만의 볼륨으로 처음부터 학습되었습니다. CVPR 2025 상호작용 3D 생의학 이미지 분할 챌린지의 기초 모델 부문에서, ENSAM은 멀티모달 3D 의료 이미지로 구성된 숨겨진 테스트 세트에서 평가되었으며, DSC AUC 2.404, NSD AUC 2.266, 최종 DSC 0.627, 최종 NSD 0.597을 기록하여 이전에 발표된 두 개의 기준 모델(VISTA3D, SAM-Med3D)을 능가하고 세 번째 모델(SegVol)과 성능을 맞추었으며, 최종 DSC에서 성능을 초과했지만 다른 세 가지 지표에서는 뒤처졌습니다. 챌린지의 코어셋 트랙에서 ENSAM은 전체 10개 중 5위를 차지했으며, 사전 학습된 가중치를 사용하지 않은 접근 방식 중에서는 최고를 기록했습니다. 절제 연구는 상대적 위치 인코딩과 Muon 옵티마이저의 사용이 각각 수렴 속도를 크게 높이고 분할 품질을 향상시킨다는 것을 확인했습니다.

## 📝 요약

ENSAM(Equivariant, Normalized, Segment Anything Model)은 경량화된 범용 3D 의료 영상 분할 모델로, 제한된 데이터와 계산 자원에서 우수한 성능을 발휘하도록 설계되었습니다. SegResNet 기반 인코더와 프롬프트 인코더, 마스크 디코더를 결합한 U-Net 스타일 아키텍처를 사용하며, 잠재 크로스 어텐션, 상대적 위치 인코딩, 정규화된 어텐션, Muon 옵티마이저를 활용합니다. ENSAM은 5,000개 미만의 다양한 모달리티(CT, MRI, PET 등) 데이터를 단일 32GB GPU로 6시간 내에 학습합니다. CVPR 2025 챌린지에서 ENSAM은 숨겨진 테스트 세트에서 높은 DSC AUC와 NSD AUC를 기록하며, 기존 모델(VISTA3D, SAM-Med3D)을 능가하고 SegVol과 유사한 성능을 보였습니다. 사전 학습 가중치를 사용하지 않은 모델 중 최고 성과를 기록했으며, 상대적 위치 인코딩과 Muon 옵티마이저의 사용이 수렴 속도와 분할 품질을 크게 향상시킴을 확인했습니다.

## 🎯 주요 포인트

- 1. ENSAM은 경량화된 범용 3D 의료 이미지 세분화 모델로, 제한된 데이터와 계산 자원 하에서도 우수한 성능을 발휘하도록 설계되었습니다.
- 2. ENSAM은 SegResNet 기반 인코더와 프롬프트 인코더, 마스크 디코더를 U-Net 스타일 아키텍처로 결합하여 잠재적 교차 주의, 상대적 위치 인코딩, 정규화된 주의, Muon 옵티마이저를 사용합니다.
- 3. ENSAM은 CVPR 2025 대회에서 다중 모달 3D 의료 이미지로 평가되어 두 개의 기존 모델을 능가하고, 세 번째 모델과 유사한 성능을 보였습니다.
- 4. ENSAM은 사전 학습된 가중치를 사용하지 않는 접근 방식 중에서 최고 성능을 기록하며, 전체적으로 10개 중 5위를 차지했습니다.
- 5. 상대적 위치 인코딩과 Muon 옵티마이저의 사용은 수렴 속도를 크게 높이고 세분화 품질을 개선하는 것으로 확인되었습니다.


---

*Generated on 2025-09-23 12:13:22*