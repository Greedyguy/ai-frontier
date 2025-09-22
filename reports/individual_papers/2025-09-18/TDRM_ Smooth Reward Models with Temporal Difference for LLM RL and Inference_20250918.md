# TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference

**Korean Title:** TDRM: LLM 강화 학습 및 추론을 위한 시간 차이 기반의 부드러운 보상 모델

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Dan Zhang|Dan Zhang]] [[authors/Min Cai|Min Cai]] [[authors/Jonathan Li|Jonathan Li]] [[authors/Ziniu Hu|Ziniu Hu]] [[authors/Yisong Yue|Yisong Yue]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Temporal Difference Regularization

## 🔗 유사한 논문
- [[Zero-Shot LLMs in Human-in-the-Loop RL_ Replacing Human Feedback for Reward Shaping_20250919|Zero-Shot LLMs in Human-in-the-Loop RL Replacing Human Feedback for Reward Shaping]] (85.2% similar)
- [[Evolving Language Models without Labels_ Majority Drives Selection, Novelty Promotes Variation_20250918|Evolving Language Models without Labels Majority Drives Selection, Novelty Promotes Variation]] (84.8% similar)
- [[Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents_20250919|Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents]] (83.6% similar)
- [[FlowRL_ Matching Reward Distributions for LLM Reasoning_20250919|FlowRL Matching Reward Distributions for LLM Reasoning]] (83.6% similar)
- [[TGPO_ Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning_20250917|TGPO Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning]] (82.5% similar)

## 📋 저자 정보

**Authors:** Dan Zhang, Min Cai, Jonathan Li, Ziniu Hu, Yisong Yue, Yuxiao Dong, Jie Tang

## 📄 Abstract (원문)

Reward models are central to both reinforcement learning (RL) with language
models and inference-time verification. However, existing reward models often
lack temporal consistency, leading to ineffective policy updates and unstable
RL training. We introduce TDRM, a method for learning smoother and more
reliable reward models by minimizing temporal differences during training. This
temporal-difference (TD) regularization produces smooth rewards and improves
alignment with long-term objectives. Incorporating TDRM into the actor-critic
style online RL loop yields consistent empirical gains. It is worth noting that
TDRM is a supplement to verifiable reward methods, and both can be used in
series. Experiments show that TD-trained process reward models (PRMs) improve
performance across Best-of-N (up to 6.6%) and tree-search (up to 23.7%)
settings. When combined with Reinforcement Learning with Verifiable Rewards
(RLVR), TD-trained PRMs lead to more data-efficient RL -- achieving comparable
performance with just 2.5k data to what baseline methods require 50.1k data to
attain -- and yield higher-quality language model policies on 8 model variants
(5 series), e.g., Qwen2.5-(0.5B, 1,5B), GLM4-9B-0414, GLM-Z1-9B-0414,
Qwen2.5-Math-(1.5B, 7B), and DeepSeek-R1-Distill-Qwen-(1.5B, 7B). We release
all code at https://github.com/THUDM/TDRM.

## 🔍 Abstract (한글 번역)

보상 모델은 언어 모델과 추론 시 검증을 포함한 강화 학습(RL)의 중심 요소입니다. 그러나 기존의 보상 모델은 종종 시간적 일관성이 부족하여 비효율적인 정책 업데이트와 불안정한 RL 훈련을 초래합니다. 우리는 훈련 중 시간 차이를 최소화하여 더 부드럽고 신뢰할 수 있는 보상 모델을 학습하는 방법인 TDRM을 소개합니다. 이 시간 차이(TD) 정규화는 부드러운 보상을 생성하고 장기 목표와의 정렬을 개선합니다. TDRM을 액터-크리틱 스타일의 온라인 RL 루프에 통합하면 일관된 경험적 이득을 얻을 수 있습니다. TDRM은 검증 가능한 보상 방법의 보조 수단이며, 두 방법 모두 연속적으로 사용할 수 있음을 주목할 가치가 있습니다. 실험 결과, TD로 훈련된 프로세스 보상 모델(PRM)은 Best-of-N(최대 6.6%) 및 트리 탐색(최대 23.7%) 설정에서 성능을 향상시킵니다. 검증 가능한 보상과 함께하는 강화 학습(RLVR)과 결합할 경우, TD로 훈련된 PRM은 데이터 효율적인 RL을 가능하게 하여, 기준 방법이 50.1k 데이터가 필요로 하는 성능을 단지 2.5k 데이터로 달성할 수 있으며, 8개의 모델 변형(5개의 시리즈)에서 더 높은 품질의 언어 모델 정책을 제공합니다. 예를 들어, Qwen2.5-(0.5B, 1.5B), GLM4-9B-0414, GLM-Z1-9B-0414, Qwen2.5-Math-(1.5B, 7B), DeepSeek-R1-Distill-Qwen-(1.5B, 7B) 등이 있습니다. 모든 코드는 https://github.com/THUDM/TDRM에서 공개됩니다.

## 📝 요약

이 논문은 강화 학습(RL)에서 보상 모델의 시간적 일관성 부족 문제를 해결하기 위해 TDRM이라는 방법을 제안합니다. TDRM은 학습 중 시간 차이를 최소화하여 더 부드럽고 신뢰성 있는 보상 모델을 학습하며, 장기 목표와의 정렬을 개선합니다. 이 방법을 온라인 RL 루프에 적용하면 일관된 성능 향상이 나타납니다. 실험 결과, TDRM을 통해 학습된 보상 모델은 Best-of-N 및 트리 검색 설정에서 각각 최대 6.6%와 23.7%의 성능 향상을 보였습니다. 또한, TDRM은 검증 가능한 보상 방법과 결합하여 데이터 효율성을 높이고, 다양한 언어 모델에서 더 높은 품질의 정책을 생성합니다. 모든 코드는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. TDRM은 강화 학습에서 시간적 차이를 최소화하여 더 부드럽고 신뢰할 수 있는 보상 모델을 학습하는 방법입니다.

- 2. TDRM을 활용하면 장기 목표와의 정렬이 개선되고, 강화 학습의 불안정성을 줄일 수 있습니다.

- 3. TDRM은 검증 가능한 보상 방법을 보완하며, 두 방법을 연속적으로 사용할 수 있습니다.

- 4. 실험 결과, TDRM을 적용한 보상 모델은 Best-of-N 및 트리 탐색 설정에서 성능을 각각 최대 6.6% 및 23.7% 향상시킵니다.

- 5. TDRM과 RLVR을 결합하면 데이터 효율성이 높아져, 2.5k 데이터만으로도 기존 방법이 50.1k 데이터를 필요로 하는 성능을 달성할 수 있습니다.

---

*Generated on 2025-09-20 01:01:16*