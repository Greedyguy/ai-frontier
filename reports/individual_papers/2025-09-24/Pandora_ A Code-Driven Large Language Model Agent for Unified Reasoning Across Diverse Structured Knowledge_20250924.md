<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:33:29.778281",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Unified Structured Knowledge Reasoning",
    "Knowledge Graphs",
    "Pandas API"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Unified Structured Knowledge Reasoning": 0.7,
    "Knowledge Graphs": 0.8,
    "Pandas API": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's approach, connecting it to a broader context of AI advancements.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Unified Structured Knowledge Reasoning",
        "canonical": "Unified Structured Knowledge Reasoning",
        "aliases": [
          "USKR"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel approach introduced by the paper, essential for understanding its unique contribution.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Knowledge Graphs",
        "canonical": "Knowledge Graphs",
        "aliases": [
          "KG"
        ],
        "category": "specific_connectable",
        "rationale": "Key component in the structured knowledge sources discussed, linking to existing research on graph-based data.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Python's Pandas API",
        "canonical": "Pandas API",
        "aliases": [
          "Python Pandas"
        ],
        "category": "specific_connectable",
        "rationale": "Integral to the proposed framework, facilitating the connection between data manipulation and LLMs.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
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
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Unified Structured Knowledge Reasoning",
      "resolved_canonical": "Unified Structured Knowledge Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Knowledge Graphs",
      "resolved_canonical": "Knowledge Graphs",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Python's Pandas API",
      "resolved_canonical": "Pandas API",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Pandora: A Code-Driven Large Language Model Agent for Unified Reasoning Across Diverse Structured Knowledge

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2504.12734.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2504.12734](https://arxiv.org/abs/2504.12734)

## 🔗 유사한 논문
- [[2025-09-23/K-DeCore_ Facilitating Knowledge Transfer in Continual Structured Knowledge Reasoning via Knowledge Decoupling_20250923|K-DeCore: Facilitating Knowledge Transfer in Continual Structured Knowledge Reasoning via Knowledge Decoupling]] (83.2% similar)
- [[2025-09-23/UR$^2$_ Unify RAG and Reasoning through Reinforcement Learning_20250923|UR$^2$: Unify RAG and Reasoning through Reinforcement Learning]] (83.0% similar)
- [[2025-09-23/WebResearcher_ Unleashing unbounded reasoning capability in Long-Horizon Agents_20250923|WebResearcher: Unleashing unbounded reasoning capability in Long-Horizon Agents]] (81.7% similar)
- [[2025-09-23/ARK-V1_ An LLM-Agent for Knowledge Graph Question Answering Requiring Commonsense Reasoning_20250923|ARK-V1: An LLM-Agent for Knowledge Graph Question Answering Requiring Commonsense Reasoning]] (81.5% similar)
- [[2025-09-22/Search and Refine During Think_ Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning_20250922|Search and Refine During Think: Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Knowledge Graphs|Knowledge Graphs]], [[keywords/Pandas API|Pandas API]]
**⚡ Unique Technical**: [[keywords/Unified Structured Knowledge Reasoning|Unified Structured Knowledge Reasoning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.12734v2 Announce Type: replace-cross 
Abstract: Unified Structured Knowledge Reasoning (USKR) aims to answer natural language questions (NLQs) by using structured sources such as tables, databases, and knowledge graphs in a unified way. Existing USKR methods either rely on employing task-specific strategies or custom-defined representations, which struggle to leverage the knowledge transfer between different SKR tasks or align with the prior of LLMs, thereby limiting their performance. This paper proposes a novel USKR framework named \textsc{Pandora}, which takes advantage of \textsc{Python}'s \textsc{Pandas} API to construct a unified knowledge representation for alignment with LLM pre-training. It employs an LLM to generate textual reasoning steps and executable Python code for each question. Demonstrations are drawn from a memory of training examples that cover various SKR tasks, facilitating knowledge transfer. Extensive experiments on four benchmarks involving three SKR tasks demonstrate that \textsc{Pandora} outperforms existing unified frameworks and competes effectively with task-specific methods.

## 📝 요약

이 논문은 자연어 질문에 대해 표, 데이터베이스, 지식 그래프와 같은 구조화된 소스를 통합적으로 활용하여 답변하는 통합 구조 지식 추론(USKR) 방법론을 제안합니다. 기존 방법론의 한계를 극복하기 위해, 이 연구는 \textsc{Pandora}라는 새로운 USKR 프레임워크를 소개합니다. \textsc{Pandora}는 \textsc{Python}의 \textsc{Pandas} API를 활용하여 통합된 지식 표현을 구축하고, 대규모 언어 모델(LLM)과의 정렬을 통해 성능을 향상시킵니다. 각 질문에 대해 텍스트 기반의 추론 단계와 실행 가능한 파이썬 코드를 생성하며, 다양한 SKR 작업을 포함한 학습 예시를 통해 지식 전이를 촉진합니다. 네 가지 벤치마크 실험 결과, \textsc{Pandora}는 기존의 통합 프레임워크를 능가하고, 작업별 특화된 방법들과 경쟁할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. USKR는 테이블, 데이터베이스, 지식 그래프와 같은 구조화된 소스를 사용하여 자연어 질문에 답하는 것을 목표로 한다.
- 2. 기존의 USKR 방법은 특정 작업 전략이나 사용자 정의 표현에 의존하여 지식 전이를 효과적으로 활용하지 못한다.
- 3. \textsc{Pandora}는 \textsc{Python}의 \textsc{Pandas} API를 활용하여 LLM 사전 훈련과의 정렬을 위한 통합 지식 표현을 구축한다.
- 4. \textsc{Pandora}는 LLM을 사용하여 각 질문에 대한 텍스트 추론 단계와 실행 가능한 Python 코드를 생성한다.
- 5. 네 가지 벤치마크 실험에서 \textsc{Pandora}는 기존 통합 프레임워크를 능가하며, 작업별 방법과도 효과적으로 경쟁한다.


---

*Generated on 2025-09-24 14:33:29*