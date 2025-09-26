<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:51:05.797511",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Conversational Question Answering",
    "Ambiguity Detection",
    "Agentic Settings"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Conversational Question Answering": 0.8,
    "Ambiguity Detection": 0.75,
    "Agentic Settings": 0.7
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
        "rationale": "LLMs are central to the paper's discussion on ambiguity in NLP, providing a strong link to existing research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Conversational Question Answering",
        "canonical": "Conversational Question Answering",
        "aliases": [
          "CQA"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application area discussed in the paper, providing a focused link for related research.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.8
      },
      {
        "surface": "Ambiguity Detection",
        "canonical": "Ambiguity Detection",
        "aliases": [
          "Ambiguity Resolution"
        ],
        "category": "unique_technical",
        "rationale": "Key focus of the paper, addressing a core challenge in NLP with specific techniques and datasets.",
        "novelty_score": 0.7,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "Agentic Settings",
        "canonical": "Agentic Settings",
        "aliases": [
          "Agent-based Systems"
        ],
        "category": "evolved_concepts",
        "rationale": "Emerging area of research highlighted for future exploration, linking to agent-based system studies.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "ambiguity",
      "disambiguation",
      "survey",
      "future research"
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
      "candidate_surface": "Conversational Question Answering",
      "resolved_canonical": "Conversational Question Answering",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Ambiguity Detection",
      "resolved_canonical": "Ambiguity Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Agentic Settings",
      "resolved_canonical": "Agentic Settings",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Disambiguation in Conversational Question Answering in the Era of LLMs and Agents: A Survey

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.12543.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2505.12543](https://arxiv.org/abs/2505.12543)

## 🔗 유사한 논문
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (88.7% similar)
- [[2025-09-17/Correct-Detect_ Balancing Performance and Ambiguity Through the Lens of Coreference Resolution in LLMs_20250917|Correct-Detect: Balancing Performance and Ambiguity Through the Lens of Coreference Resolution in LLMs]] (85.1% similar)
- [[2025-09-19/RAcQUEt_ Unveiling the Dangers of Overlooked Referential Ambiguity in Visual LLMs_20250919|RAcQUEt: Unveiling the Dangers of Overlooked Referential Ambiguity in Visual LLMs]] (84.9% similar)
- [[2025-09-17/Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (84.6% similar)
- [[2025-09-23/Question Answering with LLMs and Learning from Answer Sets_20250923|Question Answering with LLMs and Learning from Answer Sets]] (84.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Conversational Question Answering|Conversational Question Answering]], [[keywords/Ambiguity Detection|Ambiguity Detection]]
**🚀 Evolved Concepts**: [[keywords/Agentic Settings|Agentic Settings]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.12543v2 Announce Type: replace 
Abstract: Ambiguity remains a fundamental challenge in Natural Language Processing (NLP) due to the inherent complexity and flexibility of human language. With the advent of Large Language Models (LLMs), addressing ambiguity has become even more critical due to their expanded capabilities and applications. In the context of Conversational Question Answering (CQA), this paper explores the definition, forms, and implications of ambiguity for language driven systems, particularly in the context of LLMs. We define key terms and concepts, categorize various disambiguation approaches enabled by LLMs, and provide a comparative analysis of their advantages and disadvantages. We also explore publicly available datasets for benchmarking ambiguity detection and resolution techniques and highlight their relevance for ongoing research. Finally, we identify open problems and future research directions, especially in agentic settings, proposing areas for further investigation. By offering a comprehensive review of current research on ambiguities and disambiguation with LLMs, we aim to contribute to the development of more robust and reliable LLM-based systems.

## 📝 요약

이 논문은 대화형 질문 응답(CQA)에서 대형 언어 모델(LLM)을 활용한 모호성 문제를 탐구합니다. LLM의 확장된 기능과 응용으로 인해 모호성 해결이 더욱 중요해졌습니다. 논문은 모호성의 정의와 형태, LLM을 통한 다양한 해소 방법을 분류하고, 이들의 장단점을 비교 분석합니다. 또한, 모호성 탐지 및 해결을 위한 공개 데이터셋을 검토하고, 관련 연구의 중요성을 강조합니다. 마지막으로, 에이전트 환경에서의 미해결 문제와 향후 연구 방향을 제시하며, LLM 기반 시스템의 발전에 기여하고자 합니다.

## 🎯 주요 포인트

- 1. 자연어 처리(NLP)에서 모호성은 인간 언어의 복잡성과 유연성 때문에 여전히 근본적인 도전 과제입니다.
- 2. 대화형 질문 응답(CQA)에서 LLM의 맥락에서 모호성의 정의, 형태 및 함의를 탐구합니다.
- 3. LLM을 활용한 다양한 비모호화 접근 방식을 분류하고, 그들의 장단점을 비교 분석합니다.
- 4. 모호성 탐지 및 해결 기법을 벤치마킹하기 위한 공개 데이터셋을 탐구하고, 연구의 중요성을 강조합니다.
- 5. 에이전트 설정에서의 개방형 문제와 미래 연구 방향을 식별하고, 추가 연구를 위한 영역을 제안합니다.


---

*Generated on 2025-09-24 15:51:05*