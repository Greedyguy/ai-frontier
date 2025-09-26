---
keywords:
  - Neural Network
  - Zero-Shot Learning
  - Orthogonal Transformation
  - Affine Transformation
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16664
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:41:43.326478",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Zero-Shot Learning",
    "Orthogonal Transformation",
    "Affine Transformation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.78,
    "Zero-Shot Learning": 0.79,
    "Orthogonal Transformation": 0.77,
    "Affine Transformation": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "Neural Nets"
        ],
        "category": "broad_technical",
        "rationale": "Neural Networks are central to the paper's discussion on representation learning and model compatibility.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Zero-Shot Performance",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-Shot Learning is a key aspect of the paper's evaluation of model compatibility.",
        "novelty_score": 0.55,
        "connectivity_score": 0.83,
        "specificity_score": 0.72,
        "link_intent_score": 0.79
      },
      {
        "surface": "Orthogonal Transformations",
        "canonical": "Orthogonal Transformation",
        "aliases": [
          "Orthogonal Transform"
        ],
        "category": "unique_technical",
        "rationale": "Orthogonal Transformations are crucial for understanding the geometric constraints discussed in the paper.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Affine Transformations",
        "canonical": "Affine Transformation",
        "aliases": [
          "Affine Transform"
        ],
        "category": "unique_technical",
        "rationale": "Affine Transformations are a primary method discussed for adapting learned representations.",
        "novelty_score": 0.6,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "retrieval systems",
      "extensive experiments"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Zero-Shot Performance",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.83,
        "specificity": 0.72,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Orthogonal Transformations",
      "resolved_canonical": "Orthogonal Transformation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Affine Transformations",
      "resolved_canonical": "Affine Transformation",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# $\boldsymbol{\lambda}$-Orthogonality Regularization for Compatible Representation Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16664.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16664](https://arxiv.org/abs/2509.16664)

## 🔗 유사한 논문
- [[2025-09-23/Probabilistic Token Alignment for Large Language Model Fusion_20250923|Probabilistic Token Alignment for Large Language Model Fusion]] (83.7% similar)
- [[2025-09-23/LifeAlign_ Lifelong Alignment for Large Language Models with Memory-Augmented Focalized Preference Optimization_20250923|LifeAlign: Lifelong Alignment for Large Language Models with Memory-Augmented Focalized Preference Optimization]] (82.1% similar)
- [[2025-09-17/Consistent View Alignment Improves Foundation Models for 3D Medical Image Segmentation_20250917|Consistent View Alignment Improves Foundation Models for 3D Medical Image Segmentation]] (82.1% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (81.7% similar)
- [[2025-09-23/Bridging Past and Future_ Distribution-Aware Alignment for Time Series Forecasting_20250923|Bridging Past and Future: Distribution-Aware Alignment for Time Series Forecasting]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Orthogonal Transformation|Orthogonal Transformation]], [[keywords/Affine Transformation|Affine Transformation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16664v1 Announce Type: new 
Abstract: Retrieval systems rely on representations learned by increasingly powerful models. However, due to the high training cost and inconsistencies in learned representations, there is significant interest in facilitating communication between representations and ensuring compatibility across independently trained neural networks. In the literature, two primary approaches are commonly used to adapt different learned representations: affine transformations, which adapt well to specific distributions but can significantly alter the original representation, and orthogonal transformations, which preserve the original structure with strict geometric constraints but limit adaptability. A key challenge is adapting the latent spaces of updated models to align with those of previous models on downstream distributions while preserving the newly learned representation spaces. In this paper, we impose a relaxed orthogonality constraint, namely $\lambda$-orthogonality regularization, while learning an affine transformation, to obtain distribution-specific adaptation while retaining the original learned representations. Extensive experiments across various architectures and datasets validate our approach, demonstrating that it preserves the model's zero-shot performance and ensures compatibility across model updates. Code available at: https://github.com/miccunifi/lambda_orthogonality

## 📝 요약

이 논문은 검색 시스템에서 사용되는 표현 학습 모델 간의 호환성을 개선하기 위한 방법을 제안합니다. 기존의 표현 학습 모델 간의 불일치 문제를 해결하기 위해, 저자들은 완화된 직교성 제약 조건인 $\lambda$-직교성 정규화를 도입하여 새로운 표현 공간을 유지하면서도 이전 모델과의 호환성을 보장하는 방법론을 개발했습니다. 이 방법은 다양한 아키텍처와 데이터셋에서 실험을 통해 검증되었으며, 모델 업데이트 시에도 제로샷 성능을 유지하고 호환성을 보장하는 것으로 나타났습니다.

## 🎯 주요 포인트

- 1. 검색 시스템은 점점 더 강력해지는 모델에 의해 학습된 표현에 의존하지만, 독립적으로 학습된 신경망 간의 호환성을 보장하는 것이 중요합니다.
- 2. 기존의 표현을 크게 변경할 수 있는 아핀 변환과 엄격한 기하학적 제약을 가지는 직교 변환이 주로 사용됩니다.
- 3. 본 논문에서는 아핀 변환을 학습하면서 $\lambda$-직교성 정규화를 적용하여 원래의 학습된 표현을 유지하면서도 분포별 적응을 가능하게 합니다.
- 4. 다양한 아키텍처와 데이터셋에 대한 실험을 통해 제안된 방법이 모델의 제로샷 성능을 유지하고 모델 업데이트 간의 호환성을 보장함을 입증했습니다.
- 5. 연구 결과는 코드와 함께 공개되어 있으며, 이는 모델 업데이트 시 호환성 문제를 해결하는 데 기여할 수 있습니다.


---

*Generated on 2025-09-24 01:41:43*