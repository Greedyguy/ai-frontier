---
keywords:
  - Vision-Language Model
  - Visual Grounding
  - Backdoor Attack
  - Stealthy Visual Triggers
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2507.06899
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:30:39.978853",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Visual Grounding",
    "Backdoor Attack",
    "Stealthy Visual Triggers"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "Visual Grounding": 0.78,
    "Backdoor Attack": 0.82,
    "Stealthy Visual Triggers": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "LVLMs"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are central to the paper's discussion on GUI agents and their vulnerabilities.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.85
      },
      {
        "surface": "Visual Grounding",
        "canonical": "Visual Grounding",
        "aliases": [
          "Visual Mapping"
        ],
        "category": "unique_technical",
        "rationale": "Visual Grounding is a key concept in understanding how backdoor attacks manipulate GUI agents.",
        "novelty_score": 0.75,
        "connectivity_score": 0.67,
        "specificity_score": 0.81,
        "link_intent_score": 0.78
      },
      {
        "surface": "Backdoor Attack",
        "canonical": "Backdoor Attack",
        "aliases": [
          "Trojan Attack"
        ],
        "category": "specific_connectable",
        "rationale": "Backdoor attacks are a primary threat discussed in the context of GUI agents.",
        "novelty_score": 0.52,
        "connectivity_score": 0.79,
        "specificity_score": 0.76,
        "link_intent_score": 0.82
      },
      {
        "surface": "Stealthy Visual Triggers",
        "canonical": "Stealthy Visual Triggers",
        "aliases": [
          "Invisible Triggers"
        ],
        "category": "unique_technical",
        "rationale": "These triggers are crucial for understanding the stealth aspect of the proposed attack method.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "empirical results",
      "security concerns"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Visual Grounding",
      "resolved_canonical": "Visual Grounding",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.67,
        "specificity": 0.81,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Backdoor Attack",
      "resolved_canonical": "Backdoor Attack",
      "decision": "linked",
      "scores": {
        "novelty": 0.52,
        "connectivity": 0.79,
        "specificity": 0.76,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Stealthy Visual Triggers",
      "resolved_canonical": "Stealthy Visual Triggers",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# VisualTrap: A Stealthy Backdoor Attack on GUI Agents via Visual Grounding Manipulation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2507.06899.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2507.06899](https://arxiv.org/abs/2507.06899)

## 🔗 유사한 논문
- [[2025-09-24/Backdoor Attack with Invisible Triggers Based on Model Architecture Modification_20250924|Backdoor Attack with Invisible Triggers Based on Model Architecture Modification]] (85.8% similar)
- [[2025-09-23/Mano Report_20250923|Mano Report]] (84.3% similar)
- [[2025-09-22/GUI-ReWalk_ Massive Data Generation for GUI Agent via Stochastic Exploration and Intent-Aware Reasoning_20250922|GUI-ReWalk: Massive Data Generation for GUI Agent via Stochastic Exploration and Intent-Aware Reasoning]] (83.6% similar)
- [[2025-09-23/Neural Antidote_ Class-Wise Prompt Tuning for Purifying Backdoors in CLIP_20250923|Neural Antidote: Class-Wise Prompt Tuning for Purifying Backdoors in CLIP]] (83.4% similar)
- [[2025-09-23/Revisiting Backdoor Attacks on LLMs_ A Stealthy and Practical Poisoning Framework via Harmless Inputs_20250923|Revisiting Backdoor Attacks on LLMs: A Stealthy and Practical Poisoning Framework via Harmless Inputs]] (83.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Backdoor Attack|Backdoor Attack]]
**⚡ Unique Technical**: [[keywords/Visual Grounding|Visual Grounding]], [[keywords/Stealthy Visual Triggers|Stealthy Visual Triggers]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.06899v2 Announce Type: replace-cross 
Abstract: Graphical User Interface (GUI) agents powered by Large Vision-Language Models (LVLMs) have emerged as a revolutionary approach to automating human-machine interactions, capable of autonomously operating personal devices (e.g., mobile phones) or applications within the device to perform complex real-world tasks in a human-like manner. However, their close integration with personal devices raises significant security concerns, with many threats, including backdoor attacks, remaining largely unexplored. This work reveals that the visual grounding of GUI agent-mapping textual plans to GUI elements-can introduce vulnerabilities, enabling new types of backdoor attacks. With backdoor attack targeting visual grounding, the agent's behavior can be compromised even when given correct task-solving plans. To validate this vulnerability, we propose VisualTrap, a method that can hijack the grounding by misleading the agent to locate textual plans to trigger locations instead of the intended targets. VisualTrap uses the common method of injecting poisoned data for attacks, and does so during the pre-training of visual grounding to ensure practical feasibility of attacking. Empirical results show that VisualTrap can effectively hijack visual grounding with as little as 5% poisoned data and highly stealthy visual triggers (invisible to the human eye); and the attack can be generalized to downstream tasks, even after clean fine-tuning. Moreover, the injected trigger can remain effective across different GUI environments, e.g., being trained on mobile/web and generalizing to desktop environments. These findings underscore the urgent need for further research on backdoor attack risks in GUI agents.

## 📝 요약

이 논문은 대규모 비전-언어 모델(LVLMs)을 활용한 그래픽 사용자 인터페이스(GUI) 에이전트의 보안 취약점을 탐구합니다. GUI 에이전트는 개인 기기에서 복잡한 작업을 수행할 수 있지만, 이와 같은 통합은 백도어 공격과 같은 보안 위협을 초래할 수 있습니다. 연구에서는 GUI 요소와의 시각적 연결을 악용하여 백도어 공격을 가능하게 하는 취약점을 발견했습니다. 이를 검증하기 위해 VisualTrap이라는 방법을 제안하여, 시각적 연결을 오도하여 잘못된 위치로 연결되도록 합니다. VisualTrap은 훈련 과정에서 독성 데이터를 주입하여 공격의 실현 가능성을 높이며, 실험 결과 5%의 독성 데이터만으로도 효과적인 공격이 가능함을 보여줍니다. 이러한 공격은 모바일/웹 환경에서 훈련되어 데스크톱 환경으로도 일반화될 수 있습니다. 연구는 GUI 에이전트의 백도어 공격 위험에 대한 추가 연구의 필요성을 강조합니다.

## 🎯 주요 포인트

- 1. 대규모 비전-언어 모델(LVLMs)을 활용한 GUI 에이전트는 인간-기계 상호작용을 자동화하는 혁신적인 접근법으로 부상하고 있다.
- 2. GUI 에이전트의 개인 기기와의 밀접한 통합은 백도어 공격과 같은 보안 문제를 야기할 수 있다.
- 3. VisualTrap은 시각적 기반을 오도하여 에이전트가 잘못된 위치를 목표로 하도록 유도하는 백도어 공격 방법이다.
- 4. VisualTrap은 5%의 오염된 데이터만으로도 시각적 기반을 효과적으로 하이재킹할 수 있으며, 인간의 눈에 보이지 않는 트리거를 사용한다.
- 5. 이러한 공격은 모바일/웹 환경에서 훈련된 후 데스크톱 환경으로 일반화될 수 있어, GUI 에이전트의 백도어 공격 위험에 대한 추가 연구가 필요하다.


---

*Generated on 2025-09-25 16:30:39*