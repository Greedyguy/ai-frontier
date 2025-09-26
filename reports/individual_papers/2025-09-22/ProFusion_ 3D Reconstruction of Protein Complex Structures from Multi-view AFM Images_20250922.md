---
keywords:
  - Deep Learning
  - Neural Radiance Field
  - Atomic Force Microscopy
  - Protein Complex Structure Prediction
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15242
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:54:20.375824",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Neural Radiance Field",
    "Atomic Force Microscopy",
    "Protein Complex Structure Prediction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.8,
    "Neural Radiance Field": 0.78,
    "Atomic Force Microscopy": 0.77,
    "Protein Complex Structure Prediction": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Deep Learning is a fundamental technique used in the proposed framework, facilitating connections to various AI-based methodologies.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "Neural Radiance Field",
        "canonical": "Neural Radiance Field",
        "aliases": [
          "NeRF"
        ],
        "category": "unique_technical",
        "rationale": "Neural Radiance Field is a specific model used for 3D reconstruction, providing a unique link to advanced 3D modeling techniques.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Atomic Force Microscopy",
        "canonical": "Atomic Force Microscopy",
        "aliases": [
          "AFM"
        ],
        "category": "unique_technical",
        "rationale": "Atomic Force Microscopy is crucial for the multi-view imaging process, linking to experimental imaging techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Protein Complex Structure Prediction",
        "canonical": "Protein Complex Structure Prediction",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is the primary application of the framework, connecting to bioinformatics and structural biology fields.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
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
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Neural Radiance Field",
      "resolved_canonical": "Neural Radiance Field",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Atomic Force Microscopy",
      "resolved_canonical": "Atomic Force Microscopy",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Protein Complex Structure Prediction",
      "resolved_canonical": "Protein Complex Structure Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# ProFusion: 3D Reconstruction of Protein Complex Structures from Multi-view AFM Images

**Korean Title:** 프로퓨전(ProFusion): 다중 시각 AFM 이미지를 통한 단백질 복합체 구조의 3D 재구성

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15242.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15242](https://arxiv.org/abs/2509.15242)

## 🔗 유사한 논문
- [[2025-09-22/Recovering Parametric Scenes from Very Few Time-of-Flight Pixels_20250922|Recovering Parametric Scenes from Very Few Time-of-Flight Pixels]] (80.8% similar)
- [[2025-09-22/Generalizable Holographic Reconstruction via Amplitude-Only Diffusion Priors_20250922|Generalizable Holographic Reconstruction via Amplitude-Only Diffusion Priors]] (80.8% similar)
- [[2025-09-22/Monte Carlo Tree Diffusion with Multiple Experts for Protein Design_20250922|Monte Carlo Tree Diffusion with Multiple Experts for Protein Design]] (80.5% similar)
- [[2025-09-18/Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery_20250918|Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery]] (80.1% similar)
- [[2025-09-18/Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (79.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**⚡ Unique Technical**: [[keywords/Neural Radiance Field|Neural Radiance Field]], [[keywords/Atomic Force Microscopy|Atomic Force Microscopy]], [[keywords/Protein Complex Structure Prediction|Protein Complex Structure Prediction]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15242v1 Announce Type: new 
Abstract: AI-based in silico methods have improved protein structure prediction but often struggle with large protein complexes (PCs) involving multiple interacting proteins due to missing 3D spatial cues. Experimental techniques like Cryo-EM are accurate but costly and time-consuming. We present ProFusion, a hybrid framework that integrates a deep learning model with Atomic Force Microscopy (AFM), which provides high-resolution height maps from random orientations, naturally yielding multi-view data for 3D reconstruction. However, generating a large-scale AFM imaging data set sufficient to train deep learning models is impractical. Therefore, we developed a virtual AFM framework that simulates the imaging process and generated a dataset of ~542,000 proteins with multi-view synthetic AFM images. We train a conditional diffusion model to synthesize novel views from unposed inputs and an instance-specific Neural Radiance Field (NeRF) model to reconstruct 3D structures. Our reconstructed 3D protein structures achieve an average Chamfer Distance within the AFM imaging resolution, reflecting high structural fidelity. Our method is extensively validated on experimental AFM images of various PCs, demonstrating strong potential for accurate, cost-effective protein complex structure prediction and rapid iterative validation using AFM experiments.

## 🔍 Abstract (한글 번역)

arXiv:2509.15242v1 발표 유형: 신규  
초록: AI 기반의 인실리코 방법은 단백질 구조 예측을 개선했지만, 다수의 상호작용 단백질을 포함하는 대형 단백질 복합체(PCs)의 경우 3D 공간적 단서가 부족하여 종종 어려움을 겪습니다. Cryo-EM과 같은 실험적 기법은 정확하지만 비용이 많이 들고 시간이 소요됩니다. 우리는 ProFusion이라는 하이브리드 프레임워크를 제시합니다. 이는 심층 학습 모델과 원자력 현미경(AFM)을 통합하여 무작위 방향에서 고해상도 높이 지도를 제공하고, 자연스럽게 3D 재구성을 위한 다중 뷰 데이터를 생성합니다. 그러나 심층 학습 모델을 훈련시키기에 충분한 대규모 AFM 이미지 데이터 세트를 생성하는 것은 비현실적입니다. 따라서 우리는 이미징 과정을 시뮬레이션하는 가상 AFM 프레임워크를 개발하고, 다중 뷰 합성 AFM 이미지를 포함한 약 542,000개의 단백질 데이터 세트를 생성했습니다. 우리는 조건부 확산 모델을 훈련하여 포즈가 없는 입력으로부터 새로운 뷰를 합성하고, 인스턴스 특정 신경 방사장(NeRF) 모델을 사용하여 3D 구조를 재구성합니다. 우리가 재구성한 3D 단백질 구조는 AFM 이미징 해상도 내에서 평균 챔퍼 거리(Chamfer Distance)를 달성하여 높은 구조적 충실도를 반영합니다. 우리의 방법은 다양한 PC의 실험적 AFM 이미지에서 광범위하게 검증되었으며, 정확하고 비용 효율적인 단백질 복합체 구조 예측과 AFM 실험을 통한 신속한 반복 검증에 강력한 잠재력을 보여줍니다.

## 📝 요약

ProFusion은 대형 단백질 복합체의 구조 예측을 개선하기 위해 딥러닝 모델과 원자력 현미경(AFM)을 결합한 하이브리드 프레임워크입니다. AFM은 다양한 각도에서 고해상도 데이터를 제공하여 3D 재구성을 가능하게 하지만, 대규모 AFM 데이터셋을 구축하는 것은 비현실적입니다. 이를 해결하기 위해 가상 AFM 프레임워크를 개발하여 약 542,000개의 단백질에 대한 합성 AFM 이미지를 생성했습니다. 조건부 확산 모델과 Neural Radiance Field(NeRF) 모델을 사용하여 새로운 시점을 생성하고 3D 구조를 재구성했습니다. 결과적으로, 재구성된 3D 구조는 높은 구조적 정확성을 보였으며, 다양한 단백질 복합체에 대한 실험적 AFM 이미지로 검증되었습니다. 이 방법은 정확하고 비용 효율적인 단백질 복합체 구조 예측에 유망한 가능성을 제시합니다.

## 🎯 주요 포인트

- 1. ProFusion은 딥러닝 모델과 원자력 현미경(AFM)을 통합하여 다중 시점 데이터를 활용한 3D 단백질 구조 예측을 가능하게 합니다.
- 2. 대규모 AFM 이미지 데이터셋을 생성하기 어려운 문제를 해결하기 위해 가상 AFM 프레임워크를 개발하여 약 542,000개의 단백질에 대한 합성 AFM 이미지를 생성했습니다.
- 3. 조건부 확산 모델을 사용하여 새로운 시점을 합성하고, 인스턴스별 Neural Radiance Field (NeRF) 모델을 통해 3D 구조를 재구성합니다.
- 4. 재구성된 3D 단백질 구조는 AFM 이미지 해상도 내에서 평균 Chamfer Distance를 달성하여 높은 구조적 정확성을 보여줍니다.
- 5. 다양한 단백질 복합체에 대한 실험적 AFM 이미지로 검증된 본 방법은 정확하고 비용 효율적인 단백질 복합체 구조 예측 및 신속한 반복 검증의 가능성을 제시합니다.


---

*Generated on 2025-09-23 11:54:20*