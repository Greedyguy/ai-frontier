# Inverse Optimization Latent Variable Models for Learning Costs Applied to Route Problems

**Korean Title:** 경로 문제에 적용된 비용 학습을 위한 역최적화 잠재 변수 모델

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Distribution over Cost Functions

## 🔗 유사한 논문
- [[2025-09-22/Momentum-constrained Hybrid Heuristic Trajectory Optimization Framework with Residual-enhanced DRL for Visually Impaired Scenarios_20250922|Momentum-constrained Hybrid Heuristic Trajectory Optimization Framework with Residual-enhanced DRL for Visually Impaired Scenarios]] (80.2% similar)
- [[2025-09-22/PVPO_ Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning_20250922|PVPO Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning]] (80.2% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (79.8% similar)
- [[2025-09-22/Partial Column Generation with Graph Neural Networks for Team Formation and Routing_20250922|Partial Column Generation with Graph Neural Networks for Team Formation and Routing]] (79.6% similar)
- [[2025-09-18/NavMoE_ Hybrid Model- and Learning-based Traversability Estimation for Local Navigation via Mixture of Experts_20250918|NavMoE Hybrid Model- and Learning-based Traversability Estimation for Local Navigation via Mixture of Experts]] (79.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15999v1 Announce Type: new 
Abstract: Learning representations for solutions of constrained optimization problems (COPs) with unknown cost functions is challenging, as models like (Variational) Autoencoders struggle to enforce constraints when decoding structured outputs. We propose an Inverse Optimization Latent Variable Model (IO-LVM) that learns a latent space of COP cost functions from observed solutions and reconstructs feasible outputs by solving a COP with a solver in the loop. Our approach leverages estimated gradients of a Fenchel-Young loss through a non-differentiable deterministic solver to shape the latent space. Unlike standard Inverse Optimization or Inverse Reinforcement Learning methods, which typically recover a single or context-specific cost function, IO-LVM captures a distribution over cost functions, enabling the identification of diverse solution behaviors arising from different agents or conditions not available during the training process. We validate our method on real-world datasets of ship and taxi routes, as well as paths in synthetic graphs, demonstrating its ability to reconstruct paths and cycles, predict their distributions, and yield interpretable latent representations.

## 🔍 Abstract (한글 번역)

arXiv:2509.15999v1 발표 유형: 신규  
초록: 비용 함수가 알려지지 않은 제약 최적화 문제(COP)의 해에 대한 표현을 학습하는 것은 도전적입니다. (변분) 오토인코더와 같은 모델은 구조화된 출력을 디코딩할 때 제약 조건을 강제하는 데 어려움을 겪습니다. 우리는 관찰된 해로부터 COP 비용 함수의 잠재 공간을 학습하고, 루프 내에서 해석기를 사용하여 COP를 해결함으로써 실행 가능한 출력을 재구성하는 역최적화 잠재 변수 모델(IO-LVM)을 제안합니다. 우리의 접근법은 비분화 가능한 결정론적 해석기를 통해 펜첼-영 손실의 추정된 그래디언트를 활용하여 잠재 공간을 형성합니다. 표준 역최적화 또는 역강화학습 방법과 달리, IO-LVM은 단일 또는 상황별 비용 함수를 복원하는 대신 비용 함수의 분포를 포착하여 훈련 과정에서 이용할 수 없는 다양한 에이전트나 조건에서 발생하는 다양한 해의 행동을 식별할 수 있게 합니다. 우리는 실제 선박 및 택시 경로 데이터셋과 합성 그래프의 경로에서 우리의 방법을 검증하여 경로와 사이클을 재구성하고, 그 분포를 예측하며, 해석 가능한 잠재 표현을 도출하는 능력을 입증합니다.

## 📝 요약

이 논문은 비용 함수가 알려지지 않은 제약 최적화 문제(COP)의 해를 학습하는 새로운 접근법을 제안합니다. 기존 모델들이 구조화된 출력을 디코딩할 때 제약 조건을 잘 적용하지 못하는 문제를 해결하기 위해, 저자들은 관찰된 해로부터 COP 비용 함수의 잠재 공간을 학습하고, COP를 풀어 가능한 출력을 재구성하는 역최적화 잠재변수 모델(IO-LVM)을 제안합니다. 이 모델은 Fenchel-Young 손실의 추정된 그래디언트를 비미분 가능한 결정론적 솔버를 통해 활용하여 잠재 공간을 형성합니다. 기존의 역최적화나 역강화학습 방법과 달리, IO-LVM은 다양한 에이전트나 조건에서 발생할 수 있는 다양한 해의 행동을 포착할 수 있는 비용 함수의 분포를 학습합니다. 실제 데이터셋인 선박 및 택시 경로와 합성 그래프 경로에서 모델을 검증하여 경로와 사이클을 재구성하고, 그 분포를 예측하며, 해석 가능한 잠재 표현을 제공하는 능력을 입증했습니다.

## 🎯 주요 포인트

- 1. 제안된 IO-LVM 모델은 관측된 해로부터 COP 비용 함수의 잠재 공간을 학습하고, COP를 풀어내어 구조화된 출력을 재구성합니다.

- 2. IO-LVM은 Fenchel-Young 손실의 추정된 그래디언트를 비분화 가능한 결정론적 솔버를 통해 활용하여 잠재 공간을 형성합니다.

- 3. 기존의 역최적화 또는 역강화학습 방법과 달리, IO-LVM은 다양한 에이전트나 조건에서 발생할 수 있는 다양한 솔루션 행동을 식별할 수 있는 비용 함수의 분포를 포착합니다.

- 4. 실제 데이터셋(선박 및 택시 경로)과 합성 그래프 경로에서 IO-LVM의 유효성을 검증하여 경로 및 사이클을 재구성하고, 그 분포를 예측하며 해석 가능한 잠재 표현을 제공합니다.

---

*Generated on 2025-09-22 15:29:28*