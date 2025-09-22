# KITE: Kernelized and Information Theoretic Exemplars for In-Context Learning

**Korean Title:** KITE: 문맥 내 학습을 위한 커널화 및 정보 이론적 예제들

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: In-Context Learning, Kernel Trick

## 🔗 유사한 논문
- [[2025-09-18/TICL_ Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models_20250918|TICL Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models]] (84.4% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (83.4% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning An Indispensable Path towards New-Generation Large Language Models]] (82.5% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (82.1% similar)
- [[2025-09-22/Efficient and Versatile Model for Multilingual Information Retrieval of Islamic Text_ Development and Deployment in Real-World Scenarios_20250922|Efficient and Versatile Model for Multilingual Information Retrieval of Islamic Text Development and Deployment in Real-World Scenarios]] (81.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15676v1 Announce Type: cross 
Abstract: In-context learning (ICL) has emerged as a powerful paradigm for adapting large language models (LLMs) to new and data-scarce tasks using only a few carefully selected task-specific examples presented in the prompt. However, given the limited context size of LLMs, a fundamental question arises: Which examples should be selected to maximize performance on a given user query? While nearest-neighbor-based methods like KATE have been widely adopted for this purpose, they suffer from well-known drawbacks in high-dimensional embedding spaces, including poor generalization and a lack of diversity. In this work, we study this problem of example selection in ICL from a principled, information theory-driven perspective. We first model an LLM as a linear function over input embeddings and frame the example selection task as a query-specific optimization problem: selecting a subset of exemplars from a larger example bank that minimizes the prediction error on a specific query. This formulation departs from traditional generalization-focused learning theoretic approaches by targeting accurate prediction for a specific query instance. We derive a principled surrogate objective that is approximately submodular, enabling the use of a greedy algorithm with an approximation guarantee. We further enhance our method by (i) incorporating the kernel trick to operate in high-dimensional feature spaces without explicit mappings, and (ii) introducing an optimal design-based regularizer to encourage diversity in the selected examples. Empirically, we demonstrate significant improvements over standard retrieval methods across a suite of classification tasks, highlighting the benefits of structure-aware, diverse example selection for ICL in real-world, label-scarce scenarios.

## 🔍 Abstract (한글 번역)

arXiv:2509.15676v1 발표 유형: 교차  
초록: 문맥 학습(In-context learning, ICL)은 대형 언어 모델(LLMs)을 새로운 데이터가 부족한 작업에 적응시키기 위한 강력한 패러다임으로 부상하고 있으며, 프롬프트에 제시된 몇 가지 신중하게 선택된 작업별 예시만을 사용합니다. 그러나 LLM의 제한된 문맥 크기를 고려할 때, 근본적인 질문이 제기됩니다: 주어진 사용자 쿼리에 대한 성능을 극대화하기 위해 어떤 예시를 선택해야 할까요? KATE와 같은 최근접 이웃 기반 방법이 이 목적을 위해 널리 채택되었지만, 고차원 임베딩 공간에서 일반화 부족과 다양성 결여와 같은 잘 알려진 단점을 가지고 있습니다. 본 연구에서는 정보 이론에 기반한 원칙적인 관점에서 ICL에서의 예시 선택 문제를 연구합니다. 우리는 먼저 LLM을 입력 임베딩에 대한 선형 함수로 모델링하고, 예시 선택 작업을 특정 쿼리에 대한 최적화 문제로 구성합니다: 특정 쿼리에 대한 예측 오류를 최소화하는 더 큰 예시 은행에서 예시의 부분 집합을 선택하는 것입니다. 이 공식은 특정 쿼리 인스턴스에 대한 정확한 예측을 목표로 함으로써 전통적인 일반화 중심의 학습 이론적 접근 방식에서 벗어납니다. 우리는 근사적으로 부분 모듈러인 원칙적인 대리 목표를 도출하여 근사 보장이 있는 탐욕 알고리즘을 사용할 수 있게 합니다. 또한, (i) 명시적 매핑 없이 고차원 특징 공간에서 작동할 수 있도록 커널 트릭을 통합하고, (ii) 선택된 예시의 다양성을 장려하기 위해 최적 설계 기반 정규화를 도입하여 방법을 향상시킵니다. 실험적으로, 우리는 다양한 분류 작업에서 표준 검색 방법에 비해 상당한 개선을 보여주며, 실제 세계의 라벨이 부족한 시나리오에서 ICL을 위한 구조 인식적이고 다양한 예시 선택의 이점을 강조합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)을 새로운 데이터 부족 과제에 적응시키기 위한 강력한 패러다임인 문맥 내 학습(ICL)의 예제 선택 문제를 정보 이론적 관점에서 연구합니다. LLM의 제한된 문맥 크기 내에서 최적의 성능을 발휘할 수 있는 예제를 선택하는 것이 핵심 과제입니다. 기존의 최근접 이웃 기반 방법들은 고차원 임베딩 공간에서 일반화 부족과 다양성 결여 문제를 겪습니다. 본 연구는 LLM을 입력 임베딩에 대한 선형 함수로 모델링하고, 특정 쿼리에 대한 예측 오류를 최소화하는 예제 선택 문제를 최적화 문제로 정의합니다. 이를 통해 근사적으로 부분 모듈러한 대리 목표를 도출하고, 탐욕 알고리즘을 사용하여 효율적인 예제 선택을 가능하게 합니다. 또한 고차원 특징 공간에서 커널 트릭을 사용하고, 최적 설계 기반 정규화를 도입하여 선택된 예제의 다양성을 촉진합니다. 실험 결과, 다양한 분류 작업에서 표준 검색 방법보다 성능이 크게 향상됨을 보여주며, 구조를 고려한 다양한 예제 선택의 중요성을 강조합니다.

## 🎯 주요 포인트

- 1. In-context learning (ICL)은 대형 언어 모델(LLM)을 새로운 데이터가 부족한 작업에 적응시키는 강력한 패러다임으로 부상하고 있다.

- 2. LLM의 제한된 컨텍스트 크기 때문에, 사용자 쿼리에 대한 성능을 극대화하기 위해 어떤 예제를 선택해야 하는지가 중요한 문제로 대두된다.

- 3. 본 연구는 정보 이론 기반의 관점에서 ICL에서의 예제 선택 문제를 다루며, 쿼리별 최적화 문제로 예제 선택을 모델링한다.

- 4. 서브모듈러 근사 보장을 제공하는 탐욕 알고리즘을 사용하여 예제 선택을 최적화하며, 커널 트릭과 최적 설계 기반의 정규화를 도입하여 다양성을 촉진한다.

- 5. 다양한 분류 작업에서 표준 검색 방법에 비해 성능이 크게 향상되었음을 실증적으로 보여주며, ICL에서의 구조 인식 및 다양한 예제 선택의 이점을 강조한다.

---

*Generated on 2025-09-22 14:08:13*