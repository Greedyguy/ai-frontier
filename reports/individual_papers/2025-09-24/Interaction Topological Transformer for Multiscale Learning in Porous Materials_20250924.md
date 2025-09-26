<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:54:58.326217",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Interaction Topological Transformer",
    "Transformer",
    "Self-supervised Learning",
    "Porous Materials"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Interaction Topological Transformer": 0.8,
    "Transformer": 0.85,
    "Self-supervised Learning": 0.82,
    "Porous Materials": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Interaction Topological Transformer",
        "canonical": "Interaction Topological Transformer",
        "aliases": [
          "ITT"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel framework for multiscale learning in porous materials, enhancing connectivity with specific research in material science.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Connects with a widely used architecture in machine learning, facilitating links to related technical concepts.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "Self-supervised pretraining",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "self-supervised pretraining"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights a key learning strategy that is crucial for the model's performance, linking to broader machine learning techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Porous materials",
        "canonical": "Porous Materials",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Central to the study, providing a specific domain for linking material science research.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "multiscale learning",
      "materials information"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Interaction Topological Transformer",
      "resolved_canonical": "Interaction Topological Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Self-supervised pretraining",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Porous materials",
      "resolved_canonical": "Porous Materials",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Interaction Topological Transformer for Multiscale Learning in Porous Materials

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18573.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18573](https://arxiv.org/abs/2509.18573)

## 🔗 유사한 논문
- [[2025-09-22/StFT_ Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction_20250922|StFT: Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction]] (81.2% similar)
- [[2025-09-18/Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery_20250918|Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery]] (80.7% similar)
- [[2025-09-22/A Multi-Scale Graph Neural Process with Cross-Drug Co-Attention for Drug-Drug Interactions Prediction_20250922|A Multi-Scale Graph Neural Process with Cross-Drug Co-Attention for Drug-Drug Interactions Prediction]] (80.4% similar)
- [[2025-09-23/Conv-like Scale-Fusion Time Series Transformer_ A Multi-Scale Representation for Variable-Length Long Time Series_20250923|Conv-like Scale-Fusion Time Series Transformer: A Multi-Scale Representation for Variable-Length Long Time Series]] (80.2% similar)
- [[2025-09-23/HyperTTA_ Test-Time Adaptation for Hyperspectral Image Classification under Distribution Shifts_20250923|HyperTTA: Test-Time Adaptation for Hyperspectral Image Classification under Distribution Shifts]] (79.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Interaction Topological Transformer|Interaction Topological Transformer]], [[keywords/Porous Materials|Porous Materials]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18573v1 Announce Type: cross 
Abstract: Porous materials exhibit vast structural diversity and support critical applications in gas storage, separations, and catalysis. However, predictive modeling remains challenging due to the multiscale nature of structure-property relationships, where performance is governed by both local chemical environments and global pore-network topology. These complexities, combined with sparse and unevenly distributed labeled data, hinder generalization across material families. We propose the Interaction Topological Transformer (ITT), a unified data-efficient framework that leverages novel interaction topology to capture materials information across multiple scales and multiple levels, including structural, elemental, atomic, and pairwise-elemental organization. ITT extracts scale-aware features that reflect both compositional and relational structure within complex porous frameworks, and integrates them through a built-in Transformer architecture that supports joint reasoning across scales. Trained using a two-stage strategy, i.e., self-supervised pretraining on 0.6 million unlabeled structures followed by supervised fine-tuning, ITT achieves state-of-the-art, accurate, and transferable predictions for adsorption, transport, and stability properties. This framework provides a principled and scalable path for learning-guided discovery in structurally and chemically diverse porous materials.

## 📝 요약

다공성 물질의 구조적 다양성과 다중 스케일의 구조-특성 관계로 인해 예측 모델링이 어렵습니다. 이를 해결하기 위해, 우리는 다중 스케일 및 수준에서 재료 정보를 포착하는 Interaction Topological Transformer (ITT)를 제안합니다. ITT는 구조적, 원소적, 원자적, 쌍원소적 조직을 포함한 다양한 수준의 정보를 통합하여 복잡한 다공성 구조 내의 조성 및 관계 구조를 반영하는 특징을 추출합니다. 이 프레임워크는 60만 개의 비라벨 데이터에 대한 자가 지도 사전 학습과 지도 학습 미세 조정을 통해 흡착, 수송, 안정성 예측에서 최첨단 성능을 달성합니다. ITT는 구조적 및 화학적으로 다양한 다공성 물질의 발견을 위한 효율적인 경로를 제공합니다.

## 🎯 주요 포인트

- 1. 다공성 물질의 구조적 다양성과 다중 스케일의 구조-특성 관계로 인해 예측 모델링이 어려움을 겪고 있습니다.
- 2. Interaction Topological Transformer (ITT)는 새로운 상호작용 위상 구조를 활용하여 다중 스케일 및 다중 수준에서 물질 정보를 포착하는 통합 데이터 효율적 프레임워크를 제안합니다.
- 3. ITT는 복잡한 다공성 구조 내의 조성적 및 관계적 구조를 반영하는 스케일 인식 기능을 추출하고, 이를 Transformer 아키텍처를 통해 통합하여 스케일 간 공동 추론을 지원합니다.
- 4. ITT는 60만 개의 비라벨링 구조에 대한 자가 지도 사전 학습과 지도 학습 미세 조정을 통해 흡착, 수송 및 안정성 특성에 대한 최첨단, 정확하고 전이 가능한 예측을 달성합니다.
- 5. 이 프레임워크는 구조적 및 화학적으로 다양한 다공성 물질에서 학습 기반 발견을 위한 원칙적이고 확장 가능한 경로를 제공합니다.


---

*Generated on 2025-09-24 13:54:58*