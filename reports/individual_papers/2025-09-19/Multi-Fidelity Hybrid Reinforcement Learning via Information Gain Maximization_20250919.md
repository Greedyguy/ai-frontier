---
keywords:
  - Reinforcement Learning
  - Multi-Fidelity Hybrid Reinforcement Learning
  - Information Gain Maximization
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14848
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:33:02.305874",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Multi-Fidelity Hybrid Reinforcement Learning",
    "Information Gain Maximization"
  ],
  "rejected_keywords": [
    "Offline Reinforcement Learning"
  ],
  "similarity_scores": {
    "Reinforcement Learning": 0.95,
    "Multi-Fidelity Hybrid Reinforcement Learning": 0.85,
    "Information Gain Maximization": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization

**Korean Title:** 정보 이득 극대화를 통한 다중 신뢰도 하이브리드 강화 학습

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Multi-Fidelity Hybrid Reinforcement Learning|Multi-Fidelity Hybrid Reinforcement Learning]], [[keywords/Information Gain Maximization|Information Gain Maximization]]

## 🔗 유사한 논문
- [[Online_reinforcement_learning_via_sparse_Gaussian_mixture_model_Q-functions_20250919|Online reinforcement learning via sparse Gaussian mixture model Q-functions]] (86.4% similar)
- [[Mining the Long Tail A Comparative Study of Data-Centric Criticality Metrics for Robust Offline Reinforcement Learning in Autonomous Motion Planning]] (84.6% similar)
- [[Reinforcement_Learning_Agent_for_a_2D_Shooter_Game_20250919|Reinforcement Learning Agent for a 2D Shooter Game]] (84.4% similar)
- [[Zero-Shot LLMs in Human-in-the-Loop RL Replacing Human Feedback for Reward Shaping]] (82.8% similar)
- [[Hybrid_Diffusion_Policies_with_Projective_Geometric_Algebra_for_Efficient_Robot_Manipulation_Learning_20250918|Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning]] (81.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14848v1 Announce Type: new 
Abstract: Optimizing a reinforcement learning (RL) policy typically requires extensive interactions with a high-fidelity simulator of the environment, which are often costly or impractical. Offline RL addresses this problem by allowing training from pre-collected data, but its effectiveness is strongly constrained by the size and quality of the dataset. Hybrid offline-online RL leverages both offline data and interactions with a single simulator of the environment. In many real-world scenarios, however, multiple simulators with varying levels of fidelity and computational cost are available. In this work, we study multi-fidelity hybrid RL for policy optimization under a fixed cost budget. We introduce multi-fidelity hybrid RL via information gain maximization (MF-HRL-IGM), a hybrid offline-online RL algorithm that implements fidelity selection based on information gain maximization through a bootstrapping approach. Theoretical analysis establishes the no-regret property of MF-HRL-IGM, while empirical evaluations demonstrate its superior performance compared to existing benchmarks.

## 🔍 Abstract (한글 번역)

arXiv:2509.14848v1 발표 유형: 신규  
초록: 강화 학습(RL) 정책을 최적화하려면 일반적으로 환경의 고충실도 시뮬레이터와의 광범위한 상호작용이 필요하며, 이는 종종 비용이 많이 들거나 비현실적입니다. 오프라인 RL은 사전 수집된 데이터를 통해 학습을 허용함으로써 이 문제를 해결하지만, 그 효과는 데이터셋의 크기와 품질에 의해 크게 제한됩니다. 하이브리드 오프라인-온라인 RL은 오프라인 데이터와 환경의 단일 시뮬레이터와의 상호작용을 활용합니다. 그러나 많은 실제 시나리오에서는 다양한 수준의 충실도와 계산 비용을 가진 여러 시뮬레이터가 사용 가능합니다. 본 연구에서는 고정 비용 예산 하에서 정책 최적화를 위한 다중 충실도 하이브리드 RL을 연구합니다. 우리는 부트스트래핑 접근 방식을 통해 정보 이득 극대화에 기반한 충실도 선택을 구현하는 하이브리드 오프라인-온라인 RL 알고리즘인 정보 이득 극대화를 통한 다중 충실도 하이브리드 RL(MF-HRL-IGM)을 소개합니다. 이론적 분석은 MF-HRL-IGM의 무후회(no-regret) 특성을 확립하며, 실증적 평가에서는 기존 벤치마크와 비교하여 우수한 성능을 보여줍니다.

## 📝 요약

이 논문은 다양한 수준의 시뮬레이터를 활용하여 정책 최적화를 수행하는 다중-정확도 하이브리드 강화 학습(MF-HRL)을 제안합니다. 기존의 오프라인 RL은 데이터의 크기와 품질에 의해 제한되지만, 이 연구는 정보 이득 극대화를 통해 시뮬레이터의 정확도를 선택하는 MF-HRL-IGM 알고리즘을 개발했습니다. 이 알고리즘은 부트스트래핑 접근 방식을 사용하며, 이론적 분석을 통해 후회가 없음을 증명했습니다. 실험 결과, MF-HRL-IGM은 기존 벤치마크보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 강화 학습 정책 최적화는 고품질 시뮬레이터와의 상호작용이 필요하지만, 이는 비용이 많이 들거나 비현실적일 수 있습니다.

- 2. 오프라인 강화 학습은 사전 수집된 데이터를 활용하여 이러한 문제를 해결하지만, 데이터셋의 크기와 품질에 의해 효과가 제한됩니다.

- 3. 다중 충실도 하이브리드 강화 학습은 다양한 충실도와 계산 비용을 가진 여러 시뮬레이터를 활용하여 정책 최적화를 수행합니다.

- 4. MF-HRL-IGM 알고리즘은 정보 이득 최대화를 통해 충실도를 선택하는 부트스트래핑 접근법을 사용하여 하이브리드 오프라인-온라인 강화 학습을 구현합니다.

- 5. 이론적 분석을 통해 MF-HRL-IGM의 무후회 특성이 입증되었으며, 실험 결과 기존 벤치마크보다 우수한 성능을 보였습니다.

---

*Generated on 2025-09-19 15:27:33*