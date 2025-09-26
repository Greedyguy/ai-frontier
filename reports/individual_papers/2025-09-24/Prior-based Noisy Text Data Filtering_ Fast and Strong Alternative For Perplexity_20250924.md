<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:40:26.536052",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Prior-based Data Filtering",
    "Perplexity-based Filtering",
    "Multilingual Corpora"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Prior-based Data Filtering": 0.7,
    "Perplexity-based Filtering": 0.75,
    "Multilingual Corpora": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "This is a foundational concept in NLP, connecting to numerous related topics.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Prior-based Data Filtering",
        "canonical": "Prior-based Data Filtering",
        "aliases": [
          "Token Priors Filtering"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel method for data filtering, relevant for efficient model training.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Perplexity-based Filtering",
        "canonical": "Perplexity-based Filtering",
        "aliases": [
          "PPL Filtering"
        ],
        "category": "specific_connectable",
        "rationale": "A well-known technique in NLP, providing a point of comparison for the proposed method.",
        "novelty_score": 0.4,
        "connectivity_score": 0.7,
        "specificity_score": 0.65,
        "link_intent_score": 0.75
      },
      {
        "surface": "Multilingual Corpora",
        "canonical": "Multilingual Corpora",
        "aliases": [
          "Multilingual Datasets"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the adaptability of the method across different languages, relevant for global applications.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "data"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Prior-based Data Filtering",
      "resolved_canonical": "Prior-based Data Filtering",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Perplexity-based Filtering",
      "resolved_canonical": "Perplexity-based Filtering",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.7,
        "specificity": 0.65,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Multilingual Corpora",
      "resolved_canonical": "Multilingual Corpora",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Prior-based Noisy Text Data Filtering: Fast and Strong Alternative For Perplexity

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18577.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2509.18577](https://arxiv.org/abs/2509.18577)

## 🔗 유사한 논문
- [[2025-09-23/DeepInsert_ Early Layer Bypass for Efficient and Performant Multimodal Understanding_20250923|DeepInsert: Early Layer Bypass for Efficient and Performant Multimodal Understanding]] (83.6% similar)
- [[2025-09-23/PDTrim_ Targeted Pruning for Prefill-Decode Disaggregation in Inference_20250923|PDTrim: Targeted Pruning for Prefill-Decode Disaggregation in Inference]] (83.1% similar)
- [[2025-09-23/LASER_ Stratified Selective Sampling for Instruction Tuning with Dedicated Scoring Strategy_20250923|LASER: Stratified Selective Sampling for Instruction Tuning with Dedicated Scoring Strategy]] (83.0% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (82.7% similar)
- [[2025-09-24/Reinforcement Learning on Pre-Training Data_20250924|Reinforcement Learning on Pre-Training Data]] (82.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Perplexity-based Filtering|Perplexity-based Filtering]], [[keywords/Multilingual Corpora|Multilingual Corpora]]
**⚡ Unique Technical**: [[keywords/Prior-based Data Filtering|Prior-based Data Filtering]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18577v1 Announce Type: new 
Abstract: As large language models (LLMs) are pretrained on massive web corpora, careful selection of data becomes essential to ensure effective and efficient learning. While perplexity (PPL)-based filtering has shown strong performance, it suffers from drawbacks: substantial time costs and inherent unreliability of the model when handling noisy or out-of-distribution samples. In this work, we propose a simple yet powerful alternative: a prior-based data filtering method that estimates token priors using corpus-level term frequency statistics, inspired by linguistic insights on word roles and lexical density. Our approach filters documents based on the mean and standard deviation of token priors, serving as a fast proxy to PPL while requiring no model inference. Despite its simplicity, the prior-based filter achieves the highest average performance across 20 downstream benchmarks, while reducing time cost by over 1000x compared to PPL-based filtering. We further demonstrate its applicability to symbolic languages such as code and math, and its dynamic adaptability to multilingual corpora without supervision

## 📝 요약

이 연구는 대규모 언어 모델(LLM)의 학습을 위한 데이터 선택의 중요성을 강조하며, 기존의 당혹도(PPL) 기반 필터링의 시간 소모와 신뢰성 문제를 해결하기 위해 새로운 방법을 제안합니다. 제안된 방법은 코퍼스 수준의 용어 빈도 통계를 활용하여 토큰의 사전 확률을 추정하는 필터링 기법으로, 모델 추론 없이도 빠르게 수행됩니다. 이 방법은 20개의 다운스트림 벤치마크에서 최고 성능을 보였으며, PPL 기반 필터링에 비해 시간 비용을 1000배 이상 절감했습니다. 또한, 코드와 수학 같은 상징적 언어와 다국어 코퍼스에도 유연하게 적용 가능합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 효과적 학습을 위해 데이터 선택이 중요하며, 기존의 PPL 기반 필터링은 시간 소모와 신뢰성 문제를 가진다.
- 2. 본 연구에서는 코퍼스 수준의 용어 빈도 통계를 활용한 사전 기반 데이터 필터링 방법을 제안하며, 이는 PPL의 빠른 대안이 된다.
- 3. 제안된 사전 기반 필터는 모델 추론이 필요 없으며, 20개의 다운스트림 벤치마크에서 최고 평균 성능을 달성하고 시간 비용을 1000배 이상 절감한다.
- 4. 이 방법은 코드 및 수학과 같은 상징적 언어에도 적용 가능하며, 감독 없이 다국어 코퍼스에 동적으로 적응할 수 있다.


---

*Generated on 2025-09-24 15:40:26*