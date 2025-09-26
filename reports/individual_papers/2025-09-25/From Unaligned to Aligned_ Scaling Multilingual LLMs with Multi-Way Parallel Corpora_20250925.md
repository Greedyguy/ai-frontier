---
keywords:
  - Large Language Model
  - Multi-Way Parallel Data
  - Instruction Tuning
  - Cross-Lingual Semantics
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2505.14045
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:25:00.010993",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Multi-Way Parallel Data",
    "Instruction Tuning",
    "Cross-Lingual Semantics"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Multi-Way Parallel Data": 0.78,
    "Instruction Tuning": 0.82,
    "Cross-Lingual Semantics": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's discussion on multilingual scaling and are a key concept in NLP.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "multi-way parallel data",
        "canonical": "Multi-Way Parallel Data",
        "aliases": [
          "parallel corpora",
          "aligned data"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique concept introduced in the paper that enhances cross-lingual consistency, crucial for multilingual LLMs.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "instruction tuning",
        "canonical": "Instruction Tuning",
        "aliases": [
          "instruction-based tuning"
        ],
        "category": "specific_connectable",
        "rationale": "Instruction tuning is a significant method for improving model performance, connecting to broader themes in model training.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "cross-lingual semantics",
        "canonical": "Cross-Lingual Semantics",
        "aliases": [
          "cross-language semantics"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding cross-lingual semantics is vital for multilingual model performance, linking to semantic analysis.",
        "novelty_score": 0.58,
        "connectivity_score": 0.78,
        "specificity_score": 0.76,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "low-resource languages",
      "multilingual benchmarks"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "multi-way parallel data",
      "resolved_canonical": "Multi-Way Parallel Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "instruction tuning",
      "resolved_canonical": "Instruction Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "cross-lingual semantics",
      "resolved_canonical": "Cross-Lingual Semantics",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.78,
        "specificity": 0.76,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# From Unaligned to Aligned: Scaling Multilingual LLMs with Multi-Way Parallel Corpora

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.14045.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2505.14045](https://arxiv.org/abs/2505.14045)

## 🔗 유사한 논문
- [[2025-09-22/Exploring Polyglot Harmony_ On Multilingual Data Allocation for Large Language Models Pretraining_20250922|Exploring Polyglot Harmony: On Multilingual Data Allocation for Large Language Models Pretraining]] (85.4% similar)
- [[2025-09-23/CUTE_ A Multilingual Dataset for Enhancing Cross-Lingual Knowledge Transfer in Low-Resource Languages_20250923|CUTE: A Multilingual Dataset for Enhancing Cross-Lingual Knowledge Transfer in Low-Resource Languages]] (85.3% similar)
- [[2025-09-22/Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training_20250922|Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training]] (85.3% similar)
- [[2025-09-22/A method for improving multilingual quality and diversity of instruction fine-tuning datasets_20250922|A method for improving multilingual quality and diversity of instruction fine-tuning datasets]] (84.0% similar)
- [[2025-09-22/The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation_20250922|The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation]] (83.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Instruction Tuning|Instruction Tuning]], [[keywords/Cross-Lingual Semantics|Cross-Lingual Semantics]]
**⚡ Unique Technical**: [[keywords/Multi-Way Parallel Data|Multi-Way Parallel Data]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.14045v3 Announce Type: replace-cross 
Abstract: Continued pretraining and instruction tuning on large-scale multilingual data have proven to be effective in scaling large language models (LLMs) to low-resource languages. However, the unaligned nature of such data limits its ability to effectively capture cross-lingual semantics. In contrast, multi-way parallel data, where identical content is aligned across multiple languages, provides stronger cross-lingual consistency and offers greater potential for improving multilingual performance. In this paper, we introduce a large-scale, high-quality multi-way parallel corpus, TED2025, based on TED Talks. The corpus spans 113 languages, with up to 50 languages aligned in parallel, ensuring extensive multilingual coverage. Using this dataset, we investigate best practices for leveraging multi-way parallel data to enhance LLMs, including strategies for continued pretraining, instruction tuning, and the analysis of key influencing factors. Experiments on six multilingual benchmarks show that models trained on multiway parallel data consistently outperform those trained on unaligned multilingual data.

## 📝 요약

이 논문은 다국어 대규모 병렬 코퍼스 TED2025를 소개하며, 이는 113개 언어를 포함하고 최대 50개 언어가 병렬로 정렬된 고품질 데이터셋입니다. 이 데이터셋을 활용하여 대규모 언어 모델(LLM)의 성능을 향상시키기 위한 최적의 방법론을 연구했습니다. 특히, 다국어 병렬 데이터가 비정렬 다국어 데이터보다 일관된 다국어 성능을 제공함을 실험을 통해 입증했습니다. 주요 기여는 다국어 병렬 데이터의 활용 전략과 주요 영향 요인 분석을 통해 LLM의 다국어 성능을 개선한 것입니다.

## 🎯 주요 포인트

- 1. 대규모 다국어 데이터의 지속적인 사전 학습과 명령어 튜닝은 저자원 언어에서 대형 언어 모델(LLM)의 성능을 향상시키는 데 효과적이다.
- 2. 다중 병렬 데이터는 여러 언어에서 동일한 콘텐츠가 정렬되어 있어 강력한 교차 언어 일관성을 제공하며, 다국어 성능을 개선할 잠재력이 크다.
- 3. TED Talks를 기반으로 한 대규모 고품질 다중 병렬 코퍼스 TED2025를 소개하며, 113개 언어를 포함하고 최대 50개 언어가 병렬로 정렬되어 있다.
- 4. 다중 병렬 데이터를 활용하여 LLM을 향상시키기 위한 최선의 방법을 연구하며, 지속적인 사전 학습, 명령어 튜닝, 주요 영향 요인 분석을 포함한다.
- 5. 여섯 개의 다국어 벤치마크 실험에서 다중 병렬 데이터로 훈련된 모델이 비정렬 다국어 데이터로 훈련된 모델보다 일관되게 우수한 성능을 보였다.


---

*Generated on 2025-09-25 16:25:00*