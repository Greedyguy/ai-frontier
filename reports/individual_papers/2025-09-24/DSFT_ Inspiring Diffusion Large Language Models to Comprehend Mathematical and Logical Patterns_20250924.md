<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:48:19.045565",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Large Language Models",
    "Mathematical and Logical Patterns",
    "Diffusion SFT",
    "Reinforcement Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diffusion Large Language Models": 0.78,
    "Mathematical and Logical Patterns": 0.79,
    "Diffusion SFT": 0.77,
    "Reinforcement Learning": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diffusion Large Language Models",
        "canonical": "Diffusion Large Language Models",
        "aliases": [
          "dLLMs"
        ],
        "category": "unique_technical",
        "rationale": "This represents a novel architecture in language models, distinct from traditional autoregressive models, offering new insights into model training and performance.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Mathematical and Logical Patterns",
        "canonical": "Mathematical and Logical Patterns",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Understanding these patterns is crucial for improving model performance on numerically and order-sensitive tasks.",
        "novelty_score": 0.7,
        "connectivity_score": 0.8,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "DSFT",
        "canonical": "Diffusion SFT",
        "aliases": [
          "DSFT"
        ],
        "category": "unique_technical",
        "rationale": "DSFT is a specific training strategy proposed in the paper, highlighting its novel approach to improving comprehension in diffusion models.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is a key method mentioned for training models, relevant for linking with other machine learning strategies.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "pre-training",
      "fine-tuning",
      "general knowledge retention"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Diffusion Large Language Models",
      "resolved_canonical": "Diffusion Large Language Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Mathematical and Logical Patterns",
      "resolved_canonical": "Mathematical and Logical Patterns",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.8,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "DSFT",
      "resolved_canonical": "Diffusion SFT",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# DSFT: Inspiring Diffusion Large Language Models to Comprehend Mathematical and Logical Patterns

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18164.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18164](https://arxiv.org/abs/2509.18164)

## 🔗 유사한 논문
- [[2025-09-23/Time Is a Feature_ Exploiting Temporal Dynamics in Diffusion Language Models_20250923|Time Is a Feature: Exploiting Temporal Dynamics in Diffusion Language Models]] (85.9% similar)
- [[2025-09-22/Discrete Diffusion in Large Language and Multimodal Models_ A Survey_20250922|Discrete Diffusion in Large Language and Multimodal Models: A Survey]] (84.3% similar)
- [[2025-09-24/Sparse Training Scheme for Multimodal LLM_20250924|Sparse Training Scheme for Multimodal LLM]] (83.2% similar)
- [[2025-09-22/Mind the Gap_ Data Rewriting for Stable Off-Policy Supervised Fine-Tuning_20250922|Mind the Gap: Data Rewriting for Stable Off-Policy Supervised Fine-Tuning]] (83.2% similar)
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM: Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (83.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Mathematical and Logical Patterns|Mathematical and Logical Patterns]]
**⚡ Unique Technical**: [[keywords/Diffusion Large Language Models|Diffusion Large Language Models]], [[keywords/Diffusion SFT|Diffusion SFT]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18164v1 Announce Type: new 
Abstract: Diffusion large language models (dLLMs) have emerged as a new architecture following auto regressive models. Their denoising process offers a powerful generative advantage, but they present significant challenges in learning and understanding numerically sensitive mathematical and order-sensitive logical tasks. Current training methods, including pre-training, fine-tuning, and reinforcement learning, focus primarily on improving general knowledge retention and reasoning abilities, but lack a comprehensive understanding of mathematical and logical patterns. We propose DSFT, a simple yet effective Diffusion SFT strategy, by adjusting the masking strategy and loss function, guiding models to understand mathematical and logical patterns. This strategy can be flexibly combined with pre-training, reinforcement learning, and other training methods. Validated on models such as LLaDA and Dream series, we prove that DSFT on small-scale data can achieve improvements of 5-10% and approximately 2% on mathematical and logical problems, respectively. This inspiring masking approach offers insights for future learning of specific patterns, which can be easily and efficiently combined with other training methods and applied to various dLLMs. Our code is publicly available at https://anonymous.4open.science/r/DSFT-0FFB/

## 📝 요약

이 논문은 확산 대형 언어 모델(dLLMs)의 수학적 및 논리적 패턴 이해를 개선하기 위한 DSFT라는 새로운 전략을 제안합니다. 기존의 학습 방법들이 일반적인 지식 보유와 추론 능력에 중점을 두는 반면, DSFT는 마스킹 전략과 손실 함수를 조정하여 수학적 및 논리적 패턴을 이해하도록 모델을 유도합니다. LLaDA와 Dream 시리즈 모델을 통해 소규모 데이터에서 수학적 문제는 5-10%, 논리적 문제는 약 2%의 성능 향상을 확인했습니다. 이 전략은 다른 학습 방법과 쉽게 결합 가능하며 다양한 dLLMs에 적용할 수 있습니다.

## 🎯 주요 포인트

- 1. 확산 대형 언어 모델(dLLMs)은 수치 및 순서에 민감한 수학적, 논리적 과제를 학습하는 데 어려움을 겪습니다.
- 2. DSFT는 마스킹 전략과 손실 함수를 조정하여 수학적 및 논리적 패턴을 이해하도록 모델을 유도하는 간단하면서도 효과적인 전략입니다.
- 3. DSFT는 사전 훈련, 강화 학습 등과 유연하게 결합할 수 있으며, 작은 규모의 데이터에서도 수학적 문제에서 5-10%, 논리적 문제에서 약 2%의 성능 향상을 달성했습니다.
- 4. 이 마스킹 접근법은 특정 패턴 학습의 미래에 대한 통찰력을 제공하며, 다양한 dLLMs에 쉽게 적용할 수 있습니다.
- 5. DSFT의 코드는 공개적으로 제공되어 있어, 다른 연구자들이 활용할 수 있습니다.


---

*Generated on 2025-09-24 14:48:19*