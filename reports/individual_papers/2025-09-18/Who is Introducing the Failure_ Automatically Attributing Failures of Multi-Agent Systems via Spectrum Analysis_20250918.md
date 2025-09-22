
# Who is Introducing the Failure? Automatically Attributing Failures of Multi-Agent Systems via Spectrum Analysis

**Korean Title:** 누가 실패를 야기하는가? 스펙트럼 분석을 통한 다중 에이전트 시스템 실패의 자동 귀속

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Spectrum-based Failure Attribution

## 🔗 유사한 논문
- [[An Empirical Study on Failures in Automated Issue Solving]] (81.5% similar)
- [[PhysicalAgent Towards General Cognitive Robotics with Foundation World Models]] (78.3% similar)
- [[Evaluating_Classical_Software_Process_Models_as_Coordination_Mechanisms_for_LLM-Based_Software_Generation_20250918|Evaluating Classical Software Process Models as Coordination Mechanisms for LLM-Based Software Generation]] (78.0% similar)
- [[MAFA A multi-agent framework for annotation]] (78.0% similar)
- [[MIMIC-D Multi-modal Imitation for MultI-agent Coordination with Decentralized Diffusion Policies]] (77.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13782v1 Announce Type: cross 
Abstract: Large Language Model Powered Multi-Agent Systems (MASs) are increasingly employed to automate complex real-world problems, such as programming and scientific discovery. Despite their promising, MASs are not without their flaws. However, failure attribution in MASs - pinpointing the specific agent actions responsible for failures - remains underexplored and labor-intensive, posing significant challenges for debugging and system improvement. To bridge this gap, we propose FAMAS, the first spectrum-based failure attribution approach for MASs, which operates through systematic trajectory replay and abstraction, followed by spectrum analysis.The core idea of FAMAS is to estimate, from variations across repeated MAS executions, the likelihood that each agent action is responsible for the failure. In particular, we propose a novel suspiciousness formula tailored to MASs, which integrates two key factor groups, namely the agent behavior group and the action behavior group, to account for the agent activation patterns and the action activation patterns within the execution trajectories of MASs. Through expensive evaluations against 12 baselines on the Who and When benchmark, FAMAS demonstrates superior performance by outperforming all the methods in comparison.

## 🔍 Abstract (한글 번역)

arXiv:2509.13782v1 공지 유형: cross
초록: 대규모 언어 모델 기반 다중 에이전트 시스템(MAS)은 프로그래밍 및 과학적 발견과 같은 복잡한 실세계 문제를 자동화하는 데 점점 더 많이 활용되고 있다. 이들의 유망한 가능성에도 불구하고, MAS에는 결함이 없지 않다. 그러나 MAS에서의 실패 귀인(failure attribution) - 즉, 실패의 원인이 되는 특정 에이전트 행동을 정확히 찾아내는 것 - 은 여전히 충분히 탐구되지 않았으며 노동집약적이어서, 디버깅과 시스템 개선에 상당한 어려움을 제기하고 있다. 이러한 격차를 해소하기 위해, 우리는 MAS를 위한 최초의 스펙트럼 기반 실패 귀인 접근법인 FAMAS를 제안한다. 이는 체계적인 궤적 재현과 추상화를 통해 작동하며, 이후 스펙트럼 분석이 수행된다. FAMAS의 핵심 아이디어는 반복된 MAS 실행에서의 변이로부터 각 에이전트 행동이 실패에 책임이 있을 가능성을 추정하는 것이다. 특히, 우리는 MAS에 특화된 새로운 의심도 공식을 제안하는데, 이는 두 가지 핵심 요소 그룹, 즉 에이전트 행동 그룹과 행동 행위 그룹을 통합하여 MAS의 실행 궤적 내에서 에이전트 활성화 패턴과 행동 활성화 패턴을 고려한다. Who and When 벤치마크에서 12개의 기준선에 대한 광범위한 평가를 통해, FAMAS는 비교 대상이 된 모든 방법들을 능가함으로써 우수한 성능을 입증한다.

## 📝 요약

이 논문은 대형 언어 모델 기반 다중 에이전트 시스템(MAS)의 실패 원인을 효과적으로 파악하기 위한 FAMAS라는 새로운 접근법을 제안합니다. FAMAS는 시스템의 실행 경로를 체계적으로 재생하고 추상화한 후 스펙트럼 분석을 통해 각 에이전트의 행동이 실패에 기여할 가능성을 추정합니다. 특히, 에이전트의 활성화 패턴과 행동 활성화 패턴을 고려한 새로운 의심 공식이 도입되었습니다. 12개의 기준과 비교한 평가에서 FAMAS는 모든 방법을 능가하는 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델 기반 다중 에이전트 시스템(MAS)은 프로그래밍 및 과학적 발견과 같은 복잡한 현실 문제를 자동화하는 데 사용되고 있다.

- 2. MAS의 실패 원인을 특정 에이전트의 행동으로 귀속시키는 것은 여전히 탐구가 부족하고 노동 집약적이다.

- 3. FAMAS는 MAS의 실패 귀속을 위해 제안된 최초의 스펙트럼 기반 접근법으로, 체계적인 경로 재생 및 추상화, 스펙트럼 분석을 통해 작동한다.

- 4. FAMAS는 에이전트 행동 그룹과 행동 활성화 패턴을 통합한 새로운 의심 공식으로 MAS의 실패 원인을 추정한다.

- 5. FAMAS는 12개의 기준을 대상으로 한 평가에서 모든 비교 방법을 능가하는 우수한 성능을 보였다.

---

*Generated on 2025-09-19 10:44:16*