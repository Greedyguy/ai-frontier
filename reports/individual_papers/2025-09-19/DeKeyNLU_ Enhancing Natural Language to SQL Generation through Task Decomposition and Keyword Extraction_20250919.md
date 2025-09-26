---
keywords:
  - DeKeyNLU
  - Large Language Models
  - Natural Language to SQL
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14507
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:49:52.361971",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "DeKeyNLU",
    "Large Language Models",
    "Natural Language to SQL"
  ],
  "rejected_keywords": [
    "Retrieval-Augmented Generation",
    "Chain-of-Thought reasoning"
  ],
  "similarity_scores": {
    "DeKeyNLU": 0.82,
    "Large Language Models": 0.8,
    "Natural Language to SQL": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# DeKeyNLU: Enhancing Natural Language to SQL Generation through Task Decomposition and Keyword Extraction

**Korean Title:** DeKeyNLU: 작업 분해 및 키워드 추출을 통한 자연어에서 SQL 생성 향상

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Large Language Models|Large Language Models]]
**⚡ Unique Technical**: [[keywords/DeKeyNLU|DeKeyNLU]], [[keywords/Natural Language to SQL|Natural Language to SQL]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14507v1 Announce Type: new 
Abstract: Natural Language to SQL (NL2SQL) provides a new model-centric paradigm that simplifies database access for non-technical users by converting natural language queries into SQL commands. Recent advancements, particularly those integrating Retrieval-Augmented Generation (RAG) and Chain-of-Thought (CoT) reasoning, have made significant strides in enhancing NL2SQL performance. However, challenges such as inaccurate task decomposition and keyword extraction by LLMs remain major bottlenecks, often leading to errors in SQL generation. While existing datasets aim to mitigate these issues by fine-tuning models, they struggle with over-fragmentation of tasks and lack of domain-specific keyword annotations, limiting their effectiveness. To address these limitations, we present DeKeyNLU, a novel dataset which contains 1,500 meticulously annotated QA pairs aimed at refining task decomposition and enhancing keyword extraction precision for the RAG pipeline. Fine-tuned with DeKeyNLU, we propose DeKeySQL, a RAG-based NL2SQL pipeline that employs three distinct modules for user question understanding, entity retrieval, and generation to improve SQL generation accuracy. We benchmarked multiple model configurations within DeKeySQL RAG pipeline. Experimental results demonstrate that fine-tuning with DeKeyNLU significantly improves SQL generation accuracy on both BIRD (62.31% to 69.10%) and Spider (84.2% to 88.7%) dev datasets.

## 🔍 Abstract (한글 번역)

arXiv:2509.14507v1 발표 유형: 신규  
초록: 자연어를 SQL로 변환하는 NL2SQL은 비기술적 사용자가 자연어 쿼리를 SQL 명령어로 변환하여 데이터베이스에 쉽게 접근할 수 있도록 하는 새로운 모델 중심 패러다임을 제공합니다. 특히 검색 증강 생성(RAG)과 사고의 연쇄(CoT) 추론을 통합한 최근의 발전은 NL2SQL 성능을 크게 향상시켰습니다. 그러나 LLM에 의한 부정확한 작업 분해와 키워드 추출과 같은 문제는 여전히 주요 병목 현상으로 남아 있으며, 이는 종종 SQL 생성 오류로 이어집니다. 기존 데이터셋은 모델을 미세 조정하여 이러한 문제를 완화하려고 하지만, 작업의 과도한 세분화와 도메인별 키워드 주석 부족으로 인해 효과가 제한됩니다. 이러한 한계를 해결하기 위해, 우리는 RAG 파이프라인의 작업 분해를 개선하고 키워드 추출 정확성을 높이기 위한 1,500개의 세심하게 주석이 달린 QA 쌍을 포함한 새로운 데이터셋인 DeKeyNLU를 제시합니다. DeKeyNLU로 미세 조정된 우리는 사용자 질문 이해, 엔티티 검색 및 생성을 위한 세 가지 모듈을 활용하여 SQL 생성 정확성을 향상시키는 RAG 기반 NL2SQL 파이프라인인 DeKeySQL을 제안합니다. 우리는 DeKeySQL RAG 파이프라인 내에서 여러 모델 구성을 벤치마킹했습니다. 실험 결과, DeKeyNLU로 미세 조정하면 BIRD(62.31%에서 69.10%)와 Spider(84.2%에서 88.7%) 개발 데이터셋 모두에서 SQL 생성 정확도가 크게 향상됨을 보여줍니다.

## 📝 요약

이 논문은 비기술적 사용자가 자연어 쿼리를 SQL 명령으로 변환할 수 있도록 하는 NL2SQL 기술을 다룹니다. 최근 RAG와 CoT 추론을 통합한 접근법이 NL2SQL 성능을 향상시켰지만, LLM의 부정확한 작업 분해와 키워드 추출이 여전히 문제로 남아 있습니다. 이를 해결하기 위해, 저자들은 1,500개의 QA 쌍으로 구성된 DeKeyNLU라는 새로운 데이터셋을 제안하여 작업 분해와 키워드 추출의 정확성을 높였습니다. DeKeyNLU로 미세 조정된 DeKeySQL 파이프라인은 사용자 질문 이해, 엔티티 검색, 생성의 세 가지 모듈을 사용하여 SQL 생성 정확도를 개선합니다. 실험 결과, DeKeyNLU로 미세 조정한 모델은 BIRD와 Spider 데이터셋에서 SQL 생성 정확도를 각각 62.31%에서 69.10%, 84.2%에서 88.7%로 향상시켰습니다.

## 🎯 주요 포인트

- 1. NL2SQL은 비기술적 사용자를 위해 자연어 쿼리를 SQL 명령으로 변환하여 데이터베이스 접근을 간소화하는 모델 중심 패러다임을 제공합니다.

- 2. Retrieval-Augmented Generation (RAG)와 Chain-of-Thought (CoT) 추론을 통합한 최근 발전은 NL2SQL 성능을 크게 향상시켰습니다.

- 3. LLM의 부정확한 작업 분해와 키워드 추출은 SQL 생성 오류의 주요 원인으로 남아 있습니다.

- 4. DeKeyNLU는 작업 분해와 키워드 추출 정밀도를 향상시키기 위해 1,500개의 세심하게 주석된 QA 쌍을 포함하는 새로운 데이터셋입니다.

- 5. DeKeySQL은 DeKeyNLU로 미세 조정된 RAG 기반 NL2SQL 파이프라인으로, SQL 생성 정확도를 개선하기 위해 사용자 질문 이해, 엔티티 검색, 생성의 세 가지 모듈을 사용합니다.

---

*Generated on 2025-09-19 18:08:43*