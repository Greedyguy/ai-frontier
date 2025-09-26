---
keywords:
  - Algorithm Selection
  - Meta-Learning
  - Recommender Systems
  - Algorithm Features
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.20134
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T17:01:02.472676",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Algorithm Selection",
    "Meta-Learning",
    "Recommender Systems",
    "Algorithm Features"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Algorithm Selection": 0.83,
    "Meta-Learning": 0.81,
    "Recommender Systems": 0.79,
    "Algorithm Features": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Algorithm Selection Problem",
        "canonical": "Algorithm Selection",
        "aliases": [
          "Algorithm Choice",
          "Algorithm Selection Task"
        ],
        "category": "unique_technical",
        "rationale": "Algorithm Selection is central to the paper's focus and connects to broader discussions in machine learning.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.83
      },
      {
        "surface": "Meta-Learning",
        "canonical": "Meta-Learning",
        "aliases": [
          "Meta Learning"
        ],
        "category": "broad_technical",
        "rationale": "Meta-Learning is a key approach discussed and connects to various machine learning strategies.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.67,
        "link_intent_score": 0.81
      },
      {
        "surface": "Recommender Systems",
        "canonical": "Recommender Systems",
        "aliases": [
          "Recommendation Systems"
        ],
        "category": "specific_connectable",
        "rationale": "Recommender Systems are the primary application domain of the study, linking to a wide range of related research.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.79
      },
      {
        "surface": "Algorithm Features",
        "canonical": "Algorithm Features",
        "aliases": [
          "Algorithm Characteristics",
          "Algorithm Properties"
        ],
        "category": "unique_technical",
        "rationale": "Algorithm Features are a novel aspect of the paper's approach, distinguishing it from traditional methods.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "No Free Lunch",
      "Single Best Algorithm",
      "NDCG@10"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Algorithm Selection Problem",
      "resolved_canonical": "Algorithm Selection",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.83
      }
    },
    {
      "candidate_surface": "Meta-Learning",
      "resolved_canonical": "Meta-Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.67,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Recommender Systems",
      "resolved_canonical": "Recommender Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Algorithm Features",
      "resolved_canonical": "Algorithm Features",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Intelligent Algorithm Selection for Recommender Systems: Meta-Learning via in-depth algorithm feature engineering

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20134.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.20134](https://arxiv.org/abs/2509.20134)

## 🔗 유사한 논문
- [[2025-09-23/A Knowledge Graph-based Retrieval-Augmented Generation Framework for Algorithm Selection in the Facility Layout Problem_20250923|A Knowledge Graph-based Retrieval-Augmented Generation Framework for Algorithm Selection in the Facility Layout Problem]] (82.0% similar)
- [[2025-09-22/Instance Generation for Meta-Black-Box Optimization through Latent Space Reverse Engineering_20250922|Instance Generation for Meta-Black-Box Optimization through Latent Space Reverse Engineering]] (81.0% similar)
- [[2025-09-24/Development of Deep Learning Optimizers_ Approaches, Concepts, and Update Rules_20250924|Development of Deep Learning Optimizers: Approaches, Concepts, and Update Rules]] (81.0% similar)
- [[2025-09-22/Nonconvex Regularization for Feature Selection in Reinforcement Learning_20250922|Nonconvex Regularization for Feature Selection in Reinforcement Learning]] (80.5% similar)
- [[2025-09-23/AICO_ Feature Significance Tests for Supervised Learning_20250923|AICO: Feature Significance Tests for Supervised Learning]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Meta-Learning|Meta-Learning]]
**🔗 Specific Connectable**: [[keywords/Recommender Systems|Recommender Systems]]
**⚡ Unique Technical**: [[keywords/Algorithm Selection|Algorithm Selection]], [[keywords/Algorithm Features|Algorithm Features]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20134v1 Announce Type: cross 
Abstract: The "No Free Lunch" theorem dictates that no single recommender algorithm is optimal for all users, creating a significant Algorithm Selection Problem. Standard meta-learning approaches aim to solve this by selecting an algorithm based on user features, but treat the fundamentally diverse algorithms themselves as equivalent, "black-box" choices. This thesis investigates the impact of overcoming this limitation by engineering a comprehensive feature set to explicitly characterize the algorithms themselves. We combine static code metrics, Abstract Syntax Tree properties, behavioral performance landmarks, and high-level conceptual features. We evaluate two meta-learners across five datasets: a baseline using only user features and our proposed model using both user and algorithm features. Our results show that the meta-learner augmented with algorithm features achieves an average NDCG@10 of 0.143, a statistically significant improvement of 11.7% over the Single Best Algorithm baseline (0.128). However, we found that the inclusion of algorithm features did not lead to an improvement in overall NDCG@10 over the meta learner using only user features (0.144). While adding algorithm features to the meta-learner did improve its Top-1 selection accuracy (+16.1%), this was counterbalanced by leading to a lower Top-3 accuracy (-10.7%). We conclude that for the per-user algorithm selection task in recommender systems, the predictive power of user features is overwhelmingly dominant. While algorithm features improve selection precision, unlocking their potential to boost overall performance remains a non-trivial challenge.

## 📝 요약

이 논문은 추천 시스템에서 알고리즘 선택 문제를 해결하기 위해 알고리즘 자체의 특징을 명시적으로 활용하는 방법을 제안합니다. 기존 메타러닝 접근법은 사용자 특징에 기반하여 알고리즘을 선택하지만, 알고리즘 자체를 '블랙박스'로 취급하는 한계를 가집니다. 저자는 정적 코드 메트릭, 추상 구문 트리, 행동 성능 지표, 고수준 개념 특징을 결합하여 알고리즘을 특징화했습니다. 다섯 개의 데이터셋에서 두 가지 메타러너를 평가한 결과, 알고리즘 특징을 포함한 메타러너가 NDCG@10에서 11.7% 향상된 성능을 보였으나, 사용자 특징만을 사용한 메타러너와의 성능 차이는 없었습니다. 알고리즘 특징은 선택 정확성을 높였지만, 전체 성능 향상에는 한계가 있음을 발견했습니다. 사용자 특징의 예측력이 여전히 지배적이며, 알고리즘 특징의 잠재력을 완전히 발휘하는 것은 여전히 어려운 과제입니다.

## 🎯 주요 포인트

- 1. "No Free Lunch" 정리에 따라 모든 사용자에게 최적의 추천 알고리즘은 존재하지 않으며, 이는 알고리즘 선택 문제를 야기한다.
- 2. 기존 메타러닝 접근법은 사용자 특징에 기반하여 알고리즘을 선택하지만, 알고리즘 자체를 "블랙박스"로 취급한다.
- 3. 본 연구는 알고리즘을 명시적으로 특성화하는 포괄적인 특징 세트를 설계하여 이 한계를 극복하려고 시도한다.
- 4. 알고리즘 특징을 포함한 메타러너는 NDCG@10에서 평균 0.143을 기록하며, 이는 단일 최적 알고리즘 기준보다 11.7% 향상된 결과이다.
- 5. 사용자 특징의 예측력이 지배적이며, 알고리즘 특징이 선택 정확도를 개선하지만 전체 성능 향상으로 이어지지는 않는다.


---

*Generated on 2025-09-25 17:01:02*