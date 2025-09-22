
# GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search

**Korean Title:** GASLITEing 검색: 밀집 임베딩 기반 검색의 취약점 탐구

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Adversarial Passage Generation

## 🔗 유사한 논문
- [[When Content is Goliath and Algorithm is David The Style and Semantic Effects of Generative Search Engine]] (82.3% similar)
- [[AIP Subverting Retrieval-Augmented Generation via Adversarial Instructional Prompt]] (81.4% similar)
- [[Enhancing Retrieval Augmentation via Adversarial Collaboration_20250919|Enhancing Retrieval Augmentation via Adversarial Collaboration]] (81.3% similar)
- [[GRADA Graph-based Reranking against Adversarial Documents Attack]] (81.3% similar)
- [[ImpRAG Retrieval-Augmented Generation with Implicit Queries]] (80.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2412.20953v2 Announce Type: replace-cross 
Abstract: Dense embedding-based text retrieval$\unicode{x2013}$retrieval of relevant passages from corpora via deep learning encodings$\unicode{x2013}$has emerged as a powerful method attaining state-of-the-art search results and popularizing Retrieval Augmented Generation (RAG). Still, like other search methods, embedding-based retrieval may be susceptible to search-engine optimization (SEO) attacks, where adversaries promote malicious content by introducing adversarial passages to corpora. Prior work has shown such SEO is feasible, mostly demonstrating attacks against retrieval-integrated systems (e.g., RAG). Yet, these consider relaxed SEO threat models (e.g., targeting single queries), use baseline attack methods, and provide small-scale retrieval evaluation, thus obscuring our comprehensive understanding of retrievers' worst-case behavior. This work aims to faithfully and thoroughly assess retrievers' robustness, paving a path to uncover factors related to their susceptibility to SEO. To this end, we, first, propose the GASLITE attack for generating adversarial passages, that$\unicode{x2013}$without relying on the corpus content or modifying the model$\unicode{x2013}$carry adversary-chosen information while achieving high retrieval ranking, consistently outperforming prior approaches. Second, using GASLITE, we extensively evaluate retrievers' robustness, testing nine advanced models under varied threat models, while focusing on pertinent adversaries targeting queries on a specific concept (e.g., a public figure). Amongst our findings: retrievers are highly vulnerable to SEO against concept-specific queries, even under negligible poisoning rates (e.g., $\geq$0.0001% of the corpus), while generalizing across different corpora and query distributions; single-query SEO is completely solved by GASLITE; adaptive attacks demonstrate bypassing common defenses; [...]

## 🔍 Abstract (한글 번역)

arXiv:2412.20953v2 발표 유형: 교차 교체  
초록: 밀집 임베딩 기반 텍스트 검색$\unicode{x2013}$딥러닝 인코딩을 통한 관련 구문 검색$\unicode{x2013}$은 최첨단 검색 결과를 달성하고 검색 증강 생성(RAG)을 대중화하는 강력한 방법으로 부상했습니다. 그러나 다른 검색 방법과 마찬가지로 임베딩 기반 검색은 검색 엔진 최적화(SEO) 공격에 취약할 수 있습니다. 이 경우 적대자는 적대적 구문을 코퍼스에 도입하여 악의적인 콘텐츠를 홍보합니다. 이전 연구에서는 이러한 SEO가 가능하다는 것을 보여주었으며, 주로 검색 통합 시스템(예: RAG)에 대한 공격을 시연했습니다. 그러나 이들은 완화된 SEO 위협 모델(예: 단일 쿼리 대상)을 고려하고, 기본 공격 방법을 사용하며, 소규모 검색 평가를 제공하여 검색기의 최악의 동작에 대한 포괄적인 이해를 흐리게 합니다. 이 연구는 검색기의 견고성을 충실하고 철저하게 평가하여 SEO에 대한 취약성과 관련된 요인을 발견하기 위한 길을 마련하는 것을 목표로 합니다. 이를 위해 먼저 코퍼스 콘텐츠에 의존하거나 모델을 수정하지 않고도 적대자가 선택한 정보를 전달하면서 높은 검색 순위를 달성하여 이전 접근 방식을 지속적으로 능가하는 적대적 구문 생성을 위한 GASLITE 공격을 제안합니다. 둘째, GASLITE를 사용하여 다양한 위협 모델에서 아홉 가지 고급 모델을 테스트하면서 검색기의 견고성을 광범위하게 평가하고 특정 개념(예: 공인)에 대한 쿼리를 목표로 하는 관련 적대자에 중점을 둡니다. 우리의 발견 중: 검색기는 개념별 쿼리에 대한 SEO에 매우 취약하며, 코퍼스의 0.0001% 이상과 같은 미미한 중독률에서도 다양한 코퍼스 및 쿼리 분포에 걸쳐 일반화됩니다. 단일 쿼리 SEO는 GASLITE에 의해 완전히 해결됩니다. 적응형 공격은 일반적인 방어를 우회하는 것을 보여줍니다; [...]

## 📝 요약

이 논문은 밀집 임베딩 기반 텍스트 검색의 취약성을 평가하고 개선하기 위한 연구를 다룹니다. 주요 기여로는 SEO 공격에 대한 검색기의 취약성을 평가하기 위해 GASLITE라는 새로운 공격 방법을 제안한 점입니다. 이 방법은 코퍼스 내용 수정 없이도 높은 검색 순위를 달성하며, 기존 방법보다 우수한 성능을 보입니다. 연구 결과, 검색기는 특정 개념에 대한 쿼리에서 SEO 공격에 매우 취약하며, 이는 매우 낮은 비율의 데이터 변조에서도 발생할 수 있음을 발견했습니다. 또한, GASLITE는 단일 쿼리 SEO 문제를 해결하며, 적응형 공격은 일반적인 방어를 우회할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. 밀집 임베딩 기반 텍스트 검색은 SEO 공격에 취약할 수 있으며, 악의적인 콘텐츠가 적대적 구문을 통해 홍보될 수 있다.

- 2. GASLITE 공격은 코퍼스 내용이나 모델을 수정하지 않고도 높은 검색 순위를 달성하는 적대적 구문을 생성한다.

- 3. SEO에 대한 검색기의 취약성은 개념 특정 쿼리에 대해 매우 높으며, 극히 낮은 오염률에서도 발생한다.

- 4. GASLITE는 단일 쿼리 SEO 문제를 완전히 해결하며, 적응형 공격은 일반적인 방어를 우회할 수 있다.

---

*Generated on 2025-09-19 16:03:00*