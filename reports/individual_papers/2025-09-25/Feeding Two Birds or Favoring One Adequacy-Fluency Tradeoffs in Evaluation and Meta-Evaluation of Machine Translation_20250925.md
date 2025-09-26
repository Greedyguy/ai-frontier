---
keywords:
  - Machine Translation
  - Adequacy-Fluency Tradeoff
  - Meta-Evaluation
  - Translation Systems
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.20287
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:05:15.236262",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Translation",
    "Adequacy-Fluency Tradeoff",
    "Meta-Evaluation",
    "Translation Systems"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Translation": 0.85,
    "Adequacy-Fluency Tradeoff": 0.78,
    "Meta-Evaluation": 0.77,
    "Translation Systems": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Machine Translation",
        "canonical": "Machine Translation",
        "aliases": [
          "MT"
        ],
        "category": "broad_technical",
        "rationale": "Machine Translation is a core topic of the paper and connects to broader discussions in Natural Language Processing.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Adequacy-Fluency Tradeoff",
        "canonical": "Adequacy-Fluency Tradeoff",
        "aliases": [
          "Adequacy vs Fluency"
        ],
        "category": "unique_technical",
        "rationale": "The tradeoff is a unique focus of the paper, providing a specific angle on evaluation metrics.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Meta-Evaluation",
        "canonical": "Meta-Evaluation",
        "aliases": [
          "Meta Evaluation"
        ],
        "category": "specific_connectable",
        "rationale": "Meta-evaluation is crucial for understanding the evaluation of metrics and is a key concept in the paper.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "Translation Systems",
        "canonical": "Translation Systems",
        "aliases": [
          "Translation Models"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding the composition of translation systems is essential for the proposed method in the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "evaluation",
      "metrics",
      "bias"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Machine Translation",
      "resolved_canonical": "Machine Translation",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Adequacy-Fluency Tradeoff",
      "resolved_canonical": "Adequacy-Fluency Tradeoff",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Meta-Evaluation",
      "resolved_canonical": "Meta-Evaluation",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Translation Systems",
      "resolved_canonical": "Translation Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# Feeding Two Birds or Favoring One? Adequacy-Fluency Tradeoffs in Evaluation and Meta-Evaluation of Machine Translation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20287.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.20287](https://arxiv.org/abs/2509.20287)

## 🔗 유사한 논문
- [[2025-09-18/Audio-Based Crowd-Sourced Evaluation of Machine Translation Quality_20250918|Audio-Based Crowd-Sourced Evaluation of Machine Translation Quality]] (85.3% similar)
- [[2025-09-23/Specification-Aware Machine Translation and Evaluation for Purpose Alignment_20250923|Specification-Aware Machine Translation and Evaluation for Purpose Alignment]] (82.5% similar)
- [[2025-09-22/Translationese-index_ Using Likelihood Ratios for Graded and Generalizable Measurement of Translationese_20250922|Translationese-index: Using Likelihood Ratios for Graded and Generalizable Measurement of Translationese]] (82.1% similar)
- [[2025-09-23/Assumed Identities_ Quantifying Gender Bias in Machine Translation of Gender-Ambiguous Occupational Terms_20250923|Assumed Identities: Quantifying Gender Bias in Machine Translation of Gender-Ambiguous Occupational Terms]] (81.9% similar)
- [[2025-09-17/Long-context Reference-based MT Quality Estimation_20250917|Long-context Reference-based MT Quality Estimation]] (81.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Translation|Machine Translation]]
**🔗 Specific Connectable**: [[keywords/Meta-Evaluation|Meta-Evaluation]], [[keywords/Translation Systems|Translation Systems]]
**⚡ Unique Technical**: [[keywords/Adequacy-Fluency Tradeoff|Adequacy-Fluency Tradeoff]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20287v1 Announce Type: cross 
Abstract: We investigate the tradeoff between adequacy and fluency in machine translation. We show the severity of this tradeoff at the evaluation level and analyze where popular metrics fall within it. Essentially, current metrics generally lean toward adequacy, meaning that their scores correlate more strongly with the adequacy of translations than with fluency. More importantly, we find that this tradeoff also persists at the meta-evaluation level, and that the standard WMT meta-evaluation favors adequacy-oriented metrics over fluency-oriented ones. We show that this bias is partially attributed to the composition of the systems included in the meta-evaluation datasets. To control this bias, we propose a method that synthesizes translation systems in meta-evaluation. Our findings highlight the importance of understanding this tradeoff in meta-evaluation and its impact on metric rankings.

## 📝 요약

이 논문은 기계 번역에서 적합성과 유창성 간의 상충 관계를 조사합니다. 저자들은 현재의 평가 지표들이 대체로 적합성에 치우쳐 있으며, 이는 번역의 적합성과 더 강하게 상관된다고 주장합니다. 또한, WMT 메타 평가가 적합성 중심의 지표를 선호하는 경향이 있음을 발견하고, 이는 메타 평가 데이터셋에 포함된 시스템 구성에 기인한다고 분석합니다. 이러한 편향을 제어하기 위해 번역 시스템을 합성하는 방법을 제안하며, 메타 평가에서의 상충 관계 이해와 지표 순위에 미치는 영향을 강조합니다.

## 🎯 주요 포인트

- 1. 기계 번역에서 적절성과 유창성 간의 상충 관계를 조사하고, 평가 수준에서 이 상충 관계의 심각성을 보여줍니다.
- 2. 현재의 평가지표는 일반적으로 적절성에 치우쳐 있으며, 번역의 적절성과 더 강하게 상관관계를 가집니다.
- 3. WMT 메타 평가가 유창성보다 적절성 지향의 지표를 선호하는 경향이 있음을 발견했습니다.
- 4. 메타 평가 데이터셋에 포함된 시스템의 구성 때문에 이러한 편향이 부분적으로 발생하며, 이를 제어하기 위한 번역 시스템 합성 방법을 제안합니다.
- 5. 메타 평가에서의 상충 관계 이해와 지표 순위에 미치는 영향의 중요성을 강조합니다.


---

*Generated on 2025-09-25 16:05:15*