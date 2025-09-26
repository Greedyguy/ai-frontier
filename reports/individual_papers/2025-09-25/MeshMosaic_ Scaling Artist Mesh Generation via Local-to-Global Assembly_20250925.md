---
keywords:
  - MeshMosaic
  - Transformer
  - Autoregressive Models
  - High-Resolution Meshes
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.19995
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:17:54.297024",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "MeshMosaic",
    "Transformer",
    "Autoregressive Models",
    "High-Resolution Meshes"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "MeshMosaic": 0.85,
    "Transformer": 0.8,
    "Autoregressive Models": 0.78,
    "High-Resolution Meshes": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "MeshMosaic",
        "canonical": "MeshMosaic",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "MeshMosaic is a novel framework introduced in this paper, providing a unique approach to mesh generation that could be a key reference point for future research.",
        "novelty_score": 0.95,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "transformer-based methods",
        "canonical": "Transformer",
        "aliases": [
          "transformer methods"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational technology in this domain, and linking to them provides context for the generative model challenges discussed.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "autoregressive generative models",
        "canonical": "Autoregressive Models",
        "aliases": [
          "autoregressive models"
        ],
        "category": "specific_connectable",
        "rationale": "Autoregressive models are central to the paper's methodology, offering potential connections to related generative model research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "high-resolution meshes",
        "canonical": "High-Resolution Meshes",
        "aliases": [
          "detailed meshes"
        ],
        "category": "unique_technical",
        "rationale": "High-resolution meshes are a specific focus of the paper, highlighting the technical advancements in mesh scalability.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
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
      "candidate_surface": "MeshMosaic",
      "resolved_canonical": "MeshMosaic",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "transformer-based methods",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "autoregressive generative models",
      "resolved_canonical": "Autoregressive Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "high-resolution meshes",
      "resolved_canonical": "High-Resolution Meshes",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# MeshMosaic: Scaling Artist Mesh Generation via Local-to-Global Assembly

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19995.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.19995](https://arxiv.org/abs/2509.19995)

## 🔗 유사한 논문
- [[2025-09-25/TimeMosaic_ Temporal Heterogeneity Guided Time Series Forecasting via Adaptive Granularity Patch and Segment-wise Decoding_20250925|TimeMosaic: Temporal Heterogeneity Guided Time Series Forecasting via Adaptive Granularity Patch and Segment-wise Decoding]] (83.3% similar)
- [[2025-09-24/Hyper-Bagel_ A Unified Acceleration Framework for Multimodal Understanding and Generation_20250924|Hyper-Bagel: A Unified Acceleration Framework for Multimodal Understanding and Generation]] (81.7% similar)
- [[2025-09-23/Preconditioned Deformation Grids_20250923|Preconditioned Deformation Grids]] (81.5% similar)
- [[2025-09-24/MeshODENet_ A Graph-Informed Neural Ordinary Differential Equation Neural Network for Simulating Mesh-Based Physical Systems_20250924|MeshODENet: A Graph-Informed Neural Ordinary Differential Equation Neural Network for Simulating Mesh-Based Physical Systems]] (81.4% similar)
- [[2025-09-23/MMPart_ Harnessing Multi-Modal Large Language Models for Part-Aware 3D Generation_20250923|MMPart: Harnessing Multi-Modal Large Language Models for Part-Aware 3D Generation]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Autoregressive Models|Autoregressive Models]]
**⚡ Unique Technical**: [[keywords/MeshMosaic|MeshMosaic]], [[keywords/High-Resolution Meshes|High-Resolution Meshes]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19995v1 Announce Type: cross 
Abstract: Scaling artist-designed meshes to high triangle numbers remains challenging for autoregressive generative models. Existing transformer-based methods suffer from long-sequence bottlenecks and limited quantization resolution, primarily due to the large number of tokens required and constrained quantization granularity. These issues prevent faithful reproduction of fine geometric details and structured density patterns. We introduce MeshMosaic, a novel local-to-global framework for artist mesh generation that scales to over 100K triangles--substantially surpassing prior methods, which typically handle only around 8K faces. MeshMosaic first segments shapes into patches, generating each patch autoregressively and leveraging shared boundary conditions to promote coherence, symmetry, and seamless connectivity between neighboring regions. This strategy enhances scalability to high-resolution meshes by quantizing patches individually, resulting in more symmetrical and organized mesh density and structure. Extensive experiments across multiple public datasets demonstrate that MeshMosaic significantly outperforms state-of-the-art methods in both geometric fidelity and user preference, supporting superior detail representation and practical mesh generation for real-world applications.

## 📝 요약

MeshMosaic는 예술가가 디자인한 메쉬를 100K 이상의 삼각형으로 확장할 수 있는 새로운 프레임워크로, 기존 방법의 한계를 극복합니다. 이 방법은 메쉬를 패치로 분할하고, 각 패치를 자동 회귀적으로 생성하며, 경계 조건을 공유하여 인접 영역 간의 일관성과 대칭성을 유지합니다. 이를 통해 고해상도 메쉬의 확장성을 높이고, 패치를 개별적으로 양자화하여 더 대칭적이고 조직적인 메쉬 구조를 구현합니다. 다양한 공공 데이터셋 실험 결과, MeshMosaic는 기존 최첨단 방법들보다 기하학적 충실도와 사용자 선호도에서 우수한 성능을 보이며, 실제 응용을 위한 메쉬 생성에 적합함을 입증했습니다.

## 🎯 주요 포인트

- 1. MeshMosaic는 100K 이상의 삼각형을 처리할 수 있는 새로운 로컬-투-글로벌 프레임워크로, 기존의 약 8K 면을 처리하는 방법을 크게 능가합니다.
- 2. 이 방법은 모양을 패치로 분할하고, 각 패치를 자동 회귀적으로 생성하며, 공유 경계 조건을 활용하여 인접 영역 간의 일관성과 대칭성, 매끄러운 연결성을 촉진합니다.
- 3. 패치를 개별적으로 양자화하여 높은 해상도의 메시로 확장성을 높이고, 더 대칭적이고 조직적인 메시 밀도와 구조를 제공합니다.
- 4. 여러 공공 데이터셋에 대한 광범위한 실험에서 MeshMosaic는 기하학적 충실도와 사용자 선호도에서 최첨단 방법을 크게 능가합니다.
- 5. MeshMosaic는 세부 표현과 실용적인 메시 생성에서 우수한 성능을 발휘하여 실제 응용 프로그램에 적합합니다.


---

*Generated on 2025-09-26 09:17:54*