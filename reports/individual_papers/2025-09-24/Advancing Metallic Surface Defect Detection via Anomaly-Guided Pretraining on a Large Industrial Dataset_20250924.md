<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:12:43.256865",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Anomaly-Guided Self-Supervised Pretraining",
    "Metallic Surface Defect Detection",
    "Self-supervised Learning",
    "Anomaly Maps"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Anomaly-Guided Self-Supervised Pretraining": 0.78,
    "Metallic Surface Defect Detection": 0.77,
    "Self-supervised Learning": 0.82,
    "Anomaly Maps": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Anomaly-Guided Self-Supervised Pretraining",
        "canonical": "Anomaly-Guided Self-Supervised Pretraining",
        "aliases": [
          "AGSSP"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach to self-supervised learning specifically tailored for defect detection, enhancing domain-specific connections.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Metallic Surface Defect Detection",
        "canonical": "Metallic Surface Defect Detection",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Focuses on a specific application area within computer vision, facilitating targeted discussions and research connections.",
        "novelty_score": 0.72,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Self-supervised Learning",
        "canonical": "Self-supervised Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A key methodology in the paper, linking it to broader trends in machine learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Anomaly Maps",
        "canonical": "Anomaly Maps",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Central to the proposed method, these maps are crucial for guiding the pretraining process.",
        "novelty_score": 0.68,
        "connectivity_score": 0.5,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "pretraining",
      "finetuning",
      "ImageNet",
      "industrial dataset"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Anomaly-Guided Self-Supervised Pretraining",
      "resolved_canonical": "Anomaly-Guided Self-Supervised Pretraining",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Metallic Surface Defect Detection",
      "resolved_canonical": "Metallic Surface Defect Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Self-supervised Learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Anomaly Maps",
      "resolved_canonical": "Anomaly Maps",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.5,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Advancing Metallic Surface Defect Detection via Anomaly-Guided Pretraining on a Large Industrial Dataset

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18919.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18919](https://arxiv.org/abs/2509.18919)

## 🔗 유사한 논문
- [[2025-09-22/ISP-AD_ A Large-Scale Real-World Dataset for Advancing Industrial Anomaly Detection with Synthetic and Real Defects_20250922|ISP-AD: A Large-Scale Real-World Dataset for Advancing Industrial Anomaly Detection with Synthetic and Real Defects]] (83.5% similar)
- [[2025-09-22/The Missing Piece_ A Case for Pre-Training in 3D Medical Object Detection_20250922|The Missing Piece: A Case for Pre-Training in 3D Medical Object Detection]] (83.4% similar)
- [[2025-09-24/A Single Image Is All You Need_ Zero-Shot Anomaly Localization Without Training Data_20250924|A Single Image Is All You Need: Zero-Shot Anomaly Localization Without Training Data]] (83.3% similar)
- [[2025-09-23/Enhancing Semantic Segmentation with Continual Self-Supervised Pre-training_20250923|Enhancing Semantic Segmentation with Continual Self-Supervised Pre-training]] (81.4% similar)
- [[2025-09-18/Pre-training under infinite compute_20250918|Pre-training under infinite compute]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Anomaly-Guided Self-Supervised Pretraining|Anomaly-Guided Self-Supervised Pretraining]], [[keywords/Metallic Surface Defect Detection|Metallic Surface Defect Detection]], [[keywords/Anomaly Maps|Anomaly Maps]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18919v1 Announce Type: new 
Abstract: The pretraining-finetuning paradigm is a crucial strategy in metallic surface defect detection for mitigating the challenges posed by data scarcity. However, its implementation presents a critical dilemma. Pretraining on natural image datasets such as ImageNet, faces a significant domain gap. Meanwhile, naive self-supervised pretraining on in-domain industrial data is often ineffective due to the inability of existing learning objectives to distinguish subtle defect patterns from complex background noise and textures. To resolve this, we introduce Anomaly-Guided Self-Supervised Pretraining (AGSSP), a novel paradigm that explicitly guides representation learning through anomaly priors. AGSSP employs a two-stage framework: (1) it first pretrains the model's backbone by distilling knowledge from anomaly maps, encouraging the network to capture defect-salient features; (2) it then pretrains the detector using pseudo-defect boxes derived from these maps, aligning it with localization tasks. To enable this, we develop a knowledge-enhanced method to generate high-quality anomaly maps and collect a large-scale industrial dataset of 120,000 images. Additionally, we present two small-scale, pixel-level labeled metallic surface defect datasets for validation. Extensive experiments demonstrate that AGSSP consistently enhances performance across various settings, achieving up to a 10\% improvement in mAP@0.5 and 11.4\% in mAP@0.5:0.95 compared to ImageNet-based models. All code, pretrained models, and datasets are publicly available at https://clovermini.github.io/AGSSP-Dev/.

## 📝 요약

이 논문은 금속 표면 결함 탐지를 위한 사전 학습-미세 조정 패러다임의 문제를 해결하기 위해 Anomaly-Guided Self-Supervised Pretraining (AGSSP)라는 새로운 방법론을 제안합니다. 기존의 자연 이미지 데이터셋을 활용한 사전 학습은 도메인 차이로 인해 효과적이지 않으며, 단순한 자가 지도 학습은 복잡한 배경 노이즈와 텍스처로 인해 결함 패턴을 잘 구별하지 못합니다. AGSSP는 이상 지도 학습을 통해 표현 학습을 명시적으로 유도하는 두 단계의 프레임워크를 사용합니다. 첫 번째 단계에서는 이상 지도에서 지식을 추출하여 모델의 백본을 사전 학습하고, 두 번째 단계에서는 의사 결함 상자를 사용하여 탐지기를 사전 학습합니다. 이를 위해 고품질의 이상 지도를 생성하는 방법과 12만 장의 대규모 산업 데이터셋을 개발했습니다. 실험 결과, AGSSP는 다양한 설정에서 성능을 향상시켜, ImageNet 기반 모델 대비 mAP@0.5에서 최대 10%, mAP@0.5:0.95에서 11.4%의 개선을 보였습니다. 모든 코드와 데이터셋은 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 금속 표면 결함 검출에서 데이터 부족 문제를 해결하기 위해 사전 학습-미세 조정 패러다임이 중요하다.
- 2. 자연 이미지 데이터셋을 사용한 사전 학습은 도메인 차이로 인해 한계가 있다.
- 3. AGSSP는 이상 탐지 지도를 활용하여 결함을 강조하는 특징을 학습하도록 유도하는 새로운 패러다임이다.
- 4. AGSSP는 두 단계로 구성되며, 이상 탐지 지도에서 지식을 추출하여 모델의 백본을 사전 학습하고, 가상 결함 상자를 사용하여 탐지기를 사전 학습한다.
- 5. AGSSP는 다양한 설정에서 성능을 향상시키며, ImageNet 기반 모델에 비해 최대 10%의 mAP@0.5 및 11.4%의 mAP@0.5:0.95 개선을 달성한다.


---

*Generated on 2025-09-24 16:12:43*