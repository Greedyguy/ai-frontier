
# ImpRAG: Retrieval-Augmented Generation with Implicit Queries

**Korean Title:** ImpRAG: 암묵적 쿼리를 활용한 검색 증강 생성

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Query-free RAG

## 🔗 유사한 논문
- [[Enhancing Retrieval Augmentation via Adversarial Collaboration_20250919|Enhancing Retrieval Augmentation via Adversarial Collaboration]] (87.3% similar)
- [[AIP Subverting Retrieval-Augmented Generation via Adversarial Instructional Prompt]] (86.2% similar)
- [[Causal-Counterfactual RAG The Integration of Causal-Counterfactual Reasoning into RAG]] (85.7% similar)
- [[KBM Delineating Knowledge Boundary for Adaptive Retrieval in Large Language Models]] (84.7% similar)
- [[Engineering RAG Systems for Real-World Applications Design, Development, and Evaluation]] (83.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.02279v2 Announce Type: replace 
Abstract: Retrieval-Augmented Generation (RAG) systems traditionally treat retrieval and generation as separate processes, requiring explicit textual queries to connect them. This separation can limit the ability of models to generalize across diverse tasks. In this work, we propose a query-free RAG system, named ImpRAG, which integrates retrieval and generation into a unified model. ImpRAG allows models to implicitly express their information needs, eliminating the need for human-specified queries. By dividing pretrained decoder-only language models into specialized layer groups, ImpRAG optimizes retrieval and generation tasks simultaneously. Our approach employs a two-stage inference process, using the same model parameters and forward pass for both retrieval and generation, thereby minimizing the disparity between retrievers and language models. Experiments on 8 knowledge-intensive tasks demonstrate that ImpRAG achieves 3.6-11.5 improvements in exact match scores on unseen tasks with diverse formats, highlighting its effectiveness in enabling models to articulate their own information needs and generalize across tasks. Our analysis underscores the importance of balancing retrieval and generation parameters and leveraging generation perplexities as retrieval training objectives for enhanced performance.

## 🔍 Abstract (한글 번역)

arXiv:2506.02279v2 발표 유형: 교체  
초록: 검색-증강 생성(Retrieval-Augmented Generation, RAG) 시스템은 전통적으로 검색과 생성을 별개의 과정으로 취급하며, 이를 연결하기 위해 명시적인 텍스트 쿼리가 필요합니다. 이러한 분리는 모델이 다양한 작업에 대해 일반화하는 능력을 제한할 수 있습니다. 본 연구에서는 검색과 생성을 통합된 모델로 결합한 쿼리 없는 RAG 시스템, ImpRAG를 제안합니다. ImpRAG는 모델이 정보 요구를 암묵적으로 표현할 수 있게 하여, 사람이 지정한 쿼리의 필요성을 제거합니다. 사전 학습된 디코더 전용 언어 모델을 특화된 레이어 그룹으로 나누어, ImpRAG는 검색과 생성 작업을 동시에 최적화합니다. 우리의 접근법은 동일한 모델 파라미터와 전방 패스를 사용하여 검색과 생성을 수행하는 2단계 추론 과정을 채택하여, 검색기와 언어 모델 간의 차이를 최소화합니다. 8개의 지식 집약적 작업에 대한 실험 결과, ImpRAG는 다양한 형식의 보지 못한 작업에서 정확한 일치 점수가 3.6-11.5 향상되었음을 보여주며, 모델이 자체 정보 요구를 명확히 표현하고 작업 간 일반화할 수 있는 능력을 강조합니다. 우리의 분석은 검색과 생성 파라미터의 균형을 맞추는 것과 생성 당혹도를 검색 훈련 목표로 활용하는 것이 성능 향상에 중요함을 강조합니다.

## 📝 요약

이 논문에서는 검색과 생성을 통합한 쿼리 없는 RAG 시스템인 ImpRAG를 제안합니다. ImpRAG는 사전 훈련된 디코더 전용 언어 모델을 특화된 레이어 그룹으로 나누어 검색과 생성 작업을 동시에 최적화합니다. 이를 통해 모델이 명시적 쿼리 없이도 정보 요구를 표현할 수 있게 하여 다양한 작업에 대한 일반화 능력을 향상시킵니다. 8개의 지식 집약적 작업 실험에서 ImpRAG는 새로운 작업에서 3.6-11.5의 정확도 향상을 보여주었으며, 검색과 생성 매개변수의 균형과 생성 당혹도를 검색 훈련 목표로 활용하는 것이 성능 향상에 중요함을 강조합니다.

## 🎯 주요 포인트

- 1. ImpRAG는 검색과 생성을 통합하여 명시적인 텍스트 쿼리 없이 정보 검색과 생성을 수행하는 시스템입니다.

- 2. 사전 훈련된 디코더 전용 언어 모델을 특화된 레이어 그룹으로 나누어 검색과 생성 작업을 동시에 최적화합니다.

- 3. 동일한 모델 파라미터와 전방 패스를 사용하여 검색과 생성을 수행하는 2단계 추론 과정을 채택합니다.

- 4. 8개의 지식 집약적 작업 실험에서 미지의 작업에 대해 정확한 일치 점수가 3.6-11.5 향상되었습니다.

- 5. 검색과 생성 매개변수의 균형을 맞추고 생성 당혹도를 검색 훈련 목표로 활용하는 것이 성능 향상에 중요합니다.

---

*Generated on 2025-09-19 16:00:29*