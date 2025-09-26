---
keywords:
  - ChannelFlow-Tools
  - 3D Obstructed Channel Flows
  - CFD Surrogate Modeling
  - Signed Distance Field Voxelization
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15236
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T08:47:38.688636",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "ChannelFlow-Tools",
    "3D Obstructed Channel Flows",
    "CFD Surrogate Modeling",
    "Signed Distance Field Voxelization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "ChannelFlow-Tools": 0.8,
    "3D Obstructed Channel Flows": 0.78,
    "CFD Surrogate Modeling": 0.82,
    "Signed Distance Field Voxelization": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "ChannelFlow-Tools",
        "canonical": "ChannelFlow-Tools",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "ChannelFlow-Tools is a unique toolchain for dataset creation in CFD, making it a distinct technical concept.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "3D obstructed channel flows",
        "canonical": "3D Obstructed Channel Flows",
        "aliases": [
          "3D channel flows"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application area within CFD, providing a focused context for linking related research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "CFD surrogate modeling",
        "canonical": "CFD Surrogate Modeling",
        "aliases": [
          "Computational Fluid Dynamics surrogate modeling"
        ],
        "category": "specific_connectable",
        "rationale": "Surrogate modeling in CFD is a specialized technique that connects to broader machine learning applications.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "signed distance field voxelization",
        "canonical": "Signed Distance Field Voxelization",
        "aliases": [
          "SDF voxelization"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific technical process used in geometry synthesis, relevant for linking to computational geometry.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "programmatic CAD solid generation",
      "automated solver orchestration",
      "Cartesian resampling"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "ChannelFlow-Tools",
      "resolved_canonical": "ChannelFlow-Tools",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "3D obstructed channel flows",
      "resolved_canonical": "3D Obstructed Channel Flows",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "CFD surrogate modeling",
      "resolved_canonical": "CFD Surrogate Modeling",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "signed distance field voxelization",
      "resolved_canonical": "Signed Distance Field Voxelization",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# ChannelFlow-Tools: A Standardized Dataset Creation Pipeline for 3D Obstructed Channel Flows

**Korean Title:** ChannelFlow-Tools: 3D 장애물 채널 흐름을 위한 표준화된 데이터셋 생성 파이프라인

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15236.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15236](https://arxiv.org/abs/2509.15236)

## 🔗 유사한 논문
- [[2025-09-22/A Flow-rate-conserving CNN-based Domain Decomposition Method for Blood Flow Simulations_20250922|A Flow-rate-conserving CNN-based Domain Decomposition Method for Blood Flow Simulations]] (80.7% similar)
- [[2025-09-22/GenCAD-3D_ CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing_20250922|GenCAD-3D: CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing]] (80.0% similar)
- [[2025-09-19/FlowDrive_ Energy Flow Field for End-to-End Autonomous Driving_20250919|FlowDrive: Energy Flow Field for End-to-End Autonomous Driving]] (78.8% similar)
- [[2025-09-22/DebFlow_ Automating Agent Creation via Agent Debate_20250922|DebFlow: Automating Agent Creation via Agent Debate]] (78.2% similar)
- [[2025-09-18/Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (77.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/CFD Surrogate Modeling|CFD Surrogate Modeling]]
**⚡ Unique Technical**: [[keywords/ChannelFlow-Tools|ChannelFlow-Tools]], [[keywords/3D Obstructed Channel Flows|3D Obstructed Channel Flows]], [[keywords/Signed Distance Field Voxelization|Signed Distance Field Voxelization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15236v1 Announce Type: cross 
Abstract: We present ChannelFlow-Tools, a configuration-driven framework that standardizes the end-to-end path from programmatic CAD solid generation to ML-ready inputs and targets for 3D obstructed channel flows. The toolchain integrates geometry synthesis with feasibility checks, signed distance field (SDF) voxelization, automated solver orchestration on HPC (waLBerla LBM), and Cartesian resampling to co-registered multi-resolution tensors. A single Hydra/OmegaConf configuration governs all stages, enabling deterministic reproduction and controlled ablations. As a case study, we generate 10k+ scenes spanning Re=100-15000 with diverse shapes and poses. An end-to-end evaluation of storage trade-offs directly from the emitted artifacts, a minimal 3D U-Net at 128x32x32, and example surrogate models with dataset size illustrate that the standardized representations support reproducible ML training. ChannelFlow-Tools turns one-off dataset creation into a reproducible, configurable pipeline for CFD surrogate modeling.

## 🔍 Abstract (한글 번역)

arXiv:2509.15236v1 발표 유형: 교차  
초록: 우리는 ChannelFlow-Tools를 소개합니다. 이는 프로그래매틱 CAD 솔리드 생성에서 ML 준비 입력 및 3D 장애물 채널 흐름의 목표까지의 전체 경로를 표준화하는 구성 주도 프레임워크입니다. 이 도구 체인은 기하학적 합성, 타당성 검사, 서명 거리 필드(SDF) 복셀화, HPC(waLBerla LBM)에서의 자동화된 솔버 오케스트레이션, 그리고 공동 등록된 다중 해상도 텐서로의 직교 재샘플링을 통합합니다. 모든 단계는 단일 Hydra/OmegaConf 구성을 통해 관리되며, 이는 결정론적 재현성과 제어된 소거를 가능하게 합니다. 사례 연구로서, 우리는 다양한 형태와 자세를 가진 Re=100-15000 범위의 10,000개 이상의 장면을 생성합니다. 방출된 아티팩트로부터 직접적으로 저장소의 절충을 평가하고, 128x32x32의 최소 3D U-Net 및 데이터셋 크기를 가진 예제 대리 모델을 통해 표준화된 표현이 재현 가능한 ML 훈련을 지원함을 보여줍니다. ChannelFlow-Tools는 일회성 데이터셋 생성을 CFD 대리 모델링을 위한 재현 가능하고 구성 가능한 파이프라인으로 전환합니다.

## 📝 요약

ChannelFlow-Tools는 3D 장애물 채널 흐름을 위한 프로그램적 CAD 생성부터 머신러닝 준비 입력과 목표까지의 과정을 표준화하는 프레임워크입니다. 이 도구는 기하학적 합성, 타당성 검사, 서명 거리 필드(voxelization), HPC에서의 자동 솔버 조정, 다중 해상도 텐서의 직교 재샘플링을 통합합니다. Hydra/OmegaConf 설정을 통해 모든 단계를 제어하여 재현성과 통제된 실험이 가능합니다. 사례 연구로 다양한 형태와 자세를 가진 10,000개 이상의 장면을 생성하고, 저장 공간의 효율성을 평가하며, 3D U-Net 및 대체 모델을 통해 표준화된 표현이 재현 가능한 머신러닝 훈련을 지원함을 보여줍니다. 이를 통해 CFD 대체 모델링을 위한 재현 가능하고 구성 가능한 파이프라인을 제공합니다.

## 🎯 주요 포인트

- 1. ChannelFlow-Tools는 프로그램적 CAD 솔리드 생성부터 ML 준비 입력 및 목표까지의 경로를 표준화하는 프레임워크입니다.
- 2. 이 도구 체인은 기하학적 합성, 타당성 검사, 서명 거리 필드(SDF) 복셀화, HPC에서의 자동 솔버 오케스트레이션, 다중 해상도 텐서의 직교 재샘플링을 통합합니다.
- 3. Hydra/OmegaConf 구성 하나로 모든 단계를 제어하여 결정론적 재현과 통제된 소거를 가능하게 합니다.
- 4. 다양한 형태와 자세를 가진 Re=100-15000 범위의 10,000개 이상의 장면을 생성하는 사례 연구를 수행했습니다.
- 5. ChannelFlow-Tools는 CFD 대리 모델링을 위한 재현 가능하고 구성 가능한 파이프라인으로 일회성 데이터셋 생성을 전환합니다.


---

*Generated on 2025-09-23 08:47:38*