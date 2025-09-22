# PVPO: Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning

**Korean Title:** PVPO: 에이전트적 추론을 위한 사전 추정 가치 기반 정책 최적화

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Advantage Reference Anchor

## 🔗 유사한 논문
- [[2025-09-19/Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (86.3% similar)
- [[2025-09-19/PMPO_ Probabilistic Metric Prompt Optimization for Small and Large Language Models_20250919|PMPO Probabilistic Metric Prompt Optimization for Small and Large Language Models]] (83.6% similar)
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (83.3% similar)
- [[2025-09-22/Deep Reinforcement Learning with Gradient Eligibility Traces_20250922|Deep Reinforcement Learning with Gradient Eligibility Traces]] (83.3% similar)
- [[2025-09-22/A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning_20250922|A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning]] (82.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.21104v3 Announce Type: replace-cross 
Abstract: Critic-free reinforcement learning methods, particularly group policies, have attracted considerable attention for their efficiency in complex tasks. However, these methods rely heavily on multiple sampling and comparisons within the policy to estimate advantage, which may cause the policy to fall into local optimum and increase computational cost. To address these issues, we propose PVPO, an efficient reinforcement learning method enhanced by an advantage reference anchor and data pre-sampling. Specifically, we use the reference model to rollout in advance and employ the calculated reward score as a reference anchor. Our approach effectively corrects the cumulative bias introduced by intra-group comparisons and significantly reduces reliance on the number of rollouts during training. Meanwhile, the reference model can assess sample difficulty during data pre-sampling, enabling effective selection of high-gain data to improve training efficiency. Moreover, PVPO is orthogonal to other advanced critic-free RL algorithms, making it compatible with and complementary to these methods. Experiments conducted on nine datasets across two domains demonstrate that PVPO achieves State-Of-The-Art (SOTA) performance. Our approach not only demonstrates robust generalization across multiple tasks, but also exhibits scalable performance across models of varying scales.

## 🔍 Abstract (한글 번역)

arXiv:2508.21104v3 발표 유형: 교차 교체  
초록: 비평가 없는 강화 학습 방법, 특히 그룹 정책은 복잡한 작업에서의 효율성으로 인해 상당한 주목을 받고 있습니다. 그러나 이러한 방법은 정책 내에서 이점을 추정하기 위해 다중 샘플링과 비교에 크게 의존하며, 이는 정책이 지역 최적점에 빠지게 하고 계산 비용을 증가시킬 수 있습니다. 이러한 문제를 해결하기 위해, 우리는 이점 참조 앵커와 데이터 사전 샘플링으로 강화된 효율적인 강화 학습 방법인 PVPO를 제안합니다. 구체적으로, 우리는 참조 모델을 사용하여 사전에 롤아웃을 수행하고 계산된 보상 점수를 참조 앵커로 사용합니다. 우리의 접근 방식은 그룹 내 비교로 인해 발생하는 누적 편향을 효과적으로 수정하고, 훈련 중 롤아웃 수에 대한 의존도를 크게 줄입니다. 동시에, 참조 모델은 데이터 사전 샘플링 중 샘플 난이도를 평가할 수 있어, 훈련 효율성을 향상시키기 위한 고수익 데이터의 효과적인 선택을 가능하게 합니다. 더욱이, PVPO는 다른 고급 비평가 없는 RL 알고리즘과 직교하여, 이러한 방법들과 호환되고 상호 보완적입니다. 두 개의 도메인에 걸쳐 아홉 개의 데이터셋에서 수행된 실험은 PVPO가 최첨단(SOTA) 성능을 달성함을 보여줍니다. 우리의 접근 방식은 여러 작업에서 강력한 일반화를 보여줄 뿐만 아니라, 다양한 규모의 모델에서 확장 가능한 성능을 나타냅니다.

## 📝 요약

이 논문은 복잡한 작업에서 효율성을 보이는 비평가 기반 강화 학습 방법의 문제점을 해결하기 위해 PVPO라는 새로운 방법을 제안합니다. 기존 방법은 정책 내 다중 샘플링과 비교에 의존하여 지역 최적화에 빠지거나 계산 비용이 증가할 수 있습니다. PVPO는 이 문제를 해결하기 위해 이점 참조 앵커와 데이터 사전 샘플링을 활용합니다. 참조 모델을 사용하여 사전 롤아웃을 수행하고, 계산된 보상 점수를 참조 앵커로 사용하여 그룹 내 비교로 인한 누적 편향을 효과적으로 수정합니다. 또한, 데이터 사전 샘플링 단계에서 샘플의 난이도를 평가하여 고수익 데이터를 선택함으로써 훈련 효율성을 높입니다. PVPO는 다른 비평가 기반 강화 학습 알고리즘과 호환 가능하며, 실험 결과 9개의 데이터셋에서 최첨단 성능을 달성했습니다. 이 방법은 다양한 작업에서 강력한 일반화 능력을 보여주며, 다양한 규모의 모델에서 확장 가능한 성능을 나타냅니다.

## 🎯 주요 포인트

- 1. PVPO는 이점 참조 앵커와 데이터 사전 샘플링을 통해 강화 학습의 효율성을 향상시킵니다.

- 2. 참조 모델을 사용하여 사전 롤아웃을 수행하고 계산된 보상 점수를 참조 앵커로 활용합니다.

- 3. PVPO는 그룹 내 비교로 인한 누적 편향을 효과적으로 수정하고 훈련 중 롤아웃 수에 대한 의존도를 크게 줄입니다.

- 4. 데이터 사전 샘플링 중 샘플의 난이도를 평가하여 고수익 데이터를 선택함으로써 훈련 효율성을 높입니다.

- 5. PVPO는 다른 고급 비평가 없는 강화 학습 알고리즘과 호환 가능하며, 9개의 데이터셋에서 SOTA 성능을 달성했습니다.

---

*Generated on 2025-09-22 14:59:33*