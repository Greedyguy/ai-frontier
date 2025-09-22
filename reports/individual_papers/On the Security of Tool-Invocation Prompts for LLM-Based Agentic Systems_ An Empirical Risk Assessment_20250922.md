# On the Security of Tool-Invocation Prompts for LLM-Based Agentic Systems: An Empirical Risk Assessment

**Korean Title:** 도구 호출 프롬프트의 보안에 관한 연구: LLM 기반 에이전트 시스템의 경험적 위험 평가

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Agentic Systems

## 🔗 유사한 논문
- [[2025-09-19/A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks_20250919|A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks]] (86.9% similar)
- [[2025-09-19/Enterprise AI Must Enforce Participant-Aware Access Control_20250919|Enterprise AI Must Enforce Participant-Aware Access Control]] (84.7% similar)
- [[2025-09-19/The Sum Leaks More Than Its Parts_ Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration_20250919|The Sum Leaks More Than Its Parts Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration]] (83.2% similar)
- [[2025-09-19/From Capabilities to Performance_ Evaluating Key Functional Properties of LLM Architectures in Penetration Testing_20250919|From Capabilities to Performance Evaluating Key Functional Properties of LLM Architectures in Penetration Testing]] (83.0% similar)
- [[2025-09-18/An LLM Agentic Approach for Legal-Critical Software_ A Case Study for Tax Prep Software_20250918|An LLM Agentic Approach for Legal-Critical Software A Case Study for Tax Prep Software]] (82.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.05755v4 Announce Type: replace-cross 
Abstract: LLM-based agentic systems leverage large language models to handle user queries, make decisions, and execute external tools for complex tasks across domains like chatbots, customer service, and software engineering. A critical component of these systems is the Tool Invocation Prompt (TIP), which defines tool interaction protocols and guides LLMs to ensure the security and correctness of tool usage. Despite its importance, TIP security has been largely overlooked. This work investigates TIP-related security risks, revealing that major LLM-based systems like Cursor, Claude Code, and others are vulnerable to attacks such as remote code execution (RCE) and denial of service (DoS). Through a systematic TIP exploitation workflow (TEW), we demonstrate external tool behavior hijacking via manipulated tool invocations. We also propose defense mechanisms to enhance TIP security in LLM-based agentic systems.

## 🔍 Abstract (한글 번역)

arXiv:2509.05755v4 발표 유형: 교체-크로스  
초록: LLM 기반의 에이전트 시스템은 대형 언어 모델을 활용하여 사용자 쿼리를 처리하고, 결정을 내리며, 챗봇, 고객 서비스, 소프트웨어 엔지니어링과 같은 다양한 분야에서 복잡한 작업을 수행하기 위해 외부 도구를 실행합니다. 이러한 시스템의 중요한 구성 요소는 도구 호출 프롬프트(TIP)로, 도구 상호작용 프로토콜을 정의하고 LLM이 도구 사용의 보안성과 정확성을 보장하도록 안내합니다. 그 중요성에도 불구하고, TIP 보안은 크게 간과되어 왔습니다. 이 연구는 TIP 관련 보안 위험을 조사하여, Cursor, Claude Code 등과 같은 주요 LLM 기반 시스템이 원격 코드 실행(RCE) 및 서비스 거부(DoS)와 같은 공격에 취약하다는 것을 밝혀냅니다. 체계적인 TIP 악용 워크플로우(TEW)를 통해 조작된 도구 호출을 통한 외부 도구 동작 하이재킹을 시연합니다. 또한, LLM 기반 에이전트 시스템의 TIP 보안을 강화하기 위한 방어 메커니즘을 제안합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)을 기반으로 한 에이전트 시스템에서 사용되는 도구 호출 프롬프트(TIP)의 보안 문제를 다룹니다. TIP는 도구 상호작용 프로토콜을 정의하여 LLM의 도구 사용을 안내하는 중요한 요소입니다. 그러나 TIP의 보안은 지금까지 크게 간과되어 왔습니다. 연구 결과, Cursor, Claude Code 등 주요 LLM 기반 시스템이 원격 코드 실행(RCE) 및 서비스 거부(DoS) 공격에 취약함을 밝혀냈습니다. 저자들은 체계적인 TIP 악용 워크플로우(TEW)를 통해 외부 도구의 동작이 조작된 도구 호출에 의해 탈취될 수 있음을 시연하였으며, TIP 보안을 강화하기 위한 방어 메커니즘도 제안합니다.

## 🎯 주요 포인트

- 1. LLM 기반 에이전트 시스템은 사용자 쿼리 처리, 의사 결정, 외부 도구 실행을 통해 다양한 분야의 복잡한 작업을 수행합니다.

- 2. 도구 호출 프롬프트(TIP)는 도구 상호작용 프로토콜을 정의하고 LLM의 도구 사용의 보안성과 정확성을 보장하는 중요한 요소입니다.

- 3. 주요 LLM 기반 시스템들이 원격 코드 실행(RCE) 및 서비스 거부(DoS) 공격에 취약하다는 TIP 관련 보안 위험이 밝혀졌습니다.

- 4. TIP 악용 워크플로우(TEW)를 통해 조작된 도구 호출로 외부 도구 동작을 탈취할 수 있음을 시연했습니다.

- 5. LLM 기반 에이전트 시스템에서 TIP 보안을 강화하기 위한 방어 메커니즘을 제안했습니다.

---

*Generated on 2025-09-22 15:02:04*