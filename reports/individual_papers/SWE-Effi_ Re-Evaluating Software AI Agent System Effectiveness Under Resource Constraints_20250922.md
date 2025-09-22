# SWE-Effi: Re-Evaluating Software AI Agent System Effectiveness Under Resource Constraints

**Korean Title:** SWE-Effi: 자원 제약 하에서 소프트웨어 AI 에이전트 시스템의 효과성을 재평가하기

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Holistic Effectiveness Scores

## 🔗 유사한 논문
- [[2025-09-17/An Empirical Study on Failures in Automated Issue Solving_20250917|An Empirical Study on Failures in Automated Issue Solving]] (84.7% similar)
- [[2025-09-18/Designing AI-Agents with Personalities_ A Psychometric Approach_20250918|Designing AI-Agents with Personalities A Psychometric Approach]] (81.3% similar)
- [[2025-09-22/Watson_ A Cognitive Observability Framework for the Reasoning of LLM-Powered Agents_20250922|Watson A Cognitive Observability Framework for the Reasoning of LLM-Powered Agents]] (81.2% similar)
- [[2025-09-19/(P)rior(D)yna(F)low_ A Priori Dynamic Workflow Construction via Multi-Agent Collaboration_20250919|(P)rior(D)yna(F)low A Priori Dynamic Workflow Construction via Multi-Agent Collaboration]] (81.2% similar)
- [[2025-09-19/An LLM-based multi-agent framework for agile effort estimation_20250919|An LLM-based multi-agent framework for agile effort estimation]] (81.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.09853v2 Announce Type: replace-cross 
Abstract: The advancement of large language models (LLMs) and code agents has demonstrated significant potential to assist software engineering (SWE) tasks, such as autonomous issue resolution and feature addition. Existing AI for software engineering leaderboards (e.g., SWE-bench) focus solely on solution accuracy, ignoring the crucial factor of effectiveness in a resource-constrained world. This is a universal problem that also exists beyond software engineering tasks: any AI system should be more than correct - it must also be cost-effective. To address this gap, we introduce SWE-Effi, a set of new metrics to re-evaluate AI systems in terms of holistic effectiveness scores. We define effectiveness as the balance between the accuracy of outcome (e.g., issue resolve rate) and the resources consumed (e.g., token and time). In this paper, we specifically focus on the software engineering scenario by re-ranking popular AI systems for issue resolution on a subset of the SWE-bench benchmark using our new multi-dimensional metrics. We found that AI system's effectiveness depends not just on the scaffold itself, but on how well it integrates with the base model, which is key to achieving strong performance in a resource-efficient manner. We also identified systematic challenges such as the "token snowball" effect and, more significantly, a pattern of "expensive failures". In these cases, agents consume excessive resources while stuck on unsolvable tasks - an issue that not only limits practical deployment but also drives up the cost of failed rollouts during RL training. Lastly, we observed a clear trade-off between effectiveness under the token budget and effectiveness under the time budget, which plays a crucial role in managing project budgets and enabling scalable reinforcement learning, where fast responses are essential.

## 🔍 Abstract (한글 번역)

arXiv:2509.09853v2 발표 유형: 교차 교체  
초록: 대형 언어 모델(LLMs)과 코드 에이전트의 발전은 자율적인 문제 해결 및 기능 추가와 같은 소프트웨어 공학(SWE) 작업을 지원하는 데 상당한 잠재력을 보여주었습니다. 기존의 소프트웨어 공학을 위한 AI 리더보드(예: SWE-bench)는 솔루션의 정확성에만 초점을 맞추고, 자원이 제한된 환경에서의 효과성이라는 중요한 요소를 간과하고 있습니다. 이는 소프트웨어 공학 작업을 넘어서는 보편적인 문제로, 모든 AI 시스템은 단순히 정확하기만 해서는 안 되며, 비용 효율적이어야 합니다. 이러한 격차를 해결하기 위해, 우리는 AI 시스템을 총체적인 효과성 점수 측면에서 재평가하기 위한 새로운 지표 세트인 SWE-Effi를 소개합니다. 우리는 효과성을 결과의 정확성(예: 문제 해결률)과 소비된 자원(예: 토큰 및 시간) 간의 균형으로 정의합니다. 이 논문에서는 특히 소프트웨어 공학 시나리오에 초점을 맞추어, SWE-bench 벤치마크의 하위 집합에서 문제 해결을 위한 인기 있는 AI 시스템을 우리의 새로운 다차원 지표를 사용하여 재순위화합니다. 우리는 AI 시스템의 효과성이 단순히 구조 자체에 의존하는 것이 아니라, 기본 모델과 얼마나 잘 통합되는지가 자원 효율적인 방식으로 강력한 성능을 달성하는 데 중요하다는 것을 발견했습니다. 또한 "토큰 스노우볼" 효과와 더 중요하게는 "비용이 많이 드는 실패" 패턴과 같은 체계적인 문제를 확인했습니다. 이러한 경우, 에이전트는 해결할 수 없는 작업에 갇혀 과도한 자원을 소비하게 되며, 이는 실질적인 배포를 제한할 뿐만 아니라 RL 훈련 중 실패한 롤아웃의 비용을 증가시킵니다. 마지막으로, 토큰 예산 하에서의 효과성과 시간 예산 하에서의 효과성 간의 명확한 상충 관계를 관찰했으며, 이는 프로젝트 예산 관리와 빠른 응답이 필수적인 확장 가능한 강화 학습을 가능하게 하는 데 중요한 역할을 합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)과 코드 에이전트가 소프트웨어 엔지니어링(SWE) 작업을 지원하는 데 있어 잠재력을 보였지만, 기존의 AI 리더보드는 솔루션의 정확성만을 평가하고 자원 효율성을 간과하고 있음을 지적합니다. 이를 해결하기 위해, 저자들은 SWE-Effi라는 새로운 지표를 도입하여 AI 시스템의 전반적인 효과성을 평가합니다. 효과성은 결과의 정확성과 소비된 자원의 균형으로 정의됩니다. 연구는 SWE-bench 벤치마크의 하위 집합에서 인기 있는 AI 시스템을 새로운 다차원 지표로 재평가하였고, AI 시스템의 효과성은 기본 모델과의 통합 수준에 크게 좌우된다는 것을 발견했습니다. 또한 "토큰 스노우볼" 효과와 "비용이 많이 드는 실패" 패턴과 같은 체계적인 문제를 확인했습니다. 마지막으로, 토큰 예산과 시간 예산 간의 효과성 간의 명확한 상충 관계가 프로젝트 예산 관리와 확장 가능한 강화 학습에 중요한 역할을 한다고 결론지었습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델과 코드 에이전트는 소프트웨어 엔지니어링 작업에서 자율적인 문제 해결과 기능 추가를 지원할 잠재력을 보여준다.

- 2. 기존의 소프트웨어 엔지니어링 AI 리더보드는 솔루션의 정확성에만 집중하며, 자원 제약 환경에서의 효과성을 간과하고 있다.

- 3. SWE-Effi는 AI 시스템의 전반적인 효과성을 평가하기 위한 새로운 다차원 지표를 도입하여, 결과의 정확성과 소비된 자원의 균형을 정의한다.

- 4. AI 시스템의 효과성은 기반 모델과의 통합 수준에 따라 달라지며, 이는 자원 효율적인 강력한 성능을 달성하는 데 중요하다.

- 5. "토큰 스노우볼" 효과와 "비용이 많이 드는 실패" 패턴과 같은 체계적인 도전 과제가 존재하며, 이는 실용적인 배포를 제한하고 RL 훈련 중 실패한 롤아웃의 비용을 증가시킨다.

---

*Generated on 2025-09-22 15:03:42*