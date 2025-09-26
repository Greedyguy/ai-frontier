<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:29:09.689763",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Mixed Advantage Policy Optimization",
    "Group Relative Policy Optimization",
    "Reinforcement Learning",
    "Advantage Function"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Mixed Advantage Policy Optimization": 0.78,
    "Group Relative Policy Optimization": 0.7,
    "Reinforcement Learning": 0.8,
    "Advantage Function": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Mixed Advantage Policy Optimization",
        "canonical": "Mixed Advantage Policy Optimization",
        "aliases": [
          "MAPO"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel strategy in reinforcement learning that addresses specific problems in advantage allocation.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Group Relative Policy Optimization",
        "canonical": "Group Relative Policy Optimization",
        "aliases": [
          "GRPO"
        ],
        "category": "unique_technical",
        "rationale": "Serves as a foundational concept that MAPO builds upon, facilitating understanding of the new method's context.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "A core area of study relevant to the paper's contributions, providing a broad context for the research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "Advantage Function",
        "canonical": "Advantage Function",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Central to the paper's methodology, it is crucial for understanding the proposed optimization strategy.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "trajectory",
      "samples",
      "certainty"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Mixed Advantage Policy Optimization",
      "resolved_canonical": "Mixed Advantage Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Group Relative Policy Optimization",
      "resolved_canonical": "Group Relative Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Advantage Function",
      "resolved_canonical": "Advantage Function",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# MAPO: Mixed Advantage Policy Optimization

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18849.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18849](https://arxiv.org/abs/2509.18849)

## 🔗 유사한 논문
- [[2025-09-22/PVPO_ Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning_20250922|PVPO: Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning]] (86.3% similar)
- [[2025-09-23/GRPO-LEAD_ A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models_20250923|GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models]] (85.3% similar)
- [[2025-09-23/From Uniform to Heterogeneous_ Tailoring Policy Optimization to Every Token's Nature_20250923|From Uniform to Heterogeneous: Tailoring Policy Optimization to Every Token's Nature]] (85.1% similar)
- [[2025-09-19/Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (84.7% similar)
- [[2025-09-23/GPO_ Learning from Critical Steps to Improve LLM Reasoning_20250923|GPO: Learning from Critical Steps to Improve LLM Reasoning]] (84.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Advantage Function|Advantage Function]]
**⚡ Unique Technical**: [[keywords/Mixed Advantage Policy Optimization|Mixed Advantage Policy Optimization]], [[keywords/Group Relative Policy Optimization|Group Relative Policy Optimization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18849v1 Announce Type: new 
Abstract: Recent advances in reinforcement learning for foundation models, such as Group Relative Policy Optimization (GRPO), have significantly improved the performance of foundation models on reasoning tasks. Notably, the advantage function serves as a central mechanism in GRPO for ranking the trajectory importance. However, existing explorations encounter both advantage reversion and advantage mirror problems, which hinder the reasonable advantage allocation across different query samples. In this work, we propose an easy but effective GRPO strategy, Mixed Advantage Policy Optimization (MAPO). We reveal that the trajectory appears with different certainty and propose the advantage percent deviation for samples with high-certainty trajectories. Furthermore, we dynamically reweight the advantage function for samples with varying trajectory certainty, thereby adaptively configuring the advantage function to account for sample-specific characteristics. Comparison with related state-of-the-art methods, along with ablation studies on different advantage variants, validates the effectiveness of our approach.

## 📝 요약

최근 강화 학습의 발전은 Group Relative Policy Optimization (GRPO)와 같은 기초 모델의 성능을 크게 향상시켰습니다. 그러나 기존 방법들은 이점 역전 및 이점 미러 문제로 인해 쿼리 샘플 간의 적절한 이점 할당에 어려움을 겪고 있습니다. 본 연구에서는 Mixed Advantage Policy Optimization (MAPO)라는 간단하지만 효과적인 GRPO 전략을 제안합니다. 우리는 경로의 확실성이 다르게 나타남을 발견하고, 높은 확실성을 가진 샘플에 대해 이점 백분율 편차를 제안합니다. 또한, 샘플의 경로 확실성에 따라 이점 함수를 동적으로 재조정하여 샘플 특성에 맞게 적응적으로 구성합니다. 관련 최신 방법들과의 비교 및 다양한 이점 변형에 대한 소거 연구를 통해 제안한 방법의 효과를 검증했습니다.

## 🎯 주요 포인트

- 1. GRPO는 기초 모델의 추론 작업 성능을 크게 향상시켰지만, 이점 역전 및 이점 미러 문제로 인해 쿼리 샘플 간의 합리적인 이점 할당이 방해받고 있습니다.
- 2. 본 연구에서는 간단하지만 효과적인 GRPO 전략인 혼합 이점 정책 최적화(MAPO)를 제안합니다.
- 3. 우리는 경로가 다른 확실성을 가지고 나타난다는 것을 밝혀내고, 높은 확실성 경로를 가진 샘플에 대한 이점 백분율 편차를 제안합니다.
- 4. 샘플의 경로 확실성에 따라 이점 함수를 동적으로 재조정하여 샘플별 특성을 고려한 적응형 이점 함수를 구성합니다.
- 5. 관련 최첨단 방법과의 비교 및 다양한 이점 변형에 대한 소거 연구를 통해 우리의 접근 방식의 효과가 입증되었습니다.


---

*Generated on 2025-09-24 13:29:09*