---
keywords:
  - Large Language Model
  - Aggregative Question Answering
  - Conversational Data
  - Collective Insights
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2505.23765
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:04:05.225524",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Aggregative Question Answering",
    "Conversational Data",
    "Collective Insights"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Aggregative Question Answering": 0.8,
    "Conversational Data": 0.75,
    "Collective Insights": 0.7
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
        "rationale": "Large Language Models are central to the paper's discussion and connect well with other NLP concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Aggregative Question Answering",
        "canonical": "Aggregative Question Answering",
        "aliases": [
          "AQA"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel task introduced by the paper, central to its contributions.",
        "novelty_score": 0.92,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Conversational Data",
        "canonical": "Conversational Data",
        "aliases": [
          "Chat Logs"
        ],
        "category": "specific_connectable",
        "rationale": "Conversational data is crucial for understanding and linking to other works on data analysis and NLP.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Collective Insights",
        "canonical": "Collective Insights",
        "aliases": [
          "Aggregated Insights"
        ],
        "category": "unique_technical",
        "rationale": "The concept of deriving collective insights from data is unique and central to the paper's methodology.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
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
      "candidate_surface": "Aggregative Question Answering",
      "resolved_canonical": "Aggregative Question Answering",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Conversational Data",
      "resolved_canonical": "Conversational Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Collective Insights",
      "resolved_canonical": "Collective Insights",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# From Chat Logs to Collective Insights: Aggregative Question Answering

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.23765.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2505.23765](https://arxiv.org/abs/2505.23765)

## 🔗 유사한 논문
- [[2025-09-22/MMAPG_ A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs_20250922|MMAPG: A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs]] (83.5% similar)
- [[2025-09-23/Large Language Models Meet Knowledge Graphs for Question Answering_ Synthesis and Opportunities_20250923|Large Language Models Meet Knowledge Graphs for Question Answering: Synthesis and Opportunities]] (83.3% similar)
- [[2025-09-19/Graph-Enhanced Retrieval-Augmented Question Answering for E-Commerce Customer Support_20250919|Graph-Enhanced Retrieval-Augmented Question Answering for E-Commerce Customer Support]] (82.8% similar)
- [[2025-09-18/MAFA_ A multi-agent framework for annotation_20250918|MAFA: A multi-agent framework for annotation]] (81.6% similar)
- [[2025-09-23/A State-Update Prompting Strategy for Efficient and Robust Multi-turn Dialogue_20250923|A State-Update Prompting Strategy for Efficient and Robust Multi-turn Dialogue]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Conversational Data|Conversational Data]]
**⚡ Unique Technical**: [[keywords/Aggregative Question Answering|Aggregative Question Answering]], [[keywords/Collective Insights|Collective Insights]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.23765v2 Announce Type: replace-cross 
Abstract: Conversational agents powered by large language models (LLMs) are rapidly becoming integral to our daily interactions, generating unprecedented amounts of conversational data. Such datasets offer a powerful lens into societal interests, trending topics, and collective concerns. Yet, existing approaches typically treat these interactions as independent and miss critical insights that could emerge from aggregating and reasoning across large-scale conversation logs. In this paper, we introduce Aggregative Question Answering, a novel task requiring models to reason explicitly over thousands of user-chatbot interactions to answer aggregative queries, such as identifying emerging concerns among specific demographics. To enable research in this direction, we construct a benchmark, WildChat-AQA, comprising 6,027 aggregative questions derived from 182,330 real-world chatbot conversations. Experiments show that existing methods either struggle to reason effectively or incur prohibitive computational costs, underscoring the need for new approaches capable of extracting collective insights from large-scale conversational data.

## 📝 요약

대화형 에이전트와 대형 언어 모델(LLM)의 발전으로 대화 데이터가 급증하고 있습니다. 이러한 데이터는 사회적 관심사와 트렌드를 파악하는 데 유용하지만, 기존 방법은 개별 대화를 독립적으로 처리하여 중요한 통찰을 놓치고 있습니다. 본 논문에서는 수천 건의 사용자-챗봇 상호작용을 통해 집합적 질문에 답하는 새로운 과제인 '집합적 질문 응답(Aggregative Question Answering)'을 소개합니다. 이를 위해 182,330개의 실제 챗봇 대화에서 추출한 6,027개의 집합적 질문으로 구성된 벤치마크 'WildChat-AQA'를 구축했습니다. 실험 결과, 기존 방법은 효과적인 추론에 어려움을 겪거나 높은 계산 비용이 발생하여 대규모 대화 데이터에서 집합적 통찰을 추출할 수 있는 새로운 접근법의 필요성을 강조합니다.

## 🎯 주요 포인트

- 1. 대화형 에이전트는 대규모 언어 모델을 기반으로 하여 일상적인 상호작용에서 중요한 역할을 하고 있으며, 방대한 양의 대화 데이터를 생성하고 있다.
- 2. 기존 접근 방식은 대화 데이터를 독립적으로 처리하여 대규모 대화 로그에서 얻을 수 있는 중요한 통찰을 놓치고 있다.
- 3. 본 논문에서는 수천 개의 사용자-챗봇 상호작용을 통해 집합적 질문에 답하는 새로운 과제인 '집합적 질문 응답'을 소개한다.
- 4. 연구를 지원하기 위해 182,330개의 실제 챗봇 대화에서 파생된 6,027개의 집합적 질문으로 구성된 WildChat-AQA 벤치마크를 구축하였다.
- 5. 실험 결과, 기존 방법은 효과적으로 추론하지 못하거나 계산 비용이 과도하게 발생하여 대규모 대화 데이터에서 집합적 통찰을 추출할 수 있는 새로운 접근 방식이 필요함을 보여준다.


---

*Generated on 2025-09-24 01:04:05*