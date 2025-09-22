# Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context

**Korean Title:** 다중 에이전트 전문가 시스템에서 인지 실패의 진단: 동적 평가 프로토콜과 처리 컨텍스트의 후속 변이를 이용하여

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Expert Behaviour Transfer

## 🔗 유사한 논문
- [[2025-09-19/AgentCompass_ Towards Reliable Evaluation of Agentic Workflows in Production_20250919|AgentCompass Towards Reliable Evaluation of Agentic Workflows in Production]] (88.2% similar)
- [[2025-09-19/LEED_ A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning_20250919|LEED A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning]] (87.5% similar)
- [[2025-09-19/Detecting Pipeline Failures through Fine-Grained Analysis of Web Agents_20250919|Detecting Pipeline Failures through Fine-Grained Analysis of Web Agents]] (86.8% similar)
- [[2025-09-19/An LLM-based multi-agent framework for agile effort estimation_20250919|An LLM-based multi-agent framework for agile effort estimation]] (86.6% similar)
- [[2025-09-19/From Capabilities to Performance_ Evaluating Key Functional Properties of LLM Architectures in Penetration Testing_20250919|From Capabilities to Performance Evaluating Key Functional Properties of LLM Architectures in Penetration Testing]] (85.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15366v1 Announce Type: new 
Abstract: The rapid evolution of neural architectures - from multilayer perceptrons to large-scale Transformer-based models - has enabled language models (LLMs) to exhibit emergent agentic behaviours when equipped with memory, planning, and external tool use. However, their inherent stochasticity and multi-step decision processes render classical evaluation methods inadequate for diagnosing agentic performance. This work introduces a diagnostic framework for expert systems that not only evaluates but also facilitates the transfer of expert behaviour into LLM-powered agents. The framework integrates (i) curated golden datasets of expert annotations, (ii) silver datasets generated through controlled behavioural mutation, and (iii) an LLM-based Agent Judge that scores and prescribes targeted improvements. These prescriptions are embedded into a vectorized recommendation map, allowing expert interventions to propagate as reusable improvement trajectories across multiple system instances. We demonstrate the framework on a multi-agent recruiter-assistant system, showing that it uncovers latent cognitive failures - such as biased phrasing, extraction drift, and tool misrouting - while simultaneously steering agents toward expert-level reasoning and style. The results establish a foundation for standardized, reproducible expert behaviour transfer in stochastic, tool-augmented LLM agents, moving beyond static evaluation to active expert system refinement.

## 🔍 Abstract (한글 번역)

arXiv:2509.15366v1 발표 유형: 신규  
초록: 다층 퍼셉트론에서 대규모 Transformer 기반 모델로의 신경 아키텍처의 급속한 발전은 언어 모델(LLM)이 메모리, 계획 및 외부 도구 사용을 갖추었을 때 새로운 에이전트적 행동을 나타낼 수 있게 하였습니다. 그러나 이들의 내재된 확률성과 다단계 의사결정 과정은 고전적인 평가 방법이 에이전트 성능을 진단하는 데 부적절하게 만듭니다. 본 연구는 전문가 시스템을 위한 진단 프레임워크를 도입하여, 에이전트 성능을 평가할 뿐만 아니라 전문가 행동을 LLM 기반 에이전트로 전이하는 것을 촉진합니다. 이 프레임워크는 (i) 전문가 주석의 큐레이션된 골든 데이터셋, (ii) 통제된 행동 변이를 통해 생성된 실버 데이터셋, (iii) LLM 기반 에이전트 판정기를 통합하여 점수와 목표 개선을 처방합니다. 이러한 처방은 벡터화된 추천 맵에 내장되어, 전문가 개입이 여러 시스템 인스턴스에 걸쳐 재사용 가능한 개선 궤적으로 전파될 수 있게 합니다. 우리는 다중 에이전트 채용 보조 시스템에서 이 프레임워크를 시연하여, 편향된 표현, 추출 드리프트, 도구 오경로와 같은 잠재적 인지 실패를 밝혀내는 동시에 에이전트를 전문가 수준의 추론과 스타일로 유도함을 보여줍니다. 결과는 확률적이고 도구가 강화된 LLM 에이전트에서 정적 평가를 넘어 능동적인 전문가 시스템 개선으로 나아가는 표준화되고 재현 가능한 전문가 행동 전이의 기초를 확립합니다.

## 📝 요약

이 논문은 대규모 Transformer 기반 언어 모델(LLM)이 메모리, 계획, 외부 도구 사용을 통해 에이전트 행동을 보이는 상황에서 기존 평가 방법의 한계를 지적하고, 이를 개선하기 위한 진단 프레임워크를 제안합니다. 이 프레임워크는 전문가 주석으로 구성된 골든 데이터셋, 제어된 행동 변이를 통해 생성된 실버 데이터셋, 그리고 LLM 기반 에이전트 평가 시스템을 통합하여 에이전트의 성능을 평가하고 개선 방향을 제시합니다. 이를 통해 다중 에이전트 시스템에서 잠재적인 인지 오류를 발견하고, 에이전트가 전문가 수준의 추론과 스타일을 갖추도록 유도합니다. 연구 결과는 LLM 에이전트의 전문가 행동 전이를 위한 표준화된 방법론을 제시하며, 정적 평가를 넘어선 능동적인 시스템 개선의 기초를 마련합니다.

## 🎯 주요 포인트

- 1. 신경망 구조의 빠른 발전은 LLM이 메모리, 계획, 외부 도구 사용과 결합하여 에이전트 행동을 나타내게 했습니다.

- 2. 기존 평가 방법은 LLM의 확률성과 다단계 의사결정 과정을 진단하기에 불충분합니다.

- 3. 본 연구는 전문가 행동을 LLM 기반 에이전트로 전이시키는 진단 프레임워크를 제안합니다.

- 4. 프레임워크는 전문가 주석의 골든 데이터셋, 행동 변이를 통한 실버 데이터셋, LLM 기반 에이전트 판정기를 통합합니다.

- 5. 다중 에이전트 시스템에서 인지 실패를 발견하고 전문가 수준의 추론과 스타일로 에이전트를 유도하는 데 성공했습니다.

---

*Generated on 2025-09-22 13:43:43*