---
keywords:
  - Mutual Distillation
  - Reinforcement Learning
  - Invariant Representations
  - Generalization
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2501.02481
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:18:30.995691",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Mutual Distillation",
    "Reinforcement Learning",
    "Invariant Representations",
    "Generalization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Mutual Distillation": 0.72,
    "Reinforcement Learning": 0.85,
    "Invariant Representations": 0.8,
    "Generalization": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "mutual distillation",
        "canonical": "Mutual Distillation",
        "aliases": [
          "policy distillation",
          "distillation between policies"
        ],
        "category": "unique_technical",
        "rationale": "Mutual distillation is a novel concept in reinforcement learning that enhances policy robustness, making it a unique technical term with potential for new connections.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      },
      {
        "surface": "reinforcement learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement learning is a foundational concept in machine learning, providing strong connectivity across various research topics.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "invariant representations",
        "canonical": "Invariant Representations",
        "aliases": [
          "stable representations",
          "consistent representations"
        ],
        "category": "specific_connectable",
        "rationale": "Invariant representations are crucial for generalization in machine learning, linking to concepts like robustness and feature extraction.",
        "novelty_score": 0.68,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "generalization performance",
        "canonical": "Generalization",
        "aliases": [
          "generalization ability",
          "generalization capacity"
        ],
        "category": "specific_connectable",
        "rationale": "Generalization is a key goal in machine learning, connecting to diverse areas such as model evaluation and transfer learning.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "regularization",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "mutual distillation",
      "resolved_canonical": "Mutual Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "reinforcement learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "invariant representations",
      "resolved_canonical": "Invariant Representations",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "generalization performance",
      "resolved_canonical": "Generalization",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Representation Convergence: Mutual Distillation is Secretly a Form of Regularization

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2501.02481.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2501.02481](https://arxiv.org/abs/2501.02481)

## 🔗 유사한 논문
- [[2025-09-23/Rectified Robust Policy Optimization for Model-Uncertain Constrained Reinforcement Learning without Strong Duality_20250923|Rectified Robust Policy Optimization for Model-Uncertain Constrained Reinforcement Learning without Strong Duality]] (83.1% similar)
- [[2025-09-23/Model Guidance via Robust Feature Attribution_20250923|Model Guidance via Robust Feature Attribution]] (82.5% similar)
- [[2025-09-18/Data coarse graining can improve model performance_20250918|Data coarse graining can improve model performance]] (81.8% similar)
- [[2025-09-24/Stability and Generalization of Adversarial Diffusion Training_20250924|Stability and Generalization of Adversarial Diffusion Training]] (81.7% similar)
- [[2025-09-22/Nonconvex Regularization for Feature Selection in Reinforcement Learning_20250922|Nonconvex Regularization for Feature Selection in Reinforcement Learning]] (81.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Invariant Representations|Invariant Representations]], [[keywords/Generalization|Generalization]]
**⚡ Unique Technical**: [[keywords/Mutual Distillation|Mutual Distillation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.02481v5 Announce Type: replace-cross 
Abstract: In this paper, we argue that mutual distillation between reinforcement learning policies serves as an implicit regularization, preventing them from overfitting to irrelevant features. We highlight two separate contributions: (i) Theoretically, for the first time, we prove that enhancing the policy robustness to irrelevant features leads to improved generalization performance. (ii) Empirically, we demonstrate that mutual distillation between policies contributes to such robustness, enabling the spontaneous emergence of invariant representations over pixel inputs. Ultimately, we do not claim to achieve state-of-the-art performance but rather focus on uncovering the underlying principles of generalization and deepening our understanding of its mechanisms.

## 📝 요약

이 논문에서는 강화 학습 정책 간의 상호 증류가 암묵적인 정규화 역할을 하여 불필요한 특징에 대한 과적합을 방지한다고 주장합니다. 주요 기여는 두 가지입니다. 첫째, 이론적으로 정책의 불필요한 특징에 대한 강건성을 강화하면 일반화 성능이 향상된다는 것을 처음으로 증명했습니다. 둘째, 실험적으로 정책 간 상호 증류가 이러한 강건성에 기여하여 픽셀 입력에 대한 불변 표현의 자발적 형성을 가능하게 함을 보여주었습니다. 이 연구는 최첨단 성능을 주장하기보다는 일반화의 기본 원리를 밝히고 그 메커니즘에 대한 이해를 심화하는 데 중점을 둡니다.

## 🎯 주요 포인트

- 1. 강화 학습 정책 간 상호 증류는 암묵적 정규화로 작용하여 관련 없는 특징에 대한 과적합을 방지한다.
- 2. 정책의 관련 없는 특징에 대한 강건성을 향상시키면 일반화 성능이 개선된다는 것을 이론적으로 처음으로 증명하였다.
- 3. 정책 간 상호 증류가 픽셀 입력에 대한 불변 표현의 자발적 출현을 가능하게 하여 강건성에 기여함을 실증적으로 보여주었다.
- 4. 본 연구는 최첨단 성능 달성을 목표로 하기보다는 일반화의 기본 원리를 밝히고 그 메커니즘에 대한 이해를 심화하는 데 중점을 둔다.


---

*Generated on 2025-09-25 16:18:30*