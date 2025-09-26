---
keywords:
  - State Space Models
  - Code Understanding
  - Transformer
  - Sample Efficiency
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2505.01475
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:56:50.411597",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "State Space Models",
    "Code Understanding",
    "Transformer",
    "Sample Efficiency"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "State Space Models": 0.85,
    "Code Understanding": 0.8,
    "Transformer": 0.75,
    "Sample Efficiency": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "State Space Models",
        "canonical": "State Space Models",
        "aliases": [
          "SSM",
          "State Space Model"
        ],
        "category": "unique_technical",
        "rationale": "State Space Models offer a novel approach distinct from transformers, providing a new perspective in code understanding.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Code Understanding",
        "canonical": "Code Understanding",
        "aliases": [
          "Code Comprehension",
          "Code Analysis"
        ],
        "category": "specific_connectable",
        "rationale": "Code Understanding is central to the paper's focus, linking it to broader themes in software engineering.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Transformers are a well-established baseline in code tasks, providing a point of comparison for the proposed model.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      },
      {
        "surface": "Sample Efficiency",
        "canonical": "Sample Efficiency",
        "aliases": [
          "Data Efficiency"
        ],
        "category": "specific_connectable",
        "rationale": "Sample Efficiency is a key advantage of the proposed model, relevant to discussions on model training.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "retrieval",
      "classification",
      "clone detection"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "State Space Models",
      "resolved_canonical": "State Space Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Code Understanding",
      "resolved_canonical": "Code Understanding",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.7,
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
        "specificity": 0.6,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Sample Efficiency",
      "resolved_canonical": "Sample Efficiency",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# CodeSSM: Towards State Space Models for Code Understanding

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.01475.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2505.01475](https://arxiv.org/abs/2505.01475)

## 🔗 유사한 논문
- [[2025-09-22/Merging Memory and Space_ A State Space Neural Operator_20250922|Merging Memory and Space: A State Space Neural Operator]] (80.4% similar)
- [[2025-09-19/From Correction to Mastery_ Reinforced Distillation of Large Language Model Agents_20250919|From Correction to Mastery: Reinforced Distillation of Large Language Model Agents]] (79.6% similar)
- [[2025-09-17/State Space Models over Directed Graphs_20250917|State Space Models over Directed Graphs]] (79.5% similar)
- [[2025-09-19/Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models_20250919|Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models]] (79.2% similar)
- [[2025-09-19/Transcoder-based Circuit Analysis for Interpretable Single-Cell Foundation Models_20250919|Transcoder-based Circuit Analysis for Interpretable Single-Cell Foundation Models]] (79.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Code Understanding|Code Understanding]], [[keywords/Sample Efficiency|Sample Efficiency]]
**⚡ Unique Technical**: [[keywords/State Space Models|State Space Models]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.01475v3 Announce Type: replace-cross 
Abstract: Although transformers dominate many code-specific tasks, they have significant limitations. This paper explores State Space Models (SSMs) as a promising alternative for code understanding tasks such as retrieval, classification, and clone detection. We introduce CodeSSM, the first SSM-based model trained on code corpora to assess its effectiveness. Our results demonstrate that SSMs are more sample-efficient and can extrapolate to longer contexts beyond the pretraining length. Extensive experiments show that SSMs offer a viable alternative to transformers, addressing several their limitations. Additionally, CodeSSM reduces memory usage by up to 64\% compared to transformers at a context length of 2048, with greater savings as context length grows.

## 📝 요약

이 논문은 코드 이해 작업에서 트랜스포머의 한계를 극복하기 위해 상태 공간 모델(SSM)을 대안으로 탐구합니다. 코드 코퍼스에 기반한 최초의 SSM 모델인 CodeSSM을 소개하며, 이 모델이 코드 검색, 분류, 클론 탐지 작업에서 효과적임을 입증합니다. 연구 결과, SSM은 샘플 효율성이 높고 사전 학습 길이를 넘어서는 긴 문맥에서도 잘 작동함을 보여줍니다. 또한, CodeSSM은 문맥 길이가 2048일 때 트랜스포머 대비 최대 64%의 메모리 사용량을 줄이며, 문맥 길이가 길어질수록 더 큰 메모리 절감을 제공합니다.

## 🎯 주요 포인트

- 1. 본 논문은 코드 이해 작업에서 변환기(transformer)의 한계를 극복할 수 있는 대안으로 상태 공간 모델(SSM)을 탐구합니다.
- 2. CodeSSM은 코드 코퍼스에서 훈련된 최초의 SSM 기반 모델로, 코드 검색, 분류, 클론 탐지 등의 작업에서 효과를 평가합니다.
- 3. SSM은 샘플 효율성이 높고, 사전 훈련 길이를 넘어서는 긴 문맥으로의 외삽이 가능합니다.
- 4. CodeSSM은 변환기와 비교하여 문맥 길이 2048에서 최대 64%의 메모리 사용량을 줄이며, 문맥 길이가 길어질수록 더 큰 절감 효과를 보입니다.
- 5. 광범위한 실험 결과, SSM은 변환기의 여러 한계를 해결하며 실질적인 대안을 제공합니다.


---

*Generated on 2025-09-24 00:56:50*