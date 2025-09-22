
# SWE-QA: Can Language Models Answer Repository-level Code Questions?

**Korean Title:** SWE-QA: 언어 모델이 저장소 수준의 코드 질문에 답할 수 있는가?

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Repository-level Question Answering

## 🔗 유사한 논문
- [[An Empirical Study on Failures in Automated Issue Solving]] (83.9% similar)
- [[Self-Guided Function Calling in Large Language Models via Stepwise Experience Recall_20250918|Self-Guided Function Calling in Large Language Models via Stepwise Experience Recall]] (82.5% similar)
- [[MovieCORE COgnitive REasoning in Movies]] (81.2% similar)
- [[LLM Agents for Interactive Workflow Provenance Reference Architecture and Evaluation Methodology]] (80.7% similar)
- [[Do Code Semantics Help_ A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models_20250919|Do Code Semantics Help A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models]] (80.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14635v1 Announce Type: new 
Abstract: Understanding and reasoning about entire software repositories is an essential capability for intelligent software engineering tools. While existing benchmarks such as CoSQA and CodeQA have advanced the field, they predominantly focus on small, self-contained code snippets. These setups fail to capture the complexity of real-world repositories, where effective understanding and reasoning often require navigating multiple files, understanding software architecture, and grounding answers in long-range code dependencies. In this paper, we present SWE-QA, a repository-level code question answering (QA) benchmark designed to facilitate research on automated QA systems in realistic code environments. SWE-QA involves 576 high-quality question-answer pairs spanning diverse categories, including intention understanding, cross-file reasoning, and multi-hop dependency analysis. To construct SWE-QA, we first crawled 77,100 GitHub issues from 11 popular repositories. Based on an analysis of naturally occurring developer questions extracted from these issues, we developed a two-level taxonomy of repository-level questions and constructed a set of seed questions for each category. For each category, we manually curated and validated questions and collected their corresponding answers. As a prototype application, we further develop SWE-QA-Agent, an agentic framework in which LLM agents reason and act to find answers automatically. We evaluate six advanced LLMs on SWE-QA under various context augmentation strategies. Experimental results highlight the promise of LLMs, particularly our SWE-QA-Agent framework, in addressing repository-level QA, while also revealing open challenges and pointing to future research directions.

## 🔍 Abstract (한글 번역)

arXiv:2509.14635v1 발표 유형: 신규  
초록: 전체 소프트웨어 저장소에 대한 이해와 추론은 지능형 소프트웨어 엔지니어링 도구에 필수적인 능력입니다. CoSQA와 CodeQA와 같은 기존 벤치마크는 이 분야를 발전시켰지만, 주로 작고 독립적인 코드 조각에 초점을 맞추고 있습니다. 이러한 설정은 실제 저장소의 복잡성을 포착하지 못하며, 효과적인 이해와 추론은 종종 여러 파일을 탐색하고, 소프트웨어 아키텍처를 이해하며, 장거리 코드 종속성에 기반한 답변을 요구합니다. 이 논문에서는 현실적인 코드 환경에서 자동화된 QA 시스템에 대한 연구를 촉진하기 위해 설계된 저장소 수준의 코드 질문 응답(QA) 벤치마크인 SWE-QA를 소개합니다. SWE-QA는 의도 이해, 파일 간 추론, 다중 홉 종속성 분석을 포함한 다양한 범주에 걸쳐 576개의 고품질 질문-답변 쌍을 포함합니다. SWE-QA를 구성하기 위해, 우리는 11개의 인기 있는 저장소에서 77,100개의 GitHub 이슈를 수집했습니다. 이러한 이슈에서 추출한 자연 발생 개발자 질문의 분석을 기반으로, 우리는 저장소 수준 질문의 2단계 분류 체계를 개발하고 각 범주에 대한 시드 질문 세트를 구성했습니다. 각 범주에 대해, 우리는 질문을 수동으로 큐레이션하고 검증했으며, 해당 답변을 수집했습니다. 프로토타입 응용 프로그램으로서, 우리는 LLM 에이전트가 자동으로 답을 찾기 위해 추론하고 행동하는 에이전트 프레임워크인 SWE-QA-Agent를 추가로 개발했습니다. 우리는 다양한 맥락 증강 전략 하에서 SWE-QA에 대해 여섯 가지 고급 LLM을 평가했습니다. 실험 결과는 저장소 수준 QA를 해결하는 데 있어 LLM, 특히 SWE-QA-Agent 프레임워크의 가능성을 강조하는 한편, 해결되지 않은 과제를 드러내고 미래 연구 방향을 제시합니다.

## 📝 요약

이 논문은 소프트웨어 저장소 전체를 이해하고 추론하는 능력을 갖춘 지능형 소프트웨어 엔지니어링 도구 개발을 목표로 합니다. 기존 벤치마크는 주로 작은 코드 조각에 집중하지만, 이 연구는 실제 저장소의 복잡성을 다루기 위해 SWE-QA라는 저장소 수준의 코드 질문 응답(QA) 벤치마크를 제안합니다. SWE-QA는 의도 이해, 파일 간 추론, 다중 종속성 분석 등 다양한 범주에 걸쳐 576개의 고품질 질문-답변 쌍을 포함합니다. 이를 위해 11개의 인기 있는 GitHub 저장소에서 77,100개의 이슈를 분석하여 질문을 분류하고, 각 범주에 대한 질문을 수집 및 검증했습니다. 또한, SWE-QA-Agent라는 프레임워크를 개발하여 LLM 에이전트가 자동으로 답변을 찾도록 했습니다. 실험 결과는 LLM, 특히 SWE-QA-Agent가 저장소 수준 QA 문제 해결에 유망함을 보여주며, 향후 연구 방향을 제시합니다.

## 🎯 주요 포인트

- 1. SWE-QA는 실제 코드 환경에서 자동화된 질문 답변 시스템 연구를 촉진하기 위해 설계된 리포지토리 수준의 코드 질문 답변 벤치마크입니다.

- 2. SWE-QA는 의도 이해, 파일 간 추론, 다중 의존성 분석 등 다양한 범주의 576개의 고품질 질문-답변 쌍을 포함합니다.

- 3. SWE-QA-Agent는 LLM 에이전트가 자동으로 답을 찾기 위해 추론하고 행동하는 에이전틱 프레임워크로 개발되었습니다.

- 4. SWE-QA를 통해 다양한 문맥 보강 전략 하에서 여섯 개의 고급 LLM을 평가한 결과, 리포지토리 수준의 QA에서 LLM의 가능성과 함께 해결해야 할 과제와 향후 연구 방향을 제시합니다.

---

*Generated on 2025-09-19 15:50:54*