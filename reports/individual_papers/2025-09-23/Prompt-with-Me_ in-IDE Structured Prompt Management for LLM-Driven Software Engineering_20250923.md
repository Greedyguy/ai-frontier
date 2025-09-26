---
keywords:
  - Large Language Model
  - Prompt-with-Me
  - Prompt Management
  - Software Engineering Prompts
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17096
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:44:10.255400",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Prompt-with-Me",
    "Prompt Management",
    "Software Engineering Prompts"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Prompt-with-Me": 0.8,
    "Prompt Management": 0.78,
    "Software Engineering Prompts": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus on improving software engineering through structured prompt management.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Prompt-with-Me",
        "canonical": "Prompt-with-Me",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A unique tool introduced by the paper, crucial for understanding its contributions.",
        "novelty_score": 0.95,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "prompt management",
        "canonical": "Prompt Management",
        "aliases": [
          "structured prompt management"
        ],
        "category": "specific_connectable",
        "rationale": "Key concept for linking discussions on improving software engineering workflows.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "software engineering prompts",
        "canonical": "Software Engineering Prompts",
        "aliases": [
          "SE prompts"
        ],
        "category": "specific_connectable",
        "rationale": "Specific focus of the paper, relevant for discussions on LLM applications in software engineering.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
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
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Prompt-with-Me",
      "resolved_canonical": "Prompt-with-Me",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "prompt management",
      "resolved_canonical": "Prompt Management",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "software engineering prompts",
      "resolved_canonical": "Software Engineering Prompts",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Prompt-with-Me: in-IDE Structured Prompt Management for LLM-Driven Software Engineering

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17096.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17096](https://arxiv.org/abs/2509.17096)

## 🔗 유사한 논문
- [[2025-09-17/A Taxonomy of Prompt Defects in LLM Systems_20250917|A Taxonomy of Prompt Defects in LLM Systems]] (86.9% similar)
- [[2025-09-19/A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks_20250919|A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks]] (82.8% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (82.8% similar)
- [[2025-09-19/PMPO_ Probabilistic Metric Prompt Optimization for Small and Large Language Models_20250919|PMPO: Probabilistic Metric Prompt Optimization for Small and Large Language Models]] (82.7% similar)
- [[2025-09-19/On the Use of Agentic Coding_ An Empirical Study of Pull Requests on GitHub_20250919|On the Use of Agentic Coding: An Empirical Study of Pull Requests on GitHub]] (82.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Prompt Management|Prompt Management]], [[keywords/Software Engineering Prompts|Software Engineering Prompts]]
**⚡ Unique Technical**: [[keywords/Prompt-with-Me|Prompt-with-Me]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17096v1 Announce Type: cross 
Abstract: Large Language Models are transforming software engineering, yet prompt management in practice remains ad hoc, hindering reliability, reuse, and integration into industrial workflows. We present Prompt-with-Me, a practical solution for structured prompt management embedded directly in the development environment. The system automatically classifies prompts using a four-dimensional taxonomy encompassing intent, author role, software development lifecycle stage, and prompt type. To enhance prompt reuse and quality, Prompt-with-Me suggests language refinements, masks sensitive information, and extracts reusable templates from a developer's prompt library. Our taxonomy study of 1108 real-world prompts demonstrates that modern LLMs can accurately classify software engineering prompts. Furthermore, our user study with 11 participants shows strong developer acceptance, with high usability (Mean SUS=73), low cognitive load (Mean NASA-TLX=21), and reported gains in prompt quality and efficiency through reduced repetitive effort. Lastly, we offer actionable insights for building the next generation of prompt management and maintenance tools for software engineering workflows.

## 📝 요약

대형 언어 모델(LLM)이 소프트웨어 공학을 혁신하고 있지만, 실무에서의 프롬프트 관리가 체계적이지 않아 신뢰성, 재사용성, 산업 워크플로우 통합에 어려움을 겪고 있습니다. 이를 해결하기 위해 개발 환경에 직접 통합된 구조화된 프롬프트 관리 솔루션인 Prompt-with-Me를 제안합니다. 이 시스템은 의도, 작성자 역할, 소프트웨어 개발 생애주기 단계, 프롬프트 유형의 네 가지 차원을 기반으로 프롬프트를 자동으로 분류합니다. 또한, 프롬프트 재사용과 품질 향상을 위해 언어 수정 제안, 민감 정보 마스킹, 재사용 가능한 템플릿 추출 기능을 제공합니다. 1108개의 실제 프롬프트를 대상으로 한 연구에서 현대 LLM이 소프트웨어 공학 프롬프트를 정확히 분류할 수 있음을 확인했습니다. 11명의 참가자를 대상으로 한 사용자 연구에서는 높은 사용성(평균 SUS=73)과 낮은 인지 부하(평균 NASA-TLX=21)를 보였으며, 프롬프트 품질과 효율성이 향상되었다고 보고되었습니다. 이러한 연구 결과는 차세대 소프트웨어 공학 워크플로우용 프롬프트 관리 및 유지보수 도구 개발에 유용한 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. Prompt-with-Me는 개발 환경에 직접 내장된 구조화된 프롬프트 관리 솔루션을 제공합니다.
- 2. 시스템은 의도, 작성자 역할, 소프트웨어 개발 생명주기 단계, 프롬프트 유형을 포함한 4차원 분류 체계를 사용하여 프롬프트를 자동으로 분류합니다.
- 3. Prompt-with-Me는 언어 개선, 민감 정보 마스킹, 재사용 가능한 템플릿 추출을 통해 프롬프트 재사용과 품질을 향상시킵니다.
- 4. 1108개의 실제 프롬프트에 대한 분류 연구는 현대의 대형 언어 모델이 소프트웨어 엔지니어링 프롬프트를 정확하게 분류할 수 있음을 보여줍니다.
- 5. 사용자 연구 결과, 개발자들은 높은 사용성, 낮은 인지 부하, 프롬프트 품질과 효율성 향상을 보고하며, 프롬프트 관리 도구에 대한 강한 수용성을 나타냈습니다.


---

*Generated on 2025-09-23 23:44:10*