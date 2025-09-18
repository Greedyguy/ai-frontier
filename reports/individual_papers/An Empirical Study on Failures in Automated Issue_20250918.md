
# An Empirical Study on Failures in Automated Issue Solving

**Korean Title:** 자동 문제 해결에서의 실패에 관한 경험적 연구

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Multi-agent RAG|Multi-agent RAG]] [[keywords/broad/Automated issue solving|Automated issue solving]] [[keywords/broad/SWE-Bench|SWE-Bench]] [[keywords/specific/LLM-based agentic tools|LLM-based agentic tools]] [[keywords/unique/Expert-Executor framework|Expert-Executor framework]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi-agent RAG
**🔬 Broad Technical**: LLM, SWE-Bench
**🔗 Specific Connectable**: LLM-based agentic tools
**⭐ Unique Technical**: Expert-Executor framework

**ArXiv ID**: [2509.13941](https://arxiv.org/abs/2509.13941)
**Published**: 2025-09-18
**Category**: cs.AI
**PDF**: [Download](https://arxiv.org/pdf/2509.13941.pdf)


## 🏷️ 추출된 키워드



`LLM` • 

`SWE-Bench` • 

`agentic architectures` • 

`Expert-Executor framework` • 

`collaborative design`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13941v1 Announce Type: cross 
Abstract: Automated issue solving seeks to autonomously identify and repair defective code snippets across an entire codebase. SWE-Bench has emerged as the most widely adopted benchmark for evaluating progress in this area. While LLM-based agentic tools show great promise, they still fail on a substantial portion of tasks. Moreover, current evaluations primarily report aggregate issue-solving rates, which obscure the underlying causes of success and failure, making it challenging to diagnose model weaknesses or guide targeted improvements. To bridge this gap, we first analyze the performance and efficiency of three SOTA tools, spanning both pipeline-based and agentic architectures, in automated issue solving tasks of SWE-Bench-Verified under varying task characteristics. Furthermore, to move from high-level performance metrics to underlying cause analysis, we conducted a systematic manual analysis of 150 failed instances. From this analysis, we developed a comprehensive taxonomy of failure modes comprising 3 primary phases, 9 main categories, and 25 fine-grained subcategories. Then we systematically analyze the distribution of the identified failure modes, the results reveal distinct failure fingerprints between the two architectural paradigms, with the majority of agentic failures stemming from flawed reasoning and cognitive deadlocks. Motivated by these insights, we propose a collaborative Expert-Executor framework. It introduces a supervisory Expert agent tasked with providing strategic oversight and course-correction for a primary Executor agent. This architecture is designed to correct flawed reasoning and break the cognitive deadlocks that frequently lead to failure. Experiments show that our framework solves 22.2% of previously intractable issues for a leading single agent. These findings pave the way for building more robust agents through diagnostic evaluation and collaborative design.

## 🔍 Abstract (한글 번역)

arXiv:2509.13941v1 발표 유형: 교차
요약: 자동 문제 해결은 전체 코드베이스에서 결함이 있는 코드 조각을 자동으로 식별하고 수정하는 것을 목표로 합니다. SWE-Bench는 이 분야의 진전을 평가하기 위한 가장 널리 채택된 벤치마크로 등장했습니다. LLM 기반의 에이전트 도구들은 큰 약속을 보여주지만, 여전히 상당 부분의 작업에서 실패합니다. 더구나, 현재의 평가는 주로 총 문제 해결률을 보고하며, 성공과 실패의 근본적인 원인을 가려내기 어렵게 만들어 모델의 약점을 진단하거나 특정 개선을 안내하는 것이 어렵습니다. 이 간극을 메우기 위해, 우리는 먼저 SOTA 도구 3개의 성능과 효율성을 분석했습니다. 파이프라인 기반과 에이전트 아키텍처를 모두 포함하며, 다양한 작업 특성 하에서 SWE-Bench-Verified의 자동 문제 해결 작업을 다룹니다. 더불어, 고수준 성능 지표에서 근본적인 원인 분석으로 이동하기 위해 150개의 실패한 인스턴스에 대한 체계적인 수동 분석을 실시했습니다. 이 분석을 통해, 3개의 주요 단계, 9개의 주요 범주 및 25개의 세부 범주로 구성된 실패 모드의 포괄적인 분류법을 개발했습니다. 그런 다음, 식별된 실패 모드의 분포를 체계적으로 분석하면, 두 아키텍처 패러다임 간에 명확한 실패 지문이 나타납니다. 대부분의 에이전트 실패는 잘못된 추론과 인지적 막힘에서 비롯됩니다. 이러한 통찰력을 바탕으로, 우리는 협력적 전문가-수행자 프레임워크를 제안합니다. 이는 전략적 감독 및 주요 수행자 에이전트에 대한 코스 수정을 제공하는 전문가 에이전트를 소개합니다. 이 아키텍처는 실패로 이어지는 빈번한 잘못된 추론과 인지적 막힘을 교정하기 위해 설계되었습니다. 실험 결과, 우리의 프레임워크는 선도적인 단일 에이전트에 이전에 해결하기 어려웠던 문제의 22.2%를 해결합니다. 이 결과는 진단 평가와 협력적 설계를 통해 더 견고한 에이전트를 구축하는 길을 열어줍니다.

## 📝 요약

최근 자동 문제 해결 기술은 코드 기반 전체에서 결함이 있는 코드 조각을 자동으로 식별하고 수정하는 것을 목표로 합니다. SWE-Bench는 이 분야의 진전을 평가하기 위한 가장 널리 사용되는 벤치마크로 부상했습니다. LLM 기반 에이전트 도구는 큰 약속을 보이지만 여전히 상당 부분의 작업에서 실패합니다. 현재의 평가는 주로 집합적 문제 해결률을 보고하며 성공과 실패의 근본적인 원인을 명확히 하지 않아 모델 약점을 진단하거나 효과적인 개선을 이끌어내는 데 어려움을 겪습니다. 이 간극을 메우기 위해, 우리는 먼저 SWE-Bench-Verified의 자동 문제 해결 작업에서 세 가지 SOTA 도구의 성능과 효율성을 분석했습니다. 또한 고수준 성능 지표에서 원인 분석으로 이동하기 위해 150개의 실패 사례에 대한 체계적인 수동 분석을 실시했습니다. 이 분석을 통해 실패 모드의 포괄적인 분류법을 개발했고, 이를 통해 보다 강력한 에이전트를 구축하기 위한 길을 열었습니다.

## 🎯 주요 포인트


- 자동 문제 해결은 전체 코드베이스에서 결함이 있는 코드 조각을 자동으로 식별하고 수정하는 것을 목표로 한다.

- SWE-Bench는 이 분야의 진전을 평가하기 위한 가장 널리 채택된 벤치마크로 나타났다.

- 실패한 인스턴스 150개에 대한 체계적인 수동 분석을 통해 실패 모드의 종합적인 분류 체계를 개발했다.

- 전문가-실행자 프레임워크를 제안하여 실패로 이어지는 주요 원인을 교정하고 인지적 막힘이 발생하는 것을 방지한다.


---

*Generated on 2025-09-18 16:24:03*