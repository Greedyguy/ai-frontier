---
keywords:
  - Multi-Agent Reinforcement Learning
  - Contextual Markov Decision Process
  - Dynamics-Aware Context
  - Non-stationarity
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15519
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:28:50.770881",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-Agent Reinforcement Learning",
    "Contextual Markov Decision Process",
    "Dynamics-Aware Context",
    "Non-stationarity"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multi-Agent Reinforcement Learning": 0.78,
    "Contextual Markov Decision Process": 0.82,
    "Dynamics-Aware Context": 0.85,
    "Non-stationarity": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multi-Agent Reinforcement Learning",
        "canonical": "Multi-Agent Reinforcement Learning",
        "aliases": [
          "MARL"
        ],
        "category": "broad_technical",
        "rationale": "This is a core concept of the paper, linking it to the broader field of reinforcement learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Contextual Markov Decision Process",
        "canonical": "Contextual Markov Decision Process",
        "aliases": [
          "CMDP"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the proposed method and represents a novel approach within the paper.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Dynamics-Aware Context",
        "canonical": "Dynamics-Aware Context",
        "aliases": [
          "DAC"
        ],
        "category": "unique_technical",
        "rationale": "DAC is the novel method introduced in the paper, crucial for understanding the proposed solution.",
        "novelty_score": 0.78,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Non-stationarity",
        "canonical": "Non-stationarity",
        "aliases": [
          "nonstationary"
        ],
        "category": "specific_connectable",
        "rationale": "Addressing non-stationarity is a key challenge in the paper, linking to broader discussions in reinforcement learning.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "value function",
      "shared rewards"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multi-Agent Reinforcement Learning",
      "resolved_canonical": "Multi-Agent Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Contextual Markov Decision Process",
      "resolved_canonical": "Contextual Markov Decision Process",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Dynamics-Aware Context",
      "resolved_canonical": "Dynamics-Aware Context",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Non-stationarity",
      "resolved_canonical": "Non-stationarity",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Fully Decentralized Cooperative Multi-Agent Reinforcement Learning is A Context Modeling Problem

**Korean Title:** 완전 탈중앙화된 협력적 다중 에이전트 강화 학습은 맥락 모델링 문제이다.

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15519.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15519](https://arxiv.org/abs/2509.15519)

## 🔗 유사한 논문
- [[2025-09-19/Constructive Conflict-Driven Multi-Agent Reinforcement Learning for Strategic Diversity_20250919|Constructive Conflict-Driven Multi-Agent Reinforcement Learning for Strategic Diversity]] (85.7% similar)
- [[2025-09-19/Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention_20250919|Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention]] (82.8% similar)
- [[2025-09-19/CRAFT_ Coaching Reinforcement Learning Autonomously using Foundation Models for Multi-Robot Coordination Tasks_20250919|CRAFT: Coaching Reinforcement Learning Autonomously using Foundation Models for Multi-Robot Coordination Tasks]] (82.7% similar)
- [[2025-09-22/Automated Cyber Defense with Generalizable Graph-based Reinforcement Learning Agents_20250922|Automated Cyber Defense with Generalizable Graph-based Reinforcement Learning Agents]] (82.7% similar)
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (82.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Multi-Agent Reinforcement Learning|Multi-Agent Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Non-stationarity|Non-stationarity]]
**⚡ Unique Technical**: [[keywords/Contextual Markov Decision Process|Contextual Markov Decision Process]], [[keywords/Dynamics-Aware Context|Dynamics-Aware Context]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15519v1 Announce Type: new 
Abstract: This paper studies fully decentralized cooperative multi-agent reinforcement learning, where each agent solely observes the states, its local actions, and the shared rewards. The inability to access other agents' actions often leads to non-stationarity during value function updates and relative overgeneralization during value function estimation, hindering effective cooperative policy learning. However, existing works fail to address both issues simultaneously, due to their inability to model the joint policy of other agents in a fully decentralized setting. To overcome this limitation, we propose a novel method named Dynamics-Aware Context (DAC), which formalizes the task, as locally perceived by each agent, as an Contextual Markov Decision Process, and further addresses both non-stationarity and relative overgeneralization through dynamics-aware context modeling. Specifically, DAC attributes the non-stationary local task dynamics of each agent to switches between unobserved contexts, each corresponding to a distinct joint policy. Then, DAC models the step-wise dynamics distribution using latent variables and refers to them as contexts. For each agent, DAC introduces a context-based value function to address the non-stationarity issue during value function update. For value function estimation, an optimistic marginal value is derived to promote the selection of cooperative actions, thereby addressing the relative overgeneralization issue. Experimentally, we evaluate DAC on various cooperative tasks (including matrix game, predator and prey, and SMAC), and its superior performance against multiple baselines validates its effectiveness.

## 🔍 Abstract (한글 번역)

arXiv:2509.15519v1 발표 유형: 신규  
초록: 본 논문은 각 에이전트가 상태, 자신의 지역적 행동, 그리고 공유된 보상만을 관찰하는 완전 분산형 협력 다중 에이전트 강화 학습을 연구한다. 다른 에이전트의 행동에 접근할 수 없는 경우, 가치 함수 업데이트 시 비정상성 및 가치 함수 추정 시 상대적 과일반화가 발생하여 효과적인 협력 정책 학습을 저해할 수 있다. 그러나 기존 연구들은 완전 분산형 설정에서 다른 에이전트의 공동 정책을 모델링할 수 없기 때문에 두 문제를 동시에 해결하지 못한다. 이러한 한계를 극복하기 위해, 우리는 Dynamics-Aware Context (DAC)라는 새로운 방법을 제안한다. 이는 각 에이전트가 로컬하게 인식하는 작업을 컨텍스트 기반 마르코프 결정 프로세스로 형식화하고, 동적 인식 컨텍스트 모델링을 통해 비정상성과 상대적 과일반화를 모두 해결한다. 구체적으로, DAC는 각 에이전트의 비정상적인 로컬 작업 동태를 관찰되지 않은 컨텍스트 간의 전환으로 귀속시키며, 각 컨텍스트는 개별적인 공동 정책에 해당한다. 그런 다음 DAC는 잠재 변수를 사용하여 단계별 동태 분포를 모델링하고 이를 컨텍스트라고 한다. 각 에이전트에 대해, DAC는 가치 함수 업데이트 시 비정상성 문제를 해결하기 위해 컨텍스트 기반 가치 함수를 도입한다. 가치 함수 추정 시, 협력적 행동 선택을 촉진하기 위해 낙관적인 한계 가치를 도출하여 상대적 과일반화 문제를 해결한다. 실험적으로, 우리는 다양한 협력 작업(행렬 게임, 포식자와 먹이, SMAC 포함)에서 DAC를 평가하였으며, 여러 기준선 대비 우수한 성능은 그 효과성을 입증한다.

## 📝 요약

이 논문은 완전 분산형 협력 다중 에이전트 강화 학습을 연구합니다. 각 에이전트는 상태, 로컬 행동, 공유 보상만을 관찰하며, 다른 에이전트의 행동에 접근할 수 없어 비정상성과 상대적 과일반화 문제가 발생합니다. 기존 연구는 이러한 문제를 동시에 해결하지 못했으나, 본 연구에서는 Dynamics-Aware Context (DAC)라는 새로운 방법을 제안합니다. DAC는 각 에이전트가 인지하는 과제를 문맥적 마르코프 결정 과정으로 공식화하고, 비정상성과 상대적 과일반화를 해결합니다. DAC는 숨겨진 문맥 전환을 통해 비정상성을 해결하고, 문맥 기반 가치 함수를 도입하여 협력적 행동을 촉진합니다. 다양한 협력 과제에서 DAC의 우수한 성능이 입증되었습니다.

## 🎯 주요 포인트

- 1. 본 논문은 각 에이전트가 상태, 지역적 행동, 공유 보상만을 관측하는 완전 분산형 협력 다중 에이전트 강화 학습을 연구합니다.
- 2. 기존 방법들은 완전 분산형 환경에서 다른 에이전트의 공동 정책을 모델링할 수 없어 비정상성과 상대적 과일반화 문제를 동시에 해결하지 못합니다.
- 3. 제안된 Dynamics-Aware Context (DAC) 방법은 비정상성과 상대적 과일반화 문제를 해결하기 위해 동적 인식 컨텍스트 모델링을 사용합니다.
- 4. DAC는 숨겨진 컨텍스트 간 전환을 통해 비정상적인 지역적 과업 동태를 설명하고, 각 에이전트에 대해 컨텍스트 기반 가치 함수를 도입하여 비정상성 문제를 해결합니다.
- 5. DAC는 다양한 협력 과제에서 실험적으로 평가되었으며, 여러 기준선 대비 우수한 성능을 보여 그 효과성을 입증합니다.


---

*Generated on 2025-09-23 10:28:50*