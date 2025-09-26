---
keywords:
  - Reinforcement Learning
  - Proximal Policy Optimization
  - Multi-Objective Optimization
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14816
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:25:19.387774",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Proximal Policy Optimization",
    "Multi-Objective Optimization"
  ],
  "rejected_keywords": [
    "Gradient Conflict Resolution"
  ],
  "similarity_scores": {
    "Reinforcement Learning": 0.88,
    "Proximal Policy Optimization": 0.82,
    "Multi-Objective Optimization": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution

**Korean Title:** 확장 가능한 다목적 로봇 강화 학습을 위한 그래디언트 충돌 해결 방법

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|Reinforcement Learning]], [[keywords/Proximal Policy Optimization|Proximal Policy Optimization]]
**⚡ Unique Technical**: [[keywords/Multi-Objective Optimization|Multi-Objective Optimization]]

## 🔗 유사한 논문
- [[Controllable Pareto Trade-off between Fairness and Accuracy]] (82.4% similar)
- [[TGPO Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning]] (81.9% similar)
- [[Constructive_Conflict-Driven_Multi-Agent_Reinforcement_Learning_for_Strategic_Diversity_20250919|Constructive Conflict-Driven Multi-Agent Reinforcement Learning for Strategic Diversity]] (81.8% similar)
- [[FlowRL Matching Reward Distributions for LLM Reasoning]] (81.8% similar)
- [[Hybrid_Diffusion_Policies_with_Projective_Geometric_Algebra_for_Efficient_Robot_Manipulation_Learning_20250918|Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning]] (81.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14816v1 Announce Type: cross 
Abstract: Reinforcement Learning (RL) robot controllers usually aggregate many task objectives into one scalar reward. While large-scale proximal policy optimisation (PPO) has enabled impressive results such as robust robot locomotion in the real world, many tasks still require careful reward tuning and are brittle to local optima. Tuning cost and sub-optimality grow with the number of objectives, limiting scalability. Modelling reward vectors and their trade-offs can address these issues; however, multi-objective methods remain underused in RL for robotics because of computational cost and optimisation difficulty. In this work, we investigate the conflict between gradient contributions for each objective that emerge from scalarising the task objectives. In particular, we explicitly address the conflict between task-based rewards and terms that regularise the policy towards realistic behaviour. We propose GCR-PPO, a modification to actor-critic optimisation that decomposes the actor update into objective-wise gradients using a multi-headed critic and resolves conflicts based on the objective priority. Our methodology, GCR-PPO, is evaluated on the well-known IsaacLab manipulation and locomotion benchmarks and additional multi-objective modifications on two related tasks. We show superior scalability compared to parallel PPO (p = 0.04), without significant computational overhead. We also show higher performance with more conflicting tasks. GCR-PPO improves on large-scale PPO with an average improvement of 9.5%, with high-conflict tasks observing a greater improvement. The code is available at https://github.com/humphreymunn/GCR-PPO.

## 🔍 Abstract (한글 번역)

arXiv:2509.14816v1 발표 유형: 교차  
초록: 강화 학습(RL) 로봇 제어기는 일반적으로 여러 작업 목표를 하나의 스칼라 보상으로 집계합니다. 대규모 근접 정책 최적화(PPO)는 실제 환경에서의 강력한 로봇 보행과 같은 인상적인 결과를 가능하게 했지만, 많은 작업은 여전히 신중한 보상 조정이 필요하며 국소 최적점에 취약합니다. 목표의 수가 증가함에 따라 조정 비용과 비최적성이 증가하여 확장성이 제한됩니다. 보상 벡터와 그 상충 관계를 모델링하면 이러한 문제를 해결할 수 있지만, 다목적 방법은 계산 비용과 최적화의 어려움 때문에 로봇 공학의 RL에서 여전히 잘 사용되지 않습니다. 본 연구에서는 작업 목표를 스칼라화할 때 발생하는 각 목표에 대한 그래디언트 기여 간의 충돌을 조사합니다. 특히, 우리는 현실적인 행동을 향한 정책을 정규화하는 항목과 작업 기반 보상 간의 충돌을 명시적으로 다룹니다. 우리는 다중 헤드 비평가를 사용하여 목표별 그래디언트로 배우 업데이트를 분해하고 목표 우선순위에 따라 충돌을 해결하는 배우-비평가 최적화의 수정 버전인 GCR-PPO를 제안합니다. 우리의 방법론인 GCR-PPO는 잘 알려진 IsaacLab 조작 및 보행 벤치마크와 두 가지 관련 작업에 대한 추가 다목적 수정에서 평가됩니다. 우리는 병렬 PPO와 비교하여 유의미한 계산 오버헤드 없이 우수한 확장성을 보여줍니다(p = 0.04). 또한, 더 많은 상충되는 작업에서 더 높은 성능을 보여줍니다. GCR-PPO는 대규모 PPO에서 평균 9.5%의 개선을 보여주며, 높은 갈등 작업에서는 더 큰 개선을 관찰할 수 있습니다. 코드는 https://github.com/humphreymunn/GCR-PPO에서 사용할 수 있습니다.

## 📝 요약

이 논문은 강화 학습(RL) 로봇 제어에서 다중 목표를 단일 스칼라 보상으로 집계하는 기존 방법의 한계를 해결하고자 합니다. 저자들은 목표별 기울기 충돌 문제를 다루기 위해 GCR-PPO라는 방법론을 제안했습니다. 이 방법은 다중 헤드 비평가를 사용하여 목표별 기울기를 분해하고, 목표 우선순위에 따라 충돌을 해결합니다. GCR-PPO는 IsaacLab 조작 및 이동 벤치마크에서 평가되었으며, 기존의 PPO 대비 확장성이 뛰어나고, 충돌이 많은 작업에서 평균 9.5%의 성능 향상을 보였습니다. 이 연구는 RL에서 다중 목표 방법론의 활용 가능성을 높이며, 코드도 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 강화 학습 로봇 제어기는 여러 과제 목표를 하나의 스칼라 보상으로 집계하지만, 보상 튜닝이 필요하고 지역 최적점에 민감하다.

- 2. 다중 목표 방법은 계산 비용과 최적화의 어려움 때문에 로봇 공학에서 잘 활용되지 않는다.

- 3. GCR-PPO는 목표별 그래디언트를 사용하여 행위자 업데이트를 분해하고 목표 우선순위에 따라 갈등을 해결한다.

- 4. GCR-PPO는 IsaacLab 벤치마크에서 기존 PPO보다 9.5%의 평균 성능 향상을 보이며, 특히 갈등이 많은 작업에서 더 큰 개선을 보인다.

- 5. GCR-PPO는 병렬 PPO보다 더 나은 확장성을 제공하며, 추가적인 계산 부담 없이 더 높은 성능을 달성한다.

---

*Generated on 2025-09-19 15:36:09*