<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:26:14.851298",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Agentic Large Language Model",
    "Prompt Whitelisting",
    "Jailbreak Attacks",
    "False Positive and False Negative Rates"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Agentic Large Language Model": 0.8,
    "Prompt Whitelisting": 0.85,
    "Jailbreak Attacks": 0.78,
    "False Positive and False Negative Rates": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "agentic LLM",
        "canonical": "Agentic Large Language Model",
        "aliases": [
          "agentic LLMs"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel concept of LLMs with agency, which is central to the paper's security approach.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "prompt whitelisting",
        "canonical": "Prompt Whitelisting",
        "aliases": [
          "whitelist prompts"
        ],
        "category": "unique_technical",
        "rationale": "Key technique proposed in the paper to enhance security for LLMs.",
        "novelty_score": 0.78,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.85
      },
      {
        "surface": "jailbreak attacks",
        "canonical": "Jailbreak Attacks",
        "aliases": [
          "jailbreaking"
        ],
        "category": "specific_connectable",
        "rationale": "Represents a significant threat model addressed by the paper's security framework.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "false positive and false negative rates",
        "canonical": "False Positive and False Negative Rates",
        "aliases": [
          "error rates"
        ],
        "category": "specific_connectable",
        "rationale": "Metrics used to evaluate the effectiveness of the proposed security approach.",
        "novelty_score": 0.6,
        "connectivity_score": 0.72,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "traditional models",
      "operational security",
      "information security"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "agentic LLM",
      "resolved_canonical": "Agentic Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "prompt whitelisting",
      "resolved_canonical": "Prompt Whitelisting",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "jailbreak attacks",
      "resolved_canonical": "Jailbreak Attacks",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "false positive and false negative rates",
      "resolved_canonical": "False Positive and False Negative Rates",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.72,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# LLMZ+: Contextual Prompt Whitelist Principles for Agentic LLMs

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18557.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18557](https://arxiv.org/abs/2509.18557)

## 🔗 유사한 논문
- [[2025-09-19/A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks_20250919|A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks]] (87.5% similar)
- [[2025-09-23/Privacy in Action_ Towards Realistic Privacy Mitigation and Evaluation for LLM-Powered Agents_20250923|Privacy in Action: Towards Realistic Privacy Mitigation and Evaluation for LLM-Powered Agents]] (85.6% similar)
- [[2025-09-18/Agentic JWT_ A Secure Delegation Protocol for Autonomous AI Agents_20250918|Agentic JWT: A Secure Delegation Protocol for Autonomous AI Agents]] (85.6% similar)
- [[2025-09-19/Exploit Tool Invocation Prompt for Tool Behavior Hijacking in LLM-Based Agentic System_20250919|Exploit Tool Invocation Prompt for Tool Behavior Hijacking in LLM-Based Agentic System]] (85.5% similar)
- [[2025-09-23/Sugar-Coated Poison_ Benign Generation Unlocks LLM Jailbreaking_20250923|Sugar-Coated Poison: Benign Generation Unlocks LLM Jailbreaking]] (84.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Jailbreak Attacks|Jailbreak Attacks]], [[keywords/False Positive and False Negative Rates|False Positive and False Negative Rates]]
**⚡ Unique Technical**: [[keywords/Agentic Large Language Model|Agentic Large Language Model]], [[keywords/Prompt Whitelisting|Prompt Whitelisting]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18557v1 Announce Type: new 
Abstract: Compared to traditional models, agentic AI represents a highly valuable target for potential attackers as they possess privileged access to data sources and API tools, which are traditionally not incorporated into classical agents. Unlike a typical software application residing in a Demilitarized Zone (DMZ), agentic LLMs consciously rely on nondeterministic behavior of the AI (only defining a final goal, leaving the path selection to LLM). This characteristic introduces substantial security risk to both operational security and information security. Most common existing defense mechanism rely on detection of malicious intent and preventing it from reaching the LLM agent, thus protecting against jailbreak attacks such as prompt injection. In this paper, we present an alternative approach, LLMZ+, which moves beyond traditional detection-based approaches by implementing prompt whitelisting. Through this method, only contextually appropriate and safe messages are permitted to interact with the agentic LLM. By leveraging the specificity of context, LLMZ+ guarantees that all exchanges between external users and the LLM conform to predefined use cases and operational boundaries. Our approach streamlines the security framework, enhances its long-term resilience, and reduces the resources required for sustaining LLM information security. Our empirical evaluation demonstrates that LLMZ+ provides strong resilience against the most common jailbreak prompts. At the same time, legitimate business communications are not disrupted, and authorized traffic flows seamlessly between users and the agentic LLM. We measure the effectiveness of approach using false positive and false negative rates, both of which can be reduced to 0 in our experimental setting.

## 📝 요약

이 논문은 전통적인 탐지 기반 방어 메커니즘을 넘어 새로운 보안 접근법인 LLMZ+를 제안합니다. 기존의 에이전트와 달리, 에이전틱 AI는 데이터 소스와 API 도구에 대한 특권적 접근을 가지며, 비결정론적 행동을 통해 보안 위험을 초래합니다. LLMZ+는 프롬프트 화이트리스트를 구현하여 맥락적으로 적절하고 안전한 메시지만 에이전틱 LLM과 상호작용하도록 허용합니다. 이를 통해 보안 프레임워크를 간소화하고 장기적인 회복력을 강화하며, 정보 보안 유지에 필요한 자원을 줄입니다. 실험 결과, LLMZ+는 일반적인 탈옥 프롬프트에 강한 저항성을 보이며, 합법적인 비즈니스 커뮤니케이션은 방해받지 않고 원활하게 이루어집니다. 실험에서는 오탐률과 미탐률을 0으로 줄일 수 있음을 확인했습니다.

## 🎯 주요 포인트

- 1. 에이전틱 AI는 데이터 소스와 API 도구에 대한 특권적 접근으로 인해 공격자에게 높은 가치를 지닌 표적이 된다.
- 2. 에이전틱 LLM의 비결정론적 행동은 운영 및 정보 보안에 상당한 위험을 초래한다.
- 3. LLMZ+는 전통적인 탐지 기반 접근 방식을 넘어 프롬프트 화이트리스트를 구현하여 보안을 강화한다.
- 4. LLMZ+는 외부 사용자와 LLM 간의 모든 교환이 사전 정의된 사용 사례와 운영 경계를 준수하도록 보장한다.
- 5. 실험 결과, LLMZ+는 일반적인 탈옥 프롬프트에 대해 강력한 내성을 제공하며, 합법적인 비즈니스 통신은 방해받지 않는다.


---

*Generated on 2025-09-24 13:26:14*