---
keywords:
  - Tree-Guided Preference Optimization
  - Web Agents
  - Vision-Language Model
  - Offline Reinforcement Learning
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.14172
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:15:21.165120",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Tree-Guided Preference Optimization",
    "Web Agents",
    "Vision-Language Model",
    "Offline Reinforcement Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Tree-Guided Preference Optimization": 0.8,
    "Web Agents": 0.78,
    "Vision-Language Model": 0.82,
    "Offline Reinforcement Learning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Tree-Guided Preference Optimization",
        "canonical": "Tree-Guided Preference Optimization",
        "aliases": [
          "TGPO"
        ],
        "category": "unique_technical",
        "rationale": "TGPO is a novel framework specifically designed for reinforcement learning in web agents, offering unique optimization strategies.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Web Agents",
        "canonical": "Web Agents",
        "aliases": [
          "Automated Web Interaction Agents"
        ],
        "category": "evolved_concepts",
        "rationale": "Web Agents are increasingly relevant in the context of large models, facilitating automated interactions online.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLMs"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are crucial for understanding multimodal data, linking to both vision and language processing.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Offline Reinforcement Learning",
        "canonical": "Offline Reinforcement Learning",
        "aliases": [
          "Offline RL"
        ],
        "category": "specific_connectable",
        "rationale": "Offline Reinforcement Learning is a key method in the paper, providing a foundation for the proposed TGPO framework.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
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
      "candidate_surface": "Tree-Guided Preference Optimization",
      "resolved_canonical": "Tree-Guided Preference Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Web Agents",
      "resolved_canonical": "Web Agents",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Offline Reinforcement Learning",
      "resolved_canonical": "Offline Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# TGPO: Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning

**Korean Title:** TGPO: 견고한 웹 에이전트 강화 학습을 위한 트리 기반 선호 최적화

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.14172.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.14172](https://arxiv.org/abs/2509.14172)

## 🔗 유사한 논문
- [[2025-09-17/TGPO_ Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning_20250917|TGPO: Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning]] (99.2% similar)
- [[2025-09-18/TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (82.5% similar)
- [[2025-09-19/WebCoT_ Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback_20250919|WebCoT: Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback]] (82.3% similar)
- [[2025-09-19/Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (81.9% similar)
- [[2025-09-22/PVPO_ Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning_20250922|PVPO: Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Offline Reinforcement Learning|Offline Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Tree-Guided Preference Optimization|Tree-Guided Preference Optimization]]
**🚀 Evolved Concepts**: [[keywords/Web Agents|Web Agents]], [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14172v2 Announce Type: replace-cross 
Abstract: With the rapid advancement of large language models and vision-language models, employing large models as Web Agents has become essential for automated web interaction. However, training Web Agents with reinforcement learning faces critical challenges including credit assignment misallocation, prohibitively high annotation costs, and reward sparsity. To address these issues, we propose Tree-Guided Preference Optimization (TGPO), an offline reinforcement learning framework that proposes a tree-structured trajectory representation merging semantically identical states across trajectories to eliminate label conflicts. Our framework incorporates a Process Reward Model that automatically generates fine-grained rewards through subgoal progress, redundancy detection, and action verification. Additionally, a dynamic weighting mechanism prioritizes high-impact decision points during training. Experiments on Online-Mind2Web and our self-constructed C-WebShop datasets demonstrate that TGPO significantly outperforms existing methods, achieving higher success rates with fewer redundant steps.

## 🔍 Abstract (한글 번역)

arXiv:2509.14172v2 발표 유형: 교차 대체  
초록: 대형 언어 모델과 비전-언어 모델의 급속한 발전으로 인해 대형 모델을 웹 에이전트로 활용하는 것이 자동화된 웹 상호작용에 필수적이 되었습니다. 그러나 강화 학습을 통해 웹 에이전트를 훈련하는 것은 신용 할당의 잘못된 배분, 지나치게 높은 주석 비용, 보상의 희소성 등 중요한 문제에 직면해 있습니다. 이러한 문제를 해결하기 위해, 우리는 트리-유도 선호 최적화(Tree-Guided Preference Optimization, TGPO)를 제안합니다. 이는 의미적으로 동일한 상태를 경로 간에 병합하여 레이블 충돌을 제거하는 트리 구조의 경로 표현을 제안하는 오프라인 강화 학습 프레임워크입니다. 우리의 프레임워크는 하위 목표 진행, 중복 감지 및 행동 검증을 통해 세분화된 보상을 자동으로 생성하는 프로세스 보상 모델을 통합합니다. 또한, 훈련 중에 높은 영향력을 가진 결정 지점을 우선시하는 동적 가중치 메커니즘을 포함하고 있습니다. Online-Mind2Web 및 자체 구축한 C-WebShop 데이터셋에 대한 실험 결과, TGPO는 기존 방법을 크게 능가하며, 더 적은 중복 단계로 더 높은 성공률을 달성함을 보여줍니다.

## 📝 요약

이 논문은 대형 언어 모델과 비전-언어 모델의 발전에 따라 웹 에이전트의 자동화된 웹 상호작용이 중요해지는 상황에서, 강화 학습의 어려움을 해결하기 위한 Tree-Guided Preference Optimization (TGPO)라는 오프라인 강화 학습 프레임워크를 제안합니다. TGPO는 트리 구조의 경로 표현을 통해 경로 간 의미적으로 동일한 상태를 병합하여 라벨 충돌을 제거하고, 세부 목표 진행, 중복 탐지, 행동 검증을 통해 세밀한 보상을 자동 생성하는 프로세스 보상 모델을 포함합니다. 또한, 동적 가중치 메커니즘을 통해 훈련 시 중요한 의사결정 지점을 우선시합니다. 실험 결과, TGPO는 Online-Mind2Web 및 C-WebShop 데이터셋에서 기존 방법보다 높은 성공률과 적은 중복 단계로 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델과 비전-언어 모델의 발전으로 웹 에이전트의 자동화된 웹 상호작용이 필수적이 되었다.
- 2. 웹 에이전트의 강화 학습에는 크레딧 할당 오류, 높은 주석 비용, 보상의 희소성 등의 문제가 있다.
- 3. Tree-Guided Preference Optimization (TGPO)은 트리 구조의 궤적 표현을 통해 레이블 충돌을 제거하고, 오프라인 강화 학습을 지원한다.
- 4. TGPO의 프로세스 보상 모델은 세부적인 보상을 자동 생성하며, 중복 탐지와 행동 검증을 포함한다.
- 5. 실험 결과, TGPO는 기존 방법보다 높은 성공률과 적은 중복 단계로 우수한 성능을 보였다.


---

*Generated on 2025-09-23 10:15:21*