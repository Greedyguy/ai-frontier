---
keywords:
  - Lakh MIDI Dataset
  - Symbolic Music Domain
  - Contrastive Learning BERT Model
  - Deep Learning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16662
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:30:32.457812",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Lakh MIDI Dataset",
    "Symbolic Music Domain",
    "Contrastive Learning BERT Model",
    "Deep Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Lakh MIDI Dataset": 0.8,
    "Symbolic Music Domain": 0.75,
    "Contrastive Learning BERT Model": 0.77,
    "Deep Learning": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Lakh MIDI Dataset",
        "canonical": "Lakh MIDI Dataset",
        "aliases": [
          "LMD"
        ],
        "category": "unique_technical",
        "rationale": "The Lakh MIDI Dataset is a specific dataset central to the study, offering unique connectivity within the symbolic music domain.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "symbolic music domain",
        "canonical": "Symbolic Music Domain",
        "aliases": [
          "symbolic music"
        ],
        "category": "unique_technical",
        "rationale": "This domain is crucial for understanding the context of the dataset and related research, providing a specific area for linking.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "contrastive learning-based BERT model",
        "canonical": "Contrastive Learning BERT Model",
        "aliases": [
          "BERT with contrastive learning"
        ],
        "category": "specific_connectable",
        "rationale": "This model represents a specific technique used in the study, relevant for linking to machine learning and NLP discussions.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "deep-learning model",
        "canonical": "Deep Learning",
        "aliases": [
          "deep learning models"
        ],
        "category": "broad_technical",
        "rationale": "Deep learning is a foundational concept in the study, connecting to broader discussions in machine learning.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "dataset duplication",
      "retrieval method",
      "benchmark test set"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Lakh MIDI Dataset",
      "resolved_canonical": "Lakh MIDI Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "symbolic music domain",
      "resolved_canonical": "Symbolic Music Domain",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "contrastive learning-based BERT model",
      "resolved_canonical": "Contrastive Learning BERT Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "deep-learning model",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# On the de-duplication of the Lakh MIDI dataset

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16662.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16662](https://arxiv.org/abs/2509.16662)

## 🔗 유사한 논문
- [[2025-09-19/Music4All A+A_ A Multimodal Dataset for Music Information Retrieval Tasks_20250919|Music4All A+A: A Multimodal Dataset for Music Information Retrieval Tasks]] (80.6% similar)
- [[2025-09-22/Optimizing Product Deduplication in E-Commerce with Multimodal Embeddings_20250922|Optimizing Product Deduplication in E-Commerce with Multimodal Embeddings]] (80.5% similar)
- [[2025-09-18/Reveal and Release_ Iterative LLM Unlearning with Self-generated Data_20250918|Reveal and Release: Iterative LLM Unlearning with Self-generated Data]] (79.2% similar)
- [[2025-09-22/Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data_20250922|Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data]] (79.0% similar)
- [[2025-09-22/Benchmarking Debiasing Methods for LLM-based Parameter Estimates_20250922|Benchmarking Debiasing Methods for LLM-based Parameter Estimates]] (78.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Contrastive Learning BERT Model|Contrastive Learning BERT Model]]
**⚡ Unique Technical**: [[keywords/Lakh MIDI Dataset|Lakh MIDI Dataset]], [[keywords/Symbolic Music Domain|Symbolic Music Domain]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16662v1 Announce Type: cross 
Abstract: A large-scale dataset is essential for training a well-generalized deep-learning model. Most such datasets are collected via scraping from various internet sources, inevitably introducing duplicated data. In the symbolic music domain, these duplicates often come from multiple user arrangements and metadata changes after simple editing. However, despite critical issues such as unreliable training evaluation from data leakage during random splitting, dataset duplication has not been extensively addressed in the MIR community. This study investigates the dataset duplication issues regarding Lakh MIDI Dataset (LMD), one of the largest publicly available sources in the symbolic music domain. To find and evaluate the best retrieval method for duplicated data, we employed the Clean MIDI subset of the LMD as a benchmark test set, in which different versions of the same songs are grouped together. We first evaluated rule-based approaches and previous symbolic music retrieval models for de-duplication and also investigated with a contrastive learning-based BERT model with various augmentations to find duplicate files. As a result, we propose three different versions of the filtered list of LMD, which filters out at least 38,134 samples in the most conservative settings among 178,561 files.

## 📝 요약

이 연구는 심볼릭 음악 분야에서 대규모 데이터셋의 중복 문제를 조사합니다. 특히 Lakh MIDI Dataset(LMD)의 중복 데이터를 식별하고 평가하기 위해 Clean MIDI 하위 집합을 벤치마크 테스트 세트로 사용했습니다. 규칙 기반 접근법과 기존의 심볼릭 음악 검색 모델을 평가했으며, 대조 학습 기반 BERT 모델을 다양한 증강 기법과 함께 사용하여 중복 파일을 찾았습니다. 그 결과, 178,561개의 파일 중 최소 38,134개의 샘플을 걸러내는 세 가지 필터링된 LMD 목록을 제안합니다. 이 연구는 데이터셋 중복 문제를 해결하여 신뢰할 수 있는 모델 훈련과 평가를 돕는 데 기여합니다.

## 🎯 주요 포인트

- 1. 대규모 데이터셋은 잘 일반화된 딥러닝 모델을 훈련하는 데 필수적이며, 인터넷 소스에서 수집된 데이터셋은 중복 데이터를 포함할 수 있다.
- 2. 상징적 음악 도메인에서는 사용자 편곡과 메타데이터 변경으로 인해 중복 데이터가 발생할 수 있다.
- 3. Lakh MIDI Dataset (LMD)의 중복 문제를 조사하여 최적의 중복 데이터 검색 방법을 평가하였다.
- 4. 대조 학습 기반 BERT 모델과 다양한 증강 기법을 사용하여 중복 파일을 찾는 방법을 탐구하였다.
- 5. LMD에서 최소 38,134개의 샘플을 필터링한 세 가지 버전의 필터링 목록을 제안하였다.


---

*Generated on 2025-09-23 23:30:32*