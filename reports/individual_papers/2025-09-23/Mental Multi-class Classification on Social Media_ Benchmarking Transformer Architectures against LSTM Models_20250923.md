---
keywords:
  - Transformer
  - LSTM
  - Mental Health Detection
  - Attention Mechanism
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16542
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:10:18.699291",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "LSTM",
    "Mental Health Detection",
    "Attention Mechanism"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.88,
    "LSTM": 0.82,
    "Mental Health Detection": 0.78,
    "Attention Mechanism": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer architectures",
        "canonical": "Transformer",
        "aliases": [
          "Transformers"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a fundamental model architecture in NLP, crucial for linking with other deep learning concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.95,
        "specificity_score": 0.65,
        "link_intent_score": 0.88
      },
      {
        "surface": "Long Short-Term Memory",
        "canonical": "LSTM",
        "aliases": [
          "Long Short-Term Memory",
          "LSTMs"
        ],
        "category": "specific_connectable",
        "rationale": "LSTMs are a key architecture for time series and sequence data, offering strong connectivity with historical NLP models.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "mental health detection",
        "canonical": "Mental Health Detection",
        "aliases": [
          "mental health classification",
          "mental health identification"
        ],
        "category": "unique_technical",
        "rationale": "This is a specialized application area within NLP, linking mental health and AI research.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "attention-augmented LSTMs",
        "canonical": "Attention Mechanism",
        "aliases": [
          "attention-based LSTMs"
        ],
        "category": "specific_connectable",
        "rationale": "Combining attention mechanisms with LSTMs enhances model performance, linking to advanced neural network techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.87,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "social media",
      "dataset",
      "experimental results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Transformer architectures",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.95,
        "specificity": 0.65,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Long Short-Term Memory",
      "resolved_canonical": "LSTM",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "mental health detection",
      "resolved_canonical": "Mental Health Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "attention-augmented LSTMs",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.87,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Mental Multi-class Classification on Social Media: Benchmarking Transformer Architectures against LSTM Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16542.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16542](https://arxiv.org/abs/2509.16542)

## 🔗 유사한 논문
- [[2025-09-23/Multi-View Attention Multiple-Instance Learning Enhanced by LLM Reasoning for Cognitive Distortion Detection_20250923|Multi-View Attention Multiple-Instance Learning Enhanced by LLM Reasoning for Cognitive Distortion Detection]] (83.0% similar)
- [[2025-09-23/ReDepress_ A Cognitive Framework for Detecting Depression Relapse from Social Media_20250923|ReDepress: A Cognitive Framework for Detecting Depression Relapse from Social Media]] (82.4% similar)
- [[2025-09-18/A Comparative Analysis of Transformer Models in Social Bot Detection_20250918|A Comparative Analysis of Transformer Models in Social Bot Detection]] (80.8% similar)
- [[2025-09-22/A Layered Multi-Expert Framework for Long-Context Mental Health Assessments_20250922|A Layered Multi-Expert Framework for Long-Context Mental Health Assessments]] (80.8% similar)
- [[2025-09-22/A Weak Supervision Approach for Monitoring Recreational Drug Use Effects in Social Media_20250922|A Weak Supervision Approach for Monitoring Recreational Drug Use Effects in Social Media]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/LSTM|LSTM]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Mental Health Detection|Mental Health Detection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16542v1 Announce Type: cross 
Abstract: Millions of people openly share mental health struggles on social media, providing rich data for early detection of conditions such as depression, bipolar disorder, etc. However, most prior Natural Language Processing (NLP) research has focused on single-disorder identification, leaving a gap in understanding the efficacy of advanced NLP techniques for distinguishing among multiple mental health conditions. In this work, we present a large-scale comparative study of state-of-the-art transformer versus Long Short-Term Memory (LSTM)-based models to classify mental health posts into exclusive categories of mental health conditions. We first curate a large dataset of Reddit posts spanning six mental health conditions and a control group, using rigorous filtering and statistical exploratory analysis to ensure annotation quality. We then evaluate five transformer architectures (BERT, RoBERTa, DistilBERT, ALBERT, and ELECTRA) against several LSTM variants (with or without attention, using contextual or static embeddings) under identical conditions. Experimental results show that transformer models consistently outperform the alternatives, with RoBERTa achieving 91-99% F1-scores and accuracies across all classes. Notably, attention-augmented LSTMs with BERT embeddings approach transformer performance (up to 97% F1-score) while training 2-3.5 times faster, whereas LSTMs using static embeddings fail to learn useful signals. These findings represent the first comprehensive benchmark for multi-class mental health detection, offering practical guidance on model selection and highlighting an accuracy-efficiency trade-off for real-world deployment of mental health NLP systems.

## 📝 요약

이 논문은 소셜 미디어에서의 정신 건강 관련 게시물을 분석하여 여러 정신 건강 상태를 구분하는 자연어 처리(NLP) 기법의 효과를 연구한 것이다. 연구진은 Reddit에서 수집한 데이터를 바탕으로, 최신 트랜스포머 모델과 LSTM 기반 모델을 비교하여 정신 건강 상태를 분류하는 실험을 수행했다. 실험 결과, 트랜스포머 모델이 전반적으로 더 높은 성능을 보였으며, 특히 RoBERTa 모델이 91-99%의 F1-score와 정확도를 기록했다. 주목할 만한 점은 BERT 임베딩을 사용한 주의 메커니즘을 추가한 LSTM이 트랜스포머에 근접한 성능을 보이면서도 학습 속도가 2-3.5배 빠르다는 것이다. 이 연구는 다중 클래스 정신 건강 탐지에 대한 첫 종합 벤치마크를 제공하며, 모델 선택에 대한 실용적 지침과 정확도-효율성 간의 균형을 강조한다.

## 🎯 주요 포인트

- 1. 본 연구는 다양한 정신 건강 상태를 구분하기 위한 첨단 NLP 기법의 효능을 이해하는 데 중점을 두고 있습니다.
- 2. 연구에서는 여섯 가지 정신 건강 상태와 대조군을 포함한 대규모 Reddit 데이터셋을 구축하여 분석했습니다.
- 3. 실험 결과, RoBERTa를 포함한 트랜스포머 모델이 모든 클래스에서 91-99%의 F1-스코어와 정확도를 기록하며 LSTM 기반 모델보다 우수한 성능을 보였습니다.
- 4. 주의 메커니즘이 추가된 LSTM 모델은 BERT 임베딩을 활용하여 트랜스포머 모델에 근접한 성능을 보였으나, 정적 임베딩을 사용하는 LSTM은 유용한 신호를 학습하지 못했습니다.
- 5. 이 연구는 다중 클래스 정신 건강 탐지를 위한 최초의 포괄적인 벤치마크를 제공하며, 모델 선택에 대한 실질적인 지침과 정확도-효율성 간의 균형을 강조합니다.


---

*Generated on 2025-09-24 02:10:18*