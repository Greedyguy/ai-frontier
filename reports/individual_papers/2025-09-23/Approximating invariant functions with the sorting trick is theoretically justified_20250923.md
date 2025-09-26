---
keywords:
  - Group Invariance
  - Canonicalization
  - Reproducing Kernels
  - Approximation Theory
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2403.01671
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:32:10.037535",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Group Invariance",
    "Canonicalization",
    "Reproducing Kernels",
    "Approximation Theory"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Group Invariance": 0.78,
    "Canonicalization": 0.8,
    "Reproducing Kernels": 0.77,
    "Approximation Theory": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "group invariance",
        "canonical": "Group Invariance",
        "aliases": [
          "invariance structure"
        ],
        "category": "unique_technical",
        "rationale": "Group invariance is a key concept in the paper, central to the discussed methods, and offers unique insights into the theoretical framework.",
        "novelty_score": 0.65,
        "connectivity_score": 0.68,
        "specificity_score": 0.72,
        "link_intent_score": 0.78
      },
      {
        "surface": "canonicalization",
        "canonical": "Canonicalization",
        "aliases": [
          "sorting trick"
        ],
        "category": "unique_technical",
        "rationale": "Canonicalization is a core technique analyzed in the paper, providing a unique perspective on approximation theory.",
        "novelty_score": 0.7,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.8
      },
      {
        "surface": "reproducing kernels",
        "canonical": "Reproducing Kernels",
        "aliases": [
          "kernel methods"
        ],
        "category": "specific_connectable",
        "rationale": "Reproducing kernels are fundamental to the mathematical analysis presented, linking to broader kernel methods in machine learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "approximation theory",
        "canonical": "Approximation Theory",
        "aliases": [
          "theoretical approximation"
        ],
        "category": "broad_technical",
        "rationale": "Approximation theory underpins the paper's theoretical contributions, connecting to a wide range of mathematical and computational topics.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.65,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "frame averaging",
      "non-differentiability",
      "eigenvalue decay rates"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "group invariance",
      "resolved_canonical": "Group Invariance",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.68,
        "specificity": 0.72,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "canonicalization",
      "resolved_canonical": "Canonicalization",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "reproducing kernels",
      "resolved_canonical": "Reproducing Kernels",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "approximation theory",
      "resolved_canonical": "Approximation Theory",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.65,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Approximating invariant functions with the sorting trick is theoretically justified

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2403.01671.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2403.01671](https://arxiv.org/abs/2403.01671)

## 🔗 유사한 논문
- [[2025-09-18/Data coarse graining can improve model performance_20250918|Data coarse graining can improve model performance]] (83.1% similar)
- [[2025-09-23/A non-smooth regularization framework for learning over multitask graphs_20250923|A non-smooth regularization framework for learning over multitask graphs]] (81.6% similar)
- [[2025-09-17/Decentralized Optimization with Topology-Independent Communication_20250917|Decentralized Optimization with Topology-Independent Communication]] (80.4% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (79.9% similar)
- [[2025-09-23/A Generative Conditional Distribution Equality Testing Framework and Its Minimax Analysis_20250923|A Generative Conditional Distribution Equality Testing Framework and Its Minimax Analysis]] (79.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Approximation Theory|Approximation Theory]]
**🔗 Specific Connectable**: [[keywords/Reproducing Kernels|Reproducing Kernels]]
**⚡ Unique Technical**: [[keywords/Group Invariance|Group Invariance]], [[keywords/Canonicalization|Canonicalization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2403.01671v5 Announce Type: replace 
Abstract: Many machine learning models leverage group invariance which is enjoyed with a wide-range of applications. For exploiting an invariance structure, one common approach is known as \emph{frame averaging}. One popular example of frame averaging is the \emph{group averaging}, where the entire group is used to symmetrize a function. Another example is the \emph{canonicalization}, where a frame at each point consists of a single group element which transforms the point to its orbit representative, for example, sorting. Compared to group averaging, canonicalization is more efficient computationally. However, it results in non-differentiablity or discontinuity of the canonicalized function. As a result, the theoretical performance of canonicalization has not been given much attention. In this work, we establish an approximation theory for canonicalization. Specifically, we bound the point-wise and $L^2(\mathbb{P})$ approximation errors as well as the eigenvalue decay rates associated with a canonicalization trick applied to reproducing kernels. We discuss two key insights from our theoretical analyses and why they point to an interesting future research direction on how one can choose a design to fully leverage canonicalization in practice.

## 📝 요약

이 논문은 기계 학습 모델에서 그룹 불변성을 활용하는 방법 중 하나인 정준화(canonicalization)에 대한 이론적 성과를 제시합니다. 정준화는 계산 효율성이 높지만, 비분화 가능성이나 불연속성을 초래하여 이론적 성능 분석이 부족했습니다. 본 연구에서는 정준화 기법을 재생 커널에 적용했을 때의 점별 및 $L^2(\mathbb{P})$ 근사 오차와 고유값 감소율을 분석하여 정준화의 근사 이론을 확립했습니다. 이를 통해 정준화의 실용적 활용을 극대화할 수 있는 설계 선택에 대한 새로운 연구 방향을 제시합니다.

## 🎯 주요 포인트

- 1. 많은 머신러닝 모델은 다양한 응용 분야에서 그룹 불변성을 활용합니다.
- 2. 불변성 구조를 활용하기 위한 일반적인 접근 방식 중 하나는 '프레임 평균화'입니다.
- 3. '그룹 평균화'와 '정규화'는 프레임 평균화의 대표적인 예로, 정규화는 계산 효율성이 높지만 함수의 비분화 가능성이나 불연속성을 초래합니다.
- 4. 본 연구에서는 정규화에 대한 근사 이론을 수립하고, 재생 커널에 적용된 정규화 기법의 근사 오차와 고유값 감소율을 분석합니다.
- 5. 이론적 분석을 통해 정규화를 실질적으로 활용하기 위한 설계 선택에 대한 흥미로운 연구 방향을 제시합니다.


---

*Generated on 2025-09-24 02:32:10*