<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:00:40.988230",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "MK-UNet",
    "Multi-Kernel Depth-Wise Convolution",
    "Attention Mechanism",
    "Medical Image Segmentation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "MK-UNet": 0.8,
    "Multi-Kernel Depth-Wise Convolution": 0.75,
    "Attention Mechanism": 0.85,
    "Medical Image Segmentation": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "MK-UNet",
        "canonical": "MK-UNet",
        "aliases": [
          "Multi-kernel U-Net",
          "MKUNet"
        ],
        "category": "unique_technical",
        "rationale": "MK-UNet is a novel architecture specifically designed for lightweight medical image segmentation, making it a unique technical contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "multi-kernel depth-wise convolution block",
        "canonical": "Multi-Kernel Depth-Wise Convolution",
        "aliases": [
          "MKDC"
        ],
        "category": "unique_technical",
        "rationale": "This is a key component of MK-UNet, contributing to its lightweight and efficient processing capabilities.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "attention mechanisms",
        "canonical": "Attention Mechanism",
        "aliases": [
          "attention",
          "channel attention",
          "spatial attention",
          "grouped gated attention"
        ],
        "category": "specific_connectable",
        "rationale": "Attention mechanisms are crucial for enhancing feature extraction in neural networks, aligning with existing concepts.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "medical image segmentation",
        "canonical": "Medical Image Segmentation",
        "aliases": [
          "image segmentation",
          "medical segmentation"
        ],
        "category": "broad_technical",
        "rationale": "This is a fundamental application area for the discussed techniques, providing context for the technical innovations.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "state-of-the-art",
      "benchmark",
      "computational resources"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "MK-UNet",
      "resolved_canonical": "MK-UNet",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "multi-kernel depth-wise convolution block",
      "resolved_canonical": "Multi-Kernel Depth-Wise Convolution",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "attention mechanisms",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "medical image segmentation",
      "resolved_canonical": "Medical Image Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# MK-UNet: Multi-kernel Lightweight CNN for Medical Image Segmentation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18493.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18493](https://arxiv.org/abs/2509.18493)

## 🔗 유사한 논문
- [[2025-09-23/An Efficient Dual-Line Decoder Network with Multi-Scale Convolutional Attention for Multi-organ Segmentation_20250923|An Efficient Dual-Line Decoder Network with Multi-Scale Convolutional Attention for Multi-organ Segmentation]] (87.5% similar)
- [[2025-09-22/FMD-TransUNet_ Abdominal Multi-Organ Segmentation Based on Frequency Domain Multi-Axis Representation Learning and Dual Attention Mechanisms_20250922|FMD-TransUNet: Abdominal Multi-Organ Segmentation Based on Frequency Domain Multi-Axis Representation Learning and Dual Attention Mechanisms]] (87.0% similar)
- [[2025-09-23/DCFFSNet_ Deep Connectivity Feature Fusion Separation Network for Medical Image Segmentation_20250923|DCFFSNet: Deep Connectivity Feature Fusion Separation Network for Medical Image Segmentation]] (85.4% similar)
- [[2025-09-23/Unified Multimodal Coherent Field_ Synchronous Semantic-Spatial-Vision Fusion for Brain Tumor Segmentation_20250923|Unified Multimodal Coherent Field: Synchronous Semantic-Spatial-Vision Fusion for Brain Tumor Segmentation]] (84.2% similar)
- [[2025-09-23/A Unified Deep Learning Framework for Motion Correction in Medical Imaging_20250923|A Unified Deep Learning Framework for Motion Correction in Medical Imaging]] (84.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Medical Image Segmentation|Medical Image Segmentation]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/MK-UNet|MK-UNet]], [[keywords/Multi-Kernel Depth-Wise Convolution|Multi-Kernel Depth-Wise Convolution]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18493v1 Announce Type: new 
Abstract: In this paper, we introduce MK-UNet, a paradigm shift towards ultra-lightweight, multi-kernel U-shaped CNNs tailored for medical image segmentation. Central to MK-UNet is the multi-kernel depth-wise convolution block (MKDC) we design to adeptly process images through multiple kernels, while capturing complex multi-resolution spatial relationships. MK-UNet also emphasizes the images salient features through sophisticated attention mechanisms, including channel, spatial, and grouped gated attention. Our MK-UNet network, with a modest computational footprint of only 0.316M parameters and 0.314G FLOPs, represents not only a remarkably lightweight, but also significantly improved segmentation solution that provides higher accuracy over state-of-the-art (SOTA) methods across six binary medical imaging benchmarks. Specifically, MK-UNet outperforms TransUNet in DICE score with nearly 333$\times$ and 123$\times$ fewer parameters and FLOPs, respectively. Similarly, when compared against UNeXt, MK-UNet exhibits superior segmentation performance, improving the DICE score up to 6.7% margins while operating with 4.7$\times$ fewer #Params. Our MK-UNet also outperforms other recent lightweight networks, such as MedT, CMUNeXt, EGE-UNet, and Rolling-UNet, with much lower computational resources. This leap in performance, coupled with drastic computational gains, positions MK-UNet as an unparalleled solution for real-time, high-fidelity medical diagnostics in resource-limited settings, such as point-of-care devices. Our implementation is available at https://github.com/SLDGroup/MK-UNet.

## 📝 요약

이 논문에서는 의료 영상 분할을 위한 초경량 다중 커널 U자형 CNN인 MK-UNet을 소개합니다. MK-UNet의 핵심은 다중 커널 심층 컨볼루션 블록(MKDC)으로, 복잡한 다중 해상도 공간 관계를 포착하며 이미지를 처리합니다. 또한 채널, 공간, 그룹화된 게이트 주의 메커니즘을 통해 이미지의 중요한 특징을 강조합니다. MK-UNet은 0.316M의 파라미터와 0.314G FLOPs로, 기존 최첨단 방법보다 높은 정확도를 제공하며, 특히 TransUNet과 UNeXt보다 적은 자원으로 더 나은 성능을 보입니다. 이로 인해 MK-UNet은 실시간 고품질 의료 진단에 적합한 솔루션으로 자리 잡고 있습니다.

## 🎯 주요 포인트

- 1. MK-UNet은 초경량 다중 커널 U-모양 CNN으로, 의료 이미지 분할을 위해 설계되었습니다.
- 2. MK-UNet의 핵심은 다중 커널 심층 컨볼루션 블록(MKDC)으로, 복잡한 다중 해상도 공간 관계를 포착합니다.
- 3. MK-UNet은 채널, 공간, 그룹화된 게이트 주의 메커니즘을 통해 이미지의 중요한 특징을 강조합니다.
- 4. MK-UNet은 0.316M 파라미터와 0.314G FLOPs의 낮은 계산 비용으로 최첨단 방법들보다 높은 정확도를 제공합니다.
- 5. MK-UNet은 TransUNet 및 UNeXt와 비교하여 DICE 점수에서 우수한 성능을 보이며, 특히 리소스가 제한된 환경에서 실시간 고품질 의료 진단에 적합합니다.


---

*Generated on 2025-09-24 16:00:40*