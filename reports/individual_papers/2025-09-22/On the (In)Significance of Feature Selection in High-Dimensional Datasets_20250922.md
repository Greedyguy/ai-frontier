---
keywords:
  - Feature Selection
  - High-Dimensional Data
  - Computational Genomics
  - Predictive Modeling
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2508.03593
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:10:17.373677",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Feature Selection",
    "High-Dimensional Data",
    "Computational Genomics",
    "Predictive Modeling"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Feature Selection": 0.78,
    "High-Dimensional Data": 0.72,
    "Computational Genomics": 0.77,
    "Predictive Modeling": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Feature Selection",
        "canonical": "Feature Selection",
        "aliases": [
          "FS"
        ],
        "category": "unique_technical",
        "rationale": "Feature Selection is central to the paper's argument and challenges existing assumptions, making it a unique technical focus.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "High-Dimensional Datasets",
        "canonical": "High-Dimensional Data",
        "aliases": [
          "High-Dimensional Datasets"
        ],
        "category": "broad_technical",
        "rationale": "High-Dimensional Data is a fundamental concept in machine learning, relevant to understanding the paper's context.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      },
      {
        "surface": "Computational Genomics",
        "canonical": "Computational Genomics",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Computational Genomics is a key application area mentioned, linking the paper to a specific domain.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Predictive Performance",
        "canonical": "Predictive Modeling",
        "aliases": [
          "Predictive Performance"
        ],
        "category": "broad_technical",
        "rationale": "Predictive Modeling is a core concept in evaluating feature selection methods, relevant across datasets.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "microarray",
      "mass spectrometry",
      "imaging"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Feature Selection",
      "resolved_canonical": "Feature Selection",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "High-Dimensional Datasets",
      "resolved_canonical": "High-Dimensional Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Computational Genomics",
      "resolved_canonical": "Computational Genomics",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Predictive Performance",
      "resolved_canonical": "Predictive Modeling",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# On the (In)Significance of Feature Selection in High-Dimensional Datasets

**Korean Title:** 고차원 데이터셋에서 특징 선택의 (비)중요성에 관하여

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2508.03593.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2508.03593](https://arxiv.org/abs/2508.03593)

## 🔗 유사한 논문
- [[2025-09-22/Nonconvex Regularization for Feature Selection in Reinforcement Learning_20250922|Nonconvex Regularization for Feature Selection in Reinforcement Learning]] (79.2% similar)
- [[2025-09-22/Top-$k$ Feature Importance Ranking_20250922|Top-$k$ Feature Importance Ranking]] (78.9% similar)
- [[2025-09-17/Beyond Correlation_ Causal Multi-View Unsupervised Feature Selection Learning_20250917|Beyond Correlation: Causal Multi-View Unsupervised Feature Selection Learning]] (78.7% similar)
- [[2025-09-22/IEFS-GMB_ Gradient Memory Bank-Guided Feature Selection Based on Information Entropy for EEG Classification of Neurological Disorders_20250922|IEFS-GMB: Gradient Memory Bank-Guided Feature Selection Based on Information Entropy for EEG Classification of Neurological Disorders]] (78.5% similar)
- [[2025-09-18/Data coarse graining can improve model performance_20250918|Data coarse graining can improve model performance]] (77.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/High-Dimensional Data|High-Dimensional Data]], [[keywords/Predictive Modeling|Predictive Modeling]]
**🔗 Specific Connectable**: [[keywords/Computational Genomics|Computational Genomics]]
**⚡ Unique Technical**: [[keywords/Feature Selection|Feature Selection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.03593v2 Announce Type: replace 
Abstract: Feature selection (FS) is assumed to improve predictive performance and identify meaningful features in high-dimensional datasets. Surprisingly, small random subsets of features (0.02-1%) match or outperform the predictive performance of both full feature sets and FS across 28 out of 30 diverse datasets (microarray, bulk and single-cell RNA-Seq, mass spectrometry, imaging, etc.). In short, any arbitrary set of features is as good as any other (with surprisingly low variance in results) - so how can a particular set of selected features be "important" if they perform no better than an arbitrary set? These results challenge the assumption that computationally selected features reliably capture meaningful signals, emphasizing the importance of rigorous validation before interpreting selected features as actionable, particularly in computational genomics.

## 🔍 Abstract (한글 번역)

arXiv:2508.03593v2 발표 유형: 교체  
초록: 특징 선택(FS)은 예측 성능을 향상시키고 고차원 데이터셋에서 의미 있는 특징을 식별할 수 있다고 가정됩니다. 놀랍게도, 작은 무작위 특징 하위 집합(0.02-1%)이 전체 특징 집합과 FS의 예측 성능을 30개의 다양한 데이터셋(마이크로어레이, 벌크 및 단일 세포 RNA-Seq, 질량 분석, 이미지 등) 중 28개에서 맞추거나 능가합니다. 요컨대, 임의의 특징 집합은 다른 어떤 것과도 마찬가지로 좋습니다(결과의 분산이 놀라울 정도로 낮음) - 그렇다면 특정 선택된 특징 집합이 "중요하다"고 할 수 있는 이유는 무엇입니까, 임의의 집합보다 더 나은 성능을 보이지 않는다면? 이러한 결과는 계산적으로 선택된 특징이 의미 있는 신호를 신뢰성 있게 포착한다는 가정을 도전하며, 특히 계산 유전체학에서 선택된 특징을 실행 가능한 것으로 해석하기 전에 엄격한 검증의 중요성을 강조합니다.

## 📝 요약

이 논문은 고차원 데이터셋에서 특징 선택(FS)이 예측 성능을 향상시키고 의미 있는 특징을 식별한다고 가정하지만, 실제로는 무작위로 선택된 소규모 특징 집합(0.02-1%)이 전체 특징 집합이나 FS의 예측 성능을 능가하거나 동등하다는 것을 발견했습니다. 30개의 다양한 데이터셋 중 28개에서 이러한 결과가 나타났으며, 이는 특정 특징 집합이 임의의 집합보다 중요하다고 해석하기 어렵게 만듭니다. 이 연구는 계산적으로 선택된 특징이 의미 있는 신호를 포착한다는 가정을 재고할 필요성을 제기하며, 특히 계산 유전체학에서 선택된 특징을 해석하기 전에 엄격한 검증이 필요함을 강조합니다.

## 🎯 주요 포인트

- 1. 고차원 데이터셋에서 특징 선택은 예측 성능을 향상시키고 의미 있는 특징을 식별하는 것으로 가정된다.
- 2. 30개의 다양한 데이터셋 중 28개에서 작은 무작위 특징 하위 집합이 전체 특징 집합과 특징 선택을 능가하거나 동등한 예측 성능을 보였다.
- 3. 임의의 특징 집합이 선택된 특징 집합과 동등한 성능을 보이므로, 특정 특징 집합의 중요성을 주장하기 어렵다.
- 4. 이 결과는 계산적으로 선택된 특징이 의미 있는 신호를 포착한다는 가정을 도전하며, 선택된 특징을 실행 가능한 것으로 해석하기 전에 엄격한 검증의 중요성을 강조한다.
- 5. 특히 계산 유전체학에서 선택된 특징을 해석하기 전에 철저한 검증이 필요하다.


---

*Generated on 2025-09-23 11:10:17*