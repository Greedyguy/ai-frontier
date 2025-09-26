---
keywords:
  - CopilotLens
  - AI Code Assistants
  - Explanation Layer
  - Calibrated Trust
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2506.20062
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:08:46.948821",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "CopilotLens",
    "AI Code Assistants",
    "Explanation Layer",
    "Calibrated Trust"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "CopilotLens": 0.8,
    "AI Code Assistants": 0.75,
    "Explanation Layer": 0.7,
    "Calibrated Trust": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "CopilotLens",
        "canonical": "CopilotLens",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "CopilotLens is a novel framework introduced in the paper, offering a new approach to AI code completion with transparency and explainability.",
        "novelty_score": 0.9,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "AI-powered code assistants",
        "canonical": "AI Code Assistants",
        "aliases": [
          "AI coding agents",
          "AI code completion tools"
        ],
        "category": "specific_connectable",
        "rationale": "AI-powered code assistants are central to the paper's discussion, focusing on enhancing developer productivity and trust.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "explanation layer",
        "canonical": "Explanation Layer",
        "aliases": [
          "explanation interface"
        ],
        "category": "specific_connectable",
        "rationale": "The explanation layer is a key component of CopilotLens, crucial for understanding AI decision-making processes.",
        "novelty_score": 0.6,
        "connectivity_score": 0.72,
        "specificity_score": 0.68,
        "link_intent_score": 0.7
      },
      {
        "surface": "calibrated trust",
        "canonical": "Calibrated Trust",
        "aliases": [],
        "category": "evolved_concepts",
        "rationale": "Calibrated trust is a significant outcome of the proposed system, enhancing user confidence in AI outputs.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "code completions",
      "developer productivity",
      "mental models"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "CopilotLens",
      "resolved_canonical": "CopilotLens",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "AI-powered code assistants",
      "resolved_canonical": "AI Code Assistants",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "explanation layer",
      "resolved_canonical": "Explanation Layer",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.72,
        "specificity": 0.68,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "calibrated trust",
      "resolved_canonical": "Calibrated Trust",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Beyond Autocomplete: Designing CopilotLens Towards Transparent and Explainable AI Coding Agents

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.20062.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2506.20062](https://arxiv.org/abs/2506.20062)

## 🔗 유사한 논문
- [[2025-09-23/The STAR-XAI Protocol_ An Interactive Framework for Inducing Second-Order Agency in AI Agents_20250923|The STAR-XAI Protocol: An Interactive Framework for Inducing Second-Order Agency in AI Agents]] (82.9% similar)
- [[2025-09-18/Co-Investigator AI_ The Rise of Agentic AI for Smarter, Trustworthy AML Compliance Narratives_20250918|Co-Investigator AI: The Rise of Agentic AI for Smarter, Trustworthy AML Compliance Narratives]] (81.9% similar)
- [[2025-09-19/OpenLens AI_ Fully Autonomous Research Agent for Health Infomatics_20250919|OpenLens AI: Fully Autonomous Research Agent for Health Infomatics]] (81.7% similar)
- [[2025-09-22/AI Copilots for Reproducibility in Science_ A Case Study_20250922|AI Copilots for Reproducibility in Science: A Case Study]] (81.6% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (81.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/AI Code Assistants|AI Code Assistants]], [[keywords/Explanation Layer|Explanation Layer]]
**⚡ Unique Technical**: [[keywords/CopilotLens|CopilotLens]]
**🚀 Evolved Concepts**: [[keywords/Calibrated Trust|Calibrated Trust]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.20062v3 Announce Type: replace-cross 
Abstract: AI-powered code assistants are widely used to generate code completions, significantly boosting developer productivity. However, these tools typically present suggestions without explaining their rationale, leaving their decision-making process inscrutable. This opacity hinders developers' ability to critically evaluate outputs, form accurate mental models, and calibrate trust in the system. To address this, we introduce CopilotLens, a novel interactive framework that reframes code completion from a simple suggestion into a transparent, explainable interaction. CopilotLens operates as an explanation layer that reconstructs the AI agent's "thought process" through a dynamic, two-level interface. The tool aims to surface both high-level code changes and the specific codebase context influences. This paper presents the design and rationale of CopilotLens, offering a concrete framework and articulating expectations on deepening comprehension and calibrated trust, which we plan to evaluate in subsequent work.

## 📝 요약

AI 기반 코드 보조 도구는 개발자의 생산성을 크게 향상시키지만, 제안의 근거를 설명하지 않아 사용자가 결과를 비판적으로 평가하기 어렵습니다. 이를 해결하기 위해, 우리는 코드 완성을 투명하고 설명 가능한 상호작용으로 전환하는 CopilotLens를 소개합니다. CopilotLens는 AI 에이전트의 "사고 과정"을 재구성하는 설명 레이어로, 두 단계의 인터페이스를 통해 고수준의 코드 변경과 특정 코드베이스 맥락의 영향을 드러냅니다. 이 논문은 CopilotLens의 설계와 그 근거를 제시하며, 이해와 신뢰를 심화시키는 기대 효과를 설명합니다.

## 🎯 주요 포인트

- 1. AI 기반 코드 보조 도구는 코드 완성을 통해 개발자의 생산성을 크게 향상시킨다.
- 2. 기존 도구들은 제안의 근거를 설명하지 않아 개발자가 결과를 비판적으로 평가하기 어렵다.
- 3. CopilotLens는 코드 완성을 투명하고 설명 가능한 상호작용으로 재구성하는 새로운 프레임워크이다.
- 4. CopilotLens는 AI 에이전트의 "사고 과정"을 재구성하여 고급 코드 변경과 코드베이스 맥락의 영향을 드러낸다.
- 5. 이 연구는 CopilotLens의 설계와 근거를 제시하며, 이해 심화와 신뢰 조정에 대한 기대를 설명한다.


---

*Generated on 2025-09-24 01:08:46*