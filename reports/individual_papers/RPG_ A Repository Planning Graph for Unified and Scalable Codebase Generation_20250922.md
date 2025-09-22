# RPG: A Repository Planning Graph for Unified and Scalable Codebase Generation

**Korean Title:** RPG: 통합적이고 확장 가능한 코드베이스 생성을 위한 저장소 계획 그래프

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Graph-guided Code Generation

## 🔗 유사한 논문
- [[2025-09-18/KGCompass_ Knowledge Graph Enhanced Repository-Level Software Repair_20250918|KGCompass Knowledge Graph Enhanced Repository-Level Software Repair]] (80.4% similar)
- [[2025-09-19/SWE-QA_ Can Language Models Answer Repository-level Code Questions_20250919|SWE-QA Can Language Models Answer Repository-level Code Questions]] (79.4% similar)
- [[2025-09-22/Relevance to Utility_ Process-Supervised Rewrite for RAG_20250922|Relevance to Utility Process-Supervised Rewrite for RAG]] (78.8% similar)
- [[2025-09-19/On the Use of Agentic Coding_ An Empirical Study of Pull Requests on GitHub_20250919|On the Use of Agentic Coding An Empirical Study of Pull Requests on GitHub]] (78.1% similar)
- [[2025-09-19/CodeLSI_ Leveraging Foundation Models for Automated Code Generation with Low-Rank Optimization and Domain-Specific Instruction Tuning_20250919|CodeLSI Leveraging Foundation Models for Automated Code Generation with Low-Rank Optimization and Domain-Specific Instruction Tuning]] (77.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16198v1 Announce Type: cross 
Abstract: Large language models excel at function- and file-level code generation, yet generating complete repositories from scratch remains a fundamental challenge. This process demands coherent and reliable planning across proposal- and implementation-level stages, while natural language, due to its ambiguity and verbosity, is ill-suited for faithfully representing complex software structures. To address this, we introduce the Repository Planning Graph (RPG), a persistent representation that unifies proposal- and implementation-level planning by encoding capabilities, file structures, data flows, and functions in one graph. RPG replaces ambiguous natural language with an explicit blueprint, enabling long-horizon planning and scalable repository generation. Building on RPG, we develop ZeroRepo, a graph-driven framework for repository generation from scratch. It operates in three stages: proposal-level planning and implementation-level refinement to construct the graph, followed by graph-guided code generation with test validation. To evaluate this setting, we construct RepoCraft, a benchmark of six real-world projects with 1,052 tasks. On RepoCraft, ZeroRepo produces repositories averaging nearly 36K LOC, roughly 3.9$\times$ the strongest baseline (Claude Code) and about 64$\times$ other baselines. It attains 81.5% functional coverage and a 69.7% pass rate, exceeding Claude Code by 27.3 and 35.8 percentage points, respectively. Further analysis shows that RPG models complex dependencies, enables progressively more sophisticated planning through near-linear scaling, and enhances LLM understanding of repositories, thereby accelerating agent localization.

## 🔍 Abstract (한글 번역)

arXiv:2509.16198v1 발표 유형: 교차  
초록: 대형 언어 모델은 함수 및 파일 수준의 코드 생성에서 뛰어난 성능을 보이지만, 처음부터 완전한 저장소를 생성하는 것은 여전히 근본적인 도전 과제로 남아 있습니다. 이 과정은 제안 및 구현 수준의 단계에서 일관되고 신뢰할 수 있는 계획을 요구하며, 자연어는 그 모호함과 장황함 때문에 복잡한 소프트웨어 구조를 충실하게 표현하기에 적합하지 않습니다. 이를 해결하기 위해 우리는 제안 및 구현 수준의 계획을 통합하여 기능, 파일 구조, 데이터 흐름 및 기능을 하나의 그래프로 인코딩하는 지속적인 표현인 저장소 계획 그래프(Repository Planning Graph, RPG)를 소개합니다. RPG는 모호한 자연어를 명확한 청사진으로 대체하여 장기 계획 및 확장 가능한 저장소 생성을 가능하게 합니다. RPG를 기반으로 우리는 처음부터 저장소 생성을 위한 그래프 기반 프레임워크인 ZeroRepo를 개발합니다. 이는 그래프를 구성하기 위한 제안 수준의 계획 및 구현 수준의 정제, 그리고 테스트 검증을 통한 그래프 안내 코드 생성의 세 단계로 작동합니다. 이 설정을 평가하기 위해 우리는 1,052개의 작업을 포함한 6개의 실제 프로젝트 벤치마크인 RepoCraft를 구성합니다. RepoCraft에서 ZeroRepo는 평균 약 36K LOC의 저장소를 생성하며, 이는 가장 강력한 기준선(Claude Code)의 약 3.9배, 다른 기준선의 약 64배에 해당합니다. ZeroRepo는 81.5%의 기능적 커버리지와 69.7%의 통과율을 달성하여 각각 Claude Code를 27.3 및 35.8 퍼센트 포인트 초과합니다. 추가 분석 결과, RPG는 복잡한 종속성을 모델링하고, 거의 선형적인 확장을 통해 점진적으로 더 정교한 계획을 가능하게 하며, 저장소에 대한 대형 언어 모델의 이해를 향상시켜 에이전트의 위치 파악을 가속화하는 것으로 나타났습니다.

## 📝 요약

이 논문은 대형 언어 모델이 코드 생성에 뛰어나지만, 전체 저장소를 처음부터 생성하는 데 어려움이 있음을 지적합니다. 이를 해결하기 위해 제안된 '저장소 계획 그래프(RPG)'는 제안 및 구현 단계의 계획을 통합하여 명확한 청사진을 제공합니다. RPG를 기반으로 한 'ZeroRepo' 프레임워크는 세 단계로 저장소를 생성하며, 이를 평가하기 위해 'RepoCraft'라는 벤치마크를 구축했습니다. ZeroRepo는 평균 36K LOC의 저장소를 생성하며, 기존의 최고 성능보다 훨씬 높은 기능적 커버리지와 통과율을 달성했습니다. RPG는 복잡한 의존성을 모델링하고, 저장소에 대한 이해를 높여 계획을 점진적으로 개선합니다.

## 🎯 주요 포인트

- 1. Repository Planning Graph (RPG)는 제안 및 구현 단계의 계획을 통합하여 복잡한 소프트웨어 구조를 명확하게 표현하는 지속적인 표현 방식입니다.

- 2. ZeroRepo는 RPG를 기반으로 제안 단계 계획, 구현 단계 세부화, 그래프 기반 코드 생성 및 테스트 검증의 세 단계로 구성된 저장소 생성 프레임워크입니다.

- 3. RepoCraft 벤치마크에서 ZeroRepo는 평균 36K LOC의 저장소를 생성하며, 이는 가장 강력한 기준인 Claude Code보다 약 3.9배, 다른 기준보다 약 64배 더 많습니다.

- 4. ZeroRepo는 기능적 커버리지 81.5%와 통과율 69.7%를 달성하여 Claude Code보다 각각 27.3 및 35.8 퍼센트 포인트 더 높습니다.

- 5. RPG는 복잡한 의존성을 모델링하고, 선형에 가까운 확장을 통해 점진적으로 더 정교한 계획을 가능하게 하며, LLM의 저장소 이해를 향상시킵니다.

---

*Generated on 2025-09-22 14:27:29*