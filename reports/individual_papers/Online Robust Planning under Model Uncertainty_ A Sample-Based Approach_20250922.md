# Online Robust Planning under Model Uncertainty: A Sample-Based Approach

**Korean Title:** 모형 불확실성 하에서의 온라인 강건 계획: 샘플 기반 접근법

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Robust MDPs

## 🔗 유사한 논문
- [[2025-09-19/Online reinforcement learning via sparse Gaussian mixture model Q-functions_20250919|Online reinforcement learning via sparse Gaussian mixture model Q-functions]] (81.6% similar)
- [[2025-09-19/ActivePusher_ Active Learning and Planning with Residual Physics for Nonprehensile Manipulation_20250919|ActivePusher Active Learning and Planning with Residual Physics for Nonprehensile Manipulation]] (81.2% similar)
- [[2025-09-19/Optimal Control of Markov Decision Processes for Efficiency with Linear Temporal Logic Tasks_20250919|Optimal Control of Markov Decision Processes for Efficiency with Linear Temporal Logic Tasks]] (81.0% similar)
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (80.7% similar)
- [[2025-09-19/Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (80.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.10162v2 Announce Type: replace 
Abstract: Online planning in Markov Decision Processes (MDPs) enables agents to make sequential decisions by simulating future trajectories from the current state, making it well-suited for large-scale or dynamic environments. Sample-based methods such as Sparse Sampling and Monte Carlo Tree Search (MCTS) are widely adopted for their ability to approximate optimal actions using a generative model. However, in practical settings, the generative model is often learned from limited data, introducing approximation errors that can degrade performance or lead to unsafe behaviors. To address these challenges, Robust MDPs (RMDPs) offer a principled framework for planning under model uncertainty, yet existing approaches are typically computationally intensive and not suited for real-time use. In this work, we introduce Robust Sparse Sampling (RSS), the first online planning algorithm for RMDPs with finite-sample theoretical performance guarantees. Unlike Sparse Sampling, which estimates the nominal value function, RSS computes a robust value function by leveraging the efficiency and theoretical properties of Sample Average Approximation (SAA), enabling tractable robust policy computation in online settings. RSS is applicable to infinite or continuous state spaces, and its sample and computational complexities are independent of the state space size. We provide theoretical performance guarantees and empirically show that RSS outperforms standard Sparse Sampling in environments with uncertain dynamics.

## 🔍 Abstract (한글 번역)

arXiv:2509.10162v2 발표 유형: 교체  
초록: 마르코프 결정 프로세스(MDP)에서의 온라인 계획은 에이전트가 현재 상태에서 미래 경로를 시뮬레이션하여 순차적인 결정을 내릴 수 있게 하며, 대규모 또는 동적인 환경에 적합합니다. Sparse Sampling 및 몬테카를로 트리 탐색(MCTS)과 같은 샘플 기반 방법은 생성 모델을 사용하여 최적의 행동을 근사할 수 있는 능력으로 널리 채택되고 있습니다. 그러나 실제 환경에서는 생성 모델이 제한된 데이터로부터 학습되는 경우가 많아 근사 오류가 발생하여 성능 저하 또는 안전하지 않은 행동을 초래할 수 있습니다. 이러한 문제를 해결하기 위해, 강건한 MDP(RMDP)는 모델 불확실성 하에서 계획을 세우기 위한 원칙적인 프레임워크를 제공합니다. 그러나 기존 접근법은 일반적으로 계산 집약적이며 실시간 사용에 적합하지 않습니다. 본 연구에서는 유한 샘플 이론적 성능 보장을 갖춘 RMDP를 위한 최초의 온라인 계획 알고리즘인 Robust Sparse Sampling(RSS)을 소개합니다. RSS는 명목적 가치 함수를 추정하는 Sparse Sampling과 달리, 샘플 평균 근사(SAA)의 효율성과 이론적 특성을 활용하여 강건한 가치 함수를 계산함으로써 온라인 환경에서 실행 가능한 강건한 정책 계산을 가능하게 합니다. RSS는 무한 또는 연속 상태 공간에 적용 가능하며, 샘플 및 계산 복잡도는 상태 공간 크기와 독립적입니다. 우리는 이론적 성능 보장을 제공하고, 불확실한 동적 환경에서 RSS가 표준 Sparse Sampling보다 뛰어난 성능을 보임을 실증적으로 보여줍니다.

## 📝 요약

이 논문은 마르코프 결정 프로세스(MDP)에서의 온라인 계획을 위한 새로운 알고리즘인 Robust Sparse Sampling(RSS)을 제안합니다. 기존의 샘플 기반 방법은 제한된 데이터로 학습된 생성 모델로 인해 성능 저하와 안전 문제를 겪을 수 있습니다. 이를 해결하기 위해, RSS는 모델 불확실성 하에서의 계획을 위한 강건한 MDP(RMDP) 프레임워크를 활용하며, 샘플 평균 근사(SAA)의 효율성과 이론적 특성을 활용하여 강건한 가치 함수를 계산합니다. RSS는 무한 또는 연속 상태 공간에 적용 가능하며, 상태 공간 크기에 독립적인 샘플 및 계산 복잡성을 가집니다. 이론적 성능 보장을 제공하며, 불확실한 동적 환경에서 표준 Sparse Sampling보다 우수한 성능을 보입니다.

## 🎯 주요 포인트

- 1. 마르코프 결정 과정(MDP)에서 온라인 계획은 현재 상태에서 미래 경로를 시뮬레이션하여 순차적인 결정을 내리도록 돕는다.

- 2. 샘플 기반 방법인 Sparse Sampling과 몬테카를로 트리 탐색(MCTS)은 생성 모델을 사용하여 최적의 행동을 근사하는 데 널리 사용된다.

- 3. 실제 환경에서 생성 모델은 제한된 데이터로부터 학습되므로 근사 오류가 발생할 수 있으며, 이는 성능 저하나 안전하지 않은 행동으로 이어질 수 있다.

- 4. Robust MDPs(RMDPs)는 모델 불확실성 하에서 계획을 세우기 위한 체계적인 프레임워크를 제공하지만, 기존 접근법은 계산 비용이 높아 실시간 사용에 적합하지 않다.

- 5. Robust Sparse Sampling(RSS)은 RMDPs에 대한 최초의 온라인 계획 알고리즘으로, 유한 샘플 이론적 성능 보장을 제공하며, 불확실한 동적 환경에서 표준 Sparse Sampling보다 뛰어난 성능을 보인다.

---

*Generated on 2025-09-22 14:34:26*