
# Agentic JWT: A Secure Delegation Protocol for Autonomous AI Agents

**Korean Title:** 에이전틱 JWT: 자율 AI 에이전트를 위한 안전한 위임 프로토콜

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Zero-trust Guarantees

## 🔗 유사한 논문
- [[AppAgent v2 Advanced Agent for Flexible Mobile Interactions]] (82.9% similar)
- [[$Agent^2$ An Agent-Generates-Agent Framework for Reinforcement Learning Automation]] (81.3% similar)
- [[VeriOS Query-Driven Proactive Human-Agent-GUI Interaction for Trustworthy OS Agents]] (80.6% similar)
- [[Agentic UAVs LLM-Driven Autonomy with Integrated Tool-Calling and Cognitive Reasoning]] (80.4% similar)
- [[ASTREA Introducing Agentic Intelligence for Orbital Thermal Autonomy]] (80.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13597v1 Announce Type: cross 
Abstract: Autonomous LLM agents can issue thousands of API calls per hour without human oversight. OAuth 2.0 assumes deterministic clients, but in agentic settings stochastic reasoning, prompt injection, or multi-agent orchestration can silently expand privileges.
  We introduce Agentic JWT (A-JWT), a dual-faceted intent token that binds each agent's action to verifiable user intent and, optionally, to a specific workflow step. A-JWT carries an agent's identity as a one-way checksum hash derived from its prompt, tools and configuration, and a chained delegation assertion to prove which downstream agent may execute a given task, and per-agent proof-of-possession keys to prevent replay and in-process impersonation. We define a new authorization mechanism and add a lightweight client shim library that self-verifies code at run time, mints intent tokens, tracks workflow steps and derives keys, thus enabling secure agent identity and separation even within a single process.
  We illustrate a comprehensive threat model for agentic applications, implement a Python proof-of-concept and show functional blocking of scope-violating requests, replay, impersonation, and prompt-injection pathways with sub-millisecond overhead on commodity hardware. The design aligns with ongoing OAuth agent discussions and offers a drop-in path toward zero-trust guarantees for agentic applications. A comprehensive performance and security evaluation with experimental results will appear in our forthcoming journal publication

## 🔍 Abstract (한글 번역)

arXiv:2509.13597v1 공지 유형: cross 
초록: 자율 LLM 에이전트는 인간의 감독 없이 시간당 수천 건의 API 호출을 수행할 수 있다. OAuth 2.0은 결정론적 클라이언트를 가정하지만, 에이전트 환경에서는 확률적 추론, 프롬프트 인젝션, 또는 다중 에이전트 오케스트레이션이 권한을 은밀하게 확장할 수 있다.

본 연구에서는 각 에이전트의 행동을 검증 가능한 사용자 의도와 연결하고, 선택적으로 특정 워크플로 단계와 연결하는 이중 측면 의도 토큰인 Agentic JWT(A-JWT)를 소개한다. A-JWT는 프롬프트, 도구, 구성으로부터 파생된 일방향 체크섬 해시로서 에이전트의 정체성을 담고 있으며, 어떤 하위 에이전트가 주어진 작업을 수행할 수 있는지 증명하는 연쇄 위임 어설션(chained delegation assertion)과, 재생 공격 및 프로세스 내 가장을 방지하기 위한 에이전트별 소유 증명 키를 포함한다. 우리는 새로운 인가 메커니즘을 정의하고, 런타임에 코드를 자체 검증하고, 의도 토큰을 발행하며, 워크플로 단계를 추적하고 키를 파생하는 경량 클라이언트 심 라이브러리를 추가하여, 단일 프로세스 내에서도 안전한 에이전트 정체성과 분리를 가능하게 한다.

본 연구는 에이전트 애플리케이션에 대한 포괄적인 위협 모델을 제시하고, Python 개념 증명을 구현하며, 범위 위반 요청, 재생 공격, 가장, 프롬프트 인젝션 경로에 대한 기능적 차단을 일반 하드웨어에서 1밀리초 미만의 오버헤드로 보여준다. 이 설계는 진행 중인 OAuth 에이전트 논의와 일치하며, 에이전트 애플리케이션을 위한 제로 트러스트 보장으로 가는 드롭인 경로를 제공한다. 실험 결과를 포함한 포괄적인 성능 및 보안 평가는 향후 저널 출간물에서 발표될 예정이다.

## 📝 요약

이 논문은 자율적인 LLM 에이전트가 인간의 감독 없이 수천 개의 API 호출을 수행할 수 있는 환경에서 발생할 수 있는 보안 문제를 해결하기 위해 Agentic JWT (A-JWT)를 제안합니다. A-JWT는 에이전트의 행동을 사용자 의도와 특정 워크플로우 단계에 연결하여 검증 가능한 토큰을 제공합니다. 이를 통해 에이전트의 신원을 확인하고, 작업 실행 권한을 증명하며, 재사용 및 위장 공격을 방지합니다. 새로운 인증 메커니즘과 경량 클라이언트 라이브러리를 도입하여 에이전트의 신원과 작업 분리를 보장합니다. Python을 사용한 개념 증명을 통해 보안 위협을 효과적으로 차단할 수 있음을 보여주며, 이는 OAuth 에이전트 논의와 일치하고 에이전트 애플리케이션에 대한 신뢰 보장을 제공합니다. 향후 저널에 성능 및 보안 평가 결과를 발표할 예정입니다.

## 🎯 주요 포인트

- 1. 자율적인 LLM 에이전트는 인간의 감독 없이 시간당 수천 개의 API 호출을 수행할 수 있습니다.

- 2. Agentic JWT(A-JWT)는 에이전트의 행동을 검증 가능한 사용자 의도와 특정 워크플로우 단계에 연결하는 이중 목적의 토큰입니다.

- 3. A-JWT는 에이전트의 정체성을 일방향 체크섬 해시로 포함하고, 위임 주장을 통해 하위 에이전트의 작업 실행을 증명합니다.

- 4. 새로운 인증 메커니즘과 경량 클라이언트 라이브러리를 도입하여 에이전트의 신원과 프로세스 내 분리를 보장합니다.

- 5. Python으로 구현된 개념 증명을 통해 범위 위반 요청, 재생 공격, 가장 및 프롬프트 주입 경로를 차단하는 기능을 보여줍니다.

---

*Generated on 2025-09-19 10:38:16*