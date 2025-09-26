---
keywords:
  - Masked Diffusion Models
  - Reward-Weighted Sampling
  - Non-Autoregressive Generation
  - Large Language Model
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.00707
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:24:23.282387",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Masked Diffusion Models",
    "Reward-Weighted Sampling",
    "Non-Autoregressive Generation",
    "Large Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Masked Diffusion Models": 0.78,
    "Reward-Weighted Sampling": 0.82,
    "Non-Autoregressive Generation": 0.8,
    "Large Language Model": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Masked Diffusion Models",
        "canonical": "Masked Diffusion Models",
        "aliases": [
          "MDMs"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel approach in language modeling, distinct from traditional autoregressive models.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Reward-Weighted Sampling",
        "canonical": "Reward-Weighted Sampling",
        "aliases": [
          "RWS"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a new decoding strategy that enhances non-autoregressive characteristics, pivotal for linking novel methodologies.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Non-Autoregressive Generation",
        "canonical": "Non-Autoregressive Generation",
        "aliases": [
          "NAG"
        ],
        "category": "specific_connectable",
        "rationale": "Key concept in the paper that contrasts with autoregressive methods, facilitating connections to related non-sequential models.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Modeling",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Broad technical term that provides context and links to other works in language modeling.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "decoding methods",
      "evaluation metrics"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Masked Diffusion Models",
      "resolved_canonical": "Masked Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Reward-Weighted Sampling",
      "resolved_canonical": "Reward-Weighted Sampling",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Non-Autoregressive Generation",
      "resolved_canonical": "Non-Autoregressive Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Modeling",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Reward-Weighted Sampling: Enhancing Non-Autoregressive Characteristics in Masked Diffusion LLMs

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.00707.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.00707](https://arxiv.org/abs/2509.00707)

## 🔗 유사한 논문
- [[2025-09-17/Masked Diffusion Models as Energy Minimization_20250917|Masked Diffusion Models as Energy Minimization]] (83.4% similar)
- [[2025-09-18/Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning_20250918|Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning]] (82.7% similar)
- [[2025-09-23/Time Is a Feature_ Exploiting Temporal Dynamics in Diffusion Language Models_20250923|Time Is a Feature: Exploiting Temporal Dynamics in Diffusion Language Models]] (82.6% similar)
- [[2025-09-22/Discrete Diffusion in Large Language and Multimodal Models_ A Survey_20250922|Discrete Diffusion in Large Language and Multimodal Models: A Survey]] (82.2% similar)
- [[2025-09-23/Audio-Conditioned Diffusion LLMs for ASR and Deliberation Processing_20250923|Audio-Conditioned Diffusion LLMs for ASR and Deliberation Processing]] (82.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Non-Autoregressive Generation|Non-Autoregressive Generation]]
**⚡ Unique Technical**: [[keywords/Masked Diffusion Models|Masked Diffusion Models]], [[keywords/Reward-Weighted Sampling|Reward-Weighted Sampling]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.00707v2 Announce Type: replace-cross 
Abstract: Masked diffusion models (MDMs) offer a promising non-autoregressive alternative for large language modeling. Standard decoding methods for MDMs, such as confidence-based sampling, select tokens independently based on individual token confidences at each diffusion step. However, we observe that this independent token selection often results in generation orders resembling sequential autoregressive processes, limiting the advantages of non-autoregressive modeling. To mitigate this pheonomenon, we propose Reward-Weighted Sampling (RWS), a novel decoding strategy that leverages an external reward model to provide a principled global signal during the iterative diffusion process. Specifically, at each diffusion step, RWS evaluates the quality of the entire intermediate sequence and scales token logits accordingly, guiding token selection by integrating global sequence-level coherence. This method selectively increases the confidence of tokens that initially have lower scores, thereby promoting a more non-autoregressive generation order. Furthermore, we provide theoretical justification showing that reward-weighted logit scaling induces beneficial rank reversals in token selection and consistently improves expected reward. Experiments demonstrate that RWS significantly promotes non-autoregressive generation orders, leading to improvements across multiple evaluation metrics. These results highlight the effectiveness of integrating global signals in enhancing both the non-autoregressive properties and overall performance of MDMs.

## 📝 요약

마스크드 디퓨전 모델(MDM)은 대규모 언어 모델링에 비자동회귀적 대안을 제공합니다. 기존의 MDM 디코딩 방법은 각 디퓨전 단계에서 개별 토큰의 신뢰도를 기반으로 독립적으로 토큰을 선택하지만, 이는 종종 순차적 자동회귀 과정과 유사한 생성 순서를 초래합니다. 이를 해결하기 위해, 우리는 외부 보상 모델을 활용하여 전체 중간 시퀀스의 품질을 평가하고 토큰 로짓을 조정하는 보상 가중 샘플링(RWS)이라는 새로운 디코딩 전략을 제안합니다. RWS는 초기 점수가 낮은 토큰의 신뢰도를 높여 비자동회귀적 생성 순서를 촉진합니다. 이 방법은 토큰 선택에서 유익한 순위 변화를 유도하고 기대 보상을 향상시킵니다. 실험 결과, RWS는 비자동회귀적 생성 순서를 크게 촉진하여 여러 평가 지표에서 성능을 개선함을 보여줍니다.

## 🎯 주요 포인트

- 1. Masked diffusion models(MDMs)는 대규모 언어 모델링을 위한 비자기회귀적 대안으로 주목받고 있다.
- 2. 기존의 MDMs 디코딩 방법은 독립적인 토큰 선택으로 인해 자기회귀적 생성 순서를 유사하게 나타내는 경향이 있다.
- 3. Reward-Weighted Sampling(RWS)는 외부 보상 모델을 활용하여 전역적인 신호를 제공하는 새로운 디코딩 전략이다.
- 4. RWS는 전역 시퀀스 수준의 일관성을 통합하여 토큰 선택을 안내하며 비자기회귀적 생성 순서를 촉진한다.
- 5. 실험 결과, RWS는 비자기회귀적 생성 순서를 크게 촉진하고 여러 평가 지표에서 성능 향상을 이끌어낸다.


---

*Generated on 2025-09-24 01:24:23*