---
keywords:
  - Gaussian Splatting
  - Virtual Camera-based Regularization
  - Material Point Method
  - Surgical Simulation
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17027
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:41:48.381479",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Gaussian Splatting",
    "Virtual Camera-based Regularization",
    "Material Point Method",
    "Surgical Simulation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Gaussian Splatting": 0.78,
    "Virtual Camera-based Regularization": 0.72,
    "Material Point Method": 0.8,
    "Surgical Simulation": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Gaussian Splatting",
        "canonical": "Gaussian Splatting",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Gaussian Splatting is a novel technique for scene reconstruction, offering a unique approach that can be linked to advancements in 3D reconstruction.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Virtual Camera-based Regularization",
        "canonical": "Virtual Camera-based Regularization",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This method addresses overfitting in endoscopic views, providing a unique approach to improve geometric accuracy.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.72
      },
      {
        "surface": "Material Point Method",
        "canonical": "Material Point Method",
        "aliases": [
          "MPM"
        ],
        "category": "specific_connectable",
        "rationale": "The Material Point Method is crucial for simulating physical properties, linking to broader computational physics techniques.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Surgical Simulation",
        "canonical": "Surgical Simulation",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Surgical Simulation is a key application area, connecting to medical training and simulation technologies.",
        "novelty_score": 0.55,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
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
      "candidate_surface": "Virtual Camera-based Regularization",
      "resolved_canonical": "Virtual Camera-based Regularization",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Material Point Method",
      "resolved_canonical": "Material Point Method",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Surgical Simulation",
      "resolved_canonical": "Surgical Simulation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Efficient 3D Scene Reconstruction and Simulation from Sparse Endoscopic Views

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17027.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17027](https://arxiv.org/abs/2509.17027)

## 🔗 유사한 논문
- [[2025-09-23/MedGS_ Gaussian Splatting for Multi-Modal 3D Medical Imaging_20250923|MedGS: Gaussian Splatting for Multi-Modal 3D Medical Imaging]] (84.7% similar)
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (84.1% similar)
- [[2025-09-22/Recovering Parametric Scenes from Very Few Time-of-Flight Pixels_20250922|Recovering Parametric Scenes from Very Few Time-of-Flight Pixels]] (84.1% similar)
- [[2025-09-23/3D Gaussian Flats_ Hybrid 2D/3D Photometric Scene Reconstruction_20250923|3D Gaussian Flats: Hybrid 2D/3D Photometric Scene Reconstruction]] (84.0% similar)
- [[2025-09-22/Data-Efficient Learning for Generalizable Surgical Video Understanding_20250922|Data-Efficient Learning for Generalizable Surgical Video Understanding]] (84.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Material Point Method|Material Point Method]], [[keywords/Surgical Simulation|Surgical Simulation]]
**⚡ Unique Technical**: [[keywords/Gaussian Splatting|Gaussian Splatting]], [[keywords/Virtual Camera-based Regularization|Virtual Camera-based Regularization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17027v1 Announce Type: new 
Abstract: Surgical simulation is essential for medical training, enabling practitioners to develop crucial skills in a risk-free environment while improving patient safety and surgical outcomes. However, conventional methods for building simulation environments are cumbersome, time-consuming, and difficult to scale, often resulting in poor details and unrealistic simulations. In this paper, we propose a Gaussian Splatting-based framework to directly reconstruct interactive surgical scenes from endoscopic data while ensuring efficiency, rendering quality, and realism. A key challenge in this data-driven simulation paradigm is the restricted movement of endoscopic cameras, which limits viewpoint diversity. As a result, the Gaussian Splatting representation overfits specific perspectives, leading to reduced geometric accuracy. To address this issue, we introduce a novel virtual camera-based regularization method that adaptively samples virtual viewpoints around the scene and incorporates them into the optimization process to mitigate overfitting. An effective depth-based regularization is applied to both real and virtual views to further refine the scene geometry. To enable fast deformation simulation, we propose a sparse control node-based Material Point Method, which integrates physical properties into the reconstructed scene while significantly reducing computational costs. Experimental results on representative surgical data demonstrate that our method can efficiently reconstruct and simulate surgical scenes from sparse endoscopic views. Notably, our method takes only a few minutes to reconstruct the surgical scene and is able to produce physically plausible deformations in real-time with user-defined interactions.

## 📝 요약

이 논문은 내시경 데이터를 활용하여 효율적이고 현실적인 수술 시뮬레이션 환경을 구축하는 Gaussian Splatting 기반 프레임워크를 제안합니다. 기존 시뮬레이션 방법의 비효율성을 극복하기 위해, 가상 카메라 기반 정규화 방법을 도입하여 시점 다양성을 확보하고 기하학적 정확성을 높였습니다. 또한, 희소 제어 노드 기반의 물질점 방법을 통해 물리적 특성을 통합하여 계산 비용을 줄였습니다. 실험 결과, 이 방법은 내시경 시점에서 수술 장면을 신속하게 재구성하고, 사용자 정의 상호작용에 따라 실시간으로 물리적으로 타당한 변형을 생성할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. 기존의 수술 시뮬레이션 환경 구축 방법은 번거롭고 시간이 많이 소요되며 확장하기 어렵다.
- 2. 제안된 Gaussian Splatting 기반 프레임워크는 내시경 데이터를 활용하여 효율적이고 현실적인 수술 장면을 재구성한다.
- 3. 내시경 카메라의 제한된 움직임으로 인해 시점 다양성이 부족하고, 이는 기하학적 정확성을 저하시킨다.
- 4. 가상 카메라 기반의 정규화 방법을 도입하여 가상 시점을 적응적으로 샘플링하고 최적화 과정에 통합하여 과적합 문제를 완화한다.
- 5. 제안된 방법은 몇 분 만에 수술 장면을 재구성하며, 사용자 정의 상호작용을 통해 실시간으로 물리적으로 타당한 변형을 생성할 수 있다.


---

*Generated on 2025-09-24 04:41:48*