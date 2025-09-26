---
keywords:
  - Natural Language Processing
  - Feature Attribution
  - Shortcut Learning
  - Annotation Quality
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2506.19680
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:46:56.117817",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Natural Language Processing",
    "Feature Attribution",
    "Shortcut Learning",
    "Annotation Quality"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Natural Language Processing": 0.8,
    "Feature Attribution": 0.77,
    "Shortcut Learning": 0.72,
    "Annotation Quality": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Natural Language Processing",
        "canonical": "Natural Language Processing",
        "aliases": [
          "NLP"
        ],
        "category": "broad_technical",
        "rationale": "This term is a key domain where the proposed method is applied, enhancing connectivity with related works.",
        "novelty_score": 0.3,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Feature Salience",
        "canonical": "Feature Attribution",
        "aliases": [
          "Feature Importance",
          "Salience Mapping"
        ],
        "category": "specific_connectable",
        "rationale": "Feature attribution is central to the paper's methodology, linking it to a broader context of model interpretability.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      },
      {
        "surface": "Shortcut Learning",
        "canonical": "Shortcut Learning",
        "aliases": [
          "Shortcut Features"
        ],
        "category": "unique_technical",
        "rationale": "This concept is uniquely addressed in the paper, providing insights into model training challenges.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "Annotation Quality",
        "canonical": "Annotation Quality",
        "aliases": [
          "Quality of Annotations"
        ],
        "category": "unique_technical",
        "rationale": "The paper highlights the importance of annotation quality, offering a unique perspective on data labeling.",
        "novelty_score": 0.68,
        "connectivity_score": 0.55,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "model",
      "method",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Natural Language Processing",
      "resolved_canonical": "Natural Language Processing",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Feature Salience",
      "resolved_canonical": "Feature Attribution",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Shortcut Learning",
      "resolved_canonical": "Shortcut Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Annotation Quality",
      "resolved_canonical": "Annotation Quality",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.55,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Model Guidance via Robust Feature Attribution

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2506.19680.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2506.19680](https://arxiv.org/abs/2506.19680)

## 🔗 유사한 논문
- [[2025-09-23/Sycophancy Mitigation Through Reinforcement Learning with Uncertainty-Aware Adaptive Reasoning Trajectories_20250923|Sycophancy Mitigation Through Reinforcement Learning with Uncertainty-Aware Adaptive Reasoning Trajectories]] (82.4% similar)
- [[2025-09-22/Navigate Beyond Shortcuts_ Debiased Learning through the Lens of Neural Collapse_20250922|Navigate Beyond Shortcuts: Debiased Learning through the Lens of Neural Collapse]] (82.2% similar)
- [[2025-09-22/reWordBench_ Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs_20250922|reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs]] (82.2% similar)
- [[2025-09-22/Mind the Gap_ Data Rewriting for Stable Off-Policy Supervised Fine-Tuning_20250922|Mind the Gap: Data Rewriting for Stable Off-Policy Supervised Fine-Tuning]] (82.0% similar)
- [[2025-09-22/Negotiated Representations to Prevent Overfitting in Machine Learning Applications_20250922|Negotiated Representations to Prevent Overfitting in Machine Learning Applications]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Natural Language Processing|Natural Language Processing]]
**🔗 Specific Connectable**: [[keywords/Feature Attribution|Feature Attribution]]
**⚡ Unique Technical**: [[keywords/Shortcut Learning|Shortcut Learning]], [[keywords/Annotation Quality|Annotation Quality]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.19680v2 Announce Type: replace 
Abstract: Controlling the patterns a model learns is essential to preventing reliance on irrelevant or misleading features. Such reliance on irrelevant features, often called shortcut features, has been observed across domains, including medical imaging and natural language processing, where it may lead to real-world harms. A common mitigation strategy leverages annotations (provided by humans or machines) indicating which features are relevant or irrelevant. These annotations are compared to model explanations, typically in the form of feature salience, and used to guide the loss function during training. Unfortunately, recent works have demonstrated that feature salience methods are unreliable and therefore offer a poor signal to optimize. In this work, we propose a simplified objective that simultaneously optimizes for explanation robustness and mitigation of shortcut learning. Unlike prior objectives with similar aims, we demonstrate theoretically why our approach ought to be more effective. Across a comprehensive series of experiments, we show that our approach consistently reduces test-time misclassifications by 20% compared to state-of-the-art methods. We also extend prior experimental settings to include natural language processing tasks. Additionally, we conduct novel ablations that yield practical insights, including the relative importance of annotation quality over quantity. Code for our method and experiments is available at: https://github.com/Mihneaghitu/ModelGuidanceViaRobustFeatureAttribution.

## 📝 요약

이 논문은 모델이 학습하는 패턴을 제어하여 잘못된 특징에 의존하는 것을 방지하는 방법을 제안합니다. 기존의 방법들은 특징 중요도를 활용하지만, 이는 신뢰성이 낮아 최적화에 부적합합니다. 본 연구는 설명의 견고성과 단축 학습의 완화를 동시에 최적화하는 단순화된 목표를 제안하며, 이론적으로 그 효과성을 입증합니다. 실험 결과, 제안된 방법은 최신 기법 대비 테스트 시 오분류를 20% 줄였습니다. 또한, 자연어 처리 작업을 포함한 실험을 확장하고, 주석의 질이 양보다 중요하다는 실용적 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. 모델이 학습하는 패턴을 제어하는 것은 관련 없는 특징에 의존하는 것을 방지하는 데 필수적입니다.
- 2. 기존의 특징 중요도 방법은 신뢰성이 낮아 최적화에 부적절한 신호를 제공합니다.
- 3. 제안된 방법은 설명의 견고성과 지름길 학습의 완화를 동시에 최적화하는 단순화된 목표를 제시합니다.
- 4. 제안된 방법은 최첨단 방법에 비해 테스트 시 오분류를 20% 줄이는 데 일관된 성과를 보였습니다.
- 5. 실험 결과, 주석의 양보다 질이 상대적으로 더 중요하다는 실용적인 통찰을 얻었습니다.


---

*Generated on 2025-09-24 02:46:56*