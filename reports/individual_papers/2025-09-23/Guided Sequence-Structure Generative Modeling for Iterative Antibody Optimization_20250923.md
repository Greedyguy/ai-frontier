---
keywords:
  - Sequence-Structure Generative Model
  - Antibody-Antigen Complexes
  - Iterative Antibody Optimization
  - Guided Sampling
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16357
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:35:07.387034",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Sequence-Structure Generative Model",
    "Antibody-Antigen Complexes",
    "Iterative Antibody Optimization",
    "Guided Sampling"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Sequence-Structure Generative Model": 0.78,
    "Antibody-Antigen Complexes": 0.82,
    "Iterative Antibody Optimization": 0.75,
    "Guided Sampling": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "sequence-structure diffusion generative model",
        "canonical": "Sequence-Structure Generative Model",
        "aliases": [
          "diffusion generative model"
        ],
        "category": "unique_technical",
        "rationale": "This model is central to the paper's methodology and represents a novel approach combining sequence and structure data.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "antibody-antigen complexes",
        "canonical": "Antibody-Antigen Complexes",
        "aliases": [
          "antibody complexes"
        ],
        "category": "specific_connectable",
        "rationale": "Key biological entities in the study, crucial for understanding the optimization process described.",
        "novelty_score": 0.55,
        "connectivity_score": 0.79,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "iterative antibody optimization",
        "canonical": "Iterative Antibody Optimization",
        "aliases": [
          "antibody optimization"
        ],
        "category": "unique_technical",
        "rationale": "Describes the iterative process central to the paper's research focus.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      },
      {
        "surface": "guided sampling approach",
        "canonical": "Guided Sampling",
        "aliases": [
          "sampling approach"
        ],
        "category": "unique_technical",
        "rationale": "A novel technique introduced in the paper for optimizing antibody properties.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.76,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "therapeutic",
      "clinical development",
      "in vitro experiments"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "sequence-structure diffusion generative model",
      "resolved_canonical": "Sequence-Structure Generative Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "antibody-antigen complexes",
      "resolved_canonical": "Antibody-Antigen Complexes",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.79,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "iterative antibody optimization",
      "resolved_canonical": "Iterative Antibody Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "guided sampling approach",
      "resolved_canonical": "Guided Sampling",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.76,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Guided Sequence-Structure Generative Modeling for Iterative Antibody Optimization

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16357.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16357](https://arxiv.org/abs/2509.16357)

## 🔗 유사한 논문
- [[2025-09-18/Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery_20250918|Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery]] (81.6% similar)
- [[2025-09-23/$\texttt{DiffSyn}$_ A Generative Diffusion Approach to Materials Synthesis Planning_20250923|$\texttt{DiffSyn}$: A Generative Diffusion Approach to Materials Synthesis Planning]] (78.6% similar)
- [[2025-09-22/Monte Carlo Tree Diffusion with Multiple Experts for Protein Design_20250922|Monte Carlo Tree Diffusion with Multiple Experts for Protein Design]] (78.6% similar)
- [[2025-09-22/An Equivariant Graph Network for Interpretable Nanoporous Materials Design_20250922|An Equivariant Graph Network for Interpretable Nanoporous Materials Design]] (76.8% similar)
- [[2025-09-22/Rethinking Molecule Synthesizability with Chain-of-Reaction_20250922|Rethinking Molecule Synthesizability with Chain-of-Reaction]] (76.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Antibody-Antigen Complexes|Antibody-Antigen Complexes]]
**⚡ Unique Technical**: [[keywords/Sequence-Structure Generative Model|Sequence-Structure Generative Model]], [[keywords/Iterative Antibody Optimization|Iterative Antibody Optimization]], [[keywords/Guided Sampling|Guided Sampling]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16357v1 Announce Type: new 
Abstract: Therapeutic antibody candidates often require extensive engineering to improve key functional and developability properties before clinical development. This can be achieved through iterative design, where starting molecules are optimized over several rounds of in vitro experiments. While protein structure can provide a strong inductive bias, it is rarely used in iterative design due to the lack of structural data for continually evolving lead molecules over the course of optimization. In this work, we propose a strategy for iterative antibody optimization that leverages both sequence and structure as well as accumulating lab measurements of binding and developability. Building on prior work, we first train a sequence-structure diffusion generative model that operates on antibody-antigen complexes. We then outline an approach to use this model, together with carefully predicted antibody-antigen complexes, to optimize lead candidates throughout the iterative design process. Further, we describe a guided sampling approach that biases generation toward desirable properties by integrating models trained on experimental data from iterative design. We evaluate our approach in multiple in silico and in vitro experiments, demonstrating that it produces high-affinity binders at multiple stages of an active antibody optimization campaign.

## 📝 요약

이 논문은 치료용 항체 후보물질의 최적화를 위한 새로운 반복적 설계 전략을 제안합니다. 기존의 반복적 설계는 구조적 데이터의 부족으로 인해 단백질 구조를 잘 활용하지 못했으나, 본 연구는 항체-항원 복합체의 서열과 구조, 실험적 데이터를 활용한 모델을 개발했습니다. 이 모델은 항체-항원 복합체에 대한 서열-구조 확산 생성 모델을 기반으로 하며, 실험 데이터를 통합해 바람직한 특성을 갖춘 항체를 생성합니다. 여러 실험을 통해 이 접근법이 높은 친화력을 가진 결합체를 효과적으로 생성함을 입증했습니다.

## 🎯 주요 포인트

- 1. 치료용 항체 후보물질은 임상 개발 전에 기능적 및 개발 가능성의 주요 특성을 개선하기 위해 광범위한 엔지니어링이 필요하다.
- 2. 본 연구에서는 항체-항원 복합체에 작용하는 시퀀스-구조 확산 생성 모델을 활용하여 항체 최적화를 위한 전략을 제안한다.
- 3. 실험 데이터를 기반으로 훈련된 모델을 통합하여 바람직한 특성으로 생성 편향을 유도하는 가이드 샘플링 접근법을 설명한다.
- 4. 제안된 방법은 여러 단계의 항체 최적화 캠페인에서 높은 친화력의 결합체를 생성함을 입증하였다.


---

*Generated on 2025-09-24 01:35:07*