---
keywords:
  - Large Language Model
  - Ontology-driven Reasoning
  - Knowledge Graph
  - First-Order Logic
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2508.01424
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:32:45.898488",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Ontology-driven Reasoning",
    "Knowledge Graph",
    "First-Order Logic"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Ontology-driven Reasoning": 0.8,
    "Knowledge Graph": 0.78,
    "First-Order Logic": 0.77
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
        "rationale": "Central to the paper's methodology, linking to foundational concepts in NLP.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Ontology-driven Reasoning",
        "canonical": "Ontology-driven Reasoning",
        "aliases": [
          "ORACLE"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel framework for enhancing reasoning in LLMs.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Knowledge Graphs",
        "canonical": "Knowledge Graph",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Key component in the proposed framework, facilitating structured reasoning.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "First-Order Logic",
        "canonical": "First-Order Logic",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Essential for transforming ontologies into reasoning chains.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "DeepSeek-R1",
      "MQA benchmarks"
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
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Ontology-driven Reasoning",
      "resolved_canonical": "Ontology-driven Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Knowledge Graphs",
      "resolved_canonical": "Knowledge Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "First-Order Logic",
      "resolved_canonical": "First-Order Logic",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# From Query to Logic: Ontology-Driven Multi-Hop Reasoning in LLMs

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2508.01424.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2508.01424](https://arxiv.org/abs/2508.01424)

## 🔗 유사한 논문
- [[2025-09-23/Question Answering with LLMs and Learning from Answer Sets_20250923|Question Answering with LLMs and Learning from Answer Sets]] (87.9% similar)
- [[2025-09-23/ARK-V1_ An LLM-Agent for Knowledge Graph Question Answering Requiring Commonsense Reasoning_20250923|ARK-V1: An LLM-Agent for Knowledge Graph Question Answering Requiring Commonsense Reasoning]] (87.0% similar)
- [[2025-09-23/Large Language Models Meet Knowledge Graphs for Question Answering_ Synthesis and Opportunities_20250923|Large Language Models Meet Knowledge Graphs for Question Answering: Synthesis and Opportunities]] (86.4% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (86.4% similar)
- [[2025-09-23/Open Vision Reasoner_ Transferring Linguistic Cognitive Behavior for Visual Reasoning_20250923|Open Vision Reasoner: Transferring Linguistic Cognitive Behavior for Visual Reasoning]] (86.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Knowledge Graph|Knowledge Graph]], [[keywords/First-Order Logic|First-Order Logic]]
**⚡ Unique Technical**: [[keywords/Ontology-driven Reasoning|Ontology-driven Reasoning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.01424v2 Announce Type: replace-cross 
Abstract: Large Language Models (LLMs), despite their success in question answering, exhibit limitations in complex multi-hop question answering (MQA) tasks that necessitate non-linear, structured reasoning. This limitation stems from their inability to adequately capture deep conceptual relationships between entities. To overcome this challenge, we present **ORACLE** (**O**ntology-driven **R**easoning **A**nd **C**hain for **L**ogical **E**ucidation), a training-free framework that combines LLMs' generative capabilities with the structural benefits of knowledge graphs. Our approach operates through three stages: (1) dynamic construction of question-specific knowledge ontologies using LLMs, (2) transformation of these ontologies into First-Order Logic reasoning chains, and (3) systematic decomposition of the original query into logically coherent sub-questions. Experimental results on several standard MQA benchmarks show that our framework achieves highly competitive performance, rivaling current state-of-the-art models like DeepSeek-R1. Detailed analyses further confirm the effectiveness of each component, while demonstrating that our method generates more logical and interpretable reasoning chains than existing approaches.

## 📝 요약

대형 언어 모델(LLM)은 복잡한 다중 단계 질문 응답(MQA)에서 한계를 보입니다. 이를 해결하기 위해, 우리는 **ORACLE**이라는 훈련이 필요 없는 프레임워크를 제안합니다. 이 방법은 LLM의 생성 능력과 지식 그래프의 구조적 이점을 결합합니다. ORACLE은 (1) LLM을 사용하여 질문에 특화된 지식 온톨로지를 동적으로 구축하고, (2) 이를 일차 논리 추론 체인으로 변환하며, (3) 원래의 질문을 논리적으로 일관된 하위 질문으로 체계적으로 분해하는 세 단계로 작동합니다. 실험 결과, ORACLE은 여러 MQA 벤치마크에서 최첨단 모델과 경쟁할 만한 성능을 보였으며, 논리적이고 해석 가능한 추론 체인을 생성하는 데 효과적임을 입증했습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)은 복잡한 다중 단계 질문 응답(MQA)에서 비선형적이고 구조화된 추론이 필요한 경우 한계를 보인다.
- 2. ORACLE은 LLMs의 생성 능력과 지식 그래프의 구조적 이점을 결합한 훈련이 필요 없는 프레임워크이다.
- 3. 이 접근법은 질문별 지식 온톨로지의 동적 구성, 일차 논리 추론 체인으로의 변환, 논리적으로 일관된 하위 질문으로의 체계적 분해의 세 단계로 작동한다.
- 4. 여러 MQA 벤치마크 실험 결과, ORACLE은 DeepSeek-R1과 같은 최신 모델과 경쟁할 만한 성능을 보였다.
- 5. ORACLE은 기존 접근법보다 더 논리적이고 해석 가능한 추론 체인을 생성하는 것으로 나타났다.


---

*Generated on 2025-09-25 16:32:45*