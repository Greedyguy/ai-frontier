---
keywords:
  - Large Language Model
  - Token-Level Hallucination
  - Variance Signals
  - Autoregressive Models
  - SQuAD v2
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2507.04137
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:39:56.623815",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Token-Level Hallucination",
    "Variance Signals",
    "Autoregressive Models",
    "SQuAD v2"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Token-Level Hallucination": 0.7,
    "Variance Signals": 0.68,
    "Autoregressive Models": 0.72,
    "SQuAD v2": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus on hallucination detection in generative models.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Token-Level Hallucination",
        "canonical": "Token-Level Hallucination",
        "aliases": [
          "Token Hallucination"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel concept specific to the paper's framework.",
        "novelty_score": 0.78,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.7
      },
      {
        "surface": "Variance Signals",
        "canonical": "Variance Signals",
        "aliases": [
          "Variance in Token Log-Probabilities"
        ],
        "category": "unique_technical",
        "rationale": "Key method used for detecting hallucinations, specific to this study.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.68
      },
      {
        "surface": "Autoregressive Models",
        "canonical": "Autoregressive Models",
        "aliases": [
          "Autoregressive Language Models"
        ],
        "category": "specific_connectable",
        "rationale": "Relevant for understanding the types of models evaluated in the study.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      },
      {
        "surface": "SQuAD v2",
        "canonical": "SQuAD v2",
        "aliases": [
          "Stanford Question Answering Dataset v2"
        ],
        "category": "specific_connectable",
        "rationale": "A benchmark dataset used in the evaluation, linking to broader NLP research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "method",
      "framework",
      "analysis"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Token-Level Hallucination",
      "resolved_canonical": "Token-Level Hallucination",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Variance Signals",
      "resolved_canonical": "Variance Signals",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.68
      }
    },
    {
      "candidate_surface": "Autoregressive Models",
      "resolved_canonical": "Autoregressive Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "SQuAD v2",
      "resolved_canonical": "SQuAD v2",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# Detecting Token-Level Hallucinations Using Variance Signals: A Reference-Free Approach

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2507.04137.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2507.04137](https://arxiv.org/abs/2507.04137)

## 🔗 유사한 논문
- [[2025-09-23/Uncertainty-Aware Attention Heads_ Efficient Unsupervised Uncertainty Quantification for LLMs_20250923|Uncertainty-Aware Attention Heads: Efficient Unsupervised Uncertainty Quantification for LLMs]] (86.7% similar)
- [[2025-09-17/DSCC-HS_ A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models_20250917|DSCC-HS: A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models]] (86.4% similar)
- [[2025-09-23/Semantic Reformulation Entropy for Robust Hallucination Detection in QA Tasks_20250923|Semantic Reformulation Entropy for Robust Hallucination Detection in QA Tasks]] (85.8% similar)
- [[2025-09-23/Seeing is Believing? Mitigating OCR Hallucinations in Multimodal Large Language Models_20250923|Seeing is Believing? Mitigating OCR Hallucinations in Multimodal Large Language Models]] (85.6% similar)
- [[2025-09-23/How Large Language Models are Designed to Hallucinate_20250923|How Large Language Models are Designed to Hallucinate]] (84.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Autoregressive Models|Autoregressive Models]], [[keywords/SQuAD v2|SQuAD v2]]
**⚡ Unique Technical**: [[keywords/Token-Level Hallucination|Token-Level Hallucination]], [[keywords/Variance Signals|Variance Signals]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.04137v2 Announce Type: replace-cross 
Abstract: Large Language Models (LLMs) have demonstrated impressive generative capabilities across diverse tasks but remain susceptible to hallucinations, confidently generated yet factually incorrect outputs. We introduce a reference-free, token-level hallucination detection framework that leverages the variance in token log-probabilities across multiple stochastic generations. Unlike prior methods that require ground-truth references or sentence-level verification, our approach is model-agnostic, interpretable, and suited for real-time or post-hoc analysis. We evaluate our method on unanswerable question prompts from the SQuAD v2 dataset and benchmark across three autoregressive models of varying scales: GPT-Neo 125M, Falcon 1B, and Mistral 7B. Through both quantitative metrics and visual diagnostics, we show that token-level variance reliably highlights instability in model outputs and correlates with hallucination patterns. Our framework is lightweight, reproducible, and adaptable to multiple domains, offering a valuable diagnostic tool for analyzing generative reliability in LLMs.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 생성 오류인 환각을 탐지하기 위한 참조 없이 토큰 수준에서의 새로운 프레임워크를 제안합니다. 이 방법은 여러 확률적 생성에서의 토큰 로그 확률의 변동성을 활용하며, 기존의 참조 기반 또는 문장 수준 검증 방법과 달리 모델에 구애받지 않고 해석 가능하며 실시간 또는 사후 분석에 적합합니다. SQuAD v2 데이터셋의 답변 불가능한 질문과 다양한 규모의 자동회귀 모델(GPT-Neo 125M, Falcon 1B, Mistral 7B)을 통해 평가한 결과, 토큰 수준의 변동성이 모델 출력의 불안정성을 잘 나타내며 환각 패턴과 상관관계가 있음을 보여줍니다. 이 프레임워크는 경량, 재현 가능하며 여러 도메인에 적응 가능하여 LLM의 생성 신뢰성을 분석하는 데 유용한 도구를 제공합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)은 다양한 작업에서 뛰어난 생성 능력을 보이지만 사실과 다른 출력을 자신 있게 생성하는 환각 현상에 취약합니다.
- 2. 우리는 여러 확률적 생성에서 토큰 로그 확률의 변동성을 활용한 참조 없는 토큰 수준 환각 감지 프레임워크를 소개합니다.
- 3. 이 방법은 모델에 구애받지 않고 해석 가능하며, 실시간 또는 사후 분석에 적합합니다.
- 4. SQuAD v2 데이터셋의 답할 수 없는 질문 프롬프트를 사용하여 GPT-Neo 125M, Falcon 1B, Mistral 7B 모델에서 우리의 방법을 평가했습니다.
- 5. 토큰 수준의 변동성이 모델 출력의 불안정을 신뢰성 있게 강조하고 환각 패턴과 상관관계가 있음을 보여줍니다.


---

*Generated on 2025-09-26 08:39:56*