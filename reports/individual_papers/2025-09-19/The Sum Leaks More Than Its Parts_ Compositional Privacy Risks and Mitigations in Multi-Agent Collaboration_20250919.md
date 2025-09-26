---
keywords:
  - Large Language Models
  - Collaborative Consensus Defense
  - Compositional Privacy Leakage
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14284
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:21:32.855339",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Collaborative Consensus Defense",
    "Compositional Privacy Leakage"
  ],
  "rejected_keywords": [
    "Theory-of-Mind Defense",
    "Multi-Agent Systems"
  ],
  "similarity_scores": {
    "Large Language Models": 0.8,
    "Collaborative Consensus Defense": 0.72,
    "Compositional Privacy Leakage": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# The Sum Leaks More Than Its Parts: Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration

**Korean Title:** 부분의 합보다 더 많이 유출됨: 다중 에이전트 협업에서의 구성적 프라이버시 위험과 완화 방안

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Large Language Models|Large Language Models]]
**⚡ Unique Technical**: [[keywords/Collaborative Consensus Defense|Collaborative Consensus Defense]], [[keywords/Compositional Privacy Leakage|Compositional Privacy Leakage]]

## 🔗 유사한 논문
- [[Language Models Identify Ambiguities and Exploit Loopholes]] (83.9% similar)
- [[Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (83.4% similar)
- [[Understanding and Mitigating Overrefusal in LLMs from an Unveiling Perspective of Safety Decision Boundary]] (83.4% similar)
- [[CyberLLMInstruct A Pseudo-malicious Dataset Revealing Safety-performance Trade-offs in Cyber Security LLM Fine-tuning]] (83.2% similar)
- [[From Capabilities to Performance Evaluating Key Functional Properties of LLM Architectures in Penetration Testing]] (82.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14284v1 Announce Type: cross 
Abstract: As large language models (LLMs) become integral to multi-agent systems, new privacy risks emerge that extend beyond memorization, direct inference, or single-turn evaluations. In particular, seemingly innocuous responses, when composed across interactions, can cumulatively enable adversaries to recover sensitive information, a phenomenon we term compositional privacy leakage. We present the first systematic study of such compositional privacy leaks and possible mitigation methods in multi-agent LLM systems. First, we develop a framework that models how auxiliary knowledge and agent interactions jointly amplify privacy risks, even when each response is benign in isolation. Next, to mitigate this, we propose and evaluate two defense strategies: (1) Theory-of-Mind defense (ToM), where defender agents infer a questioner's intent by anticipating how their outputs may be exploited by adversaries, and (2) Collaborative Consensus Defense (CoDef), where responder agents collaborate with peers who vote based on a shared aggregated state to restrict sensitive information spread. Crucially, we balance our evaluation across compositions that expose sensitive information and compositions that yield benign inferences. Our experiments quantify how these defense strategies differ in balancing the privacy-utility trade-off. We find that while chain-of-thought alone offers limited protection to leakage (~39% sensitive blocking rate), our ToM defense substantially improves sensitive query blocking (up to 97%) but can reduce benign task success. CoDef achieves the best balance, yielding the highest Balanced Outcome (79.8%), highlighting the benefit of combining explicit reasoning with defender collaboration. Together, our results expose a new class of risks in collaborative LLM deployments and provide actionable insights for designing safeguards against compositional, context-driven privacy leakage.

## 🔍 Abstract (한글 번역)

arXiv:2509.14284v1 발표 유형: 교차  
초록: 대형 언어 모델(LLMs)이 다중 에이전트 시스템의 필수 요소가 됨에 따라, 암기, 직접 추론 또는 단일 턴 평가를 넘어서는 새로운 프라이버시 위험이 발생하고 있습니다. 특히, 개별적으로는 무해해 보이는 응답들이 상호작용을 통해 조합될 때, 적대자가 민감한 정보를 복구할 수 있게 하는 현상을 우리는 조합적 프라이버시 누출(compositional privacy leakage)이라고 명명합니다. 우리는 다중 에이전트 LLM 시스템에서 이러한 조합적 프라이버시 누출과 가능한 완화 방법에 대한 최초의 체계적인 연구를 제시합니다. 먼저, 보조 지식과 에이전트 상호작용이 어떻게 개별 응답이 무해할 때에도 프라이버시 위험을 증폭시키는지를 모델링하는 프레임워크를 개발합니다. 다음으로, 이를 완화하기 위해 두 가지 방어 전략을 제안하고 평가합니다: (1) 마음 이론 방어(ToM), 여기서 방어 에이전트는 적대자가 자신의 출력을 어떻게 악용할 수 있을지를 예상하여 질문자의 의도를 추론하며, (2) 협력적 합의 방어(CoDef), 여기서 응답 에이전트는 공유된 집계 상태에 기반하여 투표하는 동료들과 협력하여 민감한 정보 확산을 제한합니다. 중요한 것은, 우리는 민감한 정보를 노출하는 조합과 무해한 추론을 산출하는 조합 간의 평가 균형을 맞춥니다. 우리의 실험은 이러한 방어 전략이 프라이버시-유용성 균형을 맞추는 데 어떻게 차이가 있는지를 정량화합니다. 우리는 연쇄 사고(chain-of-thought)만으로는 누출에 대한 보호가 제한적임을 발견했으며(~39% 민감 차단율), 우리의 ToM 방어는 민감한 쿼리 차단을 상당히 개선하지만(최대 97%), 무해한 작업 성공률을 감소시킬 수 있음을 발견했습니다. CoDef는 최고의 균형을 달성하여, 가장 높은 균형 결과(79.8%)를 제공하며, 명시적 추론과 방어자 협력의 결합 이점을 강조합니다. 우리의 결과는 협력적 LLM 배치에서 새로운 유형의 위험을 드러내며, 조합적, 맥락 기반 프라이버시 누출에 대한 안전장치를 설계하기 위한 실질적인 통찰을 제공합니다.

## 📝 요약

대형 언어 모델(LLM)이 다중 에이전트 시스템에 통합됨에 따라 새로운 프라이버시 위험이 발생합니다. 이 연구는 이러한 조합적 프라이버시 누출을 체계적으로 분석하고 완화 방법을 제시합니다. 연구에서는 보조 지식과 에이전트 간 상호작용이 프라이버시 위험을 증대시키는 모델을 개발하였으며, 이를 완화하기 위해 두 가지 방어 전략을 제안합니다. 첫째, '마음 이론 방어(ToM)'는 질문자의 의도를 예측하여 민감한 정보의 악용을 방지하고, 둘째, '협력적 합의 방어(CoDef)'는 에이전트들이 협력하여 민감한 정보 확산을 제한합니다. 실험 결과, ToM 방어는 민감한 쿼리 차단을 크게 개선하지만, 무해한 작업 성공률을 감소시킬 수 있습니다. CoDef는 가장 균형 잡힌 결과를 제공하여 프라이버시와 유용성 간의 균형을 최적화합니다. 이 연구는 협력적 LLM 배치에서의 새로운 위험을 드러내고, 조합적 프라이버시 누출을 방지하기 위한 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM) 기반의 다중 에이전트 시스템에서 조합적 프라이버시 누출(compositional privacy leakage)이 발생할 수 있다.

- 2. 보조 지식과 에이전트 간의 상호작용이 프라이버시 위험을 증폭시킬 수 있음을 모델링하는 프레임워크를 개발하였다.

- 3. 프라이버시 누출을 완화하기 위해 Theory-of-Mind 방어(ToM)와 협력적 합의 방어(CoDef)라는 두 가지 방어 전략을 제안하고 평가하였다.

- 4. ToM 방어는 민감한 쿼리 차단을 크게 개선할 수 있지만, 무해한 작업 성공률을 감소시킬 수 있다.

- 5. CoDef는 민감 정보 차단과 무해한 추론의 균형을 가장 잘 맞추며, 명시적 추론과 방어자 협력의 이점을 강조한다.

---

*Generated on 2025-09-19 14:53:40*