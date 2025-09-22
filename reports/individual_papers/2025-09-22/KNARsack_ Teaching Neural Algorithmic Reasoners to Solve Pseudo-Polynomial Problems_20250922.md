# KNARsack: Teaching Neural Algorithmic Reasoners to Solve Pseudo-Polynomial Problems

**Korean Title:** KNARsack: 신경 알고리즘 추론자를 가르쳐 의사다항식 문제 해결하기

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Pseudo-Polynomial Problem Solving

## 🔗 유사한 논문
- [[2025-09-18/Polynomial-Time Approximation Schemes via Utility Alignment_ Unit-Demand Pricing and More_20250918|Polynomial-Time Approximation Schemes via Utility Alignment Unit-Demand Pricing and More]] (77.3% similar)
- [[2025-09-19/Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (77.3% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (77.2% similar)
- [[2025-09-19/RationAnomaly_ Log Anomaly Detection with Rationality via Chain-of-Thought and Reinforcement Learning_20250919|RationAnomaly Log Anomaly Detection with Rationality via Chain-of-Thought and Reinforcement Learning]] (77.1% similar)
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (77.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15239v1 Announce Type: new 
Abstract: Neural algorithmic reasoning (NAR) is a growing field that aims to embed algorithmic logic into neural networks by imitating classical algorithms. In this extended abstract, we detail our attempt to build a neural algorithmic reasoner that can solve Knapsack, a pseudo-polynomial problem bridging classical algorithms and combinatorial optimisation, but omitted in standard NAR benchmarks. Our neural algorithmic reasoner is designed to closely follow the two-phase pipeline for the Knapsack problem, which involves first constructing the dynamic programming table and then reconstructing the solution from it. The approach, which models intermediate states through dynamic programming supervision, achieves better generalization to larger problem instances than a direct-prediction baseline that attempts to select the optimal subset only from the problem inputs.

## 🔍 Abstract (한글 번역)

arXiv:2509.15239v1 발표 유형: 신규  
초록: 신경 알고리즘적 추론(NAR)은 고전 알고리즘을 모방하여 알고리즘적 논리를 신경망에 내재화하려는 성장하는 분야입니다. 이 확장된 초록에서는 고전 알고리즘과 조합 최적화를 연결하는 의사다항식 문제인 배낭 문제를 해결할 수 있는 신경 알고리즘 추론기를 구축하려는 시도를 자세히 설명합니다. 이 문제는 표준 NAR 벤치마크에서는 생략되었습니다. 우리의 신경 알고리즘 추론기는 배낭 문제에 대한 두 단계 파이프라인을 밀접하게 따르도록 설계되었으며, 여기에는 먼저 동적 프로그래밍 테이블을 구성한 다음 그로부터 해를 재구성하는 과정이 포함됩니다. 중간 상태를 동적 프로그래밍 감독을 통해 모델링하는 이 접근 방식은 문제 입력에서 최적의 부분 집합을 선택하려는 직접 예측 기준선보다 더 큰 문제 인스턴스에 대한 일반화 성능이 뛰어납니다.

## 📝 요약

이 논문은 신경 알고리즘적 추론(NAR)을 활용하여 배낭 문제를 해결하는 신경 알고리즘 추론기를 개발하는 연구를 다룹니다. 배낭 문제는 전통적인 알고리즘과 조합 최적화 문제를 연결하는 의사다항식 문제로, 기존 NAR 벤치마크에서는 다루어지지 않았습니다. 연구진은 배낭 문제를 해결하기 위해 동적 프로그래밍 테이블을 구성하고 이를 기반으로 솔루션을 재구성하는 두 단계의 파이프라인을 따르는 신경 알고리즘 추론기를 설계했습니다. 이 방법론은 문제 입력만으로 최적 부분집합을 선택하려는 직접 예측 방식보다 더 큰 문제 사례에 대한 일반화 성능이 우수함을 보여줍니다.

## 🎯 주요 포인트

- 1. 신경 알고리즘적 추론(NAR)은 고전 알고리즘을 모방하여 알고리즘적 논리를 신경망에 내재화하는 것을 목표로 하는 성장하는 분야입니다.

- 2. 본 연구에서는 Knapsack 문제를 해결할 수 있는 신경 알고리즘적 추론기를 구축하려는 시도를 상세히 설명합니다.

- 3. 제안된 신경 알고리즘적 추론기는 동적 프로그래밍 테이블을 구성하고 이를 통해 솔루션을 재구성하는 두 단계 파이프라인을 따릅니다.

- 4. 동적 프로그래밍 감독을 통해 중간 상태를 모델링하는 접근 방식은 문제 입력만으로 최적의 부분집합을 선택하려는 직접 예측 기준보다 더 큰 문제 인스턴스에 대한 일반화 성능이 뛰어납니다.

---

*Generated on 2025-09-22 13:42:28*