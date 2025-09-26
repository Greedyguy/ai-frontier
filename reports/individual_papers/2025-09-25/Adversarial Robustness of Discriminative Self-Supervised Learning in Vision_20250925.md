---
keywords:
  - Self-supervised Learning
  - Adversarial Robustness
  - ImageNet Classification
  - Transfer Learning
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2503.06361
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:23:49.784535",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-supervised Learning",
    "Adversarial Robustness",
    "ImageNet Classification",
    "Transfer Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Self-supervised Learning": 0.85,
    "Adversarial Robustness": 0.8,
    "ImageNet Classification": 0.78,
    "Transfer Learning": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Self-supervised learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "SSL"
        ],
        "category": "specific_connectable",
        "rationale": "Self-supervised learning is a central theme of the paper and is crucial for linking discussions on learning paradigms.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Adversarial robustness",
        "canonical": "Adversarial Robustness",
        "aliases": [
          "Robustness to adversarial attacks"
        ],
        "category": "unique_technical",
        "rationale": "The paper focuses on evaluating adversarial robustness, making it a unique technical aspect for linking.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "ImageNet classification",
        "canonical": "ImageNet Classification",
        "aliases": [
          "ImageNet"
        ],
        "category": "specific_connectable",
        "rationale": "ImageNet classification is a standard benchmark in vision, providing strong connectivity to other works.",
        "novelty_score": 0.3,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Transfer learning",
        "canonical": "Transfer Learning",
        "aliases": [
          "Transfer"
        ],
        "category": "broad_technical",
        "rationale": "Transfer learning is a widely applicable concept that enhances the paper's connectivity to broader machine learning discussions.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "segmentation",
      "detection",
      "architectural choices",
      "training duration"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Self-supervised learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Adversarial robustness",
      "resolved_canonical": "Adversarial Robustness",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "ImageNet classification",
      "resolved_canonical": "ImageNet Classification",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Transfer learning",
      "resolved_canonical": "Transfer Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Adversarial Robustness of Discriminative Self-Supervised Learning in Vision

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2503.06361.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2503.06361](https://arxiv.org/abs/2503.06361)

## 🔗 유사한 논문
- [[2025-09-23/Enhancing Semantic Segmentation with Continual Self-Supervised Pre-training_20250923|Enhancing Semantic Segmentation with Continual Self-Supervised Pre-training]] (85.9% similar)
- [[2025-09-24/DiSSECT_ Structuring Transfer-Ready Medical Image Representations through Discrete Self-Supervision_20250924|DiSSECT: Structuring Transfer-Ready Medical Image Representations through Discrete Self-Supervision]] (83.7% similar)
- [[2025-09-23/Leveraging Audio-Visual Data to Reduce the Multilingual Gap in Self-Supervised Speech Models_20250923|Leveraging Audio-Visual Data to Reduce the Multilingual Gap in Self-Supervised Speech Models]] (83.0% similar)
- [[2025-09-22/Which Direction to Choose? An Analysis on the Representation Power of Self-Supervised ViTs in Downstream Tasks_20250922|Which Direction to Choose? An Analysis on the Representation Power of Self-Supervised ViTs in Downstream Tasks]] (82.4% similar)
- [[2025-09-24/RoSe_ Robust Self-supervised Stereo Matching under Adverse Weather Conditions_20250924|RoSe: Robust Self-supervised Stereo Matching under Adverse Weather Conditions]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transfer Learning|Transfer Learning]]
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]], [[keywords/ImageNet Classification|ImageNet Classification]]
**⚡ Unique Technical**: [[keywords/Adversarial Robustness|Adversarial Robustness]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.06361v2 Announce Type: replace 
Abstract: Self-supervised learning (SSL) has advanced significantly in visual representation learning, yet comprehensive evaluations of its adversarial robustness remain limited. In this study, we evaluate the adversarial robustness of seven discriminative self-supervised models and one supervised model across diverse tasks, including ImageNet classification, transfer learning, segmentation, and detection. Our findings suggest that discriminative SSL models generally exhibit better robustness to adversarial attacks compared to their supervised counterpart on ImageNet, with this advantage extending to transfer learning when using linear evaluation. However, when fine-tuning is applied, the robustness gap between SSL and supervised models narrows considerably. Similarly, this robustness advantage diminishes in segmentation and detection tasks. We also investigate how various factors might influence adversarial robustness, including architectural choices, training duration, data augmentations, and batch sizes. Our analysis contributes to the ongoing exploration of adversarial robustness in visual self-supervised representation systems.

## 📝 요약

이 연구는 시각적 표현 학습에서의 자기 지도 학습(SSL)의 적대적 강건성을 평가합니다. ImageNet 분류, 전이 학습, 세분화, 탐지 등 다양한 작업에서 7개의 자기 지도 모델과 1개의 지도 학습 모델을 비교했습니다. 결과적으로, SSL 모델은 ImageNet에서 지도 학습 모델보다 적대적 공격에 더 강한 것으로 나타났으며, 전이 학습에서도 이점이 있었습니다. 그러나 세분화와 탐지 작업에서는 이러한 강점이 줄어들었습니다. 또한, 모델의 구조, 학습 기간, 데이터 증강, 배치 크기 등이 강건성에 미치는 영향을 분석했습니다. 이 연구는 시각적 자기 지도 표현 시스템의 적대적 강건성 탐구에 기여합니다.

## 🎯 주요 포인트

- 1. 자기 지도 학습(SSL) 모델은 ImageNet에서의 적대적 공격에 대해 감독 학습 모델보다 일반적으로 더 높은 강건성을 보인다.
- 2. 전이 학습에서 선형 평가를 사용할 경우, SSL 모델의 강건성 우위가 유지되지만, 미세 조정을 적용하면 SSL과 감독 학습 모델 간의 강건성 차이가 상당히 줄어든다.
- 3. 세분화 및 탐지 작업에서는 SSL 모델의 강건성 이점이 감소한다.
- 4. 모델의 적대적 강건성에 영향을 미칠 수 있는 다양한 요인으로는 아키텍처 선택, 학습 기간, 데이터 증강, 배치 크기 등이 있다.
- 5. 본 연구는 시각적 자기 지도 표현 시스템에서의 적대적 강건성 탐구에 기여한다.


---

*Generated on 2025-09-26 09:23:49*