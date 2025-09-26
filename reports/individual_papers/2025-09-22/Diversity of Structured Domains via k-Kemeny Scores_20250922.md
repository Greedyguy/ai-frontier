---
keywords:
  - k-Kemeny Problem
  - Single-Peaked Preferences
  - Single-Crossing Preferences
  - Group-Separable Preferences
  - Euclidean Preferences
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15812
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:16:47.636095",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "k-Kemeny Problem",
    "Single-Peaked Preferences",
    "Single-Crossing Preferences",
    "Group-Separable Preferences",
    "Euclidean Preferences"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "k-Kemeny Problem": 0.8,
    "Single-Peaked Preferences": 0.78,
    "Single-Crossing Preferences": 0.76,
    "Group-Separable Preferences": 0.77,
    "Euclidean Preferences": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "k-Kemeny problem",
        "canonical": "k-Kemeny Problem",
        "aliases": [
          "k-Kemeny",
          "Kemeny Problem"
        ],
        "category": "unique_technical",
        "rationale": "The k-Kemeny problem is central to the paper's focus on ranking and diversity, offering unique insights into ordinal elections.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "single-peaked",
        "canonical": "Single-Peaked Preferences",
        "aliases": [
          "single-peaked domain"
        ],
        "category": "specific_connectable",
        "rationale": "Single-peaked preferences are a structured domain relevant to the k-Kemeny problem, facilitating connections to voting theory.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "single-crossing",
        "canonical": "Single-Crossing Preferences",
        "aliases": [
          "single-crossing domain"
        ],
        "category": "specific_connectable",
        "rationale": "Single-crossing preferences are another structured domain examined, providing a basis for comparison within the paper.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.76
      },
      {
        "surface": "group-separable",
        "canonical": "Group-Separable Preferences",
        "aliases": [
          "group-separable domain"
        ],
        "category": "specific_connectable",
        "rationale": "Group-separable preferences offer a distinct perspective on ranking diversity, enhancing the paper's comparative analysis.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      },
      {
        "surface": "Euclidean domains",
        "canonical": "Euclidean Preferences",
        "aliases": [
          "Euclidean domain"
        ],
        "category": "specific_connectable",
        "rationale": "Euclidean preferences are a key structured domain in the study, linking to geometric interpretations of ranking.",
        "novelty_score": 0.63,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "ordinal election",
      "ranking candidates"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "k-Kemeny problem",
      "resolved_canonical": "k-Kemeny Problem",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "single-peaked",
      "resolved_canonical": "Single-Peaked Preferences",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "single-crossing",
      "resolved_canonical": "Single-Crossing Preferences",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.76
      }
    },
    {
      "candidate_surface": "group-separable",
      "resolved_canonical": "Group-Separable Preferences",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Euclidean domains",
      "resolved_canonical": "Euclidean Preferences",
      "decision": "linked",
      "scores": {
        "novelty": 0.63,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Diversity of Structured Domains via k-Kemeny Scores

**Korean Title:** 구조적 도메인의 다양성: k-Kemeny 점수

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15812.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15812](https://arxiv.org/abs/2509.15812)

## 🔗 유사한 논문
- [[2025-09-19/Domain Adaptation for Ulcerative Colitis Severity Estimation Using Patient-Level Diagnoses_20250919|Domain Adaptation for Ulcerative Colitis Severity Estimation Using Patient-Level Diagnoses]] (75.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Single-Peaked Preferences|Single-Peaked Preferences]], [[keywords/Single-Crossing Preferences|Single-Crossing Preferences]], [[keywords/Group-Separable Preferences|Group-Separable Preferences]], [[keywords/Euclidean Preferences|Euclidean Preferences]]
**⚡ Unique Technical**: [[keywords/k-Kemeny Problem|k-Kemeny Problem]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15812v1 Announce Type: cross 
Abstract: In the k-Kemeny problem, we are given an ordinal election, i.e., a collection of votes ranking the candidates from best to worst, and we seek the smallest number of swaps of adjacent candidates that ensure that the election has at most k different rankings. We study this problem for a number of structured domains, including the single-peaked, single-crossing, group-separable, and Euclidean ones. We obtain two kinds of results: (1) We show that k-Kemeny remains intractable under most of these domains, even for k=2, and (2) we use k-Kemeny to rank these domains in terms of their diversity.

## 🔍 Abstract (한글 번역)

arXiv:2509.15812v1 발표 유형: 교차  
초록: k-Kemeny 문제에서는 순서형 선거, 즉 후보자들을 최선에서 최악으로 순위화한 투표 집합이 주어지며, 선거가 최대 k개의 다른 순위를 갖도록 보장하는 인접 후보자 간의 교환 횟수를 최소화하는 것을 목표로 합니다. 우리는 단봉형, 단교차형, 그룹 분리형, 유클리드형을 포함한 여러 구조화된 도메인에 대해 이 문제를 연구합니다. 우리는 두 가지 유형의 결과를 얻습니다: (1) 대부분의 이러한 도메인에서도 k-Kemeny가 여전히 난해하다는 것을 보여주며, 심지어 k=2의 경우에도 그렇습니다. (2) 우리는 k-Kemeny를 사용하여 이러한 도메인들을 다양성 측면에서 순위화합니다.

## 📝 요약

이 논문은 k-Kemeny 문제를 다루며, 이는 후보자 순위를 최소한의 인접 교환으로 k개의 다른 순위로 제한하는 문제입니다. 연구는 단일봉, 단일교차, 그룹 분리, 유클리드 등 여러 구조적 도메인에서 수행되었습니다. 주요 기여는 두 가지입니다. 첫째, 대부분의 도메인에서 k-Kemeny 문제가 k=2인 경우에도 여전히 난해함을 보였습니다. 둘째, k-Kemeny를 활용하여 도메인들의 다양성을 평가했습니다.

## 🎯 주요 포인트

- 1. k-Kemeny 문제는 후보자 순위를 인접한 후보자 간의 최소 교환 횟수로 제한된 k개의 순위로 만드는 문제이다.
- 2. 단일 봉우리, 단일 교차, 그룹 분리, 유클리드 등 여러 구조화된 도메인에서 k-Kemeny 문제를 연구하였다.
- 3. 대부분의 도메인에서 k-Kemeny 문제는 k=2인 경우에도 여전히 계산적으로 어려운 문제임을 밝혔다.
- 4. k-Kemeny 문제를 사용하여 다양한 도메인들의 다양성을 평가하였다.


---

*Generated on 2025-09-23 09:16:47*