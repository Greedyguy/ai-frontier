---
keywords:
  - Large Language Model
  - Curriculum Reinforcement Learning
  - Mathematical Reasoning Tasks
  - Variance-based Curriculum
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19803
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:40:08.978593",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Curriculum Reinforcement Learning",
    "Mathematical Reasoning Tasks",
    "Variance-based Curriculum"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Curriculum Reinforcement Learning": 0.78,
    "Mathematical Reasoning Tasks": 0.72,
    "Variance-based Curriculum": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Central to the study, linking to a broad range of LLM-related research.",
        "novelty_score": 0.25,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Curriculum Reinforcement Learning",
        "canonical": "Curriculum Reinforcement Learning",
        "aliases": [
          "VCRL"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach specific to the paper, enhancing connectivity to curriculum learning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Mathematical Reasoning Tasks",
        "canonical": "Mathematical Reasoning Tasks",
        "aliases": [
          "Math Reasoning"
        ],
        "category": "specific_connectable",
        "rationale": "Focuses on a specific application area of LLMs, useful for linking to related tasks.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      },
      {
        "surface": "Variance-based Curriculum",
        "canonical": "Variance-based Curriculum",
        "aliases": [
          "Variance Curriculum"
        ],
        "category": "unique_technical",
        "rationale": "Highlights a unique methodological innovation in the paper.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "rollout-based reinforcement learning",
      "samples",
      "difficulty levels"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.25,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Curriculum Reinforcement Learning",
      "resolved_canonical": "Curriculum Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Mathematical Reasoning Tasks",
      "resolved_canonical": "Mathematical Reasoning Tasks",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Variance-based Curriculum",
      "resolved_canonical": "Variance-based Curriculum",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# VCRL: Variance-based Curriculum Reinforcement Learning for Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19803.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19803](https://arxiv.org/abs/2509.19803)

## 🔗 유사한 논문
- [[2025-09-23/Reinforcement Learning Meets Large Language Models_ A Survey of Advancements and Applications Across the LLM Lifecycle_20250923|Reinforcement Learning Meets Large Language Models: A Survey of Advancements and Applications Across the LLM Lifecycle]] (89.1% similar)
- [[2025-09-24/Reinforcement Learning on Pre-Training Data_20250924|Reinforcement Learning on Pre-Training Data]] (88.6% similar)
- [[2025-09-23/ConfClip_ Confidence-Weighted and Clipped Reward for Reinforcement Learning in LLMs_20250923|ConfClip: Confidence-Weighted and Clipped Reward for Reinforcement Learning in LLMs]] (88.3% similar)
- [[2025-09-22/Entropy-Regularized Process Reward Model_20250922|Entropy-Regularized Process Reward Model]] (86.4% similar)
- [[2025-09-23/EvoCoT_ Overcoming the Exploration Bottleneck in Reinforcement Learning_20250923|EvoCoT: Overcoming the Exploration Bottleneck in Reinforcement Learning]] (86.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Mathematical Reasoning Tasks|Mathematical Reasoning Tasks]]
**⚡ Unique Technical**: [[keywords/Curriculum Reinforcement Learning|Curriculum Reinforcement Learning]], [[keywords/Variance-based Curriculum|Variance-based Curriculum]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19803v1 Announce Type: new 
Abstract: Policy-based reinforcement learning currently plays an important role in improving LLMs on mathematical reasoning tasks. However, existing rollout-based reinforcement learning methods (GRPO, DAPO, GSPO, etc.) fail to explicitly consider LLMs' learning ability for samples of different difficulty levels, which is contrary to the human cognitive process of mathematical reasoning tasks from easy to difficult. Intuitively, we find that the variance of the rollout group's reward in RLVR partly reflects the difficulty of the current sample for LLMs. Samples that are too easy or too difficult have a lower variance, while samples with moderate difficulty have a higher variance. Based on this, we propose VCRL, a curriculum reinforcement learning framework that dynamically controls the difficulty of training samples based on the variance of group rewards. Experiments on five mathematical benchmarks and two models reveal the advantages of VCRL over the current LLM RL baselines.

## 📝 요약

이 논문은 정책 기반 강화 학습이 수학적 추론 과제에서 대형 언어 모델(LLM)을 개선하는 데 중요한 역할을 한다고 설명합니다. 기존의 롤아웃 기반 강화 학습 방법들은 샘플의 난이도를 명시적으로 고려하지 않아 인간의 수학적 추론 과정과 다릅니다. 연구진은 롤아웃 그룹의 보상 분산이 LLM에게 샘플의 난이도를 반영한다고 보고, 이를 기반으로 VCRL이라는 커리큘럼 강화 학습 프레임워크를 제안합니다. VCRL은 그룹 보상의 분산을 활용해 훈련 샘플의 난이도를 동적으로 조절합니다. 다섯 개의 수학적 벤치마크와 두 개의 모델 실험에서 VCRL이 기존 LLM 강화 학습 기준보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 정책 기반 강화 학습은 수학적 추론 작업에서 대형 언어 모델(LLM)의 성능 향상에 중요한 역할을 한다.
- 2. 기존의 롤아웃 기반 강화 학습 방법은 샘플의 난이도를 명시적으로 고려하지 않아 인간의 수학적 추론 과정과 상반된다.
- 3. RLVR에서 롤아웃 그룹의 보상 분산은 LLM이 샘플의 난이도를 인식하는 데 일부 기여한다.
- 4. VCRL은 그룹 보상의 분산을 기반으로 훈련 샘플의 난이도를 동적으로 조절하는 커리큘럼 강화 학습 프레임워크이다.
- 5. 다섯 개의 수학적 벤치마크와 두 개의 모델 실험에서 VCRL은 기존 LLM RL 기준보다 우수한 성능을 보였다.


---

*Generated on 2025-09-25 16:40:08*