---
keywords:
  - Physics-Informed Neural Networks
  - Thermodynamically Informed Neural Networks
  - Large Deviations Principle
  - Neural Network
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19467
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:35:56.767215",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Physics-Informed Neural Networks",
    "Thermodynamically Informed Neural Networks",
    "Large Deviations Principle",
    "Neural Network"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Physics-Informed Neural Networks": 0.78,
    "Thermodynamically Informed Neural Networks": 0.8,
    "Large Deviations Principle": 0.77,
    "Neural Network": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Physics-Informed Neural Networks",
        "canonical": "Physics-Informed Neural Networks",
        "aliases": [
          "PINNs"
        ],
        "category": "unique_technical",
        "rationale": "PINNs are a specialized form of neural networks that integrate physical laws, providing a unique approach to solving PDEs.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Thermodynamically Informed Neural Networks",
        "canonical": "Thermodynamically Informed Neural Networks",
        "aliases": [
          "THINNs"
        ],
        "category": "unique_technical",
        "rationale": "THINNs represent a novel extension of PINNs, incorporating thermodynamic principles, which is a new concept in neural network research.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Deviations Principle",
        "canonical": "Large Deviations Principle",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This principle is crucial for understanding the probabilistic framework within which THINNs operate, linking probability theory with neural network design.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      },
      {
        "surface": "Neural Network",
        "canonical": "Neural Network",
        "aliases": [
          "NN"
        ],
        "category": "broad_technical",
        "rationale": "Neural networks are the foundational technology for PINNs and THINNs, providing a broad technical context.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "penalization",
      "residual of the equation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Physics-Informed Neural Networks",
      "resolved_canonical": "Physics-Informed Neural Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Thermodynamically Informed Neural Networks",
      "resolved_canonical": "Thermodynamically Informed Neural Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Deviations Principle",
      "resolved_canonical": "Large Deviations Principle",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Neural Network",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# THINNs: Thermodynamically Informed Neural Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19467.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19467](https://arxiv.org/abs/2509.19467)

## 🔗 유사한 논문
- [[2025-09-22/PBPK-iPINNs_ Inverse Physics-Informed Neural Networks for Physiologically Based Pharmacokinetic Brain Models_20250922|PBPK-iPINNs: Inverse Physics-Informed Neural Networks for Physiologically Based Pharmacokinetic Brain Models]] (85.7% similar)
- [[2025-09-22/Bayesian Physics Informed Neural Networks for Reliable Transformer Prognostics_20250922|Bayesian Physics Informed Neural Networks for Reliable Transformer Prognostics]] (85.0% similar)
- [[2025-09-19/Evidential Physics-Informed Neural Networks for Scientific Discovery_20250919|Evidential Physics-Informed Neural Networks for Scientific Discovery]] (84.6% similar)
- [[2025-09-23/PACMANN_ Point Adaptive Collocation Method for Artificial Neural Networks_20250923|PACMANN: Point Adaptive Collocation Method for Artificial Neural Networks]] (84.0% similar)
- [[2025-09-23/Physics-Informed Operator Learning for Hemodynamic Modeling_20250923|Physics-Informed Operator Learning for Hemodynamic Modeling]] (83.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Large Deviations Principle|Large Deviations Principle]]
**⚡ Unique Technical**: [[keywords/Physics-Informed Neural Networks|Physics-Informed Neural Networks]], [[keywords/Thermodynamically Informed Neural Networks|Thermodynamically Informed Neural Networks]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19467v1 Announce Type: new 
Abstract: Physics-Informed Neural Networks (PINNs) are a class of deep learning models aiming to approximate solutions of PDEs by training neural networks to minimize the residual of the equation. Focusing on non-equilibrium fluctuating systems, we propose a physically informed choice of penalization that is consistent with the underlying fluctuation structure, as characterized by a large deviations principle. This approach yields a novel formulation of PINNs in which the penalty term is chosen to penalize improbable deviations, rather than being selected heuristically. The resulting thermodynamically consistent extension of PINNs, termed THINNs, is subsequently analyzed by establishing analytical a posteriori estimates, and providing empirical comparisons to established penalization strategies.

## 📝 요약

이 논문은 비평형 변동 시스템에 대한 물리학 정보 신경망(PINNs)의 새로운 확장을 제안합니다. 저자들은 큰 편차 원리에 기반하여, 변동 구조와 일치하는 물리적으로 정보가 있는 페널티 선택 방식을 도입했습니다. 이로 인해 PINNs의 새로운 형태인 THINNs가 개발되었으며, 이는 불가능한 편차를 페널티로 삼아 기존의 경험적 선택 방식을 개선합니다. THINNs는 열역학적으로 일관된 확장을 제공하며, 분석적 사후 추정치를 통해 이론적으로 검증되고 기존의 페널티 전략과 비교하여 실증적으로 평가되었습니다.

## 🎯 주요 포인트

- 1. 물리 정보 신경망(PINNs)은 편미분 방정식(PDE)의 해를 근사하기 위해 신경망을 훈련하여 방정식의 잔차를 최소화하는 딥러닝 모델이다.
- 2. 비평형 변동 시스템에 초점을 맞추어, 우리는 큰 편차 원리에 의해 특성화된 변동 구조와 일치하는 물리적으로 정보화된 페널티 선택을 제안한다.
- 3. 제안된 방법은 불가능한 편차를 페널티화하는 새로운 PINNs 공식을 제공하며, 이는 경험적 선택이 아닌 물리적 일관성을 기반으로 한다.
- 4. THINNs라 불리는 열역학적으로 일관된 PINNs 확장은 분석적 사후 추정치를 통해 분석되고, 기존의 페널티 전략과의 경험적 비교가 제공된다.


---

*Generated on 2025-09-25 16:35:56*