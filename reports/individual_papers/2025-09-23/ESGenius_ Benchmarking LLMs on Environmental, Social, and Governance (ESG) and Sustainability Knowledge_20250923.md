---
keywords:
  - ESGenius Benchmark
  - Large Language Model
  - Retrieval Augmented Generation
  - Zero-Shot Learning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2506.01646
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:04:45.615995",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "ESGenius Benchmark",
    "Large Language Model",
    "Retrieval Augmented Generation",
    "Zero-Shot Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "ESGenius Benchmark": 0.8,
    "Large Language Model": 0.85,
    "Retrieval Augmented Generation": 0.82,
    "Zero-Shot Learning": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "ESGenius",
        "canonical": "ESGenius Benchmark",
        "aliases": [
          "ESG Benchmark",
          "Sustainability Benchmark"
        ],
        "category": "unique_technical",
        "rationale": "ESGenius is a novel benchmark specifically designed to evaluate LLMs on ESG and sustainability, providing a unique linking opportunity in this domain.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Language Model"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's evaluation framework, providing a strong link to existing discussions on AI capabilities.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Retrieval-Augmented Generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "RAG is a trending method that significantly improves model performance in the paper, making it a valuable link to recent advancements in AI.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "Zero-Shot",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-Shot Learning is a key evaluation protocol in the paper, highlighting its importance in assessing LLMs' capabilities.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
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
      "candidate_surface": "ESGenius",
      "resolved_canonical": "ESGenius Benchmark",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Retrieval-Augmented Generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Zero-Shot",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# ESGenius: Benchmarking LLMs on Environmental, Social, and Governance (ESG) and Sustainability Knowledge

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.01646.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2506.01646](https://arxiv.org/abs/2506.01646)

## 🔗 유사한 논문
- [[2025-09-23/EngiBench_ A Benchmark for Evaluating Large Language Models on Engineering Problem Solving_20250923|EngiBench: A Benchmark for Evaluating Large Language Models on Engineering Problem Solving]] (87.1% similar)
- [[2025-09-23/MSCoRe_ A Benchmark for Multi-Stage Collaborative Reasoning in LLM Agents_20250923|MSCoRe: A Benchmark for Multi-Stage Collaborative Reasoning in LLM Agents]] (84.7% similar)
- [[2025-09-22/Beyond Pointwise Scores_ Decomposed Criteria-Based Evaluation of LLM Responses_20250922|Beyond Pointwise Scores: Decomposed Criteria-Based Evaluation of LLM Responses]] (84.7% similar)
- [[2025-09-23/EquiBench_ Benchmarking Large Language Models' Reasoning about Program Semantics via Equivalence Checking_20250923|EquiBench: Benchmarking Large Language Models' Reasoning about Program Semantics via Equivalence Checking]] (84.2% similar)
- [[2025-09-19/Select to Know_ An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering_20250919|Select to Know: An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering]] (84.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]], [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/ESGenius Benchmark|ESGenius Benchmark]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.01646v2 Announce Type: replace-cross 
Abstract: We introduce ESGenius, a comprehensive benchmark for evaluating and enhancing the proficiency of Large Language Models (LLMs) in Environmental, Social, and Governance (ESG) and sustainability-focused question answering. ESGenius comprises two key components: (i) ESGenius-QA, a collection of 1,136 Multiple-Choice Questions (MCQs) generated by LLMs and rigorously validated by domain experts, covering a broad range of ESG pillars and sustainability topics. Each question is systematically linked to its corresponding source text, enabling transparent evaluation and supporting Retrieval-Augmented Generation (RAG) methods; and (ii) ESGenius-Corpus, a meticulously curated repository of 231 foundational frameworks, standards, reports, and recommendation documents from 7 authoritative sources. Moreover, to fully assess the capabilities and adaptation potential of LLMs, we implement a rigorous two-stage evaluation protocol -- Zero-Shot and RAG. Extensive experiments across 50 LLMs (0.5B to 671B) demonstrate that state-of-the-art models achieve only moderate performance in zero-shot settings, with accuracies around 55--70%, highlighting a significant knowledge gap for LLMs in this specialized, interdisciplinary domain. However, models employing RAG demonstrate significant performance improvements, particularly for smaller models. For example, DeepSeek-R1-Distill-Qwen-14B improves from 63.82% (zero-shot) to 80.46% with RAG. These results demonstrate the necessity of grounding responses in authoritative sources for enhanced ESG understanding. To the best of our knowledge, ESGenius is the first comprehensive QA benchmark designed to rigorously evaluate LLMs on ESG and sustainability knowledge, providing a critical tool to advance trustworthy AI in this vital domain.

## 📝 요약

ESGenius는 대형 언어 모델(LLM)의 환경, 사회, 거버넌스(ESG) 및 지속 가능성 관련 질문 응답 능력을 평가하고 향상시키기 위한 포괄적인 벤치마크입니다. ESGenius는 두 가지 주요 구성 요소로 이루어져 있습니다. 첫째, ESGenius-QA는 LLM이 생성하고 전문가가 검증한 1,136개의 객관식 질문으로, ESG 및 지속 가능성 주제를 포괄합니다. 둘째, ESGenius-Corpus는 7개의 권위 있는 출처로부터 수집된 231개의 기초 문서로 구성된 데이터베이스입니다. LLM의 능력을 평가하기 위해 제로샷 및 검색 증강 생성(RAG) 방법을 사용한 평가 프로토콜을 적용했습니다. 50개의 LLM 실험 결과, 제로샷 설정에서는 55-70%의 정확도로 중간 수준의 성능을 보였으나, RAG를 활용하면 성능이 크게 향상되었습니다. 이는 ESG 이해를 높이기 위해 권위 있는 출처에 기반한 응답이 필요함을 보여줍니다. ESGenius는 ESG 및 지속 가능성 지식을 평가하기 위한 최초의 포괄적 QA 벤치마크로, 신뢰할 수 있는 AI 발전에 중요한 도구를 제공합니다.

## 🎯 주요 포인트

- 1. ESGenius는 대규모 언어 모델(LLMs)의 ESG 및 지속 가능성 관련 질문 응답 능력을 평가하고 향상시키기 위한 포괄적인 벤치마크입니다.
- 2. ESGenius는 LLM이 생성하고 도메인 전문가가 검증한 1,136개의 객관식 질문으로 구성된 ESGenius-QA와 7개의 권위 있는 출처에서 수집한 231개의 기초 문서로 구성된 ESGenius-Corpus로 이루어져 있습니다.
- 3. LLM의 능력과 적응성을 평가하기 위해 제로샷 및 RAG의 두 단계 평가 프로토콜을 구현하였으며, RAG를 활용한 모델이 특히 작은 모델에서 성능이 크게 향상됨을 확인했습니다.
- 4. 최첨단 모델도 제로샷 설정에서 55-70%의 정확도를 보여 ESG 분야에서 LLM의 지식 격차가 있음을 강조합니다.
- 5. ESGenius는 ESG 및 지속 가능성 지식을 엄격하게 평가하기 위해 설계된 최초의 포괄적인 QA 벤치마크로, 이 중요한 분야에서 신뢰할 수 있는 AI 발전에 기여합니다.


---

*Generated on 2025-09-24 01:04:45*