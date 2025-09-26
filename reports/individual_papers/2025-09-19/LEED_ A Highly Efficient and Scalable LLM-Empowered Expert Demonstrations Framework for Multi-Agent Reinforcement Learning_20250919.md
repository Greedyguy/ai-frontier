---
keywords:
  - Large Language Models
  - Reinforcement Learning
  - Federated Learning
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14680
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:39:12.011849",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Reinforcement Learning",
    "Federated Learning"
  ],
  "rejected_keywords": [
    "Expert Demonstrations"
  ],
  "similarity_scores": {
    "Large Language Models": 0.82,
    "Reinforcement Learning": 0.78,
    "Federated Learning": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# LEED: A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning

**Korean Title:** LEED: 다중 에이전트 강화 학습을 위한 고효율 확장 가능 LLM 기반 전문가 시연 프레임워크

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|Multi-agent reinforcement learning]], [[keywords/Federated Learning|Decentralized training]]
**🚀 Evolved Concepts**: [[keywords/Large Language Models|Large language models]]

## 🔗 유사한 논문
- [[Vulnerable_Agent_Identification_in_Large-Scale_Multi-Agent_Reinforcement_Learning_20250919|Vulnerable Agent Identification in Large-Scale Multi-Agent Reinforcement Learning]] (84.8% similar)
- [[Process-Supervised_Reinforcement_Learning_for_Interactive_Multimodal_Tool-Use_Agents_20250919|Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents]] (84.5% similar)
- [[Predicting_Multi-Agent_Specialization_via_Task_Parallelizability_20250919|Predicting Multi-Agent Specialization via Task Parallelizability]] (84.4% similar)
- [[Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (84.4% similar)
- [[$Agent^2$ An Agent-Generates-Agent Framework for Reinforcement Learning Automation]] (83.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14680v1 Announce Type: cross 
Abstract: Multi-agent reinforcement learning (MARL) holds substantial promise for intelligent decision-making in complex environments. However, it suffers from a coordination and scalability bottleneck as the number of agents increases. To address these issues, we propose the LLM-empowered expert demonstrations framework for multi-agent reinforcement learning (LEED). LEED consists of two components: a demonstration generation (DG) module and a policy optimization (PO) module. Specifically, the DG module leverages large language models to generate instructions for interacting with the environment, thereby producing high-quality demonstrations. The PO module adopts a decentralized training paradigm, where each agent utilizes the generated demonstrations to construct an expert policy loss, which is then integrated with its own policy loss. This enables each agent to effectively personalize and optimize its local policy based on both expert knowledge and individual experience. Experimental results show that LEED achieves superior sample efficiency, time efficiency, and robust scalability compared to state-of-the-art baselines.

## 🔍 Abstract (한글 번역)

arXiv:2509.14680v1 발표 유형: 교차  
초록: 다중 에이전트 강화 학습(MARL)은 복잡한 환경에서 지능적인 의사결정을 위한 상당한 가능성을 가지고 있습니다. 그러나 에이전트의 수가 증가함에 따라 조정 및 확장성의 병목 현상이 발생합니다. 이러한 문제를 해결하기 위해, 우리는 다중 에이전트 강화 학습을 위한 LLM 기반 전문가 시연 프레임워크인 LEED를 제안합니다. LEED는 시연 생성(DG) 모듈과 정책 최적화(PO) 모듈의 두 가지 구성 요소로 이루어져 있습니다. 구체적으로, DG 모듈은 대형 언어 모델을 활용하여 환경과 상호작용하기 위한 지침을 생성함으로써 고품질의 시연을 생성합니다. PO 모듈은 각 에이전트가 생성된 시연을 활용하여 전문가 정책 손실을 구성하고 이를 자신의 정책 손실과 통합하는 분산형 학습 패러다임을 채택합니다. 이를 통해 각 에이전트는 전문가 지식과 개별 경험을 기반으로 자신의 로컬 정책을 효과적으로 개인화하고 최적화할 수 있습니다. 실험 결과, LEED는 최신 기준과 비교하여 우수한 샘플 효율성, 시간 효율성 및 견고한 확장성을 달성함을 보여줍니다.

## 📝 요약

이 논문은 다중 에이전트 강화 학습(MARL)의 조정 및 확장성 문제를 해결하기 위해 LLM 기반 전문가 시연 프레임워크(LEED)를 제안합니다. LEED는 시연 생성(DG) 모듈과 정책 최적화(PO) 모듈로 구성됩니다. DG 모듈은 대형 언어 모델을 활용해 환경과 상호작용하는 지침을 생성하여 고품질 시연을 제공합니다. PO 모듈은 분산된 훈련 패러다임을 채택하여 각 에이전트가 생성된 시연을 활용해 전문가 정책 손실을 구축하고 이를 자체 정책 손실과 통합합니다. 이를 통해 각 에이전트는 전문가 지식과 개인 경험을 바탕으로 로컬 정책을 효과적으로 최적화할 수 있습니다. 실험 결과, LEED는 최신 기준보다 우수한 샘플 효율성, 시간 효율성 및 확장성을 보였습니다.

## 🎯 주요 포인트

- 1. 다중 에이전트 강화 학습(MARL)은 복잡한 환경에서의 지능적 의사결정에 유망하지만, 에이전트 수가 증가함에 따라 조정 및 확장성 문제를 겪습니다.

- 2. LEED는 대규모 언어 모델을 활용하여 환경과 상호작용하기 위한 지침을 생성하고, 이를 통해 고품질의 시범을 생성합니다.

- 3. 정책 최적화 모듈은 분산된 훈련 패러다임을 채택하여 각 에이전트가 생성된 시범을 사용해 전문가 정책 손실을 구성하고, 이를 자신의 정책 손실과 통합합니다.

- 4. 실험 결과, LEED는 최신 기준선과 비교하여 우수한 샘플 효율성, 시간 효율성, 강력한 확장성을 달성했습니다.

---

*Generated on 2025-09-19 15:35:43*