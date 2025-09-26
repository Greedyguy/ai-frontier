---
keywords:
  - Large Language Model
  - TranSQL+
  - Relational Database
  - Vectorized Execution
  - ROW2COL Optimization
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2502.02818
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:00:52.429022",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "TranSQL+",
    "Relational Database",
    "Vectorized Execution",
    "ROW2COL Optimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "TranSQL+": 0.8,
    "Relational Database": 0.75,
    "Vectorized Execution": 0.7,
    "ROW2COL Optimization": 0.7
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
        "rationale": "This term is central to the paper's focus on deploying LLMs on low-resource hardware.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "TranSQL+",
        "canonical": "TranSQL+",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "TranSQL+ is the unique solution proposed in the paper for executing LLM computations using SQL.",
        "novelty_score": 0.9,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "relational databases",
        "canonical": "Relational Database",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Relational databases are critical to the implementation of TranSQL+ and its execution strategy.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "vectorized execution",
        "canonical": "Vectorized Execution",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This technique is a key feature leveraged by TranSQL+ for efficient processing.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "row-to-column optimization",
        "canonical": "ROW2COL Optimization",
        "aliases": [
          "ROW2COL"
        ],
        "category": "unique_technical",
        "rationale": "This optimization is a novel contribution of the paper to improve join efficiency.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
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
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "TranSQL+",
      "resolved_canonical": "TranSQL+",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "relational databases",
      "resolved_canonical": "Relational Database",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "vectorized execution",
      "resolved_canonical": "Vectorized Execution",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "row-to-column optimization",
      "resolved_canonical": "ROW2COL Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# TranSQL+: Serving Large Language Models with SQL on Low-Resource Hardware

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2502.02818.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2502.02818](https://arxiv.org/abs/2502.02818)

## 🔗 유사한 논문
- [[2025-09-23/LightRetriever_ A LLM-based Text Retrieval Architecture with Extremely Faster Query Inference_20250923|LightRetriever: A LLM-based Text Retrieval Architecture with Extremely Faster Query Inference]] (84.7% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (84.7% similar)
- [[2025-09-23/GALLa_ Graph Aligned Large Language Models for Improved Source Code Understanding_20250923|GALLa: Graph Aligned Large Language Models for Improved Source Code Understanding]] (83.8% similar)
- [[2025-09-22/Exploring Polyglot Harmony_ On Multilingual Data Allocation for Large Language Models Pretraining_20250922|Exploring Polyglot Harmony: On Multilingual Data Allocation for Large Language Models Pretraining]] (83.1% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (83.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Relational Database|Relational Database]], [[keywords/Vectorized Execution|Vectorized Execution]]
**⚡ Unique Technical**: [[keywords/TranSQL+|TranSQL+]], [[keywords/ROW2COL Optimization|ROW2COL Optimization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.02818v3 Announce Type: replace-cross 
Abstract: Deploying Large Language Models (LLMs) on resource-constrained devices remains challenging due to limited memory, lack of GPUs, and the complexity of existing runtimes. In this paper, we introduce TranSQL+, a template-based code generator that translates LLM computation graphs into pure SQL queries for execution in relational databases. Without relying on external libraries, TranSQL+, leverages mature database features, such as vectorized execution and out-of-core processing, for efficient inference. We further propose a row-to-column (ROW2COL) optimization that improves join efficiency in matrix operations. Evaluated on Llama3-8B and DeepSeekMoE models, TranSQL+ achieves up to 20x lower prefill latency and 4x higher decoding speed compared to DeepSpeed Inference and Llama.cpp in low-memory and CPU-only configurations. Our results highlight relational databases as a practical environment for LLMs on low-resource hardware.

## 📝 요약

이 논문은 제한된 자원 환경에서 대형 언어 모델(LLM)을 효과적으로 실행하기 위한 TranSQL+를 소개합니다. TranSQL+는 LLM의 계산 그래프를 순수 SQL 쿼리로 변환하여 관계형 데이터베이스에서 실행하며, 외부 라이브러리 없이 데이터베이스의 성숙한 기능을 활용합니다. 또한 행을 열로 변환하는 ROW2COL 최적화를 통해 행렬 연산의 조인 효율성을 개선합니다. Llama3-8B 및 DeepSeekMoE 모델을 평가한 결과, TranSQL+는 낮은 메모리와 CPU 전용 환경에서 DeepSpeed Inference 및 Llama.cpp에 비해 최대 20배 낮은 초기 지연 시간과 4배 빠른 디코딩 속도를 달성했습니다. 이는 저자원이 요구되는 하드웨어에서 LLM을 실행하기 위한 실용적인 환경으로 관계형 데이터베이스의 가능성을 보여줍니다.

## 🎯 주요 포인트

- 1. TranSQL+는 LLM 계산 그래프를 순수 SQL 쿼리로 변환하여 관계형 데이터베이스에서 실행할 수 있는 템플릿 기반 코드 생성기입니다.
- 2. TranSQL+는 외부 라이브러리에 의존하지 않고 데이터베이스의 성숙한 기능을 활용하여 효율적인 추론을 지원합니다.
- 3. ROW2COL 최적화를 통해 행렬 연산에서 조인 효율성을 개선합니다.
- 4. TranSQL+는 Llama3-8B 및 DeepSeekMoE 모델에서 저메모리 및 CPU 전용 환경에서 최대 20배 낮은 프리필 대기 시간과 4배 빠른 디코딩 속도를 달성합니다.
- 5. 연구 결과는 저자원 하드웨어에서 LLM을 실행하기 위한 실용적인 환경으로 관계형 데이터베이스의 가능성을 강조합니다.


---

*Generated on 2025-09-24 03:00:52*