# Uncertainty-Based Smooth Policy Regularisation for Reinforcement Learning with Few Demonstrations

**Korean Title:** 불확실성 기반의 매끄러운 정책 정규화: 소수의 시연을 통한 강화 학습

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Uncertainty-Based Regularisation

## 🔗 유사한 논문
- [[2025-09-19/Online reinforcement learning via sparse Gaussian mixture model Q-functions_20250919|Online reinforcement learning via sparse Gaussian mixture model Q-functions]] (82.7% similar)
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (82.0% similar)
- [[2025-09-19/Sample Efficient Experience Replay in Non-stationary Environments_20250919|Sample Efficient Experience Replay in Non-stationary Environments]] (81.9% similar)
- [[2025-09-19/LEED_ A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning_20250919|LEED A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning]] (81.8% similar)
- [[2025-09-19/Online Learning of Deceptive Policies under Intermittent Observation_20250919|Online Learning of Deceptive Policies under Intermittent Observation]] (81.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15981v1 Announce Type: cross 
Abstract: In reinforcement learning with sparse rewards, demonstrations can accelerate learning, but determining when to imitate them remains challenging. We propose Smooth Policy Regularisation from Demonstrations (SPReD), a framework that addresses the fundamental question: when should an agent imitate a demonstration versus follow its own policy? SPReD uses ensemble methods to explicitly model Q-value distributions for both demonstration and policy actions, quantifying uncertainty for comparisons. We develop two complementary uncertainty-aware methods: a probabilistic approach estimating the likelihood of demonstration superiority, and an advantage-based approach scaling imitation by statistical significance. Unlike prevailing methods (e.g. Q-filter) that make binary imitation decisions, SPReD applies continuous, uncertainty-proportional regularisation weights, reducing gradient variance during training. Despite its computational simplicity, SPReD achieves remarkable gains in experiments across eight robotics tasks, outperforming existing approaches by up to a factor of 14 in complex tasks while maintaining robustness to demonstration quality and quantity. Our code is available at https://github.com/YujieZhu7/SPReD.

## 🔍 Abstract (한글 번역)

arXiv:2509.15981v1 발표 유형: 교차  
초록: 희소 보상을 사용하는 강화 학습에서 시범은 학습을 가속화할 수 있지만, 언제 이를 모방해야 하는지를 결정하는 것은 여전히 도전적입니다. 우리는 에이전트가 시범을 모방해야 할 때와 자신의 정책을 따라야 할 때를 결정하는 근본적인 질문을 해결하는 프레임워크인 시범으로부터의 부드러운 정책 정규화(SPReD)를 제안합니다. SPReD는 앙상블 방법을 사용하여 시범 및 정책 행동에 대한 Q-값 분포를 명시적으로 모델링하여 비교에 대한 불확실성을 정량화합니다. 우리는 두 가지 상호 보완적인 불확실성 인식 방법을 개발했습니다: 시범의 우월성 가능성을 추정하는 확률적 접근법과 통계적 유의성에 따라 모방을 조정하는 이점 기반 접근법. 이진 모방 결정을 내리는 기존 방법(예: Q-필터)과 달리, SPReD는 연속적이고 불확실성 비례 정규화 가중치를 적용하여 훈련 중 그래디언트 분산을 줄입니다. 계산의 단순함에도 불구하고, SPReD는 8개의 로봇 작업에서 기존 접근법을 최대 14배 능가하며 시범의 품질과 양에 대한 강건성을 유지하면서 놀라운 성과를 달성합니다. 우리의 코드는 https://github.com/YujieZhu7/SPReD에서 이용할 수 있습니다.

## 📝 요약

이 논문은 희소 보상 환경에서 강화 학습을 가속화하기 위해 제안된 SPReD(Smooth Policy Regularisation from Demonstrations)라는 프레임워크를 소개합니다. SPReD는 에이전트가 언제 시연을 모방하고 언제 자체 정책을 따를지 결정하는 문제를 해결합니다. 이를 위해 Q-value 분포를 모델링하여 시연과 정책 행동의 불확실성을 정량화하고, 시연의 우월성을 추정하는 확률적 접근과 통계적 유의성에 기반한 이점 기반 접근을 개발했습니다. 기존의 이진 모방 결정 방식과 달리, SPReD는 연속적이고 불확실성에 비례하는 정규화 가중치를 적용하여 훈련 중 그래디언트 분산을 줄입니다. SPReD는 8개의 로봇 과제 실험에서 기존 방법보다 최대 14배 뛰어난 성능을 보이며, 시연의 질과 양에 대한 강인성을 유지합니다.

## 🎯 주요 포인트

- 1. SPReD는 강화 학습에서 에이전트가 시연을 모방할 시점을 결정하는 문제를 해결하는 프레임워크입니다.

- 2. SPReD는 시연 및 정책 행동에 대한 Q-값 분포를 명시적으로 모델링하여 불확실성을 정량화합니다.

- 3. SPReD는 시연의 우월성을 추정하는 확률적 접근법과 통계적 유의성을 기반으로 모방을 조정하는 장점 기반 접근법을 개발하였습니다.

- 4. SPReD는 기존의 이진 모방 결정 방식과 달리 연속적이고 불확실성에 비례한 정규화 가중치를 적용하여 훈련 중 그래디언트 분산을 줄입니다.

- 5. SPReD는 8개의 로봇 과제 실험에서 최대 14배의 성능 향상을 달성하며 시연의 품질과 양에 대한 강건성을 유지합니다.

---

*Generated on 2025-09-22 14:20:55*