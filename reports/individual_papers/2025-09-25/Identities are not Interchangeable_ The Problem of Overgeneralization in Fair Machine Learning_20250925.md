---
keywords:
  - Fair Machine Learning
  - Identity Axis in ML
  - Context Specificity in ML
  - Forms of Oppression in ML
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2505.04038
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:38:42.849729",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Fair Machine Learning",
    "Identity Axis in ML",
    "Context Specificity in ML",
    "Forms of Oppression in ML"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Fair Machine Learning": 0.85,
    "Identity Axis in ML": 0.8,
    "Context Specificity in ML": 0.78,
    "Forms of Oppression in ML": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "fair machine learning",
        "canonical": "Fair Machine Learning",
        "aliases": [
          "fairness in ML",
          "equitable ML"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is central to the paper's discussion on addressing discrimination in machine learning.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      },
      {
        "surface": "identity axis",
        "canonical": "Identity Axis in ML",
        "aliases": [
          "identity factors",
          "identity dimensions"
        ],
        "category": "unique_technical",
        "rationale": "The paper introduces this as a critical factor in understanding discrimination across different identities in ML.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.8
      },
      {
        "surface": "context specificity",
        "canonical": "Context Specificity in ML",
        "aliases": [
          "contextual adaptation",
          "context-aware ML"
        ],
        "category": "unique_technical",
        "rationale": "Highlighting the need for context-specific approaches in ML can improve fairness and reduce overlooked harms.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "forms of oppression",
        "canonical": "Forms of Oppression in ML",
        "aliases": [
          "oppression types",
          "discrimination forms"
        ],
        "category": "unique_technical",
        "rationale": "Understanding different forms of oppression is crucial for developing fair ML systems.",
        "novelty_score": 0.66,
        "connectivity_score": 0.67,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "generalizability",
      "model architecture",
      "domains",
      "contexts"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "fair machine learning",
      "resolved_canonical": "Fair Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "identity axis",
      "resolved_canonical": "Identity Axis in ML",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "context specificity",
      "resolved_canonical": "Context Specificity in ML",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "forms of oppression",
      "resolved_canonical": "Forms of Oppression in ML",
      "decision": "linked",
      "scores": {
        "novelty": 0.66,
        "connectivity": 0.67,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Identities are not Interchangeable: The Problem of Overgeneralization in Fair Machine Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2505.04038.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2505.04038](https://arxiv.org/abs/2505.04038)

## 🔗 유사한 논문
- [[2025-09-22/Algorithmic Fairness_ Not a Purely Technical but Socio-Technical Property_20250922|Algorithmic Fairness: Not a Purely Technical but Socio-Technical Property]] (87.8% similar)
- [[2025-09-24/APFEx_ Adaptive Pareto Front Explorer for Intersectional Fairness_20250924|APFEx: Adaptive Pareto Front Explorer for Intersectional Fairness]] (84.4% similar)
- [[2025-09-17/APFEx_ Adaptive Pareto Front Explorer for Intersectional Fairness_20250917|APFEx: Adaptive Pareto Front Explorer for Intersectional Fairness]] (83.6% similar)
- [[2025-09-22/On Optimal Steering to Achieve Exact Fairness_20250922|On Optimal Steering to Achieve Exact Fairness]] (81.3% similar)
- [[2025-09-25/Blind Men and the Elephant_ Diverse Perspectives on Gender Stereotypes in Benchmark Datasets_20250925|Blind Men and the Elephant: Diverse Perspectives on Gender Stereotypes in Benchmark Datasets]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Fair Machine Learning|Fair Machine Learning]]
**⚡ Unique Technical**: [[keywords/Identity Axis in ML|Identity Axis in ML]], [[keywords/Context Specificity in ML|Context Specificity in ML]], [[keywords/Forms of Oppression in ML|Forms of Oppression in ML]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.04038v2 Announce Type: replace-cross 
Abstract: A key value proposition of machine learning is generalizability: the same methods and model architecture should be able to work across different domains and different contexts. While powerful, this generalization can sometimes go too far, and miss the importance of the specifics. In this work, we look at how fair machine learning has often treated as interchangeable the identity axis along which discrimination occurs. In other words, racism is measured and mitigated the same way as sexism, as ableism, as ageism. Disciplines outside of computer science have pointed out both the similarities and differences between these different forms of oppression, and in this work we draw out the implications for fair machine learning. While certainly not all aspects of fair machine learning need to be tailored to the specific form of oppression, there is a pressing need for greater attention to such specificity than is currently evident. Ultimately, context specificity can deepen our understanding of how to build more fair systems, widen our scope to include currently overlooked harms, and, almost paradoxically, also help to narrow our scope and counter the fear of an infinite number of group-specific methods of analysis.

## 📝 요약

이 논문은 공정한 머신러닝에서 다양한 차별 축을 동일하게 다루는 문제를 지적합니다. 인종차별, 성차별, 장애인 차별, 연령 차별 등이 동일한 방식으로 측정 및 완화되는 경향이 있지만, 이는 각 차별의 구체성을 간과할 수 있습니다. 저자들은 컴퓨터 과학 외의 분야에서 제기된 차별의 유사성과 차이점을 머신러닝에 적용하여, 특정 억압 형태에 맞춘 접근이 필요함을 강조합니다. 이를 통해 더 공정한 시스템을 구축하고, 간과된 피해를 포착하며, 분석 방법의 범위를 좁히는 데 기여할 수 있음을 제안합니다.

## 🎯 주요 포인트

- 1. 기계 학습의 일반화 능력은 강력하지만, 때로는 구체성을 놓칠 수 있다.
- 2. 공정한 기계 학습에서는 인종차별, 성차별, 장애인 차별, 연령 차별을 동일하게 취급하는 경향이 있다.
- 3. 컴퓨터 과학 외의 학문 분야에서는 이러한 억압 형태 간의 유사점과 차이점을 지적하고 있다.
- 4. 공정한 기계 학습에서는 억압의 특정 형태에 대한 세부적인 주의가 필요하다.
- 5. 맥락의 특수성은 더 공정한 시스템을 구축하고 간과된 피해를 포함하며, 분석 방법의 범위를 좁히는 데 도움을 줄 수 있다.


---

*Generated on 2025-09-26 08:38:42*