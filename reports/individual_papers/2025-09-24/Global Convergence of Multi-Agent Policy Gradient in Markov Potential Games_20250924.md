<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:20:01.142464",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Markov Potential Games",
    "Potential Games",
    "Nash Equilibrium",
    "Policy Gradient"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Markov Potential Games": 0.8,
    "Potential Games": 0.75,
    "Nash Equilibrium": 0.78,
    "Policy Gradient": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Markov Potential Games",
        "canonical": "Markov Potential Games",
        "aliases": [
          "MPG"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and represents a novel extension of potential games to Markov settings.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Potential Games",
        "canonical": "Potential Games",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Potential games are a foundational concept in game theory, facilitating connections to other works on multi-agent coordination.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Nash Policies",
        "canonical": "Nash Equilibrium",
        "aliases": [
          "Nash Policies"
        ],
        "category": "specific_connectable",
        "rationale": "Nash Equilibrium is a critical concept for linking discussions on strategy stability in multi-agent systems.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Policy Gradient",
        "canonical": "Policy Gradient",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Policy gradient methods are widely used in reinforcement learning, providing strong connectivity to related literature.",
        "novelty_score": 0.2,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "multi-agent",
      "state-games"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Markov Potential Games",
      "resolved_canonical": "Markov Potential Games",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Potential Games",
      "resolved_canonical": "Potential Games",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Nash Policies",
      "resolved_canonical": "Nash Equilibrium",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Policy Gradient",
      "resolved_canonical": "Policy Gradient",
      "decision": "linked",
      "scores": {
        "novelty": 0.2,
        "connectivity": 0.88,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Global Convergence of Multi-Agent Policy Gradient in Markov Potential Games

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2106.01969.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2106.01969](https://arxiv.org/abs/2106.01969)

## 🔗 유사한 논문
- [[2025-09-24/A Generalized Bisimulation Metric of State Similarity between Markov Decision Processes_ From Theoretical Propositions to Applications_20250924|A Generalized Bisimulation Metric of State Similarity between Markov Decision Processes: From Theoretical Propositions to Applications]] (80.3% similar)
- [[2025-09-23/Style-Preserving Policy Optimization for Game Agents_20250923|Style-Preserving Policy Optimization for Game Agents]] (79.9% similar)
- [[2025-09-22/Learning in Stackelberg Mean Field Games_ A Non-Asymptotic Analysis_20250922|Learning in Stackelberg Mean Field Games: A Non-Asymptotic Analysis]] (79.3% similar)
- [[2025-09-23/Joint Optimization of Multi-Objective Reinforcement Learning with Policy Gradient Based Algorithm_20250923|Joint Optimization of Multi-Objective Reinforcement Learning with Policy Gradient Based Algorithm]] (79.3% similar)
- [[2025-09-19/Optimal Control of Markov Decision Processes for Efficiency with Linear Temporal Logic Tasks_20250919|Optimal Control of Markov Decision Processes for Efficiency with Linear Temporal Logic Tasks]] (79.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Policy Gradient|Policy Gradient]]
**🔗 Specific Connectable**: [[keywords/Potential Games|Potential Games]], [[keywords/Nash Equilibrium|Nash Equilibrium]]
**⚡ Unique Technical**: [[keywords/Markov Potential Games|Markov Potential Games]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2106.01969v4 Announce Type: replace 
Abstract: Potential games are arguably one of the most important and widely studied classes of normal form games. They define the archetypal setting of multi-agent coordination as all agent utilities are perfectly aligned with each other via a common potential function. Can this intuitive framework be transplanted in the setting of Markov Games? What are the similarities and differences between multi-agent coordination with and without state dependence? We present a novel definition of Markov Potential Games (MPG) that generalizes prior attempts at capturing complex stateful multi-agent coordination. Counter-intuitively, insights from normal-form potential games do not carry over as MPGs can consist of settings where state-games can be zero-sum games. In the opposite direction, Markov games where every state-game is a potential game are not necessarily MPGs. Nevertheless, MPGs showcase standard desirable properties such as the existence of deterministic Nash policies. In our main technical result, we prove fast convergence of independent policy gradient to Nash policies by adapting recent gradient dominance property arguments developed for single agent MDPs to multi-agent learning settings.

## 📝 요약

이 논문은 마르코프 잠재 게임(MPG)의 새로운 정의를 제시하여 상태 의존적인 다중 에이전트 조정 문제를 다룹니다. 기존의 잠재 게임 이론을 확장하여, 상태 게임이 제로섬 게임일 수 있는 경우도 포함합니다. 또한, 모든 상태 게임이 잠재 게임인 마르코프 게임이 반드시 MPG가 되는 것은 아님을 보여줍니다. MPG는 결정론적 내쉬 정책의 존재와 같은 표준적인 특성을 가지며, 주요 기술적 결과로 독립적인 정책 경사 하강법이 내쉬 정책으로 빠르게 수렴함을 증명합니다. 이는 단일 에이전트 MDP에 대한 최근의 경사 우세성 속성을 다중 에이전트 학습 환경에 적용한 것입니다.

## 🎯 주요 포인트

- 1. 잠재적 게임은 모든 에이전트의 효용이 공통의 잠재 함수로 완벽히 정렬되는 다중 에이전트 조정의 전형적인 설정을 정의합니다.
- 2. 마르코프 잠재적 게임(MPG)은 상태 의존성을 가진 복잡한 다중 에이전트 조정을 포착하려는 이전 시도를 일반화한 새로운 정의를 제시합니다.
- 3. MPG는 상태 게임이 제로섬 게임일 수 있는 설정을 포함할 수 있어 일반적인 잠재적 게임의 통찰력이 그대로 적용되지 않습니다.
- 4. 모든 상태 게임이 잠재적 게임인 마르코프 게임은 반드시 MPG가 아닙니다.
- 5. 독립적인 정책 경사 하강법이 내쉬 정책으로 빠르게 수렴함을 증명하여 다중 에이전트 학습 설정에 단일 에이전트 MDP의 최근 경사 우세 속성 논증을 적용했습니다.


---

*Generated on 2025-09-24 15:20:01*