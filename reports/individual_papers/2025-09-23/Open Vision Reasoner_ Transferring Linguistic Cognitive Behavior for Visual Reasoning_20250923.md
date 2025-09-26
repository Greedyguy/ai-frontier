---
keywords:
  - Open Vision Reasoner
  - Multimodal Learning
  - Vision-Language Model
  - Reinforcement Learning
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2507.05255
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:17:38.050183",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Open Vision Reasoner",
    "Multimodal Learning",
    "Vision-Language Model",
    "Reinforcement Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Open Vision Reasoner": 0.8,
    "Multimodal Learning": 0.82,
    "Vision-Language Model": 0.78,
    "Reinforcement Learning": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Open Vision Reasoner",
        "canonical": "Open Vision Reasoner",
        "aliases": [
          "OVR"
        ],
        "category": "unique_technical",
        "rationale": "As a novel model, it represents a unique technical advancement in visual reasoning.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multimodal LLMs",
        "canonical": "Multimodal Learning",
        "aliases": [
          "MLLMs"
        ],
        "category": "specific_connectable",
        "rationale": "Connects the fields of language and vision, crucial for understanding cross-modal reasoning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "visual reasoning",
        "canonical": "Vision-Language Model",
        "aliases": [
          "visual reasoning"
        ],
        "category": "evolved_concepts",
        "rationale": "Represents the integration of vision and language capabilities in AI models.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "reinforcement learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "A fundamental technique used in the training process of the model.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "cold start",
      "training dynamics"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Open Vision Reasoner",
      "resolved_canonical": "Open Vision Reasoner",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multimodal LLMs",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "visual reasoning",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "reinforcement learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Open Vision Reasoner: Transferring Linguistic Cognitive Behavior for Visual Reasoning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2507.05255.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2507.05255](https://arxiv.org/abs/2507.05255)

## 🔗 유사한 논문
- [[2025-09-23/ProReason_ Multi-Modal Proactive Reasoning with Decoupled Eyesight and Wisdom_20250923|ProReason: Multi-Modal Proactive Reasoning with Decoupled Eyesight and Wisdom]] (90.4% similar)
- [[2025-09-22/Perception-R1_ Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward_20250922|Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward]] (89.5% similar)
- [[2025-09-23/GeoPQA_ Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning_20250923|GeoPQA: Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning]] (87.5% similar)
- [[2025-09-23/Reasoning Core_ A Scalable RL Environment for LLM Symbolic Reasoning_20250923|Reasoning Core: A Scalable RL Environment for LLM Symbolic Reasoning]] (87.3% similar)
- [[2025-09-23/UR$^2$_ Unify RAG and Reasoning through Reinforcement Learning_20250923|UR$^2$: Unify RAG and Reasoning through Reinforcement Learning]] (87.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Open Vision Reasoner|Open Vision Reasoner]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.05255v2 Announce Type: replace-cross 
Abstract: The remarkable reasoning capability of large language models (LLMs) stems from cognitive behaviors that emerge through reinforcement with verifiable rewards. This work investigates how to transfer this principle to Multimodal LLMs (MLLMs) to unlock advanced visual reasoning. We introduce a two-stage paradigm built on Qwen2.5-VL-7B: a massive linguistic cold-start fine-tuning, followed by multimodal reinforcement learning (RL) spanning nearly 1,000 steps, surpassing all previous open-source efforts in scale. This pioneering work reveals three fundamental insights: 1) Behavior transfer emerges surprisingly early in cold start due to linguistic mental imagery. 2) Cold start broadly memorizes visual behaviors, while RL critically discerns and scales up effective patterns. 3) Transfer strategically favors high-utility behaviors such as visual reflection. Our resulting model, Open-Vision-Reasoner (OVR), achieves state-of-the-art performance on a suite of reasoning benchmarks, including 95.3% on MATH500, 51.8% on MathVision and 54.6% on MathVerse. We release our model, data, and training dynamics to catalyze the development of more capable, behavior-aligned multimodal reasoners.

## 📝 요약

이 논문은 대규모 언어 모델(LLM)의 추론 능력을 멀티모달 LLM(MLLM)으로 확장하여 고급 시각적 추론을 가능하게 하는 방법을 연구합니다. Qwen2.5-VL-7B를 기반으로 한 두 단계의 패러다임을 도입했으며, 초기 대규모 언어 미세 조정 후 약 1,000단계의 멀티모달 강화 학습(RL)을 수행했습니다. 주요 발견사항은 다음과 같습니다: 1) 초기 단계에서 언어적 심상으로 인해 행동 전이가 빠르게 나타납니다. 2) 초기 단계는 시각적 행동을 광범위하게 기억하며, RL은 효과적인 패턴을 구별하고 확장합니다. 3) 전이는 시각적 반영과 같은 높은 유용성의 행동을 전략적으로 선호합니다. 결과적으로 개발된 모델 Open-Vision-Reasoner(OVR)는 다양한 추론 벤치마크에서 최첨단 성능을 달성했습니다. 이 모델, 데이터 및 훈련 과정을 공개하여 더 발전된 멀티모달 추론기의 개발을 촉진하고자 합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 뛰어난 추론 능력은 검증 가능한 보상을 통한 강화 학습에서 비롯되며, 이를 다중 모달 LLM(MLLM)에 적용하여 고급 시각적 추론을 가능하게 하는 방법을 연구합니다.
- 2. Qwen2.5-VL-7B를 기반으로 한 두 단계의 패러다임을 도입하여 대규모 언어적 콜드 스타트 미세 조정과 약 1,000단계에 걸친 다중 모달 강화 학습(RL)을 수행합니다.
- 3. 콜드 스타트 단계에서 언어적 심상 덕분에 행동 전이가 예상보다 일찍 나타나며, RL은 효과적인 패턴을 비판적으로 식별하고 확장합니다.
- 4. 전이는 시각적 반영과 같은 높은 효용의 행동을 전략적으로 선호하며, 최종 모델인 Open-Vision-Reasoner(OVR)는 다양한 추론 벤치마크에서 최첨단 성능을 달성합니다.
- 5. 모델, 데이터 및 학습 동태를 공개하여 더 능력 있는 행동 정렬 다중 모달 추론기의 개발을 촉진합니다.


---

*Generated on 2025-09-24 04:17:38*