---
keywords:
  - Graph-Aided Paragraph Alignment
  - Multilingual Datasets
  - Machine Translation
  - Parallel Corpus
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15789
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:53:04.100615",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph-Aided Paragraph Alignment",
    "Multilingual Datasets",
    "Machine Translation",
    "Parallel Corpus"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph-Aided Paragraph Alignment": 0.78,
    "Multilingual Datasets": 0.7,
    "Machine Translation": 0.72,
    "Parallel Corpus": 0.68
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph-Aided Paragraph Alignment",
        "canonical": "Graph-Aided Paragraph Alignment",
        "aliases": [
          "GAPA"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel algorithm specifically designed for paragraph-level alignment in multilingual datasets.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "multilingual datasets",
        "canonical": "Multilingual Datasets",
        "aliases": [
          "multilingual corpora"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus on improving machine translation through enhanced dataset quality and accessibility.",
        "novelty_score": 0.45,
        "connectivity_score": 0.82,
        "specificity_score": 0.67,
        "link_intent_score": 0.7
      },
      {
        "surface": "machine translation",
        "canonical": "Machine Translation",
        "aliases": [
          "MT"
        ],
        "category": "broad_technical",
        "rationale": "A key application area for the proposed corpus, linking to broader research in language processing.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.72
      },
      {
        "surface": "parallel corpus",
        "canonical": "Parallel Corpus",
        "aliases": [
          "bilingual corpus"
        ],
        "category": "specific_connectable",
        "rationale": "Essential for understanding the scale and scope of the dataset produced, relevant to translation studies.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.75,
        "link_intent_score": 0.68
      }
    ],
    "ban_list_suggestions": [
      "end-to-end solution",
      "data acquisition",
      "text alignment",
      "distributed computing"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph-Aided Paragraph Alignment",
      "resolved_canonical": "Graph-Aided Paragraph Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "multilingual datasets",
      "resolved_canonical": "Multilingual Datasets",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.82,
        "specificity": 0.67,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "machine translation",
      "resolved_canonical": "Machine Translation",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "parallel corpus",
      "resolved_canonical": "Parallel Corpus",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.75,
        "link_intent": 0.68
      }
    }
  ]
}
-->

# UPRPRC: Unified Pipeline for Reproducing Parallel Resources -- Corpus from the United Nations

**Korean Title:** UPRPRC: 병렬 자원 재생산을 위한 통합 파이프라인 -- 유엔 코퍼스

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15789.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15789](https://arxiv.org/abs/2509.15789)

## 🔗 유사한 논문
- [[2025-09-22/OpenWHO_ A Document-Level Parallel Corpus for Health Translation in Low-Resource Languages_20250922|OpenWHO: A Document-Level Parallel Corpus for Health Translation in Low-Resource Languages]] (79.9% similar)
- [[2025-09-19/Introducing OmniGEC_ A Silver Multilingual Dataset for Grammatical Error Correction_20250919|Introducing OmniGEC: A Silver Multilingual Dataset for Grammatical Error Correction]] (79.0% similar)
- [[2025-09-19/UnifiedVisual_ A Framework for Constructing Unified Vision-Language Datasets_20250919|UnifiedVisual: A Framework for Constructing Unified Vision-Language Datasets]] (78.0% similar)
- [[2025-09-22/MedCOD_ Enhancing English-to-Spanish Medical Translation of Large Language Models Using Enriched Chain-of-Dictionary Framework_20250922|MedCOD: Enhancing English-to-Spanish Medical Translation of Large Language Models Using Enriched Chain-of-Dictionary Framework]] (77.7% similar)
- [[2025-09-22/Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training_20250922|Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training]] (77.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Multilingual Datasets|Multilingual Datasets]], [[keywords/Machine Translation|Machine Translation]]
**🔗 Specific Connectable**: [[keywords/Parallel Corpus|Parallel Corpus]]
**⚡ Unique Technical**: [[keywords/Graph-Aided Paragraph Alignment|Graph-Aided Paragraph Alignment]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15789v1 Announce Type: cross 
Abstract: The quality and accessibility of multilingual datasets are crucial for advancing machine translation. However, previous corpora built from United Nations documents have suffered from issues such as opaque process, difficulty of reproduction, and limited scale. To address these challenges, we introduce a complete end-to-end solution, from data acquisition via web scraping to text alignment. The entire process is fully reproducible, with a minimalist single-machine example and optional distributed computing steps for scalability. At its core, we propose a new Graph-Aided Paragraph Alignment (GAPA) algorithm for efficient and flexible paragraph-level alignment. The resulting corpus contains over 713 million English tokens, more than doubling the scale of prior work. To the best of our knowledge, this represents the largest publicly available parallel corpus composed entirely of human-translated, non-AI-generated content. Our code and corpus are accessible under the MIT License.

## 🔍 Abstract (한글 번역)

arXiv:2509.15789v1 발표 유형: 교차  
초록: 다국어 데이터셋의 품질과 접근성은 기계 번역의 발전에 있어 매우 중요합니다. 그러나 이전에 유엔 문서에서 구축된 코퍼스는 불투명한 과정, 재현의 어려움, 제한된 규모와 같은 문제를 겪었습니다. 이러한 문제를 해결하기 위해, 우리는 웹 스크래핑을 통한 데이터 수집에서 텍스트 정렬에 이르는 완전한 엔드 투 엔드 솔루션을 소개합니다. 전체 과정은 완전히 재현 가능하며, 단일 기계 예제와 확장성을 위한 선택적 분산 컴퓨팅 단계가 포함된 최소주의적 접근을 제공합니다. 핵심적으로, 우리는 효율적이고 유연한 문단 수준 정렬을 위한 새로운 그래프 보조 문단 정렬(GAPA) 알고리즘을 제안합니다. 결과적으로 생성된 코퍼스는 7억 1천 3백만 개 이상의 영어 토큰을 포함하며, 이전 작업의 규모를 두 배 이상 확장합니다. 우리가 아는 한, 이는 인간 번역, 비 AI 생성 콘텐츠로만 구성된 가장 큰 공개 병렬 코퍼스를 나타냅니다. 우리의 코드와 코퍼스는 MIT 라이선스 하에 접근 가능합니다.

## 📝 요약

이 논문은 기계 번역 발전을 위한 다국어 데이터셋의 품질과 접근성을 개선하고자 합니다. 기존 유엔 문서 기반 코퍼스의 불투명한 과정, 재현의 어려움, 제한된 규모 문제를 해결하기 위해, 웹 스크래핑부터 텍스트 정렬까지 완전한 엔드 투 엔드 솔루션을 제안합니다. 특히, 효율적이고 유연한 문단 정렬을 위한 새로운 그래프 지원 문단 정렬(GAPA) 알고리즘을 도입했습니다. 이로써 7억 1,300만 개 이상의 영어 토큰을 포함하는 대규모 코퍼스를 구축했으며, 이는 이전 작업의 두 배 이상의 규모입니다. 이 코퍼스는 인간 번역으로만 구성된 가장 큰 공개 병렬 코퍼스로, MIT 라이선스 하에 코드와 함께 제공됩니다.

## 🎯 주요 포인트

- 1. 이 연구는 웹 스크래핑을 통한 데이터 수집부터 텍스트 정렬까지의 완전한 엔드 투 엔드 솔루션을 제안합니다.
- 2. 새로운 Graph-Aided Paragraph Alignment (GAPA) 알고리즘을 통해 효율적이고 유연한 문단 수준의 정렬을 구현합니다.
- 3. 결과적으로, 7억 1,300만 개 이상의 영어 토큰을 포함하는 대규모 병렬 코퍼스를 구축하였으며, 이는 이전 작업의 규모를 두 배 이상 확장한 것입니다.
- 4. 이 코퍼스는 인간 번역된 비 AI 생성 콘텐츠로만 구성된 가장 큰 공개 병렬 코퍼스로 알려져 있습니다.
- 5. 연구의 코드와 코퍼스는 MIT 라이선스 하에 접근 가능합니다.


---

*Generated on 2025-09-23 10:53:04*