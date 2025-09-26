<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:49:59.085817",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Molecular Representation Learning",
    "MolPILE Dataset",
    "Foundation Models",
    "ImageNet-like Dataset"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Molecular Representation Learning": 0.88,
    "MolPILE Dataset": 0.92,
    "Foundation Models": 0.8,
    "ImageNet-like Dataset": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "molecular representation learning",
        "canonical": "Molecular Representation Learning",
        "aliases": [
          "molecular embeddings",
          "chemical representation learning"
        ],
        "category": "specific_connectable",
        "rationale": "This term is central to the paper's focus and connects to ongoing research in chemoinformatics and machine learning.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "MolPILE",
        "canonical": "MolPILE Dataset",
        "aliases": [
          "MolPILE collection",
          "MolPILE database"
        ],
        "category": "unique_technical",
        "rationale": "MolPILE is a newly introduced dataset in the paper, essential for understanding its contribution to the field.",
        "novelty_score": 0.9,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.92
      },
      {
        "surface": "foundation models",
        "canonical": "Foundation Models",
        "aliases": [
          "base models",
          "pretrained models"
        ],
        "category": "broad_technical",
        "rationale": "Foundation models are a key concept in machine learning, relevant to the dataset's application.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "ImageNet-like dataset",
        "canonical": "ImageNet-like Dataset",
        "aliases": [
          "benchmark dataset",
          "large-scale dataset"
        ],
        "category": "evolved_concepts",
        "rationale": "This term draws a parallel to a well-known concept in machine learning, enhancing understanding of the dataset's significance.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "pretraining datasets",
      "generalization performance",
      "automated curation pipeline"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "molecular representation learning",
      "resolved_canonical": "Molecular Representation Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "MolPILE",
      "resolved_canonical": "MolPILE Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.92
      }
    },
    {
      "candidate_surface": "foundation models",
      "resolved_canonical": "Foundation Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "ImageNet-like dataset",
      "resolved_canonical": "ImageNet-like Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# MolPILE - large-scale, diverse dataset for molecular representation learning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18353.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18353](https://arxiv.org/abs/2509.18353)

## 🔗 유사한 논문
- [[2025-09-22/MolParser_ End-to-end Visual Recognition of Molecule Structures in the Wild_20250922|MolParser: End-to-end Visual Recognition of Molecule Structures in the Wild]] (86.1% similar)
- [[2025-09-19/MOLE_ Metadata Extraction and Validation in Scientific Papers Using LLMs_20250919|MOLE: Metadata Extraction and Validation in Scientific Papers Using LLMs]] (79.7% similar)
- [[2025-09-23/Test-Time Training Scaling Laws for Chemical Exploration in Drug Design_20250923|Test-Time Training Scaling Laws for Chemical Exploration in Drug Design]] (79.2% similar)
- [[2025-09-24/From Parameters to Performance_ A Data-Driven Study on LLM Structure and Development_20250924|From Parameters to Performance: A Data-Driven Study on LLM Structure and Development]] (79.0% similar)
- [[2025-09-23/ChemOrch_ Empowering LLMs with Chemical Intelligence via Synthetic Instructions_20250923|ChemOrch: Empowering LLMs with Chemical Intelligence via Synthetic Instructions]] (78.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Foundation Models|Foundation Models]]
**🔗 Specific Connectable**: [[keywords/Molecular Representation Learning|Molecular Representation Learning]]
**⚡ Unique Technical**: [[keywords/MolPILE Dataset|MolPILE Dataset]]
**🚀 Evolved Concepts**: [[keywords/ImageNet-like Dataset|ImageNet-like Dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18353v1 Announce Type: new 
Abstract: The size, diversity, and quality of pretraining datasets critically determine the generalization ability of foundation models. Despite their growing importance in chemoinformatics, the effectiveness of molecular representation learning has been hindered by limitations in existing small molecule datasets. To address this gap, we present MolPILE, large-scale, diverse, and rigorously curated collection of 222 million compounds, constructed from 6 large-scale databases using an automated curation pipeline. We present a comprehensive analysis of current pretraining datasets, highlighting considerable shortcomings for training ML models, and demonstrate how retraining existing models on MolPILE yields improvements in generalization performance. This work provides a standardized resource for model training, addressing the pressing need for an ImageNet-like dataset in molecular chemistry.

## 📝 요약

MolPILE은 2억 2,200만 개의 화합물로 구성된 대규모, 다양하고 엄격하게 큐레이션된 분자 데이터셋으로, 기존 소분자 데이터셋의 한계를 극복하고자 개발되었습니다. 이 연구는 현재의 사전 학습 데이터셋의 한계를 분석하고, MolPILE을 활용한 모델 재학습이 일반화 성능을 향상시킴을 입증했습니다. 이를 통해 분자 화학 분야에서 ImageNet과 같은 표준화된 자원을 제공하여 모델 훈련의 효과를 높이고자 합니다.

## 🎯 주요 포인트

- 1. MolPILE은 2억 2천 2백만 개의 화합물로 구성된 대규모, 다양하고 엄격하게 선별된 데이터셋입니다.
- 2. 기존의 소분자 데이터셋의 한계를 극복하기 위해 MolPILE은 6개의 대규모 데이터베이스에서 자동화된 큐레이션 파이프라인을 통해 구축되었습니다.
- 3. MolPILE을 활용한 모델 재훈련은 일반화 성능의 개선을 보여줍니다.
- 4. 이 연구는 분자 화학 분야에서 ImageNet과 같은 표준화된 모델 훈련 자원을 제공합니다.
- 5. 현재의 사전 훈련 데이터셋 분석을 통해 ML 모델 훈련의 상당한 단점을 강조합니다.


---

*Generated on 2025-09-24 14:49:59*