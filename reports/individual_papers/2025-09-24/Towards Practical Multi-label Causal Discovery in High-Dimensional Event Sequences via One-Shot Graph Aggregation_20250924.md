<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:12:28.996933",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "CARGO Method",
    "Transformer",
    "One-Shot Learning",
    "Adaptive Frequency Fusion"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "CARGO Method": 0.8,
    "Transformer": 0.85,
    "One-Shot Learning": 0.78,
    "Adaptive Frequency Fusion": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "CARGO",
        "canonical": "CARGO Method",
        "aliases": [
          "CARGO"
        ],
        "category": "unique_technical",
        "rationale": "CARGO is a novel method introduced in the paper, specifically designed for multi-label causal discovery in high-dimensional event sequences.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "causal Transformers",
        "canonical": "Transformer",
        "aliases": [
          "causal Transformer"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational model used in the method, linking to the broader technical category of machine learning models.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "one-shot causal graphs",
        "canonical": "One-Shot Learning",
        "aliases": [
          "one-shot causal graph"
        ],
        "category": "specific_connectable",
        "rationale": "The concept of one-shot learning is relevant to the method's approach to causal graph construction, enhancing connectivity with learning paradigms.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "adaptive frequency fusion",
        "canonical": "Adaptive Frequency Fusion",
        "aliases": [
          "frequency fusion"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique technique introduced for aggregating causal graphs, which is central to the method's novelty.",
        "novelty_score": 0.78,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "event sequences",
      "probabilistic reasoning",
      "Markov boundaries"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "CARGO",
      "resolved_canonical": "CARGO Method",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "causal Transformers",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "one-shot causal graphs",
      "resolved_canonical": "One-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "adaptive frequency fusion",
      "resolved_canonical": "Adaptive Frequency Fusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Towards Practical Multi-label Causal Discovery in High-Dimensional Event Sequences via One-Shot Graph Aggregation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19112.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.19112](https://arxiv.org/abs/2509.19112)

## 🔗 유사한 논문
- [[2025-09-19/Causal-Counterfactual RAG_ The Integration of Causal-Counterfactual Reasoning into RAG_20250919|Causal-Counterfactual RAG: The Integration of Causal-Counterfactual Reasoning into RAG]] (80.2% similar)
- [[2025-09-19/CausalPre_ Scalable and Effective Data Pre-processing for Causal Fairness_20250919|CausalPre: Scalable and Effective Data Pre-processing for Causal Fairness]] (79.9% similar)
- [[2025-09-23/A Multi-Level Benchmark for Causal Language Understanding in Social Media Discourse_20250923|A Multi-Level Benchmark for Causal Language Understanding in Social Media Discourse]] (79.7% similar)
- [[2025-09-23/MSGAT-GRU_ A Multi-Scale Graph Attention and Recurrent Model for Spatiotemporal Road Accident Prediction_20250923|MSGAT-GRU: A Multi-Scale Graph Attention and Recurrent Model for Spatiotemporal Road Accident Prediction]] (79.3% similar)
- [[2025-09-23/Revealing Multimodal Causality with Large Language Models_20250923|Revealing Multimodal Causality with Large Language Models]] (79.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/One-Shot Learning|One-Shot Learning]]
**⚡ Unique Technical**: [[keywords/CARGO Method|CARGO Method]], [[keywords/Adaptive Frequency Fusion|Adaptive Frequency Fusion]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19112v1 Announce Type: cross 
Abstract: Understanding causality in event sequences where outcome labels such as diseases or system failures arise from preceding events like symptoms or error codes is critical. Yet remains an unsolved challenge across domains like healthcare or vehicle diagnostics. We introduce CARGO, a scalable multi-label causal discovery method for sparse, high-dimensional event sequences comprising of thousands of unique event types. Using two pretrained causal Transformers as domain-specific foundation models for event sequences. CARGO infers in parallel, per sequence one-shot causal graphs and aggregates them using an adaptive frequency fusion to reconstruct the global Markov boundaries of labels. This two-stage approach enables efficient probabilistic reasoning at scale while bypassing the intractable cost of full-dataset conditional independence testing. Our results on a challenging real-world automotive fault prediction dataset with over 29,100 unique event types and 474 imbalanced labels demonstrate CARGO's ability to perform structured reasoning.

## 📝 요약

이 논문은 CARGO라는 새로운 방법론을 소개하여, 질병이나 시스템 오류와 같은 결과가 이전의 증상이나 오류 코드와 같은 사건에서 유래하는 인과 관계를 이해하는 문제를 다룹니다. CARGO는 수천 개의 고유한 이벤트 유형을 포함하는 희소하고 고차원적인 이벤트 시퀀스를 처리할 수 있는 확장 가능한 다중 레이블 인과 발견 방법입니다. 두 개의 사전 학습된 인과 변환기를 사용하여 각 시퀀스의 인과 그래프를 병렬로 추론하고, 적응형 빈도 융합을 통해 전역 마르코프 경계를 재구성합니다. 이 접근 방식은 전체 데이터셋의 조건부 독립성 테스트의 복잡한 비용을 피하면서 효율적인 확률적 추론을 가능하게 합니다. 실제 자동차 결함 예측 데이터셋을 통해 CARGO의 구조적 추론 능력을 입증했습니다.

## 🎯 주요 포인트

- 1. CARGO는 희소하고 고차원적인 이벤트 시퀀스에서 다중 레이블 인과 관계를 발견하는 확장 가능한 방법입니다.
- 2. 두 개의 사전 학습된 인과적 트랜스포머를 사용하여 도메인별 기초 모델로 활용합니다.
- 3. CARGO는 각 시퀀스에 대해 병렬로 일회성 인과 그래프를 추론하고, 적응형 빈도 융합을 통해 전역 마르코프 경계를 재구성합니다.
- 4. 이 접근 방식은 전체 데이터셋의 조건부 독립성 테스트의 복잡한 비용을 피하면서 효율적인 확률적 추론을 가능하게 합니다.
- 5. 실제 자동차 결함 예측 데이터셋에서 CARGO는 구조적 추론을 수행할 수 있는 능력을 입증했습니다.


---

*Generated on 2025-09-24 14:12:28*