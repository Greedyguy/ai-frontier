---
keywords:
  - Large Language Model
  - English-Anchored Optimization
  - Machine Translation
  - Synthetic Data Generation
category: cs.CL
publish_date: 2025-09-25
arxiv_id: 2509.19770
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:45:22.481561",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "English-Anchored Optimization",
    "Machine Translation",
    "Synthetic Data Generation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "English-Anchored Optimization": 0.7,
    "Machine Translation": 0.8,
    "Synthetic Data Generation": 0.78
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
        "rationale": "This term is central to the paper's focus on translation capabilities and links to a broad range of related research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "English-Anchored Optimization",
        "canonical": "English-Anchored Optimization",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a novel method introduced in the paper, pivotal for linking to specific translation strategies.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Machine Translation",
        "canonical": "Machine Translation",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A key application area for the discussed models, facilitating connections to translation research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Synthetic Data Generation",
        "canonical": "Synthetic Data Generation",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This technique is crucial for improving translation models, linking to data augmentation research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "English-Anchored Optimization",
      "resolved_canonical": "English-Anchored Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Machine Translation",
      "resolved_canonical": "Machine Translation",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Synthetic Data Generation",
      "resolved_canonical": "Synthetic Data Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# EnAnchored-X2X: English-Anchored Optimization for Many-to-Many Translation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19770.pdf)
**Category**: cs.CL
**Published**: 2025-09-25
**ArXiv ID**: [2509.19770](https://arxiv.org/abs/2509.19770)

## 🔗 유사한 논문
- [[2025-09-24/Linguistic Neuron Overlap Patterns to Facilitate Cross-lingual Transfer on Low-resource Languages_20250924|Linguistic Neuron Overlap Patterns to Facilitate Cross-lingual Transfer on Low-resource Languages]] (85.0% similar)
- [[2025-09-23/Scaling Low-Resource MT via Synthetic Data Generation with LLMs_20250923|Scaling Low-Resource MT via Synthetic Data Generation with LLMs]] (84.8% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (84.4% similar)
- [[2025-09-22/The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation_20250922|The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation]] (84.3% similar)
- [[2025-09-25/From Unaligned to Aligned_ Scaling Multilingual LLMs with Multi-Way Parallel Corpora_20250925|From Unaligned to Aligned: Scaling Multilingual LLMs with Multi-Way Parallel Corpora]] (83.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Machine Translation|Machine Translation]], [[keywords/Synthetic Data Generation|Synthetic Data Generation]]
**⚡ Unique Technical**: [[keywords/English-Anchored Optimization|English-Anchored Optimization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19770v1 Announce Type: new 
Abstract: Large language models (LLMs) have demonstrated strong machine translation capabilities for English-centric language pairs but underperform in direct non-English (x2x) translation. This work addresses this limitation through a synthetic data generation framework that leverages models' established English-to-x (en2x) capabilities. By extending English parallel corpora into omnidirectional datasets and developing an English-referenced quality evaluation proxy, we enable effective collection of high-quality x2x training data. Combined with preference-based optimization, our method achieves significant improvement across 72 x2x directions for widely used LLMs, while generalizing to enhance en2x performance. The results demonstrate that strategic exploitation of English-centric strengths can bootstrap comprehensive multilingual translation capabilities in LLMs. We release codes, datasets, and model checkpoints at https://github.com/NJUNLP/EAX

## 📝 요약

이 논문은 대형 언어 모델(LLM)이 영어 중심의 언어 쌍 번역에서는 뛰어난 성능을 보이지만, 비영어 간 직접 번역(x2x)에서는 성능이 떨어지는 문제를 해결하고자 합니다. 이를 위해 영어 병렬 코퍼스를 활용하여 모든 방향으로 확장 가능한 데이터셋을 생성하고, 영어를 참조하는 품질 평가 방법을 개발하여 고품질의 x2x 훈련 데이터를 효과적으로 수집합니다. 또한, 선호 기반 최적화를 통해 72개의 x2x 번역 방향에서 성능을 크게 향상시켰으며, 영어 중심 번역(en2x) 성능도 개선되었습니다. 이 연구는 영어 중심의 강점을 전략적으로 활용하여 LLM의 다국어 번역 능력을 향상시킬 수 있음을 보여줍니다. 코드, 데이터셋, 모델 체크포인트는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 영어 중심 언어 쌍에서는 강력한 번역 능력을 보이지만, 비영어 간 직접 번역(x2x)에서는 성능이 저하됩니다.
- 2. 본 연구는 영어 병렬 코퍼스를 전방위 데이터셋으로 확장하고, 영어 참조 품질 평가 프록시를 개발하여 고품질 x2x 학습 데이터를 효과적으로 수집하는 방법을 제안합니다.
- 3. 선호 기반 최적화와 결합하여, 제안된 방법은 널리 사용되는 LLM의 72개 x2x 방향에서 성능을 크게 향상시켰으며, en2x 성능도 개선되었습니다.
- 4. 영어 중심의 강점을 전략적으로 활용하면 LLM의 다국어 번역 능력을 포괄적으로 향상시킬 수 있음을 보여줍니다.
- 5. 연구 결과에 대한 코드, 데이터셋, 모델 체크포인트는 https://github.com/NJUNLP/EAX 에서 공개됩니다.


---

*Generated on 2025-09-26 08:45:22*