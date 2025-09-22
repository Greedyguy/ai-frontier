
# $Agent^2$: An Agent-Generates-Agent Framework for Reinforcement Learning Automation

**Korean Title:** $Agent^2$: 강화학습 자동화를 위한 에이전트-생성-에이전트 프레임워크

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Automated AI Systems

## 🔗 유사한 논문
- [[AppAgent v2 Advanced Agent for Flexible Mobile Interactions]] (85.7% similar)
- [[PhysicalAgent Towards General Cognitive Robotics with Foundation World Models]] (84.4% similar)
- [[AgentCTG Harnessing Multi-Agent Collaboration for Fine-Grained Precise Control in Text Generation]] (83.3% similar)
- [[DuetUI A Bidirectional Context Loop for Human-Agent Co-Generation of Task-Oriented Interfaces]] (83.3% similar)
- [[Co-Investigator AI The Rise of Agentic AI for Smarter, Trustworthy AML Compliance Narratives]] (83.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13368v1 Announce Type: new 
Abstract: Reinforcement learning agent development traditionally requires extensive expertise and lengthy iterations, often resulting in high failure rates and limited accessibility. This paper introduces $Agent^2$, a novel agent-generates-agent framework that achieves fully automated RL agent design through intelligent LLM-driven generation. The system autonomously transforms natural language task descriptions and environment code into comprehensive, high-performance reinforcement learning solutions without human intervention. $Agent^2$ features a revolutionary dual-agent architecture. The Generator Agent serves as an autonomous AI designer that analyzes tasks and generates executable RL agents, while the Target Agent is the resulting automatically generated RL agent. The framework decomposes RL development into two distinct stages: MDP modeling and algorithmic optimization, enabling more targeted and effective agent generation. Built on the Model Context Protocol, $Agent^2$ provides a unified framework that standardizes intelligent agent creation across diverse environments and algorithms, while incorporating adaptive training management and intelligent feedback analysis for continuous improvement. Extensive experiments on a wide range of benchmarks, including MuJoCo, MetaDrive, MPE, and SMAC, demonstrate that $Agent^2$ consistently outperforms manually designed solutions across all tasks, achieving up to 55% performance improvement and substantial gains on average. By enabling truly end-to-end, closed-loop automation, this work establishes a new paradigm in which intelligent agents design and optimize other agents, marking a fundamental breakthrough for automated AI systems.

## 🔍 Abstract (한글 번역)

arXiv:2509.13368v1 발표 유형: 신규
초록: 강화학습 에이전트 개발은 전통적으로 광범위한 전문 지식과 긴 반복 과정을 요구하며, 이는 종종 높은 실패율과 제한적인 접근성을 초래한다. 본 논문은 지능형 LLM 기반 생성을 통해 완전 자동화된 강화학습 에이전트 설계를 달성하는 새로운 에이전트-생성-에이전트 프레임워크인 $Agent^2$를 소개한다. 이 시스템은 인간의 개입 없이 자연어 작업 설명과 환경 코드를 포괄적이고 고성능의 강화학습 솔루션으로 자율적으로 변환한다. $Agent^2$는 혁신적인 이중 에이전트 아키텍처를 특징으로 한다. 생성기 에이전트(Generator Agent)는 작업을 분석하고 실행 가능한 강화학습 에이전트를 생성하는 자율적 AI 설계자 역할을 하며, 타겟 에이전트(Target Agent)는 그 결과로 자동 생성된 강화학습 에이전트이다. 이 프레임워크는 강화학습 개발을 MDP 모델링과 알고리즘 최적화라는 두 개의 별개 단계로 분해하여, 보다 표적화되고 효과적인 에이전트 생성을 가능하게 한다. 모델 컨텍스트 프로토콜(Model Context Protocol)을 기반으로 구축된 $Agent^2$는 다양한 환경과 알고리즘에 걸쳐 지능형 에이전트 생성을 표준화하는 통합 프레임워크를 제공하며, 지속적인 개선을 위한 적응형 훈련 관리와 지능형 피드백 분석을 통합한다. MuJoCo, MetaDrive, MPE, SMAC을 포함한 광범위한 벤치마크에서의 포괄적인 실험은 $Agent^2$가 모든 작업에서 수동으로 설계된 솔루션을 일관되게 능가하며, 최대 55%의 성능 향상과 평균적으로 상당한 개선을 달성함을 보여준다. 진정한 종단간 폐루프 자동화를 가능하게 함으로써, 본 연구는 지능형 에이전트가 다른 에이전트를 설계하고 최적화하는 새로운 패러다임을 확립하며, 자동화된 AI 시스템에 대한 근본적인 돌파구를 제시한다.

## 📝 요약

이 논문은 강화 학습 에이전트 개발의 자동화를 목표로 하는 $Agent^2$라는 새로운 프레임워크를 소개합니다. $Agent^2$는 자연어로 된 작업 설명과 환경 코드를 고성능 강화 학습 솔루션으로 자동 변환합니다. 이 시스템은 두 가지 주요 단계, 즉 MDP 모델링과 알고리즘 최적화를 통해 에이전트 생성을 효과적으로 수행합니다. $Agent^2$는 Generator Agent와 Target Agent로 구성된 이중 에이전트 구조를 특징으로 하며, 다양한 환경과 알고리즘에서 지능형 에이전트 생성을 표준화합니다. 실험 결과, $Agent^2$는 수작업으로 설계된 솔루션보다 최대 55% 향상된 성능을 보이며, 자동화된 AI 시스템의 새로운 패러다임을 제시합니다.

## 🎯 주요 포인트

- 1. $Agent^2$는 자연어 작업 설명과 환경 코드를 고성능 강화 학습 솔루션으로 자동 변환하는 완전 자동화된 RL 에이전트 설계 프레임워크입니다.

- 2. 이 시스템은 두 단계로 RL 개발을 분해하여 MDP 모델링과 알고리즘 최적화를 통해 보다 효과적인 에이전트 생성을 가능하게 합니다.

- 3. $Agent^2$는 다양한 환경과 알고리즘에 걸쳐 지능형 에이전트 생성을 표준화하는 통합 프레임워크를 제공합니다.

- 4. 실험 결과, $Agent^2$는 모든 작업에서 수작업으로 설계된 솔루션보다 최대 55%의 성능 향상을 달성하며 일관되게 우수한 성능을 보였습니다.

- 5. 이 연구는 지능형 에이전트가 다른 에이전트를 설계하고 최적화하는 새로운 패러다임을 제시하며, 자동화된 AI 시스템의 근본적인 발전을 의미합니다.

---

*Generated on 2025-09-19 10:26:27*