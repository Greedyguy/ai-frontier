---
keywords:
  - Large Language Model
  - Multi-Agent System
  - Adversarial Sample
  - M-Spoiler Framework
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16494
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:22:19.081152",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Multi-Agent System",
    "Adversarial Sample",
    "M-Spoiler Framework"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.8,
    "Multi-Agent System": 0.82,
    "Adversarial Sample": 0.78,
    "M-Spoiler Framework": 0.85
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the study and are a key concept in understanding the manipulation of multi-agent systems.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "multi-agent systems",
        "canonical": "Multi-Agent System",
        "aliases": [
          "MAS"
        ],
        "category": "unique_technical",
        "rationale": "The concept of multi-agent systems is crucial for linking studies on collaborative decision-making and adversarial attacks.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "adversarial samples",
        "canonical": "Adversarial Sample",
        "aliases": [
          "adversarial examples"
        ],
        "category": "specific_connectable",
        "rationale": "Adversarial samples are a key focus of the paper, linking to broader discussions on system vulnerabilities.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "M-Spoiler",
        "canonical": "M-Spoiler Framework",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "M-Spoiler is a novel framework introduced in the paper, central to the proposed methodology.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      }
    ],
    "ban_list_suggestions": [
      "individual",
      "system",
      "framework"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "multi-agent systems",
      "resolved_canonical": "Multi-Agent System",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "adversarial samples",
      "resolved_canonical": "Adversarial Sample",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "M-Spoiler",
      "resolved_canonical": "M-Spoiler Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    }
  ]
}
-->

# Can an Individual Manipulate the Collective Decisions of Multi-Agents?

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16494.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16494](https://arxiv.org/abs/2509.16494)

## 🔗 유사한 논문
- [[2025-09-19/A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks_20250919|A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks]] (87.0% similar)
- [[2025-09-19/The Sum Leaks More Than Its Parts_ Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration_20250919|The Sum Leaks More Than Its Parts: Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration]] (85.0% similar)
- [[2025-09-19/Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models: Multi-Agent Consensus Alignment]] (83.3% similar)
- [[2025-09-19/Enterprise AI Must Enforce Participant-Aware Access Control_20250919|Enterprise AI Must Enforce Participant-Aware Access Control]] (83.3% similar)
- [[2025-09-18/MUSE_ MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety in Large Language Models_20250918|MUSE: MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety in Large Language Models]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Adversarial Sample|Adversarial Sample]]
**⚡ Unique Technical**: [[keywords/Multi-Agent System|Multi-Agent System]], [[keywords/M-Spoiler Framework|M-Spoiler Framework]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16494v1 Announce Type: cross 
Abstract: Individual Large Language Models (LLMs) have demonstrated significant capabilities across various domains, such as healthcare and law. Recent studies also show that coordinated multi-agent systems exhibit enhanced decision-making and reasoning abilities through collaboration. However, due to the vulnerabilities of individual LLMs and the difficulty of accessing all agents in a multi-agent system, a key question arises: If attackers only know one agent, could they still generate adversarial samples capable of misleading the collective decision? To explore this question, we formulate it as a game with incomplete information, where attackers know only one target agent and lack knowledge of the other agents in the system. With this formulation, we propose M-Spoiler, a framework that simulates agent interactions within a multi-agent system to generate adversarial samples. These samples are then used to manipulate the target agent in the target system, misleading the system's collaborative decision-making process. More specifically, M-Spoiler introduces a stubborn agent that actively aids in optimizing adversarial samples by simulating potential stubborn responses from agents in the target system. This enhances the effectiveness of the generated adversarial samples in misleading the system. Through extensive experiments across various tasks, our findings confirm the risks posed by the knowledge of an individual agent in multi-agent systems and demonstrate the effectiveness of our framework. We also explore several defense mechanisms, showing that our proposed attack framework remains more potent than baselines, underscoring the need for further research into defensive strategies.

## 📝 요약

개별 대형 언어 모델(LLM)은 다양한 분야에서 뛰어난 능력을 보이지만, 협력적 다중 에이전트 시스템은 더욱 향상된 의사결정 및 추론 능력을 나타냅니다. 본 연구는 공격자가 단일 에이전트만 알고 있을 때도 다중 에이전트 시스템의 결정을 오도할 수 있는지를 게임 이론을 통해 탐구합니다. 이를 위해 M-Spoiler라는 프레임워크를 제안하여, 에이전트 간 상호작용을 시뮬레이션하고 적대적 샘플을 생성하여 시스템의 협력적 의사결정을 방해합니다. 특히, 고집스러운 에이전트를 도입해 적대적 샘플의 효과성을 높였습니다. 다양한 실험을 통해 개별 에이전트의 정보가 시스템에 미치는 위험성을 확인하고, 제안된 공격 프레임워크의 효율성을 입증했습니다. 또한, 방어 메커니즘을 탐구하여 추가 연구의 필요성을 강조했습니다.

## 🎯 주요 포인트

- 1. 개별 대형 언어 모델(LLM)은 다양한 분야에서 뛰어난 능력을 보여주고 있으며, 협력적인 다중 에이전트 시스템은 향상된 의사 결정 및 추론 능력을 발휘한다.
- 2. 공격자가 단일 에이전트만 알고 있어도 집단적인 의사 결정을 오도할 수 있는 적대적 샘플을 생성할 수 있는지에 대한 문제가 제기된다.
- 3. M-Spoiler는 다중 에이전트 시스템 내 에이전트 상호작용을 시뮬레이션하여 적대적 샘플을 생성하고, 이를 통해 시스템의 협력적 의사 결정 과정을 오도한다.
- 4. M-Spoiler는 고집스러운 에이전트를 도입하여 대상 시스템의 에이전트의 잠재적 고집스러운 반응을 시뮬레이션함으로써 적대적 샘플의 효과를 극대화한다.
- 5. 다양한 실험을 통해 개별 에이전트의 지식이 다중 에이전트 시스템에 미치는 위험을 확인하고, 제안된 공격 프레임워크의 효과를 입증하며, 방어 전략에 대한 추가 연구의 필요성을 강조한다.


---

*Generated on 2025-09-23 23:22:19*