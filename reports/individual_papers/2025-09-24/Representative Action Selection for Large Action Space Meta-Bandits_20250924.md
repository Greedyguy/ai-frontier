<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:25:03.466711",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Gaussian Process",
    "Epsilon-Net Algorithm",
    "Thompson Sampling",
    "Upper Confidence Bound"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Gaussian Process": 0.78,
    "Epsilon-Net Algorithm": 0.81,
    "Thompson Sampling": 0.85,
    "Upper Confidence Bound": 0.83
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Gaussian process",
        "canonical": "Gaussian Process",
        "aliases": [
          "GP"
        ],
        "category": "broad_technical",
        "rationale": "Gaussian processes are a fundamental concept in modeling related payoffs in machine learning, providing strong connectivity to probabilistic models.",
        "novelty_score": 0.45,
        "connectivity_score": 0.87,
        "specificity_score": 0.68,
        "link_intent_score": 0.78
      },
      {
        "surface": "epsilon-net algorithm",
        "canonical": "Epsilon-Net Algorithm",
        "aliases": [
          "ε-net algorithm"
        ],
        "category": "unique_technical",
        "rationale": "The epsilon-net algorithm is a unique approach proposed in the paper for action selection, offering a novel perspective on subset selection in large action spaces.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.81
      },
      {
        "surface": "Thompson Sampling",
        "canonical": "Thompson Sampling",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Thompson Sampling is a well-known method in bandit problems, providing strong connectivity to exploration-exploitation strategies.",
        "novelty_score": 0.3,
        "connectivity_score": 0.89,
        "specificity_score": 0.75,
        "link_intent_score": 0.85
      },
      {
        "surface": "Upper Confidence Bound",
        "canonical": "Upper Confidence Bound",
        "aliases": [
          "UCB"
        ],
        "category": "specific_connectable",
        "rationale": "Upper Confidence Bound is a key strategy in bandit algorithms, enhancing linkage to decision-making under uncertainty.",
        "novelty_score": 0.35,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.83
      }
    ],
    "ban_list_suggestions": [
      "action space",
      "performance",
      "subset selection"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Gaussian process",
      "resolved_canonical": "Gaussian Process",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.87,
        "specificity": 0.68,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "epsilon-net algorithm",
      "resolved_canonical": "Epsilon-Net Algorithm",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Thompson Sampling",
      "resolved_canonical": "Thompson Sampling",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.89,
        "specificity": 0.75,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Upper Confidence Bound",
      "resolved_canonical": "Upper Confidence Bound",
      "decision": "linked",
      "scores": {
        "novelty": 0.35,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.83
      }
    }
  ]
}
-->

# Representative Action Selection for Large Action Space Meta-Bandits

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2505.18269.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2505.18269](https://arxiv.org/abs/2505.18269)

## 🔗 유사한 논문
- [[2025-09-19/Optimal Algorithms for Bandit Learning in Matching Markets_20250919|Optimal Algorithms for Bandit Learning in Matching Markets]] (80.9% similar)
- [[2025-09-19/Constrained Feedback Learning for Non-Stationary Multi-Armed Bandits_20250919|Constrained Feedback Learning for Non-Stationary Multi-Armed Bandits]] (79.8% similar)
- [[2025-09-24/Consistency of Selection Strategies for Fraud Detection_20250924|Consistency of Selection Strategies for Fraud Detection]] (79.5% similar)
- [[2025-09-23/Core-elements Subsampling for Alternating Least Squares_20250923|Core-elements Subsampling for Alternating Least Squares]] (79.4% similar)
- [[2025-09-24/Asymptotically Optimal Problem-Dependent Bandit Policies for Transfer Learning_20250924|Asymptotically Optimal Problem-Dependent Bandit Policies for Transfer Learning]] (79.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Gaussian Process|Gaussian Process]]
**🔗 Specific Connectable**: [[keywords/Thompson Sampling|Thompson Sampling]], [[keywords/Upper Confidence Bound|Upper Confidence Bound]]
**⚡ Unique Technical**: [[keywords/Epsilon-Net Algorithm|Epsilon-Net Algorithm]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.18269v3 Announce Type: replace 
Abstract: We study the problem of selecting a subset from a large action space shared by a family of bandits, with the goal of achieving performance nearly matching that of using the full action space. We assume that similar actions tend to have related payoffs, modeled by a Gaussian process. To exploit this structure, we propose a simple epsilon-net algorithm to select a representative subset. We provide theoretical guarantees for its performance and compare it empirically to Thompson Sampling and Upper Confidence Bound.

## 📝 요약

이 논문은 대규모 행동 공간에서 하위 집합을 선택하여 전체 행동 공간을 사용하는 것과 유사한 성능을 달성하는 문제를 다룹니다. 유사한 행동이 관련된 보상을 갖는다는 가정 하에, 이를 가우시안 프로세스로 모델링합니다. 이러한 구조를 활용하기 위해, 대표적인 하위 집합을 선택하는 간단한 엡실론-넷 알고리즘을 제안합니다. 제안된 알고리즘의 성능에 대한 이론적 보장을 제공하며, 이를 Thompson Sampling 및 Upper Confidence Bound와 비교하여 실증적으로 평가합니다.

## 🎯 주요 포인트

- 1. 대규모 행동 공간에서 성능을 유지하면서 부분 집합을 선택하는 문제를 연구합니다.
- 2. 유사한 행동이 관련된 보상을 가진다고 가정하고 이를 가우시안 프로세스로 모델링합니다.
- 3. 대표적인 부분 집합을 선택하기 위해 간단한 epsilon-net 알고리즘을 제안합니다.
- 4. 제안된 알고리즘의 성능에 대한 이론적 보장을 제공합니다.
- 5. Thompson Sampling 및 Upper Confidence Bound와의 실증적 비교를 수행합니다.


---

*Generated on 2025-09-24 15:25:03*