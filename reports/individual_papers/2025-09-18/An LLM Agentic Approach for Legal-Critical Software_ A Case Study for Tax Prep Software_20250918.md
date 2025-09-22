
# An LLM Agentic Approach for Legal-Critical Software: A Case Study for Tax Prep Software

**Korean Title:** LLM 에이전트 접근법을 활용한 법적 중요 소프트웨어: 세무 준비 소프트웨어 사례 연구

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Agentic LLM Methodologies

## 🔗 유사한 논문
- [[Semantic_Alignment-Enhanced_Code_Translation_via_an_LLM-Based_Multi-Agent_System_20250918|Semantic Alignment-Enhanced Code Translation via an LLM-Based Multi-Agent System]] (84.4% similar)
- [[LLM Agents for Interactive Workflow Provenance Reference Architecture and Evaluation Methodology]] (83.5% similar)
- [[Evaluating_Classical_Software_Process_Models_as_Coordination_Mechanisms_for_LLM-Based_Software_Generation_20250918|Evaluating Classical Software Process Models as Coordination Mechanisms for LLM-Based Software Generation]] (82.7% similar)
- [[Using LLMs in Generating Design Rationale for Software Architecture Decisions]] (82.3% similar)
- [[AppAgent v2 Advanced Agent for Flexible Mobile Interactions]] (81.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13471v1 Announce Type: cross 
Abstract: Large language models (LLMs) show promise for translating natural-language statutes into executable logic, but reliability in legally critical settings remains challenging due to ambiguity and hallucinations. We present an agentic approach for developing legal-critical software, using U.S. federal tax preparation as a case study. The key challenge is test-case generation under the oracle problem, where correct outputs require interpreting law. Building on metamorphic testing, we introduce higher-order metamorphic relations that compare system outputs across structured shifts among similar individuals. Because authoring such relations is tedious and error-prone, we use an LLM-driven, role-based framework to automate test generation and code synthesis. We implement a multi-agent system that translates tax code into executable software and incorporates a metamorphic-testing agent that searches for counterexamples. In experiments, our framework using a smaller model (GPT-4o-mini) achieves a worst-case pass rate of 45%, outperforming frontier models (GPT-4o and Claude 3.5, 9-15%) on complex tax-code tasks. These results support agentic LLM methodologies as a path to robust, trustworthy legal-critical software from natural-language specifications.

## 🔍 Abstract (한글 번역)

arXiv:2509.13471v1 Announce Type: cross 
초록: 대규모 언어 모델(LLM)은 자연어 법령을 실행 가능한 논리로 번역하는 데 유망함을 보이지만, 모호성과 환각으로 인해 법적으로 중요한 환경에서의 신뢰성은 여전히 도전적인 과제로 남아있다. 우리는 미국 연방 세무 준비를 사례 연구로 활용하여 법적 중요도가 높은 소프트웨어 개발을 위한 에이전트 기반 접근법을 제시한다. 핵심 과제는 오라클 문제 하에서의 테스트 케이스 생성으로, 여기서 올바른 출력은 법률 해석을 필요로 한다. 메타모픽 테스팅을 기반으로, 우리는 유사한 개인들 간의 구조화된 변화에 걸쳐 시스템 출력을 비교하는 고차 메타모픽 관계를 도입한다. 이러한 관계를 작성하는 것은 지루하고 오류가 발생하기 쉽기 때문에, 우리는 테스트 생성과 코드 합성을 자동화하기 위해 LLM 기반의 역할 중심 프레임워크를 사용한다. 우리는 세법을 실행 가능한 소프트웨어로 번역하는 다중 에이전트 시스템을 구현하고, 반례를 탐색하는 메타모픽 테스팅 에이전트를 통합한다. 실험에서, 더 작은 모델(GPT-4o-mini)을 사용한 우리의 프레임워크는 복잡한 세법 과제에서 최악의 경우 통과율 45%를 달성하여, 최신 모델들(GPT-4o와 Claude 3.5, 9-15%)을 능가하는 성능을 보였다. 이러한 결과는 자연어 명세로부터 견고하고 신뢰할 수 있는 법적 중요도가 높은 소프트웨어를 구현하는 경로로서 에이전트 기반 LLM 방법론을 뒷받침한다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)을 활용하여 자연어로 작성된 법률을 실행 가능한 논리로 변환하는 방법을 연구합니다. 특히 미국 연방 세금 준비를 사례로 들어 법률 해석의 모호성과 환각 문제를 해결하기 위한 에이전트 기반 접근법을 제안합니다. 메타모픽 테스트를 기반으로, 유사한 개인 간의 구조적 변화를 비교하는 고차 메타모픽 관계를 도입하여 시스템 출력을 평가합니다. 테스트 생성과 코드 작성을 자동화하기 위해 LLM 기반의 역할 중심 프레임워크를 사용합니다. 실험 결과, 작은 모델(GPT-4o-mini)을 사용한 프레임워크가 복잡한 세금 코드 작업에서 최악의 경우 45%의 통과율을 기록하며, 기존 모델(GPT-4o 및 Claude 3.5)의 9-15%를 능가했습니다. 이는 자연어 명세로부터 신뢰할 수 있는 법률 소프트웨어 개발에 있어 에이전트 LLM 방법론의 가능성을 보여줍니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 자연어 법령을 실행 가능한 논리로 번역하는 데 유망하지만, 법적으로 중요한 환경에서의 신뢰성 문제는 여전히 도전 과제입니다.

- 2. 본 연구는 미국 연방 세금 준비를 사례 연구로 하여 법적으로 중요한 소프트웨어 개발을 위한 에이전트 접근 방식을 제시합니다.

- 3. 메타모픽 테스트를 기반으로 유사한 개인 간의 구조적 변화를 비교하는 고차 메타모픽 관계를 도입하여 테스트 케이스 생성 문제를 해결합니다.

- 4. LLM 기반의 역할 기반 프레임워크를 사용하여 테스트 생성과 코드 합성을 자동화하며, 다중 에이전트 시스템을 구현하여 세법을 실행 가능한 소프트웨어로 번역합니다.

- 5. 실험 결과, 작은 모델(GPT-4o-mini)을 사용한 프레임워크가 복잡한 세법 작업에서 최악의 경우 45%의 통과율을 기록하여 기존 모델(GPT-4o 및 Claude 3.5, 9-15%)보다 우수한 성능을 보였습니다.

---

*Generated on 2025-09-19 10:36:32*