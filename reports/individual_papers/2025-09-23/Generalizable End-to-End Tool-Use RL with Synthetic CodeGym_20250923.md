---
keywords:
  - Large Language Model
  - CodeGym
  - Reinforcement Learning
  - Out-of-distribution Generalization
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17325
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:52:12.824510",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "CodeGym",
    "Reinforcement Learning",
    "Out-of-distribution Generalization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "CodeGym": 0.8,
    "Reinforcement Learning": 0.78,
    "Out-of-distribution Generalization": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Tool-augmented large language models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM agents",
          "Tool-augmented LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Connects to existing knowledge on large language models, emphasizing their tool-augmented capabilities.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "CodeGym",
        "canonical": "CodeGym",
        "aliases": [
          "CodeGym framework"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel framework for training LLM agents, crucial for understanding the paper's contribution.",
        "novelty_score": 0.92,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "specific_connectable",
        "rationale": "A core method used in the paper, linking to a broad area of machine learning research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Out-of-distribution generalizability",
        "canonical": "Out-of-distribution Generalization",
        "aliases": [
          "OOD generalization"
        ],
        "category": "specific_connectable",
        "rationale": "Key concept for evaluating the model's performance beyond training data.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "static trajectories",
      "supervised fine-tuning"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Tool-augmented large language models",
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
      "candidate_surface": "CodeGym",
      "resolved_canonical": "CodeGym",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Out-of-distribution generalizability",
      "resolved_canonical": "Out-of-distribution Generalization",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Generalizable End-to-End Tool-Use RL with Synthetic CodeGym

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17325.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17325](https://arxiv.org/abs/2509.17325)

## 🔗 유사한 논문
- [[2025-09-19/Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents_20250919|Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents]] (86.5% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (85.2% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I: LLMs are Naturally Interleaved Multimodal Creators]] (84.9% similar)
- [[2025-09-19/LEED_ A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning_20250919|LEED: A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning]] (84.8% similar)
- [[2025-09-23/Generalizability of Large Language Model-Based Agents_ A Comprehensive Survey_20250923|Generalizability of Large Language Model-Based Agents: A Comprehensive Survey]] (84.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|Reinforcement Learning]], [[keywords/Out-of-distribution Generalization|Out-of-distribution Generalization]]
**⚡ Unique Technical**: [[keywords/CodeGym|CodeGym]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17325v1 Announce Type: cross 
Abstract: Tool-augmented large language models (LLMs), hereafter LLM agents, leverage external tools to solve diverse tasks and interface with the real world. However, current training practices largely rely on supervised fine-tuning (SFT) over static trajectories or reinforcement learning (RL) on narrow tasks, and generalize poorly beyond development settings, leading to brittleness with new tools and unseen workflows. Because code execution reflects many structures of real-world workflows, coding problems provide a natural basis for building agent training environments. Motivated by this, we introduce CodeGym, a scalable framework that synthesizes diverse, verifiable, and controllable multi-turn tool-use environments for agent RL, enabling LLM agents to explore and master various workflows actively. CodeGym rewrites static coding problems into interactive environments by extracting atomic functions or logic into callable tools, yielding verifiable tasks that span various tool-execution workflows. Models of varying sizes and chain-of-thought configurations, trained in CodeGym, exhibit consistent out-of-distribution generalizability; for example, Qwen2.5-32B-Instruct achieves an absolute accuracy gain of 8.7 points on the OOD benchmark $\tau$-Bench. These results highlight CodeGym as a step toward scalable general-purpose RL environments that align with real-world agent workflows.

## 📝 요약

이 논문은 외부 도구를 활용하여 다양한 작업을 수행하는 도구 확장형 대형 언어 모델(LLM) 에이전트의 훈련 환경을 개선하기 위해 CodeGym이라는 프레임워크를 제안합니다. 기존의 훈련 방식은 정적 경로에 대한 지도 학습이나 좁은 작업에 대한 강화 학습에 의존하여 새로운 도구와 미지의 작업 흐름에 취약합니다. CodeGym은 다양한 도구 사용 환경을 생성하여 에이전트가 다양한 작업 흐름을 탐색하고 숙달할 수 있도록 합니다. 이 프레임워크는 정적 코딩 문제를 상호작용 환경으로 변환하여 검증 가능한 작업을 제공합니다. CodeGym에서 훈련된 모델들은 개발 환경을 넘어서는 일반화 능력을 보였으며, 예를 들어 Qwen2.5-32B-Instruct 모델은 OOD 벤치마크에서 8.7점의 절대 정확도 향상을 기록했습니다. 이는 CodeGym이 현실 세계의 에이전트 작업 흐름에 맞춘 확장 가능한 범용 강화 학습 환경으로 발전할 가능성을 보여줍니다.

## 🎯 주요 포인트

- 1. LLM 에이전트는 외부 도구를 활용하여 다양한 작업을 수행하고 실제 세계와 상호작용합니다.
- 2. 기존의 훈련 방식은 새로운 도구와 보지 못한 워크플로우에 대한 일반화가 부족합니다.
- 3. CodeGym은 다양한 도구 사용 환경을 제공하여 에이전트가 다양한 워크플로우를 탐색하고 숙달할 수 있도록 합니다.
- 4. CodeGym에서 훈련된 모델은 일관된 분포 외 일반화 성능을 보이며, Qwen2.5-32B-Instruct 모델은 OOD 벤치마크에서 8.7점의 절대 정확도 향상을 달성했습니다.
- 5. CodeGym은 현실 세계의 에이전트 워크플로우에 맞춘 확장 가능한 범용 RL 환경으로의 발전을 나타냅니다.


---

*Generated on 2025-09-23 23:52:12*