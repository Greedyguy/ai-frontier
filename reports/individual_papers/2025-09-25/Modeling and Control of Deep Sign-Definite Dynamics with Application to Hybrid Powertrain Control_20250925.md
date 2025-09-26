---
keywords:
  - Deep Learning
  - Hybrid Powertrain
  - Model Predictive Control
  - Sign Constraints
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19869
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:58:50.584451",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Hybrid Powertrain",
    "Model Predictive Control",
    "Sign Constraints"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Hybrid Powertrain": 0.8,
    "Model Predictive Control": 0.78,
    "Sign Constraints": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [
          "DL"
        ],
        "category": "broad_technical",
        "rationale": "Deep Learning is central to the paper's methodology and connects to a wide range of related topics.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Hybrid Powertrain",
        "canonical": "Hybrid Powertrain",
        "aliases": [
          "Hybrid Engine",
          "Hybrid Vehicle Powertrain"
        ],
        "category": "unique_technical",
        "rationale": "The application focus of the paper, providing a unique context for linking with automotive control systems.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Model Predictive Control",
        "canonical": "Model Predictive Control",
        "aliases": [
          "MPC"
        ],
        "category": "specific_connectable",
        "rationale": "A key control strategy discussed, linking to control theory and optimization methods.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Sign Constraints",
        "canonical": "Sign Constraints",
        "aliases": [
          "Sign Restrictions"
        ],
        "category": "unique_technical",
        "rationale": "A novel methodological contribution of the paper that enhances model reliability and control.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Hybrid Powertrain",
      "resolved_canonical": "Hybrid Powertrain",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Model Predictive Control",
      "resolved_canonical": "Model Predictive Control",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Sign Constraints",
      "resolved_canonical": "Sign Constraints",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Modeling and Control of Deep Sign-Definite Dynamics with Application to Hybrid Powertrain Control

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19869.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19869](https://arxiv.org/abs/2509.19869)

## 🔗 유사한 논문
- [[2025-09-19/AdapJ_ An Adaptive Extended Jacobian Controller for Soft Manipulators_20250919|AdapJ: An Adaptive Extended Jacobian Controller for Soft Manipulators]] (82.5% similar)
- [[2025-09-23/Deep Learning as the Disciplined Construction of Tame Objects_20250923|Deep Learning as the Disciplined Construction of Tame Objects]] (82.3% similar)
- [[2025-09-23/Safe Guaranteed Dynamics Exploration with Probabilistic Models_20250923|Safe Guaranteed Dynamics Exploration with Probabilistic Models]] (81.9% similar)
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (81.4% similar)
- [[2025-09-24/Probabilistic Machine Learning for Uncertainty-Aware Diagnosis of Industrial Systems_20250924|Probabilistic Machine Learning for Uncertainty-Aware Diagnosis of Industrial Systems]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Model Predictive Control|Model Predictive Control]]
**⚡ Unique Technical**: [[keywords/Hybrid Powertrain|Hybrid Powertrain]], [[keywords/Sign Constraints|Sign Constraints]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19869v1 Announce Type: cross 
Abstract: Deep learning is increasingly used for complex, large-scale systems where first-principles modeling is difficult. However, standard deep learning models often fail to enforce physical structure or preserve convexity in downstream control, leading to physically inconsistent predictions and discontinuous inputs owing to nonconvexity. We introduce sign constraints--sign restrictions on Jacobian entries--that unify monotonicity, positivity, and sign-definiteness; additionally, we develop model-construction methods that enforce them, together with a control-synthesis procedure. In particular, we design exactly linearizable deep models satisfying these constraints and formulate model predictive control as a convex quadratic program, which yields a unique optimizer and a Lipschitz continuous control law. On a two-tank system and a hybrid powertrain, the proposed approach improves prediction accuracy and produces smoother control inputs than existing methods.

## 📝 요약

이 논문은 복잡하고 대규모 시스템에서 물리적 구조를 유지하고 볼록성을 보장하기 어려운 기존 딥러닝 모델의 한계를 극복하기 위해 새로운 접근법을 제안합니다. 저자들은 Jacobian 항목에 대한 부호 제약을 도입하여 단조성, 양수성, 부호 확정성을 통합하고, 이를 강제하는 모델 구축 방법과 제어 합성 절차를 개발했습니다. 특히, 이러한 제약을 만족하는 정확히 선형화 가능한 딥 모델을 설계하고, 모델 예측 제어를 볼록 이차 계획 문제로 공식화하여 고유한 최적화 해와 리프시츠 연속 제어 법칙을 제공합니다. 제안된 방법은 이중 탱크 시스템과 하이브리드 파워트레인에서 기존 방법보다 예측 정확성을 높이고 제어 입력을 부드럽게 만듭니다.

## 🎯 주요 포인트

- 1. 딥러닝은 복잡하고 대규모 시스템에서 점점 더 많이 사용되고 있지만, 물리적 구조를 강제하거나 볼록성을 유지하는 데 실패할 수 있습니다.
- 2. 우리는 Jacobian 항목에 대한 부호 제약을 도입하여 단조성, 양성, 부호 확정성을 통합하고 이를 강제하는 모델 구축 방법을 개발했습니다.
- 3. 제안된 접근 방식은 두 개의 탱크 시스템과 하이브리드 파워트레인에서 기존 방법보다 예측 정확성을 개선하고 더 부드러운 제어 입력을 생성합니다.
- 4. 우리는 이러한 제약을 만족하는 정확히 선형화 가능한 딥 모델을 설계하고, 모델 예측 제어를 볼록 이차 프로그램으로 공식화했습니다.
- 5. 이 방법은 고유한 최적화 해와 리프시츠 연속 제어 법칙을 제공합니다.


---

*Generated on 2025-09-25 16:58:50*