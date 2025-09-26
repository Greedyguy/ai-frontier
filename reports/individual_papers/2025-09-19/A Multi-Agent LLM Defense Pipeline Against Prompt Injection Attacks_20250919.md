---
keywords:
  - Large Language Models
  - Prompt Injection Attacks
  - Multi-Agent Defense Framework
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14285
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:00:15.616202",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Prompt Injection Attacks",
    "Multi-Agent Defense Framework"
  ],
  "rejected_keywords": [
    "Hierarchical Coordinator-Based System"
  ],
  "similarity_scores": {
    "Large Language Models": 0.85,
    "Prompt Injection Attacks": 0.8,
    "Multi-Agent Defense Framework": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks

**Korean Title:** 프롬프트 인젝션 공격에 대한 다중 에이전트 LLM 방어 파이프라인

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Large Language Models|Large Language Models]]
**⚡ Unique Technical**: [[keywords/Prompt Injection Attacks|Prompt Injection Attacks]], [[keywords/Multi-Agent Defense Framework|Multi-Agent Defense Framework]]

## 🔗 유사한 논문
- [[Sentinel_Agents_for_Secure_and_Trustworthy_Agentic_AI_in_Multi-Agent_Systems_20250919|Sentinel Agents for Secure and Trustworthy Agentic AI in Multi-Agent Systems]] (87.6% similar)
- [[Exploit_Tool_Invocation_Prompt_for_Tool_Behavior_Hijacking_in_LLM-Based_Agentic_System_20250919|Exploit Tool Invocation Prompt for Tool Behavior Hijacking in LLM-Based Agentic System]] (86.9% similar)
- [[From Capabilities to Performance Evaluating Key Functional Properties of LLM Architectures in Penetration Testing]] (86.8% similar)
- [[The Sum Leaks More Than Its Parts Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration]] (86.4% similar)
- [[Enterprise_AI_Must_Enforce_Participant-Aware_Access_Control_20250919|Enterprise AI Must Enforce Participant-Aware Access Control]] (85.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14285v1 Announce Type: cross 
Abstract: Prompt injection attacks represent a major vulnerability in Large Language Model (LLM) deployments, where malicious instructions embedded in user inputs can override system prompts and induce unintended behaviors. This paper presents a novel multi-agent defense framework that employs specialized LLM agents in coordinated pipelines to detect and neutralize prompt injection attacks in real-time. We evaluate our approach using two distinct architectures: a sequential chain-of-agents pipeline and a hierarchical coordinator-based system. Our comprehensive evaluation on 55 unique prompt injection attacks, grouped into 8 categories and totaling 400 attack instances across two LLM platforms (ChatGLM and Llama2), demonstrates significant security improvements. Without defense mechanisms, baseline Attack Success Rates (ASR) reached 30% for ChatGLM and 20% for Llama2. Our multi-agent pipeline achieved 100% mitigation, reducing ASR to 0% across all tested scenarios. The framework demonstrates robustness across multiple attack categories including direct overrides, code execution attempts, data exfiltration, and obfuscation techniques, while maintaining system functionality for legitimate queries.

## 🔍 Abstract (한글 번역)

arXiv:2509.14285v1 발표 유형: 교차  
초록: 프롬프트 인젝션 공격은 대형 언어 모델(LLM) 배포에서 주요 취약점을 나타내며, 사용자 입력에 포함된 악의적인 지시가 시스템 프롬프트를 무시하고 의도하지 않은 동작을 유발할 수 있습니다. 본 논문은 실시간으로 프롬프트 인젝션 공격을 탐지하고 무력화하기 위해 전문화된 LLM 에이전트를 조정된 파이프라인으로 활용하는 새로운 다중 에이전트 방어 프레임워크를 제시합니다. 우리는 두 가지 독립된 아키텍처를 사용하여 우리의 접근 방식을 평가합니다: 순차적 에이전트 체인 파이프라인과 계층적 조정자 기반 시스템. ChatGLM과 Llama2라는 두 개의 LLM 플랫폼에서 총 400건의 공격 사례로 구성된 8개의 카테고리로 그룹화된 55개의 고유한 프롬프트 인젝션 공격에 대한 종합적인 평가를 통해 상당한 보안 개선을 입증합니다. 방어 메커니즘이 없을 경우, 기본 공격 성공률(ASR)은 ChatGLM에서 30%, Llama2에서 20%에 달했습니다. 우리의 다중 에이전트 파이프라인은 모든 테스트 시나리오에서 ASR을 0%로 줄이며 100% 완화 효과를 달성했습니다. 이 프레임워크는 직접적인 무시, 코드 실행 시도, 데이터 유출 및 난독화 기술을 포함한 여러 공격 카테고리에서 강력함을 보여주며, 정당한 쿼리에 대한 시스템 기능을 유지합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM) 배포 시 발생할 수 있는 프롬프트 인젝션 공격을 방어하기 위한 새로운 다중 에이전트 방어 프레임워크를 제안합니다. 이 프레임워크는 특화된 LLM 에이전트들을 조정된 파이프라인으로 구성하여 실시간으로 공격을 탐지하고 무력화합니다. 두 가지 아키텍처, 즉 순차적 에이전트 체인과 계층적 조정 시스템을 사용하여 접근법을 평가했습니다. ChatGLM과 Llama2 플랫폼에서 총 400개의 공격 사례를 통해 평가한 결과, 방어 메커니즘이 없을 경우 공격 성공률이 각각 30%와 20%였으나, 제안된 다중 에이전트 파이프라인은 모든 시나리오에서 공격 성공률을 0%로 낮추며 보안성을 크게 향상시켰습니다. 이 프레임워크는 직접 오버라이드, 코드 실행 시도, 데이터 유출, 난독화 기술 등 다양한 공격 유형에 대해 강력한 방어력을 보이면서도 정상적인 쿼리에 대한 시스템 기능을 유지합니다.

## 🎯 주요 포인트

- 1. 프롬프트 인젝션 공격은 대형 언어 모델(LLM) 배포에서 주요 취약점으로, 사용자 입력에 포함된 악의적인 지시가 시스템 프롬프트를 무시하고 의도치 않은 행동을 유발할 수 있다.

- 2. 본 논문은 실시간으로 프롬프트 인젝션 공격을 탐지하고 무력화하기 위해 특화된 LLM 에이전트를 활용한 다중 에이전트 방어 프레임워크를 제안한다.

- 3. 제안된 방어 프레임워크는 순차적 에이전트 체인 파이프라인과 계층적 조정자 기반 시스템 두 가지 아키텍처를 통해 평가되었다.

- 4. 두 LLM 플랫폼(ChatGLM과 Llama2)에서 총 400개의 공격 사례를 대상으로 한 평가에서, 다중 에이전트 파이프라인은 모든 시나리오에서 공격 성공률(ASR)을 0%로 낮추며 100% 완화 성과를 보였다.

- 5. 프레임워크는 직접적인 무시, 코드 실행 시도, 데이터 유출, 난독화 기술을 포함한 다양한 공격 카테고리에서 견고성을 입증하면서도 합법적인 쿼리에 대한 시스템 기능을 유지한다.

---

*Generated on 2025-09-19 15:34:15*