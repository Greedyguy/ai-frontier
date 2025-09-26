---
keywords:
  - Multimodal Learning
  - Vision-Language Model
  - Knowledge Distillation
  - Self-supervised Learning
  - Generative Adversarial Network
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.16017
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:17:36.359005",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Vision-Language Model",
    "Knowledge Distillation",
    "Self-supervised Learning",
    "Generative Adversarial Network"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.82,
    "Vision-Language Model": 0.79,
    "Knowledge Distillation": 0.77,
    "Self-supervised Learning": 0.78,
    "Generative Adversarial Network": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal Image Matching",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Cross-modal Image Matching"
        ],
        "category": "specific_connectable",
        "rationale": "This term is central to the paper's focus on matching images across different modalities, aligning with the concept of Multimodal Learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Vision Foundation Model",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VFM"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision Foundation Models are a key component in the paper, similar to Vision-Language Models in their cross-modal capabilities.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "Knowledge Distillation",
        "canonical": "Knowledge Distillation",
        "aliases": [
          "Model Compression"
        ],
        "category": "broad_technical",
        "rationale": "This technique is crucial for transferring knowledge from large models to smaller ones, a core process in the paper.",
        "novelty_score": 0.47,
        "connectivity_score": 0.83,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "DINOv2",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "DINO",
          "DINOv3"
        ],
        "category": "specific_connectable",
        "rationale": "DINO models are examples of self-supervised learning, which is pivotal for feature extraction in this context.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.76,
        "link_intent_score": 0.78
      },
      {
        "surface": "V2I-GAN",
        "canonical": "Generative Adversarial Network",
        "aliases": [
          "Visible to Infrared GAN"
        ],
        "category": "unique_technical",
        "rationale": "This specific GAN variant is used for data augmentation, enhancing model generalization in the paper.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.74
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
      "candidate_surface": "Multimodal Image Matching",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Vision Foundation Model",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Knowledge Distillation",
      "resolved_canonical": "Knowledge Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.47,
        "connectivity": 0.83,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "DINOv2",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.76,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "V2I-GAN",
      "resolved_canonical": "Generative Adversarial Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# DistillMatch: Leveraging Knowledge Distillation from Vision Foundation Model for Multimodal Image Matching

**Korean Title:** 디스틸매치: 멀티모달 이미지 매칭을 위한 비전 파운데이션 모델의 지식 증류 활용

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16017.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.16017](https://arxiv.org/abs/2509.16017)

## 🔗 유사한 논문
- [[2025-09-22/Efficient Multimodal Dataset Distillation via Generative Models_20250922|Efficient Multimodal Dataset Distillation via Generative Models]] (83.6% similar)
- [[2025-09-19/Multimodal Knowledge Distillation for Egocentric Action Recognition Robust to Missing Modalities_20250919|Multimodal Knowledge Distillation for Egocentric Action Recognition Robust to Missing Modalities]] (83.3% similar)
- [[2025-09-19/MARIC_ Multi-Agent Reasoning for Image Classification_20250919|MARIC: Multi-Agent Reasoning for Image Classification]] (82.4% similar)
- [[2025-09-22/The Moon's Many Faces_ A Single Unified Transformer for Multimodal Lunar Reconstruction_20250922|The Moon's Many Faces: A Single Unified Transformer for Multimodal Lunar Reconstruction]] (81.2% similar)
- [[2025-09-22/Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation_20250922|Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Knowledge Distillation|Knowledge Distillation]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Generative Adversarial Network|Generative Adversarial Network]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16017v1 Announce Type: new 
Abstract: Multimodal image matching seeks pixel-level correspondences between images of different modalities, crucial for cross-modal perception, fusion and analysis. However, the significant appearance differences between modalities make this task challenging. Due to the scarcity of high-quality annotated datasets, existing deep learning methods that extract modality-common features for matching perform poorly and lack adaptability to diverse scenarios. Vision Foundation Model (VFM), trained on large-scale data, yields generalizable and robust feature representations adapted to data and tasks of various modalities, including multimodal matching. Thus, we propose DistillMatch, a multimodal image matching method using knowledge distillation from VFM. DistillMatch employs knowledge distillation to build a lightweight student model that extracts high-level semantic features from VFM (including DINOv2 and DINOv3) to assist matching across modalities. To retain modality-specific information, it extracts and injects modality category information into the other modality's features, which enhances the model's understanding of cross-modal correlations. Furthermore, we design V2I-GAN to boost the model's generalization by translating visible to pseudo-infrared images for data augmentation. Experiments show that DistillMatch outperforms existing algorithms on public datasets.

## 🔍 Abstract (한글 번역)

arXiv:2509.16017v1 발표 유형: 신규  
초록: 다중 모달 이미지 매칭은 서로 다른 모달리티의 이미지 간에 픽셀 수준의 대응을 찾는 작업으로, 교차 모달 인식, 융합 및 분석에 필수적입니다. 그러나 모달리티 간의 상당한 외관 차이로 인해 이 작업은 도전적입니다. 고품질 주석 데이터셋의 부족으로 인해, 매칭을 위한 모달리티 공통 특징을 추출하는 기존의 딥러닝 방법들은 성능이 저조하며 다양한 시나리오에 대한 적응력이 부족합니다. 대규모 데이터로 훈련된 비전 파운데이션 모델(VFM)은 다중 모달 매칭을 포함하여 다양한 모달리티의 데이터와 작업에 적응된 일반적이고 강력한 특징 표현을 제공합니다. 따라서 우리는 VFM으로부터 지식 증류를 사용하는 다중 모달 이미지 매칭 방법인 DistillMatch를 제안합니다. DistillMatch는 VFM(예: DINOv2 및 DINOv3)에서 고수준의 의미적 특징을 추출하여 모달리티 간 매칭을 지원하는 경량 학생 모델을 구축하기 위해 지식 증류를 활용합니다. 모달리티 특유의 정보를 유지하기 위해, 다른 모달리티의 특징에 모달리티 범주 정보를 추출하여 주입함으로써 모델의 교차 모달 상관 관계 이해를 향상시킵니다. 더욱이, 우리는 데이터 증강을 위해 가시 이미지를 가상 적외선 이미지로 변환하여 모델의 일반화를 향상시키는 V2I-GAN을 설계했습니다. 실험 결과, DistillMatch는 공공 데이터셋에서 기존 알고리즘보다 우수한 성능을 보였습니다.

## 📝 요약

다중 모달 이미지 매칭은 서로 다른 모달리티의 이미지 간 픽셀 수준의 대응을 찾는 작업으로, 모달리티 간 인식, 융합 및 분석에 중요합니다. 그러나 모달리티 간의 큰 외관 차이로 인해 이 작업은 어려움을 겪고 있습니다. 기존의 딥러닝 방법은 모달리티 공통 특징을 추출하는 데 한계가 있으며, 다양한 시나리오에 적응하기 어렵습니다. 이에 우리는 대규모 데이터로 학습된 비전 파운데이션 모델(VFM)을 활용한 DistillMatch를 제안합니다. DistillMatch는 VFM으로부터 지식 증류를 통해 경량화된 학생 모델을 구축하여 모달리티 간 매칭을 돕습니다. 또한, 모달리티 고유 정보를 유지하기 위해 모달리티 범주 정보를 다른 모달리티의 특징에 주입하여 상호 모달 상관성을 강화합니다. V2I-GAN을 설계하여 가시 이미지를 가상 적외선 이미지로 변환해 데이터 증강을 통해 모델의 일반화를 향상시킵니다. 실험 결과, DistillMatch는 기존 알고리즘보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 멀티모달 이미지 매칭은 서로 다른 모달리티의 이미지 간 픽셀 수준의 대응을 찾는 작업으로, 모달리티 간 인식, 융합 및 분석에 중요하다.
- 2. 기존의 딥러닝 방법은 고품질의 주석 데이터셋 부족으로 인해 다양한 시나리오에 적응하지 못하고 성능이 저조하다.
- 3. Vision Foundation Model(VFM)은 대규모 데이터로 훈련되어 다양한 모달리티의 데이터와 작업에 적응 가능한 일반적이고 강력한 특징 표현을 제공한다.
- 4. DistillMatch는 VFM으로부터 지식 증류를 활용하여 경량의 학생 모델을 구축하고, 모달리티 간 매칭을 돕기 위해 고수준의 의미적 특징을 추출한다.
- 5. V2I-GAN을 설계하여 가시 이미지를 가상 적외선 이미지로 변환함으로써 데이터 증강을 통해 모델의 일반화를 향상시킨다.


---

*Generated on 2025-09-23 12:17:36*