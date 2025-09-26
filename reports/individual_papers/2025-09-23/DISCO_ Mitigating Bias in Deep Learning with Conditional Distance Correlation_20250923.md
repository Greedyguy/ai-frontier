---
keywords:
  - Deep Learning
  - Conditional Distance Correlation
  - Causal Stability
  - Bias Mitigation
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2506.11653
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:07:16.501031",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Conditional Distance Correlation",
    "Causal Stability",
    "Bias Mitigation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Conditional Distance Correlation": 0.8,
    "Causal Stability": 0.78,
    "Bias Mitigation": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Deep Learning is a core concept in the paper, linking it to broader technical discussions.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "Conditional Distance Correlation",
        "canonical": "Conditional Distance Correlation",
        "aliases": [
          "DISCO"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique technical concept introduced in the paper, crucial for understanding the proposed method.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Causal Stability",
        "canonical": "Causal Stability",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Causal Stability is a specific concept that connects causal theory with practical applications in the paper.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Bias Mitigation",
        "canonical": "Bias Mitigation",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Bias Mitigation is a key theme of the paper, linking it to ongoing discussions about fairness in AI.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
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
        "specificity": 0.5,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Conditional Distance Correlation",
      "resolved_canonical": "Conditional Distance Correlation",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Causal Stability",
      "resolved_canonical": "Causal Stability",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Bias Mitigation",
      "resolved_canonical": "Bias Mitigation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# DISCO: Mitigating Bias in Deep Learning with Conditional Distance Correlation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.11653.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2506.11653](https://arxiv.org/abs/2506.11653)

## 🔗 유사한 논문
- [[2025-09-19/CausalPre_ Scalable and Effective Data Pre-processing for Causal Fairness_20250919|CausalPre: Scalable and Effective Data Pre-processing for Causal Fairness]] (82.8% similar)
- [[2025-09-23/Does Reasoning Introduce Bias? A Study of Social Bias Evaluation and Mitigation in LLM Reasoning_20250923|Does Reasoning Introduce Bias? A Study of Social Bias Evaluation and Mitigation in LLM Reasoning]] (81.9% similar)
- [[2025-09-17/Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (81.6% similar)
- [[2025-09-23/Causal Fuzzing for Verifying Machine Unlearning_20250923|Causal Fuzzing for Verifying Machine Unlearning]] (81.4% similar)
- [[2025-09-22/Navigate Beyond Shortcuts_ Debiased Learning through the Lens of Neural Collapse_20250922|Navigate Beyond Shortcuts: Debiased Learning through the Lens of Neural Collapse]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Causal Stability|Causal Stability]], [[keywords/Bias Mitigation|Bias Mitigation]]
**⚡ Unique Technical**: [[keywords/Conditional Distance Correlation|Conditional Distance Correlation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.11653v2 Announce Type: replace-cross 
Abstract: Dataset bias often leads deep learning models to exploit spurious correlations instead of task-relevant signals. We introduce the Standard Anti-Causal Model (SAM), a unifying causal framework that characterizes bias mechanisms and yields a conditional independence criterion for causal stability. Building on this theory, we propose DISCO$_m$ and sDISCO, efficient and scalable estimators of conditional distance correlation that enable independence regularization in black-box models. Across five diverse datasets, our methods consistently outperform or are competitive in existing bias mitigation approaches, while requiring fewer hyperparameters and scaling seamlessly to multi-bias scenarios. This work bridges causal theory and practical deep learning, providing both a principled foundation and effective tools for robust prediction. Source Code: https://github.com/***.

## 📝 요약

이 논문에서는 데이터셋 편향이 심층 학습 모델이 과제와 관련 없는 상관관계를 이용하게 만드는 문제를 다룹니다. 이를 해결하기 위해, 편향 메커니즘을 설명하고 인과적 안정성을 위한 조건부 독립 기준을 제공하는 표준 반인과 모델(SAM)을 제안합니다. 이 이론을 바탕으로, 조건부 거리 상관을 추정하는 효율적이고 확장 가능한 방법인 DISCO$_m$와 sDISCO를 개발하여 블랙박스 모델에서 독립성 규제를 가능하게 합니다. 다섯 개의 다양한 데이터셋에서, 제안된 방법은 기존의 편향 완화 접근법보다 우수하거나 경쟁력 있는 성능을 보이며, 적은 하이퍼파라미터로 다중 편향 시나리오에 원활하게 확장됩니다. 이 연구는 인과 이론과 실용적인 심층 학습을 연결하여 견고한 예측을 위한 원칙적 기반과 효과적인 도구를 제공합니다.

## 🎯 주요 포인트

- 1. 데이터셋 편향은 딥러닝 모델이 과제 관련 신호 대신 잘못된 상관관계를 활용하게 만듭니다.
- 2. 우리는 편향 메커니즘을 특징짓고 인과적 안정성을 위한 조건부 독립 기준을 제공하는 표준 반인과 모델(SAM)을 소개합니다.
- 3. DISCO$_m$ 및 sDISCO는 조건부 거리 상관을 효율적이고 확장 가능하게 추정하여 블랙박스 모델에서 독립성 정규화를 가능하게 합니다.
- 4. 제안된 방법은 다섯 가지 다양한 데이터셋에서 기존 편향 완화 접근법보다 일관되게 우수하거나 경쟁력을 가지며, 하이퍼파라미터가 적고 다중 편향 시나리오에 원활하게 확장됩니다.
- 5. 이 연구는 인과 이론과 실용적인 딥러닝을 연결하여 강력한 예측을 위한 원칙적 기초와 효과적인 도구를 제공합니다.


---

*Generated on 2025-09-24 01:07:16*