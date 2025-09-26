---
keywords:
  - Large Language Models
  - Optimization
  - agentic framework
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14279
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:20:49.250738",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Optimization",
    "agentic framework"
  ],
  "rejected_keywords": [
    "robust-kbench",
    "evolutionary meta-generation"
  ],
  "similarity_scores": {
    "Large Language Models": 0.85,
    "Optimization": 0.78,
    "agentic framework": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization

**Korean Title:** 견고한 에이전트 CUDA 커널 벤치마킹, 검증 및 최적화를 향하여

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Optimization|CUDA kernel optimization]]
**⚡ Unique Technical**: [[keywords/agentic framework|agentic framework]]
**🚀 Evolved Concepts**: [[keywords/Large Language Models|Large Language Models]]

## 🔗 유사한 논문
- [[Evolution of Kernels Automated RISC-V Kernel Optimization with Large Language Models]] (84.0% similar)
- [[AgentCompass Towards Reliable Evaluation of Agentic Workflows in Production]] (82.8% similar)
- [[From Capabilities to Performance Evaluating Key Functional Properties of LLM Architectures in Penetration Testing]] (81.9% similar)
- [[LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (81.4% similar)
- [[From Legacy Fortran to Portable Kokkos An Autonomous Agentic AI Workflow]] (81.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14279v1 Announce Type: cross 
Abstract: Recent advances in large language models (LLMs) demonstrate their effectiveness in scaling test-time compute for software engineering tasks. However, these approaches often focus on high-level solutions, with limited attention to optimizing low-level CUDA kernel implementations. Additionally, existing kernel generation benchmarks suffer from exploitable loopholes and insufficient diversity in testing conditions, hindering true generalization assessment. To address these limitations, we introduce robust-kbench, a new benchmark for rigorous evaluation of kernel performance and correctness across varied scenarios. Furthermore, we present a comprehensive agentic framework that automates CUDA kernel discovery, verification, and optimization. This pipeline enables frontier LLMs to translate torch code to CUDA kernels and iteratively improve their runtime within our robust evaluation setting. Our sequential workflow first translates PyTorch code into equivalent CUDA kernels. It then optimizes their runtime using a novel evolutionary meta-generation procedure tailored to the CUDA ecosystem, guided by LLM-based verifiers for correctness and efficient filtering. Evaluated on robust-kbench, our approach produces CUDA kernels outperforming torch implementations for practical applications, including forward and backward passes. It can fuse operations and deploy various runtime optimization strategies. The verifier workflow accurately classifies incorrect kernels, enhancing hardware verification efficiency.

## 🔍 Abstract (한글 번역)

arXiv:2509.14279v1 발표 유형: 교차  
초록: 최근 대형 언어 모델(LLMs)의 발전은 소프트웨어 공학 작업에서 테스트 시점의 계산을 확장하는 데 있어 그 효과성을 보여주고 있습니다. 그러나 이러한 접근 방식은 종종 고수준 솔루션에 중점을 두며, 저수준 CUDA 커널 구현 최적화에는 제한적인 관심을 기울입니다. 또한, 기존의 커널 생성 벤치마크는 악용 가능한 허점과 테스트 조건의 다양성 부족으로 인해 진정한 일반화 평가를 방해합니다. 이러한 한계를 해결하기 위해, 우리는 다양한 시나리오에서 커널 성능과 정확성을 엄격하게 평가할 수 있는 새로운 벤치마크인 robust-kbench를 소개합니다. 더 나아가, CUDA 커널 탐색, 검증 및 최적화를 자동화하는 포괄적인 에이전틱 프레임워크를 제시합니다. 이 파이프라인은 최첨단 LLM이 torch 코드를 CUDA 커널로 변환하고, 우리의 강력한 평가 환경 내에서 실행 시간을 반복적으로 개선할 수 있게 합니다. 우리의 순차적 워크플로우는 먼저 PyTorch 코드를 동등한 CUDA 커널로 변환합니다. 그런 다음, CUDA 생태계에 맞춘 새로운 진화적 메타 생성 절차를 사용하여 실행 시간을 최적화하며, LLM 기반 검증자를 통해 정확성과 효율적인 필터링을 안내합니다. robust-kbench에서 평가한 결과, 우리의 접근 방식은 torch 구현을 능가하는 CUDA 커널을 생성하여, 순방향 및 역방향 패스를 포함한 실제 응용 프로그램에 적용할 수 있습니다. 이는 연산을 융합하고 다양한 실행 시간 최적화 전략을 배포할 수 있습니다. 검증자 워크플로우는 잘못된 커널을 정확하게 분류하여 하드웨어 검증 효율성을 향상시킵니다.

## 📝 요약

최근 대형 언어 모델(LLM)의 발전은 소프트웨어 엔지니어링 작업에서의 성능을 입증했지만, 저수준의 CUDA 커널 구현 최적화에는 한계가 있었습니다. 이를 해결하기 위해 다양한 시나리오에서 커널 성능과 정확성을 평가할 수 있는 새로운 벤치마크인 robust-kbench를 소개합니다. 또한, CUDA 커널의 발견, 검증 및 최적화를 자동화하는 포괄적인 에이전트 프레임워크를 제안합니다. 이 프레임워크는 PyTorch 코드를 CUDA 커널로 변환하고, LLM 기반 검증기를 통해 정확성과 효율성을 높이며, 새로운 진화적 메타 생성 절차를 통해 런타임을 최적화합니다. robust-kbench 평가 결과, 우리의 접근 방식은 실제 응용 프로그램에서 torch 구현보다 우수한 CUDA 커널을 생성하며, 다양한 런타임 최적화 전략을 적용할 수 있습니다. 검증 워크플로는 잘못된 커널을 정확히 분류하여 하드웨어 검증 효율성을 높입니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)은 소프트웨어 엔지니어링 작업에서 테스트 시간 계산을 확장하는 데 효과적임을 보여주었지만, 저수준 CUDA 커널 구현 최적화에는 제한적인 관심을 두고 있습니다.

- 2. 기존 커널 생성 벤치마크는 취약점이 있으며, 테스트 조건의 다양성이 부족하여 일반화 평가에 한계가 있습니다.

- 3. robust-kbench라는 새로운 벤치마크를 도입하여 다양한 시나리오에서 커널 성능과 정확성을 엄격하게 평가합니다.

- 4. CUDA 커널 발견, 검증 및 최적화를 자동화하는 포괄적인 에이전틱 프레임워크를 제시하여, PyTorch 코드를 CUDA 커널로 변환하고 런타임을 개선합니다.

- 5. 제안된 방법은 robust-kbench에서 평가된 결과, 실제 응용 프로그램에서 torch 구현보다 뛰어난 CUDA 커널을 생성하며, 다양한 런타임 최적화 전략을 활용합니다.

---

*Generated on 2025-09-19 14:53:13*