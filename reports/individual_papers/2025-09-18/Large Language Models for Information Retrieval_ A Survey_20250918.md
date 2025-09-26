---
keywords:
  - Large Language Models
  - Information Retrieval
  - Search Agents
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2308.07107
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:22:42.162692",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Information Retrieval",
    "Search Agents"
  ],
  "rejected_keywords": [
    "Neural Networks",
    "Query Rewriters"
  ],
  "similarity_scores": {
    "Large Language Models": 0.9,
    "Information Retrieval": 0.85,
    "Search Agents": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Large Language Models for Information Retrieval: A Survey

**Korean Title:** 정보 검색을 위한 대규모 언어 모델: 조사

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Information Retrieval|Information Retrieval]]
**⚡ Unique Technical**: [[keywords/Search Agents|Search Agents]]
**🚀 Evolved Concepts**: [[keywords/Large Language Models|Large Language Models]]

## 🔗 유사한 논문
- [[From_Automation_to_Autonomy_A_Survey_on_Large_Language_Models_in_Scientific_Discovery_20250918|From Automation to Autonomy: A Survey on Large Language Models in Scientific Discovery]] (87.4% similar)
- [[A Comprehensive Survey on the Trustworthiness of Large Language Models in Healthcare]] (83.8% similar)
- [[KBM_Delineating_Knowledge_Boundary_for_Adaptive_Retrieval_in_Large_Language_Models_20250918|KBM: Delineating Knowledge Boundary for Adaptive Retrieval in Large Language Models]] (82.8% similar)
- [[Self-Guided_Function_Calling_in_Large_Language_Models_via_Stepwise_Experience_Recall_20250918|Self-Guided Function Calling in Large Language Models via Stepwise Experience Recall]] (82.0% similar)
- [[LLM-I_LLMs_are_Naturally_Interleaved_Multimodal_Creators_20250918|LLM-I: LLMs are Naturally Interleaved Multimodal Creators]] (81.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2308.07107v5 Announce Type: replace 
Abstract: As a primary means of information acquisition, information retrieval (IR) systems, such as search engines, have integrated themselves into our daily lives. These systems also serve as components of dialogue, question-answering, and recommender systems. The trajectory of IR has evolved dynamically from its origins in term-based methods to its integration with advanced neural models. While the neural models excel at capturing complex contextual signals and semantic nuances, thereby reshaping the IR landscape, they still face challenges such as data scarcity, interpretability, and the generation of contextually plausible yet potentially inaccurate responses. This evolution requires a combination of both traditional methods (such as term-based sparse retrieval methods with rapid response) and modern neural architectures (such as language models with powerful language understanding capacity). Meanwhile, the emergence of large language models (LLMs), typified by ChatGPT and GPT-4, has revolutionized natural language processing due to their remarkable language understanding, generation, generalization, and reasoning abilities. Consequently, recent research has sought to leverage LLMs to improve IR systems. Given the rapid evolution of this research trajectory, it is necessary to consolidate existing methodologies and provide nuanced insights through a comprehensive overview. In this survey, we delve into the confluence of LLMs and IR systems, including crucial aspects such as query rewriters, retrievers, rerankers, and readers. Additionally, we explore promising directions, such as search agents, within this expanding field.

## 🔍 Abstract (한글 번역)

arXiv:2308.07107v5 발표 유형: 교체
요약: 정보 검색(IR) 시스템은 정보 획득의 주요 수단으로서, 검색 엔진과 같은 시스템은 우리의 일상 속에 통합되어 있습니다. 이러한 시스템은 또한 대화, 질의응답 및 추천 시스템의 구성 요소로 작용합니다. IR의 궤적은 용어 기반 방법에서 고급 신경 모델과의 통합으로 동적으로 진화해 왔습니다. 신경 모델은 복잡한 맥락 신호와 의미적 미묘함을 잡아내는 데 뛰어나며, 이로 인해 IR 풍경을 재구성하고 있지만, 데이터 부족, 해석 가능성 및 맥락적으로 타당하지만 잠재적으로 부정확한 응답 생성과 같은 도전에 직면하고 있습니다. 이러한 진화는 전통적인 방법(빠른 응답을 제공하는 용어 기반 희소 검색 방법과 같은)과 현대적인 신경 구조(강력한 언어 이해 능력을 갖춘 언어 모델과 같은)의 조합을 필요로 합니다. 한편, ChatGPT 및 GPT-4와 같은 대형 언어 모델(LLM)의 등장은 놀라운 언어 이해, 생성, 일반화 및 추론 능력으로 자연어 처리를 혁신적으로 바꿨습니다. 결과적으로 최근 연구는 IR 시스템을 개선하기 위해 LLM을 활용하려고 하고 있습니다. 이 연구 궤적의 신속한 진화를 고려할 때, 기존 방법론을 정리하고 포괄적인 개요를 통해 세밀한 통찰을 제공하는 것이 필요합니다. 본 조사에서는 LLM과 IR 시스템의 융합, 쿼리 재작성기, 검색기, 재순위 지정기 및 리더와 같은 중요한 측면을 탐구합니다. 또한, 이 확장되는 분야 내에서 검색 에이전트와 같은 유망한 방향을 탐구합니다.

## 📝 요약

정보 검색(IR) 시스템은 우리 일상에 통합되어 있으며 대화, 질의응답, 추천 시스템의 구성 요소로 작용한다. IR의 발전은 용어 기반 방법에서 고급 신경 모델과 통합됨에 따라 맥락 신호와 의미적 뉘앙스를 잡는 데 우수하나 데이터 부족, 해석 가능성, 문맥적으로 타당하지만 잠재적으로 부정확한 응답 생성과 같은 도전에 직면한다. 이 연구는 전통적 방법(용어 기반 희소 검색 방법)과 현대적 신경 구조(강력한 언어 이해 능력을 갖춘 언어 모델)의 결합을 요구하며 대형 언어 모델(LLM)의 등장으로 IR 시스템 개선을 위해 LLM을 활용하는 연구가 활발히 진행되고 있다. 이 연구는 LLM과 IR 시스템의 융합에 대해 종합적으로 살펴보고 쿼리 재작성기, 검색기, 재순위 지정자, 리더 등의 중요한 측면과 검색 에이전트와 같은 유망한 방향을 탐구한다.

## 🎯 주요 포인트

- 1. 정보 검색 시스템은 우리의 일상에 통합되어 있으며, 최신 신경 모델과 전통적인 방법을 결합하여 발전하고 있다.

- 2. 대형 언어 모델은 자연어 처리 분야를 혁신적으로 변화시키고 있으며, 정보 검색 시스템에 적용되어 성능을 향상시키는 연구가 진행 중이다.

- 3. 연구는 쿼리 재작성기, 검색기, 재순위 지정기, 리더 등을 포함한 다양한 측면을 다루고 있으며, 검색 에이전트와 같은 유망한 방향도 탐구하고 있다.

---

*Generated on 2025-09-18 16:53:46*