# Query-Efficient Locally Private Hypothesis Selection via the Scheffe Graph

**Korean Title:** 셰페 그래프를 통한 쿼리 효율적인 지역적 프라이버시 가설 선택

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Query-Efficient Algorithms|Query-Efficient Algorithms]] [[keywords/specific/Hypothesis Selection|Hypothesis Selection]] [[keywords/broad/Local Differential Privacy|Local Differential Privacy]] [[keywords/unique/Scheffe Graph|Scheffe Graph]] [[categories/cs.LG|cs.LG]] [[2025-09-22/Personalized Prediction By Learning Halfspace Reference Classes Under Well-Behaved Distribution_20250922|Personalized Prediction By Learning Halfspace Reference Classes Under Well-Behaved Distribution]] (78.8% similar) [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (78.2% similar) [[2025-09-19/Federated Hypergraph Learning with Local Differential Privacy_ Toward Privacy-Aware Hypergraph Structure Completion_20250919|Federated Hypergraph Learning with Local Differential Privacy: Toward Privacy-Aware Hypergraph Structure Completion]] (77.3% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Query-efficient Algorithms
**🔗 Specific Connectable**: Hypothesis Selection
**🔬 Broad Technical**: Local Differential Privacy
**⭐ Unique Technical**: Scheffe Graph
## 🔗 유사한 논문
- [[2025-09-22/Personalized Prediction By Learning Halfspace Reference Classes Under Well-Behaved Distribution_20250922|Personalized Prediction By Learning Halfspace Reference Classes Under Well-Behaved Distribution]] (78.8% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (78.2% similar)
- [[2025-09-19/Federated Hypergraph Learning with Local Differential Privacy_ Toward Privacy-Aware Hypergraph Structure Completion_20250919|Federated Hypergraph Learning with Local Differential Privacy Toward Privacy-Aware Hypergraph Structure Completion]] (77.3% similar)
- [[2025-09-19/Preference Isolation Forest for Structure-based Anomaly Detection_20250919|Preference Isolation Forest for Structure-based Anomaly Detection]] (77.3% similar)
- [[2025-09-18/Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning_20250918|Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning]] (77.1% similar)


**ArXiv ID**: [2509.16180](https://arxiv.org/abs/2509.16180)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.16180.pdf)


**ArXiv ID**: [2509.16180](https://arxiv.org/abs/2509.16180)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.16180.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Query-Efficient Algorithms
**🔗 Specific Connectable**: Hypothesis Selection
**⭐ Unique Technical**: Scheffe Graph
**🔬 Broad Technical**: Local Differential Privacy

## 🏷️ 추출된 키워드



`Local Differential Privacy` • 

`Hypothesis Selection` • 

`Scheffe Graph` • 

`Query-Efficient Algorithms`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16180v1 Announce Type: cross 
Abstract: We propose an algorithm with improved query-complexity for the problem of hypothesis selection under local differential privacy constraints. Given a set of $k$ probability distributions $Q$, we describe an algorithm that satisfies local differential privacy, performs $\tilde{O}(k^{3/2})$ non-adaptive queries to individuals who each have samples from a probability distribution $p$, and outputs a probability distribution from the set $Q$ which is nearly the closest to $p$. Previous algorithms required either $\Omega(k^2)$ queries or many rounds of interactive queries.
  Technically, we introduce a new object we dub the Scheff\'e graph, which captures structure of the differences between distributions in $Q$, and may be of more broad interest for hypothesis selection tasks.

## 🔍 Abstract (한글 번역)

arXiv:2509.16180v1 발표 유형: 교차  
초록: 우리는 지역 차등 프라이버시 제약 조건 하에서 가설 선택 문제에 대한 쿼리 복잡성을 개선한 알고리즘을 제안합니다. $k$개의 확률 분포 집합 $Q$가 주어졌을 때, 우리는 지역 차등 프라이버시를 만족하고, 확률 분포 $p$에서 샘플을 가진 개인에게 $\tilde{O}(k^{3/2})$개의 비적응적 쿼리를 수행하며, $Q$ 집합에서 $p$에 거의 가장 가까운 확률 분포를 출력하는 알고리즘을 설명합니다. 이전 알고리즘은 $\Omega(k^2)$ 쿼리를 필요로 하거나 여러 라운드의 상호작용 쿼리를 요구했습니다. 기술적으로, 우리는 $Q$ 내 분포 간의 차이 구조를 포착하는 Scheffé 그래프라는 새로운 객체를 도입하며, 이는 가설 선택 작업에 더 광범위한 관심을 받을 수 있습니다.

## 📝 요약

이 논문은 지역적 차등 프라이버시 제약 하에서 가설 선택 문제를 해결하기 위한 알고리즘을 제안합니다. 주어진 $k$개의 확률 분포 집합 $Q$에 대해, 이 알고리즘은 $\tilde{O}(k^{3/2})$개의 비적응적 쿼리를 수행하여 각 개인이 가진 확률 분포 $p$와 거의 가장 가까운 분포를 $Q$에서 출력합니다. 이전 알고리즘은 $\Omega(k^2)$ 쿼리나 여러 번의 상호작용 쿼리가 필요했습니다. 기술적으로, 우리는 Scheffé 그래프라는 새로운 개념을 도입하여 $Q$ 내 분포 간의 차이 구조를 포착하며, 이는 가설 선택 작업에 폭넓게 활용될 수 있습니다.

## 🎯 주요 포인트


- 1. 본 논문은 지역 차등 프라이버시 제약 하에서 가설 선택 문제를 위한 개선된 쿼리 복잡도 알고리즘을 제안합니다.

- 2. 제안된 알고리즘은 $\tilde{O}(k^{3/2})$의 비적응적 쿼리를 사용하여, 집합 $Q$에서 $p$에 거의 가장 가까운 확률 분포를 출력합니다.

- 3. 이전 알고리즘은 $\Omega(k^2)$ 쿼리 또는 여러 라운드의 상호작용 쿼리를 필요로 했습니다.

- 4. 새로운 개념인 Scheffé 그래프를 도입하여, $Q$ 내 분포 간 차이의 구조를 포착하고 가설 선택 작업에 광범위하게 활용될 수 있습니다.


---

*Generated on 2025-09-22 15:47:48*