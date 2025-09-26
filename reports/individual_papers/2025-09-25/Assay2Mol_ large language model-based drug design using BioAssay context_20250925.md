---
keywords:
  - Assay2Mol
  - Large Language Model
  - Few-Shot Learning
  - Biochemical Screening Assays
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2507.12574
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:31:39.651155",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Assay2Mol",
    "Large Language Model",
    "Few-Shot Learning",
    "Biochemical Screening Assays"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Assay2Mol": 0.8,
    "Large Language Model": 0.9,
    "Few-Shot Learning": 0.85,
    "Biochemical Screening Assays": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Assay2Mol",
        "canonical": "Assay2Mol",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Assay2Mol is a novel workflow specifically designed for drug discovery using biochemical assays, making it a unique technical term.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the workflow described and connect to a broad range of AI research topics.",
        "novelty_score": 0.3,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.9
      },
      {
        "surface": "In-context Learning",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "In-context Learning"
        ],
        "category": "specific_connectable",
        "rationale": "In-context learning is closely related to Few-Shot Learning, which is a trending concept in AI for learning with minimal data.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.85
      },
      {
        "surface": "Biochemical Screening Assays",
        "canonical": "Biochemical Screening Assays",
        "aliases": [
          "Molecule Screening Assays"
        ],
        "category": "unique_technical",
        "rationale": "Biochemical Screening Assays are crucial for drug discovery and provide a specific context for the paper's methodology.",
        "novelty_score": 0.7,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "drug design",
      "disease targets",
      "experimental screening protocols"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Assay2Mol",
      "resolved_canonical": "Assay2Mol",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "In-context Learning",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Biochemical Screening Assays",
      "resolved_canonical": "Biochemical Screening Assays",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Assay2Mol: large language model-based drug design using BioAssay context

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2507.12574.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2507.12574](https://arxiv.org/abs/2507.12574)

## 🔗 유사한 논문
- [[2025-09-23/Test-Time Training Scaling Laws for Chemical Exploration in Drug Design_20250923|Test-Time Training Scaling Laws for Chemical Exploration in Drug Design]] (83.4% similar)
- [[2025-09-22/MolParser_ End-to-end Visual Recognition of Molecule Structures in the Wild_20250922|MolParser: End-to-end Visual Recognition of Molecule Structures in the Wild]] (82.3% similar)
- [[2025-09-19/MOLE_ Metadata Extraction and Validation in Scientific Papers Using LLMs_20250919|MOLE: Metadata Extraction and Validation in Scientific Papers Using LLMs]] (81.5% similar)
- [[2025-09-18/Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery_20250918|Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery]] (80.9% similar)
- [[2025-09-24/MolPILE - large-scale, diverse dataset for molecular representation learning_20250924|MolPILE - large-scale, diverse dataset for molecular representation learning]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Assay2Mol|Assay2Mol]], [[keywords/Biochemical Screening Assays|Biochemical Screening Assays]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.12574v2 Announce Type: replace-cross 
Abstract: Scientific databases aggregate vast amounts of quantitative data alongside descriptive text. In biochemistry, molecule screening assays evaluate candidate molecules' functional responses against disease targets. Unstructured text that describes the biological mechanisms through which these targets operate, experimental screening protocols, and other attributes of assays offer rich information for drug discovery campaigns but has been untapped because of that unstructured format. We present Assay2Mol, a large language model-based workflow that can capitalize on the vast existing biochemical screening assays for early-stage drug discovery. Assay2Mol retrieves existing assay records involving targets similar to the new target and generates candidate molecules using in-context learning with the retrieved assay screening data. Assay2Mol outperforms recent machine learning approaches that generate candidate ligand molecules for target protein structures, while also promoting more synthesizable molecule generation.

## 📝 요약

Assay2Mol은 생화학 스크리닝 실험 데이터를 활용하여 초기 단계의 약물 발견을 지원하는 대형 언어 모델 기반 워크플로우입니다. 이 모델은 새로운 표적과 유사한 기존 실험 기록을 검색하고, 검색된 데이터를 바탕으로 후보 분자를 생성합니다. Assay2Mol은 기존의 기계 학습 방법보다 더 우수한 성능을 보이며, 합성 가능한 분자 생성도 촉진합니다. 이를 통해 비구조화된 텍스트가 포함된 방대한 과학 데이터베이스를 효과적으로 활용할 수 있습니다.

## 🎯 주요 포인트

- 1. Assay2Mol은 생화학적 스크리닝 어세이를 활용하여 초기 단계의 약물 발견을 지원하는 대형 언어 모델 기반 워크플로우입니다.
- 2. 이 모델은 새로운 타겟과 유사한 기존 어세이 기록을 검색하고, 검색된 어세이 데이터를 활용하여 후보 분자를 생성합니다.
- 3. Assay2Mol은 타겟 단백질 구조에 대한 후보 리간드 분자를 생성하는 최근의 기계 학습 접근법보다 우수한 성능을 보입니다.
- 4. 이 모델은 더 합성 가능한 분자의 생성을 촉진합니다.
- 5. 비구조화된 텍스트에서 풍부한 정보를 추출하여 약물 발견 캠페인에 활용할 수 있습니다.


---

*Generated on 2025-09-25 16:31:39*