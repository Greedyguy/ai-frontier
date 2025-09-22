# Database-Augmented Query Representation for Information Retrieval

**Korean Title:** 데이터베이스 보강 쿼리 표현을 통한 정보 검색

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Query Expansion with Metadata

## 🔗 유사한 논문
- [[2025-09-22/Chunk Knowledge Generation Model for Enhanced Information Retrieval_ A Multi-task Learning Approach_20250922|Chunk Knowledge Generation Model for Enhanced Information Retrieval A Multi-task Learning Approach]] (83.2% similar)
- [[2025-09-18/MAFA_ A multi-agent framework for annotation_20250918|MAFA A multi-agent framework for annotation]] (80.4% similar)
- [[2025-09-19/ImpRAG_ Retrieval-Augmented Generation with Implicit Queries_20250919|ImpRAG Retrieval-Augmented Generation with Implicit Queries]] (80.4% similar)
- [[2025-09-19/What's the Best Way to Retrieve Slides A Comparative Study of Multimodal, Caption-Based, and Hybrid Retrieval Techniques_20250919|What's the Best Way to Retrieve Slides A Comparative Study of Multimodal, Caption-Based, and Hybrid Retrieval Techniques]] (79.9% similar)
- [[2025-09-19/GASLITEing the Retrieval_ Exploring Vulnerabilities in Dense Embedding-based Search_20250919|GASLITEing the Retrieval Exploring Vulnerabilities in Dense Embedding-based Search]] (79.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2406.16013v3 Announce Type: replace-cross 
Abstract: Information retrieval models that aim to search for documents relevant to a query have shown multiple successes, which have been applied to diverse tasks. Yet, the query from the user is oftentimes short, which challenges the retrievers to correctly fetch relevant documents. To tackle this, previous studies have proposed expanding the query with a couple of additional (user-related) features related to it. However, they may be suboptimal to effectively augment the query, and there is plenty of other information available to augment it in a relational database. Motivated by this fact, we present a novel retrieval framework called Database-Augmented Query representation (DAQu), which augments the original query with various (query-related) metadata across multiple tables. In addition, as the number of features in the metadata can be very large and there is no order among them, we encode them with the graph-based set-encoding strategy, which considers hierarchies of features in the database without order. We validate our DAQu in diverse retrieval scenarios, demonstrating that it significantly enhances overall retrieval performance over relevant baselines.

## 🔍 Abstract (한글 번역)

arXiv:2406.16013v3 발표 유형: 교차 교체  
요약: 쿼리에 관련된 문서를 검색하려는 정보 검색 모델은 다양한 작업에 적용되어 여러 성공을 거두었습니다. 그러나 사용자의 쿼리는 종종 짧아서 검색자가 관련 문서를 올바르게 가져오는 데 어려움을 겪습니다. 이를 해결하기 위해 이전 연구에서는 쿼리와 관련된 몇 가지 추가적인 (사용자 관련) 기능으로 쿼리를 확장하는 방법을 제안했습니다. 그러나 이러한 방법은 쿼리를 효과적으로 확장하기에는 최적이 아닐 수 있으며, 관계형 데이터베이스에서 이를 확장할 수 있는 다양한 정보가 제공됩니다. 이러한 사실에 영감을 받아, 우리는 Database-Augmented Query representation (DAQu)라는 새로운 검색 프레임워크를 제안합니다. 이는 여러 테이블에 걸쳐 다양한 (쿼리 관련) 메타데이터로 원래 쿼리를 확장합니다. 또한, 메타데이터의 기능 수가 매우 많을 수 있고 그들 사이에 순서가 없기 때문에, 데이터베이스의 기능 계층을 순서 없이 고려하는 그래프 기반의 집합 인코딩 전략으로 이를 인코딩합니다. 우리는 다양한 검색 시나리오에서 DAQu를 검증하여 관련 기준선보다 전반적인 검색 성능을 크게 향상시킴을 입증합니다.

## 📝 요약

이 논문은 정보 검색 모델의 성능을 향상시키기 위해 제안된 새로운 프레임워크인 DAQu(Database-Augmented Query representation)를 소개합니다. 기존의 짧은 사용자 쿼리를 보완하기 위해 추가적인 사용자 관련 정보를 활용하는 방법이 있었으나, 이는 최적의 결과를 보장하지 못했습니다. DAQu는 여러 테이블의 메타데이터를 활용하여 쿼리를 확장하며, 그래프 기반의 집합 인코딩 전략을 통해 메타데이터의 계층 구조를 고려하여 인코딩합니다. 다양한 검색 시나리오에서 DAQu의 성능을 검증한 결과, 관련 기준 모델 대비 검색 성능이 크게 향상됨을 확인했습니다.

## 🎯 주요 포인트

- 1. 정보 검색 모델은 사용자의 짧은 쿼리로 인해 관련 문서를 정확히 검색하는 데 어려움을 겪습니다.

- 2. 기존 연구들은 쿼리를 확장하기 위해 사용자 관련 기능을 추가하는 방법을 제안했으나, 이는 최적의 방법이 아닐 수 있습니다.

- 3. DAQu(데이터베이스 확장 쿼리 표현)는 여러 테이블의 메타데이터를 활용하여 쿼리를 확장하는 새로운 검색 프레임워크입니다.

- 4. 메타데이터의 특징 수가 많고 순서가 없는 경우, 그래프 기반의 집합 인코딩 전략을 사용하여 데이터베이스 내 계층 구조를 고려합니다.

- 5. DAQu는 다양한 검색 시나리오에서 기존의 관련 기준선보다 검색 성능을 크게 향상시킵니다.

---

*Generated on 2025-09-22 14:36:15*