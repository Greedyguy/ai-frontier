---
keywords:
  - Poisoning Attacks
  - Retrieval-Augmented Generation
  - Responsibility Attribution
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:42:27.771024",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Poisoning Attacks",
    "Retrieval-Augmented Generation",
    "Responsibility Attribution"
  ],
  "rejected_keywords": [
    "Large Language Models",
    "Unsupervised Clustering"
  ],
  "similarity_scores": {
    "Poisoning Attacks": 0.85,
    "Retrieval-Augmented Generation": 0.8,
    "Responsibility Attribution": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Who Taught the Lie? Responsibility Attribution for Poisoned Knowledge in Retrieval-Augmented Generation

**Korean Title:** "누가 거짓을 가르쳤는가? 검색 증강 생성에서 오염된 지식에 대한 책임 귀속"

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Poisoning Attacks|Poisoning Attacks]]
**⚡ Unique Technical**: [[keywords/Retrieval-Augmented Generation|Retrieval-Augmented Generation]], [[keywords/Responsibility Attribution|Responsibility Attribution]]

## 🔗 유사한 논문
- [[Enhancing Retrieval Augmentation via Adversarial Collaboration_20250919|Enhancing Retrieval Augmentation via Adversarial Collaboration]] (84.9% similar)
- [[AIP_ Subverting Retrieval-Augmented Generation via Adversarial Instructional Prompt_20250919|AIP Subverting Retrieval-Augmented Generation via Adversarial Instructional Prompt]] (84.8% similar)
- [[Causal-Counterfactual RAG_ The Integration of Causal-Counterfactual Reasoning into RAG_20250919|Causal-Counterfactual RAG The Integration of Causal-Counterfactual Reasoning into RAG]] (83.4% similar)
- [[Engineering RAG Systems for Real-World Applications_ Design, Development, and Evaluation_20250919|Engineering RAG Systems for Real-World Applications Design, Development, and Evaluation]] (83.2% similar)
- [[GRADA_ Graph-based Reranking against Adversarial Documents Attack_20250919|GRADA Graph-based Reranking against Adversarial Documents Attack]] (83.0% similar)

## 📋 저자 정보

**Authors:** Baolei Zhang, Haoran Xin, Yuxi Chen, Zhuqing Liu, Biao Yi, Tong Li, Lihai Nie, Zheli Liu, Minghong Fang

## 📄 Abstract (원문)

Retrieval-Augmented Generation (RAG) integrates external knowledge into large
language models to improve response quality. However, recent work has shown
that RAG systems are highly vulnerable to poisoning attacks, where malicious
texts are inserted into the knowledge database to influence model outputs.
While several defenses have been proposed, they are often circumvented by more
adaptive or sophisticated attacks.
  This paper presents RAGOrigin, a black-box responsibility attribution
framework designed to identify which texts in the knowledge database are
responsible for misleading or incorrect generations. Our method constructs a
focused attribution scope tailored to each misgeneration event and assigns a
responsibility score to each candidate text by evaluating its retrieval
ranking, semantic relevance, and influence on the generated response. The
system then isolates poisoned texts using an unsupervised clustering method. We
evaluate RAGOrigin across seven datasets and fifteen poisoning attacks,
including newly developed adaptive poisoning strategies and multi-attacker
scenarios. Our approach outperforms existing baselines in identifying poisoned
content and remains robust under dynamic and noisy conditions. These results
suggest that RAGOrigin provides a practical and effective solution for tracing
the origins of corrupted knowledge in RAG systems.

## 🔍 Abstract (한글 번역)

검색 증강 생성(Retrieval-Augmented Generation, RAG)은 외부 지식을 대형 언어 모델에 통합하여 응답 품질을 향상시킵니다. 그러나 최근 연구에 따르면 RAG 시스템은 지식 데이터베이스에 악의적인 텍스트를 삽입하여 모델 출력을 조작하는 중독 공격에 매우 취약합니다. 여러 방어책이 제안되었지만, 이러한 방어책은 종종 더 적응적이거나 정교한 공격에 의해 우회됩니다.

이 논문은 오도되거나 잘못된 생성에 책임이 있는 지식 데이터베이스의 텍스트를 식별하기 위해 설계된 블랙박스 책임 귀속 프레임워크인 RAGOrigin을 제시합니다. 우리의 방법은 각 잘못된 생성 이벤트에 맞춘 집중적인 귀속 범위를 구성하고, 검색 순위, 의미적 관련성, 생성된 응답에 대한 영향을 평가하여 각 후보 텍스트에 책임 점수를 부여합니다. 그런 다음 시스템은 비지도 클러스터링 방법을 사용하여 중독된 텍스트를 분리합니다. 우리는 RAGOrigin을 일곱 개의 데이터셋과 열다섯 개의 중독 공격, 새로 개발된 적응형 중독 전략 및 다중 공격자 시나리오를 포함하여 평가합니다. 우리의 접근 방식은 중독된 콘텐츠를 식별하는 데 있어 기존의 기준선을 능가하며, 동적이고 소음이 많은 조건에서도 견고함을 유지합니다. 이러한 결과는 RAGOrigin이 RAG 시스템에서 손상된 지식의 출처를 추적하는 실용적이고 효과적인 솔루션을 제공함을 시사합니다.

## 📝 요약

RAGOrigin은 외부 지식을 통합한 대형 언어 모델인 RAG 시스템의 취약점을 보완하기 위해 개발된 책임 귀속 프레임워크입니다. 이 시스템은 지식 데이터베이스 내에서 잘못된 생성 결과를 유발하는 텍스트를 식별합니다. 각 오류 발생 시점에 맞춰 특정 귀속 범위를 설정하고, 후보 텍스트의 검색 순위, 의미적 관련성, 생성 응답에 대한 영향을 평가하여 책임 점수를 부여합니다. 이후 비지도 학습 클러스터링 방법을 통해 악의적인 텍스트를 분리합니다. RAGOrigin은 7개의 데이터셋과 15개의 공격 시나리오에서 기존 방법보다 우수한 성능을 보였으며, 동적이고 잡음이 많은 환경에서도 견고함을 입증했습니다. 이를 통해 RAG 시스템의 손상된 지식 출처를 추적하는 실용적이고 효과적인 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. RAG 시스템은 외부 지식을 통합하여 응답 품질을 향상시키지만, 악의적인 텍스트 삽입 공격에 취약합니다.

- 2. RAGOrigin은 잘못된 생성의 원인이 되는 지식 데이터베이스의 텍스트를 식별하는 블랙박스 책임 할당 프레임워크입니다.

- 3. RAGOrigin은 각 잘못된 생성 이벤트에 맞춘 집중적인 책임 범위를 구축하고, 텍스트의 검색 순위, 의미적 관련성, 생성된 응답에 대한 영향을 평가하여 책임 점수를 할당합니다.

- 4. 비지도 클러스터링 방법을 사용하여 중독된 텍스트를 분리하며, 7개의 데이터셋과 15개의 중독 공격 시나리오에서 평가되었습니다.

- 5. RAGOrigin은 기존의 기준선을 능가하며, 동적이고 소음이 많은 조건에서도 강력한 성능을 유지합니다.

---

*Generated on 2025-09-20 09:34:29*