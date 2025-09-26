---
keywords:
  - Discourse Relation Classification
  - Transformer
  - Qwen Model
  - Augmented Dataset
  - Low-Resource Languages
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.11498
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:13:34.190069",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Discourse Relation Classification",
    "Transformer",
    "Qwen Model",
    "Augmented Dataset",
    "Low-Resource Languages"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Discourse Relation Classification": 0.8,
    "Transformer": 0.85,
    "Qwen Model": 0.78,
    "Augmented Dataset": 0.7,
    "Low-Resource Languages": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "discourse relation classification",
        "canonical": "Discourse Relation Classification",
        "aliases": [
          "discourse relations",
          "relation classification"
        ],
        "category": "unique_technical",
        "rationale": "This is the primary focus of the paper and a unique technical term that can connect to related discourse analysis research.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "mt5-based encoder",
        "canonical": "Transformer",
        "aliases": [
          "mt5 encoder",
          "mt5"
        ],
        "category": "broad_technical",
        "rationale": "mt5 is a variant of the Transformer model, which is a fundamental concept in NLP.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Qwen model",
        "canonical": "Qwen Model",
        "aliases": [
          "Qwen"
        ],
        "category": "unique_technical",
        "rationale": "The Qwen model is a specific model used in the paper, potentially linking to other works using the same model.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "augmented dataset",
        "canonical": "Augmented Dataset",
        "aliases": [
          "data augmentation"
        ],
        "category": "specific_connectable",
        "rationale": "Augmented datasets are crucial for improving model performance, especially in low-resource settings.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      },
      {
        "surface": "low-resource languages",
        "canonical": "Low-Resource Languages",
        "aliases": [
          "resource-scarce languages"
        ],
        "category": "specific_connectable",
        "rationale": "This term connects to research focused on language processing for less commonly supported languages.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "system",
      "approach",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "discourse relation classification",
      "resolved_canonical": "Discourse Relation Classification",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "mt5-based encoder",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Qwen model",
      "resolved_canonical": "Qwen Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "augmented dataset",
      "resolved_canonical": "Augmented Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "low-resource languages",
      "resolved_canonical": "Low-Resource Languages",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# DeDisCo at the DISRPT 2025 Shared Task: A System for Discourse Relation Classification

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.11498.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.11498](https://arxiv.org/abs/2509.11498)

## 🔗 유사한 논문
- [[2025-09-23/CLaC at DISRPT 2025_ Hierarchical Adapters for Cross-Framework Multi-lingual Discourse Relation Classification_20250923|CLaC at DISRPT 2025: Hierarchical Adapters for Cross-Framework Multi-lingual Discourse Relation Classification]] (85.0% similar)
- [[2025-09-23/CorPipe at CRAC 2025_ Evaluating Multilingual Encoders for Multilingual Coreference Resolution_20250923|CorPipe at CRAC 2025: Evaluating Multilingual Encoders for Multilingual Coreference Resolution]] (79.6% similar)
- [[2025-09-23/Findings of the Fourth Shared Task on Multilingual Coreference Resolution_ Can LLMs Dethrone Traditional Approaches?_20250923|Findings of the Fourth Shared Task on Multilingual Coreference Resolution: Can LLMs Dethrone Traditional Approaches?]] (79.6% similar)
- [[2025-09-23/DiscoSG_ Towards Discourse-Level Text Scene Graph Parsing through Iterative Graph Refinement_20250923|DiscoSG: Towards Discourse-Level Text Scene Graph Parsing through Iterative Graph Refinement]] (79.4% similar)
- [[2025-09-23/AISTAT lab system for DCASE2025 Task6_ Language-based audio retrieval_20250923|AISTAT lab system for DCASE2025 Task6: Language-based audio retrieval]] (79.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Augmented Dataset|Augmented Dataset]], [[keywords/Low-Resource Languages|Low-Resource Languages]]
**⚡ Unique Technical**: [[keywords/Discourse Relation Classification|Discourse Relation Classification]], [[keywords/Qwen Model|Qwen Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.11498v4 Announce Type: replace 
Abstract: This paper presents DeDisCo, Georgetown University's entry in the DISRPT 2025 shared task on discourse relation classification. We test two approaches, using an mt5-based encoder and a decoder based approach using the openly available Qwen model. We also experiment on training with augmented dataset for low-resource languages using matched data translated automatically from English, as well as using some additional linguistic features inspired by entries in previous editions of the Shared Task. Our system achieves a macro-accuracy score of 71.28, and we provide some interpretation and error analysis for our results.

## 📝 요약

이 논문은 Georgetown University의 DISRPT 2025 담화 관계 분류 공유 과제 참가작인 DeDisCo를 소개합니다. mt5 기반 인코더와 Qwen 모델을 활용한 디코더 접근법을 테스트하였으며, 저자들은 데이터가 부족한 언어에 대해 영어에서 자동 번역된 데이터를 활용한 증강 데이터셋으로 학습을 시도했습니다. 또한, 이전 대회 참가작에서 영감을 얻은 추가적인 언어적 특징도 사용했습니다. 시스템은 71.28의 매크로 정확도를 달성했으며, 결과에 대한 해석과 오류 분석도 제공합니다.

## 🎯 주요 포인트

- 1. DeDisCo는 Georgetown University가 DISRPT 2025 담화 관계 분류 공유 과제에 제출한 시스템입니다.
- 2. 두 가지 접근법을 테스트했으며, mt5 기반 인코더와 공개된 Qwen 모델을 사용한 디코더 기반 접근법을 사용했습니다.
- 3. 저자들은 영어에서 자동 번역된 데이터를 사용하여 저자원 언어에 대한 증강 데이터셋으로 훈련을 시도했습니다.
- 4. 이전 공유 과제의 참가작에서 영감을 받은 추가적인 언어적 특징을 사용했습니다.
- 5. 시스템은 매크로 정확도 점수 71.28을 달성했으며, 결과에 대한 해석 및 오류 분석을 제공했습니다.


---

*Generated on 2025-09-24 04:13:34*