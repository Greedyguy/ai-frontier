---
keywords:
  - Large Language Models
  - RISC-V Kernel Optimization
  - Evolution of Kernels
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14265
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:44:58.292762",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "RISC-V Kernel Optimization",
    "Evolution of Kernels"
  ],
  "rejected_keywords": [
    "Retrieval-Augmented Generation"
  ],
  "similarity_scores": {
    "Large Language Models": 0.8,
    "RISC-V Kernel Optimization": 0.78,
    "Evolution of Kernels": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Evolution of Kernels: Automated RISC-V Kernel Optimization with Large Language Models

**Korean Title:** 커널의 진화: 대형 언어 모델을 활용한 자동화된 RISC-V 커널 최적화

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Large Language Models|Large Language Models]]
**⚡ Unique Technical**: [[keywords/RISC-V Kernel Optimization|RISC-V Kernel Optimization]], [[keywords/Evolution of Kernels|Evolution of Kernels]]

## 🔗 유사한 논문
- [[LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (81.1% similar)
- [[TopoSizing An LLM-aided Framework of Topology-based Understanding and Sizing for AMS Circuits]] (80.4% similar)
- [[(P)rior(D)yna(F)low A Priori Dynamic Workflow Construction via Multi-Agent Collaboration]] (79.9% similar)
- [[Using LLMs in Generating Design Rationale for Software Architecture Decisions]] (79.4% similar)
- [[From Legacy Fortran to Portable Kokkos An Autonomous Agentic AI Workflow]] (79.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14265v1 Announce Type: cross 
Abstract: Automated kernel design is critical for overcoming software ecosystem barriers in emerging hardware platforms like RISC-V. While large language models (LLMs) have shown promise for automated kernel optimization, demonstrating success in CUDA domains with comprehensive technical documents and mature codebases, their effectiveness remains unproven for reference-scarce domains like RISC-V. We present Evolution of Kernels (EoK), a novel LLM-based evolutionary program search framework that automates kernel design for domains with limited reference material. EoK mitigates reference scarcity by mining and formalizing reusable optimization ideas (general design principles + actionable thoughts) from established kernel libraries' development histories; it then guides parallel LLM explorations using these ideas, enriched via Retrieval-Augmented Generation (RAG) with RISC-V-specific context, prioritizing historically effective techniques. Empirically, EoK achieves a median 1.27x speedup, surpassing human experts on all 80 evaluated kernel design tasks and improving upon prior LLM-based automated kernel design methods by 20%. These results underscore the viability of incorporating human experience into emerging domains and highlight the immense potential of LLM-based automated kernel optimization.

## 🔍 Abstract (한글 번역)

arXiv:2509.14265v1 발표 유형: 교차  
초록: 자동화된 커널 설계는 RISC-V와 같은 신흥 하드웨어 플랫폼에서 소프트웨어 생태계의 장벽을 극복하는 데 중요합니다. 대형 언어 모델(LLM)은 포괄적인 기술 문서와 성숙한 코드베이스를 갖춘 CUDA 도메인에서 자동화된 커널 최적화의 가능성을 보여주었지만, 참조 자료가 부족한 RISC-V와 같은 도메인에서는 그 효과가 입증되지 않았습니다. 우리는 Evolution of Kernels (EoK)을 소개합니다. 이는 제한된 참조 자료를 가진 도메인에서 커널 설계를 자동화하는 새로운 LLM 기반 진화적 프로그램 검색 프레임워크입니다. EoK는 확립된 커널 라이브러리의 개발 이력에서 재사용 가능한 최적화 아이디어(일반 설계 원칙 + 실행 가능한 생각)를 발굴하고 공식화하여 참조 부족 문제를 완화합니다. 그런 다음 이러한 아이디어를 사용하여 병렬 LLM 탐색을 안내하며, RISC-V 특정 컨텍스트로 보강된 검색-증강 생성(RAG)을 통해 역사적으로 효과적인 기술을 우선시합니다. 실험적으로, EoK는 평가된 80개의 커널 설계 작업에서 인간 전문가를 능가하며, 이전 LLM 기반 자동 커널 설계 방법보다 20% 개선된 중간값 1.27배의 속도 향상을 달성합니다. 이러한 결과는 신흥 도메인에 인간의 경험을 통합하는 것의 실현 가능성을 강조하며, LLM 기반 자동 커널 최적화의 엄청난 잠재력을 부각시킵니다.

## 📝 요약

이 논문은 RISC-V와 같은 신흥 하드웨어 플랫폼에서 소프트웨어 생태계의 장벽을 극복하기 위한 자동화된 커널 설계의 중요성을 다룹니다. 기존의 대형 언어 모델(LLM)이 CUDA와 같은 성숙한 코드베이스에서 커널 최적화에 성공했지만, RISC-V와 같은 참고 자료가 부족한 분야에서는 그 효과가 입증되지 않았습니다. 이를 해결하기 위해, 논문은 제한된 참고 자료를 가진 분야에서 커널 설계를 자동화하는 새로운 LLM 기반의 진화적 프로그램 탐색 프레임워크인 EoK를 제안합니다. EoK는 기존 커널 라이브러리의 개발 역사를 통해 재사용 가능한 최적화 아이디어를 추출하고, RISC-V에 특화된 문맥을 사용해 병렬 LLM 탐색을 안내합니다. 실험 결과, EoK는 80개의 커널 설계 과제에서 인간 전문가를 능가하며, 이전 LLM 기반 방법보다 20% 향상된 성능을 보였습니다. 이는 신흥 분야에 인간 경험을 통합하는 것의 가능성을 보여주며, LLM 기반 자동화 커널 최적화의 잠재력을 강조합니다.

## 🎯 주요 포인트

- 1. EoK는 참조 자료가 부족한 도메인에서도 커널 설계를 자동화하는 LLM 기반 진화적 프로그램 탐색 프레임워크입니다.

- 2. EoK는 기존 커널 라이브러리의 개발 역사를 통해 재사용 가능한 최적화 아이디어를 발굴하고 형식화하여 참조 부족 문제를 해결합니다.

- 3. RISC-V 특정 문맥을 활용한 Retrieval-Augmented Generation (RAG)을 통해 병렬 LLM 탐색을 안내하며, 역사적으로 효과적인 기술을 우선시합니다.

- 4. EoK는 80개의 커널 설계 작업에서 인간 전문가를 능가하며, 기존 LLM 기반 자동 커널 설계 방법보다 20% 향상된 1.27배의 중간 속도 향상을 달성했습니다.

- 5. 이 연구는 인간 경험을 신흥 도메인에 통합하는 것의 가능성을 강조하며, LLM 기반 자동 커널 최적화의 잠재력을 부각합니다.

---

*Generated on 2025-09-19 14:51:44*