---
keywords:
  - Neural Network
  - Conditional Value-at-Risk
  - Quadratic-Constraint Framework
  - Semidefinite Programming
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17413
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:55:52.392799",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Conditional Value-at-Risk",
    "Quadratic-Constraint Framework",
    "Semidefinite Programming"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.85,
    "Conditional Value-at-Risk": 0.78,
    "Quadratic-Constraint Framework": 0.7,
    "Semidefinite Programming": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural Network",
        "canonical": "Neural Network",
        "aliases": [
          "NN",
          "Neural Networks"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus on safety verification and robustness analysis.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Conditional Value-at-Risk",
        "canonical": "Conditional Value-at-Risk",
        "aliases": [
          "CVaR",
          "Worst-Case CVaR"
        ],
        "category": "unique_technical",
        "rationale": "Key concept for integrating risk assessment in neural network verification.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Quadratic-Constraint Framework",
        "canonical": "Quadratic-Constraint Framework",
        "aliases": [
          "QC Framework"
        ],
        "category": "unique_technical",
        "rationale": "Specific framework expanded upon in the paper for safety verification.",
        "novelty_score": 0.65,
        "connectivity_score": 0.65,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
      },
      {
        "surface": "Semidefinite Programming",
        "canonical": "Semidefinite Programming",
        "aliases": [
          "SDP"
        ],
        "category": "specific_connectable",
        "rationale": "Integral to the verification process described in the paper.",
        "novelty_score": 0.4,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "safety",
      "verification",
      "control systems"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural Network",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Conditional Value-at-Risk",
      "resolved_canonical": "Conditional Value-at-Risk",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Quadratic-Constraint Framework",
      "resolved_canonical": "Quadratic-Constraint Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.65,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Semidefinite Programming",
      "resolved_canonical": "Semidefinite Programming",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Distributionally Robust Safety Verification of Neural Networks via Worst-Case CVaR

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17413.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17413](https://arxiv.org/abs/2509.17413)

## 🔗 유사한 논문
- [[2025-09-18/Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning_20250918|Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning]] (81.9% similar)
- [[2025-09-19/Compositional Design of Safety Controllers for Large-scale Stochastic Hybrid Systems_20250919|Compositional Design of Safety Controllers for Large-scale Stochastic Hybrid Systems]] (81.0% similar)
- [[2025-09-19/Mini-Batch Robustness Verification of Deep Neural Networks_20250919|Mini-Batch Robustness Verification of Deep Neural Networks]] (80.8% similar)
- [[2025-09-17/A Conformal Prediction Framework for Uncertainty Quantification in Physics-Informed Neural Networks_20250917|A Conformal Prediction Framework for Uncertainty Quantification in Physics-Informed Neural Networks]] (80.1% similar)
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (79.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Semidefinite Programming|Semidefinite Programming]]
**⚡ Unique Technical**: [[keywords/Conditional Value-at-Risk|Conditional Value-at-Risk]], [[keywords/Quadratic-Constraint Framework|Quadratic-Constraint Framework]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17413v1 Announce Type: cross 
Abstract: Ensuring the safety of neural networks under input uncertainty is a fundamental challenge in safety-critical applications. This paper builds on and expands Fazlyab's quadratic-constraint (QC) and semidefinite-programming (SDP) framework for neural network verification to a distributionally robust and tail-risk-aware setting by integrating worst-case Conditional Value-at-Risk (WC-CVaR) over a moment-based ambiguity set with fixed mean and covariance. The resulting conditions remain SDP-checkable and explicitly account for tail risk. This integration broadens input-uncertainty geometry-covering ellipsoids, polytopes, and hyperplanes-and extends applicability to safety-critical domains where tail-event severity matters. Applications to closed-loop reachability of control systems and classification are demonstrated through numerical experiments, illustrating how the risk level $\varepsilon$ trades conservatism for tolerance to tail events-while preserving the computational structure of prior QC/SDP methods for neural network verification and robustness analysis.

## 📝 요약

이 논문은 입력 불확실성이 있는 상황에서 신경망의 안전성을 보장하기 위한 방법을 제안합니다. Fazlyab의 이차 제약(QC) 및 반정의 프로그래밍(SDP) 프레임워크를 확장하여, 평균과 공분산이 고정된 모멘트 기반 모호성 집합에서 최악의 조건부 가치 위험(WC-CVaR)을 통합합니다. 이로 인해 꼬리 위험을 명시적으로 고려하면서도 SDP로 검증 가능한 조건을 제공합니다. 이러한 접근은 입력 불확실성의 기하학적 범위를 넓히고, 꼬리 사건의 심각성이 중요한 안전 분야에 적용할 수 있도록 합니다. 제어 시스템의 폐루프 도달 가능성과 분류 문제에 대한 수치 실험을 통해, 위험 수준 $\varepsilon$이 보수성과 꼬리 사건에 대한 내성을 어떻게 조절하는지를 보여줍니다. 이는 기존 QC/SDP 방법의 계산 구조를 유지하면서 신경망 검증 및 강건성 분석에 기여합니다.

## 🎯 주요 포인트

- 1. 본 논문은 신경망 검증을 위해 Fazlyab의 이차 제약 및 반정의 프로그래밍 프레임워크를 분포적으로 강건하고 꼬리 위험을 고려하는 설정으로 확장합니다.
- 2. 최악의 조건부 가치 위험(WC-CVaR)을 고정된 평균 및 공분산을 가진 모멘트 기반의 모호성 집합에 통합하여 꼬리 위험을 명시적으로 고려합니다.
- 3. 이 통합은 입력 불확실성의 기하학적 범위를 넓히고, 안전이 중요한 분야에서 꼬리 사건의 심각성을 고려할 수 있도록 합니다.
- 4. 제안된 방법은 제어 시스템의 폐루프 도달 가능성과 분류에 대한 수치 실험을 통해 적용 가능성을 보여줍니다.
- 5. 위험 수준 $\varepsilon$는 보수성과 꼬리 사건에 대한 관용성을 교환하며, 기존 QC/SDP 방법의 계산 구조를 유지합니다.


---

*Generated on 2025-09-23 23:55:52*