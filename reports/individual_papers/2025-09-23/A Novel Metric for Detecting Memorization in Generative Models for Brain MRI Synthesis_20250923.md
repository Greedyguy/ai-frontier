---
keywords:
  - DeepSSIM
  - Self-supervised Learning
  - Latent Diffusion Model
  - Structural Similarity Index
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16582
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:11:09.749761",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "DeepSSIM",
    "Self-supervised Learning",
    "Latent Diffusion Model",
    "Structural Similarity Index"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "DeepSSIM": 0.78,
    "Self-supervised Learning": 0.8,
    "Latent Diffusion Model": 0.77,
    "Structural Similarity Index": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "DeepSSIM",
        "canonical": "DeepSSIM",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "DeepSSIM is a novel metric specifically designed for detecting memorization in generative models, making it a unique contribution to the field.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Self-supervised metric",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "self-supervised approach"
        ],
        "category": "specific_connectable",
        "rationale": "The self-supervised nature of DeepSSIM aligns with existing concepts in self-supervised learning, facilitating connections with related research.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Latent Diffusion Model",
        "canonical": "Latent Diffusion Model",
        "aliases": [
          "LDM"
        ],
        "category": "unique_technical",
        "rationale": "Latent Diffusion Models are a specific type of generative model relevant to the study, providing a focused link to similar research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Structural Similarity Index",
        "canonical": "Structural Similarity Index",
        "aliases": [
          "SSIM"
        ],
        "category": "broad_technical",
        "rationale": "SSIM is a widely used metric in image processing, providing a foundational link to other works utilizing image similarity measures.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.65,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "generative models",
      "medical imaging",
      "training data"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "DeepSSIM",
      "resolved_canonical": "DeepSSIM",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Self-supervised metric",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Latent Diffusion Model",
      "resolved_canonical": "Latent Diffusion Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Structural Similarity Index",
      "resolved_canonical": "Structural Similarity Index",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.65,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# A Novel Metric for Detecting Memorization in Generative Models for Brain MRI Synthesis

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16582.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16582](https://arxiv.org/abs/2509.16582)

## 🔗 유사한 논문
- [[2025-09-22/SLaM-DiMM_ Shared Latent Modeling for Diffusion Based Missing Modality Synthesis in MRI_20250922|SLaM-DiMM: Shared Latent Modeling for Diffusion Based Missing Modality Synthesis in MRI]] (86.3% similar)
- [[2025-09-22/Toward Medical Deepfake Detection_ A Comprehensive Dataset and Novel Method_20250922|Toward Medical Deepfake Detection: A Comprehensive Dataset and Novel Method]] (83.3% similar)
- [[2025-09-22/Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation_20250922|Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation]] (83.2% similar)
- [[2025-09-22/PRISM_ Phase-enhanced Radial-based Image Signature Mapping framework for fingerprinting AI-generated images_20250922|PRISM: Phase-enhanced Radial-based Image Signature Mapping framework for fingerprinting AI-generated images]] (82.4% similar)
- [[2025-09-22/Domain-invariant feature learning in brain MR imaging for content-based image retrieval_20250922|Domain-invariant feature learning in brain MR imaging for content-based image retrieval]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Structural Similarity Index|Structural Similarity Index]]
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/DeepSSIM|DeepSSIM]], [[keywords/Latent Diffusion Model|Latent Diffusion Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16582v1 Announce Type: cross 
Abstract: Deep generative models have emerged as a transformative tool in medical imaging, offering substantial potential for synthetic data generation. However, recent empirical studies highlight a critical vulnerability: these models can memorize sensitive training data, posing significant risks of unauthorized patient information disclosure. Detecting memorization in generative models remains particularly challenging, necessitating scalable methods capable of identifying training data leakage across large sets of generated samples. In this work, we propose DeepSSIM, a novel self-supervised metric for quantifying memorization in generative models. DeepSSIM is trained to: i) project images into a learned embedding space and ii) force the cosine similarity between embeddings to match the ground-truth SSIM (Structural Similarity Index) scores computed in the image space. To capture domain-specific anatomical features, training incorporates structure-preserving augmentations, allowing DeepSSIM to estimate similarity reliably without requiring precise spatial alignment. We evaluate DeepSSIM in a case study involving synthetic brain MRI data generated by a Latent Diffusion Model (LDM) trained under memorization-prone conditions, using 2,195 MRI scans from two publicly available datasets (IXI and CoRR). Compared to state-of-the-art memorization metrics, DeepSSIM achieves superior performance, improving F1 scores by an average of +52.03% over the best existing method. Code and data of our approach are publicly available at the following link: https://github.com/brAIn-science/DeepSSIM.

## 📝 요약

이 논문은 의료 영상에서 딥 생성 모델의 민감한 데이터 암기 문제를 해결하기 위해 DeepSSIM이라는 새로운 자기 지도 학습 지표를 제안합니다. DeepSSIM은 이미지 임베딩 공간을 학습하고, 임베딩 간 코사인 유사도가 이미지 공간의 SSIM 점수와 일치하도록 합니다. 구조 보존 증강을 통해 도메인 특화 해부학적 특징을 포착하며, 정밀한 공간 정렬 없이도 유사성을 신뢰성 있게 추정합니다. Latent Diffusion Model로 생성된 합성 뇌 MRI 데이터를 사용한 사례 연구에서 DeepSSIM은 기존 암기 측정 방법보다 평균 F1 점수를 52.03% 향상시켰습니다. 코드와 데이터는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 딥 생성 모델은 의료 영상에서 합성 데이터 생성의 잠재력을 제공하지만, 민감한 훈련 데이터의 암기 문제로 인해 환자 정보 유출 위험이 존재한다.
- 2. DeepSSIM은 생성 모델의 암기를 정량화하기 위한 새로운 자가 지도 학습 기반의 메트릭으로, 이미지 임베딩 공간에서 코사인 유사도를 실제 SSIM 점수와 맞추도록 훈련된다.
- 3. 구조 보존 증강을 통해 도메인 특유의 해부학적 특징을 포착하며, 정확한 공간 정렬 없이도 유사성을 신뢰성 있게 추정할 수 있다.
- 4. DeepSSIM은 기존의 암기 측정 메트릭과 비교하여 평균 F1 점수를 52.03% 향상시키며 우수한 성능을 보인다.
- 5. 연구에 사용된 코드와 데이터는 공개되어 있으며, 링크를 통해 접근할 수 있다: https://github.com/brAIn-science/DeepSSIM.


---

*Generated on 2025-09-24 02:11:09*