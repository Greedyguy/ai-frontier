---
keywords:
  - Transformer
  - Symbolic Regression
  - Pre-training Data Distribution
  - Out-of-Distribution Generalization
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19849
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:51:03.038500",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Symbolic Regression",
    "Pre-training Data Distribution",
    "Out-of-Distribution Generalization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Symbolic Regression": 0.8,
    "Pre-training Data Distribution": 0.75,
    "Out-of-Distribution Generalization": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer-based models",
        "canonical": "Transformer",
        "aliases": [
          "Transformer models",
          "Transformer architecture"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational technology in machine learning, linking well with a wide range of topics.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Symbolic regression",
        "canonical": "Symbolic Regression",
        "aliases": [
          "Symbolic formula discovery"
        ],
        "category": "unique_technical",
        "rationale": "Symbolic regression is a specialized area of study that connects to mathematical modeling and data fitting.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Pre-training distribution",
        "canonical": "Pre-training Data Distribution",
        "aliases": [
          "Training data distribution"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding data distribution is crucial for evaluating model generalization and performance.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      },
      {
        "surface": "Out-of-distribution challenges",
        "canonical": "Out-of-Distribution Generalization",
        "aliases": [
          "OOD challenges",
          "Generalization beyond training"
        ],
        "category": "specific_connectable",
        "rationale": "Out-of-distribution generalization is a critical aspect of model robustness and applicability.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "generalization",
      "performance",
      "practitioners"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Transformer-based models",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Symbolic regression",
      "resolved_canonical": "Symbolic Regression",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Pre-training distribution",
      "resolved_canonical": "Pre-training Data Distribution",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Out-of-distribution challenges",
      "resolved_canonical": "Out-of-Distribution Generalization",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Analyzing Generalization in Pre-Trained Symbolic Regression

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19849.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19849](https://arxiv.org/abs/2509.19849)

## 🔗 유사한 논문
- [[2025-09-22/Improving Monte Carlo Tree Search for Symbolic Regression_20250922|Improving Monte Carlo Tree Search for Symbolic Regression]] (81.6% similar)
- [[2025-09-23/Evolution of Concepts in Language Model Pre-Training_20250923|Evolution of Concepts in Language Model Pre-Training]] (80.2% similar)
- [[2025-09-18/Pre-training under infinite compute_20250918|Pre-training under infinite compute]] (80.1% similar)
- [[2025-09-24/Is Pre-training Truly Better Than Meta-Learning?_20250924|Is Pre-training Truly Better Than Meta-Learning?]] (79.9% similar)
- [[2025-09-25/Linear Transformers Implicitly Discover Unified Numerical Algorithms_20250925|Linear Transformers Implicitly Discover Unified Numerical Algorithms]] (79.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Pre-training Data Distribution|Pre-training Data Distribution]], [[keywords/Out-of-Distribution Generalization|Out-of-Distribution Generalization]]
**⚡ Unique Technical**: [[keywords/Symbolic Regression|Symbolic Regression]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19849v1 Announce Type: cross 
Abstract: Symbolic regression algorithms search a space of mathematical expressions for formulas that explain given data. Transformer-based models have emerged as a promising, scalable approach shifting the expensive combinatorial search to a large-scale pre-training phase. However, the success of these models is critically dependent on their pre-training data. Their ability to generalize to problems outside of this pre-training distribution remains largely unexplored. In this work, we conduct a systematic empirical study to evaluate the generalization capabilities of pre-trained, transformer-based symbolic regression. We rigorously test performance both within the pre-training distribution and on a series of out-of-distribution challenges for several state of the art approaches. Our findings reveal a significant dichotomy: while pre-trained models perform well in-distribution, the performance consistently degrades in out-of-distribution scenarios. We conclude that this generalization gap is a critical barrier for practitioners, as it severely limits the practical use of pre-trained approaches for real-world applications.

## 📝 요약

이 논문은 수식 회귀 알고리즘에서 변환기 기반 모델의 일반화 능력을 평가합니다. 변환기 기반 모델은 대규모 사전 학습을 통해 수식 탐색을 효율화하지만, 사전 학습 데이터에 크게 의존합니다. 연구 결과, 사전 학습 분포 내에서는 성능이 우수하지만, 분포 외 문제에서는 성능이 저하되는 경향이 발견되었습니다. 이는 실제 응용에서 사전 학습된 모델의 활용에 중요한 제약이 될 수 있음을 시사합니다.

## 🎯 주요 포인트

- 1. 기호 회귀 알고리즘은 주어진 데이터를 설명하는 수학적 표현식을 탐색하는 방법이다.
- 2. 트랜스포머 기반 모델은 대규모 사전 학습을 통해 비용이 많이 드는 조합적 탐색을 대체하는 유망한 접근 방식으로 부상했다.
- 3. 사전 학습된 트랜스포머 기반 기호 회귀의 일반화 능력을 평가하기 위한 체계적인 실증 연구를 수행했다.
- 4. 연구 결과, 사전 학습된 모델은 사전 학습 분포 내에서는 성능이 뛰어나지만, 분포 외 시나리오에서는 성능이 일관되게 저하되는 것으로 나타났다.
- 5. 이러한 일반화 격차는 실제 응용에서 사전 학습 접근 방식의 실용성을 심각하게 제한하는 중요한 장애물로 결론지었다.


---

*Generated on 2025-09-25 15:51:03*