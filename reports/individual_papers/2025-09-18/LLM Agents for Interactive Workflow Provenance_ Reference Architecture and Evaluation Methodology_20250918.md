---
keywords:
  - Retrieval-Augmented Generation
  - Large Language Models
  - Workflow Provenance
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.13978
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:23:51.562268",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Retrieval-Augmented Generation",
    "Large Language Models",
    "Workflow Provenance"
  ],
  "rejected_keywords": [
    "Modular Design"
  ],
  "similarity_scores": {
    "Retrieval-Augmented Generation": 0.78,
    "Large Language Models": 0.8,
    "Workflow Provenance": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# LLM Agents for Interactive Workflow Provenance: Reference Architecture and Evaluation Methodology

**Korean Title:** LLM 에이전트 기반 상호작용 워크플로 프로버넌스: 참조 아키텍처 및 평가 방법론

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Large Language Models|Large Language Model agents]]
**⚡ Unique Technical**: [[keywords/Workflow Provenance|workflow provenance]]
**🚀 Evolved Concepts**: [[keywords/Retrieval-Augmented Generation|Retrieval-Augmented Generation]]

## 🔗 유사한 논문
- [[An LLM Agentic Approach for Legal-Critical Software A Case Study for Tax Prep Software]] (83.5% similar)
- [[From Automation to Autonomy A Survey on Large Language Models in Scientific Discovery]] (83.1% similar)
- [[AppAgent v2 Advanced Agent for Flexible Mobile Interactions]] (82.6% similar)
- [[Meta-Learning Linear Models for Molecular Property Prediction]] (81.8% similar)
- [[LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (81.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13978v1 Announce Type: cross 
Abstract: Modern scientific discovery increasingly relies on workflows that process data across the Edge, Cloud, and High Performance Computing (HPC) continuum. Comprehensive and in-depth analyses of these data are critical for hypothesis validation, anomaly detection, reproducibility, and impactful findings. Although workflow provenance techniques support such analyses, at large scale, the provenance data become complex and difficult to analyze. Existing systems depend on custom scripts, structured queries, or static dashboards, limiting data interaction. In this work, we introduce an evaluation methodology, reference architecture, and open-source implementation that leverages interactive Large Language Model (LLM) agents for runtime data analysis. Our approach uses a lightweight, metadata-driven design that translates natural language into structured provenance queries. Evaluations across LLaMA, GPT, Gemini, and Claude, covering diverse query classes and a real-world chemistry workflow, show that modular design, prompt tuning, and Retrieval-Augmented Generation (RAG) enable accurate and insightful LLM agent responses beyond recorded provenance.

## 🔍 Abstract (한글 번역)

arXiv:2509.13978v1 공지 유형: cross
초록: 현대 과학적 발견은 엣지(Edge), 클라우드(Cloud), 고성능 컴퓨팅(HPC) 연속체 전반에 걸쳐 데이터를 처리하는 워크플로우에 점점 더 의존하고 있다. 이러한 데이터에 대한 포괄적이고 심층적인 분석은 가설 검증, 이상 탐지, 재현성, 그리고 영향력 있는 발견에 있어 매우 중요하다. 워크플로우 프로버넌스(provenance) 기법이 이러한 분석을 지원하지만, 대규모에서는 프로버넌스 데이터가 복잡해지고 분석하기 어려워진다. 기존 시스템은 맞춤형 스크립트, 구조화된 질의, 또는 정적 대시보드에 의존하여 데이터 상호작용을 제한한다. 본 연구에서는 런타임 데이터 분석을 위해 상호작용적 대규모 언어 모델(LLM) 에이전트를 활용하는 평가 방법론, 참조 아키텍처, 그리고 오픈소스 구현을 소개한다. 우리의 접근법은 자연어를 구조화된 프로버넌스 질의로 변환하는 경량의 메타데이터 기반 설계를 사용한다. 다양한 질의 클래스와 실제 화학 워크플로우를 포괄하는 LLaMA, GPT, Gemini, Claude에 대한 평가는 모듈화 설계, 프롬프트 튜닝, 그리고 검색 증강 생성(RAG)이 기록된 프로버넌스를 넘어서는 정확하고 통찰력 있는 LLM 에이전트 응답을 가능하게 함을 보여준다.

## 📝 요약

이 논문은 엣지, 클라우드, 고성능 컴퓨팅(HPC) 환경에서 데이터를 처리하는 워크플로우의 분석을 개선하기 위한 방법론을 제안합니다. 기존의 워크플로우 계보 데이터 분석은 복잡하고 상호작용이 제한적이었으나, 저자들은 대화형 대형 언어 모델(LLM) 에이전트를 활용하여 이를 개선하고자 합니다. 이 방법론은 자연어를 구조화된 계보 쿼리로 변환하는 경량 메타데이터 기반 설계를 사용합니다. LLaMA, GPT, Gemini, Claude 모델을 활용한 평가에서, 모듈형 설계, 프롬프트 튜닝, 검색 증강 생성(RAG)을 통해 정확하고 통찰력 있는 분석이 가능함을 입증했습니다.

## 🎯 주요 포인트

- 1. 현대 과학 발견은 엣지, 클라우드, 고성능 컴퓨팅(HPC) 연속체 전반에 걸쳐 데이터를 처리하는 워크플로우에 의존하고 있습니다.

- 2. 대규모에서의 워크플로우 출처 데이터는 복잡하고 분석하기 어려워 기존 시스템은 사용자 정의 스크립트나 정적 대시보드에 의존합니다.

- 3. 본 연구는 대화형 대형 언어 모델(LLM) 에이전트를 활용한 런타임 데이터 분석을 위한 평가 방법론, 참조 아키텍처, 오픈 소스 구현을 제안합니다.

- 4. 자연어를 구조화된 출처 쿼리로 변환하는 경량의 메타데이터 기반 설계를 사용하여 다양한 쿼리 클래스와 실제 화학 워크플로우에서 정확하고 통찰력 있는 응답을 제공합니다.

- 5. 모듈식 설계, 프롬프트 튜닝, 검색 증강 생성(RAG)을 통해 기록된 출처를 넘어서는 정확한 LLM 에이전트 응답이 가능함을 보여줍니다.

---

*Generated on 2025-09-19 10:47:17*