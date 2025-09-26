---
keywords:
  - Large Language Model
  - BISAC Classification
  - BM25 Retrieval
  - Multi-Agent Debate
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15568
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:04:34.359063",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "BISAC Classification",
    "BM25 Retrieval",
    "Multi-Agent Debate"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "BISAC Classification": 0.65,
    "BM25 Retrieval": 0.7,
    "Multi-Agent Debate": 0.68
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
        "rationale": "Connects to a foundational concept in NLP and machine learning, facilitating integration with existing research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "BISAC book classification system",
        "canonical": "BISAC Classification",
        "aliases": [
          "BISAC",
          "Book Industry Standards and Communications"
        ],
        "category": "unique_technical",
        "rationale": "Provides a structured topic organization method, crucial for understanding the paper's approach.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.65
      },
      {
        "surface": "BM25 retrieval",
        "canonical": "BM25 Retrieval",
        "aliases": [
          "BM25",
          "Best Matching 25"
        ],
        "category": "specific_connectable",
        "rationale": "A well-known information retrieval algorithm, connecting to broader IR and NLP topics.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.7
      },
      {
        "surface": "multi-agent debate",
        "canonical": "Multi-Agent Debate",
        "aliases": [
          "Agent Debate",
          "Debate Mechanism"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach for generating diverse topics, enhancing the paper's methodological contribution.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.68
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
      "candidate_surface": "BISAC book classification system",
      "resolved_canonical": "BISAC Classification",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.65
      }
    },
    {
      "candidate_surface": "BM25 retrieval",
      "resolved_canonical": "BM25 Retrieval",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "multi-agent debate",
      "resolved_canonical": "Multi-Agent Debate",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.68
      }
    }
  ]
}
-->

# LiteLong: Resource-Efficient Long-Context Data Synthesis for LLMs

**Korean Title:** LiteLong: LLM을 위한 자원 효율적인 장문 컨텍스트 데이터 합성

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15568.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15568](https://arxiv.org/abs/2509.15568)

## 🔗 유사한 논문
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (83.7% similar)
- [[2025-09-22/SyGra_ A Unified Graph-Based Framework for Scalable Generation, Quality Tagging, and Management of Synthetic Data_20250922|SyGra: A Unified Graph-Based Framework for Scalable Generation, Quality Tagging, and Management of Synthetic Data]] (83.1% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (83.1% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (82.7% similar)
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM: Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/BM25 Retrieval|BM25 Retrieval]]
**⚡ Unique Technical**: [[keywords/BISAC Classification|BISAC Classification]], [[keywords/Multi-Agent Debate|Multi-Agent Debate]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15568v1 Announce Type: cross 
Abstract: High-quality long-context data is essential for training large language models (LLMs) capable of processing extensive documents, yet existing synthesis approaches using relevance-based aggregation face challenges of computational efficiency. We present LiteLong, a resource-efficient method for synthesizing long-context data through structured topic organization and multi-agent debate. Our approach leverages the BISAC book classification system to provide a comprehensive hierarchical topic organization, and then employs a debate mechanism with multiple LLMs to generate diverse, high-quality topics within this structure. For each topic, we use lightweight BM25 retrieval to obtain relevant documents and concatenate them into 128K-token training samples. Experiments on HELMET and Ruler benchmarks demonstrate that LiteLong achieves competitive long-context performance and can seamlessly integrate with other long-dependency enhancement methods. LiteLong makes high-quality long-context data synthesis more accessible by reducing both computational and data engineering costs, facilitating further research in long-context language training.

## 🔍 Abstract (한글 번역)

arXiv:2509.15568v1 발표 유형: 교차  
초록: 고품질의 긴 문맥 데이터를 생성하는 것은 방대한 문서를 처리할 수 있는 대형 언어 모델(LLMs)을 훈련하는 데 필수적이지만, 기존의 관련성 기반 집계 방법은 계산 효율성에서 문제를 겪고 있습니다. 우리는 구조화된 주제 조직화와 다중 에이전트 토론을 통해 긴 문맥 데이터를 효율적으로 합성하는 방법인 LiteLong을 제시합니다. 우리의 접근법은 BISAC 도서 분류 시스템을 활용하여 포괄적인 계층적 주제 조직화를 제공하고, 이 구조 내에서 다양한 고품질 주제를 생성하기 위해 여러 LLMs와의 토론 메커니즘을 사용합니다. 각 주제에 대해, 우리는 경량화된 BM25 검색을 사용하여 관련 문서를 얻고 이를 128K-토큰 훈련 샘플로 연결합니다. HELMET 및 Ruler 벤치마크에 대한 실험은 LiteLong이 경쟁력 있는 긴 문맥 성능을 달성하며 다른 긴 의존성 강화 방법과 원활하게 통합될 수 있음을 보여줍니다. LiteLong은 계산 및 데이터 엔지니어링 비용을 줄여 고품질의 긴 문맥 데이터 합성을 보다 쉽게 접근할 수 있게 하여 긴 문맥 언어 훈련에 대한 추가 연구를 촉진합니다.

## 📝 요약

LiteLong은 대규모 언어 모델(LLM)을 위한 고품질 장문 데이터 생성을 위한 효율적인 방법론을 제안합니다. BISAC 도서 분류 시스템을 활용하여 주제를 체계적으로 조직하고, 다중 에이전트 토론을 통해 다양한 고품질 주제를 생성합니다. 각 주제에 대해 BM25 검색을 사용하여 관련 문서를 수집하고, 이를 128K 토큰의 훈련 샘플로 결합합니다. HELMET 및 Ruler 벤치마크 실험에서 LiteLong은 경쟁력 있는 성능을 보였으며, 다른 장기 의존성 강화 방법과도 원활하게 통합될 수 있음을 입증했습니다. 이를 통해 LiteLong은 장문 데이터 합성의 비용을 줄여, 장문 언어 훈련 연구를 더욱 촉진합니다.

## 🎯 주요 포인트

- 1. LiteLong은 구조화된 주제 조직화와 다중 에이전트 토론을 통해 자원 효율적인 장문 맥락 데이터 합성을 제공합니다.
- 2. BISAC 도서 분류 시스템을 활용하여 포괄적인 계층적 주제 조직화를 구현합니다.
- 3. 경량 BM25 검색을 사용하여 각 주제에 대한 관련 문서를 얻고 이를 128K 토큰 훈련 샘플로 연결합니다.
- 4. HELMET 및 Ruler 벤치마크 실험에서 LiteLong은 경쟁력 있는 장문 맥락 성능을 보여줍니다.
- 5. LiteLong은 계산 및 데이터 엔지니어링 비용을 줄여 장문 맥락 데이터 합성을 더 쉽게 접근할 수 있게 합니다.


---

*Generated on 2025-09-23 09:04:34*