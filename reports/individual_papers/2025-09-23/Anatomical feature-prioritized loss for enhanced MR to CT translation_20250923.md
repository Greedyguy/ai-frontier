---
keywords:
  - Anatomical Feature-Prioritized Loss
  - MR to CT Translation
  - Generative Adversarial Networks
  - Pre-trained Segmentation Models
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2410.10328
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:33:57.983947",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Anatomical Feature-Prioritized Loss",
    "MR to CT Translation",
    "Generative Adversarial Networks",
    "Pre-trained Segmentation Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Anatomical Feature-Prioritized Loss": 0.8,
    "MR to CT Translation": 0.78,
    "Generative Adversarial Networks": 0.72,
    "Pre-trained Segmentation Models": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "anatomical feature-prioritized loss",
        "canonical": "Anatomical Feature-Prioritized Loss",
        "aliases": [
          "AFP loss"
        ],
        "category": "unique_technical",
        "rationale": "This novel loss function is central to the paper's contribution, enhancing the specificity of medical image synthesis.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "MR to CT translation",
        "canonical": "MR to CT Translation",
        "aliases": [
          "MRI to CT conversion"
        ],
        "category": "specific_connectable",
        "rationale": "This process is a key application area for the proposed method, relevant to medical imaging research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "GAN-based models",
        "canonical": "Generative Adversarial Networks",
        "aliases": [
          "GANs"
        ],
        "category": "broad_technical",
        "rationale": "GANs are a fundamental technology in image synthesis, providing a basis for the proposed method.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      },
      {
        "surface": "pre-trained segmentation models",
        "canonical": "Pre-trained Segmentation Models",
        "aliases": [
          "segmentation networks"
        ],
        "category": "specific_connectable",
        "rationale": "These models are crucial for extracting anatomical features, directly supporting the paper's methodology.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "image reconstruction",
      "synthesis networks"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "anatomical feature-prioritized loss",
      "resolved_canonical": "Anatomical Feature-Prioritized Loss",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "MR to CT translation",
      "resolved_canonical": "MR to CT Translation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "GAN-based models",
      "resolved_canonical": "Generative Adversarial Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "pre-trained segmentation models",
      "resolved_canonical": "Pre-trained Segmentation Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Anatomical feature-prioritized loss for enhanced MR to CT translation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2410.10328.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2410.10328](https://arxiv.org/abs/2410.10328)

## 🔗 유사한 논문
- [[2025-09-23/Semantic and Visual Crop-Guided Diffusion Models for Heterogeneous Tissue Synthesis in Histopathology_20250923|Semantic and Visual Crop-Guided Diffusion Models for Heterogeneous Tissue Synthesis in Histopathology]] (83.4% similar)
- [[2025-09-22/Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images_20250922|Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images]] (82.8% similar)
- [[2025-09-22/Prostate Capsule Segmentation from Micro-Ultrasound Images using Adaptive Focal Loss_20250922|Prostate Capsule Segmentation from Micro-Ultrasound Images using Adaptive Focal Loss]] (82.7% similar)
- [[2025-09-22/SLaM-DiMM_ Shared Latent Modeling for Diffusion Based Missing Modality Synthesis in MRI_20250922|SLaM-DiMM: Shared Latent Modeling for Diffusion Based Missing Modality Synthesis in MRI]] (82.0% similar)
- [[2025-09-23/Interpretability-Aware Pruning for Efficient Medical Image Analysis_20250923|Interpretability-Aware Pruning for Efficient Medical Image Analysis]] (81.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Generative Adversarial Networks|Generative Adversarial Networks]]
**🔗 Specific Connectable**: [[keywords/MR to CT Translation|MR to CT Translation]], [[keywords/Pre-trained Segmentation Models|Pre-trained Segmentation Models]]
**⚡ Unique Technical**: [[keywords/Anatomical Feature-Prioritized Loss|Anatomical Feature-Prioritized Loss]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2410.10328v3 Announce Type: replace-cross 
Abstract: In medical image synthesis, the precision of localized structural details is crucial, particularly when addressing specific clinical requirements such as the identification and measurement of fine structures. Traditional methods for image translation and synthesis are generally optimized for global image reconstruction but often fall short in providing the finesse required for detailed local analysis. This study represents a step toward addressing this challenge by introducing a novel anatomical feature-prioritized (AFP) loss function into the synthesis process. This method enhances reconstruction by focusing on clinically significant structures, utilizing features from a pre-trained model designed for a specific downstream task, such as the segmentation of particular anatomical regions. The AFP loss function can replace or complement global reconstruction methods, ensuring a balanced emphasis on both global image fidelity and local structural details. Various implementations of this loss function are explored, including its integration into different synthesis networks such as GAN-based and CNN-based models. Our approach is applied and evaluated in two contexts: lung MR to CT translation, focusing on high-quality reconstruction of bronchial structures, using a private dataset; and pelvis MR to CT synthesis, targeting the accurate representation of organs and muscles, utilizing a public dataset from the Synthrad2023 challenge. We leverage embeddings from pre-trained segmentation models specific to these anatomical regions to demonstrate the capability of the AFP loss to prioritize and accurately reconstruct essential features. This tailored approach shows promising potential for enhancing the specificity and practicality of medical image synthesis in clinical applications.

## 📝 요약

이 연구는 의료 영상 합성에서 국부적 구조 세부 사항의 정밀성을 향상시키기 위해 새로운 해부학적 특징 우선(AFP) 손실 함수를 도입했습니다. 이 방법은 특정 해부학적 영역의 분할과 같은 다운스트림 작업을 위해 사전 훈련된 모델의 특징을 활용하여 임상적으로 중요한 구조에 중점을 둡니다. AFP 손실 함수는 전통적인 전역 재구성 방법을 대체하거나 보완하여 전역 이미지 충실도와 국부적 구조 세부 사항 간의 균형을 맞춥니다. 이 연구는 GAN 및 CNN 기반 모델 등 다양한 합성 네트워크에 AFP 손실 함수를 통합하여 폐 MR에서 CT로의 변환과 골반 MR에서 CT 합성에 적용했습니다. 이 방법은 특정 해부학적 영역에 대한 사전 훈련된 분할 모델의 임베딩을 활용하여 필수 특징을 정확하게 재구성하는 능력을 입증하며, 임상 응용에서 의료 영상 합성의 특이성과 실용성을 향상시킬 가능성을 보여줍니다.

## 🎯 주요 포인트

- 1. 본 연구는 의료 영상 합성에서 국부적 구조 세부 사항의 정밀성을 향상시키기 위해 새로운 해부학적 특징 우선(AFP) 손실 함수를 도입했습니다.
- 2. AFP 손실 함수는 특정 해부학적 영역의 분할과 같은 다운스트림 작업을 위해 설계된 사전 학습된 모델의 특징을 활용하여 임상적으로 중요한 구조에 중점을 둡니다.
- 3. 이 방법은 GAN 기반 및 CNN 기반 모델과 같은 다양한 합성 네트워크에 통합되어 전역 이미지 충실도와 국부적 구조 세부 사항 간의 균형을 보장합니다.
- 4. 연구는 폐 MR에서 CT로의 변환과 골반 MR에서 CT 합성에 적용되어 각각 기관지 구조와 장기 및 근육의 정확한 재현을 목표로 합니다.
- 5. AFP 손실 함수는 특정 해부학적 영역에 대한 사전 학습된 분할 모델의 임베딩을 활용하여 필수 특징을 우선적으로 정확하게 재구성할 수 있음을 입증합니다.


---

*Generated on 2025-09-24 05:33:57*