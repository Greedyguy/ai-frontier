---
keywords:
  - Entity Discovery and Linking
  - Mahābhārata
  - Cross-lingual Linking
  - Sanskrit
category: cs.CL
publish_date: 2025-09-25
arxiv_id: 2509.19844
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:45:35.760366",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Entity Discovery and Linking",
    "Mahābhārata",
    "Cross-lingual Linking",
    "Sanskrit"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Entity Discovery and Linking": 0.85,
    "Mahābhārata": 0.8,
    "Cross-lingual Linking": 0.79,
    "Sanskrit": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Entity Discovery and Linking",
        "canonical": "Entity Discovery and Linking",
        "aliases": [
          "EDL"
        ],
        "category": "unique_technical",
        "rationale": "This is a core concept of the paper, focusing on resolving entities in literary texts, which is crucial for linking.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      },
      {
        "surface": "Mahābhārata",
        "canonical": "Mahābhārata",
        "aliases": [
          "Mahabharata"
        ],
        "category": "unique_technical",
        "rationale": "The dataset is derived from this epic, making it central to the paper's context and linking potential.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "cross-lingual linking",
        "canonical": "Cross-lingual Linking",
        "aliases": [
          "cross-lingual entity linking"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is vital for understanding the paper's approach to linking entities across languages.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      },
      {
        "surface": "Sanskrit",
        "canonical": "Sanskrit",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The focus on this under-resourced language is a unique aspect of the dataset and paper.",
        "novelty_score": 0.8,
        "connectivity_score": 0.55,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "dataset",
      "evaluation",
      "resolution systems"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Entity Discovery and Linking",
      "resolved_canonical": "Entity Discovery and Linking",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Mahābhārata",
      "resolved_canonical": "Mahābhārata",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "cross-lingual linking",
      "resolved_canonical": "Cross-lingual Linking",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Sanskrit",
      "resolved_canonical": "Sanskrit",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.55,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Mah\={a}n\={a}ma: A Unique Testbed for Literary Entity Discovery and Linking

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19844.pdf)
**Category**: cs.CL
**Published**: 2025-09-25
**ArXiv ID**: [2509.19844](https://arxiv.org/abs/2509.19844)

## 🔗 유사한 논문
- [[2025-09-23/SciNLP_ A Domain-Specific Benchmark for Full-Text Scientific Entity and Relation Extraction in NLP_20250923|SciNLP: A Domain-Specific Benchmark for Full-Text Scientific Entity and Relation Extraction in NLP]] (79.6% similar)
- [[2025-09-18/TextMine_ LLM-Powered Knowledge Extraction for Humanitarian Mine Action_20250918|TextMine: LLM-Powered Knowledge Extraction for Humanitarian Mine Action]] (77.6% similar)
- [[2025-09-19/MOLE_ Metadata Extraction and Validation in Scientific Papers Using LLMs_20250919|MOLE: Metadata Extraction and Validation in Scientific Papers Using LLMs]] (77.0% similar)
- [[2025-09-22/DynamicNER_ A Dynamic, Multilingual, and Fine-Grained Dataset for LLM-based Named Entity Recognition_20250922|DynamicNER: A Dynamic, Multilingual, and Fine-Grained Dataset for LLM-based Named Entity Recognition]] (76.9% similar)
- [[2025-09-24/MAPEX_ A Multi-Agent Pipeline for Keyphrase Extraction_20250924|MAPEX: A Multi-Agent Pipeline for Keyphrase Extraction]] (76.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Cross-lingual Linking|Cross-lingual Linking]]
**⚡ Unique Technical**: [[keywords/Entity Discovery and Linking|Entity Discovery and Linking]], [[keywords/Mahābhārata|Mahābhārata]], [[keywords/Sanskrit|Sanskrit]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19844v1 Announce Type: new 
Abstract: High lexical variation, ambiguous references, and long-range dependencies make entity resolution in literary texts particularly challenging. We present Mah\={a}n\={a}ma, the first large-scale dataset for end-to-end Entity Discovery and Linking (EDL) in Sanskrit, a morphologically rich and under-resourced language. Derived from the Mah\={a}bh\={a}rata, the world's longest epic, the dataset comprises over 109K named entity mentions mapped to 5.5K unique entities, and is aligned with an English knowledge base to support cross-lingual linking. The complex narrative structure of Mah\={a}n\={a}ma, coupled with extensive name variation and ambiguity, poses significant challenges to resolution systems. Our evaluation reveals that current coreference and entity linking models struggle when evaluated on the global context of the test set. These results highlight the limitations of current approaches in resolving entities within such complex discourse. Mah\=an\=ama thus provides a unique benchmark for advancing entity resolution, especially in literary domains.

## 📝 요약

이 논문은 문학 텍스트에서의 엔티티 해결 문제를 다루며, 산스크리트어의 엔티티 발견 및 연결(EDL)을 위한 대규모 데이터셋인 Mahānāma를 소개합니다. Mahānāma는 세계에서 가장 긴 서사시인 마하바라타에서 유래된 데이터셋으로, 109,000개 이상의 명명된 엔티티 언급이 5,500개의 고유 엔티티와 연결되어 있습니다. 이 데이터셋은 영어 지식 기반과의 교차 언어 연결을 지원합니다. 연구 결과, 현재의 공지 및 엔티티 연결 모델은 복잡한 서사 구조와 이름의 변이 및 모호성으로 인해 엔티티 해결에 어려움을 겪고 있음을 보여줍니다. Mahānāma는 특히 문학 분야에서 엔티티 해결을 발전시키기 위한 독특한 기준점을 제공합니다.

## 🎯 주요 포인트

- 1. Mahānāma는 산스크리트어의 엔티티 발견 및 연결(EDL)을 위한 최초의 대규모 데이터셋입니다.
- 2. 이 데이터셋은 세계에서 가장 긴 서사시인 마하바라타에서 파생되었으며, 109K 이상의 명명된 엔티티 언급이 5.5K의 고유 엔티티에 매핑되어 있습니다.
- 3. Mahānāma는 영어 지식 기반과 정렬되어 있어 교차 언어 연결을 지원합니다.
- 4. 현재의 상호 참조 및 엔티티 연결 모델은 테스트 세트의 글로벌 컨텍스트에서 평가될 때 어려움을 겪고 있습니다.
- 5. Mahānāma는 문학적 도메인에서 엔티티 해석을 발전시키기 위한 독특한 벤치마크를 제공합니다.


---

*Generated on 2025-09-26 08:45:35*