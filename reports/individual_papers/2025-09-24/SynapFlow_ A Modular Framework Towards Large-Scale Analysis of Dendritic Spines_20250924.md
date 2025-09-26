<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:13:23.813170",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Dendritic Spines",
    "Transformer",
    "Two-Photon Microscopy",
    "Feature Extraction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Dendritic Spines": 0.8,
    "Transformer": 0.7,
    "Two-Photon Microscopy": 0.75,
    "Feature Extraction": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "dendritic spines",
        "canonical": "Dendritic Spines",
        "aliases": [
          "spines",
          "neural spines"
        ],
        "category": "unique_technical",
        "rationale": "Central to the study, providing a direct link to neuroscience research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "transformer-based detection",
        "canonical": "Transformer",
        "aliases": [
          "transformer detection"
        ],
        "category": "broad_technical",
        "rationale": "Connects to existing research in machine learning and computer vision.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "two-photon microscopy",
        "canonical": "Two-Photon Microscopy",
        "aliases": [
          "2-photon microscopy",
          "2P microscopy"
        ],
        "category": "unique_technical",
        "rationale": "Specific imaging technique crucial for the study's methodology.",
        "novelty_score": 0.65,
        "connectivity_score": 0.55,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "feature extraction",
        "canonical": "Feature Extraction",
        "aliases": [
          "feature analysis"
        ],
        "category": "specific_connectable",
        "rationale": "Key process in data analysis and machine learning, enhancing connectivity.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "modular",
      "pipeline",
      "baseline"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "dendritic spines",
      "resolved_canonical": "Dendritic Spines",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "transformer-based detection",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "two-photon microscopy",
      "resolved_canonical": "Two-Photon Microscopy",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.55,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "feature extraction",
      "resolved_canonical": "Feature Extraction",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# SynapFlow: A Modular Framework Towards Large-Scale Analysis of Dendritic Spines

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18926.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18926](https://arxiv.org/abs/2509.18926)

## 🔗 유사한 논문
- [[2025-09-23/Towards Generalized Synapse Detection Across Invertebrate Species_20250923|Towards Generalized Synapse Detection Across Invertebrate Species]] (83.8% similar)
- [[2025-09-23/DynSTG-Mamba_ Dynamic Spatio-Temporal Graph Mamba with Cross-Graph Knowledge Distillation for Gait Disorders Recognition_20250923|DynSTG-Mamba: Dynamic Spatio-Temporal Graph Mamba with Cross-Graph Knowledge Distillation for Gait Disorders Recognition]] (80.2% similar)
- [[2025-09-22/SLaM-DiMM_ Shared Latent Modeling for Diffusion Based Missing Modality Synthesis in MRI_20250922|SLaM-DiMM: Shared Latent Modeling for Diffusion Based Missing Modality Synthesis in MRI]] (80.2% similar)
- [[2025-09-23/Semantic and Visual Crop-Guided Diffusion Models for Heterogeneous Tissue Synthesis in Histopathology_20250923|Semantic and Visual Crop-Guided Diffusion Models for Heterogeneous Tissue Synthesis in Histopathology]] (80.1% similar)
- [[2025-09-24/Dynamical Modeling of Behaviorally Relevant Spatiotemporal Patterns in Neural Imaging Data_20250924|Dynamical Modeling of Behaviorally Relevant Spatiotemporal Patterns in Neural Imaging Data]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Feature Extraction|Feature Extraction]]
**⚡ Unique Technical**: [[keywords/Dendritic Spines|Dendritic Spines]], [[keywords/Two-Photon Microscopy|Two-Photon Microscopy]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18926v1 Announce Type: new 
Abstract: Dendritic spines are key structural components of excitatory synapses in the brain. Given the size of dendritic spines provides a proxy for synaptic efficacy, their detection and tracking across time is important for studies of the neural basis of learning and memory. Despite their relevance, large-scale analyses of the structural dynamics of dendritic spines in 3D+time microscopy data remain challenging and labor-intense. Here, we present a modular machine learning-based pipeline designed to automate the detection, time-tracking, and feature extraction of dendritic spines in volumes chronically recorded with two-photon microscopy. Our approach tackles the challenges posed by biological data by combining a transformer-based detection module, a depth-tracking component that integrates spatial features, a time-tracking module to associate 3D spines across time by leveraging spatial consistency, and a feature extraction unit that quantifies biologically relevant spine properties. We validate our method on open-source labeled spine data, and on two complementary annotated datasets that we publish alongside this work: one for detection and depth-tracking, and one for time-tracking, which, to the best of our knowledge, is the first data of this kind. To encourage future research, we release our data, code, and pre-trained weights at https://github.com/pamelaosuna/SynapFlow, establishing a baseline for scalable, end-to-end analysis of dendritic spine dynamics.

## 📝 요약

이 논문은 뇌의 흥분성 시냅스에서 중요한 구조적 요소인 수상돌기 가시의 3D+시간 현미경 데이터 분석을 자동화하는 기계 학습 기반 파이프라인을 제안합니다. 이 방법은 변환기 기반 탐지 모듈, 공간적 특징을 통합한 깊이 추적, 시간 일관성을 활용한 시간 추적, 생물학적으로 중요한 가시 특성을 정량화하는 특징 추출 유닛으로 구성되어 있습니다. 제안된 방법은 공개된 라벨 데이터와 새로 제공된 두 개의 주석 데이터셋으로 검증되었습니다. 연구의 결과물은 GitHub에서 공개되어 향후 연구를 위한 기초를 제공합니다.

## 🎯 주요 포인트

- 1. 수상돌기는 뇌의 흥분성 시냅스의 주요 구조적 구성 요소이며, 그 크기는 시냅스 효율성을 나타내는 지표로 사용됩니다.
- 2. 본 연구는 이차원 현미경으로 기록된 수상돌기의 검출, 시간 추적 및 특징 추출을 자동화하는 모듈식 기계 학습 기반 파이프라인을 제안합니다.
- 3. 제안된 방법은 변환기 기반 검출 모듈, 공간적 특징을 통합한 깊이 추적 구성 요소, 3D 수상돌기를 시간에 따라 연관시키는 시간 추적 모듈, 생물학적으로 관련된 수상돌기 특성을 정량화하는 특징 추출 유닛을 결합하여 문제를 해결합니다.
- 4. 우리는 공개 소스 레이블 수상돌기 데이터와 두 가지 보완적인 주석 데이터셋에서 우리의 방법을 검증하며, 이 데이터는 검출 및 깊이 추적, 시간 추적을 위한 최초의 데이터입니다.
- 5. 연구의 확산을 위해 데이터, 코드 및 사전 훈련된 가중치를 공개하여 수상돌기 역학의 확장 가능한 종단 간 분석에 대한 기준을 설정합니다.


---

*Generated on 2025-09-24 16:13:23*