---
keywords:
  - Audio Classification
  - Test-Time Scaling
  - Reasoning Models
  - Zero-Shot Learning
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19676
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:43:51.001577",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Audio Classification",
    "Test-Time Scaling",
    "Reasoning Models",
    "Zero-Shot Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Audio Classification": 0.82,
    "Test-Time Scaling": 0.78,
    "Reasoning Models": 0.79,
    "Zero-Shot Learning": 0.81
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "audio classification",
        "canonical": "Audio Classification",
        "aliases": [
          "sound classification"
        ],
        "category": "specific_connectable",
        "rationale": "Audio classification is a specific task that can be linked to various models and techniques in machine learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "test-time scaling",
        "canonical": "Test-Time Scaling",
        "aliases": [
          "scaling during inference"
        ],
        "category": "unique_technical",
        "rationale": "Test-time scaling is a novel approach discussed in the paper that enhances model performance during inference.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "reasoning models",
        "canonical": "Reasoning Models",
        "aliases": [
          "logical models",
          "cognitive models"
        ],
        "category": "specific_connectable",
        "rationale": "Reasoning models are central to the paper's approach and can be linked to advancements in AI reasoning capabilities.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.79
      },
      {
        "surface": "zero-shot reasoning",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "zero-shot inference"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-shot reasoning is a trending concept that aligns with the paper's exploration of reasoning capabilities.",
        "novelty_score": 0.58,
        "connectivity_score": 0.88,
        "specificity_score": 0.77,
        "link_intent_score": 0.81
      }
    ],
    "ban_list_suggestions": [
      "performance",
      "method"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "audio classification",
      "resolved_canonical": "Audio Classification",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "test-time scaling",
      "resolved_canonical": "Test-Time Scaling",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "reasoning models",
      "resolved_canonical": "Reasoning Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "zero-shot reasoning",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.88,
        "specificity": 0.77,
        "link_intent": 0.81
      }
    }
  ]
}
-->

# Thinking While Listening: Simple Test Time Scaling For Audio Classification

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19676.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19676](https://arxiv.org/abs/2509.19676)

## 🔗 유사한 논문
- [[2025-09-23/Audio-Reasoner_ Improving Reasoning Capability in Large Audio Language Models_20250923|Audio-Reasoner: Improving Reasoning Capability in Large Audio Language Models]] (87.2% similar)
- [[2025-09-23/SoundMind_ RL-Incentivized Logic Reasoning for Audio-Language Models_20250923|SoundMind: RL-Incentivized Logic Reasoning for Audio-Language Models]] (86.2% similar)
- [[2025-09-24/Teaching Audio Models to Reason_ A Unified Framework for Source- and Layer-wise Distillation_20250924|Teaching Audio Models to Reason: A Unified Framework for Source- and Layer-wise Distillation]] (86.0% similar)
- [[2025-09-18/Spatial Audio Motion Understanding and Reasoning_20250918|Spatial Audio Motion Understanding and Reasoning]] (85.2% similar)
- [[2025-09-23/AuditoryBench++_ Can Language Models Understand Auditory Knowledge without Hearing?_20250923|AuditoryBench++: Can Language Models Understand Auditory Knowledge without Hearing?]] (84.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Audio Classification|Audio Classification]], [[keywords/Reasoning Models|Reasoning Models]], [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Test-Time Scaling|Test-Time Scaling]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19676v1 Announce Type: cross 
Abstract: We propose a framework that enables neural models to "think while listening" to everyday sounds, thereby enhancing audio classification performance. Motivated by recent advances in the reasoning capabilities of large language models, we address two central questions: (i) how can thinking be incorporated into existing audio classification pipelines to enable reasoning in the category space and improve performance, and (ii) can a new architecture be designed from the ground up to support both thinking and test-time scaling? We demonstrate that in both settings, our models exhibit improved classification accuracy. Leveraging test-time scaling, we observe consistent gains as the number of sampled traces increases. Furthermore, we evaluate two open-source reasoning models, GPT-OSS-20B and Qwen3-14B, showing that while such models are capable of zero-shot reasoning, a lightweight approach--retraining only the embedding matrix of a frozen, smaller model like GPT-2--can surpass the performance of billion-parameter text-based reasoning models.

## 📝 요약

이 논문은 일상 소리를 들으면서 "생각하는" 신경망 모델을 제안하여 오디오 분류 성능을 향상시키는 방법을 연구합니다. 주요 기여는 두 가지 질문에 대한 답을 제시하는 것입니다: 첫째, 기존 오디오 분류 파이프라인에 사고 과정을 어떻게 통합하여 성능을 향상시킬 수 있는가, 둘째, 사고와 테스트 시 확장을 지원하는 새로운 아키텍처를 설계할 수 있는가입니다. 제안된 모델은 분류 정확도를 개선하며, 테스트 시 확장을 활용하여 샘플 수가 증가할수록 일관된 성능 향상을 보입니다. 또한, 두 개의 오픈소스 추론 모델인 GPT-OSS-20B와 Qwen3-14B를 평가한 결과, 경량 접근법으로 작은 모델의 임베딩 매트릭스만 재훈련해도 대규모 텍스트 기반 추론 모델의 성능을 능가할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. 본 연구는 일상 소리를 들으면서 사고할 수 있는 신경망 모델 프레임워크를 제안하여 오디오 분류 성능을 향상시킵니다.
- 2. 기존 오디오 분류 파이프라인에 사고 과정을 통합하여 범주 공간에서의 추론을 가능하게 하고 성능을 개선하는 방법을 탐구합니다.
- 3. 새로운 아키텍처를 설계하여 사고와 테스트 시 확장을 지원하는 방법을 모색합니다.
- 4. 테스트 시 확장을 활용하여 샘플링된 추적 수가 증가함에 따라 일관된 성능 향상을 관찰했습니다.
- 5. 경량 접근 방식인 임베딩 매트릭스 재훈련이 대규모 텍스트 기반 추론 모델의 성능을 능가할 수 있음을 보여줍니다.


---

*Generated on 2025-09-25 15:43:51*