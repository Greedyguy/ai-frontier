
# FlowRL: Matching Reward Distributions for LLM Reasoning

**Korean Title:** FlowRL: LLM 추론을 위한 보상 분포 매칭

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Reward Distribution Matching, Flow Balancing

## 🔗 유사한 논문
- [[THOR Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning]] (81.0% similar)
- [[MAgICoRe Multi-Agent, Iterative, Coarse-to-Fine Refinement for Reasoning]] (80.9% similar)
- [[Video-Language Critic Transferable Reward Functions for Language-Conditioned Robotics]] (80.3% similar)
- [[Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (79.7% similar)
- [[Generalizable_Geometric_Image_Caption_Synthesis_20250919|Generalizable Geometric Image Caption Synthesis]] (79.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15207v1 Announce Type: cross 
Abstract: We propose FlowRL: matching the full reward distribution via flow balancing instead of maximizing rewards in large language model (LLM) reinforcement learning (RL). Recent advanced reasoning models adopt reward-maximizing methods (\eg, PPO and GRPO), which tend to over-optimize dominant reward signals while neglecting less frequent but valid reasoning paths, thus reducing diversity. In contrast, we transform scalar rewards into a normalized target distribution using a learnable partition function, and then minimize the reverse KL divergence between the policy and the target distribution. We implement this idea as a flow-balanced optimization method that promotes diverse exploration and generalizable reasoning trajectories. We conduct experiments on math and code reasoning tasks: FlowRL achieves a significant average improvement of $10.0\%$ over GRPO and $5.1\%$ over PPO on math benchmarks, and performs consistently better on code reasoning tasks. These results highlight reward distribution-matching as a key step toward efficient exploration and diverse reasoning in LLM reinforcement learning.

## 🔍 Abstract (한글 번역)

arXiv:2509.15207v1 발표 유형: 교차  
초록: 우리는 대규모 언어 모델(LLM) 강화 학습(RL)에서 보상을 최대화하는 대신 흐름 균형을 통해 전체 보상 분포를 매칭하는 FlowRL을 제안합니다. 최근의 고급 추론 모델은 보상 최대화 방법(예: PPO 및 GRPO)을 채택하여 지배적인 보상 신호를 과도하게 최적화하는 경향이 있으며, 이로 인해 덜 빈번하지만 유효한 추론 경로를 무시하여 다양성이 감소합니다. 이에 반해, 우리는 스칼라 보상을 학습 가능한 분할 함수를 사용하여 정규화된 목표 분포로 변환한 후, 정책과 목표 분포 간의 역 KL 발산을 최소화합니다. 우리는 이 아이디어를 다양한 탐색과 일반화 가능한 추론 경로를 촉진하는 흐름 균형 최적화 방법으로 구현합니다. 수학 및 코드 추론 작업에 대한 실험을 수행한 결과, FlowRL은 수학 벤치마크에서 GRPO보다 평균적으로 10.0% 개선, PPO보다 5.1% 개선을 달성했으며, 코드 추론 작업에서도 일관되게 더 나은 성능을 보였습니다. 이러한 결과는 LLM 강화 학습에서 효율적인 탐색과 다양한 추론을 위한 핵심 단계로서 보상 분포 매칭의 중요성을 강조합니다.

## 📝 요약

FlowRL은 대형 언어 모델 강화 학습에서 보상 최대화 대신 보상 분포를 흐름 균형을 통해 매칭하는 방법을 제안합니다. 기존 모델들은 주로 보상 최대화 방법을 사용하여 지배적인 보상 신호에 과도하게 최적화되지만, 이는 다양한 추론 경로를 간과할 수 있습니다. FlowRL은 스칼라 보상을 정규화된 목표 분포로 변환하고, 정책과 목표 분포 간의 역 KL 발산을 최소화합니다. 이를 통해 다양한 탐색과 일반화 가능한 추론 경로를 촉진합니다. 수학 및 코드 추론 작업 실험에서 FlowRL은 GRPO 대비 평균 10.0%, PPO 대비 5.1% 향상을 보였으며, 코드 추론 작업에서도 일관되게 우수한 성능을 나타냈습니다. 이는 보상 분포 매칭이 효율적인 탐색과 다양한 추론을 위한 핵심 단계임을 강조합니다.

## 🎯 주요 포인트

- 1. FlowRL은 대규모 언어 모델 강화 학습에서 보상 최대화 대신 흐름 균형을 통해 전체 보상 분포를 매칭하는 방법을 제안합니다.

- 2. 기존의 보상 최대화 방법들은 지배적인 보상 신호를 과도하게 최적화하여 다양한 추론 경로를 간과하는 경향이 있습니다.

- 3. FlowRL은 스칼라 보상을 정규화된 목표 분포로 변환하고, 정책과 목표 분포 간의 역 KL 발산을 최소화하는 흐름 균형 최적화 방법을 구현합니다.

- 4. 수학 및 코드 추론 작업에서 FlowRL은 GRPO 대비 평균 10.0%, PPO 대비 5.1%의 성능 향상을 보였으며, 코드 추론 작업에서도 일관되게 더 나은 성능을 발휘했습니다.

- 5. 이러한 결과는 보상 분포 매칭이 LLM 강화 학습에서 효율적인 탐색과 다양한 추론을 위한 핵심 단계임을 강조합니다.

---

*Generated on 2025-09-19 15:08:18*