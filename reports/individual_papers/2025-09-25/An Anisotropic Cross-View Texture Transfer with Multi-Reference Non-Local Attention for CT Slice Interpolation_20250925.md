---
keywords:
  - Deep Learning
  - Attention Mechanism
  - Volumetric Super-Resolution
  - CT Slice Interpolation
  - Anisotropic CT Volume
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.20242
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:14:29.497893",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Attention Mechanism",
    "Volumetric Super-Resolution",
    "CT Slice Interpolation",
    "Anisotropic CT Volume"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Attention Mechanism": 0.82,
    "Volumetric Super-Resolution": 0.78,
    "CT Slice Interpolation": 0.8,
    "Anisotropic CT Volume": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [
          "DL"
        ],
        "category": "broad_technical",
        "rationale": "Deep Learning is a foundational technology in the proposed CT slice interpolation method, linking it to a wide range of related research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Non-local Attention",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Non-local Attention"
        ],
        "category": "specific_connectable",
        "rationale": "The non-local attention module is crucial for texture transfer, connecting this work to broader attention mechanism research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Volumetric Super-Resolution",
        "canonical": "Volumetric Super-Resolution",
        "aliases": [
          "3D Super-Resolution"
        ],
        "category": "unique_technical",
        "rationale": "This technique is central to the paper's contribution, offering a unique approach to improving CT slice resolution.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "CT Slice Interpolation",
        "canonical": "CT Slice Interpolation",
        "aliases": [
          "Computed Tomography Slice Interpolation"
        ],
        "category": "unique_technical",
        "rationale": "The main focus of the paper, providing a specific application area for linking with medical imaging research.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Anisotropic CT Volume",
        "canonical": "Anisotropic CT Volume",
        "aliases": [
          "Anisotropic Computed Tomography Volume"
        ],
        "category": "unique_technical",
        "rationale": "This concept is critical for understanding the challenges addressed by the paper, linking it to specific imaging challenges.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.75
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
      "candidate_surface": "Deep Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Non-local Attention",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Volumetric Super-Resolution",
      "resolved_canonical": "Volumetric Super-Resolution",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "CT Slice Interpolation",
      "resolved_canonical": "CT Slice Interpolation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Anisotropic CT Volume",
      "resolved_canonical": "Anisotropic CT Volume",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# An Anisotropic Cross-View Texture Transfer with Multi-Reference Non-Local Attention for CT Slice Interpolation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20242.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.20242](https://arxiv.org/abs/2509.20242)

## 🔗 유사한 논문
- [[2025-09-18/Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction for Sparse-View CT_20250918|Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction for Sparse-View CT]] (84.8% similar)
- [[2025-09-24/Reconstruction of Optical Coherence Tomography Images from Wavelength-space Using Deep-learning_20250924|Reconstruction of Optical Coherence Tomography Images from Wavelength-space Using Deep-learning]] (83.9% similar)
- [[2025-09-19/DICE_ Diffusion Consensus Equilibrium for Sparse-view CT Reconstruction_20250919|DICE: Diffusion Consensus Equilibrium for Sparse-view CT Reconstruction]] (83.0% similar)
- [[2025-09-23/Anatomical feature-prioritized loss for enhanced MR to CT translation_20250923|Anatomical feature-prioritized loss for enhanced MR to CT translation]] (82.0% similar)
- [[2025-09-17/Consistent View Alignment Improves Foundation Models for 3D Medical Image Segmentation_20250917|Consistent View Alignment Improves Foundation Models for 3D Medical Image Segmentation]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Volumetric Super-Resolution|Volumetric Super-Resolution]], [[keywords/CT Slice Interpolation|CT Slice Interpolation]], [[keywords/Anisotropic CT Volume|Anisotropic CT Volume]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20242v1 Announce Type: new 
Abstract: Computed tomography (CT) is one of the most widely used non-invasive imaging modalities for medical diagnosis. In clinical practice, CT images are usually acquired with large slice thicknesses due to the high cost of memory storage and operation time, resulting in an anisotropic CT volume with much lower inter-slice resolution than in-plane resolution. Since such inconsistent resolution may lead to difficulties in disease diagnosis, deep learning-based volumetric super-resolution methods have been developed to improve inter-slice resolution. Most existing methods conduct single-image super-resolution on the through-plane or synthesize intermediate slices from adjacent slices; however, the anisotropic characteristic of 3D CT volume has not been well explored. In this paper, we propose a novel cross-view texture transfer approach for CT slice interpolation by fully utilizing the anisotropic nature of 3D CT volume. Specifically, we design a unique framework that takes high-resolution in-plane texture details as a reference and transfers them to low-resolution through-plane images. To this end, we introduce a multi-reference non-local attention module that extracts meaningful features for reconstructing through-plane high-frequency details from multiple in-plane images. Through extensive experiments, we demonstrate that our method performs significantly better in CT slice interpolation than existing competing methods on public CT datasets including a real-paired benchmark, verifying the effectiveness of the proposed framework. The source code of this work is available at https://github.com/khuhm/ACVTT.

## 📝 요약

이 논문은 CT 영상의 비등방성 문제를 해결하기 위해 새로운 교차 뷰 텍스처 전이 방법을 제안합니다. 기존 방법들은 단일 이미지 초해상도나 인접 슬라이스로부터 중간 슬라이스를 합성하는 데 중점을 두었지만, 이 연구는 3D CT 볼륨의 비등방성 특성을 활용하여 슬라이스 간 해상도를 개선합니다. 제안된 프레임워크는 고해상도 평면 내 텍스처를 참조하여 저해상도 슬라이스에 전이하며, 다중 참조 비지역 주의 모듈을 도입하여 평면 내 이미지로부터 의미 있는 특징을 추출합니다. 실험 결과, 제안된 방법은 기존 방법들보다 CT 슬라이스 보간에서 뛰어난 성능을 보였습니다. 연구의 소스 코드는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. CT 이미지는 메모리 저장 비용과 운영 시간 때문에 큰 슬라이스 두께로 획득되어, 슬라이스 간 해상도가 낮아지는 문제가 발생합니다.
- 2. 기존의 딥러닝 기반 볼륨 슈퍼 해상도 방법들은 주로 단일 이미지 슈퍼 해상도나 인접 슬라이스로부터 중간 슬라이스를 합성하는 방식에 의존합니다.
- 3. 본 연구에서는 3D CT 볼륨의 비등방성 특성을 활용하여 CT 슬라이스 보간을 위한 새로운 교차-뷰 텍스처 전이 방법을 제안합니다.
- 4. 제안된 방법은 고해상도 평면 내 텍스처 세부 정보를 참조하여 저해상도 슬라이스에 전이하는 독특한 프레임워크를 설계합니다.
- 5. 실험 결과, 제안된 방법이 기존의 경쟁 방법들보다 CT 슬라이스 보간에서 뛰어난 성능을 보임을 입증하였습니다.


---

*Generated on 2025-09-26 09:14:29*