---
keywords:
  - Machine Learning
  - Graph Neural Network
  - Distribution Classification
  - Approximate Bayesian Computation
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2505.11228
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:38:57.267320",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Learning",
    "Graph Neural Network",
    "Distribution Classification",
    "Approximate Bayesian Computation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Learning": 0.85,
    "Graph Neural Network": 0.9,
    "Distribution Classification": 0.7,
    "Approximate Bayesian Computation": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Machine Learning framework",
        "canonical": "Machine Learning",
        "aliases": [
          "ML framework"
        ],
        "category": "broad_technical",
        "rationale": "Machine Learning is a fundamental area that connects various methods and frameworks in the study.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Graph Neural Network",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Neural Networks are directly compared as a baseline, indicating a strong connection to the study's methodology.",
        "novelty_score": 0.5,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.9
      },
      {
        "surface": "Distribution Classification",
        "canonical": "Distribution Classification",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a novel method proposed in the paper, crucial for understanding its unique contribution.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Approximate Bayesian Computation",
        "canonical": "Approximate Bayesian Computation",
        "aliases": [
          "ABC"
        ],
        "category": "specific_connectable",
        "rationale": "This is a key baseline method used for comparison, providing context for the study's results.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "spreading dynamics",
      "social networks",
      "real-world situations"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Machine Learning framework",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Graph Neural Network",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Distribution Classification",
      "resolved_canonical": "Distribution Classification",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Approximate Bayesian Computation",
      "resolved_canonical": "Approximate Bayesian Computation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Learning hidden cascades via classification

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2505.11228.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2505.11228](https://arxiv.org/abs/2505.11228)

## 🔗 유사한 논문
- [[2025-09-23/Adaptive Graph Convolution and Semantic-Guided Attention for Multimodal Risk Detection in Social Networks_20250923|Adaptive Graph Convolution and Semantic-Guided Attention for Multimodal Risk Detection in Social Networks]] (81.3% similar)
- [[2025-09-25/Probabilistic Runtime Verification, Evaluation and Risk Assessment of Visual Deep Learning Systems_20250925|Probabilistic Runtime Verification, Evaluation and Risk Assessment of Visual Deep Learning Systems]] (81.0% similar)
- [[2025-09-25/Incomplete Data, Complete Dynamics_ A Diffusion Approach_20250925|Incomplete Data, Complete Dynamics: A Diffusion Approach]] (80.3% similar)
- [[2025-09-17/Defending Diffusion Models Against Membership Inference Attacks via Higher-Order Langevin Dynamics_20250917|Defending Diffusion Models Against Membership Inference Attacks via Higher-Order Langevin Dynamics]] (79.5% similar)
- [[2025-09-24/Towards Privacy-Aware Bayesian Networks_ A Credal Approach_20250924|Towards Privacy-Aware Bayesian Networks: A Credal Approach]] (79.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]], [[keywords/Approximate Bayesian Computation|Approximate Bayesian Computation]]
**⚡ Unique Technical**: [[keywords/Distribution Classification|Distribution Classification]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.11228v3 Announce Type: replace-cross 
Abstract: The spreading dynamics in social networks are often studied under the assumption that individuals' statuses, whether informed or infected, are fully observable. However, in many real-world situations, such statuses remain unobservable, which is crucial for determining an individual's potential to further spread the infection. While final statuses are hidden, intermediate indicators such as symptoms of infection are observable and provide useful representations of the underlying diffusion process. We propose a partial observability-aware Machine Learning framework to learn the characteristics of the spreading model. We term the method Distribution Classification, which utilizes the power of classifiers to infer the underlying transmission dynamics. Through extensive benchmarking against Approximate Bayesian Computation and GNN-based baselines, our framework consistently outperforms these state-of-the-art methods, delivering accurate parameter estimates across diverse diffusion settings while scaling efficiently to large networks. We validate the method on synthetic networks and extend the study to a real-world insider trading network, demonstrating its effectiveness in analyzing spreading phenomena where direct observation of individual statuses is not possible.

## 📝 요약

이 논문은 사회적 네트워크에서의 확산 동역학을 연구하며, 개인의 상태가 완전히 관찰되지 않는 상황을 다룹니다. 저자들은 부분적으로 관찰 가능한 증상 등을 활용하여 확산 모델의 특성을 학습하는 머신러닝 프레임워크를 제안합니다. 이 방법은 '분포 분류'로 불리며, 분류기의 능력을 활용해 전파 동역학을 추론합니다. 제안된 프레임워크는 Approximate Bayesian Computation 및 GNN 기반의 최신 방법들보다 우수한 성능을 보이며, 다양한 확산 환경에서 정확한 파라미터 추정을 제공합니다. 이 방법은 합성 네트워크 및 실제 내부자 거래 네트워크에 적용되어, 개인 상태의 직접 관찰이 불가능한 상황에서도 효과적으로 확산 현상을 분석할 수 있음을 입증했습니다.

## 🎯 주요 포인트

- 1. 사회적 네트워크에서의 확산 동역학은 개인의 상태가 완전히 관찰 가능하다는 가정 하에 연구되지만, 실제로는 이러한 상태가 관찰 불가능한 경우가 많다.
- 2. 중간 지표인 감염 증상은 관찰 가능하며, 확산 과정의 유용한 표현을 제공한다.
- 3. 부분 관찰 가능성을 고려한 머신러닝 프레임워크를 제안하여 확산 모델의 특성을 학습한다.
- 4. 제안된 방법인 분포 분류는 분류기의 힘을 활용하여 전파 동역학을 추론하며, 최신 방법들을 능가하는 성능을 보인다.
- 5. 이 방법은 합성 네트워크와 실제 내부자 거래 네트워크에서 검증되어, 직접적인 상태 관찰이 불가능한 확산 현상 분석에 효과적임을 입증한다.


---

*Generated on 2025-09-26 08:38:57*