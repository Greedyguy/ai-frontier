---
keywords:
  - Sparse Models
  - Phase Transition in Feature Selection
  - Neural Network
  - Sparsity-Promoting Penalties
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2411.17180
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:57:40.613996",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Sparse Models",
    "Phase Transition in Feature Selection",
    "Neural Network",
    "Sparsity-Promoting Penalties"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Sparse Models": 0.79,
    "Phase Transition in Feature Selection": 0.72,
    "Neural Network": 0.77,
    "Sparsity-Promoting Penalties": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Sparse Models",
        "canonical": "Sparse Models",
        "aliases": [
          "Sparse Learning",
          "Sparse Representation"
        ],
        "category": "specific_connectable",
        "rationale": "Sparse models are crucial for reducing complexity and enhancing interpretability in AI, making them a strong link to feature selection and efficiency.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.79
      },
      {
        "surface": "Phase Transition",
        "canonical": "Phase Transition in Feature Selection",
        "aliases": [
          "Feature Selection Phase Transition"
        ],
        "category": "unique_technical",
        "rationale": "The concept of phase transition in feature selection is a novel approach that enhances understanding of sparsity in models.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      },
      {
        "surface": "Artificial Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "ANN",
          "Deep Neural Networks"
        ],
        "category": "broad_technical",
        "rationale": "Neural networks are foundational to the study and application of sparse learning and feature selection.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.77
      },
      {
        "surface": "Sparsity-Promoting Penalties",
        "canonical": "Sparsity-Promoting Penalties",
        "aliases": [
          "Sparsity Penalties",
          "Regularization Techniques"
        ],
        "category": "specific_connectable",
        "rationale": "These penalties are essential for implementing sparsity in models, directly linking to the paper's focus on feature selection.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "Validation-Free",
      "Real-World Data"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Sparse Models",
      "resolved_canonical": "Sparse Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Phase Transition",
      "resolved_canonical": "Phase Transition in Feature Selection",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Artificial Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Sparsity-Promoting Penalties",
      "resolved_canonical": "Sparsity-Promoting Penalties",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Validation-Free Sparse Learning: A Phase Transition Approach to Feature Selection

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2411.17180.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2411.17180](https://arxiv.org/abs/2411.17180)

## 🔗 유사한 논문
- [[2025-09-18/Balancing Sparse RNNs with Hyperparameterization Benefiting Meta-Learning_20250918|Balancing Sparse RNNs with Hyperparameterization Benefiting Meta-Learning]] (82.0% similar)
- [[2025-09-22/Automated Constitutive Model Discovery by Pairing Sparse Regression Algorithms with Model Selection Criteria_20250922|Automated Constitutive Model Discovery by Pairing Sparse Regression Algorithms with Model Selection Criteria]] (81.9% similar)
- [[2025-09-23/Model Guidance via Robust Feature Attribution_20250923|Model Guidance via Robust Feature Attribution]] (80.0% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (79.3% similar)
- [[2025-09-22/Nonconvex Regularization for Feature Selection in Reinforcement Learning_20250922|Nonconvex Regularization for Feature Selection in Reinforcement Learning]] (79.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Sparse Models|Sparse Models]], [[keywords/Sparsity-Promoting Penalties|Sparsity-Promoting Penalties]]
**⚡ Unique Technical**: [[keywords/Phase Transition in Feature Selection|Phase Transition in Feature Selection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2411.17180v4 Announce Type: replace-cross 
Abstract: The growing environmental footprint of artificial intelligence (AI), especially in terms of storage and computation, calls for more frugal and interpretable models. Sparse models (e.g., linear, neural networks) offer a promising solution by selecting only the most relevant features, reducing complexity, preventing over-fitting and enabling interpretation-marking a step towards truly intelligent AI.
  The concept of a right amount of sparsity (without too many false positive or too few true positive) is subjective. So we propose a new paradigm previously only observed and mathematically studied for compressed sensing (noiseless linear models): obtaining a phase transition in the probability of retrieving the relevant features. We show in practice how to obtain this phase transition for a class of sparse learners. Our approach is flexible and applicable to complex models ranging from linear to shallow and deep artificial neural networks while supporting various loss functions and sparsity-promoting penalties. It does not rely on cross-validation or on a validation set to select its single regularization parameter. For real-world data, it provides a good balance between predictive accuracy and feature sparsity.
  A Python package is available at https://github.com/VcMaxouuu/HarderLASSO containing all the simulations and ready-to-use models.

## 📝 요약

이 논문은 인공지능(AI)의 환경적 영향을 줄이기 위해 희소 모델을 활용하는 방법을 제안합니다. 희소 모델은 관련 있는 특징만 선택하여 복잡성을 줄이고 과적합을 방지하며 해석 가능성을 높입니다. 저자들은 압축 센싱에서 관찰된 개념을 차용하여, 관련 특징을 효과적으로 추출할 수 있는 확률적 전이 현상을 설명합니다. 이 방법은 선형 모델부터 심층 신경망까지 다양한 복잡한 모델에 적용 가능하며, 교차 검증 없이도 적절한 정규화 매개변수를 선택할 수 있습니다. 실제 데이터에 적용 시 예측 정확도와 특징 희소성 간의 균형을 잘 유지합니다. 관련 Python 패키지도 제공됩니다.

## 🎯 주요 포인트

- 1. 인공지능의 환경적 영향을 줄이기 위해 해석 가능한 희소 모델이 필요합니다.
- 2. 희소 모델은 복잡성을 줄이고 과적합을 방지하며 해석 가능성을 높입니다.
- 3. 적절한 희소성의 개념은 주관적이며, 우리는 관련 특징을 추출하는 확률의 상전이를 제안합니다.
- 4. 제안된 접근법은 다양한 복잡한 모델에 적용 가능하며, 교차 검증에 의존하지 않습니다.
- 5. Python 패키지를 통해 제안된 모델과 시뮬레이션을 사용할 수 있습니다.


---

*Generated on 2025-09-24 02:57:40*