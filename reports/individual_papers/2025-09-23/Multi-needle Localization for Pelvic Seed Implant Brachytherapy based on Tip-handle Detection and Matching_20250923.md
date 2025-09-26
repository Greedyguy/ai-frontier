---
keywords:
  - Multi-needle Localization
  - HRNet
  - Greedy Matching and Merging
  - Seed Implant Brachytherapy
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17931
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:06:07.853142",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-needle Localization",
    "HRNet",
    "Greedy Matching and Merging",
    "Seed Implant Brachytherapy"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multi-needle Localization": 0.78,
    "HRNet": 0.82,
    "Greedy Matching and Merging": 0.77,
    "Seed Implant Brachytherapy": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "multi-needle localization",
        "canonical": "Multi-needle Localization",
        "aliases": [
          "needle localization",
          "needle detection"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's contribution and represents a specific technical challenge in medical imaging.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "HRNet",
        "canonical": "HRNet",
        "aliases": [
          "High-Resolution Network"
        ],
        "category": "specific_connectable",
        "rationale": "HRNet is a known architecture in computer vision, facilitating connections with other works using similar models.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "greedy matching and merging",
        "canonical": "Greedy Matching and Merging",
        "aliases": [
          "GMM method"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel method introduced in the paper, crucial for solving the unbalanced assignment problem in the context discussed.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      },
      {
        "surface": "seed implant brachytherapy",
        "canonical": "Seed Implant Brachytherapy",
        "aliases": [
          "pelvic seed implant"
        ],
        "category": "unique_technical",
        "rationale": "This term specifies the medical application context, which is essential for linking to related medical imaging and treatment research.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "multi-needle localization",
      "resolved_canonical": "Multi-needle Localization",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "HRNet",
      "resolved_canonical": "HRNet",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "greedy matching and merging",
      "resolved_canonical": "Greedy Matching and Merging",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "seed implant brachytherapy",
      "resolved_canonical": "Seed Implant Brachytherapy",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Multi-needle Localization for Pelvic Seed Implant Brachytherapy based on Tip-handle Detection and Matching

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17931.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17931](https://arxiv.org/abs/2509.17931)

## 🔗 유사한 논문
- [[2025-09-22/Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images_20250922|Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images]] (84.3% similar)
- [[2025-09-23/Automated Labeling of Intracranial Arteries with Uncertainty Quantification Using Deep Learning_20250923|Automated Labeling of Intracranial Arteries with Uncertainty Quantification Using Deep Learning]] (83.7% similar)
- [[2025-09-23/Block-Fused Attention-Driven Adaptively-Pooled ResNet Model for Improved Cervical Cancer Classification_20250923|Block-Fused Attention-Driven Adaptively-Pooled ResNet Model for Improved Cervical Cancer Classification]] (82.2% similar)
- [[2025-09-23/An Efficient Dual-Line Decoder Network with Multi-Scale Convolutional Attention for Multi-organ Segmentation_20250923|An Efficient Dual-Line Decoder Network with Multi-Scale Convolutional Attention for Multi-organ Segmentation]] (82.1% similar)
- [[2025-09-23/R-Net_ A Reliable and Resource-Efficient CNN for Colorectal Cancer Detection with XAI Integration_20250923|R-Net: A Reliable and Resource-Efficient CNN for Colorectal Cancer Detection with XAI Integration]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/HRNet|HRNet]]
**⚡ Unique Technical**: [[keywords/Multi-needle Localization|Multi-needle Localization]], [[keywords/Greedy Matching and Merging|Greedy Matching and Merging]], [[keywords/Seed Implant Brachytherapy|Seed Implant Brachytherapy]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17931v1 Announce Type: new 
Abstract: Accurate multi-needle localization in intraoperative CT images is crucial for optimizing seed placement in pelvic seed implant brachytherapy. However, this task is challenging due to poor image contrast and needle adhesion. This paper presents a novel approach that reframes needle localization as a tip-handle detection and matching problem to overcome these difficulties. An anchor-free network, based on HRNet, is proposed to extract multi-scale features and accurately detect needle tips and handles by predicting their centers and orientations using decoupled branches for heatmap regression and polar angle prediction. To associate detected tips and handles into individual needles, a greedy matching and merging (GMM) method designed to solve the unbalanced assignment problem with constraints (UAP-C) is presented. The GMM method iteratively selects the most probable tip-handle pairs and merges them based on a distance metric to reconstruct 3D needle paths. Evaluated on a dataset of 100 patients, the proposed method demonstrates superior performance, achieving higher precision and F1 score compared to a segmentation-based method utilizing the nnUNet model,thereby offering a more robust and accurate solution for needle localization in complex clinical scenarios.

## 📝 요약

이 논문은 골반 씨앗 삽입 근접치료에서 바늘의 정확한 위치를 찾는 문제를 해결하기 위해 새로운 접근 방식을 제안합니다. 기존의 이미지 대비와 바늘 부착 문제를 극복하기 위해 바늘 위치 찾기를 팁-핸들 감지 및 매칭 문제로 재구성했습니다. HRNet 기반의 앵커 프리 네트워크를 사용하여 바늘 팁과 핸들의 중심과 방향을 예측하는 방법을 제안합니다. 또한, 탐지된 팁과 핸들을 개별 바늘로 연결하기 위해 제약이 있는 불균형 할당 문제(UAP-C)를 해결하는 탐욕적 매칭 및 병합(GMM) 방법을 소개합니다. 100명의 환자 데이터를 평가한 결과, 제안된 방법은 nnUNet 모델을 사용하는 세분화 기반 방법보다 높은 정밀도와 F1 점수를 달성하여 복잡한 임상 시나리오에서 바늘 위치 찾기에 더 강력하고 정확한 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. 본 연구는 골반 씨앗 이식 근접치료에서 바늘 위치를 최적화하기 위해 바늘 위치 추정을 팁-핸들 탐지 및 매칭 문제로 재구성하는 새로운 접근 방식을 제안합니다.
- 2. HRNet 기반의 앵커 프리 네트워크를 사용하여 멀티 스케일 특징을 추출하고, 히트맵 회귀와 극각 예측을 통해 바늘 팁과 핸들의 중심과 방향을 정확하게 예측합니다.
- 3. 탐지된 팁과 핸들을 개별 바늘로 연결하기 위해 제약이 있는 불균형 할당 문제(UAP-C)를 해결하는 탐욕적 매칭 및 병합(GMM) 방법을 제안합니다.
- 4. 제안된 방법은 100명의 환자 데이터셋에서 평가되었으며, nnUNet 모델을 사용하는 세분화 기반 방법보다 높은 정밀도와 F1 점수를 달성하여 복잡한 임상 시나리오에서 바늘 위치 추정의 강력하고 정확한 솔루션을 제공합니다.


---

*Generated on 2025-09-24 05:06:07*