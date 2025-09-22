# Query Optimization for Parametric Knowledge Refinement in Retrieval-Augmented Large Language Models

**Korean Title:** 쿼리 최적화: 검색 증강 대형 언어 모델에서의 매개변수적 지식 정제

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/specific/Query Optimization|Query Optimization]] [[keywords/specific/Knowledge Distillation|Knowledge Distillation]] [[keywords/broad/Large Language Models|Large Language Models]] [[keywords/broad/Retrieval-Augmented Generation|Retrieval-Augmented Generation]] [[keywords/unique/Extract-Refine-Retrieve-Read Framework|Extract-Refine-Retrieve-Read Framework]] [[categories/cs.CL|cs.CL]] [[2025-09-18/KBM_ Delineating Knowledge Boundary for Adaptive Retrieval in Large Language Models_20250918|KBM: Delineating Knowledge Boundary for Adaptive Retrieval in Large Language Models]] (88.5% similar) [[2025-09-19/Select to Know_ An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering_20250919|Select to Know: An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering]] (86.8% similar) [[2025-09-22/Search and Refine During Think_ Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning_20250922|Search and Refine During Think: Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning]] (86.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Query Optimization, Knowledge Distillation
**🔬 Broad Technical**: Large Language Models, Retrieval-Augmented Generation
**⭐ Unique Technical**: Extract-Refine-Retrieve-Read Framework
## 🔗 유사한 논문
- [[2025-09-18/KBM_ Delineating Knowledge Boundary for Adaptive Retrieval in Large Language Models_20250918|KBM Delineating Knowledge Boundary for Adaptive Retrieval in Large Language Models]] (88.5% similar)
- [[2025-09-19/Select to Know_ An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering_20250919|Select to Know An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering]] (86.8% similar)
- [[2025-09-22/Search and Refine During Think_ Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning_20250922|Search and Refine During Think Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning]] (86.2% similar)
- [[2025-09-22/Temporal Reasoning with Large Language Models Augmented by Evolving Knowledge Graphs_20250922|Temporal Reasoning with Large Language Models Augmented by Evolving Knowledge Graphs]] (85.9% similar)
- [[2025-09-19/ImpRAG_ Retrieval-Augmented Generation with Implicit Queries_20250919|ImpRAG Retrieval-Augmented Generation with Implicit Queries]] (85.8% similar)


**ArXiv ID**: [2411.07820](https://arxiv.org/abs/2411.07820)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2411.07820.pdf)


**ArXiv ID**: [2411.07820](https://arxiv.org/abs/2411.07820)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2411.07820.pdf)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Query Optimization, Knowledge Distillation
**⭐ Unique Technical**: Extract-Refine-Retrieve-Read Framework
**🔬 Broad Technical**: Large Language Models, Retrieval-Augmented Generation

## 🏷️ 추출된 키워드



`Large Language Models` • 

`Retrieval-Augmented Generation` • 

`Query Optimization` • 

`Knowledge Distillation` • 

`Extract-Refine-Retrieve-Read Framework`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2411.07820v4 Announce Type: replace 
Abstract: We introduce the \textit{Extract-Refine-Retrieve-Read} (ERRR) framework, a novel approach designed to bridge the pre-retrieval information gap in Retrieval-Augmented Generation (RAG) systems through query optimization tailored to meet the specific knowledge requirements of Large Language Models (LLMs). Unlike conventional query optimization techniques used in RAG, the ERRR framework begins by extracting parametric knowledge from LLMs, followed by using a specialized query optimizer for refining these queries. This process ensures the retrieval of only the most pertinent information essential for generating accurate responses. Moreover, to enhance flexibility and reduce computational costs, we propose a trainable scheme for our pipeline that utilizes a smaller, tunable model as the query optimizer, which is refined through knowledge distillation from a larger teacher model. Our evaluations on various question-answering (QA) datasets and with different retrieval systems show that ERRR consistently outperforms existing baselines, proving to be a versatile and cost-effective module for improving the utility and accuracy of RAG systems.

## 🔍 Abstract (한글 번역)

arXiv:2411.07820v4 발표 유형: 교체  
초록: 우리는 \textit{Extract-Refine-Retrieve-Read} (ERRR) 프레임워크를 소개합니다. 이 새로운 접근 방식은 대규모 언어 모델(LLM)의 특정 지식 요구를 충족시키기 위해 쿼리 최적화를 통해 검색 보강 생성(RAG) 시스템의 사전 검색 정보 격차를 해소하도록 설계되었습니다. RAG에서 사용되는 기존의 쿼리 최적화 기술과 달리, ERRR 프레임워크는 LLM에서 매개변수 지식을 추출하는 것으로 시작하여 이러한 쿼리를 정제하기 위해 특수한 쿼리 최적화기를 사용합니다. 이 과정은 정확한 응답 생성을 위해 필수적인 가장 관련성 높은 정보만 검색되도록 보장합니다. 또한, 유연성을 높이고 계산 비용을 줄이기 위해, 우리는 더 작은 조정 가능한 모델을 쿼리 최적화기로 활용하는 훈련 가능한 방식을 제안하며, 이는 더 큰 교사 모델로부터의 지식 증류를 통해 정제됩니다. 다양한 질문-응답(QA) 데이터셋과 다양한 검색 시스템에 대한 우리의 평가에서 ERRR은 기존의 기준선을 지속적으로 능가하며, RAG 시스템의 유용성과 정확성을 향상시키는 다재다능하고 비용 효율적인 모듈임을 입증합니다.

## 📝 요약

이 논문에서는 대규모 언어 모델(LLM)의 지식 요구 사항을 충족하기 위해 쿼리를 최적화하는 \textit{Extract-Refine-Retrieve-Read} (ERRR) 프레임워크를 제안합니다. ERRR는 기존의 정보 검색 강화 생성(RAG) 시스템의 쿼리 최적화 방식과 달리, LLM에서 파라메트릭 지식을 추출하고 이를 정제하여 가장 관련성 높은 정보를 검색합니다. 또한, ERRR는 작은 모델을 쿼리 최적화에 활용하여 유연성을 높이고 비용을 절감하며, 큰 모델로부터 지식 증류를 통해 정제합니다. 다양한 QA 데이터셋과 검색 시스템 평가에서 ERRR는 기존 기법보다 뛰어난 성능을 보였습니다.

## 🎯 주요 포인트


- 1. ERRR 프레임워크는 대형 언어 모델(LLM)의 특정 지식 요구 사항을 충족하기 위해 쿼리 최적화를 통해 검색 증강 생성(RAG) 시스템의 사전 검색 정보 격차를 해소하는 새로운 접근 방식입니다.

- 2. ERRR는 LLM에서 파라메트릭 지식을 추출한 후, 이를 정제하기 위한 전문화된 쿼리 최적화기를 사용하여 가장 관련성이 높은 정보를 검색합니다.

- 3. ERRR 프레임워크는 작은 튜닝 가능한 모델을 쿼리 최적화기로 사용하고, 이를 더 큰 교사 모델로부터 지식 증류를 통해 정제하여 유연성을 높이고 계산 비용을 줄입니다.

- 4. 다양한 질문-응답(QA) 데이터셋과 검색 시스템을 통한 평가에서 ERRR은 기존의 기준선을 일관되게 능가하여 RAG 시스템의 유용성과 정확성을 향상시키는 다재다능하고 비용 효율적인 모듈임을 입증했습니다.


---

*Generated on 2025-09-22 16:32:52*