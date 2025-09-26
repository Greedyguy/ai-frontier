---
keywords:
  - Multilingual Retrieval
  - Crosslingual Retrieval
  - Fact-Checked Claims
  - Large Language Model
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2505.22118
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:00:18.474811",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multilingual Retrieval",
    "Crosslingual Retrieval",
    "Fact-Checked Claims",
    "Large Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multilingual Retrieval": 0.78,
    "Crosslingual Retrieval": 0.79,
    "Fact-Checked Claims": 0.77,
    "Large Language Model": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "multilingual retrieval",
        "canonical": "Multilingual Retrieval",
        "aliases": [
          "multilingual search"
        ],
        "category": "unique_technical",
        "rationale": "This term is crucial for linking discussions on language-specific retrieval systems.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "crosslingual retrieval",
        "canonical": "Crosslingual Retrieval",
        "aliases": [
          "cross-language retrieval"
        ],
        "category": "unique_technical",
        "rationale": "It highlights the unique challenges and methodologies in retrieving information across different languages.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "fact-checked claims",
        "canonical": "Fact-Checked Claims",
        "aliases": [
          "verified claims"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to discussions on verification and misinformation.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      },
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are pivotal in enhancing retrieval tasks through advanced language understanding.",
        "novelty_score": 0.3,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "retrieval",
      "claims",
      "languages"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "multilingual retrieval",
      "resolved_canonical": "Multilingual Retrieval",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "crosslingual retrieval",
      "resolved_canonical": "Crosslingual Retrieval",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "fact-checked claims",
      "resolved_canonical": "Fact-Checked Claims",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Multilingual vs Crosslingual Retrieval of Fact-Checked Claims: A Tale of Two Approaches

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.22118.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2505.22118](https://arxiv.org/abs/2505.22118)

## 🔗 유사한 논문
- [[2025-09-19/ReCoVeR the Target Language_ Language Steering without Sacrificing Task Performance_20250919|ReCoVeR the Target Language: Language Steering without Sacrificing Task Performance]] (84.1% similar)
- [[2025-09-22/PolBiX_ Detecting LLMs' Political Bias in Fact-Checking through X-phemisms_20250922|PolBiX: Detecting LLMs' Political Bias in Fact-Checking through X-phemisms]] (83.9% similar)
- [[2025-09-22/The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation_20250922|The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation]] (83.8% similar)
- [[2025-09-22/Best-of-L_ Cross-Lingual Reward Modeling for Mathematical Reasoning_20250922|Best-of-L: Cross-Lingual Reward Modeling for Mathematical Reasoning]] (83.2% similar)
- [[2025-09-22/Language Mixing in Reasoning Language Models_ Patterns, Impact, and Internal Causes_20250922|Language Mixing in Reasoning Language Models: Patterns, Impact, and Internal Causes]] (83.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Multilingual Retrieval|Multilingual Retrieval]], [[keywords/Crosslingual Retrieval|Crosslingual Retrieval]], [[keywords/Fact-Checked Claims|Fact-Checked Claims]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.22118v2 Announce Type: replace 
Abstract: Retrieval of previously fact-checked claims is a well-established task, whose automation can assist professional fact-checkers in the initial steps of information verification. Previous works have mostly tackled the task monolingually, i.e., having both the input and the retrieved claims in the same language. However, especially for languages with a limited availability of fact-checks and in case of global narratives, such as pandemics, wars, or international politics, it is crucial to be able to retrieve claims across languages. In this work, we examine strategies to improve the multilingual and crosslingual performance, namely selection of negative examples (in the supervised) and re-ranking (in the unsupervised setting). We evaluate all approaches on a dataset containing posts and claims in 47 languages (283 language combinations). We observe that the best results are obtained by using LLM-based re-ranking, followed by fine-tuning with negative examples sampled using a sentence similarity-based strategy. Most importantly, we show that crosslinguality is a setup with its own unique characteristics compared to the multilingual setup.

## 📝 요약

이 논문은 다국어 및 교차언어 환경에서의 사실 확인 자동화 방법을 연구합니다. 기존 연구는 주로 단일 언어 내에서만 수행되었으나, 이 연구는 다양한 언어로 된 주장을 검색할 수 있는 방법을 탐구합니다. 저자들은 감독 학습에서의 부정 예시 선택과 비감독 학습에서의 재정렬 전략을 통해 성능을 개선하고자 했습니다. 47개 언어로 구성된 데이터셋을 통해 평가한 결과, 대형 언어 모델(LLM)을 활용한 재정렬이 가장 효과적이었으며, 문장 유사도 기반으로 샘플링한 부정 예시를 활용한 미세 조정이 뒤를 이었습니다. 또한, 교차언어 환경이 다국어 환경과는 고유한 특성을 지닌다는 점을 강조합니다.

## 🎯 주요 포인트

- 1. 기존의 사실 확인된 주장 검색 작업은 주로 단일 언어로 수행되었으나, 다국어 및 교차 언어 검색의 필요성이 강조된다.
- 2. 이 연구는 다국어 및 교차 언어 성능 향상을 위한 전략으로 감독 학습에서의 부정 예시 선택과 비감독 학습에서의 재랭킹을 탐구한다.
- 3. 47개 언어의 게시물과 주장으로 구성된 데이터셋을 통해 다양한 접근 방식을 평가하였다.
- 4. LLM 기반 재랭킹이 가장 우수한 결과를 보였으며, 문장 유사성 기반 전략으로 샘플링된 부정 예시를 활용한 미세 조정이 그 뒤를 이었다.
- 5. 교차 언어 설정은 다국어 설정과 비교하여 고유한 특성을 지닌다는 점을 강조하였다.


---

*Generated on 2025-09-24 04:00:18*