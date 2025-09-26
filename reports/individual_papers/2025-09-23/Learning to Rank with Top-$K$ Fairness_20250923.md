---
keywords:
  - Machine Learning
  - Top-K Exposure Disparity
  - List-wise Learning-to-Rank
  - Stochastic Optimization
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.18067
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:01:46.225812",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Learning",
    "Top-K Exposure Disparity",
    "List-wise Learning-to-Rank",
    "Stochastic Optimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Learning": 0.7,
    "Top-K Exposure Disparity": 0.85,
    "List-wise Learning-to-Rank": 0.8,
    "Stochastic Optimization": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "ranking models",
        "canonical": "Machine Learning",
        "aliases": [
          "ranker",
          "ranking systems"
        ],
        "category": "broad_technical",
        "rationale": "Ranking models are a fundamental aspect of machine learning, connecting well with existing concepts in the field.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "top-K exposure disparity",
        "canonical": "Top-K Exposure Disparity",
        "aliases": [
          "top-K fairness",
          "top-K disparity"
        ],
        "category": "unique_technical",
        "rationale": "This concept introduces a novel fairness metric specific to top-K rankings, which is crucial for linking fairness in ranking contexts.",
        "novelty_score": 0.78,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      },
      {
        "surface": "list-wise learning-to-rank framework",
        "canonical": "List-wise Learning-to-Rank",
        "aliases": [
          "list-wise ranking",
          "learning to rank"
        ],
        "category": "specific_connectable",
        "rationale": "This framework is a specific method within machine learning that addresses ranking fairness, making it a strong link candidate.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "stochastic optimization algorithms",
        "canonical": "Stochastic Optimization",
        "aliases": [
          "stochastic algorithms",
          "optimization"
        ],
        "category": "specific_connectable",
        "rationale": "Stochastic optimization is a key technique in machine learning, linking well with optimization methods in the field.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.68,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "ranking beyond top-K",
      "decision-makers",
      "resource allocation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "ranking models",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "top-K exposure disparity",
      "resolved_canonical": "Top-K Exposure Disparity",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "list-wise learning-to-rank framework",
      "resolved_canonical": "List-wise Learning-to-Rank",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "stochastic optimization algorithms",
      "resolved_canonical": "Stochastic Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.68,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Learning to Rank with Top-$K$ Fairness

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18067.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.18067](https://arxiv.org/abs/2509.18067)

## 🔗 유사한 논문
- [[2025-09-22/Top-$k$ Feature Importance Ranking_20250922|Top-$k$ Feature Importance Ranking]] (79.9% similar)
- [[2025-09-17/APFEx_ Adaptive Pareto Front Explorer for Intersectional Fairness_20250917|APFEx: Adaptive Pareto Front Explorer for Intersectional Fairness]] (79.7% similar)
- [[2025-09-22/Where Fact Ends and Fairness Begins_ Redefining AI Bias Evaluation through Cognitive Biases_20250922|Where Fact Ends and Fairness Begins: Redefining AI Bias Evaluation through Cognitive Biases]] (78.4% similar)
- [[2025-09-19/Let's Grow an Unbiased Community_ Guiding the Fairness of Graphs via New Links_20250919|Let's Grow an Unbiased Community: Guiding the Fairness of Graphs via New Links]] (78.2% similar)
- [[2025-09-22/On Optimal Steering to Achieve Exact Fairness_20250922|On Optimal Steering to Achieve Exact Fairness]] (77.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**🔗 Specific Connectable**: [[keywords/List-wise Learning-to-Rank|List-wise Learning-to-Rank]], [[keywords/Stochastic Optimization|Stochastic Optimization]]
**⚡ Unique Technical**: [[keywords/Top-K Exposure Disparity|Top-K Exposure Disparity]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18067v1 Announce Type: new 
Abstract: Fairness in ranking models is crucial, as disparities in exposure can disproportionately affect protected groups. Most fairness-aware ranking systems focus on ensuring comparable average exposure for groups across the entire ranked list, which may not fully address real-world concerns. For example, when a ranking model is used for allocating resources among candidates or disaster hotspots, decision-makers often prioritize only the top-$K$ ranked items, while the ranking beyond top-$K$ becomes less relevant. In this paper, we propose a list-wise learning-to-rank framework that addresses the issues of inequalities in top-$K$ rankings at training time. Specifically, we propose a top-$K$ exposure disparity measure that extends the classic exposure disparity metric in a ranked list. We then learn a ranker to balance relevance and fairness in top-$K$ rankings. Since direct top-$K$ selection is computationally expensive for a large number of items, we transform the non-differentiable selection process into a differentiable objective function and develop efficient stochastic optimization algorithms to achieve both high accuracy and sufficient fairness. Extensive experiments demonstrate that our method outperforms existing methods.

## 📝 요약

이 논문은 랭킹 모델에서의 공정성을 개선하기 위한 새로운 접근법을 제안합니다. 기존의 공정성 인식 랭킹 시스템은 전체 목록에서 그룹 간 평균 노출을 보장하는 데 중점을 두지만, 이는 실제 문제를 완전히 해결하지 못할 수 있습니다. 특히, 자원 배분이나 재난 대응과 같은 상황에서는 상위 $K$개의 항목이 더 중요합니다. 본 연구에서는 학습 시 상위 $K$ 랭킹의 불평등 문제를 해결하기 위한 리스트 기반 학습-투-랭크 프레임워크를 제안합니다. 이를 위해 상위 $K$ 노출 불균형 측정 방법을 도입하고, 관련성과 공정성을 균형 있게 고려하는 랭커를 학습합니다. 또한, 비차별적 선택 과정을 차별 가능한 목표 함수로 변환하고 효율적인 확률적 최적화 알고리즘을 개발하여 높은 정확도와 충분한 공정성을 달성합니다. 실험 결과, 제안된 방법이 기존 방법보다 우수함을 입증합니다.

## 🎯 주요 포인트

- 1. 랭킹 모델에서의 공정성은 보호 그룹에 대한 노출 불균형을 줄이는 데 중요하다.
- 2. 기존의 공정성 인식 랭킹 시스템은 전체 랭킹 리스트에서 그룹 간 평균 노출을 비교하는 데 초점을 맞추지만, 이는 실제 문제를 완전히 해결하지 못할 수 있다.
- 3. 본 논문에서는 훈련 시점에서 상위-$K$ 랭킹의 불평등 문제를 해결하는 리스트 기반 학습-랭킹 프레임워크를 제안한다.
- 4. 상위-$K$ 노출 불균형 측정을 제안하여 기존의 노출 불균형 메트릭을 확장하고, 관련성과 공정성을 균형 있게 고려하는 랭커를 학습한다.
- 5. 제안된 방법은 기존 방법들보다 뛰어난 성능을 보이며, 효율적인 확률적 최적화 알고리즘을 통해 높은 정확도와 충분한 공정성을 달성한다.


---

*Generated on 2025-09-24 02:01:46*