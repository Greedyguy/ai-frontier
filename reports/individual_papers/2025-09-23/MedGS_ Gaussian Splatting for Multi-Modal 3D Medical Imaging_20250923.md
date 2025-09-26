---
keywords:
  - Gaussian Splatting
  - Neural Implicit Surface Reconstruction
  - Multimodal Learning
  - Medical Imaging
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.16806
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:35:03.221870",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Gaussian Splatting",
    "Neural Implicit Surface Reconstruction",
    "Multimodal Learning",
    "Medical Imaging"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Gaussian Splatting": 0.78,
    "Neural Implicit Surface Reconstruction": 0.75,
    "Multimodal Learning": 0.8,
    "Medical Imaging": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Gaussian Splatting",
        "canonical": "Gaussian Splatting",
        "aliases": [
          "GS"
        ],
        "category": "unique_technical",
        "rationale": "Gaussian Splatting is a novel interpolation technique crucial for enhancing noise robustness and surface reconstruction in medical imaging.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Neural Implicit Surface Reconstruction",
        "canonical": "Neural Implicit Surface Reconstruction",
        "aliases": [
          "Implicit Surface Reconstruction"
        ],
        "category": "unique_technical",
        "rationale": "This technique is central to the paper's approach for modeling complex anatomical structures, offering a new paradigm in medical imaging.",
        "novelty_score": 0.72,
        "connectivity_score": 0.7,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      },
      {
        "surface": "Multi-modal 3D Medical Imaging",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multi-modal Imaging"
        ],
        "category": "specific_connectable",
        "rationale": "Connecting to Multimodal Learning highlights the integration of various imaging modalities and their collective analysis.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Medical Imaging",
        "canonical": "Medical Imaging",
        "aliases": [
          "3D Medical Imaging"
        ],
        "category": "broad_technical",
        "rationale": "Medical Imaging is a fundamental domain that connects to various technical and clinical applications.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "surface reconstruction",
      "frame interpolation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Gaussian Splatting",
      "resolved_canonical": "Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Neural Implicit Surface Reconstruction",
      "resolved_canonical": "Neural Implicit Surface Reconstruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.7,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Multi-modal 3D Medical Imaging",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Medical Imaging",
      "resolved_canonical": "Medical Imaging",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# MedGS: Gaussian Splatting for Multi-Modal 3D Medical Imaging

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16806.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.16806](https://arxiv.org/abs/2509.16806)

## 🔗 유사한 논문
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (86.2% similar)
- [[2025-09-22/GS-Scale_ Unlocking Large-Scale 3D Gaussian Splatting Training via Host Offloading_20250922|GS-Scale: Unlocking Large-Scale 3D Gaussian Splatting Training via Host Offloading]] (85.7% similar)
- [[2025-09-18/Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images_20250918|Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images]] (84.5% similar)
- [[2025-09-23/PGSTalker_ Real-Time Audio-Driven Talking Head Generation via 3D Gaussian Splatting with Pixel-Aware Density Control_20250923|PGSTalker: Real-Time Audio-Driven Talking Head Generation via 3D Gaussian Splatting with Pixel-Aware Density Control]] (82.7% similar)
- [[2025-09-23/A Novel Metric for Detecting Memorization in Generative Models for Brain MRI Synthesis_20250923|A Novel Metric for Detecting Memorization in Generative Models for Brain MRI Synthesis]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Medical Imaging|Medical Imaging]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Gaussian Splatting|Gaussian Splatting]], [[keywords/Neural Implicit Surface Reconstruction|Neural Implicit Surface Reconstruction]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16806v1 Announce Type: new 
Abstract: Multi-modal three-dimensional (3D) medical imaging data, derived from ultrasound, magnetic resonance imaging (MRI), and potentially computed tomography (CT), provide a widely adopted approach for non-invasive anatomical visualization. Accurate modeling, registration, and visualization in this setting depend on surface reconstruction and frame-to-frame interpolation. Traditional methods often face limitations due to image noise and incomplete information between frames. To address these challenges, we present MedGS, a semi-supervised neural implicit surface reconstruction framework that employs a Gaussian Splatting (GS)-based interpolation mechanism. In this framework, medical imaging data are represented as consecutive two-dimensional (2D) frames embedded in 3D space and modeled using Gaussian-based distributions. This representation enables robust frame interpolation and high-fidelity surface reconstruction across imaging modalities. As a result, MedGS offers more efficient training than traditional neural implicit methods. Its explicit GS-based representation enhances noise robustness, allows flexible editing, and supports precise modeling of complex anatomical structures with fewer artifacts. These features make MedGS highly suitable for scalable and practical applications in medical imaging.

## 📝 요약

MedGS는 초음파, MRI, CT 등 다중 모달 3D 의료 이미징 데이터를 위한 반지도 학습 기반의 신경 암시적 표면 재구성 프레임워크입니다. 이 연구는 Gaussian Splatting 기반의 보간 메커니즘을 사용하여 이미지 노이즈와 프레임 간 불완전한 정보를 극복합니다. MedGS는 2D 프레임을 3D 공간에 임베딩하고 Gaussian 분포로 모델링하여 강력한 프레임 보간과 고품질 표면 재구성을 제공합니다. 이로 인해 전통적인 방법보다 효율적인 학습이 가능하며, 복잡한 해부학적 구조를 정밀하게 모델링할 수 있습니다. MedGS는 의료 이미징의 확장성과 실용성을 높이는 데 기여합니다.

## 🎯 주요 포인트

- 1. MedGS는 초음파, MRI, CT 등 다중 모달리티 3D 의료 이미징 데이터를 위한 반지도 학습 기반의 신경 암시적 표면 재구성 프레임워크입니다.
- 2. Gaussian Splatting 기반의 보간 메커니즘을 통해 이미지 노이즈와 프레임 간 불완전한 정보 문제를 해결합니다.
- 3. MedGS는 2D 프레임을 3D 공간에 임베딩하여 강력한 프레임 보간과 고품질 표면 재구성을 가능하게 합니다.
- 4. 이 프레임워크는 전통적인 방법보다 효율적인 학습을 제공하며, 노이즈에 대한 강한 내성을 갖추고 복잡한 해부학적 구조를 정밀하게 모델링할 수 있습니다.
- 5. MedGS는 의료 이미징에서 확장 가능하고 실용적인 응용에 적합합니다.


---

*Generated on 2025-09-24 04:35:03*