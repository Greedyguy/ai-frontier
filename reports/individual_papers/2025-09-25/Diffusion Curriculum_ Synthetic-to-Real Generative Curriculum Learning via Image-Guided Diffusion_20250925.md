---
keywords:
  - Diffusion Curriculum
  - Synthetic-to-Real Generative Curriculum Learning
  - Image-Guided Diffusion
  - Long-Tail Classification
  - Out-of-Distribution Data
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2410.13674
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:17:50.057887",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Curriculum",
    "Synthetic-to-Real Generative Curriculum Learning",
    "Image-Guided Diffusion",
    "Long-Tail Classification",
    "Out-of-Distribution Data"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diffusion Curriculum": 0.8,
    "Synthetic-to-Real Generative Curriculum Learning": 0.78,
    "Image-Guided Diffusion": 0.77,
    "Long-Tail Classification": 0.79,
    "Out-of-Distribution Data": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diffusion Curriculum",
        "canonical": "Diffusion Curriculum",
        "aliases": [
          "DisCL"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach to curriculum learning using diffusion models, which is central to the paper's contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Synthetic-to-Real Generative Curriculum Learning",
        "canonical": "Synthetic-to-Real Generative Curriculum Learning",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Represents a specific application of generative models to bridge synthetic and real data, a key innovation in the study.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Image-Guided Diffusion",
        "canonical": "Image-Guided Diffusion",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Describes a novel method for controlling the synthesis of images, crucial for the paper's methodology.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Long-Tail Classification",
        "canonical": "Long-Tail Classification",
        "aliases": [
          "LT Classification"
        ],
        "category": "specific_connectable",
        "rationale": "A specific task addressed by the proposed method, relevant for connecting to broader discussions on classification challenges.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.79
      },
      {
        "surface": "Out-of-Distribution Data",
        "canonical": "Out-of-Distribution Data",
        "aliases": [
          "OOD Data"
        ],
        "category": "specific_connectable",
        "rationale": "Critical for understanding the challenges addressed by the paper, linking to broader topics in model robustness.",
        "novelty_score": 0.5,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "data augmentation",
      "model performance",
      "training stage"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Diffusion Curriculum",
      "resolved_canonical": "Diffusion Curriculum",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Synthetic-to-Real Generative Curriculum Learning",
      "resolved_canonical": "Synthetic-to-Real Generative Curriculum Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Image-Guided Diffusion",
      "resolved_canonical": "Image-Guided Diffusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Long-Tail Classification",
      "resolved_canonical": "Long-Tail Classification",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Out-of-Distribution Data",
      "resolved_canonical": "Out-of-Distribution Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Diffusion Curriculum: Synthetic-to-Real Generative Curriculum Learning via Image-Guided Diffusion

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2410.13674.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2410.13674](https://arxiv.org/abs/2410.13674)

## 🔗 유사한 논문
- [[2025-09-22/LowDiff_ Efficient Diffusion Sampling with Low-Resolution Condition_20250922|LowDiff: Efficient Diffusion Sampling with Low-Resolution Condition]] (85.4% similar)
- [[2025-09-22/Efficient Multimodal Dataset Distillation via Generative Models_20250922|Efficient Multimodal Dataset Distillation via Generative Models]] (84.9% similar)
- [[2025-09-23/Penalizing Boundary Activation for Object Completeness in Diffusion Models_20250923|Penalizing Boundary Activation for Object Completeness in Diffusion Models]] (84.7% similar)
- [[2025-09-22/RespoDiff_ Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation_20250922|RespoDiff: Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation]] (84.5% similar)
- [[2025-09-22/MaskAttn-SDXL_ Controllable Region-Level Text-To-Image Generation_20250922|MaskAttn-SDXL: Controllable Region-Level Text-To-Image Generation]] (84.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Long-Tail Classification|Long-Tail Classification]], [[keywords/Out-of-Distribution Data|Out-of-Distribution Data]]
**⚡ Unique Technical**: [[keywords/Diffusion Curriculum|Diffusion Curriculum]], [[keywords/Synthetic-to-Real Generative Curriculum Learning|Synthetic-to-Real Generative Curriculum Learning]], [[keywords/Image-Guided Diffusion|Image-Guided Diffusion]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2410.13674v3 Announce Type: replace-cross 
Abstract: Low-quality or scarce data has posed significant challenges for training deep neural networks in practice. While classical data augmentation cannot contribute very different new data, diffusion models opens up a new door to build self-evolving AI by generating high-quality and diverse synthetic data through text-guided prompts. However, text-only guidance cannot control synthetic images' proximity to the original images, resulting in out-of-distribution data detrimental to the model performance. To overcome the limitation, we study image guidance to achieve a spectrum of interpolations between synthetic and real images. With stronger image guidance, the generated images are similar to the training data but hard to learn. While with weaker image guidance, the synthetic images will be easier for model but contribute to a larger distribution gap with the original data. The generated full spectrum of data enables us to build a novel "Diffusion Curriculum (DisCL)". DisCL adjusts the image guidance level of image synthesis for each training stage: It identifies and focuses on hard samples for the model and assesses the most effective guidance level of synthetic images to improve hard data learning. We apply DisCL to two challenging tasks: long-tail (LT) classification and learning from low-quality data. It focuses on lower-guidance images of high-quality to learn prototypical features as a warm-up of learning higher-guidance images that might be weak on diversity or quality. Extensive experiments showcase a gain of 2.7% and 2.1% in OOD and ID macro-accuracy when applying DisCL to iWildCam dataset. On ImageNet-LT, DisCL improves the base model's tail-class accuracy from 4.4% to 23.64% and leads to a 4.02% improvement in all-class accuracy.

## 📝 요약

이 논문은 데이터 품질이 낮거나 부족한 상황에서 딥러닝 모델을 효과적으로 훈련하기 위한 새로운 방법론을 제안합니다. 전통적인 데이터 증강의 한계를 극복하기 위해, 텍스트 기반 프롬프트를 활용한 확산 모델을 통해 고품질의 다양한 합성 데이터를 생성하는 방법을 연구합니다. 그러나 텍스트만으로는 합성 이미지가 원본 이미지와 얼마나 유사한지 제어하기 어려워, 모델 성능에 부정적인 영향을 미칠 수 있는 분포 외 데이터가 생성될 수 있습니다. 이를 해결하기 위해, 이미지 가이던스를 사용하여 합성 이미지와 실제 이미지 간의 스펙트럼을 조정하는 방법을 제안합니다. 이 방법론을 통해 'Diffusion Curriculum (DisCL)'을 개발하였으며, 이는 각 훈련 단계에서 이미지 합성의 가이던스 수준을 조정하여 모델이 어려운 샘플에 집중할 수 있도록 합니다. DisCL은 iWildCam 데이터셋과 ImageNet-LT에서 성능을 크게 향상시켰으며, 특히 ImageNet-LT에서 꼬리 클래스 정확도를 4.4%에서 23.64%로 개선하였습니다.

## 🎯 주요 포인트

- 1. 저품질 또는 희소한 데이터는 심층 신경망 훈련에 큰 도전 과제를 제시합니다.
- 2. 확산 모델은 텍스트 기반 프롬프트를 통해 고품질 및 다양한 합성 데이터를 생성하여 새로운 AI 발전의 가능성을 열어줍니다.
- 3. 이미지 가이던스를 통해 합성 이미지와 실제 이미지 간의 보간 스펙트럼을 달성하여 모델 성능을 향상시킬 수 있습니다.
- 4. DisCL은 각 훈련 단계에서 이미지 합성의 가이던스 수준을 조정하여 어려운 샘플 학습을 개선합니다.
- 5. DisCL을 iWildCam 및 ImageNet-LT 데이터셋에 적용한 결과, 모델의 정확도가 크게 향상되었습니다.


---

*Generated on 2025-09-25 16:17:50*