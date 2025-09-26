---
keywords:
  - Differentially Private Stochastic Gradient Descent
  - Gradient Clipping
  - Geometry-Aware Clipping
  - Gradient Distribution
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2506.06549
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:45:13.824761",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Differentially Private Stochastic Gradient Descent",
    "Gradient Clipping",
    "Geometry-Aware Clipping",
    "Gradient Distribution"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Differentially Private Stochastic Gradient Descent": 0.8,
    "Gradient Clipping": 0.78,
    "Geometry-Aware Clipping": 0.85,
    "Gradient Distribution": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Differentially Private Stochastic Gradient Descent",
        "canonical": "Differentially Private Stochastic Gradient Descent",
        "aliases": [
          "DP-SGD"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific technique for ensuring privacy in machine learning, crucial for linking privacy-focused research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Gradient Clipping",
        "canonical": "Gradient Clipping",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A common technique in optimization that can be linked to various machine learning methods.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Geometry-Aware Clipping",
        "canonical": "Geometry-Aware Clipping",
        "aliases": [
          "GeoClip"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach to gradient clipping that considers geometric properties, enhancing privacy-utility trade-offs.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Gradient Distribution",
        "canonical": "Gradient Distribution",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Understanding gradient distribution is key for optimization techniques and can connect to statistical analysis methods.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Differentially Private Stochastic Gradient Descent",
      "resolved_canonical": "Differentially Private Stochastic Gradient Descent",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Gradient Clipping",
      "resolved_canonical": "Gradient Clipping",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Geometry-Aware Clipping",
      "resolved_canonical": "Geometry-Aware Clipping",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Gradient Distribution",
      "resolved_canonical": "Gradient Distribution",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# GeoClip: Geometry-Aware Clipping for Differentially Private SGD

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2506.06549.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2506.06549](https://arxiv.org/abs/2506.06549)

## 🔗 유사한 논문
- [[2025-09-23/Preserving Node-level Privacy in Graph Neural Networks_20250923|Preserving Node-level Privacy in Graph Neural Networks]] (81.6% similar)
- [[2025-09-19/Seeing 3D Through 2D Lenses_ 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification_20250919|Seeing 3D Through 2D Lenses: 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (80.3% similar)
- [[2025-09-22/Analysis Plug-and-Play Methods for Imaging Inverse Problems_20250922|Analysis Plug-and-Play Methods for Imaging Inverse Problems]] (80.3% similar)
- [[2025-09-18/Stochastic Adaptive Gradient Descent Without Descent_20250918|Stochastic Adaptive Gradient Descent Without Descent]] (79.7% similar)
- [[2025-09-18/Singular Value Few-shot Adaptation of Vision-Language Models_20250918|Singular Value Few-shot Adaptation of Vision-Language Models]] (78.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Gradient Clipping|Gradient Clipping]], [[keywords/Gradient Distribution|Gradient Distribution]]
**⚡ Unique Technical**: [[keywords/Differentially Private Stochastic Gradient Descent|Differentially Private Stochastic Gradient Descent]], [[keywords/Geometry-Aware Clipping|Geometry-Aware Clipping]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.06549v2 Announce Type: replace 
Abstract: Differentially private stochastic gradient descent (DP-SGD) is the most widely used method for training machine learning models with provable privacy guarantees. A key challenge in DP-SGD is setting the per-sample gradient clipping threshold, which significantly affects the trade-off between privacy and utility. While recent adaptive methods improve performance by adjusting this threshold during training, they operate in the standard coordinate system and fail to account for correlations across the coordinates of the gradient. We propose GeoClip, a geometry-aware framework that clips and perturbs gradients in a transformed basis aligned with the geometry of the gradient distribution. GeoClip adaptively estimates this transformation using only previously released noisy gradients, incurring no additional privacy cost. We provide convergence guarantees for GeoClip and derive a closed-form solution for the optimal transformation that minimizes the amount of noise added while keeping the probability of gradient clipping under control. Experiments on both tabular and image datasets demonstrate that GeoClip consistently outperforms existing adaptive clipping methods under the same privacy budget.

## 📝 요약

이 논문은 기하학적 정보를 활용한 새로운 차등적 프라이버시 경사 하강법(DP-SGD) 방법인 GeoClip을 제안합니다. 기존 방법들은 좌표계에서 경사 간의 상관관계를 고려하지 못했으나, GeoClip은 경사 분포의 기하학에 맞춰 변환된 기저에서 경사를 클리핑하고 노이즈를 추가합니다. 이 방법은 이전에 공개된 노이즈가 포함된 경사만을 사용하여 변환을 추정하므로 추가적인 프라이버시 비용이 발생하지 않습니다. GeoClip은 수렴 보장을 제공하며, 최적의 변환을 통해 노이즈 추가를 최소화하면서 경사 클리핑 확률을 제어합니다. 실험 결과, GeoClip은 동일한 프라이버시 예산 하에서 기존의 적응형 클리핑 방법보다 일관되게 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. DP-SGD의 주요 과제는 샘플별 그래디언트 클리핑 임계값 설정으로, 이는 프라이버시와 유틸리티 간의 균형에 큰 영향을 미친다.
- 2. GeoClip은 그래디언트 분포의 기하학적 특성에 맞춰 변환된 기저에서 그래디언트를 클리핑하고 노이즈를 추가하는 기하학적 인식 프레임워크를 제안한다.
- 3. GeoClip은 이전에 공개된 노이즈가 포함된 그래디언트만을 사용하여 변환을 적응적으로 추정하며 추가적인 프라이버시 비용을 발생시키지 않는다.
- 4. GeoClip의 수렴 보장을 제공하고, 그래디언트 클리핑 확률을 제어하면서 추가되는 노이즈를 최소화하는 최적 변환의 닫힌 형태 해를 도출한다.
- 5. 실험 결과, GeoClip은 동일한 프라이버시 예산 하에서 기존의 적응형 클리핑 방법보다 일관되게 우수한 성능을 보인다.


---

*Generated on 2025-09-24 02:45:13*