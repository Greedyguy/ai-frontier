---
keywords:
  - Micro-ultrasound Imaging
  - Prostate Capsule Segmentation
  - Adaptive Focal Loss Function
  - Deep Learning
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15595
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:24:12.063354",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Micro-ultrasound Imaging",
    "Prostate Capsule Segmentation",
    "Adaptive Focal Loss Function",
    "Deep Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Micro-ultrasound Imaging": 0.78,
    "Prostate Capsule Segmentation": 0.8,
    "Adaptive Focal Loss Function": 0.82,
    "Deep Learning": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Micro-ultrasound",
        "canonical": "Micro-ultrasound Imaging",
        "aliases": [
          "micro-US"
        ],
        "category": "unique_technical",
        "rationale": "Micro-ultrasound is a specific imaging technique crucial for prostate cancer detection, offering unique insights into the field.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Prostate Capsule Segmentation",
        "canonical": "Prostate Capsule Segmentation",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is the primary focus of the study, providing a specific application of deep learning in medical imaging.",
        "novelty_score": 0.7,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Adaptive Focal Loss",
        "canonical": "Adaptive Focal Loss Function",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The adaptive focal loss function is a novel approach introduced in the paper, enhancing segmentation accuracy.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.82
      },
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Deep learning is the foundational technology used in the study, connecting it to a broad range of related research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
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
      "candidate_surface": "Micro-ultrasound",
      "resolved_canonical": "Micro-ultrasound Imaging",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Prostate Capsule Segmentation",
      "resolved_canonical": "Prostate Capsule Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Adaptive Focal Loss",
      "resolved_canonical": "Adaptive Focal Loss Function",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Deep Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Prostate Capsule Segmentation from Micro-Ultrasound Images using Adaptive Focal Loss

**Korean Title:** 마이크로 초음파 영상에서 적응형 포컬 손실을 이용한 전립선 캡슐 분할

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15595.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15595](https://arxiv.org/abs/2509.15595)

## 🔗 유사한 논문
- [[2025-09-22/Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images_20250922|Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images]] (82.7% similar)
- [[2025-09-19/Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2_ Atypical Mitosis Classification_20250919|Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2: Atypical Mitosis Classification]] (80.6% similar)
- [[2025-09-22/MIDOG 2025_ Mitotic Figure Detection with Attention-Guided False Positive Correction_20250922|MIDOG 2025: Mitotic Figure Detection with Attention-Guided False Positive Correction]] (80.6% similar)
- [[2025-09-22/Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation_20250922|Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation]] (80.4% similar)
- [[2025-09-22/pFedSAM_ Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation_20250922|pFedSAM: Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation]] (80.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**⚡ Unique Technical**: [[keywords/Micro-ultrasound Imaging|Micro-ultrasound Imaging]], [[keywords/Prostate Capsule Segmentation|Prostate Capsule Segmentation]], [[keywords/Adaptive Focal Loss Function|Adaptive Focal Loss Function]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15595v1 Announce Type: cross 
Abstract: Micro-ultrasound (micro-US) is a promising imaging technique for cancer detection and computer-assisted visualization. This study investigates prostate capsule segmentation using deep learning techniques from micro-US images, addressing the challenges posed by the ambiguous boundaries of the prostate capsule. Existing methods often struggle in such cases, motivating the development of a tailored approach. This study introduces an adaptive focal loss function that dynamically emphasizes both hard and easy regions, taking into account their respective difficulty levels and annotation variability. The proposed methodology has two primary strategies: integrating a standard focal loss function as a baseline to design an adaptive focal loss function for proper prostate capsule segmentation. The focal loss baseline provides a robust foundation, incorporating class balancing and focusing on examples that are difficult to classify. The adaptive focal loss offers additional flexibility, addressing the fuzzy region of the prostate capsule and annotation variability by dilating the hard regions identified through discrepancies between expert and non-expert annotations. The proposed method dynamically adjusts the segmentation model's weights better to identify the fuzzy regions of the prostate capsule. The proposed adaptive focal loss function demonstrates superior performance, achieving a mean dice coefficient (DSC) of 0.940 and a mean Hausdorff distance (HD) of 1.949 mm in the testing dataset. These results highlight the effectiveness of integrating advanced loss functions and adaptive techniques into deep learning models. This enhances the accuracy of prostate capsule segmentation in micro-US images, offering the potential to improve clinical decision-making in prostate cancer diagnosis and treatment planning.

## 🔍 Abstract (한글 번역)

arXiv:2509.15595v1 발표 유형: 교차  
초록: 마이크로 초음파(micro-US)는 암 탐지 및 컴퓨터 지원 시각화를 위한 유망한 영상 기법입니다. 본 연구는 마이크로 초음파 이미지를 활용한 심층 학습 기법을 통해 전립선 피막 분할을 조사하며, 전립선 피막의 모호한 경계로 인한 문제를 해결합니다. 기존 방법들은 이러한 경우에 종종 어려움을 겪으며, 이를 해결하기 위해 맞춤형 접근법의 개발이 필요합니다. 본 연구는 난이도 수준과 주석 변동성을 고려하여 어려운 영역과 쉬운 영역 모두에 동적으로 강조를 두는 적응형 포컬 손실 함수를 소개합니다. 제안된 방법론은 두 가지 주요 전략을 가지고 있습니다: 표준 포컬 손실 함수를 통합하여 적응형 포컬 손실 함수를 설계하고, 이를 통해 적절한 전립선 피막 분할을 수행합니다. 포컬 손실 기준선은 클래스 균형을 포함하고 분류하기 어려운 예제에 집중하여 견고한 기반을 제공합니다. 적응형 포컬 손실은 추가적인 유연성을 제공하며, 전문가와 비전문가 주석 간의 불일치를 통해 식별된 어려운 영역을 확장함으로써 전립선 피막의 모호한 영역과 주석 변동성을 해결합니다. 제안된 방법은 전립선 피막의 모호한 영역을 더 잘 식별하기 위해 분할 모델의 가중치를 동적으로 조정합니다. 제안된 적응형 포컬 손실 함수는 테스트 데이터셋에서 평균 다이스 계수(DSC) 0.940과 평균 하우스도르프 거리(HD) 1.949 mm를 달성하며 우수한 성능을 입증합니다. 이러한 결과는 심층 학습 모델에 고급 손실 함수와 적응형 기술을 통합하는 것이 효과적임을 강조합니다. 이는 마이크로 초음파 이미지에서 전립선 피막 분할의 정확성을 향상시키며, 전립선 암 진단 및 치료 계획에서 임상적 의사 결정을 개선할 잠재력을 제공합니다.

## 📝 요약

이 연구는 마이크로 초음파(micro-US) 이미지를 활용한 전립선 피막 분할을 위해 심층 학습 기법을 적용하여, 모호한 경계 문제를 해결하고자 합니다. 기존 방법의 한계를 극복하기 위해, 연구진은 적응형 포컬 손실 함수(adaptive focal loss function)를 도입했습니다. 이 함수는 난이도와 주석의 변동성을 고려하여 어려운 영역과 쉬운 영역을 동적으로 강조합니다. 제안된 방법론은 표준 포컬 손실 함수를 기반으로 하여 적응형 포컬 손실 함수를 설계하고, 전문가와 비전문가 주석 간의 차이를 통해 식별된 어려운 영역을 확장함으로써 모호한 전립선 피막 영역을 효과적으로 식별합니다. 이 방법은 평균 다이스 계수(DSC) 0.940과 평균 하우스도르프 거리(HD) 1.949 mm를 달성하여 우수한 성능을 보였습니다. 이는 심층 학습 모델에 고급 손실 함수와 적응형 기법을 통합함으로써 전립선 암 진단 및 치료 계획에서 임상적 의사 결정을 개선할 수 있는 가능성을 제시합니다.

## 🎯 주요 포인트

- 1. 본 연구는 미세 초음파 이미지를 활용하여 전립선 캡슐의 경계를 명확히 구분하기 위한 심층 학습 기술을 조사합니다.
- 2. 기존 방법이 전립선 캡슐의 모호한 경계에서 어려움을 겪는 문제를 해결하기 위해 적응형 포컬 손실 함수를 도입했습니다.
- 3. 제안된 방법론은 표준 포컬 손실 함수를 기반으로 적응형 포컬 손실 함수를 설계하여 전립선 캡슐의 정확한 분할을 목표로 합니다.
- 4. 적응형 포컬 손실 함수는 전문가와 비전문가 주석 간의 불일치를 통해 식별된 어려운 영역을 확장하여 모호한 영역을 더 잘 식별합니다.
- 5. 제안된 방법은 테스트 데이터셋에서 평균 dice 계수 0.940과 평균 Hausdorff 거리 1.949 mm를 달성하여 전립선 캡슐 분할의 정확성을 향상시킵니다.


---

*Generated on 2025-09-23 12:24:12*