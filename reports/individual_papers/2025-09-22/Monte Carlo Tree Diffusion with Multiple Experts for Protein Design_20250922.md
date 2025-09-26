---
keywords:
  - Monte Carlo Tree Diffusion
  - Multiple Experts
  - Inverse Folding
  - Diffusion Denoising
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15796
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:13:39.160613",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Monte Carlo Tree Diffusion",
    "Multiple Experts",
    "Inverse Folding",
    "Diffusion Denoising"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Monte Carlo Tree Diffusion": 0.78,
    "Multiple Experts": 0.75,
    "Inverse Folding": 0.8,
    "Diffusion Denoising": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Monte Carlo Tree Diffusion",
        "canonical": "Monte Carlo Tree Diffusion",
        "aliases": [
          "MCTD"
        ],
        "category": "unique_technical",
        "rationale": "A novel approach integrating diffusion models with tree search, offering a new perspective in protein design.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Multiple Experts",
        "canonical": "Multiple Experts",
        "aliases": [
          "Expert Ensembles"
        ],
        "category": "specific_connectable",
        "rationale": "Enhances exploration in protein design by leveraging diverse expert models, which is a key concept in ensemble learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.72,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Inverse Folding",
        "canonical": "Inverse Folding",
        "aliases": [
          "Protein Inverse Folding"
        ],
        "category": "specific_connectable",
        "rationale": "A critical task in protein design, connecting to broader themes in structural biology and computational modeling.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.8
      },
      {
        "surface": "Diffusion Denoising",
        "canonical": "Diffusion Denoising",
        "aliases": [
          "Denoising Diffusion"
        ],
        "category": "unique_technical",
        "rationale": "Central to the proposed method's rollout engine, linking to diffusion models in machine learning.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "Monte Carlo Tree Search",
      "autogressive planners",
      "pLDDT"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Monte Carlo Tree Diffusion",
      "resolved_canonical": "Monte Carlo Tree Diffusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Multiple Experts",
      "resolved_canonical": "Multiple Experts",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.72,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Inverse Folding",
      "resolved_canonical": "Inverse Folding",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Diffusion Denoising",
      "resolved_canonical": "Diffusion Denoising",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Monte Carlo Tree Diffusion with Multiple Experts for Protein Design

**Korean Title:** 단백질 설계를 위한 다중 전문가 몬테카를로 트리 확산

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15796.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15796](https://arxiv.org/abs/2509.15796)

## 🔗 유사한 논문
- [[2025-09-22/ProFusion_ 3D Reconstruction of Protein Complex Structures from Multi-view AFM Images_20250922|ProFusion: 3D Reconstruction of Protein Complex Structures from Multi-view AFM Images]] (80.5% similar)
- [[2025-09-18/Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery_20250918|Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery]] (80.3% similar)
- [[2025-09-22/DiEP_ Adaptive Mixture-of-Experts Compression through Differentiable Expert Pruning_20250922|DiEP: Adaptive Mixture-of-Experts Compression through Differentiable Expert Pruning]] (79.4% similar)
- [[2025-09-22/TrueMoE_ Dual-Routing Mixture of Discriminative Experts for Synthetic Image Detection_20250922|TrueMoE: Dual-Routing Mixture of Discriminative Experts for Synthetic Image Detection]] (79.2% similar)
- [[2025-09-18/Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model_20250918|Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model]] (79.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multiple Experts|Multiple Experts]], [[keywords/Inverse Folding|Inverse Folding]]
**⚡ Unique Technical**: [[keywords/Monte Carlo Tree Diffusion|Monte Carlo Tree Diffusion]], [[keywords/Diffusion Denoising|Diffusion Denoising]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15796v1 Announce Type: cross 
Abstract: The goal of protein design is to generate amino acid sequences that fold into functional structures with desired properties. Prior methods combining autoregressive language models with Monte Carlo Tree Search (MCTS) struggle with long-range dependencies and suffer from an impractically large search space. We propose MCTD-ME, Monte Carlo Tree Diffusion with Multiple Experts, which integrates masked diffusion models with tree search to enable multi-token planning and efficient exploration. Unlike autoregressive planners, MCTD-ME uses biophysical-fidelity-enhanced diffusion denoising as the rollout engine, jointly revising multiple positions and scaling to large sequence spaces. It further leverages experts of varying capacities to enrich exploration, guided by a pLDDT-based masking schedule that targets low-confidence regions while preserving reliable residues. We propose a novel multi-expert selection rule (PH-UCT-ME) extends predictive-entropy UCT to expert ensembles. On the inverse folding task (CAMEO and PDB benchmarks), MCTD-ME outperforms single-expert and unguided baselines in both sequence recovery (AAR) and structural similarity (scTM), with gains increasing for longer proteins and benefiting from multi-expert guidance. More generally, the framework is model-agnostic and applicable beyond inverse folding, including de novo protein engineering and multi-objective molecular generation.

## 🔍 Abstract (한글 번역)

arXiv:2509.15796v1 발표 유형: 교차  
초록: 단백질 설계의 목표는 원하는 특성을 가진 기능적 구조로 접히는 아미노산 서열을 생성하는 것입니다. 이전의 자귀회귀 언어 모델과 몬테카를로 트리 탐색(MCTS)을 결합한 방법은 장거리 의존성에서 어려움을 겪고, 비현실적으로 큰 탐색 공간을 가지고 있습니다. 우리는 MCTD-ME, 다중 전문가를 활용한 몬테카를로 트리 확산(Monte Carlo Tree Diffusion with Multiple Experts)을 제안합니다. 이는 마스크된 확산 모델을 트리 탐색과 통합하여 다중 토큰 계획 및 효율적인 탐색을 가능하게 합니다. 자귀회귀 계획자와 달리, MCTD-ME는 생물물리적 충실도가 강화된 확산 디노이징을 롤아웃 엔진으로 사용하여 여러 위치를 공동으로 수정하고 큰 서열 공간으로 확장합니다. 또한, 다양한 역량을 가진 전문가들을 활용하여 탐색을 풍부하게 하며, 신뢰도가 낮은 영역을 목표로 하면서 신뢰할 수 있는 잔기를 보존하는 pLDDT 기반 마스킹 일정에 의해 안내됩니다. 우리는 예측 엔트로피 UCT를 전문가 앙상블로 확장하는 새로운 다중 전문가 선택 규칙(PH-UCT-ME)을 제안합니다. 역접힘 과제(CAMEO 및 PDB 벤치마크)에서 MCTD-ME는 단일 전문가 및 비유도 기준선보다 서열 회복(AAR) 및 구조적 유사성(scTM) 모두에서 뛰어난 성능을 보이며, 긴 단백질에 대한 이득이 증가하고 다중 전문가 지침의 혜택을 받습니다. 보다 일반적으로, 이 프레임워크는 모델에 구애받지 않으며, 역접힘을 넘어 새로운 단백질 공학 및 다목적 분자 생성에도 적용할 수 있습니다.

## 📝 요약

이 논문은 단백질 설계에서 원하는 기능을 가진 아미노산 서열을 생성하는 방법을 제안합니다. 기존의 자가회귀 언어 모델과 몬테카를로 트리 탐색(MCTS) 방법은 긴 범위의 의존성 문제와 큰 탐색 공간으로 인해 어려움을 겪습니다. 이를 해결하기 위해, 저자들은 MCTD-ME라는 새로운 방법을 제안합니다. 이 방법은 마스크된 확산 모델과 트리 탐색을 결합하여 다중 토큰 계획과 효율적인 탐색을 가능하게 합니다. MCTD-ME는 생물물리적 정확성을 높인 확산 복원 엔진을 사용하여 여러 위치를 동시에 수정하고, 다양한 전문가를 활용하여 탐색을 풍부하게 합니다. 또한, pLDDT 기반 마스킹 스케줄을 통해 신뢰도가 낮은 영역을 타겟으로 하여 탐색을 안내합니다. 제안된 다중 전문가 선택 규칙(PH-UCT-ME)은 예측 엔트로피 UCT를 전문가 집단에 확장합니다. CAMEO와 PDB 벤치마크에서의 역접힘 과제에서 MCTD-ME는 단일 전문가 및 비유도 기준보다 서열 회복과 구조적 유사성에서 뛰어난 성능을 보였으며, 특히 긴 단백질에서 그 성능이 두드러졌습니다. 이 프레임워크는 모델에 구애받지 않으며, 역접힘뿐만 아니라 새로운 단백질 공학 및 다목적 분자 생성에도 적용 가능합니다.

## 🎯 주요 포인트

- 1. MCTD-ME는 마스크된 확산 모델과 트리 탐색을 결합하여 다중 토큰 계획과 효율적인 탐색을 가능하게 합니다.
- 2. 이 방법은 생물물리적 정확성이 강화된 확산 복원을 사용하여 여러 위치를 동시에 수정하고 큰 시퀀스 공간으로 확장할 수 있습니다.
- 3. 다양한 역량을 가진 전문가들을 활용하여 탐색을 풍부하게 하고, pLDDT 기반 마스킹 스케줄을 통해 신뢰도가 낮은 영역을 목표로 하면서 신뢰할 수 있는 잔여물을 보존합니다.
- 4. 새로운 다중 전문가 선택 규칙인 PH-UCT-ME는 예측 엔트로피 UCT를 전문가 앙상블로 확장합니다.
- 5. MCTD-ME는 역 폴딩 작업에서 단일 전문가 및 비가이드 기준보다 시퀀스 회복 및 구조적 유사성에서 우수한 성능을 보이며, 특히 긴 단백질에서 다중 전문가의 지도를 통해 이점을 얻습니다.


---

*Generated on 2025-09-23 09:13:39*