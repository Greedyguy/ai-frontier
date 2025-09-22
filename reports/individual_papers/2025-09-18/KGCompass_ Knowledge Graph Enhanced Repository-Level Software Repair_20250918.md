
# KGCompass: Knowledge Graph Enhanced Repository-Level Software Repair

**Korean Title:** KGCompass: 지식 그래프 강화 저장소 수준 소프트웨어 수리

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Path-guided Repair

## 🔗 유사한 논문
- [[An Empirical Study on Failures in Automated Issue Solving]] (77.0% similar)
- [[Semantic_Alignment-Enhanced_Code_Translation_via_an_LLM-Based_Multi-Agent_System_20250918|Semantic Alignment-Enhanced Code Translation via an LLM-Based Multi-Agent System]] (76.4% similar)
- [[Using LLMs in Generating Design Rationale for Software Architecture Decisions]] (76.3% similar)
- [[MAgICoRe: Multi-Agent, Iterative, Coarse-to-Fine Refinement for Reasoning]] (76.0% similar)
- [[LLM_Agents_for_Interactive_Workflow_Provenance_Reference_Architecture_and_Evaluation_Methodology_20250918|LLM Agents for Interactive Workflow Provenance: Reference Architecture and Evaluation Methodology]] (75.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.21710v2 Announce Type: replace 
Abstract: Repository-level software repair faces challenges in bridging semantic gaps between issue descriptions and code patches. Existing approaches, which primarily rely on large language models (LLMs), are hindered by semantic ambiguities, limited understanding of structural context, and insufficient reasoning capabilities. To address these limitations, we propose KGCompass with two innovations: (1) a novel repository-aware knowledge graph (KG) that accurately links repository artifacts (issues and pull requests) and codebase entities (files, classes, and functions), allowing us to effectively narrow down the vast search space to only 20 most relevant functions with accurate candidate fault locations and contextual information, and (2) a path-guided repair mechanism that leverages KG-mined entity paths, tracing through which allows us to augment LLMs with relevant contextual information to generate precise patches along with their explanations. Experimental results in the SWE-bench Lite demonstrate that KGCompass achieves state-of-the-art single-LLM repair performance (58.3%) and function-level fault location accuracy (56.0%) across open-source approaches with a single repair model, costing only $0.2 per repair. Among the bugs that KGCompass successfully localizes, 89.7% lack explicit location hints in the issue and are found only through multi-hop graph traversal, where pure LLMs struggle to locate bugs accurately. Relative to pure-LLM baselines, KGCompass lifts the resolved rate by 50.8% on Claude-4 Sonnet, 30.2% on Claude-3.5 Sonnet, 115.7% on DeepSeek-V3, and 156.4% on Qwen2.5 Max. These consistent improvements demonstrate that this graph-guided repair framework delivers model-agnostic, cost-efficient repair and sets a strong new baseline for repository-level repair.

## 🔍 Abstract (한글 번역)

arXiv:2503.21710v2 발표 유형: 대체
요약: 저장소 수준의 소프트웨어 수리는 문제 설명과 코드 패치 사이의 의미적 간극을 극복하는 데 어려움을 겪고 있습니다. 주로 대형 언어 모델 (LLM)에 의존하는 기존 접근 방식은 의미적 모호성, 구조적 맥락의 제한된 이해, 그리고 충분하지 않은 추론 능력으로 인해 제약을 받고 있습니다. 이러한 한계를 극복하기 위해, 우리는 KGCompass를 제안합니다. KGCompass는 두 가지 혁신을 통해 이러한 한계를 극복합니다: (1) 저장소 인식 지식 그래프 (KG)로, 이를 통해 저장소 자산 (이슈 및 풀 리퀘스트)와 코드베이스 엔티티 (파일, 클래스 및 함수)를 정확하게 연결하여 정확한 후보 결함 위치 및 문맥 정보를 가진 가장 관련성 높은 20개의 함수로 검색 공간을 효과적으로 좁힐 수 있고, (2) KG에서 채굴한 엔티티 경로를 활용하는 경로 안내 수리 메커니즘으로, 이를 통해 LLM에 관련 문맥 정보를 부여하여 정확한 패치와 그에 대한 설명을 생성할 수 있습니다. SWE-bench Lite에서의 실험 결과는 KGCompass가 단일-LLM 수리 성능 (58.3%) 및 함수 수준의 결함 위치 정확도 (56.0%)에서 오픈 소스 접근 방식을 통해 최신 기술을 달성하며, 단일 수리 모델로만 0.2달러의 비용으로 수리할 수 있음을 보여줍니다. KGCompass가 성공적으로 지역화하는 버그 중 89.7%는 이슈에서 명시적인 위치 힌트가 없으며, 순수 LLM이 정확하게 버그를 찾는 데 어려워하는 다중 홉 그래프 탐색을 통해서만 발견됩니다. 순수 LLM 기준에 비해, KGCompass는 Claude-4 Sonnet에서 해결률을 50.8%, Claude-3.5 Sonnet에서 30.2%, DeepSeek-V3에서 115.7%, Qwen2.5 Max에서 156.4% 향상시킵니다. 이러한 일관된 개선은 그래프 안내 수리 프레임워크가 모델에 중립적이고 비용 효율적인 수리를 제공하며 저장소 수준의 수리에 강력한 새로운 기준을 설정한다는 것을 보여줍니다.

## 📝 요약

KGCompass는 저장소 수준의 소프트웨어 수리에 대한 새로운 방법론으로, 저장소 아티팩트와 코드베이스 엔티티를 정확하게 연결하는 새로운 지식 그래프를 제안하고, 이를 통해 정확한 후보 결함 위치와 문맥 정보를 제공하여 정확한 패치를 생성하는 경로 안내 수리 메커니즘을 도입했다. 실험 결과는 KGCompass가 최신 단일 LLM 수리 성능과 함수 수준 결함 위치 정확도를 달성하며, 단일 수리 모델을 사용하여 비용 효율적인 수리를 제공함을 보여준다. 이러한 일관된 개선은 그래프 안내 수리 프레임워크가 모델에 중립적이고 비용 효율적인 수리를 제공하며 저장소 수준 수리에 강력한 새로운 기준을 제시한다.

## 🎯 주요 포인트

- 1. KGCompass는 저장소 수준의 소프트웨어 수리에 대한 새로운 그래프 안내 수리 프레임워크를 제안한다.

- 2. KGCompass는 저장소 아티팩트와 코드베이스 엔티티를 정확하게 연결하는 새로운 지식 그래프를 활용한다.

- 3. KGCompass는 상태-of-the-art 단일-LLM 수리 성능을 달성하며 비용 효율적인 수리를 제공한다.

---

*Generated on 2025-09-18 17:23:45*