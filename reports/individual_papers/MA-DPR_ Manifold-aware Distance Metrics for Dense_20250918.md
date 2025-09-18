
# MA-DPR: Manifold-aware Distance Metrics for Dense Passage Retrieval

**Korean Title:** MA-DPR: 밀도 높은 통로 검색을 위한 매니폴드 인식 거리 측정법

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Out-of-distribution Passage Retrieval|Out-of-distribution Passage Retrieval]] [[keywords/broad/Dense Passage Retrieval|Dense Passage Retrieval]] [[keywords/broad/Manifold-aware Distance Metrics|Manifold-aware Distance Metrics]] [[keywords/specific/Nearest Neighbor Graph|Nearest Neighbor Graph]] [[keywords/unique/MA-DPR|MA-DPR]] [[categories/cs.IR|cs.IR]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Out-of-distribution Passage Retrieval
**🔬 Broad Technical**: Dense Passage Retrieval, Manifold-aware Distance Metrics
**🔗 Specific Connectable**: Nearest Neighbor Graph
**⭐ Unique Technical**: MA-DPR

**ArXiv ID**: [2509.13562](https://arxiv.org/abs/2509.13562)
**Published**: 2025-09-18
**Category**: cs.IR
**PDF**: [Download](https://arxiv.org/pdf/2509.13562.pdf)


## 🏷️ 추출된 키워드



`Dense Passage Retrieval` • 

`Manifold-aware Distance Metrics` • 

`Nearest Neighbor Graph` • 

`MA-DPR` • 

`Out-of-distribution Passage Retrieval`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13562v1 Announce Type: new 
Abstract: Dense Passage Retrieval (DPR) typically relies on Euclidean or cosine distance to measure query-passage relevance in embedding space, which is effective when embeddings lie on a linear manifold. However, our experiments across DPR benchmarks suggest that embeddings often lie on lower-dimensional, non-linear manifolds, especially in out-of-distribution (OOD) settings, where cosine and Euclidean distance fail to capture semantic similarity. To address this limitation, we propose a manifold-aware distance metric for DPR (MA-DPR) that models the intrinsic manifold structure of passages using a nearest neighbor graph and measures query-passage distance based on their shortest path in this graph. We show that MA-DPR outperforms Euclidean and cosine distances by up to 26% on OOD passage retrieval with comparable in-distribution performance across various embedding models while incurring a minimal increase in query inference time. Empirical evidence suggests that manifold-aware distance allows DPR to leverage context from related neighboring passages, making it effective even in the absence of direct semantic overlap. MADPR can be applied to a wide range of dense embedding and retrieval tasks, offering potential benefits across a wide spectrum of domains.

## 🔍 Abstract (한글 번역)

arXiv:2509.13562v1 발표 유형: 새로운
요약: 밀집 통로 검색 (DPR)은 일반적으로 쿼리-통로 관련성을 임베딩 공간에서 측정하기 위해 유클리드 거리나 코사인 거리를 의존하는데, 이는 임베딩이 선형 매니폴드에 위치할 때 효과적입니다. 그러나 DPR 벤치마크를 통해 한 실험 결과, 임베딩이 종종 낮은 차원의 비선형 매니폴드에 위치하며, 특히 분포 이탈 (OOD) 환경에서는 코사인 거리와 유클리드 거리가 의미론적 유사성을 포착하지 못하는 것으로 나타났습니다. 이 한계를 해결하기 위해, 우리는 DPR (MA-DPR)을 위한 매니폴드 인식 거리 메트릭을 제안합니다. 이 메트릭은 최근접 이웃 그래프를 사용하여 통로의 내재 매니폴드 구조를 모델링하고, 이 그래프에서의 최단 경로를 기반으로 쿼리-통로 거리를 측정합니다. 우리는 MA-DPR이 OOD 통로 검색에서 유클리드와 코사인 거리를 최대 26%까지 능가하며, 다양한 임베딩 모델에서의 분포 내 성능과 비교 가능한 성능을 보여주는 동안, 쿼리 추론 시간의 증가는 최소화된다는 것을 보여줍니다. 경험적 증거는 매니폴드 인식 거리가 DPR이 관련된 이웃 통로로부터의 문맥을 활용하게 하여, 직접적인 의미적 중첩이 없어도 효과적으로 만들어준다는 것을 시사합니다. MADPR은 다양한 밀집 임베딩 및 검색 작업에 적용될 수 있으며, 다양한 도메인에서 잠재적 이점을 제공합니다.

## 📝 요약

한국어 요약:
본 연구는 Dense Passage Retrieval (DPR)에서 사용되는 유클리드 거리나 코사인 거리가 임베딩 공간에서 쿼리-패스지 관련성을 측정하는 데 효과적이지만, 임베딩이 선형 다양체에 있을 때만 유효하다는 것을 발견했습니다. 이에 우리는 패스지의 내재 다양체 구조를 모델링하고 이를 기반으로 쿼리-패스지 거리를 측정하는 매니폴드 인식 거리 메트릭 MA-DPR을 제안합니다. MA-DPR은 OOD 패스지 검색에서 최대 26%까지 성능을 향상시키고 쿼리 추론 시간을 최소화하면서 다양한 임베딩 모델에서 비교 가능한 인-분포 성능을 보입니다. 매니폴드 인식 거리는 DPR이 직접적인 의미적 중복이 없어도 관련 이웃 패스지의 컨텍스트를 활용할 수 있게 함으로써 효과적입니다. MADPR은 밀도 임베딩 및 검색 작업에 적용될 수 있으며 다양한 도메인에서 잠재적 이점을 제공할 수 있습니다.

## 🎯 주요 포인트


- 1. DPR에서는 임베딩 공간에서 쿼리-통과 문 관련성을 측정하기 위해 유클리드나 코사인 거리를 사용하는데, 이는 임베딩이 선형 다양체에 위치할 때 효과적이다.

- 2. 그러나 실험 결과, 임베딩은 종종 낮은 차원의 비선형 다양체에 위치하며, 특히 OOD 설정에서 코사인과 유클리드 거리는 의미 유사성을 포착하지 못한다.

- 3. MA-DPR은 통과의 내재 다양체 구조를 모델링하고, 이 그래프에서 쿼리-통과 거리를 측정하여 OOD 통과 검색에서 Euclidean과 cosine 거리를 최대 26%까지 능가한다.


---

*Generated on 2025-09-18 17:12:53*