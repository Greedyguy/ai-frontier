---
keywords:
  - 3D Medical Object Detection
  - Pre-training
  - Self-supervised Learning
  - Neural Network
  - Reconstruction-based Self-supervised Learning
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15947
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:54:51.454059",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Medical Object Detection",
    "Pre-training",
    "Self-supervised Learning",
    "Neural Network",
    "Reconstruction-based Self-supervised Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Medical Object Detection": 0.78,
    "Pre-training": 0.72,
    "Self-supervised Learning": 0.85,
    "Neural Network": 0.8,
    "Reconstruction-based Self-supervised Learning": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "3D medical object detection",
        "canonical": "3D Medical Object Detection",
        "aliases": [
          "3D object detection in medical imaging"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application area that connects with advancements in medical imaging and AI.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "pre-training",
        "canonical": "Pre-training",
        "aliases": [
          "pretraining"
        ],
        "category": "broad_technical",
        "rationale": "Pre-training is a foundational concept in machine learning, relevant across various domains.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.72
      },
      {
        "surface": "self-supervised pre-training",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "self-supervised pretraining"
        ],
        "category": "specific_connectable",
        "rationale": "Self-supervised learning is a trending approach that enhances model performance without labeled data.",
        "novelty_score": 0.55,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "CNNs and Transformers",
        "canonical": "Neural Network",
        "aliases": [
          "Convolutional Neural Networks",
          "Transformers"
        ],
        "category": "broad_technical",
        "rationale": "These are key architectures in deep learning, widely applicable across various tasks.",
        "novelty_score": 0.4,
        "connectivity_score": 0.92,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "reconstruction-based self-supervised pre-training",
        "canonical": "Reconstruction-based Self-supervised Learning",
        "aliases": [
          "reconstruction-based pretraining"
        ],
        "category": "unique_technical",
        "rationale": "This specific method shows superior performance in the study, indicating its importance.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.82
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
      "candidate_surface": "3D medical object detection",
      "resolved_canonical": "3D Medical Object Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "pre-training",
      "resolved_canonical": "Pre-training",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.6,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "self-supervised pre-training",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "CNNs and Transformers",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.92,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "reconstruction-based self-supervised pre-training",
      "resolved_canonical": "Reconstruction-based Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# The Missing Piece: A Case for Pre-Training in 3D Medical Object Detection

**Korean Title:** 누락된 조각: 3D 의료 객체 탐지에서 사전 훈련의 필요성에 대한 사례

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15947.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15947](https://arxiv.org/abs/2509.15947)

## 🔗 유사한 논문
- [[2025-09-22/Sparse Multiview Open-Vocabulary 3D Detection_20250922|Sparse Multiview Open-Vocabulary 3D Detection]] (83.9% similar)
- [[2025-09-18/Semi-Supervised 3D Medical Segmentation from 2D Natural Images Pretrained Model_20250918|Semi-Supervised 3D Medical Segmentation from 2D Natural Images Pretrained Model]] (81.7% similar)
- [[2025-09-22/Screener_ Self-supervised Pathology Segmentation in Medical CT Images_20250922|Screener: Self-supervised Pathology Segmentation in Medical CT Images]] (81.3% similar)
- [[2025-09-22/PAN_ Pillars-Attention-Based Network for 3D Object Detection_20250922|PAN: Pillars-Attention-Based Network for 3D Object Detection]] (81.1% similar)
- [[2025-09-22/SegDINO3D_ 3D Instance Segmentation Empowered by Both Image-Level and Object-Level 2D Features_20250922|SegDINO3D: 3D Instance Segmentation Empowered by Both Image-Level and Object-Level 2D Features]] (81.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Pre-training|Pre-training]], [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/3D Medical Object Detection|3D Medical Object Detection]], [[keywords/Reconstruction-based Self-supervised Learning|Reconstruction-based Self-supervised Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15947v1 Announce Type: cross 
Abstract: Large-scale pre-training holds the promise to advance 3D medical object detection, a crucial component of accurate computer-aided diagnosis. Yet, it remains underexplored compared to segmentation, where pre-training has already demonstrated significant benefits. Existing pre-training approaches for 3D object detection rely on 2D medical data or natural image pre-training, failing to fully leverage 3D volumetric information. In this work, we present the first systematic study of how existing pre-training methods can be integrated into state-of-the-art detection architectures, covering both CNNs and Transformers. Our results show that pre-training consistently improves detection performance across various tasks and datasets. Notably, reconstruction-based self-supervised pre-training outperforms supervised pre-training, while contrastive pre-training provides no clear benefit for 3D medical object detection. Our code is publicly available at: https://github.com/MIC-DKFZ/nnDetection-finetuning.

## 🔍 Abstract (한글 번역)

arXiv:2509.15947v1 발표 유형: 교차  
초록: 대규모 사전 학습은 정확한 컴퓨터 보조 진단의 중요한 구성 요소인 3D 의료 객체 탐지를 발전시킬 가능성을 가지고 있습니다. 그러나 사전 학습이 이미 상당한 이점을 입증한 세분화에 비해 여전히 충분히 탐구되지 않았습니다. 기존의 3D 객체 탐지를 위한 사전 학습 접근법은 2D 의료 데이터 또는 자연 이미지 사전 학습에 의존하여 3D 볼륨 정보를 완전히 활용하지 못하고 있습니다. 본 연구에서는 기존 사전 학습 방법을 최첨단 탐지 아키텍처에 통합할 수 있는 방법에 대한 최초의 체계적인 연구를 제시하며, CNN과 트랜스포머를 모두 다룹니다. 우리의 결과는 사전 학습이 다양한 작업과 데이터셋에서 탐지 성능을 일관되게 향상시킨다는 것을 보여줍니다. 특히, 재구성 기반의 자가 지도 사전 학습이 지도 사전 학습보다 우수한 성능을 보이며, 대조적 사전 학습은 3D 의료 객체 탐지에 명확한 이점을 제공하지 않는 것으로 나타났습니다. 우리의 코드는 다음에서 공개적으로 이용 가능합니다: https://github.com/MIC-DKFZ/nnDetection-finetuning.

## 📝 요약

이 논문은 3D 의료 객체 탐지 분야에서 대규모 사전 학습의 잠재력을 탐구합니다. 기존의 3D 객체 탐지 사전 학습 방법이 2D 의료 데이터나 자연 이미지에 의존하는 한계를 극복하기 위해, CNN과 트랜스포머를 포함한 최신 탐지 아키텍처에 사전 학습 방법을 통합하는 체계적인 연구를 수행했습니다. 연구 결과, 사전 학습은 다양한 작업과 데이터셋에서 탐지 성능을 일관되게 향상시켰으며, 특히 재구성 기반의 자가 지도 사전 학습이 지도 학습을 능가하는 성과를 보였습니다. 반면, 대조 학습은 3D 의료 객체 탐지에 명확한 이점을 제공하지 않았습니다. 연구에 사용된 코드는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 대규모 사전 학습은 3D 의료 객체 탐지의 발전 가능성을 지니고 있으며, 이는 정확한 컴퓨터 보조 진단의 중요한 요소이다.
- 2. 기존의 3D 객체 탐지를 위한 사전 학습 방법은 2D 의료 데이터나 자연 이미지 사전 학습에 의존하여 3D 볼륨 정보를 충분히 활용하지 못하고 있다.
- 3. 본 연구는 기존 사전 학습 방법을 최첨단 탐지 아키텍처에 통합하는 체계적인 연구를 처음으로 제시하며, CNN과 트랜스포머를 모두 다룬다.
- 4. 사전 학습은 다양한 작업과 데이터셋에서 탐지 성능을 일관되게 향상시키며, 특히 재구성 기반의 자가 지도 사전 학습이 지도 사전 학습보다 우수한 성능을 보인다.
- 5. 대조적 사전 학습은 3D 의료 객체 탐지에 명확한 이점을 제공하지 못한다.


---

*Generated on 2025-09-23 10:54:51*