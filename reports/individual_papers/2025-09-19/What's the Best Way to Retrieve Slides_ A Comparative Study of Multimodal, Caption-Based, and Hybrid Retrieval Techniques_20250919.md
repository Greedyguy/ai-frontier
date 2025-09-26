---
keywords:
  - Vision-Language Models
  - Multi-Modal Learning
  - Hybrid Retrieval Techniques
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.15211
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:17:34.855879",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Models",
    "Multi-Modal Learning",
    "Hybrid Retrieval Techniques"
  ],
  "rejected_keywords": [
    "Reciprocal Rank Fusion"
  ],
  "similarity_scores": {
    "Vision-Language Models": 0.88,
    "Multi-Modal Learning": 0.85,
    "Hybrid Retrieval Techniques": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# What's the Best Way to Retrieve Slides? A Comparative Study of Multimodal, Caption-Based, and Hybrid Retrieval Techniques

**Korean Title:** 슬라이드를 검색하는 최선의 방법은 무엇인가? 다중 모드, 캡션 기반, 하이브리드 검색 기법의 비교 연구

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Hybrid Retrieval Techniques|Hybrid Retrieval Techniques]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Models|Vision-Language Models]], [[keywords/Multi-Modal Learning|Multimodal Retrieval]]

## 🔗 유사한 논문
- [[Auto-Slides An Interactive Multi-Agent System for Creating and Customizing Research Presentations]] (79.9% similar)
- [[Search-TTA A Multimodal Test-Time Adaptation Framework for Visual Search in the Wild]] (79.7% similar)
- [[Engineering RAG Systems for Real-World Applications Design, Development, and Evaluation]] (79.2% similar)
- [[Modernizing Facebook Scoped Search Keyword and Embedding Hybrid Retrieval with LLM Evaluation]] (79.2% similar)
- [[Enhancing Retrieval Augmentation via Adversarial Collaboration_20250919|Enhancing Retrieval Augmentation via Adversarial Collaboration]] (79.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15211v1 Announce Type: new 
Abstract: Slide decks, serving as digital reports that bridge the gap between presentation slides and written documents, are a prevalent medium for conveying information in both academic and corporate settings. Their multimodal nature, combining text, images, and charts, presents challenges for retrieval-augmented generation systems, where the quality of retrieval directly impacts downstream performance. Traditional approaches to slide retrieval often involve separate indexing of modalities, which can increase complexity and lose contextual information. This paper investigates various methodologies for effective slide retrieval, including visual late-interaction embedding models like ColPali, the use of visual rerankers, and hybrid retrieval techniques that combine dense retrieval with BM25, further enhanced by textual rerankers and fusion methods like Reciprocal Rank Fusion. A novel Vision-Language Models-based captioning pipeline is also evaluated, demonstrating significantly reduced embedding storage requirements compared to visual late-interaction techniques, alongside comparable retrieval performance. Our analysis extends to the practical aspects of these methods, evaluating their runtime performance and storage demands alongside retrieval efficacy, thus offering practical guidance for the selection and development of efficient and robust slide retrieval systems for real-world applications.

## 🔍 Abstract (한글 번역)

arXiv:2509.15211v1 발표 유형: 신규  
초록: 슬라이드 덱은 프레젠테이션 슬라이드와 문서 사이의 간극을 메우는 디지털 보고서로서, 학계와 기업 환경 모두에서 정보를 전달하는 데 널리 사용되는 매체입니다. 텍스트, 이미지, 차트를 결합한 이들의 다중 모달 특성은 검색 증강 생성 시스템에서 도전 과제를 제시하며, 검색의 품질이 후속 성능에 직접적으로 영향을 미칩니다. 전통적인 슬라이드 검색 접근법은 종종 모달리티를 개별적으로 색인화하는데, 이는 복잡성을 증가시키고 맥락 정보를 잃을 수 있습니다. 본 논문은 ColPali와 같은 시각적 후기 상호작용 임베딩 모델, 시각적 재순위화기 사용, BM25와 밀집 검색을 결합한 하이브리드 검색 기법 등 효과적인 슬라이드 검색을 위한 다양한 방법론을 조사합니다. 또한, 텍스트 재순위화기와 상호 순위 융합(Reciprocal Rank Fusion)과 같은 융합 방법으로 강화된 방법도 포함됩니다. 새로운 비전-언어 모델 기반 캡션 파이프라인도 평가되었으며, 시각적 후기 상호작용 기법에 비해 임베딩 저장 요구 사항이 크게 감소하면서도 유사한 검색 성능을 보여줍니다. 우리의 분석은 이러한 방법들의 실용적인 측면까지 확장되어, 실행 시간 성능과 저장 요구 사항을 검색 효율성과 함께 평가하여 실제 응용을 위한 효율적이고 견고한 슬라이드 검색 시스템의 선택과 개발에 실질적인 지침을 제공합니다.

## 📝 요약

이 논문은 학술 및 기업 환경에서 정보 전달을 위한 슬라이드 덱의 효과적인 검색 방법론을 연구합니다. 전통적인 슬라이드 검색은 텍스트, 이미지, 차트를 개별적으로 색인화하여 복잡성을 증가시키고 맥락 정보를 잃을 수 있습니다. 본 연구는 ColPali와 같은 시각적 후반 상호작용 임베딩 모델, 시각적 재랭커, BM25와 밀집 검색을 결합한 하이브리드 검색 기술을 조사합니다. 또한, 비전-언어 모델 기반 캡션 파이프라인을 평가하여 임베딩 저장 요구를 크게 줄이면서 유사한 검색 성능을 보였습니다. 실용적인 측면에서 이 방법들의 실행 시간 성능과 저장 요구를 평가하여 실세계 응용을 위한 효율적이고 견고한 슬라이드 검색 시스템 개발에 대한 지침을 제공합니다.

## 🎯 주요 포인트

- 1. 슬라이드 덱은 텍스트, 이미지, 차트를 결합한 멀티모달 형식으로 정보 전달에 사용되며, 이로 인해 검색 기반 생성 시스템에서의 검색 품질이 중요하다.

- 2. 전통적인 슬라이드 검색 방법은 모달리티를 별도로 색인화하여 복잡성을 증가시키고 맥락 정보를 잃을 수 있다.

- 3. 본 논문은 ColPali와 같은 시각적 후기 상호작용 임베딩 모델, 시각적 재정렬기, BM25와의 조밀 검색 결합 등 다양한 슬라이드 검색 방법론을 조사한다.

- 4. 비전-언어 모델 기반 캡션 파이프라인은 시각적 후기 상호작용 기법에 비해 임베딩 저장 요구를 크게 줄이면서도 유사한 검색 성능을 보인다.

- 5. 실용적인 측면에서 각 방법의 실행 시간 성능과 저장 요구 사항을 평가하여 실제 응용을 위한 효율적이고 견고한 슬라이드 검색 시스템 개발에 실질적인 지침을 제공한다.

---

*Generated on 2025-09-19 15:55:44*