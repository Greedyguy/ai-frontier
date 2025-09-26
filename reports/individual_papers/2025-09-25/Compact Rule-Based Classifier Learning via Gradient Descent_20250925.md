---
keywords:
  - Fuzzy Rule-based Reasoner
  - Rule-based Models
  - Fuzzy Logic
  - Gradient Descent
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2502.01375
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:18:59.668624",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Fuzzy Rule-based Reasoner",
    "Rule-based Models",
    "Fuzzy Logic",
    "Gradient Descent"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Fuzzy Rule-based Reasoner": 0.8,
    "Rule-based Models": 0.7,
    "Fuzzy Logic": 0.78,
    "Gradient Descent": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Fuzzy Rule-based Reasoner",
        "canonical": "Fuzzy Rule-based Reasoner",
        "aliases": [
          "FRR"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel system for rule-based learning, enhancing interpretability and efficiency.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.8
      },
      {
        "surface": "Rule-based models",
        "canonical": "Rule-based Models",
        "aliases": [
          "Rule-based systems"
        ],
        "category": "broad_technical",
        "rationale": "A fundamental concept in decision-making systems, linking to various optimization techniques.",
        "novelty_score": 0.45,
        "connectivity_score": 0.78,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Fuzzy logic partitions",
        "canonical": "Fuzzy Logic",
        "aliases": [
          "Fuzzy partitions"
        ],
        "category": "specific_connectable",
        "rationale": "Key to enhancing interpretability in rule-based systems, connecting to logic-based reasoning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.72,
        "link_intent_score": 0.78
      },
      {
        "surface": "Gradient-based rule learning",
        "canonical": "Gradient Descent",
        "aliases": [
          "Gradient-based learning"
        ],
        "category": "specific_connectable",
        "rationale": "Connects rule learning with optimization techniques, crucial for scalable model training.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "optimization",
      "performance",
      "evaluation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Fuzzy Rule-based Reasoner",
      "resolved_canonical": "Fuzzy Rule-based Reasoner",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Rule-based models",
      "resolved_canonical": "Rule-based Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.78,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Fuzzy logic partitions",
      "resolved_canonical": "Fuzzy Logic",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.72,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Gradient-based rule learning",
      "resolved_canonical": "Gradient Descent",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Compact Rule-Based Classifier Learning via Gradient Descent

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2502.01375.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2502.01375](https://arxiv.org/abs/2502.01375)

## 🔗 유사한 논문
- [[2025-09-23/Improving Deep Tabular Learning_20250923|Improving Deep Tabular Learning]] (81.4% similar)
- [[2025-09-24/Comparative Analysis of FOLD-SE vs. FOLD-R++ in Binary Classification and XGBoost in Multi-Category Classification_20250924|Comparative Analysis of FOLD-SE vs. FOLD-R++ in Binary Classification and XGBoost in Multi-Category Classification]] (81.3% similar)
- [[2025-09-23/Rectified Robust Policy Optimization for Model-Uncertain Constrained Reinforcement Learning without Strong Duality_20250923|Rectified Robust Policy Optimization for Model-Uncertain Constrained Reinforcement Learning without Strong Duality]] (81.0% similar)
- [[2025-09-22/ConCISE_ Confidence-guided Compression in Step-by-step Efficient Reasoning_20250922|ConCISE: Confidence-guided Compression in Step-by-step Efficient Reasoning]] (80.5% similar)
- [[2025-09-23/Enhancing Study-Level Inference from Clinical Trial Papers via Reinforcement Learning-Based Numeric Reasoning_20250923|Enhancing Study-Level Inference from Clinical Trial Papers via Reinforcement Learning-Based Numeric Reasoning]] (80.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Rule-based Models|Rule-based Models]]
**🔗 Specific Connectable**: [[keywords/Fuzzy Logic|Fuzzy Logic]], [[keywords/Gradient Descent|Gradient Descent]]
**⚡ Unique Technical**: [[keywords/Fuzzy Rule-based Reasoner|Fuzzy Rule-based Reasoner]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.01375v2 Announce Type: replace-cross 
Abstract: Rule-based models are essential for high-stakes decision-making due to their transparency and interpretability, but their discrete nature creates challenges for optimization and scalability. In this work, we present the Fuzzy Rule-based Reasoner (FRR), a novel gradient-based rule learning system that supports strict user constraints over rule-based complexity while achieving competitive performance. To maximize interpretability, the FRR uses semantically meaningful fuzzy logic partitions, unattainable with existing neuro-fuzzy approaches, and sufficient (single-rule) decision-making, which avoids the combinatorial complexity of additive rule ensembles. Through extensive evaluation across 40 datasets, FRR demonstrates: (1) superior performance to traditional rule-based methods (e.g., $5\%$ average accuracy over RIPPER); (2) comparable accuracy to tree-based models (e.g., CART) using rule bases $90\%$ more compact; and (3) achieves $96\%$ of the accuracy of state-of-the-art additive rule-based models while using only sufficient rules and requiring only $3\%$ of their rule base size.

## 📝 요약

이 논문에서는 투명성과 해석 가능성 때문에 중요한 의사결정에 필수적인 규칙 기반 모델의 최적화 및 확장성 문제를 해결하기 위해 Fuzzy Rule-based Reasoner (FRR)를 제안합니다. FRR은 의미 있는 퍼지 논리 분할을 사용하여 해석 가능성을 극대화하며, 단일 규칙으로 의사결정을 수행하여 복잡성을 줄입니다. 40개의 데이터셋을 통해 평가한 결과, FRR은 전통적인 규칙 기반 방법보다 평균 5% 높은 정확도를 보였고, 규칙 기반 크기를 90% 줄이면서도 트리 기반 모델과 유사한 정확도를 달성했습니다. 또한, 최첨단 가산 규칙 기반 모델의 96% 정확도를 단일 규칙만으로 달성하며, 규칙 기반 크기는 3%에 불과합니다.

## 🎯 주요 포인트

- 1. FRR는 규칙 기반 모델의 복잡성을 엄격하게 제어하면서도 경쟁력 있는 성능을 제공하는 새로운 경사 기반 규칙 학습 시스템입니다.
- 2. FRR는 기존의 신경-퍼지 접근법으로는 불가능한 의미론적으로 의미 있는 퍼지 논리 분할을 사용하여 해석 가능성을 극대화합니다.
- 3. FRR는 40개의 데이터셋에 대한 평가에서 전통적인 규칙 기반 방법보다 평균 5% 높은 정확도를 보여주었습니다.
- 4. FRR는 규칙 기반의 크기를 90% 줄이면서도 트리 기반 모델(CART)과 유사한 정확도를 달성했습니다.
- 5. FRR는 최첨단 가산 규칙 기반 모델의 정확도의 96%를 달성하면서도 필요한 규칙만 사용하고, 규칙 기반 크기의 3%만을 필요로 합니다.


---

*Generated on 2025-09-25 16:18:59*