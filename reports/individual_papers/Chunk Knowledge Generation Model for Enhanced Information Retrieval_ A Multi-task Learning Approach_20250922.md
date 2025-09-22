# Chunk Knowledge Generation Model for Enhanced Information Retrieval: A Multi-task Learning Approach

**Korean Title:** 향상된 정보 검색을 위한 청크 지식 생성 모델: 다중 과제 학습 접근법

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Multi-task Learning, Query Expansion

## 🔗 유사한 논문
- [[2025-09-19/ImpRAG_ Retrieval-Augmented Generation with Implicit Queries_20250919|ImpRAG Retrieval-Augmented Generation with Implicit Queries]] (84.2% similar)
- [[2025-09-22/Relevance to Utility_ Process-Supervised Rewrite for RAG_20250922|Relevance to Utility Process-Supervised Rewrite for RAG]] (84.0% similar)
- [[2025-09-19/Select to Know_ An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering_20250919|Select to Know An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering]] (83.6% similar)
- [[2025-09-18/KBM_ Delineating Knowledge Boundary for Adaptive Retrieval in Large Language Models_20250918|KBM Delineating Knowledge Boundary for Adaptive Retrieval in Large Language Models]] (82.7% similar)
- [[2025-09-19/Graph-Enhanced Retrieval-Augmented Question Answering for E-Commerce Customer Support_20250919|Graph-Enhanced Retrieval-Augmented Question Answering for E-Commerce Customer Support]] (82.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15658v1 Announce Type: cross 
Abstract: Traditional query expansion techniques for addressing vocabulary mismatch problems in information retrieval are context-sensitive and may lead to performance degradation. As an alternative, document expansion research has gained attention, but existing methods such as Doc2Query have limitations including excessive preprocessing costs, increased index size, and reliability issues with generated content. To mitigate these problems and seek more structured and efficient alternatives, this study proposes a method that divides documents into chunk units and generates textual data for each chunk to simultaneously improve retrieval efficiency and accuracy. The proposed "Chunk Knowledge Generation Model" adopts a T5-based multi-task learning structure that simultaneously generates titles and candidate questions from each document chunk while extracting keywords from user queries. This approach maximizes computational efficiency by generating and extracting three types of semantic information in parallel through a single encoding and two decoding processes. The generated data is utilized as additional information in the retrieval system. GPT-based evaluation on 305 query-document pairs showed that retrieval using the proposed model achieved 95.41% accuracy at Top@10, demonstrating superior performance compared to document chunk-level retrieval. This study contributes by proposing an approach that simultaneously generates titles and candidate questions from document chunks for application in retrieval pipelines, and provides empirical evidence applicable to large-scale information retrieval systems by demonstrating improved retrieval accuracy through qualitative evaluation.

## 🔍 Abstract (한글 번역)

arXiv:2509.15658v1 발표 유형: 교차  
초록: 정보 검색에서 어휘 불일치 문제를 해결하기 위한 전통적인 쿼리 확장 기법은 문맥에 민감하여 성능 저하를 초래할 수 있습니다. 이에 대한 대안으로 문서 확장 연구가 주목받고 있지만, Doc2Query와 같은 기존 방법은 과도한 전처리 비용, 증가된 인덱스 크기, 생성된 콘텐츠의 신뢰성 문제 등의 한계를 가지고 있습니다. 이러한 문제를 완화하고 보다 구조적이고 효율적인 대안을 모색하기 위해, 본 연구는 문서를 청크 단위로 나누고 각 청크에 대한 텍스트 데이터를 생성하여 검색 효율성과 정확성을 동시에 향상시키는 방법을 제안합니다. 제안된 "청크 지식 생성 모델"은 T5 기반의 멀티태스크 학습 구조를 채택하여 각 문서 청크에서 제목과 후보 질문을 생성하는 동시에 사용자 쿼리에서 키워드를 추출합니다. 이 접근 방식은 단일 인코딩과 두 개의 디코딩 프로세스를 통해 세 가지 유형의 의미 정보를 병렬로 생성하고 추출하여 계산 효율성을 극대화합니다. 생성된 데이터는 검색 시스템에서 추가 정보로 활용됩니다. 305개의 쿼리-문서 쌍에 대한 GPT 기반 평가에서 제안된 모델을 사용한 검색이 Top@10에서 95.41%의 정확도를 달성하여 문서 청크 수준의 검색보다 우수한 성능을 보여주었습니다. 본 연구는 검색 파이프라인에 적용하기 위해 문서 청크에서 제목과 후보 질문을 동시에 생성하는 접근 방식을 제안하고, 질적 평가를 통해 검색 정확도가 향상됨을 입증하여 대규모 정보 검색 시스템에 적용 가능한 실증적 증거를 제공합니다.

## 📝 요약

이 연구는 정보 검색에서 어휘 불일치 문제를 해결하기 위해 전통적인 질의 확장 기법 대신 문서 확장 접근법을 제안합니다. 기존 방법의 한계를 극복하기 위해 문서를 청크 단위로 나누고, 각 청크에서 제목과 후보 질문을 생성하는 "청크 지식 생성 모델"을 제안합니다. 이 모델은 T5 기반의 멀티태스크 학습 구조를 사용하여 사용자 질의에서 키워드를 추출하고, 단일 인코딩과 두 개의 디코딩 과정을 통해 효율적으로 세 가지 의미 정보를 생성합니다. 생성된 데이터는 검색 시스템에서 추가 정보로 활용되며, GPT 기반 평가에서 Top@10에서 95.41%의 정확도를 기록하여 우수한 성능을 입증했습니다. 이 연구는 대규모 정보 검색 시스템에서 검색 정확도를 향상시키는 방법론을 제시하고, 질적 평가를 통해 그 효과를 입증합니다.

## 🎯 주요 포인트

- 1. 기존의 쿼리 확장 기법은 문맥에 민감하여 성능 저하를 초래할 수 있으며, 이를 대체하기 위해 문서 확장 연구가 주목받고 있습니다.

- 2. 제안된 "청크 지식 생성 모델"은 T5 기반의 멀티태스크 학습 구조를 채택하여 문서 청크에서 제목과 후보 질문을 생성하고 사용자 쿼리에서 키워드를 추출합니다.

- 3. 이 모델은 단일 인코딩과 두 개의 디코딩 과정을 통해 세 가지 유형의 의미 정보를 병렬로 생성 및 추출하여 계산 효율성을 극대화합니다.

- 4. 제안된 모델을 사용한 검색은 305개의 쿼리-문서 쌍에서 Top@10 기준 95.41%의 정확도를 달성하여 문서 청크 수준 검색보다 우수한 성능을 보였습니다.

- 5. 본 연구는 문서 청크에서 제목과 후보 질문을 동시에 생성하는 접근 방식을 제안하고, 대규모 정보 검색 시스템에 적용 가능한 경험적 증거를 제공합니다.

---

*Generated on 2025-09-22 14:06:46*