<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:50:29.944641",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Hyperbolic Space",
    "Few-Shot Learning",
    "Hyperbolic Contrastive Loss",
    "Maximum Entropy Distribution"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Hyperbolic Space": 0.88,
    "Few-Shot Learning": 0.92,
    "Hyperbolic Contrastive Loss": 0.8,
    "Maximum Entropy Distribution": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Hyperbolic Space",
        "canonical": "Hyperbolic Space",
        "aliases": [
          "Poincaré Ball",
          "Hyperbolic Geometry"
        ],
        "category": "specific_connectable",
        "rationale": "Hyperbolic space is crucial for representing hierarchical data, which is central to the paper's methodology.",
        "novelty_score": 0.75,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "Few-Shot Class-Incremental Learning",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "C2FSCIL",
          "Few-Shot Incremental Learning"
        ],
        "category": "specific_connectable",
        "rationale": "This is a specific task that combines few-shot learning with class-incremental learning, a trending topic.",
        "novelty_score": 0.7,
        "connectivity_score": 0.9,
        "specificity_score": 0.85,
        "link_intent_score": 0.92
      },
      {
        "surface": "Hyperbolic Contrastive Loss",
        "canonical": "Hyperbolic Contrastive Loss",
        "aliases": [
          "Hyperbolic Loss",
          "Contrastive Loss in Hyperbolic Space"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel loss function tailored for hyperbolic space, enhancing model optimization.",
        "novelty_score": 0.78,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "Maximum Entropy Distribution",
        "canonical": "Maximum Entropy Distribution",
        "aliases": [
          "MaxEnt Distribution"
        ],
        "category": "unique_technical",
        "rationale": "Used to estimate probability distributions in hyperbolic space, crucial for feature augmentation.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
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
      "candidate_surface": "Hyperbolic Space",
      "resolved_canonical": "Hyperbolic Space",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Few-Shot Class-Incremental Learning",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.9,
        "specificity": 0.85,
        "link_intent": 0.92
      }
    },
    {
      "candidate_surface": "Hyperbolic Contrastive Loss",
      "resolved_canonical": "Hyperbolic Contrastive Loss",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Maximum Entropy Distribution",
      "resolved_canonical": "Maximum Entropy Distribution",
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

# Hyperbolic Coarse-to-Fine Few-Shot Class-Incremental Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18504.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18504](https://arxiv.org/abs/2509.18504)

## 🔗 유사한 논문
- [[2025-09-19/Seeing 3D Through 2D Lenses_ 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification_20250919|Seeing 3D Through 2D Lenses: 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (82.2% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (81.7% similar)
- [[2025-09-23/Superpixel Graph Contrastive Clustering with Semantic-Invariant Augmentations for Hyperspectral Images_20250923|Superpixel Graph Contrastive Clustering with Semantic-Invariant Augmentations for Hyperspectral Images]] (80.7% similar)
- [[2025-09-23/Learning Attribute-Aware Hash Codes for Fine-Grained Image Retrieval via Query Optimization_20250923|Learning Attribute-Aware Hash Codes for Fine-Grained Image Retrieval via Query Optimization]] (80.3% similar)
- [[2025-09-22/Self-Supervised Cross-Modal Learning for Image-to-Point Cloud Registration_20250922|Self-Supervised Cross-Modal Learning for Image-to-Point Cloud Registration]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Hyperbolic Space|Hyperbolic Space]], [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Hyperbolic Contrastive Loss|Hyperbolic Contrastive Loss]], [[keywords/Maximum Entropy Distribution|Maximum Entropy Distribution]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18504v1 Announce Type: cross 
Abstract: In the field of machine learning, hyperbolic space demonstrates superior representation capabilities for hierarchical data compared to conventional Euclidean space. This work focuses on the Coarse-To-Fine Few-Shot Class-Incremental Learning (C2FSCIL) task. Our study follows the Knowe approach, which contrastively learns coarse class labels and subsequently normalizes and freezes the classifier weights of learned fine classes in the embedding space. To better interpret the "coarse-to-fine" paradigm, we propose embedding the feature extractor into hyperbolic space. Specifically, we employ the Poincar\'e ball model of hyperbolic space, enabling the feature extractor to transform input images into feature vectors within the Poincar\'e ball instead of Euclidean space. We further introduce hyperbolic contrastive loss and hyperbolic fully-connected layers to facilitate model optimization and classification in hyperbolic space. Additionally, to enhance performance under few-shot conditions, we implement maximum entropy distribution in hyperbolic space to estimate the probability distribution of fine-class feature vectors. This allows generation of augmented features from the distribution to mitigate overfitting during training with limited samples. Experiments on C2FSCIL benchmarks show that our method effectively improves both coarse and fine class accuracies.

## 📝 요약

이 논문은 계층적 데이터를 표현하는 데 있어 유클리드 공간보다 뛰어난 성능을 보이는 쌍곡 공간을 활용한 연구를 다룹니다. Coarse-To-Fine Few-Shot Class-Incremental Learning(C2FSCIL) 과제를 중심으로, Knowe 접근법을 따라 대조 학습을 통해 거친 클래스 레이블을 학습하고, 세밀한 클래스의 분류기 가중치를 임베딩 공간에서 정규화 및 고정합니다. 특히, Poincaré 공 모델을 사용하여 입력 이미지를 쌍곡 공간 내의 특징 벡터로 변환하며, 쌍곡 대조 손실과 쌍곡 완전연결층을 도입하여 모델 최적화 및 분류를 지원합니다. 또한, 소수 샷 조건에서 성능 향상을 위해 쌍곡 공간에서 최대 엔트로피 분포를 사용하여 세밀한 클래스 특징 벡터의 확률 분포를 추정하고, 이를 통해 생성된 증강 특징을 활용해 과적합을 완화합니다. 실험 결과, 제안된 방법이 C2FSCIL 벤치마크에서 거친 클래스와 세밀한 클래스의 정확도를 효과적으로 개선함을 보여줍니다.

## 🎯 주요 포인트

- 1. 하이퍼볼릭 공간은 계층적 데이터를 표현하는 데 유클리드 공간보다 우수한 성능을 보인다.
- 2. 본 연구는 Coarse-To-Fine Few-Shot Class-Incremental Learning (C2FSCIL) 과제에 초점을 맞추고 있다.
- 3. Poincaré ball 모델을 사용하여 입력 이미지를 하이퍼볼릭 공간의 특징 벡터로 변환한다.
- 4. 하이퍼볼릭 대조 손실과 완전 연결 계층을 도입하여 모델 최적화 및 분류를 지원한다.
- 5. 최대 엔트로피 분포를 활용하여 제한된 샘플로 인한 과적합을 완화하고 성능을 향상시킨다.


---

*Generated on 2025-09-24 13:50:29*