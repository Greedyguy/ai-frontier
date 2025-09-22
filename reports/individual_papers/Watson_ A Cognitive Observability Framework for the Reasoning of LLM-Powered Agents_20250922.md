# Watson: A Cognitive Observability Framework for the Reasoning of LLM-Powered Agents

**Korean Title:** 왓슨: LLM 기반 에이전트의 추론을 위한 인지 관찰 프레임워크

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Cognitive Observability

## 🔗 유사한 논문
- [[2025-09-19/WebCoT_ Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback_20250919|WebCoT Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback]] (88.9% similar)
- [[2025-09-19/AgentCompass_ Towards Reliable Evaluation of Agentic Workflows in Production_20250919|AgentCompass Towards Reliable Evaluation of Agentic Workflows in Production]] (85.3% similar)
- [[2025-09-22/Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context_20250922|Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context]] (85.1% similar)
- [[2025-09-18/AppAgent v2_ Advanced Agent for Flexible Mobile Interactions_20250918|AppAgent v2 Advanced Agent for Flexible Mobile Interactions]] (84.1% similar)
- [[2025-09-19/Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (84.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2411.03455v3 Announce Type: replace 
Abstract: Large language models (LLMs) are increasingly integrated into autonomous systems, giving rise to a new class of software known as Agentware, where LLM-powered agents perform complex, open-ended tasks in domains such as software engineering, customer service, and data analysis. However, their high autonomy and opaque reasoning processes pose significant challenges for traditional software observability methods. To address this, we introduce the concept of cognitive observability - the ability to recover and inspect the implicit reasoning behind agent decisions. We present Watson, a general-purpose framework for observing the reasoning processes of fast-thinking LLM agents without altering their behavior. Watson retroactively infers reasoning traces using prompt attribution techniques. We evaluate Watson in both manual debugging and automated correction scenarios across the MMLU benchmark and the AutoCodeRover and OpenHands agents on the SWE-bench-lite dataset. In both static and dynamic settings, Watson surfaces actionable reasoning insights and supports targeted interventions, demonstrating its practical utility for improving transparency and reliability in Agentware systems.

## 🔍 Abstract (한글 번역)

arXiv:2411.03455v3 발표 유형: 교체  
초록: 대형 언어 모델(LLM)은 점점 더 자율 시스템에 통합되어, 소프트웨어 엔지니어링, 고객 서비스, 데이터 분석과 같은 분야에서 LLM 기반 에이전트가 복잡하고 개방형 작업을 수행하는 새로운 소프트웨어 클래스인 Agentware를 탄생시켰습니다. 그러나 이들의 높은 자율성과 불투명한 추론 과정은 전통적인 소프트웨어 관측 방법에 상당한 도전을 제기합니다. 이를 해결하기 위해, 에이전트 결정의 암묵적 추론을 복구하고 검사할 수 있는 능력인 인지 관측성의 개념을 도입합니다. 우리는 빠르게 사고하는 LLM 에이전트의 추론 과정을 그들의 행동을 변경하지 않고 관찰할 수 있는 범용 프레임워크인 Watson을 제시합니다. Watson은 프롬프트 귀속 기법을 사용하여 추론 흔적을 소급적으로 추론합니다. 우리는 MMLU 벤치마크와 SWE-bench-lite 데이터셋의 AutoCodeRover 및 OpenHands 에이전트를 대상으로 수동 디버깅 및 자동 수정 시나리오에서 Watson을 평가합니다. 정적 및 동적 설정 모두에서 Watson은 실행 가능한 추론 통찰을 표면화하고 목표 지향적 개입을 지원하며, Agentware 시스템의 투명성과 신뢰성을 향상시키는 실용적 유용성을 입증합니다.

## 📝 요약

대형 언어 모델(LLM)이 자율 시스템에 통합되면서 소프트웨어 공학, 고객 서비스, 데이터 분석 등 다양한 분야에서 복잡한 작업을 수행하는 에이전트웨어가 등장했습니다. 그러나 이들의 높은 자율성과 불투명한 추론 과정은 기존 소프트웨어 관찰 방법에 도전 과제를 제기합니다. 이를 해결하기 위해, 우리는 에이전트의 결정 뒤에 숨겨진 추론을 복구하고 검사할 수 있는 인지 관찰성 개념을 도입했습니다. Watson은 LLM 에이전트의 빠른 추론 과정을 관찰할 수 있는 범용 프레임워크로, 행동을 변경하지 않고도 추론 흔적을 복구합니다. Watson은 MMLU 벤치마크 및 SWE-bench-lite 데이터셋의 AutoCodeRover와 OpenHands 에이전트에서 수동 디버깅과 자동 수정 시나리오를 평가하여, 에이전트웨어 시스템의 투명성과 신뢰성을 향상시키는 실용성을 입증했습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)이 자율 시스템에 통합되면서 Agentware라는 새로운 소프트웨어 클래스가 등장하고 있습니다.

- 2. 전통적인 소프트웨어 관측 방법으로는 LLM의 높은 자율성과 불투명한 추론 과정을 다루기 어렵습니다.

- 3. Watson은 LLM 에이전트의 추론 과정을 관찰할 수 있는 일반적인 프레임워크로, 에이전트의 행동을 변경하지 않고도 추론 흔적을 복원합니다.

- 4. Watson은 MMLU 벤치마크와 SWE-bench-lite 데이터셋의 AutoCodeRover 및 OpenHands 에이전트에서 수동 디버깅 및 자동 수정 시나리오를 평가합니다.

- 5. Watson은 정적 및 동적 환경 모두에서 실행 가능한 추론 통찰력을 제공하여 Agentware 시스템의 투명성과 신뢰성을 향상시킵니다.

---

*Generated on 2025-09-22 14:29:09*