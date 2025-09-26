---
keywords:
  - FragAtlas-62M
  - Fragment-Based Drug Discovery
  - ZINC Fragment Subset
  - Large Language Model
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19586
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:38:54.316012",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "FragAtlas-62M",
    "Fragment-Based Drug Discovery",
    "ZINC Fragment Subset",
    "Large Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "FragAtlas-62M": 0.8,
    "Fragment-Based Drug Discovery": 0.9,
    "ZINC Fragment Subset": 0.75,
    "Large Language Model": 0.85
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "FragAtlas-62M",
        "canonical": "FragAtlas-62M",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a unique model introduced in the paper, crucial for linking to specific research on fragment-based drug discovery.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "fragment-based drug discovery",
        "canonical": "Fragment-Based Drug Discovery",
        "aliases": [
          "FBDD"
        ],
        "category": "specific_connectable",
        "rationale": "This is a specific method in drug discovery that connects to a niche area of research.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.9
      },
      {
        "surface": "ZINC-22 fragment subset",
        "canonical": "ZINC Fragment Subset",
        "aliases": [
          "ZINC-22"
        ],
        "category": "unique_technical",
        "rationale": "This dataset is central to the study, linking to chemical databases and fragment research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "GPT-2 based model",
        "canonical": "Large Language Model",
        "aliases": [
          "GPT-2"
        ],
        "category": "broad_technical",
        "rationale": "GPT-2 is a well-known large language model, linking to broader AI and machine learning research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
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
      "candidate_surface": "FragAtlas-62M",
      "resolved_canonical": "FragAtlas-62M",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "fragment-based drug discovery",
      "resolved_canonical": "Fragment-Based Drug Discovery",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "ZINC-22 fragment subset",
      "resolved_canonical": "ZINC Fragment Subset",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "GPT-2 based model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    }
  ]
}
-->

# A Foundation Chemical Language Model for Comprehensive Fragment-Based Drug Discovery

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19586.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19586](https://arxiv.org/abs/2509.19586)

## 🔗 유사한 논문
- [[2025-09-24/FragmentGPT_ A Unified GPT Model for Fragment Growing, Linking, and Merging in Molecular Design_20250924|FragmentGPT: A Unified GPT Model for Fragment Growing, Linking, and Merging in Molecular Design]] (86.5% similar)
- [[2025-09-24/MolPILE - large-scale, diverse dataset for molecular representation learning_20250924|MolPILE - large-scale, diverse dataset for molecular representation learning]] (81.3% similar)
- [[2025-09-22/MolParser_ End-to-end Visual Recognition of Molecule Structures in the Wild_20250922|MolParser: End-to-end Visual Recognition of Molecule Structures in the Wild]] (80.3% similar)
- [[2025-09-24/Topological Feature Compression for Molecular Graph Neural Networks_20250924|Topological Feature Compression for Molecular Graph Neural Networks]] (80.1% similar)
- [[2025-09-22/ProFusion_ 3D Reconstruction of Protein Complex Structures from Multi-view AFM Images_20250922|ProFusion: 3D Reconstruction of Protein Complex Structures from Multi-view AFM Images]] (79.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Fragment-Based Drug Discovery|Fragment-Based Drug Discovery]]
**⚡ Unique Technical**: [[keywords/FragAtlas-62M|FragAtlas-62M]], [[keywords/ZINC Fragment Subset|ZINC Fragment Subset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19586v1 Announce Type: cross 
Abstract: We introduce FragAtlas-62M, a specialized foundation model trained on the largest fragment dataset to date. Built on the complete ZINC-22 fragment subset comprising over 62 million molecules, it achieves unprecedented coverage of fragment chemical space. Our GPT-2 based model (42.7M parameters) generates 99.90% chemically valid fragments. Validation across 12 descriptors and three fingerprint methods shows generated fragments closely match the training distribution (all effect sizes < 0.4). The model retains 53.6% of known ZINC fragments while producing 22% novel structures with practical relevance. We release FragAtlas-62M with training code, preprocessed data, documentation, and model weights to accelerate adoption.

## 📝 요약

FragAtlas-62M은 6,200만 개 이상의 분자로 구성된 ZINC-22 조각 데이터셋을 기반으로 한 특화된 모델로, 화학 조각 공간을 광범위하게 커버합니다. 4,270만 개의 매개변수를 가진 GPT-2 기반 모델로, 99.90%의 화학적으로 유효한 조각을 생성합니다. 12개의 기술 지표와 세 가지 지문 방법을 통해 검증한 결과, 생성된 조각이 훈련 분포와 매우 유사함을 확인했습니다. 모델은 ZINC 조각의 53.6%를 유지하면서도 22%의 새로운 구조를 생성했습니다. FragAtlas-62M은 훈련 코드, 전처리 데이터, 문서 및 모델 가중치와 함께 공개되어 연구의 가속화를 돕습니다.

## 🎯 주요 포인트

- 1. FragAtlas-62M은 6,200만 개 이상의 분자 데이터를 포함한 ZINC-22 조각 하위 집합을 기반으로 구축된 특화된 기초 모델입니다.
- 2. 이 모델은 화학적으로 유효한 조각을 99.90% 생성하며, 12개의 서술자와 세 가지 지문 방법을 통해 검증되었습니다.
- 3. 생성된 조각은 훈련 분포와 매우 유사하며, 효과 크기가 모두 0.4 미만입니다.
- 4. 모델은 알려진 ZINC 조각의 53.6%를 유지하면서 실질적으로 유용한 22%의 새로운 구조를 생성합니다.
- 5. FragAtlas-62M은 훈련 코드, 전처리된 데이터, 문서 및 모델 가중치와 함께 제공되어 채택을 가속화합니다.


---

*Generated on 2025-09-25 15:38:54*