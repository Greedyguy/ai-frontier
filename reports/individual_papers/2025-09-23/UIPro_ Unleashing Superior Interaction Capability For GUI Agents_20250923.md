---
keywords:
  - Graphical User Interface Agents
  - Vision-Language Model
  - Unified Action Space
  - Multi-Platform GUI Interaction
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17328
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:49:01.164255",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graphical User Interface Agents",
    "Vision-Language Model",
    "Unified Action Space",
    "Multi-Platform GUI Interaction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graphical User Interface Agents": 0.78,
    "Vision-Language Model": 0.82,
    "Unified Action Space": 0.77,
    "Multi-Platform GUI Interaction": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "GUI Agents",
        "canonical": "Graphical User Interface Agents",
        "aliases": [
          "GUI Agents",
          "GUI Interaction Agents"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus on developing agents that interact with GUIs, making it a unique technical concept.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLMs",
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "This concept is crucial for understanding the multi-modal comprehension ability discussed in the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Unified Action Space",
        "canonical": "Unified Action Space",
        "aliases": [
          "Harmonized Action Space"
        ],
        "category": "unique_technical",
        "rationale": "This concept is key to resolving issues with heterogeneous action spaces in GUI agents.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Multi-Platform GUI Interaction",
        "canonical": "Multi-Platform GUI Interaction",
        "aliases": [
          "Cross-Platform GUI Interaction"
        ],
        "category": "unique_technical",
        "rationale": "This term highlights the paper's focus on generalist agents capable of operating across multiple platforms.",
        "novelty_score": 0.7,
        "connectivity_score": 0.67,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "GUI Agents",
      "resolved_canonical": "Graphical User Interface Agents",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Unified Action Space",
      "resolved_canonical": "Unified Action Space",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Multi-Platform GUI Interaction",
      "resolved_canonical": "Multi-Platform GUI Interaction",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.67,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# UIPro: Unleashing Superior Interaction Capability For GUI Agents

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17328.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17328](https://arxiv.org/abs/2509.17328)

## 🔗 유사한 논문
- [[2025-09-23/Mano Report_20250923|Mano Report]] (88.3% similar)
- [[2025-09-22/GUI-ReWalk_ Massive Data Generation for GUI Agent via Stochastic Exploration and Intent-Aware Reasoning_20250922|GUI-ReWalk: Massive Data Generation for GUI Agent via Stochastic Exploration and Intent-Aware Reasoning]] (87.1% similar)
- [[2025-09-22/GUI-ARP_ Enhancing Grounding with Adaptive Region Perception for GUI Agents_20250922|GUI-ARP: Enhancing Grounding with Adaptive Region Perception for GUI Agents]] (86.8% similar)
- [[2025-09-22/BTL-UI_ Blink-Think-Link Reasoning Model for GUI Agent_20250922|BTL-UI: Blink-Think-Link Reasoning Model for GUI Agent]] (84.7% similar)
- [[2025-09-23/Orcust_ Stepwise-Feedback Reinforcement Learning for GUI Agent_20250923|Orcust: Stepwise-Feedback Reinforcement Learning for GUI Agent]] (83.8% similar)

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Graphical User Interface Agents|Graphical User Interface Agents]], [[keywords/Unified Action Space|Unified Action Space]], [[keywords/Multi-Platform GUI Interaction|Multi-Platform GUI Interaction]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17328v1 Announce Type: new 
Abstract: Building autonomous agents that perceive and operate graphical user interfaces (GUIs) like humans has long been a vision in the field of artificial intelligence. Central to these agents is the capability for GUI interaction, which involves GUI understanding and planning capabilities. Existing methods have tried developing GUI agents based on the multi-modal comprehension ability of vision-language models (VLMs). However, the limited scenario, insufficient size, and heterogeneous action spaces hinder the progress of building generalist GUI agents. To resolve these issues, this paper proposes \textbf{UIPro}, a novel generalist GUI agent trained with extensive multi-platform and multi-task GUI interaction data, coupled with a unified action space. We first curate a comprehensive dataset encompassing 20.6 million GUI understanding tasks to pre-train UIPro, granting it a strong GUI grounding capability, which is key to downstream GUI agent tasks. Subsequently, we establish a unified action space to harmonize heterogeneous GUI agent task datasets and produce a merged dataset to foster the action prediction ability of UIPro via continued fine-tuning. Experimental results demonstrate UIPro's superior performance across multiple GUI task benchmarks on various platforms, highlighting the effectiveness of our approach.

## 📝 요약

이 논문은 인간처럼 그래픽 사용자 인터페이스(GUI)를 인식하고 조작할 수 있는 자율 에이전트를 개발하는 것을 목표로 합니다. 기존 방법들은 비전-언어 모델(VLMs)의 다중 모달 이해 능력을 기반으로 GUI 에이전트를 개발하려 했으나, 제한된 시나리오와 이질적인 행동 공간 때문에 한계가 있었습니다. 이를 해결하기 위해, 본 논문에서는 다양한 플랫폼과 작업에서 GUI 상호작용 데이터를 활용하여 훈련된 새로운 일반 GUI 에이전트인 UIPro를 제안합니다. 20.6백만 개의 GUI 이해 작업을 포함한 데이터셋으로 UIPro를 사전 훈련하여 강력한 GUI 기반 능력을 부여하고, 통합된 행동 공간을 통해 이질적인 GUI 에이전트 작업 데이터셋을 조화시켰습니다. 실험 결과, UIPro는 여러 플랫폼에서 다양한 GUI 작업 벤치마크에서 우수한 성능을 보이며, 제안된 접근 방식의 효과를 입증했습니다.

## 🎯 주요 포인트

- 1. UIPro는 다양한 플랫폼과 작업에서 GUI 상호작용 데이터를 활용하여 훈련된 일반적인 GUI 에이전트입니다.
- 2. 20.6백만 개의 GUI 이해 작업을 포함한 포괄적인 데이터셋을 통해 UIPro를 사전 훈련하여 강력한 GUI 기반 능력을 부여했습니다.
- 3. 이질적인 GUI 에이전트 작업 데이터셋을 통합하기 위해 통합된 액션 공간을 설정하고, 이를 통해 UIPro의 액션 예측 능력을 강화했습니다.
- 4. 실험 결과, UIPro는 여러 GUI 작업 벤치마크에서 우수한 성능을 보여주며 제안된 접근 방식의 효과를 입증했습니다.


---

*Generated on 2025-09-24 04:49:01*