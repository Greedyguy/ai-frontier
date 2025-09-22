# Personalized Federated Learning with Heat-Kernel Enhanced Tensorized Multi-View Clustering

**Korean Title:** 개인화된 연방 학습과 열 커널이 강화된 텐서화된 다중 뷰 클러스터링

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Privacy-Preserving Personalization

## 🔗 유사한 논문
- [[2025-09-22/FedHK-MVFC_ Federated Heat Kernel Multi-View Clustering_20250922|FedHK-MVFC Federated Heat Kernel Multi-View Clustering]] (86.8% similar)
- [[2025-09-19/Federated Hypergraph Learning with Local Differential Privacy_ Toward Privacy-Aware Hypergraph Structure Completion_20250919|Federated Hypergraph Learning with Local Differential Privacy Toward Privacy-Aware Hypergraph Structure Completion]] (81.9% similar)
- [[2025-09-19/Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning_20250919|Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning]] (81.4% similar)
- [[2025-09-17/Differential Privacy in Federated Learning_ Mitigating Inference Attacks with Randomized Response_20250917|Differential Privacy in Federated Learning Mitigating Inference Attacks with Randomized Response]] (81.2% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (80.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16101v1 Announce Type: new 
Abstract: We present a robust personalized federated learning framework that leverages heat-kernel enhanced tensorized multi-view fuzzy c-means clustering with advanced tensor decomposition techniques. Our approach integrates heat-kernel coefficients adapted from quantum field theory with Tucker decomposition and canonical polyadic decomposition (CANDECOMP/PARAFAC) to transform conventional distance metrics and efficiently represent high-dimensional multi-view structures. The framework employs matriculation and vectorization techniques to facilitate the discovery of hidden structures and multilinear relationships via N-way generalized tensors. The proposed method introduces a dual-level optimization scheme: local heat-kernel enhanced fuzzy clustering with tensor decomposition operating on order-N input tensors, and federated aggregation of tensor factors with privacy-preserving personalization mechanisms. The local stage employs tensorized kernel Euclidean distance transformations and Tucker decomposition to discover client-specific patterns in multi-view tensor data, while the global aggregation process coordinates tensor factors (core tensors and factor matrices) across clients through differential privacy-preserving protocols. This tensorized approach enables efficient handling of high-dimensional multi-view data with significant communication savings through low-rank tensor approximations.

## 🔍 Abstract (한글 번역)

arXiv:2509.16101v1 발표 유형: 신규  
초록: 우리는 열핵 강화 텐서화 다중 뷰 퍼지 c-평균 클러스터링과 고급 텐서 분해 기법을 활용한 견고한 개인화 연합 학습 프레임워크를 제시합니다. 우리의 접근법은 양자장 이론에서 적응된 열핵 계수를 터커 분해 및 정준 다항식 분해(CANDECOMP/PARAFAC)와 통합하여 기존의 거리 측정값을 변환하고 고차원 다중 뷰 구조를 효율적으로 표현합니다. 이 프레임워크는 행렬화 및 벡터화 기법을 사용하여 N-방향 일반화 텐서를 통해 숨겨진 구조와 다중 선형 관계를 발견합니다. 제안된 방법은 이중 수준 최적화 체계를 도입합니다: 순서-N 입력 텐서에서 작동하는 지역 열핵 강화 퍼지 클러스터링과 텐서 분해, 그리고 프라이버시 보호 개인화 메커니즘을 통한 텐서 요소의 연합 집계. 지역 단계에서는 텐서화된 커널 유클리드 거리 변환과 터커 분해를 사용하여 다중 뷰 텐서 데이터에서 클라이언트별 패턴을 발견하며, 글로벌 집계 프로세스는 차등 프라이버시 보호 프로토콜을 통해 클라이언트 간의 텐서 요소(코어 텐서 및 요소 행렬)를 조정합니다. 이 텐서화 접근법은 저차 텐서 근사를 통한 통신 절약을 통해 고차원 다중 뷰 데이터를 효율적으로 처리할 수 있게 합니다.

## 📝 요약

이 논문은 열핵 커널을 활용한 텐서화된 다중 뷰 퍼지 C-평균 클러스터링을 통해 개인화된 연합 학습 프레임워크를 제안합니다. 양자장 이론에서 차용한 열핵 계수를 터커 분해와 CANDECOMP/PARAFAC 분해와 결합하여 고차원 다중 뷰 구조를 효율적으로 표현합니다. 이 방법은 N-방향 일반화 텐서를 통해 숨겨진 구조와 다중 선형 관계를 발견하며, 로컬 및 글로벌 최적화 단계를 포함합니다. 로컬 단계에서는 클라이언트별 패턴을 발견하고, 글로벌 단계에서는 차별적 프라이버시를 유지하며 텐서 요인을 집계합니다. 이 접근법은 고차원 데이터를 효율적으로 처리하며 통신 비용을 절감합니다.

## 🎯 주요 포인트

- 1. 본 연구는 열 커널을 활용한 텐서화된 다중 뷰 퍼지 C-평균 클러스터링을 통해 개인화된 연합 학습 프레임워크를 제안합니다.

- 2. 양자장 이론에서 적응된 열 커널 계수를 Tucker 분해 및 CANDECOMP/PARAFAC과 통합하여 고차원 다중 뷰 구조를 효율적으로 표현합니다.

- 3. N-way 일반화 텐서를 통해 숨겨진 구조와 다중 선형 관계를 발견하기 위해 행렬화 및 벡터화 기법을 사용합니다.

- 4. 제안된 방법은 로컬 열 커널 퍼지 클러스터링과 텐서 분해, 그리고 프라이버시를 보장하는 개인화 메커니즘을 통한 연합 집계를 포함한 이중 최적화 체계를 도입합니다.

- 5. 저차원 텐서 근사를 통해 고차원 다중 뷰 데이터를 효율적으로 처리하고 통신 비용을 절감합니다.

---

*Generated on 2025-09-22 15:32:41*