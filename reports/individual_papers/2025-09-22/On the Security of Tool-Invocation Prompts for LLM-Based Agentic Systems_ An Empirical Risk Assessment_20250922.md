---
keywords:
  - Large Language Model Systems
  - Tool Invocation Prompt
  - Remote Code Execution
  - Denial of Service
  - TIP Exploitation Workflow
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.05755
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:11:33.707534",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model Systems",
    "Tool Invocation Prompt",
    "Remote Code Execution",
    "Denial of Service",
    "TIP Exploitation Workflow"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model Systems": 0.72,
    "Tool Invocation Prompt": 0.78,
    "Remote Code Execution": 0.79,
    "Denial of Service": 0.77,
    "TIP Exploitation Workflow": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "LLM-based agentic systems",
        "canonical": "Large Language Model Systems",
        "aliases": [
          "LLM systems",
          "agentic systems"
        ],
        "category": "broad_technical",
        "rationale": "This term connects to the broader concept of systems using large language models, relevant across various domains.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      },
      {
        "surface": "Tool Invocation Prompt",
        "canonical": "Tool Invocation Prompt",
        "aliases": [
          "TIP"
        ],
        "category": "unique_technical",
        "rationale": "A specific concept crucial for understanding security in LLM-based systems, offering unique insights.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "remote code execution",
        "canonical": "Remote Code Execution",
        "aliases": [
          "RCE"
        ],
        "category": "specific_connectable",
        "rationale": "A well-known security vulnerability, important for linking discussions on system security.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      },
      {
        "surface": "denial of service",
        "canonical": "Denial of Service",
        "aliases": [
          "DoS"
        ],
        "category": "specific_connectable",
        "rationale": "A key security threat relevant to system stability and resilience discussions.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      },
      {
        "surface": "TIP exploitation workflow",
        "canonical": "TIP Exploitation Workflow",
        "aliases": [
          "TEW"
        ],
        "category": "unique_technical",
        "rationale": "A novel concept introduced in the paper, crucial for understanding the attack vectors on TIPs.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "security",
      "system",
      "attack"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "LLM-based agentic systems",
      "resolved_canonical": "Large Language Model Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Tool Invocation Prompt",
      "resolved_canonical": "Tool Invocation Prompt",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "remote code execution",
      "resolved_canonical": "Remote Code Execution",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "denial of service",
      "resolved_canonical": "Denial of Service",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "TIP exploitation workflow",
      "resolved_canonical": "TIP Exploitation Workflow",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# On the Security of Tool-Invocation Prompts for LLM-Based Agentic Systems: An Empirical Risk Assessment

**Korean Title:** 도구 호출 프롬프트의 보안에 관한 연구: LLM 기반 에이전트 시스템을 위한 실증적 위험 평가

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.05755.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.05755](https://arxiv.org/abs/2509.05755)

## 🔗 유사한 논문
- [[2025-09-19/A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks_20250919|A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks]] (86.9% similar)
- [[2025-09-19/Enterprise AI Must Enforce Participant-Aware Access Control_20250919|Enterprise AI Must Enforce Participant-Aware Access Control]] (84.7% similar)
- [[2025-09-19/The Sum Leaks More Than Its Parts_ Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration_20250919|The Sum Leaks More Than Its Parts: Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration]] (83.2% similar)
- [[2025-09-19/From Capabilities to Performance_ Evaluating Key Functional Properties of LLM Architectures in Penetration Testing_20250919|From Capabilities to Performance: Evaluating Key Functional Properties of LLM Architectures in Penetration Testing]] (83.0% similar)
- [[2025-09-18/An LLM Agentic Approach for Legal-Critical Software_ A Case Study for Tax Prep Software_20250918|An LLM Agentic Approach for Legal-Critical Software: A Case Study for Tax Prep Software]] (82.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model Systems|Large Language Model Systems]]
**🔗 Specific Connectable**: [[keywords/Remote Code Execution|Remote Code Execution]], [[keywords/Denial of Service|Denial of Service]]
**⚡ Unique Technical**: [[keywords/Tool Invocation Prompt|Tool Invocation Prompt]], [[keywords/TIP Exploitation Workflow|TIP Exploitation Workflow]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.05755v4 Announce Type: replace-cross 
Abstract: LLM-based agentic systems leverage large language models to handle user queries, make decisions, and execute external tools for complex tasks across domains like chatbots, customer service, and software engineering. A critical component of these systems is the Tool Invocation Prompt (TIP), which defines tool interaction protocols and guides LLMs to ensure the security and correctness of tool usage. Despite its importance, TIP security has been largely overlooked. This work investigates TIP-related security risks, revealing that major LLM-based systems like Cursor, Claude Code, and others are vulnerable to attacks such as remote code execution (RCE) and denial of service (DoS). Through a systematic TIP exploitation workflow (TEW), we demonstrate external tool behavior hijacking via manipulated tool invocations. We also propose defense mechanisms to enhance TIP security in LLM-based agentic systems.

## 🔍 Abstract (한글 번역)

arXiv:2509.05755v4 발표 유형: 교차 대체  
초록: LLM 기반 에이전트 시스템은 대형 언어 모델을 활용하여 사용자 쿼리를 처리하고, 결정을 내리며, 챗봇, 고객 서비스, 소프트웨어 엔지니어링과 같은 다양한 도메인에서 복잡한 작업을 수행하기 위해 외부 도구를 실행합니다. 이러한 시스템의 중요한 구성 요소는 도구 호출 프롬프트(TIP)로, 도구 상호작용 프로토콜을 정의하고 LLM이 도구 사용의 보안성과 정확성을 보장하도록 안내합니다. 그 중요성에도 불구하고, TIP 보안은 크게 간과되어 왔습니다. 본 연구는 TIP 관련 보안 위험을 조사하여 Cursor, Claude Code 등과 같은 주요 LLM 기반 시스템이 원격 코드 실행(RCE) 및 서비스 거부(DoS)와 같은 공격에 취약하다는 것을 밝혀냅니다. 체계적인 TIP 악용 워크플로우(TEW)를 통해 조작된 도구 호출을 통한 외부 도구 동작 가로채기를 시연합니다. 또한, LLM 기반 에이전트 시스템에서 TIP 보안을 강화하기 위한 방어 메커니즘을 제안합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)을 활용한 에이전트 시스템에서의 도구 호출 프롬프트(TIP)의 보안 문제를 다룹니다. TIP는 도구와의 상호작용 프로토콜을 정의하여 LLM이 도구를 안전하고 정확하게 사용할 수 있도록 안내하는 중요한 요소입니다. 그러나 TIP의 보안은 그동안 간과되어 왔습니다. 연구 결과, 주요 LLM 기반 시스템들이 원격 코드 실행(RCE) 및 서비스 거부(DoS) 공격에 취약하다는 사실이 밝혀졌습니다. 저자들은 체계적인 TIP 악용 워크플로우(TEW)를 통해 외부 도구의 동작이 조작될 수 있음을 보여주고, 이를 방지하기 위한 방어 메커니즘을 제안합니다.

## 🎯 주요 포인트

- 1. LLM 기반 에이전트 시스템은 대형 언어 모델을 활용하여 사용자 쿼리 처리, 의사 결정 및 외부 도구 실행을 수행합니다.
- 2. 도구 호출 프롬프트(TIP)는 도구 상호작용 프로토콜을 정의하고 LLM의 도구 사용 보안 및 정확성을 안내하는 중요한 요소입니다.
- 3. 주요 LLM 기반 시스템들이 원격 코드 실행(RCE) 및 서비스 거부(DoS) 공격에 취약하다는 사실이 밝혀졌습니다.
- 4. 체계적인 TIP 악용 워크플로우(TEW)를 통해 조작된 도구 호출을 통한 외부 도구 행동 하이재킹을 시연합니다.
- 5. LLM 기반 에이전트 시스템의 TIP 보안을 강화하기 위한 방어 메커니즘을 제안합니다.


---

*Generated on 2025-09-23 10:11:33*