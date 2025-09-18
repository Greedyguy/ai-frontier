
# Who Taught the Lie? Responsibility Attribution for Poisoned Knowledge in Retrieval-Augmented Generation

**Korean Title:** 거짓을 가르친 사람은 누구인가? 검색 증강 생성에서 중독된 지식에 대한 책임 귀속

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Adaptive Poisoning Strategies|Adaptive Poisoning Strategies]] [[keywords/broad/Retrieval-Augmented Generation|Retrieval-Augmented Generation]] [[keywords/broad/Poisoning Attacks|Poisoning Attacks]] [[keywords/specific/RAGOrigin|RAGOrigin]] [[keywords/unique/RAGOrigin|RAGOrigin]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Adaptive Poisoning Strategies
**🔬 Broad Technical**: Retrieval-Augmented Generation, Poisoning Attacks
**🔗 Specific Connectable**: RAGOrigin
**⭐ Unique Technical**: RAGOrigin

**ArXiv ID**: [2509.13772](https://arxiv.org/abs/2509.13772)
**Published**: 2025-09-18
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.13772.pdf)


## 🏷️ 추출된 키워드



`Retrieval-Augmented Generation` • 

`Poisoning Attacks` • 

`RAGOrigin` • 

`RAGOrigin` • 

`Adaptive Poisoning Strategies`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13772v1 Announce Type: cross 
Abstract: Retrieval-Augmented Generation (RAG) integrates external knowledge into large language models to improve response quality. However, recent work has shown that RAG systems are highly vulnerable to poisoning attacks, where malicious texts are inserted into the knowledge database to influence model outputs. While several defenses have been proposed, they are often circumvented by more adaptive or sophisticated attacks.
  This paper presents RAGOrigin, a black-box responsibility attribution framework designed to identify which texts in the knowledge database are responsible for misleading or incorrect generations. Our method constructs a focused attribution scope tailored to each misgeneration event and assigns a responsibility score to each candidate text by evaluating its retrieval ranking, semantic relevance, and influence on the generated response. The system then isolates poisoned texts using an unsupervised clustering method. We evaluate RAGOrigin across seven datasets and fifteen poisoning attacks, including newly developed adaptive poisoning strategies and multi-attacker scenarios. Our approach outperforms existing baselines in identifying poisoned content and remains robust under dynamic and noisy conditions. These results suggest that RAGOrigin provides a practical and effective solution for tracing the origins of corrupted knowledge in RAG systems.

## 🔍 Abstract (한글 번역)

arXiv:2509.13772v1 발표 유형: 교차
요약: 검색 증강 생성(RAG)은 외부 지식을 대규모 언어 모델에 통합하여 응답 품질을 향상시키는 기술입니다. 그러나 최근 연구에 따르면, RAG 시스템은 악의적인 텍스트가 지식 데이터베이스에 삽입되어 모델 출력에 영향을 미치는 독립성 공격에 매우 취약합니다. 여러 방어책이 제안되었지만, 더 적응적이거나 정교한 공격에 의해 종종 우회됩니다.
본 논문은 RAGOrigin이라는 블랙박스 책임 할당 프레임워크를 제시하여, 지식 데이터베이스의 어떤 텍스트가 잘못된 생성에 책임을 지는지 식별하도록 설계되었습니다. 우리의 방법은 각 잘못된 생성 이벤트에 맞춘 집중된 책임 할당 범위를 구성하고, 검색 순위, 의미적 관련성 및 생성된 응답에 미치는 영향을 평가하여 각 후보 텍스트에 책임 점수를 할당합니다. 시스템은 그런 후 독립적인 클러스터링 방법을 사용하여 독립된 텍스트를 분리합니다. 우리는 RAGOrigin을 일곱 개의 데이터셋과 십오 개의 독립성 공격을 포함한 새로 개발된 적응적 독립성 전략 및 다중 공격자 시나리오를 통해 평가합니다. 우리의 접근 방식은 독립적인 콘텐츠를 식별하는 데 기존의 기준선을 능가하며, 동적이고 소음이 많은 조건 하에서도 견고함을 유지합니다. 이러한 결과는 RAG 시스템에서 오염된 지식의 원천을 추적하는 실용적이고 효과적인 해결책을 제공하는 RAGOrigin을 시사합니다.

## 📝 요약

이 연구는 외부 지식을 대규모 언어 모델에 통합하여 응답 품질을 향상시키는 Retrieval-Augmented Generation (RAG)이 악의적인 텍스트가 지식 데이터베이스에 삽입되어 모델 출력에 영향을 미치는 독성 공격에 매우 취약하다는 것을 보여준다. 본 논문은 RAGOrigin이라는 블랙박스 책임 귀속 프레임워크를 제안하여 잘못된 생성물에 책임을 지는 지식 데이터베이스의 텍스트를 식별한다. 우리의 방법론은 각 오분류 이벤트에 맞춘 집중된 귀속 범위를 구성하고, 검색 랭킹, 의미적 관련성 및 생성된 응답에 미치는 영향을 평가하여 각 후보 텍스트에 책임 점수를 할당한다. 시스템은 그런 다음 비지도 클러스터링 방법을 사용하여 독성 텍스트를 격리한다. 우리는 RAGOrigin을 일곱 개의 데이터셋과 십오 개의 독성 공격을 포함한 새로 개발된 적응적 독성 전략 및 다중 공격자 시나리오를 통해 평가한다. 우리의 접근 방식은 독성 콘텐츠를 식별하는 데 기존 기준을 능가하며 동적이고 소음이 있는 조건에서도 견고함을 유지한다. 이러한 결과는 RAG 시스템에서 오염된 지식의 원천을 추적하는 실용적이고 효과적인 해결책을 제공한다는 것을 시사한다.

## 🎯 주요 포인트


- 1. 외부 지식을 통합하여 응답 품질을 향상시키는 RAG 시스템은 독성 공격에 매우 취약하다.

- 2. RAGOrigin은 오도된 지식의 원천을 식별하기 위한 검은 상자 책임 할당 프레임워크를 제시한다.

- 3. 우리의 방법은 독성 텍스트를 식별하기 위해 검색 순위, 의미적 관련성 및 영향력을 평가하여 책임 점수를 할당한다.


---

*Generated on 2025-09-18 16:43:49*