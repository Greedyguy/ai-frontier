---
keywords:
  - Diffusion Models
  - Missing Modality Generation
  - Coherence Enhancement Mechanism
  - Multimodal Learning
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.16019
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:26:18.283456",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Missing Modality Generation",
    "Coherence Enhancement Mechanism",
    "Multimodal Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diffusion Models": 0.8,
    "Missing Modality Generation": 0.78,
    "Coherence Enhancement Mechanism": 0.75,
    "Multimodal Learning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diffusion Models",
        "canonical": "Diffusion Models",
        "aliases": [
          "Diffusion-based Models"
        ],
        "category": "broad_technical",
        "rationale": "Diffusion models are a key component of the proposed framework and are increasingly relevant in generative tasks.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      },
      {
        "surface": "Missing Modality Generation",
        "canonical": "Missing Modality Generation",
        "aliases": [
          "Modality Synthesis",
          "Modality Reconstruction"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique challenge in medical imaging, directly addressed by the paper's framework.",
        "novelty_score": 0.75,
        "connectivity_score": 0.64,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Coherence Enhancement Mechanism",
        "canonical": "Coherence Enhancement Mechanism",
        "aliases": [
          "Structural Coherence Enhancement"
        ],
        "category": "unique_technical",
        "rationale": "This mechanism is crucial for maintaining structural integrity in generated images, a novel aspect of the approach.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      },
      {
        "surface": "Multimodal",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal"
        ],
        "category": "specific_connectable",
        "rationale": "The paper's approach leverages multiple MRI modalities, aligning with the concept of multimodal learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.68,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "MRI",
      "BraTS-Lighthouse-2025 Challenge"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Diffusion Models",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Missing Modality Generation",
      "resolved_canonical": "Missing Modality Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.64,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Coherence Enhancement Mechanism",
      "resolved_canonical": "Coherence Enhancement Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Multimodal",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.68,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# SLaM-DiMM: Shared Latent Modeling for Diffusion Based Missing Modality Synthesis in MRI

**Korean Title:** SLaM-DiMM: MRI에서 확산 기반 결측 모달리티 합성을 위한 공유 잠재 모델링

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16019.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.16019](https://arxiv.org/abs/2509.16019)

## 🔗 유사한 논문
- [[2025-09-22/UniMRSeg_ Unified Modality-Relax Segmentation via Hierarchical Self-Supervised Compensation_20250922|UniMRSeg: Unified Modality-Relax Segmentation via Hierarchical Self-Supervised Compensation]] (83.8% similar)
- [[2025-09-22/iCBIR-Sli_ Interpretable Content-Based Image Retrieval with 2D Slice Embeddings_20250922|iCBIR-Sli: Interpretable Content-Based Image Retrieval with 2D Slice Embeddings]] (82.5% similar)
- [[2025-09-22/Exploring the Capabilities of LLM Encoders for Image-Text Retrieval in Chest X-rays_20250922|Exploring the Capabilities of LLM Encoders for Image-Text Retrieval in Chest X-rays]] (82.3% similar)
- [[2025-09-19/Superpose Task-specific Features for Model Merging_20250919|Superpose Task-specific Features for Model Merging]] (82.1% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (82.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Diffusion Models|Diffusion Models]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Missing Modality Generation|Missing Modality Generation]], [[keywords/Coherence Enhancement Mechanism|Coherence Enhancement Mechanism]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16019v1 Announce Type: cross 
Abstract: Brain MRI scans are often found in four modalities, consisting of T1-weighted with and without contrast enhancement (T1ce and T1w), T2-weighted imaging (T2w), and Flair. Leveraging complementary information from these different modalities enables models to learn richer, more discriminative features for understanding brain anatomy, which could be used in downstream tasks such as anomaly detection. However, in clinical practice, not all MRI modalities are always available due to various reasons. This makes missing modality generation a critical challenge in medical image analysis. In this paper, we propose SLaM-DiMM, a novel missing modality generation framework that harnesses the power of diffusion models to synthesize any of the four target MRI modalities from other available modalities. Our approach not only generates high-fidelity images but also ensures structural coherence across the depth of the volume through a dedicated coherence enhancement mechanism. Qualitative and quantitative evaluations on the BraTS-Lighthouse-2025 Challenge dataset demonstrate the effectiveness of the proposed approach in synthesizing anatomically plausible and structurally consistent results. Code is available at https://github.com/BheeshmSharma/SLaM-DiMM-MICCAI-BraTS-Challenge-2025.

## 🔍 Abstract (한글 번역)

arXiv:2509.16019v1 발표 유형: 교차  
초록: 뇌 MRI 스캔은 일반적으로 네 가지 모달리티로 제공되며, 이는 조영제 강화 유무에 따른 T1 강조 영상(T1ce 및 T1w), T2 강조 영상(T2w), 그리고 Flair로 구성됩니다. 이러한 다양한 모달리티에서 보완적인 정보를 활용하면 모델이 뇌 해부학을 이해하기 위한 더 풍부하고 변별력 있는 특징을 학습할 수 있으며, 이는 이상 탐지와 같은 후속 작업에 사용될 수 있습니다. 그러나 임상 실습에서는 다양한 이유로 인해 모든 MRI 모달리티가 항상 제공되지 않습니다. 이는 의료 영상 분석에서 누락된 모달리티 생성이 중요한 과제가 되는 이유입니다. 본 논문에서는 SLaM-DiMM이라는 새로운 누락 모달리티 생성 프레임워크를 제안하며, 이는 확산 모델의 힘을 활용하여 다른 사용 가능한 모달리티로부터 네 가지 목표 MRI 모달리티 중 어느 것이든 합성할 수 있습니다. 우리의 접근 방식은 고품질 이미지를 생성할 뿐만 아니라, 전용 일관성 향상 메커니즘을 통해 볼륨의 깊이에 걸쳐 구조적 일관성을 보장합니다. BraTS-Lighthouse-2025 챌린지 데이터셋에 대한 정성적 및 정량적 평가를 통해 해부학적으로 그럴듯하고 구조적으로 일관된 결과를 합성하는 데 있어 제안된 접근 방식의 효과가 입증되었습니다. 코드는 https://github.com/BheeshmSharma/SLaM-DiMM-MICCAI-BraTS-Challenge-2025에서 제공됩니다.

## 📝 요약

이 논문에서는 뇌 MRI 스캔의 네 가지 모달리티(T1ce, T1w, T2w, Flair) 중 일부가 누락된 경우에도 다른 모달리티로부터 누락된 모달리티를 생성할 수 있는 새로운 프레임워크인 SLaM-DiMM을 제안합니다. 이 방법은 확산 모델을 활용하여 고품질의 이미지를 생성하며, 구조적 일관성을 유지하기 위한 메커니즘을 포함하고 있습니다. 제안된 방법은 BraTS-Lighthouse-2025 Challenge 데이터셋을 통해 정성적 및 정량적으로 평가되었으며, 해부학적으로 그럴듯하고 구조적으로 일관된 결과를 생성하는 데 효과적임을 입증했습니다.

## 🎯 주요 포인트

- 1. 뇌 MRI 스캔은 T1, T1ce, T2w, Flair의 네 가지 모달리티로 구성되며, 이들의 상호 보완적 정보를 활용하여 뇌 해부학을 이해하는 데 유리한 특징을 학습할 수 있다.
- 2. 임상 실무에서는 다양한 이유로 모든 MRI 모달리티가 항상 제공되지 않으며, 이는 의료 영상 분석에서 중요한 과제로 작용한다.
- 3. SLaM-DiMM은 확산 모델을 활용하여 사용 가능한 모달리티로부터 누락된 MRI 모달리티를 생성하는 새로운 프레임워크로, 고품질 이미지 생성과 구조적 일관성을 보장한다.
- 4. 제안된 접근법은 BraTS-Lighthouse-2025 Challenge 데이터셋에서 해부학적으로 그럴듯하고 구조적으로 일관된 결과를 생성하는 데 효과적임을 입증하였다.


---

*Generated on 2025-09-23 12:26:18*