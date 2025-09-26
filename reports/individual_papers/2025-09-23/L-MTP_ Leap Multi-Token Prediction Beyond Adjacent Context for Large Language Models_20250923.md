---
keywords:
  - Large Language Model
  - Leap Multi-Token Prediction
  - Next-Token Prediction
  - Inference Efficiency
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2505.17505
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:57:53.151212",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Leap Multi-Token Prediction",
    "Next-Token Prediction",
    "Inference Efficiency"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Leap Multi-Token Prediction": 0.9,
    "Next-Token Prediction": 0.8,
    "Inference Efficiency": 0.7
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
        "rationale": "This is a fundamental concept in the paper, connecting to a wide range of topics in AI and NLP.",
        "novelty_score": 0.2,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Leap Multi-Token Prediction",
        "canonical": "Leap Multi-Token Prediction",
        "aliases": [
          "L-MTP"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel prediction mechanism that is central to the paper's contributions.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.9
      },
      {
        "surface": "Next-Token Prediction",
        "canonical": "Next-Token Prediction",
        "aliases": [
          "NTP"
        ],
        "category": "specific_connectable",
        "rationale": "A key concept in language model training that contrasts with the proposed method.",
        "novelty_score": 0.3,
        "connectivity_score": 0.7,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Inference Efficiency",
        "canonical": "Inference Efficiency",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A critical aspect of model performance discussed in the paper.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.2,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Leap Multi-Token Prediction",
      "resolved_canonical": "Leap Multi-Token Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Next-Token Prediction",
      "resolved_canonical": "Next-Token Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.7,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Inference Efficiency",
      "resolved_canonical": "Inference Efficiency",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# L-MTP: Leap Multi-Token Prediction Beyond Adjacent Context for Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.17505.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2505.17505](https://arxiv.org/abs/2505.17505)

## 🔗 유사한 논문
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning: An Indispensable Path towards New-Generation Large Language Models]] (86.4% similar)
- [[2025-09-23/Probabilistic Token Alignment for Large Language Model Fusion_20250923|Probabilistic Token Alignment for Large Language Model Fusion]] (86.1% similar)
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM: Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (86.0% similar)
- [[2025-09-22/Predicting Language Models' Success at Zero-Shot Probabilistic Prediction_20250922|Predicting Language Models' Success at Zero-Shot Probabilistic Prediction]] (86.0% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (85.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Next-Token Prediction|Next-Token Prediction]], [[keywords/Inference Efficiency|Inference Efficiency]]
**⚡ Unique Technical**: [[keywords/Leap Multi-Token Prediction|Leap Multi-Token Prediction]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.17505v2 Announce Type: replace 
Abstract: Large language models (LLMs) have achieved notable progress. Despite their success, next-token prediction (NTP), the dominant method for LLM training and inference, is constrained in both contextual coverage and inference efficiency due to its inherently sequential process. To overcome these challenges, we propose leap multi-token prediction~(L-MTP), an innovative token prediction method that extends the capabilities of multi-token prediction (MTP) by introducing a leap-based mechanism. Unlike conventional MTP, which generates multiple tokens at adjacent positions, L-MTP strategically skips over intermediate tokens, predicting non-sequential ones in a single forward pass. This structured leap not only enhances the model's ability to capture long-range dependencies but also enables a decoding strategy specially optimized for non-sequential leap token generation, effectively accelerating inference. We theoretically demonstrate the benefit of L-MTP in improving inference efficiency. Experiments across diverse benchmarks validate its merit in boosting both LLM performance and inference speed. The source code is available at https://github.com/Xiaohao-Liu/L-MTP.

## 📝 요약

대형 언어 모델(LLM)은 상당한 발전을 이루었으나, 기존의 다음 토큰 예측(NTP) 방식은 순차적 처리로 인해 문맥 범위와 추론 효율성에 한계가 있습니다. 이를 해결하기 위해, 우리는 도약 기반 메커니즘을 도입한 혁신적인 토큰 예측 방법인 L-MTP를 제안합니다. L-MTP는 기존의 다중 토큰 예측(MTP)과 달리 중간 토큰을 건너뛰어 비순차적으로 예측하며, 이는 모델이 장거리 의존성을 더 잘 포착하고 추론 속도를 가속화할 수 있게 합니다. 이 방법의 이론적 이점과 다양한 벤치마크 실험을 통해 LLM 성능과 추론 속도 향상을 입증했습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 기존 다음 토큰 예측(NTP) 방식은 순차적 처리로 인해 문맥적 범위와 추론 효율성에 한계가 있다.
- 2. L-MTP는 기존 다중 토큰 예측(MTP) 방식의 한계를 극복하기 위해 도약 기반 메커니즘을 도입하여 비순차적 토큰을 예측한다.
- 3. L-MTP는 중간 토큰을 건너뛰고 비순차적 토큰을 예측함으로써, 장거리 의존성을 더 잘 포착하고 추론 속도를 가속화한다.
- 4. 이론적으로 L-MTP는 추론 효율성을 개선하는 데 유리함을 입증하였다.
- 5. 다양한 벤치마크 실험에서 L-MTP는 LLM의 성능과 추론 속도를 모두 향상시키는 것으로 검증되었다.


---

*Generated on 2025-09-24 03:57:53*