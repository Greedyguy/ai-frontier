---
keywords:
  - Large Language Models
  - Retrieval-Augmented Generation
  - Substructure Search
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2508.12536
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:16:06.909276",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Retrieval-Augmented Generation",
    "Substructure Search"
  ],
  "rejected_keywords": [
    "Geospatial Analytics"
  ],
  "similarity_scores": {
    "Large Language Models": 0.8,
    "Retrieval-Augmented Generation": 0.77,
    "Substructure Search": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# jXBW: Fast Substructure Search for Large-Scale JSONL Datasets with LLM Applications

**Korean Title:** jXBW: LLM 응용을 위한 대규모 JSONL 데이터셋의 빠른 부분 구조 검색

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Large Language Models|Large Language Models]], [[keywords/Retrieval-Augmented Generation|Retrieval-Augmented Generation]]
**⚡ Unique Technical**: [[keywords/Substructure Search|Substructure Search]]

## 🔗 유사한 논문
- [[LLM Agents for Interactive Workflow Provenance Reference Architecture and Evaluation Methodology]] (78.3% similar)
- [[MOLE Metadata Extraction and Validation in Scientific Papers Using LLMs]] (77.9% similar)
- [[SWE-QA Can Language Models Answer Repository-level Code Questions]] (76.8% similar)
- [[GASLITEing the Retrieval Exploring Vulnerabilities in Dense Embedding-based Search]] (76.7% similar)
- [[Modernizing Facebook Scoped Search Keyword and Embedding Hybrid Retrieval with LLM Evaluation]] (76.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.12536v2 Announce Type: replace-cross 
Abstract: JSON Lines (JSONL) is widely used for managing large collections of semi-structured data, ranging from large language model (LLM) prompts to chemical compound records and geospatial datasets. A key operation is substructure search, which identifies all JSON objects containing a query pattern. This task underpins applications such as drug discovery (querying compounds for functional groups), prompt engineering (extracting prompts with schema fragments), and geospatial analytics (finding entities with nested attributes). However, existing methods are inefficient: traversal requires exhaustive tree matching, succinct JSON representations save space but do not accelerate search, and XML-based approaches incur conversion overhead and semantic mismatches. We present jXBW, a compressed index for efficient substructure search over JSONL. jXBW introduces three innovations: (i) a merged tree representation that consolidates repeated structures, (ii) a succinct tree index based on the eXtended Burrows--Wheeler Transform (XBW), and (iii) a three-phase algorithm for substructure search. These enable query-dependent complexity, where cost depends on query characteristics rather than dataset size, while retaining succinct space. This resolves a key bottleneck in retrieval-augmented generation (RAG) systems requiring structure-aware retrieval. Experiments on seven real datasets, including PubChem (1M compounds) and OSM geospatial data (6.6M objects), achieve up to 4,700$\times$ speedup over tree-based methods and over $6\times 10^6$ speedup relative to XML-based approaches. jXBW makes JSONL substructure search practical for the first time, opening opportunities for large-scale LLM-based analytics.

## 🔍 Abstract (한글 번역)

arXiv:2508.12536v2 발표 유형: 교차 교체  
초록: JSON Lines (JSONL)은 대규모 언어 모델(LLM) 프롬프트에서 화합물 기록 및 지리 공간 데이터 세트에 이르기까지 대규모 반구조화 데이터 컬렉션을 관리하는 데 널리 사용됩니다. 주요 작업은 하위 구조 검색으로, 쿼리 패턴을 포함하는 모든 JSON 객체를 식별합니다. 이 작업은 약물 발견(기능 그룹에 대한 화합물 쿼리), 프롬프트 엔지니어링(스키마 조각이 있는 프롬프트 추출) 및 지리 공간 분석(중첩된 속성이 있는 엔티티 찾기)과 같은 응용 프로그램의 기반이 됩니다. 그러나 기존 방법은 비효율적입니다. 트리 순회에는 철저한 트리 매칭이 필요하고, 간결한 JSON 표현은 공간을 절약하지만 검색 속도를 높이지 않으며, XML 기반 접근 방식은 변환 오버헤드와 의미적 불일치를 초래합니다. 우리는 JSONL에 대한 효율적인 하위 구조 검색을 위한 압축 인덱스인 jXBW를 제시합니다. jXBW는 세 가지 혁신을 도입합니다: (i) 반복 구조를 통합하는 병합 트리 표현, (ii) 확장된 버로우즈-휠러 변환(XBW)을 기반으로 한 간결한 트리 인덱스, (iii) 하위 구조 검색을 위한 3단계 알고리즘. 이러한 요소들은 데이터 세트 크기보다는 쿼리 특성에 따라 비용이 결정되는 쿼리 종속 복잡성을 가능하게 하면서도 간결한 공간을 유지합니다. 이는 구조 인식 검색을 요구하는 검색 증강 생성(RAG) 시스템의 주요 병목 현상을 해결합니다. PubChem(100만 화합물) 및 OSM 지리 공간 데이터(660만 객체)를 포함한 7개의 실제 데이터 세트에 대한 실험에서 트리 기반 방법에 비해 최대 4,700배, XML 기반 접근 방식에 비해 6×10^6배 이상의 속도 향상을 달성했습니다. jXBW는 JSONL 하위 구조 검색을 처음으로 실용적으로 만들어 대규모 LLM 기반 분석을 위한 기회를 열어줍니다.

## 📝 요약

JSON Lines(JSONL)은 대규모 반구조화 데이터를 관리하는 데 널리 사용되며, 주요 작업 중 하나는 쿼리 패턴을 포함하는 JSON 객체를 식별하는 부분 구조 검색입니다. 기존 방법들은 비효율적이며, 이를 해결하기 위해 jXBW라는 압축 인덱스를 제안합니다. jXBW는 반복 구조를 통합하는 병합 트리 표현, 확장된 Burrows-Wheeler 변환(XBW)에 기반한 간결한 트리 인덱스, 그리고 세 단계의 알고리즘을 도입하여 쿼리 특성에 따른 복잡성을 제공합니다. 이는 구조 인식 검색을 요구하는 시스템의 주요 병목을 해결하며, 실험 결과 최대 4,700배의 속도 향상을 보여줍니다. jXBW는 JSONL의 부분 구조 검색을 실용적으로 만들어 대규모 LLM 기반 분석의 기회를 열어줍니다.

## 🎯 주요 포인트

- 1. JSON Lines(JSONL)는 대규모 반구조화 데이터 관리에 널리 사용되며, 주요 작업은 쿼리 패턴을 포함하는 JSON 객체를 식별하는 서브스트럭처 검색이다.

- 2. 기존 방법들은 비효율적이며, 트리 기반 방법은 전수 트리 매칭이 필요하고, XML 기반 접근법은 변환 오버헤드와 의미적 불일치를 초래한다.

- 3. jXBW는 JSONL에 대한 효율적인 서브스트럭처 검색을 위한 압축 인덱스를 제공하며, 반복 구조를 통합하는 병합 트리 표현, XBW 기반의 간결한 트리 인덱스, 그리고 세 단계 알고리즘을 도입한다.

- 4. jXBW는 쿼리 특성에 따라 복잡도가 결정되며, 데이터셋 크기에 의존하지 않고 간결한 공간을 유지하면서 검색 속도를 크게 향상시킨다.

- 5. 실험 결과, jXBW는 트리 기반 방법에 비해 최대 4,700배, XML 기반 접근법에 비해 6백만 배 이상의 속도 향상을 달성하여 대규모 LLM 기반 분석에 실용적인 서브스트럭처 검색을 가능하게 한다.

---

*Generated on 2025-09-19 16:25:14*