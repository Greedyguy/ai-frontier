---
keywords:
  - k-Nearest Neighbors Machine Translation
  - Neural Machine Translation
  - Angular Dispersion
  - Hidden State Representations
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16729
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:14:35.140958",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "k-Nearest Neighbors Machine Translation",
    "Neural Machine Translation",
    "Angular Dispersion",
    "Hidden State Representations"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "k-Nearest Neighbors Machine Translation": 0.8,
    "Neural Machine Translation": 0.75,
    "Angular Dispersion": 0.7,
    "Hidden State Representations": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "k-nearest neighbors machine translation",
        "canonical": "k-Nearest Neighbors Machine Translation",
        "aliases": [
          "k-NN MT"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific method discussed in the paper, crucial for understanding the proposed improvements.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "neural machine translation",
        "canonical": "Neural Machine Translation",
        "aliases": [
          "NMT"
        ],
        "category": "specific_connectable",
        "rationale": "A key area of application for machine learning techniques, directly relevant to the paper's focus.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "angular dispersion",
        "canonical": "Angular Dispersion",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A novel concept introduced in the paper to improve retrieval performance.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "hidden state representations",
        "canonical": "Hidden State Representations",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Central to the retrieval process in k-NN MT, linking to broader neural network concepts.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "data store"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "k-nearest neighbors machine translation",
      "resolved_canonical": "k-Nearest Neighbors Machine Translation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "neural machine translation",
      "resolved_canonical": "Neural Machine Translation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "angular dispersion",
      "resolved_canonical": "Angular Dispersion",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "hidden state representations",
      "resolved_canonical": "Hidden State Representations",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Angular Dispersion Accelerates $k$-Nearest Neighbors Machine Translation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16729.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16729](https://arxiv.org/abs/2509.16729)

## 🔗 유사한 논문
- [[2025-09-23/KNN-MMD_ Cross Domain Wireless Sensing via Local Distribution Alignment_20250923|KNN-MMD: Cross Domain Wireless Sensing via Local Distribution Alignment]] (79.5% similar)
- [[2025-09-22/KVCompose_ Efficient Structured KV Cache Compression with Composite Tokens_20250922|KVCompose: Efficient Structured KV Cache Compression with Composite Tokens]] (79.2% similar)
- [[2025-09-23/Neural Attention Search_20250923|Neural Attention Search]] (79.1% similar)
- [[2025-09-19/Value-Guided KV Compression for LLMs via Approximated CUR Decomposition_20250919|Value-Guided KV Compression for LLMs via Approximated CUR Decomposition]] (78.5% similar)
- [[2025-09-17/You Are What You Train_ Effects of Data Composition on Training Context-aware Machine Translation Models_20250917|You Are What You Train: Effects of Data Composition on Training Context-aware Machine Translation Models]] (78.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Neural Machine Translation|Neural Machine Translation]], [[keywords/Hidden State Representations|Hidden State Representations]]
**⚡ Unique Technical**: [[keywords/k-Nearest Neighbors Machine Translation|k-Nearest Neighbors Machine Translation]], [[keywords/Angular Dispersion|Angular Dispersion]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16729v1 Announce Type: cross 
Abstract: Augmenting neural machine translation with external memory at decoding time, in the form of k-nearest neighbors machine translation ($k$-NN MT), is a well-established strategy for increasing translation performance. $k$-NN MT retrieves a set of tokens that occurred in the most similar contexts recorded in a prepared data store, using hidden state representations of translation contexts as vector lookup keys. One of the main disadvantages of this method is the high computational cost and memory requirements. Since an exhaustive search is not feasible in large data stores, practitioners commonly use approximate $k$-NN MT lookup, yet even such algorithms are a bottleneck. In contrast to research directions seeking to accelerate $k$-NN MT by reducing data store size or the number of lookup calls, we pursue an orthogonal direction based on the performance properties of approximate $k$-NN MT lookup data structures. In particular, we propose to encourage angular dispersion of the neural hidden representations of contexts. We show that improving dispersion leads to better balance in the retrieval data structures, accelerating retrieval and slightly improving translations.

## 📝 요약

이 논문은 신경 기계 번역(NMT) 성능을 향상시키기 위해 외부 메모리를 활용하는 $k$-최근접 이웃 기계 번역($k$-NN MT) 방법을 다룹니다. 기존의 $k$-NN MT는 높은 계산 비용과 메모리 요구량이 단점으로, 근사적 $k$-NN MT 검색을 사용하지만 여전히 병목현상이 발생합니다. 본 연구는 데이터 저장소 크기나 검색 호출 수를 줄이는 대신, 근사적 $k$-NN MT 검색 구조의 성능 특성을 활용하여 신경망의 숨겨진 표현의 각 분산을 증가시킵니다. 이를 통해 검색 구조의 균형을 개선하고 검색 속도를 높이며 번역 성능을 약간 향상시켰습니다.

## 🎯 주요 포인트

- 1. 외부 메모리를 활용한 k-최근접 이웃 기계 번역($k$-NN MT)은 번역 성능 향상을 위한 잘 확립된 전략이다.
- 2. $k$-NN MT는 준비된 데이터 저장소에서 가장 유사한 문맥에서 발생한 토큰 집합을 검색한다.
- 3. 이 방법의 주요 단점은 높은 계산 비용과 메모리 요구 사항이다.
- 4. 우리는 근사 $k$-NN MT 검색 데이터 구조의 성능 특성을 기반으로 한 새로운 접근 방식을 제안한다.
- 5. 문맥의 신경 은닉 표현의 각도 분산을 개선하면 검색 속도가 빨라지고 번역이 약간 개선된다.


---

*Generated on 2025-09-24 02:14:35*