---
keywords:
  - Local-Canonicalization Equivariant Graph Neural Networks
  - Graph Neural Networks
  - Reinforcement Learning
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14431
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:37:16.629349",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Local-Canonicalization Equivariant Graph Neural Networks",
    "Graph Neural Networks",
    "Reinforcement Learning"
  ],
  "rejected_keywords": [
    "Swarm Robot Control"
  ],
  "similarity_scores": {
    "Local-Canonicalization Equivariant Graph Neural Networks": 0.82,
    "Graph Neural Networks": 0.8,
    "Reinforcement Learning": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Local-Canonicalization Equivariant Graph Neural Networks for Sample-Efficient and Generalizable Swarm Robot Control

**Korean Title:** 샘플 효율적이고 일반화 가능한 군집 로봇 제어를 위한 지역-정준화 등변 그래프 신경망

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Networks|Graph Neural Networks]], [[keywords/Reinforcement Learning|Multi-agent reinforcement learning]]
**⚡ Unique Technical**: [[keywords/Local-Canonicalization Equivariant Graph Neural Networks|Local-Canonicalization Equivariant Graph Neural Networks]]

## 🔗 유사한 논문
- [[LEED A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning]] (88.1% similar)
- [[Vulnerable Agent Identification in Large-Scale Multi-Agent Reinforcement Learning_20250919|Vulnerable Agent Identification in Large-Scale Multi-Agent Reinforcement Learning]] (84.8% similar)
- [[CRAFT Coaching Reinforcement Learning Autonomously using Foundation Models for Multi-Robot Coordination Tasks]] (84.6% similar)
- [[MIMIC-D Multi-modal Imitation for MultI-agent Coordination with Decentralized Diffusion Policies]] (83.8% similar)
- [[Traffic Co-Simulation Framework Empowered by Infrastructure Camera Sensing and Reinforcement Learning_20250919|Traffic Co-Simulation Framework Empowered by Infrastructure Camera Sensing and Reinforcement Learning]] (83.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14431v1 Announce Type: new 
Abstract: Multi-agent reinforcement learning (MARL) has emerged as a powerful paradigm for coordinating swarms of agents in complex decision-making, yet major challenges remain. In competitive settings such as pursuer-evader tasks, simultaneous adaptation can destabilize training; non-kinetic countermeasures often fail under adverse conditions; and policies trained in one configuration rarely generalize to environments with a different number of agents. To address these issues, we propose the Local-Canonicalization Equivariant Graph Neural Networks (LEGO) framework, which integrates seamlessly with popular MARL algorithms such as MAPPO. LEGO employs graph neural networks to capture permutation equivariance and generalization to different agent numbers, canonicalization to enforce E(n)-equivariance, and heterogeneous representations to encode role-specific inductive biases. Experiments on cooperative and competitive swarm benchmarks show that LEGO outperforms strong baselines and improves generalization. In real-world experiments, LEGO demonstrates robustness to varying team sizes and agent failure.

## 🔍 Abstract (한글 번역)

arXiv:2509.14431v1 발표 유형: 신규  
초록: 다중 에이전트 강화 학습(MARL)은 복잡한 의사 결정에서 에이전트 무리를 조정하는 강력한 패러다임으로 부상하였으나 여전히 주요 과제가 남아 있습니다. 추적자-회피자 과제와 같은 경쟁 환경에서는 동시 적응이 훈련을 불안정하게 만들 수 있으며, 비운동적 대응책은 악조건에서 종종 실패하고, 하나의 구성에서 훈련된 정책은 다른 수의 에이전트를 가진 환경에 일반화되지 않는 경우가 많습니다. 이러한 문제를 해결하기 위해, 우리는 MAPPO와 같은 인기 있는 MARL 알고리즘과 원활하게 통합되는 Local-Canonicalization Equivariant Graph Neural Networks (LEGO) 프레임워크를 제안합니다. LEGO는 그래프 신경망을 사용하여 순열 등가성과 다양한 에이전트 수에 대한 일반화를 포착하고, E(n)-등가성을 강제하는 정준화를 수행하며, 역할별 귀납적 편향을 인코딩하는 이질적 표현을 사용합니다. 협력 및 경쟁 무리 벤치마크에 대한 실험 결과, LEGO는 강력한 기준선을 능가하고 일반화를 개선함을 보여줍니다. 실제 실험에서 LEGO는 다양한 팀 크기와 에이전트 실패에 대한 견고성을 입증합니다.

## 📝 요약

이 논문은 다중 에이전트 강화 학습(MARL)에서 발생하는 문제를 해결하기 위해 Local-Canonicalization Equivariant Graph Neural Networks (LEGO) 프레임워크를 제안합니다. LEGO는 그래프 신경망을 활용하여 에이전트 수의 변화에 대한 일반화를 지원하고, E(n)-등변성을 보장하며, 역할별 유도 편향을 인코딩합니다. MAPPO와 같은 기존 MARL 알고리즘과 통합이 가능하며, 협력 및 경쟁 환경에서의 실험을 통해 강력한 성능과 일반화 능력을 입증했습니다. 실제 환경에서도 다양한 팀 크기와 에이전트 실패에 대한 강건성을 보여주었습니다.

## 🎯 주요 포인트

- 1. 다중 에이전트 강화 학습(MARL)은 복잡한 의사결정에서 에이전트 무리를 조정하는 강력한 패러다임으로 부상했으나, 여전히 주요 과제가 존재합니다.

- 2. 경쟁 환경에서의 동시 적응은 훈련을 불안정하게 만들 수 있으며, 비운동적 대응책은 악조건에서 종종 실패합니다.

- 3. LEGO 프레임워크는 그래프 신경망을 활용하여 다른 수의 에이전트에 대한 일반화를 가능하게 하고, 역할별 귀납적 편향을 인코딩합니다.

- 4. LEGO는 협력 및 경쟁적 무리 벤치마크 실험에서 강력한 기준선을 능가하며 일반화를 개선합니다.

- 5. 실제 실험에서 LEGO는 팀 크기 변화와 에이전트 실패에 대한 강건성을 보여줍니다.

---

*Generated on 2025-09-19 16:30:13*