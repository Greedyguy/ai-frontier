---
keywords:
  - Multimodal Learning
  - Self-supervised Learning
  - Chain-of-Thought Reasoning
  - Zero-Shot Learning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2505.20024
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:01:49.166193",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Self-supervised Learning",
    "Chain-of-Thought Reasoning",
    "Zero-Shot Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.85,
    "Self-supervised Learning": 0.78,
    "Chain-of-Thought Reasoning": 0.8,
    "Zero-Shot Learning": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "multimodal large language models",
        "canonical": "Multimodal Learning",
        "aliases": [
          "MLLMs"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Learning is a key concept for linking vision and language reasoning in autonomous systems.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "self-supervised Next Scene Prediction",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "Next Scene Prediction"
        ],
        "category": "specific_connectable",
        "rationale": "Self-supervised Learning is crucial for training models to predict future scenes without labeled data.",
        "novelty_score": 0.6,
        "connectivity_score": 0.82,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Decision Chain-of-Thought",
        "canonical": "Chain-of-Thought Reasoning",
        "aliases": [
          "Decision Reasoning"
        ],
        "category": "unique_technical",
        "rationale": "Chain-of-Thought Reasoning enhances decision-making processes in autonomous systems.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "zero-shot generalization",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "zero-shot"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-Shot Learning is essential for adapting models to new, unseen scenarios without additional training.",
        "novelty_score": 0.58,
        "connectivity_score": 0.84,
        "specificity_score": 0.77,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "closed-loop systems",
      "E2E imitation learning"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "multimodal large language models",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "self-supervised Next Scene Prediction",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.82,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Decision Chain-of-Thought",
      "resolved_canonical": "Chain-of-Thought Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "zero-shot generalization",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.84,
        "specificity": 0.77,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# ReasonPlan: Unified Scene Prediction and Decision Reasoning for Closed-loop Autonomous Driving

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.20024.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2505.20024](https://arxiv.org/abs/2505.20024)

## 🔗 유사한 논문
- [[2025-09-17/MAP_ End-to-End Autonomous Driving with Map-Assisted Planning_20250917|MAP: End-to-End Autonomous Driving with Map-Assisted Planning]] (85.3% similar)
- [[2025-09-23/ProReason_ Multi-Modal Proactive Reasoning with Decoupled Eyesight and Wisdom_20250923|ProReason: Multi-Modal Proactive Reasoning with Decoupled Eyesight and Wisdom]] (84.7% similar)
- [[2025-09-22/CoReVLA_ A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine_20250922|CoReVLA: A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine]] (83.3% similar)
- [[2025-09-23/Reasoning Core_ A Scalable RL Environment for LLM Symbolic Reasoning_20250923|Reasoning Core: A Scalable RL Environment for LLM Symbolic Reasoning]] (83.1% similar)
- [[2025-09-19/ThinkAct_ Vision-Language-Action Reasoning via Reinforced Visual Latent Planning_20250919|ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning]] (82.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Self-supervised Learning|Self-supervised Learning]], [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Chain-of-Thought Reasoning|Chain-of-Thought Reasoning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.20024v2 Announce Type: replace-cross 
Abstract: Due to the powerful vision-language reasoning and generalization abilities, multimodal large language models (MLLMs) have garnered significant attention in the field of end-to-end (E2E) autonomous driving. However, their application to closed-loop systems remains underexplored, and current MLLM-based methods have not shown clear superiority to mainstream E2E imitation learning approaches. In this work, we propose ReasonPlan, a novel MLLM fine-tuning framework designed for closed-loop driving through holistic reasoning with a self-supervised Next Scene Prediction task and supervised Decision Chain-of-Thought process. This dual mechanism encourages the model to align visual representations with actionable driving context, while promoting interpretable and causally grounded decision making. We curate a planning-oriented decision reasoning dataset, namely PDR, comprising 210k diverse and high-quality samples. Our method outperforms the mainstream E2E imitation learning method by a large margin of 19% L2 and 16.1 driving score on Bench2Drive benchmark. Furthermore, ReasonPlan demonstrates strong zero-shot generalization on unseen DOS benchmark, highlighting its adaptability in handling zero-shot corner cases. Code and dataset will be found in https://github.com/Liuxueyi/ReasonPlan.

## 📝 요약

이 논문에서는 멀티모달 대형 언어 모델(MLLM)을 활용한 자율주행 기술을 개선하기 위해 ReasonPlan이라는 새로운 프레임워크를 제안합니다. 이 프레임워크는 자기 지도 학습 기반의 다음 장면 예측과 지도 학습 기반의 의사결정 사고 과정을 통해 모델이 시각적 표현과 주행 맥락을 정렬하고, 해석 가능하며 인과적으로 타당한 의사결정을 하도록 유도합니다. 이를 위해 21만 개의 다양한 샘플로 구성된 계획 지향적 의사결정 데이터셋(PDR)을 구축했습니다. 제안된 방법은 Bench2Drive 벤치마크에서 기존의 E2E 모방 학습 방법보다 19% L2와 16.1의 주행 점수로 우수한 성능을 보였으며, 새로운 DOS 벤치마크에서 제로샷 일반화 능력을 입증했습니다. 코드와 데이터셋은 GitHub에서 제공됩니다.

## 🎯 주요 포인트

- 1. ReasonPlan은 폐쇄 루프 주행을 위한 새로운 MLLM 미세 조정 프레임워크로, 자기 지도 학습과 감독 학습을 결합하여 해석 가능하고 인과적으로 근거 있는 의사 결정을 촉진합니다.
- 2. PDR이라는 계획 지향적 의사 결정 추론 데이터셋을 구축하여 21만 개의 다양한 고품질 샘플을 포함합니다.
- 3. ReasonPlan은 Bench2Drive 벤치마크에서 주류 E2E 모방 학습 방법을 L2 19%와 주행 점수 16.1로 큰 차이로 능가합니다.
- 4. ReasonPlan은 보지 못한 DOS 벤치마크에서 강력한 제로샷 일반화를 보여주며, 제로샷 코너 케이스를 처리하는 적응성을 강조합니다.
- 5. 코드와 데이터셋은 https://github.com/Liuxueyi/ReasonPlan에서 찾을 수 있습니다.


---

*Generated on 2025-09-24 01:01:49*