---
keywords:
  - Agentic AI
  - Planner-Caller-Generator
  - Korean-first Policy
  - LLM Evaluation Protocol
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19369
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:31:18.781417",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Agentic AI",
    "Planner-Caller-Generator",
    "Korean-first Policy",
    "LLM Evaluation Protocol"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Agentic AI": 0.78,
    "Planner-Caller-Generator": 0.82,
    "Korean-first Policy": 0.75,
    "LLM Evaluation Protocol": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "SLM-Based Agentic AI",
        "canonical": "Agentic AI",
        "aliases": [
          "Small-Scale Language Model Agentic AI"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel architecture tailored for Korean tool use, enhancing specificity and novelty.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Planner-Caller-Generator",
        "canonical": "Planner-Caller-Generator",
        "aliases": [
          "P-C-G"
        ],
        "category": "unique_technical",
        "rationale": "Represents a distinct architectural framework that could be linked to similar modular AI systems.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.82
      },
      {
        "surface": "Korean-first value policy",
        "canonical": "Korean-first Policy",
        "aliases": [
          "Korean-first value policy"
        ],
        "category": "unique_technical",
        "rationale": "Highlights a specific policy approach that addresses language-specific execution challenges.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "LLM-as-a-Judge protocol",
        "canonical": "LLM Evaluation Protocol",
        "aliases": [
          "LLM-as-a-Judge"
        ],
        "category": "specific_connectable",
        "rationale": "Provides a method for evaluating language models, linking to broader evaluation techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "tool-use accuracy",
      "end-to-end quality"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "SLM-Based Agentic AI",
      "resolved_canonical": "Agentic AI",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Planner-Caller-Generator",
      "resolved_canonical": "Planner-Caller-Generator",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Korean-first value policy",
      "resolved_canonical": "Korean-first Policy",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "LLM-as-a-Judge protocol",
      "resolved_canonical": "LLM Evaluation Protocol",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# SLM-Based Agentic AI with P-C-G: Optimized for Korean Tool Use

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19369.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19369](https://arxiv.org/abs/2509.19369)

## 🔗 유사한 논문
- [[2025-09-24/Code Driven Planning with Domain-Adaptive Critic_20250924|Code Driven Planning with Domain-Adaptive Critic]] (83.3% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (82.9% similar)
- [[2025-09-25/Nano Bio-Agents (NBA)_ Small Language Model Agents for Genomics_20250925|Nano Bio-Agents (NBA): Small Language Model Agents for Genomics]] (82.7% similar)
- [[2025-09-24/Failure Makes the Agent Stronger_ Enhancing Accuracy through Structured Reflection for Reliable Tool Interactions_20250924|Failure Makes the Agent Stronger: Enhancing Accuracy through Structured Reflection for Reliable Tool Interactions]] (82.7% similar)
- [[2025-09-23/Tool Preferences in Agentic LLMs are Unreliable_20250923|Tool Preferences in Agentic LLMs are Unreliable]] (82.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/LLM Evaluation Protocol|LLM Evaluation Protocol]]
**⚡ Unique Technical**: [[keywords/Agentic AI|Agentic AI]], [[keywords/Planner-Caller-Generator|Planner-Caller-Generator]], [[keywords/Korean-first Policy|Korean-first Policy]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19369v1 Announce Type: cross 
Abstract: We propose a small-scale language model (SLM) based agent architecture, Planner-Caller-Generator (P-C-G), optimized for Korean tool use. P-C-G separates planning, calling, and generation by role: the Planner produces an initial batch plan with limited on-demand replanning; the Caller returns a normalized call object after joint schema-value validation; and the Generator integrates tool outputs to produce the final answer. We apply a Korean-first value policy to reduce execution failures caused by frequent Korean-to-English code switching in Korean settings. Evaluation assumes Korean queries and Korean tool/parameter specifications; it covers single-chain, multi-chain, missing-parameters, and missing-functions scenarios, and is conducted via an LLM-as-a-Judge protocol averaged over five runs under a unified I/O interface. Results show that P-C-G delivers competitive tool-use accuracy and end-to-end quality while reducing tokens and maintaining acceptable latency, indicating that role-specialized SLMs are a cost-effective alternative for Korean tool-use agents.

## 📝 요약

이 논문에서는 한국어 도구 사용에 최적화된 소규모 언어 모델(SLM) 기반의 에이전트 아키텍처인 Planner-Caller-Generator(P-C-G)를 제안합니다. P-C-G는 계획, 호출, 생성의 역할을 분리하여, Planner가 초기 계획을 수립하고, Caller가 호출 객체를 반환하며, Generator가 도구 출력을 통합하여 최종 답변을 생성합니다. 한국어 환경에서의 코드 전환 문제를 줄이기 위해 한국어 우선 정책을 적용했습니다. 평가 결과, P-C-G는 도구 사용 정확도와 품질에서 경쟁력을 보이며, 토큰 수를 줄이고 지연 시간을 유지하면서 비용 효율적인 대안임을 입증했습니다.

## 🎯 주요 포인트

- 1. Planner-Caller-Generator(P-C-G) 구조는 한국어 도구 사용에 최적화된 소규모 언어 모델 기반 에이전트 아키텍처입니다.
- 2. P-C-G는 계획, 호출, 생성의 역할을 분리하여 각각의 기능을 수행합니다.
- 3. 한국어 환경에서의 코드 전환 문제를 줄이기 위해 한국어 우선 가치 정책을 적용합니다.
- 4. 다양한 시나리오에서 평가를 통해 P-C-G가 도구 사용 정확도와 전체 품질을 유지하면서도 비용 효율적인 대안임을 입증합니다.
- 5. P-C-G는 토큰 수를 줄이고 적절한 지연 시간을 유지하면서도 경쟁력 있는 성능을 제공합니다.


---

*Generated on 2025-09-25 15:31:18*