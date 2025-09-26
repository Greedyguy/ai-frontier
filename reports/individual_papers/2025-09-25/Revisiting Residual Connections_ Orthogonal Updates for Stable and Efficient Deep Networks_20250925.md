---
keywords:
  - Residual Connections
  - Orthogonal Residual Update
  - Vision Transformers
  - Deep Learning
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2505.11881
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:24:45.726564",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Residual Connections",
    "Orthogonal Residual Update",
    "Vision Transformers",
    "Deep Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Residual Connections": 0.78,
    "Orthogonal Residual Update": 0.82,
    "Vision Transformers": 0.79,
    "Deep Learning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Residual Connections",
        "canonical": "Residual Connections",
        "aliases": [
          "Residual Links"
        ],
        "category": "specific_connectable",
        "rationale": "Residual connections are a fundamental component in deep learning architectures, enhancing connectivity and stability.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.78
      },
      {
        "surface": "Orthogonal Residual Update",
        "canonical": "Orthogonal Residual Update",
        "aliases": [
          "Orthogonal Update"
        ],
        "category": "unique_technical",
        "rationale": "This novel approach enhances feature learning by introducing orthogonal updates, offering a unique perspective in neural network training.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Vision Transformers",
        "canonical": "Vision Transformers",
        "aliases": [
          "ViT"
        ],
        "category": "specific_connectable",
        "rationale": "Vision Transformers are a key architecture in computer vision, relevant for linking advancements in model design.",
        "novelty_score": 0.6,
        "connectivity_score": 0.87,
        "specificity_score": 0.75,
        "link_intent_score": 0.79
      },
      {
        "surface": "Deep Neural Networks",
        "canonical": "Deep Learning",
        "aliases": [
          "DNNs"
        ],
        "category": "broad_technical",
        "rationale": "Deep Learning is a broad technical category that encompasses the study and application of deep neural networks.",
        "novelty_score": 0.4,
        "connectivity_score": 0.92,
        "specificity_score": 0.65,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "module's output",
      "input stream"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Residual Connections",
      "resolved_canonical": "Residual Connections",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Orthogonal Residual Update",
      "resolved_canonical": "Orthogonal Residual Update",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Vision Transformers",
      "resolved_canonical": "Vision Transformers",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.87,
        "specificity": 0.75,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Deep Neural Networks",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.92,
        "specificity": 0.65,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Revisiting Residual Connections: Orthogonal Updates for Stable and Efficient Deep Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.11881.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2505.11881](https://arxiv.org/abs/2505.11881)

## 🔗 유사한 논문
- [[2025-09-23/Pulling Back the Curtain on ReLU Networks_20250923|Pulling Back the Curtain on ReLU Networks]] (81.6% similar)
- [[2025-09-24/Shared-Weights Extender and Gradient Voting for Neural Network Expansion_20250924|Shared-Weights Extender and Gradient Voting for Neural Network Expansion]] (81.2% similar)
- [[2025-09-17/A Variational Framework for Residual-Based Adaptivity in Neural PDE Solvers and Operator Learning_20250917|A Variational Framework for Residual-Based Adaptivity in Neural PDE Solvers and Operator Learning]] (81.1% similar)
- [[2025-09-23/Controlling Neural Collapse Enhances Out-of-Distribution Detection and Transfer Learning_20250923|Controlling Neural Collapse Enhances Out-of-Distribution Detection and Transfer Learning]] (80.8% similar)
- [[2025-09-23/Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs_20250923|Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs]] (80.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Residual Connections|Residual Connections]], [[keywords/Vision Transformers|Vision Transformers]]
**⚡ Unique Technical**: [[keywords/Orthogonal Residual Update|Orthogonal Residual Update]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.11881v2 Announce Type: replace-cross 
Abstract: Residual connections are pivotal for deep neural networks, enabling greater depth by mitigating vanishing gradients. However, in standard residual updates, the module's output is directly added to the input stream. This can lead to updates that predominantly reinforce or modulate the existing stream direction, potentially underutilizing the module's capacity for learning entirely novel features. In this work, we introduce Orthogonal Residual Update: we decompose the module's output relative to the input stream and add only the component orthogonal to this stream. This design aims to guide modules to contribute primarily new representational directions, fostering richer feature learning while promoting more efficient training. We demonstrate that our orthogonal update strategy improves generalization accuracy and training stability across diverse architectures (ResNetV2, Vision Transformers) and datasets (CIFARs, TinyImageNet, ImageNet-1k), achieving, for instance, a +4.3\%p top-1 accuracy gain for ViT-B on ImageNet-1k.

## 📝 요약

이 논문은 심층 신경망에서 잔차 연결의 한계를 극복하기 위해 '직교 잔차 업데이트'를 제안합니다. 기존의 잔차 업데이트는 모듈의 출력을 입력 스트림에 직접 추가하여 새로운 특징 학습을 제한할 수 있습니다. 제안된 방법은 모듈 출력을 입력 스트림에 직교하는 성분만 추가하여 새로운 표현 방향을 학습하도록 유도합니다. 이를 통해 특징 학습을 풍부하게 하고 훈련 효율성을 높입니다. 다양한 아키텍처(ResNetV2, Vision Transformers)와 데이터셋(CIFARs, TinyImageNet, ImageNet-1k)에서 일반화 정확도와 훈련 안정성을 향상시켰으며, 특히 ImageNet-1k에서 ViT-B의 top-1 정확도를 4.3%p 개선했습니다.

## 🎯 주요 포인트

- 1. 잔차 연결은 심층 신경망에서 소멸 기울기를 완화하여 더 큰 깊이를 가능하게 한다.
- 2. 기존 잔차 업데이트는 모듈의 출력을 입력 스트림에 직접 추가하여 새로운 특징 학습을 저해할 수 있다.
- 3. 본 연구에서는 입력 스트림에 대해 직교하는 성분만 추가하는 직교 잔차 업데이트를 제안한다.
- 4. 직교 업데이트 전략은 새로운 표현 방향을 주로 기여하게 하여 풍부한 특징 학습과 효율적인 훈련을 촉진한다.
- 5. 제안된 방법은 다양한 아키텍처와 데이터셋에서 일반화 정확도와 훈련 안정성을 향상시킨다.


---

*Generated on 2025-09-25 16:24:45*