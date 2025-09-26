---
keywords:
  - Natural Language Processing
  - Cross-lingual Augmentation
  - Machine Translation
  - Transliteration Systems
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.12853
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:13:54.715862",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Natural Language Processing",
    "Cross-lingual Augmentation",
    "Machine Translation",
    "Transliteration Systems"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Natural Language Processing": 0.85,
    "Cross-lingual Augmentation": 0.78,
    "Machine Translation": 0.82,
    "Transliteration Systems": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Natural Language Processing",
        "canonical": "Natural Language Processing",
        "aliases": [
          "NLP"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's theme of enhancing Maltese NLP through Arabic data.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Cross-lingual Augmentation",
        "canonical": "Cross-lingual Augmentation",
        "aliases": [
          "Multilingual Augmentation"
        ],
        "category": "unique_technical",
        "rationale": "Key technique explored in the paper for leveraging Arabic resources.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Machine Translation",
        "canonical": "Machine Translation",
        "aliases": [
          "MT"
        ],
        "category": "specific_connectable",
        "rationale": "A significant method used for aligning Arabic and Maltese data.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "Transliteration Systems",
        "canonical": "Transliteration Systems",
        "aliases": [
          "Transliteration Schemes"
        ],
        "category": "unique_technical",
        "rationale": "Introduces novel systems that are crucial for representing Maltese orthography.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "Semitic language",
      "Romance languages",
      "Germanic languages",
      "Italian",
      "English"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Natural Language Processing",
      "resolved_canonical": "Natural Language Processing",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Cross-lingual Augmentation",
      "resolved_canonical": "Cross-lingual Augmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Machine Translation",
      "resolved_canonical": "Machine Translation",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Transliteration Systems",
      "resolved_canonical": "Transliteration Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Data Augmentation for Maltese NLP using Transliterated and Machine Translated Arabic Data

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.12853.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.12853](https://arxiv.org/abs/2509.12853)

## 🔗 유사한 논문
- [[2025-09-22/Frustratingly Easy Data Augmentation for Low-Resource ASR_20250922|Frustratingly Easy Data Augmentation for Low-Resource ASR]] (81.3% similar)
- [[2025-09-19/MOLE_ Metadata Extraction and Validation in Scientific Papers Using LLMs_20250919|MOLE: Metadata Extraction and Validation in Scientific Papers Using LLMs]] (80.4% similar)
- [[2025-09-23/AutoArabic_ A Three-Stage Framework for Localizing Video-Text Retrieval Benchmarks_20250923|AutoArabic: A Three-Stage Framework for Localizing Video-Text Retrieval Benchmarks]] (80.2% similar)
- [[2025-09-22/mucAI at BAREC Shared Task 2025_ Towards Uncertainty Aware Arabic Readability Assessment_20250922|mucAI at BAREC Shared Task 2025: Towards Uncertainty Aware Arabic Readability Assessment]] (79.8% similar)
- [[2025-09-23/Scaling, Simplification, and Adaptation_ Lessons from Pretraining on Machine-Translated Text_20250923|Scaling, Simplification, and Adaptation: Lessons from Pretraining on Machine-Translated Text]] (79.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Natural Language Processing|Natural Language Processing]]
**🔗 Specific Connectable**: [[keywords/Machine Translation|Machine Translation]]
**⚡ Unique Technical**: [[keywords/Cross-lingual Augmentation|Cross-lingual Augmentation]], [[keywords/Transliteration Systems|Transliteration Systems]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.12853v2 Announce Type: replace 
Abstract: Maltese is a unique Semitic language that has evolved under extensive influence from Romance and Germanic languages, particularly Italian and English. Despite its Semitic roots, its orthography is based on the Latin script, creating a gap between it and its closest linguistic relatives in Arabic. In this paper, we explore whether Arabic-language resources can support Maltese natural language processing (NLP) through cross-lingual augmentation techniques. We investigate multiple strategies for aligning Arabic textual data with Maltese, including various transliteration schemes and machine translation (MT) approaches. As part of this, we also introduce novel transliteration systems that better represent Maltese orthography. We evaluate the impact of these augmentations on monolingual and mutlilingual models and demonstrate that Arabic-based augmentation can significantly benefit Maltese NLP tasks.

## 📝 요약

이 논문은 몰타어 자연어 처리(NLP)에 아랍어 자원을 활용할 수 있는지 탐구합니다. 몰타어는 라틴 문자로 표기되며, 로망스 및 게르만 언어의 영향을 많이 받았습니다. 연구에서는 아랍어 텍스트 데이터를 몰타어와 정렬하기 위한 다양한 전략을 조사하고, 새로운 음역 시스템을 도입하여 몰타어 표기를 더 잘 표현합니다. 이러한 증강 기법이 단일 및 다중 언어 모델에 미치는 영향을 평가한 결과, 아랍어 기반 증강이 몰타어 NLP 작업에 상당한 이점을 제공함을 입증했습니다.

## 🎯 주요 포인트

- 1. 몰타어는 로망스 및 게르만 언어의 영향을 받아 발전한 독특한 셈어로, 라틴 문자 기반의 철자를 사용합니다.
- 2. 아랍어 자원을 활용한 교차 언어 증강 기법이 몰타어 자연어 처리(NLP)에 도움을 줄 수 있는지 탐구합니다.
- 3. 아랍어 텍스트 데이터를 몰타어와 정렬하기 위한 다양한 전사 체계 및 기계 번역 접근법을 조사합니다.
- 4. 몰타어 철자를 더 잘 표현하는 새로운 전사 시스템을 도입합니다.
- 5. 아랍어 기반 증강이 몰타어 NLP 작업에 유의미한 이점을 제공할 수 있음을 입증합니다.


---

*Generated on 2025-09-24 04:13:54*