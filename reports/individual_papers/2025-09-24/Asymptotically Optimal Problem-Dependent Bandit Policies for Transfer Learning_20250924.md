<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:00:02.273439",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-Armed Bandit",
    "Transfer Learning",
    "KL-UCB-Transfer",
    "Cumulative Regret"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multi-Armed Bandit": 0.78,
    "Transfer Learning": 0.85,
    "KL-UCB-Transfer": 0.8,
    "Cumulative Regret": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "multi-armed bandit problem",
        "canonical": "Multi-Armed Bandit",
        "aliases": [
          "MAB"
        ],
        "category": "specific_connectable",
        "rationale": "The multi-armed bandit problem is a fundamental concept in reinforcement learning and decision theory, providing strong connectivity to related works.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "transfer learning",
        "canonical": "Transfer Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Transfer learning is a widely applicable technique in machine learning, linking to numerous studies and applications.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "KL-UCB-Transfer",
        "canonical": "KL-UCB-Transfer",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "KL-UCB-Transfer is a novel policy introduced in this paper, offering a unique point of reference for future research.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "cumulative regret",
        "canonical": "Cumulative Regret",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Cumulative regret is a key metric in evaluating bandit algorithms, facilitating connections to performance analysis studies.",
        "novelty_score": 0.4,
        "connectivity_score": 0.83,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "non-contextual",
      "samples",
      "simulations"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "multi-armed bandit problem",
      "resolved_canonical": "Multi-Armed Bandit",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "transfer learning",
      "resolved_canonical": "Transfer Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "KL-UCB-Transfer",
      "resolved_canonical": "KL-UCB-Transfer",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "cumulative regret",
      "resolved_canonical": "Cumulative Regret",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.83,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Asymptotically Optimal Problem-Dependent Bandit Policies for Transfer Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19098.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.19098](https://arxiv.org/abs/2509.19098)

## 🔗 유사한 논문
- [[2025-09-19/Constrained Feedback Learning for Non-Stationary Multi-Armed Bandits_20250919|Constrained Feedback Learning for Non-Stationary Multi-Armed Bandits]] (84.6% similar)
- [[2025-09-24/Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training_20250924|Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training]] (81.5% similar)
- [[2025-09-19/Optimal Algorithms for Bandit Learning in Matching Markets_20250919|Optimal Algorithms for Bandit Learning in Matching Markets]] (81.3% similar)
- [[2025-09-23/Statistical Inference for Misspecified Contextual Bandits_20250923|Statistical Inference for Misspecified Contextual Bandits]] (80.7% similar)
- [[2025-09-23/Bayesian Algorithms for Adversarial Online Learning_ from Finite to Infinite Action Spaces_20250923|Bayesian Algorithms for Adversarial Online Learning: from Finite to Infinite Action Spaces]] (80.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transfer Learning|Transfer Learning]]
**🔗 Specific Connectable**: [[keywords/Multi-Armed Bandit|Multi-Armed Bandit]], [[keywords/Cumulative Regret|Cumulative Regret]]
**⚡ Unique Technical**: [[keywords/KL-UCB-Transfer|KL-UCB-Transfer]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19098v1 Announce Type: new 
Abstract: We study the non-contextual multi-armed bandit problem in a transfer learning setting: before any pulls, the learner is given N'_k i.i.d. samples from each source distribution nu'_k, and the true target distributions nu_k lie within a known distance bound d_k(nu_k, nu'_k) <= L_k. In this framework, we first derive a problem-dependent asymptotic lower bound on cumulative regret that extends the classical Lai-Robbins result to incorporate the transfer parameters (d_k, L_k, N'_k). We then propose KL-UCB-Transfer, a simple index policy that matches this new bound in the Gaussian case. Finally, we validate our approach via simulations, showing that KL-UCB-Transfer significantly outperforms the no-prior baseline when source and target distributions are sufficiently close.

## 📝 요약

이 논문은 전이 학습 환경에서 비맥락적 다중 슬롯머신 문제를 연구합니다. 학습자는 각 소스 분포로부터 N'_k개의 독립적 샘플을 제공받으며, 실제 목표 분포는 알려진 거리 범위 내에 있습니다. 연구에서는 전이 매개변수를 포함하여 누적 후회의 문제 의존적 점근적 하한을 도출하고, 이를 기반으로 한 새로운 지수 정책인 KL-UCB-Transfer를 제안합니다. 이 정책은 가우시안 경우에서 새로운 하한과 일치하며, 시뮬레이션을 통해 소스와 목표 분포가 충분히 가까울 때 기존 방법보다 성능이 뛰어남을 검증합니다.

## 🎯 주요 포인트

- 1. 비맥락적 다중 슬롯머신 문제를 전이 학습 설정에서 연구합니다.
- 2. 누적 후회에 대한 문제 의존적 점근적 하한을 도출하여 전이 매개변수를 포함한 Lai-Robbins 결과를 확장합니다.
- 3. Gaussian 경우에서 새로운 하한에 부합하는 간단한 지수 정책인 KL-UCB-Transfer를 제안합니다.
- 4. 시뮬레이션을 통해 KL-UCB-Transfer가 소스와 대상 분포가 충분히 가까울 때 사전 지식이 없는 기준보다 성능이 우수함을 검증합니다.


---

*Generated on 2025-09-24 15:00:02*