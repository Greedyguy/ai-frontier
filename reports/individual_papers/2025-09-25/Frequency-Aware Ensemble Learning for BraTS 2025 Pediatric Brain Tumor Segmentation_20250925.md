---
keywords:
  - Neural Network
  - Attention Mechanism
  - Frequency Domain Decomposition
  - BraTS Challenge
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.19353
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:17:19.292922",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Attention Mechanism",
    "Frequency Domain Decomposition",
    "BraTS Challenge"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.82,
    "Attention Mechanism": 0.79,
    "Frequency Domain Decomposition": 0.77,
    "BraTS Challenge": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "nnU-Net",
        "canonical": "Neural Network",
        "aliases": [
          "nnU-Net"
        ],
        "category": "broad_technical",
        "rationale": "nnU-Net is a specific implementation of neural networks, which are central to deep learning and medical image segmentation.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Swin UNETR",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Swin UNETR"
        ],
        "category": "specific_connectable",
        "rationale": "Swin UNETR utilizes attention mechanisms, which are crucial for enhancing model performance in complex image segmentation tasks.",
        "novelty_score": 0.58,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      },
      {
        "surface": "HFF-Net",
        "canonical": "Frequency Domain Decomposition",
        "aliases": [
          "HFF-Net"
        ],
        "category": "unique_technical",
        "rationale": "HFF-Net introduces a novel approach using frequency domain decomposition, which is specific to the task of separating tissue contours and texture details.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      },
      {
        "surface": "BraTS 2025",
        "canonical": "BraTS Challenge",
        "aliases": [
          "BraTS-PED 2025"
        ],
        "category": "unique_technical",
        "rationale": "BraTS 2025 is a specific challenge that provides context and relevance for pediatric brain tumor segmentation research.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "ensemble approach",
      "Dice scores",
      "clinical diagnosis"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "nnU-Net",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Swin UNETR",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "HFF-Net",
      "resolved_canonical": "Frequency Domain Decomposition",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "BraTS 2025",
      "resolved_canonical": "BraTS Challenge",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Frequency-Aware Ensemble Learning for BraTS 2025 Pediatric Brain Tumor Segmentation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19353.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.19353](https://arxiv.org/abs/2509.19353)

## 🔗 유사한 논문
- [[2025-09-23/Unified Multimodal Coherent Field_ Synchronous Semantic-Spatial-Vision Fusion for Brain Tumor Segmentation_20250923|Unified Multimodal Coherent Field: Synchronous Semantic-Spatial-Vision Fusion for Brain Tumor Segmentation]] (85.0% similar)
- [[2025-09-23/Training the next generation of physicians for artificial intelligence-assisted clinical neuroradiology_ ASNR MICCAI Brain Tumor Segmentation (BraTS) 2025 Lighthouse Challenge education platform_20250923|Training the next generation of physicians for artificial intelligence-assisted clinical neuroradiology: ASNR MICCAI Brain Tumor Segmentation (BraTS) 2025 Lighthouse Challenge education platform]] (84.2% similar)
- [[2025-09-23/An Efficient Dual-Line Decoder Network with Multi-Scale Convolutional Attention for Multi-organ Segmentation_20250923|An Efficient Dual-Line Decoder Network with Multi-Scale Convolutional Attention for Multi-organ Segmentation]] (83.1% similar)
- [[2025-09-22/Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images_20250922|Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images]] (82.6% similar)
- [[2025-09-23/Multi-needle Localization for Pelvic Seed Implant Brachytherapy based on Tip-handle Detection and Matching_20250923|Multi-needle Localization for Pelvic Seed Implant Brachytherapy based on Tip-handle Detection and Matching]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Frequency Domain Decomposition|Frequency Domain Decomposition]], [[keywords/BraTS Challenge|BraTS Challenge]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19353v1 Announce Type: cross 
Abstract: Pediatric brain tumor segmentation presents unique challenges due to the rarity and heterogeneity of these malignancies, yet remains critical for clinical diagnosis and treatment planning. We propose an ensemble approach integrating nnU-Net, Swin UNETR, and HFF-Net for the BraTS-PED 2025 challenge. Our method incorporates three key extensions: adjustable initialization scales for optimal nnU-Net complexity control, transfer learning from BraTS 2021 pre-trained models to enhance Swin UNETR's generalization on pediatric dataset, and frequency domain decomposition for HFF-Net to separate low-frequency tissue contours from high-frequency texture details. Our final ensemble combines nnU-Net ($\gamma=0.7$), fine-tuned Swin UNETR, and HFF-Net, achieving Dice scores of 72.3% (ET), 95.6% (NET), 68.9% (CC), 89.5% (ED), 92.3% (TC), and 92.3% (WT), respectively.

## 📝 요약

이 논문은 소아 뇌종양 분할의 어려움을 해결하기 위해 nnU-Net, Swin UNETR, HFF-Net를 통합한 앙상블 접근법을 제안합니다. 주요 기여로는 nnU-Net의 복잡성을 조절하기 위한 초기화 스케일 조정, BraTS 2021 사전 학습 모델을 활용한 Swin UNETR의 전이 학습, HFF-Net의 주파수 영역 분해를 통한 조직 윤곽과 질감 분리입니다. 최종 앙상블은 높은 Dice 점수를 기록하며, 소아 데이터셋에서의 일반화 성능을 향상시켰습니다.

## 🎯 주요 포인트

- 1. 소아 뇌종양 분할의 중요성과 도전 과제를 해결하기 위해 nnU-Net, Swin UNETR, HFF-Net를 통합한 앙상블 접근법을 제안했습니다.
- 2. nnU-Net의 복잡성을 최적화하기 위해 조정 가능한 초기화 스케일을 도입했습니다.
- 3. Swin UNETR의 소아 데이터셋에 대한 일반화 성능을 향상시키기 위해 BraTS 2021 사전 학습 모델을 활용한 전이 학습을 적용했습니다.
- 4. HFF-Net에서는 주파수 도메인 분해를 통해 저주파 조직 윤곽과 고주파 텍스처 세부 정보를 분리했습니다.
- 5. 최종 앙상블은 다양한 지표에서 높은 Dice 점수를 기록하며, 특히 NET에서 95.6%의 성과를 달성했습니다.


---

*Generated on 2025-09-26 09:17:19*