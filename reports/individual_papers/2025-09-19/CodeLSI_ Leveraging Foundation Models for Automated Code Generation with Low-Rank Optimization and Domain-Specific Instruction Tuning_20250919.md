
# CodeLSI: Leveraging Foundation Models for Automated Code Generation with Low-Rank Optimization and Domain-Specific Instruction Tuning

**Korean Title:** CodeLSI: 저차원 최적화 및 도메인 특화 명령어 튜닝을 통한 자동 코드 생성에 기초 모델 활용

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Low-rank Optimization, Domain-specific Instruction Tuning

## 🔗 유사한 논문
- [[Do Code Semantics Help_ A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models_20250919|Do Code Semantics Help A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models]] (83.1% similar)
- [[An LLM Agentic Approach for Legal-Critical Software A Case Study for Tax Prep Software]] (81.9% similar)
- [[Automated and Context-Aware Code Documentation Leveraging Advanced LLMs_20250919|Automated and Context-Aware Code Documentation Leveraging Advanced LLMs]] (81.8% similar)
- [[Evolution of Kernels Automated RISC-V Kernel Optimization with Large Language Models]] (81.7% similar)
- [[LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (81.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14373v1 Announce Type: new 
Abstract: Context: Automated code generation using Foundation Models (FMs) offers promising solutions for enhancing software development efficiency. However, challenges remain in ensuring domain specificity, cost-effectiveness, and security - especially when relying on third-party APIs. This paper introduces CodeLSI, a framework that combines low-rank optimization and domain-specific instruction tuning to address these challenges.
  Objectives: The aim of this study is to develop and evaluate CodeLSI, a novel approach for generating high-quality code tailored to specific domains, using FMs fine-tuned on company infrastructure without dependence on external APIs.
  Methods: CodeLSI applies low-rank adaptation techniques to reduce the computational cost of model pre-training and fine-tuning. Domain-specific instruction tuning is employed to align code generation with organizational needs. We implemented and tested the framework on real-world JavaScript coding tasks using datasets drawn from internal software projects.
  Results: Experimental evaluations show that CodeLSI produces high-quality, context aware code. It outperforms baseline models in terms of relevance, accuracy, and domain fit. The use of low-rank optimization significantly reduced resource requirements, enabling scalable training on company-owned infrastructure.
  Conclusion: CodeLSI demonstrates that combining low-rank optimization with domain specific tuning can enhance the practicality and performance of FMs for automated code generation. This approach provides a secure, cost-efficient alternative to commercial API based solutions and supports faster, more targeted innovation in software development.

## 🔍 Abstract (한글 번역)

arXiv:2509.14373v1 발표 유형: 신규  
초록: 배경: 파운데이션 모델(FM)을 활용한 자동 코드 생성은 소프트웨어 개발 효율성을 향상시키기 위한 유망한 솔루션을 제공합니다. 그러나 도메인 특화, 비용 효율성, 보안 - 특히 서드파티 API에 의존할 때 - 에 대한 문제는 여전히 남아 있습니다. 본 논문은 이러한 문제를 해결하기 위해 저순위 최적화와 도메인 특화 명령어 튜닝을 결합한 프레임워크인 CodeLSI를 소개합니다.  
목적: 본 연구의 목적은 외부 API에 의존하지 않고 회사 인프라에서 미세 조정된 FM을 사용하여 특정 도메인에 맞춘 고품질 코드를 생성하는 새로운 접근 방식인 CodeLSI를 개발하고 평가하는 것입니다.  
방법: CodeLSI는 모델 사전 훈련 및 미세 조정의 계산 비용을 줄이기 위해 저순위 적응 기법을 적용합니다. 도메인 특화 명령어 튜닝은 코드 생성이 조직의 요구에 맞도록 조정됩니다. 우리는 내부 소프트웨어 프로젝트에서 수집한 데이터셋을 사용하여 실제 JavaScript 코딩 작업에 프레임워크를 구현하고 테스트했습니다.  
결과: 실험적 평가 결과, CodeLSI는 높은 품질의 컨텍스트 인식 코드를 생성하는 것으로 나타났습니다. 관련성, 정확성, 도메인 적합성 측면에서 기준 모델보다 우수합니다. 저순위 최적화를 사용하여 리소스 요구 사항을 크게 줄였으며, 회사 소유 인프라에서의 확장 가능한 훈련을 가능하게 했습니다.  
결론: CodeLSI는 저순위 최적화와 도메인 특화 튜닝을 결합함으로써 FM의 자동 코드 생성 실용성과 성능을 향상시킬 수 있음을 보여줍니다. 이 접근 방식은 상업적 API 기반 솔루션에 대한 안전하고 비용 효율적인 대안을 제공하며, 소프트웨어 개발에서 더 빠르고 목표 지향적인 혁신을 지원합니다.

## 📝 요약

이 논문은 자동 코드 생성을 위한 프레임워크인 CodeLSI를 소개합니다. CodeLSI는 저순위 최적화와 도메인 특화 지침 조정을 결합하여, 외부 API에 의존하지 않고 기업 인프라에서 고품질의 도메인 맞춤형 코드를 생성합니다. 저순위 적응 기법을 사용하여 모델의 사전 훈련 및 미세 조정의 계산 비용을 줄이고, 도메인 특화 지침 조정을 통해 조직의 요구에 맞춘 코드 생성을 수행합니다. 실험 결과, CodeLSI는 기존 모델보다 높은 관련성, 정확성, 도메인 적합성을 보이며, 리소스 요구를 크게 줄여 기업 소유 인프라에서의 확장 가능한 훈련을 가능하게 했습니다. 이 접근법은 상업적 API 기반 솔루션에 대한 안전하고 비용 효율적인 대안을 제공하며, 소프트웨어 개발에서 더 빠르고 목표 지향적인 혁신을 지원합니다.

## 🎯 주요 포인트

- 1. CodeLSI는 저랭크 최적화와 도메인 특화 튜닝을 결합하여 자동 코드 생성의 실용성과 성능을 향상시킵니다.

- 2. 외부 API에 의존하지 않고 회사 인프라에서 파인튜닝된 FMs를 사용하여 특정 도메인에 맞춘 고품질 코드를 생성합니다.

- 3. 저랭크 적응 기술을 적용하여 모델의 사전 훈련 및 파인튜닝의 계산 비용을 절감합니다.

- 4. 실험 결과, CodeLSI는 관련성, 정확성, 도메인 적합성 측면에서 기존 모델보다 우수한 성능을 보였습니다.

- 5. 이 접근법은 상업적 API 기반 솔루션에 대한 안전하고 비용 효율적인 대안을 제공하며, 소프트웨어 개발에서 더 빠르고 목표 지향적인 혁신을 지원합니다.

---

*Generated on 2025-09-19 16:40:19*