---
keywords:
  - Reinforcement Learning with Verifiable Reward
  - Large Language Model
  - Chain-of-Thought Reasoning
  - Curriculum Learning Framework
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2508.07809
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:49:42.668228",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning with Verifiable Reward",
    "Large Language Model",
    "Chain-of-Thought Reasoning",
    "Curriculum Learning Framework"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Reinforcement Learning with Verifiable Reward": 0.8,
    "Large Language Model": 0.85,
    "Chain-of-Thought Reasoning": 0.78,
    "Curriculum Learning Framework": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Reinforcement Learning with Verifiable Reward",
        "canonical": "Reinforcement Learning with Verifiable Reward",
        "aliases": [
          "RLVR"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's approach and represents a novel paradigm in reinforcement learning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are crucial to the paper's methodology and are a well-established concept in machine learning.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Chain-of-Thought Reasoning",
        "canonical": "Chain-of-Thought Reasoning",
        "aliases": [
          "CoT Reasoning"
        ],
        "category": "specific_connectable",
        "rationale": "This reasoning method is a key component of the proposed framework and enhances understanding of LLM capabilities.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Curriculum Learning Framework",
        "canonical": "Curriculum Learning Framework",
        "aliases": [
          "Curriculum Learning"
        ],
        "category": "specific_connectable",
        "rationale": "Curriculum learning is a strategic approach in machine learning that aligns with the paper's focus on improving LLM performance.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "exploration bottleneck",
      "rollout accuracy",
      "sparse rewards"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Reinforcement Learning with Verifiable Reward",
      "resolved_canonical": "Reinforcement Learning with Verifiable Reward",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Chain-of-Thought Reasoning",
      "resolved_canonical": "Chain-of-Thought Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Curriculum Learning Framework",
      "resolved_canonical": "Curriculum Learning Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# EvoCoT: Overcoming the Exploration Bottleneck in Reinforcement Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2508.07809.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2508.07809](https://arxiv.org/abs/2508.07809)

## 🔗 유사한 논문
- [[2025-09-23/ConfClip_ Confidence-Weighted and Clipped Reward for Reinforcement Learning in LLMs_20250923|ConfClip: Confidence-Weighted and Clipped Reward for Reinforcement Learning in LLMs]] (86.7% similar)
- [[2025-09-22/Cache-of-Thought_ Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning_20250922|Cache-of-Thought: Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning]] (86.6% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (86.5% similar)
- [[2025-09-23/Large Language Models as End-to-end Combinatorial Optimization Solvers_20250923|Large Language Models as End-to-end Combinatorial Optimization Solvers]] (86.2% similar)
- [[2025-09-22/Perception-R1_ Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward_20250922|Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward]] (86.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Chain-of-Thought Reasoning|Chain-of-Thought Reasoning]], [[keywords/Curriculum Learning Framework|Curriculum Learning Framework]]
**⚡ Unique Technical**: [[keywords/Reinforcement Learning with Verifiable Reward|Reinforcement Learning with Verifiable Reward]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.07809v3 Announce Type: replace 
Abstract: Reinforcement learning with verifiable reward (RLVR) has become a promising paradigm for post-training large language models (LLMs) to improve their reasoning capability. However, when the rollout accuracy is low on hard problems, the reward becomes sparse, limiting learning efficiency and causing exploration bottlenecks. Existing approaches either rely on teacher models for distillation or filter out difficult problems, which limits scalability or restricts reasoning improvement through exploration.
  We propose EvoCoT, a self-evolving curriculum learning framework based on two-stage chain-of-thought (CoT) reasoning optimization. EvoCoT constrains the exploration space by self-generating and verifying CoT trajectories, then gradually shortens CoT steps to expand the space in a controlled way. The framework enables LLMs to stably learn from initially unsolved hard problems under sparse rewards. We apply EvoCoT to multiple LLM families, including Qwen, DeepSeek, and Llama. Experiments show that EvoCoT enables LLMs to solve previously unsolved problems, improves reasoning capability without external CoT supervision, and is compatible with various RL fine-tuning methods. We release the source code to support future research.

## 📝 요약

이 논문은 강화 학습에서 검증 가능한 보상을 활용하여 대형 언어 모델(LLM)의 추론 능력을 향상시키는 새로운 접근법인 EvoCoT를 제안합니다. 기존 방법은 어려운 문제에서 보상이 희소해 학습 효율이 떨어지는 문제를 겪습니다. EvoCoT는 두 단계의 사고 사슬(CoT) 최적화를 통해 탐색 공간을 제한하고, 자가 생성 및 검증을 통해 점진적으로 CoT 단계를 줄여가며 탐색 공간을 확장합니다. 이를 통해 초기에는 해결되지 않았던 어려운 문제에서도 LLM이 안정적으로 학습할 수 있게 합니다. EvoCoT는 Qwen, DeepSeek, Llama 등 다양한 LLM에 적용되어 이전에 해결하지 못한 문제를 해결하고, 외부 CoT 감독 없이도 추론 능력을 향상시킵니다. 실험 결과, EvoCoT는 다양한 강화 학습 미세 조정 방법과 호환되며, 소스 코드를 공개하여 향후 연구를 지원합니다.

## 🎯 주요 포인트

- 1. 강화 학습에서 검증 가능한 보상(RLVR)은 대형 언어 모델(LLM)의 추론 능력을 향상시키기 위한 유망한 패러다임으로 주목받고 있다.
- 2. EvoCoT는 두 단계의 연쇄적 사고(CoT) 최적화를 기반으로 한 자기 진화형 커리큘럼 학습 프레임워크를 제안한다.
- 3. EvoCoT는 CoT 경로를 자체 생성 및 검증하여 탐색 공간을 제한하고, CoT 단계를 점진적으로 단축하여 탐색 공간을 통제된 방식으로 확장한다.
- 4. EvoCoT는 Qwen, DeepSeek, Llama를 포함한 여러 LLM 계열에 적용되어, 외부 CoT 감독 없이도 추론 능력을 향상시키고 다양한 강화 학습 미세 조정 방법과 호환된다.
- 5. 실험 결과, EvoCoT는 이전에 해결되지 않았던 문제를 해결할 수 있게 하고, 소스 코드를 공개하여 향후 연구를 지원한다.


---

*Generated on 2025-09-24 02:49:42*