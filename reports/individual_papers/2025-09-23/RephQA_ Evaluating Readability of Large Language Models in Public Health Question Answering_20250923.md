---
keywords:
  - Large Language Model
  - RephQA
  - Readability Enhancement
  - Group Relative Policy Optimization
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.16360
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:11:05.733141",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "RephQA",
    "Readability Enhancement",
    "Group Relative Policy Optimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "RephQA": 0.78,
    "Readability Enhancement": 0.81,
    "Group Relative Policy Optimization": 0.79
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
        "rationale": "This is a foundational concept in the paper, linking it to the broader context of AI and NLP.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "RephQA",
        "canonical": "RephQA",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Introduces a new benchmark specific to the paper's focus on readability in public health QA.",
        "novelty_score": 0.92,
        "connectivity_score": 0.55,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "readability-enhancing strategies",
        "canonical": "Readability Enhancement",
        "aliases": [
          "readability strategies"
        ],
        "category": "specific_connectable",
        "rationale": "Key concept for improving LLM outputs, relevant to practical applications in NLP.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.77,
        "link_intent_score": 0.81
      },
      {
        "surface": "Group Relative Policy Optimization",
        "canonical": "Group Relative Policy Optimization",
        "aliases": [
          "GRPO"
        ],
        "category": "unique_technical",
        "rationale": "A novel strategy discussed in the paper to enhance readability, contributing to specific technical discourse.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "public health",
      "question answering",
      "evaluation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "RephQA",
      "resolved_canonical": "RephQA",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.55,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "readability-enhancing strategies",
      "resolved_canonical": "Readability Enhancement",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.77,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Group Relative Policy Optimization",
      "resolved_canonical": "Group Relative Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# RephQA: Evaluating Readability of Large Language Models in Public Health Question Answering

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16360.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.16360](https://arxiv.org/abs/2509.16360)

## 🔗 유사한 논문
- [[2025-09-23/Large Language Models Meet Knowledge Graphs for Question Answering_ Synthesis and Opportunities_20250923|Large Language Models Meet Knowledge Graphs for Question Answering: Synthesis and Opportunities]] (86.3% similar)
- [[2025-09-23/SparseDoctor_ Towards Efficient Chat Doctor with Mixture of Experts Enhanced Large Language Models_20250923|SparseDoctor: Towards Efficient Chat Doctor with Mixture of Experts Enhanced Large Language Models]] (86.2% similar)
- [[2025-09-23/A State-Update Prompting Strategy for Efficient and Robust Multi-turn Dialogue_20250923|A State-Update Prompting Strategy for Efficient and Robust Multi-turn Dialogue]] (85.2% similar)
- [[2025-09-23/From Scores to Steps_ Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations_20250923|From Scores to Steps: Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations]] (85.1% similar)
- [[2025-09-22/EHR-MCP_ Real-world Evaluation of Clinical Information Retrieval by Large Language Models via Model Context Protocol_20250922|EHR-MCP: Real-world Evaluation of Clinical Information Retrieval by Large Language Models via Model Context Protocol]] (85.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Readability Enhancement|Readability Enhancement]]
**⚡ Unique Technical**: [[keywords/RephQA|RephQA]], [[keywords/Group Relative Policy Optimization|Group Relative Policy Optimization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16360v1 Announce Type: new 
Abstract: Large Language Models (LLMs) hold promise in addressing complex medical problems. However, while most prior studies focus on improving accuracy and reasoning abilities, a significant bottleneck in developing effective healthcare agents lies in the readability of LLM-generated responses, specifically, their ability to answer public health problems clearly and simply to people without medical backgrounds. In this work, we introduce RephQA, a benchmark for evaluating the readability of LLMs in public health question answering (QA). It contains 533 expert-reviewed QA pairs from 27 sources across 13 topics, and includes a proxy multiple-choice task to assess informativeness, along with two readability metrics: Flesch-Kincaid grade level and professional score. Evaluation of 25 LLMs reveals that most fail to meet readability standards, highlighting a gap between reasoning and effective communication. To address this, we explore four readability-enhancing strategies-standard prompting, chain-of-thought prompting, Group Relative Policy Optimization (GRPO), and a token-adapted variant. Token-adapted GRPO achieves the best results, advancing the development of more practical and user-friendly public health agents. These results represent a step toward building more practical agents for public health.

## 📝 요약

이 논문은 대형 언어 모델(LLM)이 복잡한 의료 문제를 해결하는 데 유망하지만, 비전문가에게 명확하고 간단하게 답변하는 읽기 쉬운 응답 생성이 주요 과제임을 지적합니다. 이를 위해 공중 보건 질문 응답(QA)의 가독성을 평가하는 벤치마크인 RephQA를 소개합니다. 13개 주제에서 533개의 전문가 검토 QA 쌍을 포함하며, 정보성 평가를 위한 다지선다형 과제와 두 가지 가독성 지표를 제공합니다. 25개의 LLM을 평가한 결과, 대부분이 가독성 기준을 충족하지 못했으며, 이는 추론과 효과적인 의사소통 간의 격차를 보여줍니다. 이를 해결하기 위해 네 가지 가독성 향상 전략을 탐구했으며, Token-adapted GRPO가 가장 우수한 결과를 보였습니다. 이 연구는 실용적이고 사용자 친화적인 공중 보건 에이전트 개발에 기여합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)은 복잡한 의료 문제 해결에 잠재력을 가지고 있지만, 비전문가에게 명확하고 간단하게 답변하는 능력에서 한계가 있다.
- 2. RephQA는 공중 보건 질문 응답에서 LLM의 가독성을 평가하기 위한 벤치마크로, 13개 주제에서 533개의 전문가 검토 QA 쌍을 포함한다.
- 3. 25개의 LLM 평가 결과, 대부분이 가독성 기준을 충족하지 못하며, 추론과 효과적인 의사소통 간의 격차가 드러났다.
- 4. 가독성 향상을 위해 표준 프롬프트, 사고의 연쇄 프롬프트, 그룹 상대 정책 최적화(GRPO), 토큰 적응형 변형 등 네 가지 전략을 탐구했다.
- 5. 토큰 적응형 GRPO가 가장 우수한 결과를 보여, 보다 실용적이고 사용자 친화적인 공중 보건 에이전트 개발에 기여했다.


---

*Generated on 2025-09-24 03:11:05*