---
keywords:
  - Ge'ez Language
  - Morphological Synthesizer
  - Rule-Based System
  - Morphology
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.20341
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:08:13.521432",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Ge'ez Language",
    "Morphological Synthesizer",
    "Rule-Based System",
    "Morphology"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Ge'ez Language": 0.88,
    "Morphological Synthesizer": 0.82,
    "Rule-Based System": 0.7,
    "Morphology": 0.68
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Ge'ez",
        "canonical": "Ge'ez Language",
        "aliases": [
          "Ge'ez Script"
        ],
        "category": "unique_technical",
        "rationale": "Ge'ez is a central focus of the paper, representing a unique linguistic subject with historical and cultural significance.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "morphological synthesizer",
        "canonical": "Morphological Synthesizer",
        "aliases": [
          "morphology generator"
        ],
        "category": "unique_technical",
        "rationale": "The morphological synthesizer is a novel tool proposed in the paper, crucial for advancing NLP in Ge'ez.",
        "novelty_score": 0.78,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "rule-based",
        "canonical": "Rule-Based System",
        "aliases": [
          "rule-based approach"
        ],
        "category": "broad_technical",
        "rationale": "Rule-based systems are a foundational approach in computational linguistics, relevant for linking with other NLP methodologies.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "morphology",
        "canonical": "Morphology",
        "aliases": [
          "morphological structure"
        ],
        "category": "broad_technical",
        "rationale": "Morphology is a key linguistic concept that connects to various language processing studies.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.68
      }
    ],
    "ban_list_suggestions": [
      "NLP",
      "performance",
      "system"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Ge'ez",
      "resolved_canonical": "Ge'ez Language",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "morphological synthesizer",
      "resolved_canonical": "Morphological Synthesizer",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "rule-based",
      "resolved_canonical": "Rule-Based System",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "morphology",
      "resolved_canonical": "Morphology",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.68
      }
    }
  ]
}
-->

# Morphological Synthesizer for Ge'ez Language: Addressing Morphological Complexity and Resource Limitations

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20341.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.20341](https://arxiv.org/abs/2509.20341)

## 🔗 유사한 논문
- [[2025-09-25/Low-Resource English-Tigrinya MT_ Leveraging Multilingual Models, Custom Tokenizers, and Clean Evaluation Benchmarks_20250925|Low-Resource English-Tigrinya MT: Leveraging Multilingual Models, Custom Tokenizers, and Clean Evaluation Benchmarks]] (78.4% similar)
- [[2025-09-25/EngravingGNN_ A Hybrid Graph Neural Network for End-to-End Piano Score Engraving_20250925|EngravingGNN: A Hybrid Graph Neural Network for End-to-End Piano Score Engraving]] (77.1% similar)
- [[2025-09-23/Enhancing Cross-Lingual Transfer through Reversible Transliteration_ A Huffman-Based Approach for Low-Resource Languages_20250923|Enhancing Cross-Lingual Transfer through Reversible Transliteration: A Huffman-Based Approach for Low-Resource Languages]] (76.9% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (76.9% similar)
- [[2025-09-22/How do Language Models Generate Slang_ A Systematic Comparison between Human and Machine-Generated Slang Usages_20250922|How do Language Models Generate Slang: A Systematic Comparison between Human and Machine-Generated Slang Usages]] (76.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Rule-Based System|Rule-Based System]], [[keywords/Morphology|Morphology]]
**⚡ Unique Technical**: [[keywords/Ge'ez Language|Ge'ez Language]], [[keywords/Morphological Synthesizer|Morphological Synthesizer]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20341v1 Announce Type: cross 
Abstract: Ge'ez is an ancient Semitic language renowned for its unique alphabet. It serves as the script for numerous languages, including Tigrinya and Amharic, and played a pivotal role in Ethiopia's cultural and religious development during the Aksumite kingdom era. Ge'ez remains significant as a liturgical language in Ethiopia and Eritrea, with much of the national identity documentation recorded in Ge'ez. These written materials are invaluable primary sources for studying Ethiopian and Eritrean philosophy, creativity, knowledge, and civilization. Ge'ez has a complex morphological structure with rich inflectional and derivational morphology, and no usable NLP has been developed and published until now due to the scarcity of annotated linguistic data, corpora, labeled datasets, and lexicons. Therefore, we propose a rule-based Ge'ez morphological synthesizer to generate surface words from root words according to the morphological structures of the language. We used 1,102 sample verbs, representing all verb morphological structures, to test and evaluate the system. The system achieves a performance of 97.4%, outperforming the baseline model and suggesting that future work should build a comprehensive system considering morphological variations of the language.
  Keywords: Ge'ez, NLP, morphology, morphological synthesizer, rule-based

## 📝 요약

이 논문은 고대 셈어인 게즈어의 복잡한 형태론적 구조를 다루며, 이를 위한 형태 합성기를 제안합니다. 게즈어는 에티오피아와 에리트레아의 문화 및 종교 발전에 중요한 역할을 했으며, 현재도 예배 언어로 사용됩니다. 그러나 주석이 달린 언어 데이터가 부족하여 자연어 처리(NLP) 연구가 어려웠습니다. 이에 저자들은 규칙 기반의 게즈어 형태 합성기를 개발하여, 1,102개의 동사 샘플을 통해 97.4%의 높은 성능을 달성했습니다. 이는 기존 모델을 능가하며, 향후 연구에서는 언어의 형태 변화를 고려한 포괄적인 시스템 구축이 필요함을 시사합니다.

## 🎯 주요 포인트

- 1. Ge'ez는 독특한 알파벳을 가진 고대 셈어로, 티그리냐어와 암하라어 등의 문자로 사용되며, 아크숨 왕국 시대 에티오피아의 문화 및 종교 발전에 중요한 역할을 했습니다.
- 2. Ge'ez는 에티오피아와 에리트레아에서 여전히 예배 언어로 사용되며, 국가 정체성 문서가 Ge'ez로 기록되어 있어 철학, 창의성, 지식, 문명을 연구하는 데 중요한 1차 자료입니다.
- 3. Ge'ez는 복잡한 형태론적 구조를 가지고 있으며, 주석이 달린 언어 데이터 부족으로 인해 사용 가능한 자연어 처리(NLP) 도구가 개발되지 않았습니다.
- 4. 이 논문에서는 Ge'ez의 형태론적 구조에 따라 어근에서 표면 단어를 생성하는 규칙 기반 형태론적 합성기를 제안하며, 1,102개의 샘플 동사를 사용하여 시스템을 테스트한 결과 97.4%의 성능을 달성했습니다.
- 5. 제안된 시스템은 기존 모델을 능가하며, 향후 연구에서는 언어의 형태론적 변화를 고려한 포괄적인 시스템 구축이 필요합니다.


---

*Generated on 2025-09-25 16:08:13*