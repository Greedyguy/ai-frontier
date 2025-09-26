<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:42:47.641450",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Retrieval Augmented Generation",
    "Workflow Provenance",
    "Metadata-Driven Design"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Retrieval Augmented Generation": 0.78,
    "Workflow Provenance": 0.7,
    "Metadata-Driven Design": 0.65
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
        "rationale": "Large Language Models are central to the paper's approach, enabling interactive data analysis.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Retrieval-Augmented Generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "RAG is a trending technique that enhances LLM capabilities, relevant to the paper's methodology.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "workflow provenance",
        "canonical": "Workflow Provenance",
        "aliases": [
          "provenance data"
        ],
        "category": "unique_technical",
        "rationale": "Workflow provenance is a unique technical concept crucial for understanding data lineage in scientific workflows.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "metadata-driven design",
        "canonical": "Metadata-Driven Design",
        "aliases": [
          "metadata approach"
        ],
        "category": "unique_technical",
        "rationale": "This design approach is key to the paper's methodology, facilitating natural language query translation.",
        "novelty_score": 0.68,
        "connectivity_score": 0.55,
        "specificity_score": 0.78,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "methodology",
      "evaluation",
      "architecture"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Model",
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
      "candidate_surface": "Retrieval-Augmented Generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "workflow provenance",
      "resolved_canonical": "Workflow Provenance",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "metadata-driven design",
      "resolved_canonical": "Metadata-Driven Design",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.55,
        "specificity": 0.78,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# LLM Agents for Interactive Workflow Provenance: Reference Architecture and Evaluation Methodology

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.13978.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.13978](https://arxiv.org/abs/2509.13978)

## 🔗 유사한 논문
- [[2025-09-19/An LLM-based multi-agent framework for agile effort estimation_20250919|An LLM-based multi-agent framework for agile effort estimation]] (84.3% similar)
- [[2025-09-19/(P)rior(D)yna(F)low_ A Priori Dynamic Workflow Construction via Multi-Agent Collaboration_20250919|(P)rior(D)yna(F)low: A Priori Dynamic Workflow Construction via Multi-Agent Collaboration]] (83.9% similar)
- [[2025-09-24/Difficulty-Aware Agent Orchestration in LLM-Powered Workflows_20250924|Difficulty-Aware Agent Orchestration in LLM-Powered Workflows]] (83.7% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (83.6% similar)
- [[2025-09-18/An LLM Agentic Approach for Legal-Critical Software_ A Case Study for Tax Prep Software_20250918|An LLM Agentic Approach for Legal-Critical Software: A Case Study for Tax Prep Software]] (83.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]]
**⚡ Unique Technical**: [[keywords/Workflow Provenance|Workflow Provenance]], [[keywords/Metadata-Driven Design|Metadata-Driven Design]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13978v2 Announce Type: replace-cross 
Abstract: Modern scientific discovery increasingly relies on workflows that process data across the Edge, Cloud, and High Performance Computing (HPC) continuum. Comprehensive and in-depth analyses of these data are critical for hypothesis validation, anomaly detection, reproducibility, and impactful findings. Although workflow provenance techniques support such analyses, at large scale, the provenance data become complex and difficult to analyze. Existing systems depend on custom scripts, structured queries, or static dashboards, limiting data interaction. In this work, we introduce an evaluation methodology, reference architecture, and open-source implementation that leverages interactive Large Language Model (LLM) agents for runtime data analysis. Our approach uses a lightweight, metadata-driven design that translates natural language into structured provenance queries. Evaluations across LLaMA, GPT, Gemini, and Claude, covering diverse query classes and a real-world chemistry workflow, show that modular design, prompt tuning, and Retrieval-Augmented Generation (RAG) enable accurate and insightful LLM agent responses beyond recorded provenance.

## 📝 요약

이 논문은 엣지, 클라우드, 고성능 컴퓨팅(HPC) 환경에서 데이터를 처리하는 워크플로우의 분석을 개선하기 위한 방법론을 제안합니다. 기존의 워크플로우 계보 데이터 분석은 복잡하고 상호작용이 제한적이었으나, 본 연구에서는 대화형 대형 언어 모델(LLM) 에이전트를 활용하여 자연어를 구조화된 쿼리로 변환하는 경량 메타데이터 기반 설계를 도입합니다. LLaMA, GPT, Gemini, Claude 모델을 사용한 평가 결과, 모듈식 설계와 프롬프트 튜닝, 검색 증강 생성(RAG) 기법이 정확하고 통찰력 있는 분석을 가능하게 함을 보여줍니다.

## 🎯 주요 포인트

- 1. 현대 과학 발견은 엣지, 클라우드, 고성능 컴퓨팅(HPC) 연속체를 아우르는 워크플로우에 점점 더 의존하고 있습니다.
- 2. 대규모에서의 워크플로우 출처 데이터는 복잡하고 분석하기 어려워 기존 시스템은 사용자 정의 스크립트, 구조화된 쿼리 또는 정적 대시보드에 의존합니다.
- 3. 본 연구는 상호작용적인 대형 언어 모델(LLM) 에이전트를 활용한 런타임 데이터 분석을 위한 평가 방법론, 참조 아키텍처 및 오픈 소스 구현을 소개합니다.
- 4. 자연어를 구조화된 출처 쿼리로 변환하는 경량의 메타데이터 기반 설계를 사용하여 다양한 쿼리 클래스와 실제 화학 워크플로우에 대한 평가를 수행했습니다.
- 5. 모듈식 설계, 프롬프트 튜닝, 검색 증강 생성(RAG)을 통해 기록된 출처를 넘어 정확하고 통찰력 있는 LLM 에이전트 응답을 가능하게 합니다.


---

*Generated on 2025-09-24 14:42:47*