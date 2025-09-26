---
keywords:
  - General User Model
  - Multimodal Learning
  - Proactive Assistants
  - Human-Computer Interaction
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2505.10831
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:57:49.600645",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "General User Model",
    "Multimodal Learning",
    "Proactive Assistants",
    "Human-Computer Interaction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "General User Model": 0.8,
    "Multimodal Learning": 0.78,
    "Proactive Assistants": 0.75,
    "Human-Computer Interaction": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "General User Model",
        "canonical": "General User Model",
        "aliases": [
          "GUM"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and represents a novel approach to user modeling.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multimodal Observations",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal learning is a trending area that connects well with the paper's focus on diverse data inputs.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Proactive Assistants",
        "canonical": "Proactive Assistants",
        "aliases": [
          "GUMBOs"
        ],
        "category": "unique_technical",
        "rationale": "Proactive assistants represent a specific application of the GUM architecture, highlighting its practical use.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Human-Computer Interaction",
        "canonical": "Human-Computer Interaction",
        "aliases": [
          "HCI"
        ],
        "category": "broad_technical",
        "rationale": "HCI is a foundational field relevant to the paper's exploration of user models.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
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
      "candidate_surface": "General User Model",
      "resolved_canonical": "General User Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multimodal Observations",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Proactive Assistants",
      "resolved_canonical": "Proactive Assistants",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Human-Computer Interaction",
      "resolved_canonical": "Human-Computer Interaction",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Creating General User Models from Computer Use

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.10831.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2505.10831](https://arxiv.org/abs/2505.10831)

## 🔗 유사한 논문
- [[2025-09-22/Subjective Behaviors and Preferences in LLM_ Language of Browsing_20250922|Subjective Behaviors and Preferences in LLM: Language of Browsing]] (78.4% similar)
- [[2025-09-22/BTL-UI_ Blink-Think-Link Reasoning Model for GUI Agent_20250922|BTL-UI: Blink-Think-Link Reasoning Model for GUI Agent]] (78.4% similar)
- [[2025-09-22/UniGist_ Towards General and Hardware-aligned Sequence-level Long Context Compression_20250922|UniGist: Towards General and Hardware-aligned Sequence-level Long Context Compression]] (78.2% similar)
- [[2025-09-22/MMAPG_ A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs_20250922|MMAPG: A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs]] (78.2% similar)
- [[2025-09-22/How do Language Models Generate Slang_ A Systematic Comparison between Human and Machine-Generated Slang Usages_20250922|How do Language Models Generate Slang: A Systematic Comparison between Human and Machine-Generated Slang Usages]] (78.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Human-Computer Interaction|Human-Computer Interaction]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/General User Model|General User Model]], [[keywords/Proactive Assistants|Proactive Assistants]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.10831v3 Announce Type: replace-cross 
Abstract: Human-computer interaction has long imagined technology that understands us-from our preferences and habits, to the timing and purpose of our everyday actions. Yet current user models remain fragmented, narrowly tailored to specific apps, and incapable of the flexible reasoning required to fulfill these visions. This paper presents an architecture for a general user model (GUM) that learns about you by observing any interaction you have with your computer. The GUM takes as input any unstructured observation of a user (e.g., device screenshots) and constructs confidence-weighted propositions that capture user knowledge and preferences. GUMs can infer that a user is preparing for a wedding they're attending from messages with a friend. Or recognize that a user is struggling with a collaborator's feedback on a draft by observing multiple stalled edits and a switch to reading related work. GUMs introduce an architecture that infers new propositions about a user from multimodal observations, retrieves related propositions for context, and continuously revises existing propositions. To illustrate the breadth of applications that GUMs enable, we demonstrate how they augment chat-based assistants with context, manage OS notifications to selectively surface important information, and enable interactive agents that adapt to preferences across apps. We also instantiate proactive assistants (GUMBOs) that discover and execute useful suggestions on a user's behalf using their GUM. In our evaluations, we find that GUMs make calibrated and accurate inferences about users, and that assistants built on GUMs proactively identify and perform actions that users wouldn't think to request explicitly. Altogether, GUMs introduce methods that leverage multimodal models to understand unstructured context, enabling long-standing visions of HCI and entirely new interactive systems that anticipate user needs.

## 📝 요약

이 논문은 사용자의 컴퓨터 상호작용을 관찰하여 사용자에 대한 일반 사용자 모델(GUM)을 구축하는 아키텍처를 제안합니다. GUM은 비구조화된 사용자 관찰 데이터를 입력으로 받아 사용자 지식과 선호도를 캡처하는 명제를 생성합니다. 이를 통해 사용자가 친구와의 메시지를 통해 결혼식 준비 중임을 추론하거나, 협업자의 피드백에 어려움을 겪고 있음을 인식할 수 있습니다. GUM은 다중 모달 관찰을 통해 새로운 명제를 추론하고, 관련 명제를 검색하여 맥락을 제공하며, 기존 명제를 지속적으로 수정합니다. 이를 통해 GUM은 채팅 기반 비서에 맥락을 추가하고, 운영체제 알림을 관리하며, 앱 전반에 걸쳐 사용자 선호에 맞게 적응하는 인터랙티브 에이전트를 가능하게 합니다. 평가 결과, GUM은 사용자의 행동을 정확히 추론하며, GUM 기반 비서는 사용자가 명시적으로 요청하지 않은 유용한 제안을 발견하고 실행할 수 있음을 보여줍니다. GUM은 비구조화된 맥락을 이해하기 위해 다중 모달 모델을 활용하는 방법을 제시하여, 인간-컴퓨터 상호작용의 오랜 비전을 실현하고 새로운 인터랙티브 시스템을 가능하게 합니다.

## 🎯 주요 포인트

- 1. 일반 사용자 모델(GUM)은 사용자의 모든 컴퓨터 상호작용을 관찰하여 사용자에 대한 지식과 선호도를 학습합니다.
- 2. GUM은 사용자의 메시지나 작업 패턴을 통해 사용자의 현재 상황이나 감정을 추론할 수 있습니다.
- 3. GUM은 다중 모드 관찰을 통해 새로운 사용자 정보를 추론하고, 관련 정보를 검색하여 문맥을 제공하며, 기존 정보를 지속적으로 수정합니다.
- 4. GUM 기반의 비서 시스템은 사용자가 명시적으로 요청하지 않은 작업을 선제적으로 식별하고 수행할 수 있습니다.
- 5. GUM은 비구조화된 문맥을 이해하기 위해 다중 모드 모델을 활용하여 HCI의 오랜 비전을 실현하고 새로운 상호작용 시스템을 가능하게 합니다.


---

*Generated on 2025-09-24 00:57:49*