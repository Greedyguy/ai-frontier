---
keywords:
  - LLM-based Honeypot
  - LDAP Server
  - Deception Tools
  - Cybersecurity Threats
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16682
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:31:25.965260",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "LLM-based Honeypot",
    "LDAP Server",
    "Deception Tools",
    "Cybersecurity Threats"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "LLM-based Honeypot": 0.78,
    "LDAP Server": 0.77,
    "Deception Tools": 0.72,
    "Cybersecurity Threats": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "LLM-based honeypot",
        "canonical": "LLM-based Honeypot",
        "aliases": [
          "Large Language Model honeypot"
        ],
        "category": "unique_technical",
        "rationale": "This represents a novel application of LLMs in cybersecurity, enhancing deception strategies.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "LDAP server",
        "canonical": "LDAP Server",
        "aliases": [
          "Lightweight Directory Access Protocol server"
        ],
        "category": "specific_connectable",
        "rationale": "LDAP servers are critical in identity management, making them a key target for security solutions.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "deception tools",
        "canonical": "Deception Tools",
        "aliases": [
          "cyber deception tools"
        ],
        "category": "broad_technical",
        "rationale": "Deception tools are a foundational concept in cybersecurity, linking various defensive strategies.",
        "novelty_score": 0.48,
        "connectivity_score": 0.79,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      },
      {
        "surface": "cybersecurity threats",
        "canonical": "Cybersecurity Threats",
        "aliases": [
          "cyber threats"
        ],
        "category": "broad_technical",
        "rationale": "Understanding cybersecurity threats is essential for linking various security measures and responses.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
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
      "candidate_surface": "LLM-based honeypot",
      "resolved_canonical": "LLM-based Honeypot",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "LDAP server",
      "resolved_canonical": "LDAP Server",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "deception tools",
      "resolved_canonical": "Deception Tools",
      "decision": "linked",
      "scores": {
        "novelty": 0.48,
        "connectivity": 0.79,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "cybersecurity threats",
      "resolved_canonical": "Cybersecurity Threats",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Design and Development of an Intelligent LLM-based LDAP Honeypot

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16682.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16682](https://arxiv.org/abs/2509.16682)

## 🔗 유사한 논문
- [[2025-09-19/Exploit Tool Invocation Prompt for Tool Behavior Hijacking in LLM-Based Agentic System_20250919|Exploit Tool Invocation Prompt for Tool Behavior Hijacking in LLM-Based Agentic System]] (83.9% similar)
- [[2025-09-19/A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks_20250919|A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks]] (83.1% similar)
- [[2025-09-19/The Sum Leaks More Than Its Parts_ Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration_20250919|The Sum Leaks More Than Its Parts: Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration]] (82.8% similar)
- [[2025-09-19/Enterprise AI Must Enforce Participant-Aware Access Control_20250919|Enterprise AI Must Enforce Participant-Aware Access Control]] (82.8% similar)
- [[2025-09-19/From Capabilities to Performance_ Evaluating Key Functional Properties of LLM Architectures in Penetration Testing_20250919|From Capabilities to Performance: Evaluating Key Functional Properties of LLM Architectures in Penetration Testing]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deception Tools|Deception Tools]], [[keywords/Cybersecurity Threats|Cybersecurity Threats]]
**🔗 Specific Connectable**: [[keywords/LDAP Server|LDAP Server]]
**⚡ Unique Technical**: [[keywords/LLM-based Honeypot|LLM-based Honeypot]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16682v1 Announce Type: cross 
Abstract: Cybersecurity threats continue to increase, with a growing number of previously unknown attacks each year targeting both large corporations and smaller entities. This scenario demands the implementation of advanced security measures, not only to mitigate damage but also to anticipate emerging attack trends. In this context, deception tools have become a key strategy, enabling the detection, deterrence, and deception of potential attackers while facilitating the collection of information about their tactics and methods. Among these tools, honeypots have proven their value, although they have traditionally been limited by rigidity and configuration complexity, hindering their adaptability to dynamic scenarios. The rise of artificial intelligence, and particularly general-purpose Large Language Models (LLMs), is driving the development of new deception solutions capable of offering greater adaptability and ease of use. This work proposes the design and implementation of an LLM-based honeypot to simulate an LDAP server, a critical protocol present in most organizations due to its central role in identity and access management. The proposed solution aims to provide a flexible and realistic tool capable of convincingly interacting with attackers, thereby contributing to early detection and threat analysis while enhancing the defensive capabilities of infrastructures against intrusions targeting this service.

## 📝 요약

이 논문은 사이버 보안 위협이 증가하는 상황에서, 특히 대규모 기업과 소규모 조직을 대상으로 하는 새로운 공격이 늘어남에 따라 고급 보안 조치의 필요성을 강조합니다. 주요 기여는 인공지능, 특히 범용 대형 언어 모델(LLM)을 활용한 새로운 기만 도구 개발입니다. 이 도구는 유연성과 사용의 용이성을 제공하며, LDAP 서버를 시뮬레이션하는 LLM 기반 허니팟을 설계 및 구현하여 공격자와의 상호작용을 통해 위협을 조기 탐지하고 분석할 수 있도록 합니다. 이를 통해 인프라의 방어 능력을 강화하고 침입에 대한 대응력을 높이는 데 기여합니다.

## 🎯 주요 포인트

- 1. 사이버 보안 위협이 증가함에 따라 고급 보안 조치의 필요성이 강조되고 있습니다.
- 2. 기만 도구는 공격자 탐지, 억제 및 기만을 통해 공격자의 전술과 방법에 대한 정보를 수집하는 데 중요한 전략으로 자리잡고 있습니다.
- 3. 전통적인 허니팟은 유연성과 구성의 복잡성 때문에 동적 시나리오에 적응하기 어려웠습니다.
- 4. 인공지능, 특히 범용 대형 언어 모델(LLM)의 발전은 더 높은 적응성과 사용 용이성을 제공하는 새로운 기만 솔루션 개발을 촉진하고 있습니다.
- 5. 본 연구는 LLM 기반 허니팟을 설계 및 구현하여 LDAP 서버를 시뮬레이션하고, 이를 통해 공격자와의 상호작용을 통해 조기 탐지 및 위협 분석에 기여하고자 합니다.


---

*Generated on 2025-09-23 23:31:25*