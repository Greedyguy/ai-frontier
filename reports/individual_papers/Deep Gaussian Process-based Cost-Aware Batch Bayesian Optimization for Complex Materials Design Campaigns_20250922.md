# Deep Gaussian Process-based Cost-Aware Batch Bayesian Optimization for Complex Materials Design Campaigns

**Korean Title:** 복잡한 재료 설계 캠페인을 위한 비용 인식 배치 베이지안 최적화를 기반으로 한 심층 가우시안 프로세스

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Cost-aware Batch Optimization

## 🔗 유사한 논문
- [[2025-09-19/Compactly-supported nonstationary kernels for computing exact Gaussian processes on big data_20250919|Compactly-supported nonstationary kernels for computing exact Gaussian processes on big data]] (80.4% similar)
- [[2025-09-17/Physics-based deep kernel learning for parameter estimation in high dimensional PDEs_20250917|Physics-based deep kernel learning for parameter estimation in high dimensional PDEs]] (79.9% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (79.7% similar)
- [[2025-09-22/An Equivariant Graph Network for Interpretable Nanoporous Materials Design_20250922|An Equivariant Graph Network for Interpretable Nanoporous Materials Design]] (79.6% similar)
- [[2025-09-22/Learning to Optimize Capacity Planning in Semiconductor Manufacturing_20250922|Learning to Optimize Capacity Planning in Semiconductor Manufacturing]] (79.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14408v1 Announce Type: cross 
Abstract: The accelerating pace and expanding scope of materials discovery demand optimization frameworks that efficiently navigate vast, nonlinear design spaces while judiciously allocating limited evaluation resources. We present a cost-aware, batch Bayesian optimization scheme powered by deep Gaussian process (DGP) surrogates and a heterotopic querying strategy. Our DGP surrogate, formed by stacking GP layers, models complex hierarchical relationships among high-dimensional compositional features and captures correlations across multiple target properties, propagating uncertainty through successive layers. We integrate evaluation cost into an upper-confidence-bound acquisition extension, which, together with heterotopic querying, proposes small batches of candidates in parallel, balancing exploration of under-characterized regions with exploitation of high-mean, low-variance predictions across correlated properties. Applied to refractory high-entropy alloys for high-temperature applications, our framework converges to optimal formulations in fewer iterations with cost-aware queries than conventional GP-based BO, highlighting the value of deep, uncertainty-aware, cost-sensitive strategies in materials campaigns.

## 🔍 Abstract (한글 번역)

arXiv:2509.14408v1 발표 유형: 교차  
초록: 재료 발견의 가속화된 속도와 확장된 범위는 방대한 비선형 설계 공간을 효율적으로 탐색하면서 제한된 평가 자원을 신중하게 할당하는 최적화 프레임워크를 요구합니다. 우리는 심층 가우시안 프로세스(DGP) 대리모델과 이질적 쿼리 전략에 의해 구동되는 비용 인식 일괄 베이지안 최적화 방식을 제시합니다. GP 계층을 쌓아 형성된 우리의 DGP 대리모델은 고차원 조성적 특징 간의 복잡한 계층적 관계를 모델링하고, 여러 목표 특성 간의 상관관계를 포착하며, 불확실성을 연속적인 계층을 통해 전파합니다. 우리는 평가 비용을 상한 신뢰 경계 획득 확장에 통합하여, 이질적 쿼리와 함께 상관된 특성 전반에 걸쳐 고평균, 저분산 예측의 착취와 덜 특성화된 영역의 탐색을 균형 있게 수행하며, 병렬로 소규모 후보군을 제안합니다. 고온 응용을 위한 내화 고엔트로피 합금에 적용된 우리의 프레임워크는 비용 인식 쿼리를 통해 기존의 GP 기반 베이지안 최적화보다 적은 반복으로 최적의 조성에 수렴하며, 재료 캠페인에서 심층, 불확실성 인식, 비용 민감 전략의 가치를 강조합니다.

## 📝 요약

이 논문은 재료 발견의 가속화된 속도와 확장된 범위에 대응하기 위해, 제한된 평가 자원을 효율적으로 활용하는 최적화 프레임워크를 제안합니다. 제안된 방법은 딥 가우시안 프로세스(DGP) 대리모델과 이질적 쿼리 전략을 활용한 비용 인식 배치 베이지안 최적화 기법입니다. DGP 대리모델은 고차원 구성 요소 간의 복잡한 계층적 관계를 모델링하고, 여러 목표 특성 간의 상관관계를 포착하여 불확실성을 계층적으로 전파합니다. 평가 비용을 고려한 상한 신뢰 구간 획득 확장을 통합하여, 이질적 쿼리와 함께 소규모 후보군을 병렬로 제안합니다. 이 방법은 고온용 내화 고엔트로피 합금에 적용되어, 기존의 GP 기반 베이지안 최적화보다 적은 반복으로 최적의 조성을 찾아냅니다. 이는 재료 개발 캠페인에서 딥러닝 기반의 불확실성 인식 및 비용 민감 전략의 가치를 강조합니다.

## 🎯 주요 포인트

- 1. 본 연구는 심층 가우시안 프로세스(DGP) 대리모델과 이질적 쿼리 전략을 활용한 비용 인식 배치 베이지안 최적화 방식을 제안합니다.

- 2. DGP 대리모델은 고차원 조성 특징 간의 복잡한 계층적 관계를 모델링하고, 여러 목표 특성 간의 상관관계를 포착하여 불확실성을 계층적으로 전파합니다.

- 3. 평가 비용을 상한 신뢰 경계 획득 확장에 통합하여, 이질적 쿼리와 함께 고평균, 저분산 예측을 활용하며 덜 특성화된 영역을 탐색합니다.

- 4. 고온 응용을 위한 내화 고엔트로피 합금에 적용한 결과, 비용 인식 쿼리를 통해 기존 GP 기반 BO보다 적은 반복으로 최적의 조성에 수렴했습니다.

- 5. 본 프레임워크는 재료 개발 캠페인에서 심층적, 불확실성 인식, 비용 민감 전략의 가치를 강조합니다.

---

*Generated on 2025-09-22 15:35:25*