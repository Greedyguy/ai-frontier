# On the Convergence of Muon and Beyond

**Korean Title:** 뮤온과 그 너머의 수렴에 관하여

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Polyak Lojasiewicz Condition

## 🔗 유사한 논문
- [[2025-09-18/LiMuon_ Light and Fast Muon Optimizer for Large Models_20250918|LiMuon Light and Fast Muon Optimizer for Large Models]] (88.9% similar)
- [[2025-09-22/Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization_20250922|Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization]] (80.8% similar)
- [[2025-09-18/Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (80.3% similar)
- [[2025-09-17/A Universal Banach--Bregman Framework for Stochastic Iterations_ Unifying Stochastic Mirror Descent, Learning and LLM Training_20250917|A Universal Banach--Bregman Framework for Stochastic Iterations Unifying Stochastic Mirror Descent, Learning and LLM Training]] (79.9% similar)
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (79.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15816v1 Announce Type: new 
Abstract: The Muon optimizer has demonstrated remarkable empirical success in handling matrix-structured parameters for training neural networks. However, a significant gap persists between its practical performance and theoretical understanding. Existing analyses indicate that the standard Muon variant achieves only a suboptimal convergence rate of $\mathcal{O}(T^{-1/4})$ in stochastic non-convex settings, where $T$ denotes the number of iterations. To explore the theoretical limits of the Muon framework, we construct and analyze a variance-reduced variant, termed Muon-VR2. We provide the first rigorous proof that incorporating a variance-reduction mechanism enables Muon-VR2 to attain an optimal convergence rate of $\tilde{\mathcal{O}}(T^{-1/3})$, thereby matching the theoretical lower bound for this class of problems. Moreover, our analysis establishes convergence guarantees for Muon variants under the Polyak-{\L}ojasiewicz (P{\L}) condition. Extensive experiments on vision (CIFAR-10) and language (C4) benchmarks corroborate our theoretical findings on per-iteration convergence. Overall, this work provides the first proof of optimality for a Muon-style optimizer and clarifies the path toward developing more practically efficient, accelerated variants.

## 🔍 Abstract (한글 번역)

arXiv:2509.15816v1 발표 유형: 신규  
초록: 뮤온(Muon) 최적화 기법은 신경망 훈련을 위한 행렬 구조의 매개변수 처리에서 놀라운 경험적 성공을 보여주었습니다. 그러나 실질적인 성능과 이론적 이해 사이에는 여전히 상당한 격차가 존재합니다. 기존 분석에 따르면, 표준 뮤온 변형은 확률적 비볼록 설정에서 $\mathcal{O}(T^{-1/4})$의 비최적 수렴 속도만 달성한다고 합니다. 여기서 $T$는 반복 횟수를 나타냅니다. 뮤온 프레임워크의 이론적 한계를 탐구하기 위해, 우리는 분산 감소 변형인 Muon-VR2를 구성하고 분석합니다. 분산 감소 메커니즘을 통합함으로써 Muon-VR2가 이 문제 유형에 대한 이론적 하한과 일치하는 최적 수렴 속도인 $\tilde{\mathcal{O}}(T^{-1/3})$를 달성할 수 있음을 최초로 엄밀히 증명합니다. 또한, 우리의 분석은 Polyak-{\L}ojasiewicz (P{\L}) 조건 하에서 뮤온 변형의 수렴 보장을 확립합니다. 비전(CIFAR-10) 및 언어(C4) 벤치마크에 대한 광범위한 실험은 반복당 수렴에 대한 우리의 이론적 발견을 입증합니다. 전반적으로, 이 연구는 뮤온 스타일 최적화 기법의 최적성을 최초로 증명하고, 보다 실용적으로 효율적이고 가속화된 변형 개발을 위한 경로를 명확히 합니다.

## 📝 요약

Muon 최적화 기법은 신경망 학습에서 행렬 구조의 매개변수를 효과적으로 처리하지만, 이론적 이해가 부족합니다. 기존 분석에 따르면, 표준 Muon은 확률적 비볼록 환경에서 $\mathcal{O}(T^{-1/4})$의 수렴 속도를 보입니다. 이를 개선하기 위해, 우리는 분산 감소 기법을 적용한 Muon-VR2를 제안하고, 이 기법이 $\tilde{\mathcal{O}}(T^{-1/3})$의 최적 수렴 속도를 달성함을 증명했습니다. 또한, Polyak-{\L}ojasiewicz 조건 하에서 Muon 변형의 수렴성을 입증했습니다. CIFAR-10 및 C4 벤치마크 실험 결과는 이론적 발견을 뒷받침합니다. 이 연구는 Muon 스타일 최적화 기법의 최적성을 최초로 증명하고, 실용적으로 효율적인 가속 변형 개발의 방향을 제시합니다.

## 🎯 주요 포인트

- 1. Muon 최적화 기법은 신경망 훈련에서 행렬 구조의 매개변수를 효과적으로 처리하는 데 성공을 거두었다.

- 2. 기존 Muon 변형은 확률적 비볼록 환경에서 $\mathcal{O}(T^{-1/4})$의 수렴 속도를 보이며 최적의 성능을 발휘하지 못한다.

- 3. Muon-VR2라는 분산 감소 변형을 통해 이론적 하한에 맞춘 $\tilde{\mathcal{O}}(T^{-1/3})$의 최적 수렴 속도를 달성할 수 있음을 증명하였다.

- 4. Muon 변형은 Polyak-{\L}ojasiewicz (P{\L}) 조건 하에서 수렴 보장을 제공한다.

- 5. CIFAR-10 및 C4 벤치마크 실험을 통해 이론적 발견이 실험적으로도 확인되었다.

---

*Generated on 2025-09-22 15:24:48*