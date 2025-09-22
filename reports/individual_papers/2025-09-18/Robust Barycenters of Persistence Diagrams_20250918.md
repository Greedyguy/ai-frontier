# Robust Barycenters of Persistence Diagrams

**Korean Title:** 지속성 다이어그램의 강건한 중심점

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Keanu Sisouk|Keanu Sisouk]] [[authors/Eloi Tanguy|Eloi Tanguy]] [[authors/Julie Delon|Julie Delon]] [[authors/Julien Tierny|Julien Tierny]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Outlier Robustness

## 🔗 유사한 논문
- [[Geometry-Aware Decentralized Sinkhorn for Wasserstein Barycenters_20250919|Geometry-Aware Decentralized Sinkhorn for Wasserstein Barycenters]] (79.3% similar)
- [[Distributionally Robust Equilibria over the Wasserstein Distance for Generalized Nash Game_20250918|Distributionally Robust Equilibria over the Wasserstein Distance for Generalized Nash Game]] (76.8% similar)
- [[Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (76.3% similar)
- [[A Universal Banach--Bregman Framework for Stochastic Iterations_ Unifying Stochastic Mirror Descent, Learning and LLM Training_20250917|A Universal Banach--Bregman Framework for Stochastic Iterations Unifying Stochastic Mirror Descent, Learning and LLM Training]] (75.4% similar)
- [[Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (75.2% similar)

## 📋 저자 정보

**Authors:** Keanu Sisouk, Eloi Tanguy, Julie Delon, Julien Tierny

## 📄 Abstract (원문)

This short paper presents a general approach for computing robust Wasserstein
barycenters of persistence diagrams. The classical method consists in computing
assignment arithmetic means after finding the optimal transport plans between
the barycenter and the persistence diagrams. However, this procedure only works
for the transportation cost related to the $q$-Wasserstein distance $W_q$ when
$q=2$. We adapt an alternative fixed-point method to compute a barycenter
diagram for generic transportation costs ($q > 1$), in particular those robust
to outliers, $q \in (1,2)$. We show the utility of our work in two
applications: \emph{(i)} the clustering of persistence diagrams on their metric
space and \emph{(ii)} the dictionary encoding of persistence diagrams. In both
scenarios, we demonstrate the added robustness to outliers provided by our
generalized framework. Our Python implementation is available at this address:
https://github.com/Keanu-Sisouk/RobustBarycenter .

## 🔍 Abstract (한글 번역)

이 짧은 논문은 지속성 다이어그램의 강건한 Wasserstein 중심을 계산하기 위한 일반적인 접근 방식을 제시합니다. 고전적인 방법은 중심과 지속성 다이어그램 간의 최적 수송 계획을 찾은 후 할당 산술 평균을 계산하는 것으로 구성됩니다. 그러나 이 절차는 $q$-Wasserstein 거리 $W_q$와 관련된 수송 비용에 대해 $q=2$일 때만 작동합니다. 우리는 일반적인 수송 비용($q > 1$), 특히 이상치에 강건한 $q \in (1,2)$에 대해 중심 다이어그램을 계산하기 위해 대안적인 고정점 방법을 적용합니다. 우리는 두 가지 응용에서 우리의 작업의 유용성을 보여줍니다: \emph{(i)} 지속성 다이어그램의 거리 공간에서의 클러스터링과 \emph{(ii)} 지속성 다이어그램의 사전 인코딩. 두 시나리오 모두에서, 우리는 우리의 일반화된 프레임워크가 제공하는 이상치에 대한 추가적인 강건성을 입증합니다. 우리의 Python 구현은 다음 주소에서 확인할 수 있습니다: https://github.com/Keanu-Sisouk/RobustBarycenter .

## 📝 요약

이 논문은 지속성 다이어그램의 강건한 Wasserstein 중심을 계산하는 일반적인 접근법을 제시합니다. 기존 방법은 $q$-Wasserstein 거리 $W_q$에서 $q=2$일 때만 최적 수송 계획을 통해 중심을 계산합니다. 본 연구에서는 $q>1$인 일반적인 수송 비용, 특히 이상치에 강건한 $q \in (1,2)$의 경우에도 적용 가능한 고정점 방법을 도입했습니다. 이 방법의 유용성은 지속성 다이어그램의 군집화와 사전 인코딩 두 가지 응용에서 입증되었으며, 이상치에 대한 강건성을 강화했습니다. Python 구현은 GitHub에서 확인할 수 있습니다.

## 🎯 주요 포인트

- 1. 이 논문은 지속성 다이어그램의 강건한 Wasserstein 중심을 계산하는 일반적인 접근 방식을 제시합니다.

- 2. 기존 방법은 $q=2$인 경우에만 적용되며, 본 연구는 $q > 1$인 일반적인 운송 비용에 대해 대안적인 고정점 방법을 적용합니다.

- 3. 제안된 방법은 이상치에 강건한 $q \in (1,2)$의 경우에도 적용 가능하며, 지속성 다이어그램의 클러스터링 및 사전 인코딩에 유용합니다.

- 4. 제안된 프레임워크는 이상치에 대한 강건성을 제공하며, Python 구현은 GitHub에서 제공됩니다.

---

*Generated on 2025-09-20 02:44:32*