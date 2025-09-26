---
keywords:
  - Source-Free Domain Adaptation
  - Remote Sensing Semantic Segmentation
  - Prototype-Based Pseudo-Label Denoising
  - Self-supervised Learning
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.16942
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:38:51.086824",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Source-Free Domain Adaptation",
    "Remote Sensing Semantic Segmentation",
    "Prototype-Based Pseudo-Label Denoising",
    "Self-supervised Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Source-Free Domain Adaptation": 0.78,
    "Remote Sensing Semantic Segmentation": 0.77,
    "Prototype-Based Pseudo-Label Denoising": 0.79,
    "Self-supervised Learning": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Source-Free Domain Adaptation",
        "canonical": "Source-Free Domain Adaptation",
        "aliases": [
          "SFDA"
        ],
        "category": "unique_technical",
        "rationale": "This is a specialized technique in domain adaptation, crucial for linking discussions on domain shift without source data.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Remote Sensing Semantic Segmentation",
        "canonical": "Remote Sensing Semantic Segmentation",
        "aliases": [
          "RSI Segmentation"
        ],
        "category": "unique_technical",
        "rationale": "This term is highly specific to the application of semantic segmentation in remote sensing, providing a distinct link point.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.77
      },
      {
        "surface": "Prototype-Based Pseudo-Label Denoising",
        "canonical": "Prototype-Based Pseudo-Label Denoising",
        "aliases": [
          "Prototype-Weighted Pseudo-Labels"
        ],
        "category": "unique_technical",
        "rationale": "This technique is central to the paper's contribution, offering a novel approach to improve pseudo-label reliability.",
        "novelty_score": 0.8,
        "connectivity_score": 0.55,
        "specificity_score": 0.9,
        "link_intent_score": 0.79
      },
      {
        "surface": "Self-Training",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "ST"
        ],
        "category": "specific_connectable",
        "rationale": "Self-training is a form of self-supervised learning, relevant for linking to broader discussions on learning paradigms.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "domain shift",
      "ground-truth supervision"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Source-Free Domain Adaptation",
      "resolved_canonical": "Source-Free Domain Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Remote Sensing Semantic Segmentation",
      "resolved_canonical": "Remote Sensing Semantic Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Prototype-Based Pseudo-Label Denoising",
      "resolved_canonical": "Prototype-Based Pseudo-Label Denoising",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.55,
        "specificity": 0.9,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Self-Training",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Prototype-Based Pseudo-Label Denoising for Source-Free Domain Adaptation in Remote Sensing Semantic Segmentation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16942.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.16942](https://arxiv.org/abs/2509.16942)

## 🔗 유사한 논문
- [[2025-09-23/Training-Free Label Space Alignment for Universal Domain Adaptation_20250923|Training-Free Label Space Alignment for Universal Domain Adaptation]] (82.8% similar)
- [[2025-09-22/pFedSAM_ Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation_20250922|pFedSAM: Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation]] (81.6% similar)
- [[2025-09-23/Unsupervised Structural-Counterfactual Generation under Domain Shift_20250923|Unsupervised Structural-Counterfactual Generation under Domain Shift]] (81.2% similar)
- [[2025-09-18/Masked Feature Modeling Enhances Adaptive Segmentation_20250918|Masked Feature Modeling Enhances Adaptive Segmentation]] (81.0% similar)
- [[2025-09-22/Improving Anomalous Sound Detection with Attribute-aware Representation from Domain-adaptive Pre-training_20250922|Improving Anomalous Sound Detection with Attribute-aware Representation from Domain-adaptive Pre-training]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Source-Free Domain Adaptation|Source-Free Domain Adaptation]], [[keywords/Remote Sensing Semantic Segmentation|Remote Sensing Semantic Segmentation]], [[keywords/Prototype-Based Pseudo-Label Denoising|Prototype-Based Pseudo-Label Denoising]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16942v1 Announce Type: new 
Abstract: Source-Free Domain Adaptation (SFDA) enables domain adaptation for semantic segmentation of Remote Sensing Images (RSIs) using only a well-trained source model and unlabeled target domain data. However, the lack of ground-truth labels in the target domain often leads to the generation of noisy pseudo-labels. Such noise impedes the effective mitigation of domain shift (DS). To address this challenge, we propose ProSFDA, a prototype-guided SFDA framework. It employs prototype-weighted pseudo-labels to facilitate reliable self-training (ST) under pseudo-labels noise. We, in addition, introduce a prototype-contrast strategy that encourages the aggregation of features belonging to the same class, enabling the model to learn discriminative target domain representations without relying on ground-truth supervision. Extensive experiments show that our approach substantially outperforms existing methods.

## 📝 요약

이 논문은 원천 모델과 라벨이 없는 목표 도메인 데이터만을 사용하여 원격 감지 이미지의 의미론적 분할을 위한 도메인 적응을 가능하게 하는 Source-Free Domain Adaptation(SFDA)을 다룹니다. 목표 도메인에 대한 실제 라벨이 없어 발생하는 노이즈 문제를 해결하기 위해, 저자들은 ProSFDA라는 프로토타입 기반의 SFDA 프레임워크를 제안합니다. 이 프레임워크는 프로토타입 가중치를 활용한 신뢰성 있는 자기 학습을 통해 노이즈 문제를 완화하며, 프로토타입 대조 전략을 도입하여 동일 클래스의 특징을 집합화하고 차별적인 목표 도메인 표현을 학습할 수 있도록 합니다. 실험 결과, 제안된 방법이 기존 방법들보다 뛰어난 성능을 보였습니다.

## 🎯 주요 포인트

- 1. Source-Free Domain Adaptation (SFDA)는 원천 모델과 레이블이 없는 대상 도메인 데이터만을 사용하여 원격 감지 이미지의 의미론적 분할을 위한 도메인 적응을 가능하게 합니다.
- 2. 대상 도메인에서의 실제 레이블 부족은 종종 노이즈가 있는 의사 레이블을 생성하게 하여 도메인 이동의 효과적인 완화를 방해합니다.
- 3. ProSFDA는 프로토타입 가중 의사 레이블을 사용하여 의사 레이블 노이즈 하에서 신뢰할 수 있는 자기 학습을 촉진하는 프로토타입 기반 SFDA 프레임워크입니다.
- 4. 프로토타입 대비 전략을 도입하여 동일한 클래스에 속하는 특징의 집합을 장려하고, 실제 레이블 감독 없이도 변별력 있는 대상 도메인 표현을 학습할 수 있게 합니다.
- 5. 광범위한 실험을 통해 제안된 방법이 기존 방법보다 상당히 우수한 성능을 보임을 입증하였습니다.


---

*Generated on 2025-09-24 04:38:51*