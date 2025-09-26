<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:53:25.460222",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reverse-Complement Consistency Regularization",
    "DNA Language Model",
    "Transformer",
    "Sequence Classification"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Reverse-Complement Consistency Regularization": 0.88,
    "DNA Language Model": 0.82,
    "Transformer": 0.85,
    "Sequence Classification": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Reverse-Complement Consistency Regularization",
        "canonical": "Reverse-Complement Consistency Regularization",
        "aliases": [
          "RCCR"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and introduces a novel approach to improving DNA language model robustness.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "DNA language models",
        "canonical": "DNA Language Model",
        "aliases": [
          "DNA models"
        ],
        "category": "specific_connectable",
        "rationale": "This is a specific application of language models in genomics, connecting to broader machine learning concepts.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Nucleotide Transformer",
        "canonical": "Transformer",
        "aliases": [
          "Nucleotide Transformer"
        ],
        "category": "broad_technical",
        "rationale": "This is a specific instance of a Transformer model applied to nucleotide sequences, linking it to the broader Transformer category.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "sequence classification",
        "canonical": "Sequence Classification",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This task is a common application in bioinformatics, linking to various machine learning techniques.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "state-of-the-art",
      "model-agnostic"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Reverse-Complement Consistency Regularization",
      "resolved_canonical": "Reverse-Complement Consistency Regularization",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "DNA language models",
      "resolved_canonical": "DNA Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Nucleotide Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "sequence classification",
      "resolved_canonical": "Sequence Classification",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Reverse-Complement Consistency for DNA Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18529.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18529](https://arxiv.org/abs/2509.18529)

## 🔗 유사한 논문
- [[2025-09-24/nDNA -- the Semantic Helix of Artificial Cognition_20250924|nDNA -- the Semantic Helix of Artificial Cognition]] (81.9% similar)
- [[2025-09-24/Explicit Path CGR_ Maintaining Sequence Fidelity in Geometric Representations_20250924|Explicit Path CGR: Maintaining Sequence Fidelity in Geometric Representations]] (80.9% similar)
- [[2025-09-23/DCR_ Quantifying Data Contamination in LLMs Evaluation_20250923|DCR: Quantifying Data Contamination in LLMs Evaluation]] (80.1% similar)
- [[2025-09-22/DNA-DetectLLM_ Unveiling AI-Generated Text via a DNA-Inspired Mutation-Repair Paradigm_20250922|DNA-DetectLLM: Unveiling AI-Generated Text via a DNA-Inspired Mutation-Repair Paradigm]] (79.9% similar)
- [[2025-09-24/Biology-Instructions_ A Dataset and Benchmark for Multi-Omics Sequence Understanding Capability of Large Language Models_20250924|Biology-Instructions: A Dataset and Benchmark for Multi-Omics Sequence Understanding Capability of Large Language Models]] (78.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/DNA Language Model|DNA Language Model]], [[keywords/Sequence Classification|Sequence Classification]]
**⚡ Unique Technical**: [[keywords/Reverse-Complement Consistency Regularization|Reverse-Complement Consistency Regularization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18529v1 Announce Type: new 
Abstract: A fundamental property of DNA is that the reverse complement (RC) of a sequence often carries identical biological meaning. However, state-of-the-art DNA language models frequently fail to capture this symmetry, producing inconsistent predictions for a sequence and its RC counterpart, which undermines their reliability. In this work, we introduce Reverse-Complement Consistency Regularization (RCCR), a simple and model-agnostic fine-tuning objective that directly penalizes the divergence between a model's prediction on a sequence and the aligned prediction on its reverse complement. We evaluate RCCR across three diverse backbones (Nucleotide Transformer, HyenaDNA, DNABERT-2) on a wide range of genomic tasks, including sequence classification, scalar regression, and profile prediction. Our experiments show that RCCR substantially improves RC robustness by dramatically reducing prediction flips and errors, all while maintaining or improving task accuracy compared to baselines such as RC data augmentation and test-time averaging. By integrating a key biological prior directly into the learning process, RCCR produces a single, intrinsically robust, and computationally efficient model fine-tuning recipe for diverse biology tasks.

## 📝 요약

이 연구는 DNA 서열의 역상보성(RC) 특성을 효과적으로 반영하지 못하는 기존 DNA 언어 모델의 문제를 해결하기 위해, 역상보성 일관성 정규화(RCCR)를 제안합니다. RCCR은 모델의 예측과 그 역상보성 서열의 예측 간의 차이를 줄이는 간단한 미세 조정 기법입니다. Nucleotide Transformer, HyenaDNA, DNABERT-2 등 다양한 모델에 RCCR을 적용하여 서열 분류, 스칼라 회귀, 프로파일 예측 등의 유전체 과제에서 성능을 평가한 결과, RCCR은 예측 오류를 줄이고, 기존 기법보다 높은 정확도를 유지하거나 개선했습니다. 이는 생물학적 사전 지식을 학습 과정에 직접 통합하여 다양한 생물학적 과제에 강력하고 효율적인 모델을 제공합니다.

## 🎯 주요 포인트

- 1. DNA 서열의 역상보 서열(RC)은 동일한 생물학적 의미를 지니지만, 최신 DNA 언어 모델은 이 대칭성을 잘 포착하지 못하는 경우가 많습니다.
- 2. 역상보 일관성 정규화(RCCR)는 모델의 예측과 역상보 서열에 대한 예측 간의 차이를 줄이는 간단하고 모델에 구애받지 않는 미세 조정 목표입니다.
- 3. RCCR은 다양한 유전체 작업에서 예측 오류를 줄이고, 기존 기법과 비교하여 작업 정확도를 유지하거나 개선합니다.
- 4. RCCR은 생물학적 사전 지식을 학습 과정에 직접 통합하여 다양한 생물학 작업에 대해 본질적으로 강력하고 효율적인 모델 미세 조정 방법을 제공합니다.


---

*Generated on 2025-09-24 14:53:25*