---
keywords:
  - Reinforcement Learning
  - Mixed Proximal Policy Optimization
  - Diverse Play Styles
  - Evolutionary Algorithms
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2506.16995
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:28:00.080980",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Mixed Proximal Policy Optimization",
    "Diverse Play Styles",
    "Evolutionary Algorithms"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Reinforcement Learning": 0.8,
    "Mixed Proximal Policy Optimization": 0.85,
    "Diverse Play Styles": 0.78,
    "Evolutionary Algorithms": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "reinforcement learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is a foundational technique in game AI, providing strong connectivity with existing literature.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "Mixed Proximal Policy Optimization",
        "canonical": "Mixed Proximal Policy Optimization",
        "aliases": [
          "MPPO"
        ],
        "category": "unique_technical",
        "rationale": "MPPO is a novel approach introduced in this paper, crucial for connecting discussions on style-preserving optimization.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.85
      },
      {
        "surface": "diverse play styles",
        "canonical": "Diverse Play Styles",
        "aliases": [
          "play style diversity"
        ],
        "category": "specific_connectable",
        "rationale": "Diverse Play Styles are central to the paper's contribution, linking to broader discussions on agent behavior.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "evolution algorithms",
        "canonical": "Evolutionary Algorithms",
        "aliases": [
          "evolutionary methods"
        ],
        "category": "specific_connectable",
        "rationale": "Evolutionary Algorithms provide a contrasting approach to RL, enhancing connectivity with optimization techniques.",
        "novelty_score": 0.4,
        "connectivity_score": 0.8,
        "specificity_score": 0.68,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "proficiency",
      "gaming experience",
      "empirical results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "reinforcement learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Mixed Proximal Policy Optimization",
      "resolved_canonical": "Mixed Proximal Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "diverse play styles",
      "resolved_canonical": "Diverse Play Styles",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "evolution algorithms",
      "resolved_canonical": "Evolutionary Algorithms",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.8,
        "specificity": 0.68,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Style-Preserving Policy Optimization for Game Agents

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.16995.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2506.16995](https://arxiv.org/abs/2506.16995)

## 🔗 유사한 논문
- [[2025-09-19/Reinforcement Learning Agent for a 2D Shooter Game_20250919|Reinforcement Learning Agent for a 2D Shooter Game]] (85.3% similar)
- [[2025-09-18/$Agent^2$_ An Agent-Generates-Agent Framework for Reinforcement Learning Automation_20250918|$Agent^2$: An Agent-Generates-Agent Framework for Reinforcement Learning Automation]] (83.1% similar)
- [[2025-09-22/PVPO_ Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning_20250922|PVPO: Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning]] (82.7% similar)
- [[2025-09-19/Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (81.7% similar)
- [[2025-09-19/Beyond the high score_ Prosocial ability profiles of multi-agent populations_20250919|Beyond the high score: Prosocial ability profiles of multi-agent populations]] (81.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Diverse Play Styles|Diverse Play Styles]], [[keywords/Evolutionary Algorithms|Evolutionary Algorithms]]
**⚡ Unique Technical**: [[keywords/Mixed Proximal Policy Optimization|Mixed Proximal Policy Optimization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.16995v3 Announce Type: replace 
Abstract: Proficient game agents with diverse play styles enrich the gaming experience and enhance the replay value of games. However, recent advancements in game AI based on reinforcement learning have predominantly focused on improving proficiency, whereas methods based on evolution algorithms generate agents with diverse play styles but exhibit subpar performance compared to RL methods. To address this gap, this paper proposes Mixed Proximal Policy Optimization (MPPO), a method designed to improve the proficiency of existing suboptimal agents while retaining their distinct styles. MPPO unifies loss objectives for both online and offline samples and introduces an implicit constraint to approximate demonstrator policies by adjusting the empirical distribution of samples. Empirical results across environments of varying scales demonstrate that MPPO achieves proficiency levels comparable to, or even superior to, pure online algorithms while preserving demonstrators' play styles. This work presents an effective approach for generating highly proficient and diverse game agents, ultimately contributing to more engaging gameplay experiences.

## 📝 요약

이 논문은 게임 AI에서 다양한 플레이 스타일을 가진 에이전트를 생성하는 방법을 제안합니다. 기존의 강화 학습은 주로 능력 향상에 중점을 두었고, 진화 알고리즘은 다양한 스타일을 생성하지만 성능이 낮았습니다. 이를 해결하기 위해, 이 논문은 Mixed Proximal Policy Optimization (MPPO) 방법을 제안하여 기존의 최적이 아닌 에이전트의 능력을 향상시키면서도 그들의 고유한 스타일을 유지합니다. MPPO는 온라인 및 오프라인 샘플의 손실 목표를 통합하고, 샘플의 경험적 분포를 조정하여 시연자 정책을 근사하는 암묵적 제약을 도입합니다. 실험 결과, MPPO는 다양한 환경에서 순수 온라인 알고리즘과 동등하거나 더 높은 수준의 능력을 달성하면서도 시연자의 플레이 스타일을 보존하는 것으로 나타났습니다. 이 연구는 능력 있고 다양한 게임 에이전트를 생성하는 효과적인 접근법을 제시하여 게임 플레이 경험을 더욱 풍부하게 만듭니다.

## 🎯 주요 포인트

- 1. 최근 게임 AI는 주로 강화 학습을 통해 능력을 향상시키는 데 중점을 두었으나, 다양한 플레이 스타일을 생성하는 진화 알고리즘 기반 방법은 성능이 낮았다.
- 2. 본 논문은 Mixed Proximal Policy Optimization (MPPO)을 제안하여 기존의 최적화되지 않은 에이전트의 능력을 향상시키면서도 그들의 독특한 스타일을 유지한다.
- 3. MPPO는 온라인 및 오프라인 샘플에 대한 손실 목표를 통합하고, 샘플의 경험적 분포를 조정하여 시연자 정책을 근사하는 암시적 제약을 도입한다.
- 4. 다양한 규모의 환경에서 실험 결과, MPPO는 순수 온라인 알고리즘과 비교하여 동등하거나 더 우수한 능력 수준을 달성하면서도 시연자의 플레이 스타일을 보존한다.
- 5. 이 연구는 높은 능력과 다양한 게임 에이전트를 생성하는 효과적인 접근법을 제시하여, 보다 몰입감 있는 게임 플레이 경험에 기여한다.


---

*Generated on 2025-09-24 00:28:00*