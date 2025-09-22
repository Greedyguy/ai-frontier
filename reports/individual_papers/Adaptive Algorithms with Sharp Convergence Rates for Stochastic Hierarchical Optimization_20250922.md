# Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization

**Korean Title:** 적응형 알고리즘의 예리한 수렴 속도를 갖춘 확률적 계층 최적화

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Minimax Optimization, Bilevel Optimization

## 🔗 유사한 논문
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (86.4% similar)
- [[2025-09-18/Stochastic Adaptive Gradient Descent Without Descent_20250918|Stochastic Adaptive Gradient Descent Without Descent]] (84.5% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (83.4% similar)
- [[2025-09-17/Decentralized Optimization with Topology-Independent Communication_20250917|Decentralized Optimization with Topology-Independent Communication]] (81.9% similar)
- [[2025-09-17/A Variational Framework for Residual-Based Adaptivity in Neural PDE Solvers and Operator Learning_20250917|A Variational Framework for Residual-Based Adaptivity in Neural PDE Solvers and Operator Learning]] (81.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15399v1 Announce Type: new 
Abstract: Hierarchical optimization refers to problems with interdependent decision variables and objectives, such as minimax and bilevel formulations. While various algorithms have been proposed, existing methods and analyses lack adaptivity in stochastic optimization settings: they cannot achieve optimal convergence rates across a wide spectrum of gradient noise levels without prior knowledge of the noise magnitude. In this paper, we propose novel adaptive algorithms for two important classes of stochastic hierarchical optimization problems: nonconvex-strongly-concave minimax optimization and nonconvex-strongly-convex bilevel optimization. Our algorithms achieve sharp convergence rates of $\widetilde{O}(1/\sqrt{T} + \sqrt{\bar{\sigma}}/T^{1/4})$ in $T$ iterations for the gradient norm, where $\bar{\sigma}$ is an upper bound on the stochastic gradient noise. Notably, these rates are obtained without prior knowledge of the noise level, thereby enabling automatic adaptivity in both low and high-noise regimes. To our knowledge, this work provides the first adaptive and sharp convergence guarantees for stochastic hierarchical optimization. Our algorithm design combines the momentum normalization technique with novel adaptive parameter choices. Extensive experiments on synthetic and deep learning tasks demonstrate the effectiveness of our proposed algorithms.

## 🔍 Abstract (한글 번역)

arXiv:2509.15399v1 발표 유형: 신규  
초록: 계층적 최적화는 최소-최대 및 이중 수준 형식과 같이 상호 의존적인 결정 변수와 목표를 가진 문제를 의미합니다. 다양한 알고리즘이 제안되었지만, 기존 방법과 분석은 확률적 최적화 환경에서 적응성을 결여하고 있습니다. 즉, 잡음의 크기에 대한 사전 지식 없이도 다양한 범위의 기울기 잡음 수준에서 최적의 수렴 속도를 달성할 수 없습니다. 본 논문에서는 두 가지 중요한 클래스의 확률적 계층적 최적화 문제에 대한 새로운 적응형 알고리즘을 제안합니다: 비볼록-강한 오목 최소-최대 최적화와 비볼록-강한 볼록 이중 수준 최적화. 우리의 알고리즘은 기울기 노름에 대해 $T$ 반복에서 $\widetilde{O}(1/\sqrt{T} + \sqrt{\bar{\sigma}}/T^{1/4})$의 명확한 수렴 속도를 달성하며, 여기서 $\bar{\sigma}$는 확률적 기울기 잡음의 상한입니다. 특히, 이러한 속도는 잡음 수준에 대한 사전 지식 없이 얻어지며, 저잡음 및 고잡음 환경 모두에서 자동 적응성을 가능하게 합니다. 우리의 지식에 따르면, 이 연구는 확률적 계층적 최적화에 대한 최초의 적응형 및 명확한 수렴 보장을 제공합니다. 우리의 알고리즘 설계는 모멘텀 정규화 기법과 새로운 적응형 매개변수 선택을 결합합니다. 합성 및 심층 학습 과제에 대한 광범위한 실험은 제안된 알고리즘의 효과를 입증합니다.

## 📝 요약

이 논문은 계층적 최적화 문제에서의 새로운 적응형 알고리즘을 제안합니다. 기존 방법들은 잡음 수준에 대한 사전 지식 없이 최적의 수렴 속도를 달성하지 못하는 한계가 있었습니다. 본 연구에서는 비볼록-강한 오목 최소최대 최적화와 비볼록-강한 볼록 이수준 최적화 문제에 대해 새로운 알고리즘을 제안하여, 잡음 수준에 상관없이 자동으로 적응할 수 있는 수렴 속도를 달성했습니다. 제안된 알고리즘은 모멘텀 정규화 기법과 새로운 적응형 매개변수 선택을 결합하여, $T$ 반복에서 기울기 노름에 대해 $\widetilde{O}(1/\sqrt{T} + \sqrt{\bar{\sigma}}/T^{1/4})$의 수렴 속도를 보장합니다. 이는 계층적 최적화 문제에서 최초로 적응형 및 날카로운 수렴 보장을 제공하는 연구로, 실험을 통해 그 효과를 입증했습니다.

## 🎯 주요 포인트

- 1. 계층적 최적화 문제에서 기존 방법들은 확률적 최적화 환경에서 적응성을 결여하고 있다.

- 2. 본 논문은 비볼록-강한 오목 최소극대화와 비볼록-강한 볼록 이수준 최적화 문제를 위한 새로운 적응형 알고리즘을 제안한다.

- 3. 제안된 알고리즘은 사전 소음 수준에 대한 정보 없이도 자동 적응성을 가능하게 하며, 날카로운 수렴 속도를 달성한다.

- 4. 모멘텀 정규화 기법과 새로운 적응형 매개변수 선택을 결합하여 알고리즘을 설계하였다.

- 5. 합성 및 딥러닝 과제에서의 광범위한 실험을 통해 제안된 알고리즘의 효과가 입증되었다.

---

*Generated on 2025-09-22 15:13:09*