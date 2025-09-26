---
keywords:
  - HL7 FHIR
  - Large Language Model
  - FHIR-AgentBench
  - Interoperable Clinical Data
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19319
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:22:56.390873",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "HL7 FHIR",
    "Large Language Model",
    "FHIR-AgentBench",
    "Interoperable Clinical Data"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "HL7 FHIR": 0.82,
    "Large Language Model": 0.78,
    "FHIR-AgentBench": 0.8,
    "Interoperable Clinical Data": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "HL7 FHIR standard",
        "canonical": "HL7 FHIR",
        "aliases": [
          "Health Level Seven Fast Healthcare Interoperability Resources"
        ],
        "category": "unique_technical",
        "rationale": "HL7 FHIR is a critical standard for interoperable healthcare data, making it a unique and essential link for clinical AI applications.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are foundational to the discussed agentic frameworks and their evaluation.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "FHIR-AgentBench",
        "canonical": "FHIR-AgentBench",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "FHIR-AgentBench is a newly introduced benchmark specifically designed for evaluating LLM agents in a healthcare context.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "interoperable clinical data",
        "canonical": "Interoperable Clinical Data",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Interoperable clinical data is essential for understanding the context and challenges of using LLMs in healthcare.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "benchmark",
      "evaluation suite"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "HL7 FHIR standard",
      "resolved_canonical": "HL7 FHIR",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "FHIR-AgentBench",
      "resolved_canonical": "FHIR-AgentBench",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "interoperable clinical data",
      "resolved_canonical": "Interoperable Clinical Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# FHIR-AgentBench: Benchmarking LLM Agents for Realistic Interoperable EHR Question Answering

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19319.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19319](https://arxiv.org/abs/2509.19319)

## 🔗 유사한 논문
- [[2025-09-23/Benchmarking Contextual and Paralinguistic Reasoning in Speech-LLMs_ A Case Study with In-the-Wild Data_20250923|Benchmarking Contextual and Paralinguistic Reasoning in Speech-LLMs: A Case Study with In-the-Wild Data]] (84.6% similar)
- [[2025-09-23/From Scores to Steps_ Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations_20250923|From Scores to Steps: Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations]] (84.2% similar)
- [[2025-09-23/RephQA_ Evaluating Readability of Large Language Models in Public Health Question Answering_20250923|RephQA: Evaluating Readability of Large Language Models in Public Health Question Answering]] (83.7% similar)
- [[2025-09-23/Sequential-NIAH_ A Needle-In-A-Haystack Benchmark for Extracting Sequential Needles from Long Contexts_20250923|Sequential-NIAH: A Needle-In-A-Haystack Benchmark for Extracting Sequential Needles from Long Contexts]] (83.5% similar)
- [[2025-09-23/Filling in the Clinical Gaps in Benchmark_ Case for HealthBench for the Japanese medical system_20250923|Filling in the Clinical Gaps in Benchmark: Case for HealthBench for the Japanese medical system]] (83.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Interoperable Clinical Data|Interoperable Clinical Data]]
**⚡ Unique Technical**: [[keywords/HL7 FHIR|HL7 FHIR]], [[keywords/FHIR-AgentBench|FHIR-AgentBench]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19319v1 Announce Type: cross 
Abstract: The recent shift toward the Health Level Seven Fast Healthcare Interoperability Resources (HL7 FHIR) standard opens a new frontier for clinical AI, demanding LLM agents to navigate complex, resource-based data models instead of conventional structured health data. However, existing benchmarks have lagged behind this transition, lacking the realism needed to evaluate recent LLMs on interoperable clinical data. To bridge this gap, we introduce FHIR-AgentBench, a benchmark that grounds 2,931 real-world clinical questions in the HL7 FHIR standard. Using this benchmark, we systematically evaluate agentic frameworks, comparing different data retrieval strategies (direct FHIR API calls vs. specialized tools), interaction patterns (single-turn vs. multi-turn), and reasoning strategies (natural language vs. code generation). Our experiments highlight the practical challenges of retrieving data from intricate FHIR resources and the difficulty of reasoning over them, both of which critically affect question answering performance. We publicly release the FHIR-AgentBench dataset and evaluation suite (https://github.com/glee4810/FHIR-AgentBench) to promote reproducible research and the development of robust, reliable LLM agents for clinical applications.

## 📝 요약

최근 HL7 FHIR 표준으로의 전환은 임상 AI 분야에 새로운 도전을 제시하며, LLM 에이전트가 복잡한 자원 기반 데이터 모델을 탐색해야 합니다. 기존 벤치마크는 이러한 변화를 따라가지 못했으며, 상호운용 가능한 임상 데이터에서 최신 LLM을 평가하는 데 필요한 현실성이 부족했습니다. 이를 해결하기 위해 우리는 2,931개의 실제 임상 질문을 HL7 FHIR 표준에 기반한 FHIR-AgentBench 벤치마크를 소개합니다. 이 벤치마크를 통해 다양한 데이터 검색 전략, 상호작용 패턴, 추론 전략을 체계적으로 평가했습니다. 실험 결과, 복잡한 FHIR 자원에서 데이터를 검색하고 이를 기반으로 추론하는 데 실질적인 어려움이 있으며, 이는 질문 응답 성능에 중요한 영향을 미친다는 것을 발견했습니다. 우리는 FHIR-AgentBench 데이터셋과 평가 도구를 공개하여 임상 응용을 위한 견고하고 신뢰할 수 있는 LLM 에이전트 개발을 촉진하고자 합니다.

## 🎯 주요 포인트

- 1. HL7 FHIR 표준으로의 전환은 임상 AI에 새로운 도전 과제를 제시하며, LLM 에이전트가 복잡한 자원 기반 데이터 모델을 탐색해야 합니다.
- 2. 기존 벤치마크는 상호운용 가능한 임상 데이터를 평가하는 데 필요한 현실성이 부족하여 최근 LLM 평가에 적합하지 않습니다.
- 3. FHIR-AgentBench는 2,931개의 실제 임상 질문을 HL7 FHIR 표준에 기반하여 평가하기 위한 벤치마크를 제공합니다.
- 4. 실험 결과, 복잡한 FHIR 자원에서 데이터를 검색하고 이를 기반으로 추론하는 데 실질적인 어려움이 있음을 강조합니다.
- 5. FHIR-AgentBench 데이터셋과 평가 도구를 공개하여 임상 응용을 위한 강력하고 신뢰할 수 있는 LLM 에이전트 개발을 촉진합니다.


---

*Generated on 2025-09-25 15:22:56*