---
keywords:
  - Zero-Shot Learning
  - Speaker Verification
  - Adversarial Mixup Regularization
  - Embedding Space
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2503.16718
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:02:31.240507",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Zero-Shot Learning",
    "Speaker Verification",
    "Adversarial Mixup Regularization",
    "Embedding Space"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Zero-Shot Learning": 0.88,
    "Speaker Verification": 0.78,
    "Adversarial Mixup Regularization": 0.82,
    "Embedding Space": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Zero-Shot Learning",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "zero-shot"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-Shot Learning is a key concept in the paper, linking it to broader trends in machine learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "Speaker Verification",
        "canonical": "Speaker Verification",
        "aliases": [
          "voice authentication"
        ],
        "category": "unique_technical",
        "rationale": "Speaker Verification is a unique application area discussed in the paper, crucial for understanding its context.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Adversarial Mixup Regularization",
        "canonical": "Adversarial Mixup Regularization",
        "aliases": [
          "adversarial mixup"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel technique introduced in the paper, central to its contributions.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      },
      {
        "surface": "Embedding Space",
        "canonical": "Embedding Space",
        "aliases": [
          "latent space"
        ],
        "category": "broad_technical",
        "rationale": "Embedding Space is a fundamental concept in machine learning, relevant to the paper's methodology.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.65
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
      "candidate_surface": "Zero-Shot Learning",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Speaker Verification",
      "resolved_canonical": "Speaker Verification",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Adversarial Mixup Regularization",
      "resolved_canonical": "Adversarial Mixup Regularization",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Embedding Space",
      "resolved_canonical": "Embedding Space",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# CAARMA: Class Augmentation with Adversarial Mixup Regularization

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2503.16718.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2503.16718](https://arxiv.org/abs/2503.16718)

## 🔗 유사한 논문
- [[2025-09-22/MoCA_ Multi-modal Cross-masked Autoencoder for Digital Health Measurements_20250922|MoCA: Multi-modal Cross-masked Autoencoder for Digital Health Measurements]] (80.9% similar)
- [[2025-09-23/Intra-Cluster Mixup_ An Effective Data Augmentation Technique for Complementary-Label Learning_20250923|Intra-Cluster Mixup: An Effective Data Augmentation Technique for Complementary-Label Learning]] (80.4% similar)
- [[2025-09-19/Multimodal Knowledge Distillation for Egocentric Action Recognition Robust to Missing Modalities_20250919|Multimodal Knowledge Distillation for Egocentric Action Recognition Robust to Missing Modalities]] (80.2% similar)
- [[2025-09-22/Session-Level Spoken Language Assessment with a Multimodal Foundation Model via Multi-Target Learning_20250922|Session-Level Spoken Language Assessment with a Multimodal Foundation Model via Multi-Target Learning]] (80.1% similar)
- [[2025-09-23/MVCL-DAF++_ Enhancing Multimodal Intent Recognition via Prototype-Aware Contrastive Alignment and Coarse-to-Fine Dynamic Attention Fusion_20250923|MVCL-DAF++: Enhancing Multimodal Intent Recognition via Prototype-Aware Contrastive Alignment and Coarse-to-Fine Dynamic Attention Fusion]] (80.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Embedding Space|Embedding Space]]
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Speaker Verification|Speaker Verification]], [[keywords/Adversarial Mixup Regularization|Adversarial Mixup Regularization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.16718v3 Announce Type: replace-cross 
Abstract: Speaker verification is a typical zero-shot learning task, where inference of unseen classes is performed by comparing embeddings of test instances to known examples. The models performing inference must hence naturally generate embeddings that cluster same-class instances compactly, while maintaining separation across classes. In order to learn to do so, they are typically trained on a large number of classes (speakers), often using specialized losses. However real-world speaker datasets often lack the class diversity needed to effectively learn this in a generalizable manner. We introduce CAARMA, a class augmentation framework that addresses this problem by generating synthetic classes through data mixing in the embedding space, expanding the number of training classes. To ensure the authenticity of the synthetic classes we adopt a novel adversarial refinement mechanism that minimizes categorical distinctions between synthetic and real classes. We evaluate CAARMA on multiple speaker verification tasks, as well as other representative zero-shot comparison-based speech analysis tasks and obtain consistent improvements: our framework demonstrates a significant improvement of 8\% over all baseline models. The code is available at: https://github.com/massabaali7/CAARMA/

## 📝 요약

이 논문은 화자 검증에서 제로샷 학습 문제를 해결하기 위해 CAARMA라는 클래스 증강 프레임워크를 제안합니다. CAARMA는 임베딩 공간에서 데이터 혼합을 통해 합성 클래스를 생성하여 훈련 클래스 수를 확장합니다. 합성 클래스의 진정성을 보장하기 위해 새로운 적대적 정제 메커니즘을 도입하여 합성 클래스와 실제 클래스 간의 범주적 차이를 최소화합니다. CAARMA는 여러 화자 검증 작업과 제로샷 비교 기반 음성 분석 작업에서 8%의 성능 향상을 보여주었습니다.

## 🎯 주요 포인트

- 1. 화자 검증은 보통 제로샷 학습 과제로, 테스트 인스턴스의 임베딩을 알려진 예시와 비교하여 미지의 클래스를 추론합니다.
- 2. CAARMA는 임베딩 공간에서 데이터 혼합을 통해 합성 클래스를 생성하여 훈련 클래스 수를 확장하는 클래스 증강 프레임워크입니다.
- 3. 합성 클래스의 진정성을 보장하기 위해 합성과 실제 클래스 간의 범주적 차이를 최소화하는 새로운 적대적 정제 메커니즘을 채택했습니다.
- 4. CAARMA는 여러 화자 검증 및 제로샷 비교 기반 음성 분석 작업에서 일관된 성능 향상을 보여주었으며, 모든 기준 모델 대비 8%의 유의미한 개선을 달성했습니다.


---

*Generated on 2025-09-24 03:02:31*