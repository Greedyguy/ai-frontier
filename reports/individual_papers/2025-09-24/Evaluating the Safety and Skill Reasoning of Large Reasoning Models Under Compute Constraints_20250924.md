<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:24:39.854047",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Chain-of-Thought Reasoning",
    "Model Quantization",
    "Length Controlled Policy Optimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.8,
    "Chain-of-Thought Reasoning": 0.78,
    "Model Quantization": 0.72,
    "Length Controlled Policy Optimization": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "reasoning language models",
        "canonical": "Large Language Model",
        "aliases": [
          "reasoning models"
        ],
        "category": "broad_technical",
        "rationale": "Links to existing knowledge on large language models and their reasoning capabilities.",
        "novelty_score": 0.3,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "chain-of-thought sequences",
        "canonical": "Chain-of-Thought Reasoning",
        "aliases": [
          "CoT sequences"
        ],
        "category": "unique_technical",
        "rationale": "Represents a specific reasoning approach that is central to the paper's focus.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "model quantization",
        "canonical": "Model Quantization",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A key technique discussed for reducing computational demand, relevant to efficiency studies.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      },
      {
        "surface": "length controlled policy optimization",
        "canonical": "Length Controlled Policy Optimization",
        "aliases": [
          "LCPO"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a specific optimization method relevant to the study's methodology.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "compute constraint",
      "safety performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "reasoning language models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "chain-of-thought sequences",
      "resolved_canonical": "Chain-of-Thought Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "model quantization",
      "resolved_canonical": "Model Quantization",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "length controlled policy optimization",
      "resolved_canonical": "Length Controlled Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Evaluating the Safety and Skill Reasoning of Large Reasoning Models Under Compute Constraints

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18382.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18382](https://arxiv.org/abs/2509.18382)

## 🔗 유사한 논문
- [[2025-09-18/Early Stopping Chain-of-thoughts in Large Language Models_20250918|Early Stopping Chain-of-thoughts in Large Language Models]] (87.1% similar)
- [[2025-09-17/Reasoning Efficiently Through Adaptive Chain-of-Thought Compression_ A Self-Optimizing Framework_20250917|Reasoning Efficiently Through Adaptive Chain-of-Thought Compression: A Self-Optimizing Framework]] (86.5% similar)
- [[2025-09-22/ConCISE_ Confidence-guided Compression in Step-by-step Efficient Reasoning_20250922|ConCISE: Confidence-guided Compression in Step-by-step Efficient Reasoning]] (85.9% similar)
- [[2025-09-23/LTA-thinker_ Latent Thought-Augmented Training Framework for Large Language Models on Complex Reasoning_20250923|LTA-thinker: Latent Thought-Augmented Training Framework for Large Language Models on Complex Reasoning]] (85.7% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (84.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Model Quantization|Model Quantization]]
**⚡ Unique Technical**: [[keywords/Chain-of-Thought Reasoning|Chain-of-Thought Reasoning]], [[keywords/Length Controlled Policy Optimization|Length Controlled Policy Optimization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18382v1 Announce Type: new 
Abstract: Test-time compute scaling has demonstrated the ability to improve the performance of reasoning language models by generating longer chain-of-thought (CoT) sequences. However, this increase in performance comes with a significant increase in computational cost. In this work, we investigate two compute constraint strategies: (1) reasoning length constraint and (2) model quantization, as methods to reduce the compute demand of reasoning models and study their impact on their safety performance. Specifically, we explore two approaches to apply compute constraints to reasoning models: (1) fine-tuning reasoning models using a length controlled policy optimization (LCPO) based reinforcement learning method to satisfy a user-defined CoT reasoning length, and (2) applying quantization to maximize the generation of CoT sequences within a user-defined compute constraint. Furthermore, we study the trade-off between the computational efficiency and the safety of the model.

## 📝 요약

이 연구는 추론 언어 모델의 성능을 향상시키기 위해 긴 사고 과정(Chain-of-Thought, CoT) 시퀀스를 생성하는 테스트 시점 계산 확장이 성능을 높이지만, 계산 비용이 크게 증가하는 문제를 해결하고자 합니다. 이를 위해 두 가지 계산 제약 전략을 제안합니다: (1) 추론 길이 제약과 (2) 모델 양자화. 첫 번째 방법은 길이 제어 정책 최적화(LCPO) 기반 강화 학습을 통해 사용자 정의 CoT 추론 길이를 만족시키도록 모델을 미세 조정하는 것이고, 두 번째 방법은 사용자 정의 계산 제약 내에서 CoT 시퀀스 생성을 최대화하기 위해 양자화를 적용하는 것입니다. 연구는 계산 효율성과 모델 안전성 간의 균형을 분석합니다.

## 🎯 주요 포인트

- 1. 테스트 시 계산 확장은 더 긴 사고의 흐름(CoT) 시퀀스를 생성하여 추론 언어 모델의 성능을 향상시킬 수 있습니다.
- 2. 성능 향상은 계산 비용의 증가를 동반하며, 이를 줄이기 위해 두 가지 계산 제약 전략을 조사합니다: 추론 길이 제약과 모델 양자화.
- 3. 길이 제어 정책 최적화(LCPO) 기반 강화 학습 방법을 사용하여 사용자 정의 CoT 추론 길이를 만족시키도록 모델을 미세 조정합니다.
- 4. 사용자 정의 계산 제약 내에서 CoT 시퀀스 생성을 극대화하기 위해 양자화를 적용합니다.
- 5. 계산 효율성과 모델의 안전성 간의 균형을 연구합니다.


---

*Generated on 2025-09-24 13:24:39*