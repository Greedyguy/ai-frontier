---
keywords:
  - Space Group Equivariant Crystal Diffusion
  - Transformer
  - Space Group Symmetries
  - SE(3)-invariant
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2505.10994
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:56:47.884632",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Space Group Equivariant Crystal Diffusion",
    "Transformer",
    "Space Group Symmetries",
    "SE(3)-invariant"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Space Group Equivariant Crystal Diffusion": 0.8,
    "Transformer": 0.85,
    "Space Group Symmetries": 0.78,
    "SE(3)-invariant": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Space Group Equivariant Crystal Diffusion",
        "canonical": "Space Group Equivariant Crystal Diffusion",
        "aliases": [
          "SGEquiDiff"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach specific to the paper, linking space group symmetries with crystal generation.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Transformer-based Autoregressive Sampling",
        "canonical": "Transformer",
        "aliases": [
          "Autoregressive Sampling"
        ],
        "category": "broad_technical",
        "rationale": "Connects the use of Transformer models in autoregressive sampling, a key component in the methodology.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Space Group Symmetries",
        "canonical": "Space Group Symmetries",
        "aliases": [
          "Symmetry Groups"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's focus on crystal properties and their generative modeling.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "SE(3)-invariant",
        "canonical": "SE(3)-invariant",
        "aliases": [
          "Special Euclidean Group Invariance"
        ],
        "category": "specific_connectable",
        "rationale": "Essential for understanding the geometric invariance in crystal modeling.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "benchmark datasets"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Space Group Equivariant Crystal Diffusion",
      "resolved_canonical": "Space Group Equivariant Crystal Diffusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Transformer-based Autoregressive Sampling",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Space Group Symmetries",
      "resolved_canonical": "Space Group Symmetries",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "SE(3)-invariant",
      "resolved_canonical": "SE(3)-invariant",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Space Group Equivariant Crystal Diffusion

**Korean Title:** 공간군 등변 결정 확산

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.10994.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2505.10994](https://arxiv.org/abs/2505.10994)

## 🔗 유사한 논문
- [[2025-09-22/G2D2_ Gradient-Guided Discrete Diffusion for Inverse Problem Solving_20250922|G2D2: Gradient-Guided Discrete Diffusion for Inverse Problem Solving]] (80.4% similar)
- [[2025-09-22/SAGE_ Semantic-Aware Shared Sampling for Efficient Diffusion_20250922|SAGE: Semantic-Aware Shared Sampling for Efficient Diffusion]] (80.2% similar)
- [[2025-09-22/LowDiff_ Efficient Diffusion Sampling with Low-Resolution Condition_20250922|LowDiff: Efficient Diffusion Sampling with Low-Resolution Condition]] (79.6% similar)
- [[2025-09-22/An Equivariant Graph Network for Interpretable Nanoporous Materials Design_20250922|An Equivariant Graph Network for Interpretable Nanoporous Materials Design]] (78.6% similar)
- [[2025-09-17/SpecDiff_ Accelerating Diffusion Model Inference with Self-Speculation_20250917|SpecDiff: Accelerating Diffusion Model Inference with Self-Speculation]] (78.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/SE(3)-invariant|SE(3)-invariant]]
**⚡ Unique Technical**: [[keywords/Space Group Equivariant Crystal Diffusion|Space Group Equivariant Crystal Diffusion]], [[keywords/Space Group Symmetries|Space Group Symmetries]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.10994v2 Announce Type: replace-cross 
Abstract: Accelerating inverse design of crystalline materials with generative models has significant implications for a range of technologies. Unlike other atomic systems, 3D crystals are invariant to discrete groups of isometries called the space groups. Crucially, these space group symmetries are known to heavily influence materials properties. We propose SGEquiDiff, a crystal generative model which naturally handles space group constraints with space group invariant likelihoods. SGEquiD-iff consists of an SE(3)-invariant, telescoping discrete sampler of crystal lattices; permutation-invariant, transformer-based autoregressive sampling of Wyckoff positions, elements, and numbers of symmetrically unique atoms; and space group equivariant diffusion of atomic coordinates. We show that space group equivariant vector fields automatically live in the tangent spaces of the Wyckoff positions. SGEquiDiff achieves state-of-the-art performance on standard benchmark datasets as assessed by quantitative proxy metrics and quantum mechanical calculations. Our code is available at https://github.com/rees-c/sgequidiff.

## 🔍 Abstract (한글 번역)

arXiv:2505.10994v2 발표 유형: 교차 교체  
초록: 생성 모델을 사용한 결정성 물질의 역설계 가속화는 다양한 기술에 중대한 영향을 미칩니다. 다른 원자 시스템과 달리, 3D 결정체는 공간군이라고 불리는 이산적인 등거리 변환 그룹에 대해 불변성을 가집니다. 중요한 점은 이러한 공간군 대칭이 물질의 특성에 크게 영향을 미친다는 것입니다. 우리는 공간군 불변 가능성을 통해 공간군 제약을 자연스럽게 처리하는 결정 생성 모델인 SGEquiDiff를 제안합니다. SGEquiDiff는 SE(3) 불변의 결정 격자에 대한 망원경식 이산 샘플러, 순열 불변의 트랜스포머 기반 자귀적 샘플링을 통한 Wyckoff 위치, 원소 및 대칭적으로 고유한 원자의 수, 그리고 원자 좌표의 공간군 등변 확산으로 구성됩니다. 우리는 공간군 등변 벡터장이 자동으로 Wyckoff 위치의 접공간에 존재함을 보여줍니다. SGEquiDiff는 정량적 대리 지표와 양자역학적 계산에 의해 평가된 표준 벤치마크 데이터셋에서 최첨단 성능을 달성합니다. 우리의 코드는 https://github.com/rees-c/sgequidiff에서 이용할 수 있습니다.

## 📝 요약

SGEquiDiff는 결정체의 역설계를 가속화하기 위해 공간군 대칭을 고려한 생성 모델입니다. 이 모델은 SE(3)-불변의 격자 샘플링, Wyckoff 위치 및 원소의 순열 불변 샘플링, 원자 좌표의 공간군 등가 확산을 포함합니다. 이를 통해 Wyckoff 위치의 접공간에서 자동으로 작동하는 벡터 필드를 구현합니다. SGEquiDiff는 표준 벤치마크 데이터셋에서 최첨단 성능을 보이며, 이는 정량적 대리 메트릭과 양자역학적 계산으로 평가되었습니다. 코드와 자세한 내용은 GitHub에서 확인할 수 있습니다.

## 🎯 주요 포인트

- 1. SGEquiDiff는 공간군 대칭을 자연스럽게 처리하는 결정 생성 모델로, 공간군 불변 가능성을 활용합니다.
- 2. 모델은 SE(3)-불변의 망원경형 결정 격자 샘플러와 순열 불변의 트랜스포머 기반 자율 회귀 샘플링을 포함합니다.
- 3. 공간군 등변 벡터 필드는 Wyckoff 위치의 접공간에 자동으로 존재합니다.
- 4. SGEquiDiff는 표준 벤치마크 데이터셋에서 최첨단 성능을 달성했습니다.
- 5. 연구의 코드는 GitHub에서 공개되어 있습니다.


---

*Generated on 2025-09-23 09:56:47*