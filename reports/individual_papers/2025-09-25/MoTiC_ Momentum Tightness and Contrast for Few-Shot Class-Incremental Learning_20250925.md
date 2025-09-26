---
keywords:
  - Few-Shot Learning
  - Self-supervised Learning
  - Momentum Tightness and Contrast
  - Bayesian Analysis
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19664
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:43:02.935355",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Few-Shot Learning",
    "Self-supervised Learning",
    "Momentum Tightness and Contrast",
    "Bayesian Analysis"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Few-Shot Learning": 0.85,
    "Self-supervised Learning": 0.8,
    "Momentum Tightness and Contrast": 0.78,
    "Bayesian Analysis": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Few-Shot Class-Incremental Learning",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "FSCIL"
        ],
        "category": "specific_connectable",
        "rationale": "Links to the concept of learning from limited data while adapting to new classes, a trending topic in machine learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      },
      {
        "surface": "Contrastive Learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "Contrastive Learning"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to the self-supervised learning paradigm, enhancing feature representation learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.79,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Momentum Tightness and Contrast",
        "canonical": "Momentum Tightness and Contrast",
        "aliases": [
          "MoTiC"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel framework specific to the paper, enhancing feature space representation.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Bayesian Analysis",
        "canonical": "Bayesian Analysis",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Provides a statistical approach to align class priors, relevant to many machine learning methods.",
        "novelty_score": 0.4,
        "connectivity_score": 0.7,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
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
      "candidate_surface": "Few-Shot Class-Incremental Learning",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Contrastive Learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.79,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Momentum Tightness and Contrast",
      "resolved_canonical": "Momentum Tightness and Contrast",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Bayesian Analysis",
      "resolved_canonical": "Bayesian Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.7,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# MoTiC: Momentum Tightness and Contrast for Few-Shot Class-Incremental Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19664.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19664](https://arxiv.org/abs/2509.19664)

## 🔗 유사한 논문
- [[2025-09-23/Min_ Mixture of Noise for Pre-Trained Model-Based Class-Incremental Learning_20250923|Min: Mixture of Noise for Pre-Trained Model-Based Class-Incremental Learning]] (85.1% similar)
- [[2025-09-24/Hyperbolic Coarse-to-Fine Few-Shot Class-Incremental Learning_20250924|Hyperbolic Coarse-to-Fine Few-Shot Class-Incremental Learning]] (83.0% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (82.4% similar)
- [[2025-09-19/Seeing 3D Through 2D Lenses_ 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification_20250919|Seeing 3D Through 2D Lenses: 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (81.9% similar)
- [[2025-09-24/Class-wise Balancing Data Replay for Federated Class-Incremental Learning_20250924|Class-wise Balancing Data Replay for Federated Class-Incremental Learning]] (81.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Bayesian Analysis|Bayesian Analysis]]
**🔗 Specific Connectable**: [[keywords/Few-Shot Learning|Few-Shot Learning]], [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Momentum Tightness and Contrast|Momentum Tightness and Contrast]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19664v1 Announce Type: cross 
Abstract: Few-Shot Class-Incremental Learning (FSCIL) must contend with the dual challenge of learning new classes from scarce samples while preserving old class knowledge. Existing methods use the frozen feature extractor and class-averaged prototypes to mitigate against catastrophic forgetting and overfitting. However, new-class prototypes suffer significant estimation bias due to extreme data scarcity, whereas base-class prototypes benefit from sufficient data. In this work, we theoretically demonstrate that aligning the new-class priors with old-class statistics via Bayesian analysis reduces variance and improves prototype accuracy. Furthermore, we propose large-scale contrastive learning to enforce cross-category feature tightness. To further enrich feature diversity and inject prior information for new-class prototypes, we integrate momentum self-supervision and virtual categories into the Momentum Tightness and Contrast framework (MoTiC), constructing a feature space with rich representations and enhanced interclass cohesion. Experiments on three FSCIL benchmarks produce state-of-the-art performances, particularly on the fine-grained task CUB-200, validating our method's ability to reduce estimation bias and improve incremental learning robustness.

## 📝 요약

이 논문은 Few-Shot Class-Incremental Learning (FSCIL)에서 새로운 클래스를 적은 샘플로 학습하면서 기존 클래스의 지식을 유지하는 문제를 다룹니다. 기존 방법들은 고정된 특징 추출기와 클래스 평균 프로토타입을 사용하여 망각과 과적합을 방지하지만, 새로운 클래스의 프로토타입은 데이터 부족으로 인해 큰 추정 편향을 겪습니다. 본 연구는 베이지안 분석을 통해 새로운 클래스의 사전 정보를 기존 클래스 통계와 정렬하면 분산이 줄고 프로토타입 정확도가 향상됨을 이론적으로 증명합니다. 또한, 대규모 대조 학습을 통해 범주 간 특징의 밀도를 강화하고, 모멘텀 자기 지도 학습과 가상 카테고리를 통합하여 특징 다양성을 풍부하게 합니다. 제안된 MoTiC 프레임워크는 풍부한 표현과 향상된 클래스 간 결속력을 가진 특징 공간을 구축합니다. 세 가지 FSCIL 벤치마크 실험에서 특히 세밀한 작업인 CUB-200에서 최첨단 성능을 보여주며, 추정 편향을 줄이고 증분 학습의 강건성을 향상시키는 방법의 유효성을 입증합니다.

## 🎯 주요 포인트

- 1. Few-Shot Class-Incremental Learning (FSCIL)은 새로운 클래스 학습 시 샘플 부족 문제와 기존 클래스 지식 보존 문제를 동시에 해결해야 합니다.
- 2. 기존 방법들은 고정된 특징 추출기와 클래스 평균 프로토타입을 사용하여 망각과 과적합을 완화하려고 합니다.
- 3. 새로운 클래스의 프로토타입은 데이터 부족으로 인해 큰 추정 편향을 겪는 반면, 기본 클래스 프로토타입은 충분한 데이터를 활용합니다.
- 4. 본 연구에서는 베이지안 분석을 통해 새로운 클래스의 사전 정보를 기존 클래스 통계와 정렬하여 분산을 줄이고 프로토타입 정확성을 향상시킴을 이론적으로 입증합니다.
- 5. 제안된 MoTiC 프레임워크는 모멘텀 자기 지도 학습과 가상 카테고리를 통합하여 풍부한 표현과 향상된 클래스 간 결속력을 가진 특징 공간을 구축합니다.


---

*Generated on 2025-09-25 15:43:02*