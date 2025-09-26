---
keywords:
  - Attention Mechanism
  - Dual-Line Decoder Network
  - Mutation-Based Loss Function
  - Computer Vision
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2508.17007
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:21:55.927294",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Attention Mechanism",
    "Dual-Line Decoder Network",
    "Mutation-Based Loss Function",
    "Computer Vision"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Attention Mechanism": 0.85,
    "Dual-Line Decoder Network": 0.8,
    "Mutation-Based Loss Function": 0.75,
    "Computer Vision": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multi-Scale Convolutional Attention",
        "canonical": "Attention Mechanism",
        "aliases": [
          "MSCAM",
          "Multi-Scale Attention"
        ],
        "category": "specific_connectable",
        "rationale": "This mechanism enhances feature representation and aligns with the known concept of attention mechanisms in neural networks.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Dual-Line Decoder Network",
        "canonical": "Dual-Line Decoder Network",
        "aliases": [
          "EDLDNet"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel architecture specific to this paper, crucial for understanding its contribution.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Mutation-Based Loss Function",
        "canonical": "Mutation-Based Loss Function",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Introduces a new method for enhancing model generalization, unique to this study.",
        "novelty_score": 0.7,
        "connectivity_score": 0.55,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Medical Image Segmentation",
        "canonical": "Computer Vision",
        "aliases": [
          "Organ Segmentation"
        ],
        "category": "broad_technical",
        "rationale": "Links to the broader field of computer vision, of which medical image segmentation is a part.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "SOTA",
      "performance",
      "efficiency"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multi-Scale Convolutional Attention",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Dual-Line Decoder Network",
      "resolved_canonical": "Dual-Line Decoder Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Mutation-Based Loss Function",
      "resolved_canonical": "Mutation-Based Loss Function",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.55,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Medical Image Segmentation",
      "resolved_canonical": "Computer Vision",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# An Efficient Dual-Line Decoder Network with Multi-Scale Convolutional Attention for Multi-organ Segmentation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2508.17007.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2508.17007](https://arxiv.org/abs/2508.17007)

## 🔗 유사한 논문
- [[2025-09-22/FMD-TransUNet_ Abdominal Multi-Organ Segmentation Based on Frequency Domain Multi-Axis Representation Learning and Dual Attention Mechanisms_20250922|FMD-TransUNet: Abdominal Multi-Organ Segmentation Based on Frequency Domain Multi-Axis Representation Learning and Dual Attention Mechanisms]] (86.0% similar)
- [[2025-09-22/ENSAM_ an efficient foundation model for interactive segmentation of 3D medical images_20250922|ENSAM: an efficient foundation model for interactive segmentation of 3D medical images]] (85.4% similar)
- [[2025-09-23/R-Net_ A Reliable and Resource-Efficient CNN for Colorectal Cancer Detection with XAI Integration_20250923|R-Net: A Reliable and Resource-Efficient CNN for Colorectal Cancer Detection with XAI Integration]] (84.8% similar)
- [[2025-09-22/DPC-QA Net_ A No-Reference Dual-Stream Perceptual and Cellular Quality Assessment Network for Histopathology Images_20250922|DPC-QA Net: A No-Reference Dual-Stream Perceptual and Cellular Quality Assessment Network for Histopathology Images]] (84.1% similar)
- [[2025-09-22/pFedSAM_ Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation_20250922|pFedSAM: Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation]] (84.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Computer Vision|Computer Vision]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Dual-Line Decoder Network|Dual-Line Decoder Network]], [[keywords/Mutation-Based Loss Function|Mutation-Based Loss Function]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.17007v2 Announce Type: replace-cross 
Abstract: Proper segmentation of organs-at-risk is important for radiation therapy, surgical planning, and diagnostic decision-making in medical image analysis. While deep learning-based segmentation architectures have made significant progress, they often fail to balance segmentation accuracy with computational efficiency. Most of the current state-of-the-art methods either prioritize performance at the cost of high computational complexity or compromise accuracy for efficiency. This paper addresses this gap by introducing an efficient dual-line decoder segmentation network (EDLDNet). The proposed method features a noisy decoder, which learns to incorporate structured perturbation at training time for better model robustness, yet at inference time only the noise-free decoder is executed, leading to lower computational cost. Multi-Scale convolutional Attention Modules (MSCAMs), Attention Gates (AGs), and Up-Convolution Blocks (UCBs) are further utilized to optimize feature representation and boost segmentation performance. By leveraging multi-scale segmentation masks from both decoders, we also utilize a mutation-based loss function to enhance the model's generalization. Our approach outperforms SOTA segmentation architectures on four publicly available medical imaging datasets. EDLDNet achieves SOTA performance with an 84.00% Dice score on the Synapse dataset, surpassing baseline model like UNet by 13.89% in Dice score while significantly reducing Multiply-Accumulate Operations (MACs) by 89.7%. Compared to recent approaches like EMCAD, our EDLDNet not only achieves higher Dice score but also maintains comparable computational efficiency. The outstanding performance across diverse datasets establishes EDLDNet's strong generalization, computational efficiency, and robustness. The source code, pre-processed data, and pre-trained weights will be available at https://github.com/riadhassan/EDLDNet .

## 📝 요약

이 논문은 방사선 치료 및 진단 의사결정에 중요한 장기 위험 기관의 분할 문제를 다루며, 효율적인 이중 라인 디코더 분할 네트워크(EDLDNet)를 제안합니다. 이 방법은 구조적 잡음을 학습하여 모델의 견고성을 높이고, 추론 시에는 잡음 없는 디코더만 실행하여 계산 비용을 줄입니다. 또한, 다중 스케일 합성곱 주의 모듈(MSCAM), 주의 게이트(AG), 업-컨볼루션 블록(UCB)을 활용하여 특징 표현을 최적화하고 성능을 향상시킵니다. EDLDNet은 4개의 공개 의료 이미지 데이터셋에서 최첨단 성능을 보이며, Synapse 데이터셋에서 84.00%의 Dice 점수를 기록하여 UNet보다 13.89% 향상된 성능을 보였습니다. 또한, 계산 효율성을 유지하면서도 EMCAD와 비교하여 더 높은 Dice 점수를 달성합니다. 이 연구는 EDLDNet의 강력한 일반화 능력과 계산 효율성을 입증하며, 소스 코드와 데이터는 GitHub에서 제공될 예정입니다.

## 🎯 주요 포인트

- 1. EDLDNet는 방사선 치료 및 진단 의사 결정에 중요한 장기 위험 기관의 세분화를 효율적으로 수행하는 네트워크입니다.
- 2. 제안된 네트워크는 학습 시 구조적 섭동을 통합하는 노이즈 디코더를 사용하여 모델의 견고성을 높이고, 추론 시에는 노이즈 없는 디코더만 실행하여 계산 비용을 낮춥니다.
- 3. Multi-Scale Convolutional Attention Modules (MSCAMs), Attention Gates (AGs), Up-Convolution Blocks (UCBs)를 활용하여 특징 표현을 최적화하고 세분화 성능을 향상시킵니다.
- 4. EDLDNet는 Synapse 데이터셋에서 84.00%의 Dice 점수를 기록하며, UNet 대비 13.89% 높은 성능을 보이고, MACs를 89.7% 줄였습니다.
- 5. 다양한 데이터셋에서의 뛰어난 성능은 EDLDNet의 강력한 일반화 능력, 계산 효율성 및 견고성을 입증합니다.


---

*Generated on 2025-09-24 01:21:55*