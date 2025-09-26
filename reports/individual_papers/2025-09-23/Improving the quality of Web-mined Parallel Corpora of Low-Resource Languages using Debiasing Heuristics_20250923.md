---
keywords:
  - Neural Machine Translation
  - Large Language Model
  - Parallel Data Curation
  - Debiasing Heuristics
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2502.19074
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:51:12.486107",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Machine Translation",
    "Large Language Model",
    "Parallel Data Curation",
    "Debiasing Heuristics"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Machine Translation": 0.8,
    "Large Language Model": 0.85,
    "Parallel Data Curation": 0.78,
    "Debiasing Heuristics": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural Machine Translation",
        "canonical": "Neural Machine Translation",
        "aliases": [
          "NMT"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus on improving translation quality, linking to broader NLP topics.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Pre-trained Multilingual Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "multiPLM"
        ],
        "category": "broad_technical",
        "rationale": "Key to understanding the biases in sentence pair selection, linking to language model discussions.",
        "novelty_score": 0.5,
        "connectivity_score": 0.88,
        "specificity_score": 0.75,
        "link_intent_score": 0.85
      },
      {
        "surface": "Parallel Data Curation",
        "canonical": "Parallel Data Curation",
        "aliases": [
          "PDC"
        ],
        "category": "unique_technical",
        "rationale": "Specific technique discussed for filtering noisy data, relevant for corpus quality improvement.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Debiasing Heuristics",
        "canonical": "Debiasing Heuristics",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach to improve corpus quality, offering new insights into bias reduction.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "sentence embeddings",
      "similarity scores",
      "source code"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural Machine Translation",
      "resolved_canonical": "Neural Machine Translation",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Pre-trained Multilingual Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.88,
        "specificity": 0.75,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Parallel Data Curation",
      "resolved_canonical": "Parallel Data Curation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Debiasing Heuristics",
      "resolved_canonical": "Debiasing Heuristics",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Improving the quality of Web-mined Parallel Corpora of Low-Resource Languages using Debiasing Heuristics

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2502.19074.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2502.19074](https://arxiv.org/abs/2502.19074)

## 🔗 유사한 논문
- [[2025-09-22/UPRPRC_ Unified Pipeline for Reproducing Parallel Resources -- Corpus from the United Nations_20250922|UPRPRC: Unified Pipeline for Reproducing Parallel Resources -- Corpus from the United Nations]] (83.0% similar)
- [[2025-09-23/DCAD-2000_ A Multilingual Dataset across 2000+ Languages with Data Cleaning as Anomaly Detection_20250923|DCAD-2000: A Multilingual Dataset across 2000+ Languages with Data Cleaning as Anomaly Detection]] (81.7% similar)
- [[2025-09-22/PCSR_ Pseudo-label Consistency-Guided Sample Refinement for Noisy Correspondence Learning_20250922|PCSR: Pseudo-label Consistency-Guided Sample Refinement for Noisy Correspondence Learning]] (80.3% similar)
- [[2025-09-23/CUTE_ A Multilingual Dataset for Enhancing Cross-Lingual Knowledge Transfer in Low-Resource Languages_20250923|CUTE: A Multilingual Dataset for Enhancing Cross-Lingual Knowledge Transfer in Low-Resource Languages]] (80.2% similar)
- [[2025-09-23/Efficient Beam Search for Large Language Models Using Trie-Based Decoding_20250923|Efficient Beam Search for Large Language Models Using Trie-Based Decoding]] (79.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Machine Translation|Neural Machine Translation]], [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Parallel Data Curation|Parallel Data Curation]], [[keywords/Debiasing Heuristics|Debiasing Heuristics]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.19074v3 Announce Type: replace 
Abstract: Parallel Data Curation (PDC) techniques aim to filter out noisy parallel sentences from web-mined corpora. Ranking sentence pairs using similarity scores on sentence embeddings derived from Pre-trained Multilingual Language Models (multiPLMs) is the most common PDC technique. However, previous research has shown that the choice of the multiPLM significantly impacts the quality of the filtered parallel corpus, and the Neural Machine Translation (NMT) models trained using such data show a disparity across multiPLMs. This paper shows that this disparity is due to different multiPLMs being biased towards certain types of sentence pairs, which are treated as noise from an NMT point of view. We show that such noisy parallel sentences can be removed to a certain extent by employing a series of heuristics. The NMT models, trained using the curated corpus, lead to producing better results while minimizing the disparity across multiPLMs. We publicly release the source code and the curated datasets.

## 📝 요약

이 논문은 웹에서 수집한 병렬 문장 데이터의 잡음을 제거하는 병렬 데이터 큐레이션(PDC) 기술에 대해 다룹니다. 기존의 PDC 기술은 사전 학습된 다국어 언어 모델(multiPLM)에서 파생된 문장 임베딩의 유사도 점수를 사용하여 문장 쌍을 정렬합니다. 그러나 multiPLM의 선택이 필터링된 병렬 코퍼스의 품질에 큰 영향을 미치며, 이로 인해 신경망 기계 번역(NMT) 모델의 성능 차이가 발생합니다. 본 연구는 이러한 차이가 multiPLM이 특정 유형의 문장 쌍에 편향되어 있기 때문임을 밝히고, 일련의 휴리스틱을 통해 이러한 잡음 문장을 제거할 수 있음을 보여줍니다. 큐레이션된 코퍼스를 사용해 훈련된 NMT 모델은 multiPLM 간의 성능 차이를 줄이면서 더 나은 번역 결과를 제공합니다. 연구진은 소스 코드와 큐레이션된 데이터셋을 공개했습니다.

## 🎯 주요 포인트

- 1. 병렬 데이터 큐레이션(PDC) 기술은 웹에서 수집한 코퍼스에서 잡음이 있는 병렬 문장을 필터링하는 것을 목표로 합니다.
- 2. 사전 학습된 다국어 언어 모델(multiPLMs)에서 파생된 문장 임베딩의 유사도 점수를 사용하여 문장 쌍을 랭킹하는 것이 일반적인 PDC 기술입니다.
- 3. 다양한 multiPLM이 특정 유형의 문장 쌍에 편향되어 있어 필터링된 병렬 코퍼스의 품질에 영향을 미칩니다.
- 4. 일련의 휴리스틱을 사용하여 잡음이 있는 병렬 문장을 어느 정도 제거할 수 있으며, 이를 통해 NMT 모델의 성능을 향상시킬 수 있습니다.
- 5. 본 연구에서는 소스 코드와 큐레이션된 데이터셋을 공개합니다.


---

*Generated on 2025-09-24 03:51:12*