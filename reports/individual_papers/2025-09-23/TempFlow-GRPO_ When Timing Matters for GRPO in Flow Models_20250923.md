---
keywords:
  - TempFlow-GRPO
  - Text-to-Image Generation
  - Reinforcement Learning
  - Human Preference Alignment
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2508.04324
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:28:32.281463",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "TempFlow-GRPO",
    "Text-to-Image Generation",
    "Reinforcement Learning",
    "Human Preference Alignment"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "TempFlow-GRPO": 0.78,
    "Text-to-Image Generation": 0.79,
    "Reinforcement Learning": 0.75,
    "Human Preference Alignment": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "TempFlow-GRPO",
        "canonical": "TempFlow-GRPO",
        "aliases": [
          "Temporal Flow GRPO"
        ],
        "category": "unique_technical",
        "rationale": "TempFlow-GRPO is a novel framework specifically designed for improving GRPO training in flow models, offering unique insights into temporal optimization.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "text-to-image generation",
        "canonical": "Text-to-Image Generation",
        "aliases": [
          "text to image synthesis"
        ],
        "category": "specific_connectable",
        "rationale": "Text-to-Image Generation is a key application area for flow models, facilitating connections to multimodal learning and vision-language models.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "reinforcement learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is integral to the optimization process discussed, linking to broader machine learning strategies.",
        "novelty_score": 0.3,
        "connectivity_score": 0.92,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "human preference alignment",
        "canonical": "Human Preference Alignment",
        "aliases": [
          "preference alignment"
        ],
        "category": "evolved_concepts",
        "rationale": "Human Preference Alignment is crucial for ensuring models align with user expectations, linking to ethical AI and user-centric design.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "TempFlow-GRPO",
      "resolved_canonical": "TempFlow-GRPO",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "text-to-image generation",
      "resolved_canonical": "Text-to-Image Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "reinforcement learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.92,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "human preference alignment",
      "resolved_canonical": "Human Preference Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# TempFlow-GRPO: When Timing Matters for GRPO in Flow Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2508.04324.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2508.04324](https://arxiv.org/abs/2508.04324)

## 🔗 유사한 논문
- [[2025-09-23/GRPOformer_ Advancing Hyperparameter Optimization via Group Relative Policy Optimization_20250923|GRPOformer: Advancing Hyperparameter Optimization via Group Relative Policy Optimization]] (83.4% similar)
- [[2025-09-22/OSPO_ Object-centric Self-improving Preference Optimization for Text-to-Image Generation_20250922|OSPO: Object-centric Self-improving Preference Optimization for Text-to-Image Generation]] (83.2% similar)
- [[2025-09-23/TempSamp-R1_ Effective Temporal Sampling with Reinforcement Fine-Tuning for Video LLMs_20250923|TempSamp-R1: Effective Temporal Sampling with Reinforcement Fine-Tuning for Video LLMs]] (82.9% similar)
- [[2025-09-17/TGPO_ Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning_20250917|TGPO: Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning]] (82.4% similar)
- [[2025-09-19/FlowRL_ Matching Reward Distributions for LLM Reasoning_20250919|FlowRL: Matching Reward Distributions for LLM Reasoning]] (82.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Text-to-Image Generation|Text-to-Image Generation]]
**⚡ Unique Technical**: [[keywords/TempFlow-GRPO|TempFlow-GRPO]]
**🚀 Evolved Concepts**: [[keywords/Human Preference Alignment|Human Preference Alignment]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.04324v2 Announce Type: replace 
Abstract: Recent flow matching models for text-to-image generation have achieved remarkable quality, yet their integration with reinforcement learning for human preference alignment remains suboptimal, hindering fine-grained reward-based optimization. We observe that the key impediment to effective GRPO training of flow models is the temporal uniformity assumption in existing approaches: sparse terminal rewards with uniform credit assignment fail to capture the varying criticality of decisions across generation timesteps, resulting in inefficient exploration and suboptimal convergence. To remedy this shortcoming, we introduce \textbf{TempFlow-GRPO} (Temporal Flow GRPO), a principled GRPO framework that captures and exploits the temporal structure inherent in flow-based generation. TempFlow-GRPO introduces three key innovations: (i) a trajectory branching mechanism that provides process rewards by concentrating stochasticity at designated branching points, enabling precise credit assignment without requiring specialized intermediate reward models; (ii) a noise-aware weighting scheme that modulates policy optimization according to the intrinsic exploration potential of each timestep, prioritizing learning during high-impact early stages while ensuring stable refinement in later phases; and (iii) a seed group strategy that controls for initialization effects to isolate exploration contributions. These innovations endow the model with temporally-aware optimization that respects the underlying generative dynamics, leading to state-of-the-art performance in human preference alignment and text-to-image benchmarks.

## 📝 요약

최근 텍스트-이미지 생성에서 흐름 매칭 모델의 품질은 뛰어나지만, 인간의 선호도에 맞춘 강화 학습과의 통합은 미흡하여 세밀한 보상 기반 최적화가 어렵습니다. 기존 방법의 시간적 균일성 가정이 비효율적인 탐색과 최적화의 장애물로 작용함을 발견했습니다. 이를 해결하기 위해, 우리는 \textbf{TempFlow-GRPO}라는 새로운 프레임워크를 제안합니다. TempFlow-GRPO는 (i) 지정된 분기점에서 확률성을 집중시켜 정확한 보상 할당을 가능하게 하는 경로 분기 메커니즘, (ii) 각 시간 단계의 탐색 잠재력에 따라 정책 최적화를 조절하는 노이즈 인식 가중치 체계, (iii) 초기화 효과를 통제하여 탐색 기여를 분리하는 시드 그룹 전략을 도입합니다. 이러한 혁신은 모델이 생성의 시간적 구조를 고려한 최적화를 가능하게 하여 인간 선호도 정렬과 텍스트-이미지 생성에서 최첨단 성능을 달성하게 합니다.

## 🎯 주요 포인트

- 1. 기존의 텍스트-이미지 생성 흐름 모델은 강화 학습과의 통합에서 비효율적인 탐색과 수렴 문제를 겪고 있습니다.
- 2. TempFlow-GRPO는 흐름 기반 생성의 시간 구조를 활용하여 강화 학습을 최적화하는 새로운 프레임워크입니다.
- 3. 이 프레임워크는 지정된 분기점에서 확률성을 집중시켜 정확한 크레딧 할당을 가능하게 하는 궤적 분기 메커니즘을 도입합니다.
- 4. 시간 단계별 탐색 잠재력에 따라 정책 최적화를 조절하는 노이즈 인식 가중치 체계를 통해 학습을 우선시합니다.
- 5. 초기화 효과를 통제하여 탐색 기여를 분리하는 시드 그룹 전략을 통해 인간 선호도 정렬 및 텍스트-이미지 벤치마크에서 최첨단 성능을 달성합니다.


---

*Generated on 2025-09-24 05:28:32*