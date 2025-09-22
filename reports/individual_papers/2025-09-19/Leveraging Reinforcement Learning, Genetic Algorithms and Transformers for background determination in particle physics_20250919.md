
# Leveraging Reinforcement Learning, Genetic Algorithms and Transformers for background determination in particle physics

**Korean Title:** 강화 학습, 유전 알고리즘 및 트랜스포머를 활용한 입자 물리학에서의 배경 결정

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Sparse Rewards

## 🔗 유사한 논문
- [[Reinforcement_Learning_Agent_for_a_2D_Shooter_Game_20250919|Reinforcement Learning Agent for a 2D Shooter Game]] (79.9% similar)
- [[Hybrid_Diffusion_Policies_with_Projective_Geometric_Algebra_for_Efficient_Robot_Manipulation_Learning_20250918|Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning]] (79.5% similar)
- [[Generalizable_Geometric_Image_Caption_Synthesis_20250919|Generalizable Geometric Image Caption Synthesis]] (79.3% similar)
- [[Multi-Fidelity_Hybrid_Reinforcement_Learning_via_Information_Gain_Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (79.1% similar)
- [[Online_reinforcement_learning_via_sparse_Gaussian_mixture_model_Q-functions_20250919|Online reinforcement learning via sparse Gaussian mixture model Q-functions]] (78.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14894v1 Announce Type: new 
Abstract: Experimental studies of beauty hadron decays face significant challenges due to a wide range of backgrounds arising from the numerous possible decay channels with similar final states. For a particular signal decay, the process for ascertaining the most relevant background processes necessitates a detailed analysis of final state particles, potential misidentifications, and kinematic overlaps, which, due to computational limitations, is restricted to the simulation of only the most relevant backgrounds. Moreover, this process typically relies on the physicist's intuition and expertise, as no systematic method exists.
  This paper has two primary goals. First, from a particle physics perspective, we present a novel approach that utilises Reinforcement Learning (RL) to overcome the aforementioned challenges by systematically determining the critical backgrounds affecting beauty hadron decay measurements. While beauty hadron physics serves as the case study in this work, the proposed strategy is broadly adaptable to other types of particle physics measurements. Second, from a Machine Learning perspective, we introduce a novel algorithm which exploits the synergy between RL and Genetic Algorithms (GAs) for environments with highly sparse rewards and a large trajectory space. This strategy leverages GAs to efficiently explore the trajectory space and identify successful trajectories, which are used to guide the RL agent's training. Our method also incorporates a transformer architecture for the RL agent to handle token sequences representing decays.

## 🔍 Abstract (한글 번역)

arXiv:2509.14894v1 발표 유형: 신규  
초록: 아름다움 하드론 붕괴의 실험적 연구는 유사한 최종 상태를 가진 다양한 붕괴 경로로 인해 발생하는 광범위한 배경으로 인해 상당한 도전에 직면합니다. 특정 신호 붕괴에 대해 가장 관련성이 높은 배경 과정을 확인하기 위한 과정은 최종 상태 입자, 잠재적 오식별, 운동학적 중첩에 대한 세부 분석을 필요로 하며, 이는 계산상의 제한으로 인해 가장 관련성이 높은 배경의 시뮬레이션으로 제한됩니다. 더욱이, 이 과정은 체계적인 방법이 존재하지 않기 때문에 일반적으로 물리학자의 직관과 전문성에 의존합니다.  
이 논문은 두 가지 주요 목표를 가지고 있습니다. 첫째, 입자 물리학 관점에서 우리는 강화 학습(RL)을 활용하여 아름다움 하드론 붕괴 측정에 영향을 미치는 중요한 배경을 체계적으로 결정함으로써 앞서 언급한 도전을 극복하는 새로운 접근 방식을 제시합니다. 아름다움 하드론 물리학이 이 연구의 사례 연구로 사용되지만, 제안된 전략은 다른 유형의 입자 물리학 측정에도 널리 적용 가능합니다. 둘째, 기계 학습 관점에서 우리는 보상이 매우 희소하고 궤적 공간이 큰 환경에서 RL과 유전 알고리즘(GA)의 시너지를 활용하는 새로운 알고리즘을 소개합니다. 이 전략은 GA를 활용하여 궤적 공간을 효율적으로 탐색하고 성공적인 궤적을 식별하며, 이는 RL 에이전트의 훈련을 안내하는 데 사용됩니다. 우리의 방법은 또한 RL 에이전트가 붕괴를 나타내는 토큰 시퀀스를 처리할 수 있도록 트랜스포머 아키텍처를 통합합니다.

## 📝 요약

이 논문은 아름다운 하드론 붕괴의 실험적 연구에서 발생하는 다양한 배경 문제를 해결하기 위해 강화 학습(RL)과 유전 알고리즘(GA)을 결합한 새로운 접근법을 제안합니다. 이 방법은 배경 과정의 체계적 식별을 통해 붕괴 측정의 정확성을 높이며, 다른 입자 물리학 측정에도 적용 가능합니다. 또한, GA를 활용해 넓은 경로 공간을 탐색하고, 성공적인 경로를 RL 에이전트의 학습에 활용합니다. RL 에이전트는 변환기 아키텍처를 사용하여 붕괴를 나타내는 토큰 시퀀스를 처리합니다.

## 🎯 주요 포인트

- 1. 미용 하드론 붕괴 실험 연구는 유사한 최종 상태를 가진 다양한 붕괴 채널로 인한 광범위한 배경 때문에 어려움을 겪고 있습니다.

- 2. 본 논문은 강화 학습(RL)을 활용하여 미용 하드론 붕괴 측정에 영향을 미치는 중요한 배경을 체계적으로 결정하는 새로운 접근법을 제시합니다.

- 3. 제안된 전략은 미용 하드론 물리학에 국한되지 않고 다른 입자 물리학 측정에도 널리 적용 가능합니다.

- 4. 강화 학습과 유전 알고리즘(GA)의 시너지를 활용하여 보상이 매우 희소하고 경로 공간이 큰 환경에서 성공적인 경로를 식별하는 새로운 알고리즘을 소개합니다.

- 5. RL 에이전트의 훈련을 위해 변환기 아키텍처를 도입하여 붕괴를 나타내는 토큰 시퀀스를 처리합니다.

---

*Generated on 2025-09-19 15:27:55*