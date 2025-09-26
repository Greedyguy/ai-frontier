<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:39:51.328977",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Event Causality Identification",
    "Rubin Causal Model",
    "Synthetic Control Method",
    "Text Embedding Synthesis"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Event Causality Identification": 0.78,
    "Rubin Causal Model": 0.82,
    "Synthetic Control Method": 0.79,
    "Text Embedding Synthesis": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Event Causality Identification",
        "canonical": "Event Causality Identification",
        "aliases": [
          "ECI"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's contribution and is specific to the domain of causal inference in text.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Rubin Causal Model",
        "canonical": "Rubin Causal Model",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "The Rubin Causal Model is a foundational concept in causal inference, providing strong connectivity to related works.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Synthetic Control Method",
        "canonical": "Synthetic Control Method",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This method is a key technique used in the paper and connects to broader discussions on causal analysis.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.77,
        "link_intent_score": 0.79
      },
      {
        "surface": "Text Embedding Synthesis",
        "canonical": "Text Embedding Synthesis",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a novel technique introduced in the paper, relevant for linking to text processing methods.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "causality",
      "correlation",
      "treatment",
      "outcome"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Event Causality Identification",
      "resolved_canonical": "Event Causality Identification",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Rubin Causal Model",
      "resolved_canonical": "Rubin Causal Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Synthetic Control Method",
      "resolved_canonical": "Synthetic Control Method",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.77,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Text Embedding Synthesis",
      "resolved_canonical": "Text Embedding Synthesis",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Event Causality Identification with Synthetic Control

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18156.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18156](https://arxiv.org/abs/2509.18156)

## 🔗 유사한 논문
- [[2025-09-22/Can Large Language Models Infer Causal Relationships from Real-World Text?_20250922|Can Large Language Models Infer Causal Relationships from Real-World Text?]] (82.0% similar)
- [[2025-09-19/Causal-Counterfactual RAG_ The Integration of Causal-Counterfactual Reasoning into RAG_20250919|Causal-Counterfactual RAG: The Integration of Causal-Counterfactual Reasoning into RAG]] (79.7% similar)
- [[2025-09-23/A Multi-Level Benchmark for Causal Language Understanding in Social Media Discourse_20250923|A Multi-Level Benchmark for Causal Language Understanding in Social Media Discourse]] (79.2% similar)
- [[2025-09-23/Entropic Causal Inference_ Graph Identifiability_20250923|Entropic Causal Inference: Graph Identifiability]] (79.2% similar)
- [[2025-09-18/AgentCTG_ Harnessing Multi-Agent Collaboration for Fine-Grained Precise Control in Text Generation_20250918|AgentCTG: Harnessing Multi-Agent Collaboration for Fine-Grained Precise Control in Text Generation]] (78.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Rubin Causal Model|Rubin Causal Model]], [[keywords/Synthetic Control Method|Synthetic Control Method]]
**⚡ Unique Technical**: [[keywords/Event Causality Identification|Event Causality Identification]], [[keywords/Text Embedding Synthesis|Text Embedding Synthesis]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18156v1 Announce Type: cross 
Abstract: Event causality identification (ECI), a process that extracts causal relations between events from text, is crucial for distinguishing causation from correlation. Traditional approaches to ECI have primarily utilized linguistic patterns and multi-hop relational inference, risking false causality identification due to informal usage of causality and specious graphical inference. In this paper, we adopt the Rubin Causal Model to identify event causality: given two temporally ordered events, we see the first event as the treatment and the second one as the observed outcome. Determining their causality involves manipulating the treatment and estimating the resultant change in the likelihood of the outcome. Given that it is only possible to implement manipulation conceptually in the text domain, as a work-around, we try to find a twin for the protagonist from existing corpora. This twin should have identical life experiences with the protagonist before the treatment but undergoes an intervention of treatment. However, the practical difficulty of locating such a match limits its feasibility. Addressing this issue, we use the synthetic control method to generate such a twin' from relevant historical data, leveraging text embedding synthesis and inversion techniques. This approach allows us to identify causal relations more robustly than previous methods, including GPT-4, which is demonstrated on a causality benchmark, COPES-hard.

## 📝 요약

이 논문은 텍스트에서 사건 간 인과관계를 추출하는 과정인 사건 인과성 식별(ECI)을 다룹니다. 기존 방법들은 언어적 패턴과 다중 단계의 관계 추론을 사용했으나, 이는 잘못된 인과성 식별의 위험이 있었습니다. 본 연구에서는 Rubin 인과 모델을 채택하여 시간 순서가 있는 두 사건 간의 인과성을 식별하고자 합니다. 이를 위해 첫 번째 사건을 처리로, 두 번째 사건을 결과로 간주하여 인과성을 평가합니다. 텍스트 도메인에서의 개념적 조작의 한계를 극복하기 위해, 기존 데이터에서 주인공과 유사한 '쌍둥이'를 생성하는 합성 제어 방법을 사용합니다. 이 방법은 텍스트 임베딩 합성과 반전 기술을 활용하여, 기존 방법들보다 더 강력하게 인과관계를 식별할 수 있음을 COPES-hard 벤치마크에서 입증했습니다.

## 🎯 주요 포인트

- 1. 사건 인과 관계 식별(ECI)은 사건 간의 인과 관계를 텍스트에서 추출하는 과정으로, 인과와 상관을 구별하는 데 중요하다.
- 2. 전통적인 ECI 접근법은 언어적 패턴과 다중 홉 관계 추론을 사용했으나, 비공식적인 인과 사용과 그럴듯한 그래픽 추론으로 인해 잘못된 인과 식별의 위험이 있다.
- 3. 본 논문에서는 Rubin Causal Model을 채택하여 사건 인과 관계를 식별하며, 이를 위해 주인공과 동일한 삶의 경험을 가진 '쌍둥이'를 기존 코퍼스에서 찾으려 하지만, 실용적인 어려움이 존재한다.
- 4. 이러한 문제를 해결하기 위해, 우리는 관련 역사적 데이터를 활용하여 텍스트 임베딩 합성과 반전 기법을 통해 '쌍둥이'를 생성하는 합성 제어 방법을 사용한다.
- 5. 이 접근법은 GPT-4를 포함한 이전 방법들보다 인과 관계를 더 견고하게 식별할 수 있으며, 이는 COPES-hard라는 인과 관계 벤치마크에서 입증되었다.


---

*Generated on 2025-09-24 13:39:51*