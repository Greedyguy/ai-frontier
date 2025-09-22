# MatchFixAgent: Language-Agnostic Autonomous Repository-Level Code Translation Validation and Repair

**Korean Title:** MatchFixAgent: 언어 비종속적 자율 저장소 수준 코드 번역 검증 및 수리

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Multi-agent Architecture|Multi-agent Architecture]] [[keywords/specific/Equivalence Validation|Equivalence Validation]] [[keywords/specific/Code Translation|Code Translation]] [[keywords/broad/Large Language Model|Large Language Model]] [[keywords/unique/MatchFixAgent|MatchFixAgent]] [[categories/cs.LG|cs.LG]] [[2025-09-18/Semantic Alignment-Enhanced Code Translation via an LLM-Based Multi-Agent System_20250918|Semantic Alignment-Enhanced Code Translation via an LLM-Based Multi-Agent System]] (86.4% similar) [[2025-09-19/RulER_ Automated Rule-Based Semantic Error Localization and Repair for Code Translation_20250919|RulER: Automated Rule-Based Semantic Error Localization and Repair for Code Translation]] (84.0% similar) [[2025-09-19/On the Use of Agentic Coding_ An Empirical Study of Pull Requests on GitHub_20250919|On the Use of Agentic Coding: An Empirical Study of Pull Requests on GitHub]] (81.4% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi-agent Architecture
**🔗 Specific Connectable**: Equivalence Validation
**🔬 Broad Technical**: Large Language Model
**⭐ Unique Technical**: MatchFixAgent
## 🔗 유사한 논문
- [[2025-09-18/Semantic Alignment-Enhanced Code Translation via an LLM-Based Multi-Agent System_20250918|Semantic Alignment-Enhanced Code Translation via an LLM-Based Multi-Agent System]] (86.4% similar)
- [[2025-09-19/RulER_ Automated Rule-Based Semantic Error Localization and Repair for Code Translation_20250919|RulER Automated Rule-Based Semantic Error Localization and Repair for Code Translation]] (84.0% similar)
- [[2025-09-19/On the Use of Agentic Coding_ An Empirical Study of Pull Requests on GitHub_20250919|On the Use of Agentic Coding An Empirical Study of Pull Requests on GitHub]] (81.4% similar)
- [[2025-09-19/Translate, then Detect_ Leveraging Machine Translation for Cross-Lingual Toxicity Classification_20250919|Translate, then Detect Leveraging Machine Translation for Cross-Lingual Toxicity Classification]] (80.4% similar)
- [[2025-09-19/Ticket-Bench_ A Kickoff for Multilingual and Regionalized Agent Evaluation_20250919|Ticket-Bench A Kickoff for Multilingual and Regionalized Agent Evaluation]] (80.3% similar)


**ArXiv ID**: [2509.16187](https://arxiv.org/abs/2509.16187)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.16187.pdf)


**ArXiv ID**: [2509.16187](https://arxiv.org/abs/2509.16187)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.16187.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi-agent Architecture
**🔗 Specific Connectable**: Equivalence Validation, Translation Repair
**⭐ Unique Technical**: MatchFixAgent
**🔬 Broad Technical**: Large Language Model

## 🏷️ 추출된 키워드



`Large Language Model` • 

`Equivalence Validation` • 

`MatchFixAgent` • 

`Multi-agent Architecture`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16187v1 Announce Type: cross 
Abstract: Code translation transforms source code from one programming language (PL) to another. Validating the functional equivalence of translation and repairing, if necessary, are critical steps in code translation. Existing automated validation and repair approaches struggle to generalize to many PLs due to high engineering overhead, and they rely on existing and often inadequate test suites, which results in false claims of equivalence and ineffective translation repair. We develop MatchFixAgent, a large language model (LLM)-based, PL-agnostic framework for equivalence validation and repair of translations. MatchFixAgent features a multi-agent architecture that divides equivalence validation into several sub-tasks to ensure thorough and consistent semantic analysis of the translation. Then it feeds this analysis to test agent to write and execute tests. Upon observing a test failure, the repair agent attempts to fix the translation bug. The final (in)equivalence decision is made by the verdict agent, considering semantic analyses and test execution results.
  We compare MatchFixAgent's validation and repair results with four repository-level code translation techniques. We use 2,219 translation pairs from their artifacts, which cover 6 PL pairs, and are collected from 24 GitHub projects totaling over 900K lines of code. Our results demonstrate that MatchFixAgent produces (in)equivalence verdicts for 99.2% of translation pairs, with the same equivalence validation result as prior work on 72.8% of them. When MatchFixAgent's result disagrees with prior work, we find that 60.7% of the time MatchFixAgent's result is actually correct. In addition, we show that MatchFixAgent can repair 50.6% of inequivalent translation, compared to prior work's 18.5%. This demonstrates that MatchFixAgent is far more adaptable to many PL pairs than prior work, while producing highly accurate validation results.

## 🔍 Abstract (한글 번역)

arXiv:2509.16187v1 발표 유형: 교차  
초록: 코드 번역은 소스 코드를 하나의 프로그래밍 언어(PL)에서 다른 언어로 변환하는 작업입니다. 번역의 기능적 동등성을 검증하고 필요한 경우 수정하는 것은 코드 번역에서 중요한 단계입니다. 기존의 자동화된 검증 및 수정 접근법은 높은 엔지니어링 부담으로 인해 많은 프로그래밍 언어에 일반화하는 데 어려움을 겪으며, 기존의 불충분한 테스트 스위트에 의존하여 동등성에 대한 잘못된 주장과 비효율적인 번역 수정을 초래합니다. 우리는 번역의 동등성 검증 및 수정을 위한 대형 언어 모델(LLM) 기반의 프로그래밍 언어에 구애받지 않는 프레임워크인 MatchFixAgent를 개발했습니다. MatchFixAgent는 번역의 철저하고 일관된 의미 분석을 보장하기 위해 동등성 검증을 여러 하위 작업으로 나누는 다중 에이전트 아키텍처를 특징으로 합니다. 그런 다음 이 분석을 테스트 에이전트에 전달하여 테스트를 작성하고 실행합니다. 테스트 실패가 관찰되면 수정 에이전트가 번역 버그를 수정하려고 시도합니다. 최종 동등성 여부 결정은 의미 분석과 테스트 실행 결과를 고려하여 판결 에이전트에 의해 이루어집니다.  
우리는 MatchFixAgent의 검증 및 수정 결과를 네 가지 저장소 수준 코드 번역 기술과 비교했습니다. 6개의 프로그래밍 언어 쌍을 다루고, 24개의 GitHub 프로젝트에서 총 90만 줄 이상의 코드에서 수집된 2,219개의 번역 쌍을 사용했습니다. 우리의 결과는 MatchFixAgent가 번역 쌍의 99.2%에 대해 동등성 여부를 판결하며, 그 중 72.8%는 이전 연구와 동일한 동등성 검증 결과를 나타냅니다. MatchFixAgent의 결과가 이전 연구와 일치하지 않을 때, 60.7%의 경우 MatchFixAgent의 결과가 실제로 올바르다는 것을 발견했습니다. 또한, MatchFixAgent는 이전 연구의 18.5%에 비해 50.6%의 비동등 번역을 수정할 수 있음을 보여줍니다. 이는 MatchFixAgent가 많은 프로그래밍 언어 쌍에 대해 이전 연구보다 훨씬 더 적응력이 뛰어나며, 높은 정확도의 검증 결과를 생성함을 입증합니다.

## 📝 요약

이 논문은 코드 번역의 기능적 동등성을 검증하고 필요 시 수정하는 새로운 방법론인 MatchFixAgent를 제안합니다. MatchFixAgent는 프로그래밍 언어에 구애받지 않는 대규모 언어 모델 기반의 프레임워크로, 다중 에이전트 구조를 통해 번역의 의미 분석을 세분화하여 철저한 검증을 수행합니다. 테스트 에이전트가 테스트를 실행하고, 실패 시 수정 에이전트가 번역 오류를 수정합니다. 최종 판단은 판결 에이전트가 내립니다. 6개의 프로그래밍 언어 쌍을 포함한 2,219개의 번역 쌍을 대상으로 한 실험에서 MatchFixAgent는 99.2%의 번역 쌍에 대해 동등성 여부를 판단했으며, 기존 기법보다 60.7% 더 정확한 결과를 보였습니다. 또한, MatchFixAgent는 기존 기법보다 50.6% 더 많은 비동등 번역을 성공적으로 수정했습니다. 이는 MatchFixAgent가 다양한 프로그래밍 언어 쌍에 더 적응력이 뛰어나고 높은 정확도의 검증 결과를 제공함을 보여줍니다.

## 🎯 주요 포인트


- 1. MatchFixAgent는 프로그래밍 언어에 구애받지 않는 대규모 언어 모델 기반의 번역 등가성 검증 및 수정을 위한 프레임워크입니다.

- 2. MatchFixAgent는 다중 에이전트 아키텍처를 통해 번역의 철저하고 일관된 의미 분석을 수행하고, 테스트 에이전트를 통해 테스트를 작성 및 실행합니다.

- 3. MatchFixAgent는 2,219개의 번역 쌍을 대상으로 99.2%의 번역 쌍에 대해 (비)등가성 판결을 내렸으며, 이전 연구와 72.8%의 일치율을 보였습니다.

- 4. MatchFixAgent는 이전 연구보다 50.6%의 비등가 번역을 수정할 수 있으며, 이는 이전 연구의 18.5%와 비교하여 훨씬 높은 수정 능력을 보여줍니다.

- 5. MatchFixAgent는 다양한 프로그래밍 언어 쌍에 대해 높은 적응성을 가지며, 매우 정확한 검증 결과를 제공합니다.


---

*Generated on 2025-09-22 15:48:34*