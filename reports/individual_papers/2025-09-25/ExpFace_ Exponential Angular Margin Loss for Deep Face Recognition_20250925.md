---
keywords:
  - Deep Learning
  - Exponential Angular Margin Loss
  - Margin-based Softmax Losses
  - Angular Space
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19753
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:47:05.746161",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Exponential Angular Margin Loss",
    "Margin-based Softmax Losses",
    "Angular Space"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.75,
    "Exponential Angular Margin Loss": 0.8,
    "Margin-based Softmax Losses": 0.78,
    "Angular Space": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Face Recognition",
        "canonical": "Deep Learning",
        "aliases": [
          "Deep Face Recognition"
        ],
        "category": "broad_technical",
        "rationale": "Deep Face Recognition is a specific application of Deep Learning, which is a broad technical category.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      },
      {
        "surface": "Exponential Angular Margin Loss",
        "canonical": "Exponential Angular Margin Loss",
        "aliases": [
          "ExpFace"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel loss function introduced in the paper, providing a unique technical concept for linking.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Margin-based Softmax Losses",
        "canonical": "Margin-based Softmax Losses",
        "aliases": [
          "SphereFace",
          "CosFace",
          "ArcFace"
        ],
        "category": "specific_connectable",
        "rationale": "These are well-known methods in face recognition, providing strong connectivity for related research.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Angular Space",
        "canonical": "Angular Space",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Angular Space is a specific concept used in the paper to describe the distribution of samples, important for understanding the proposed method.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "state-of-the-art",
      "source code",
      "training instability"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep Face Recognition",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Exponential Angular Margin Loss",
      "resolved_canonical": "Exponential Angular Margin Loss",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Margin-based Softmax Losses",
      "resolved_canonical": "Margin-based Softmax Losses",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Angular Space",
      "resolved_canonical": "Angular Space",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# ExpFace: Exponential Angular Margin Loss for Deep Face Recognition

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19753.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19753](https://arxiv.org/abs/2509.19753)

## 🔗 유사한 논문
- [[2025-09-22/Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection_20250922|Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection]] (82.5% similar)
- [[2025-09-23/Optimized Learned Image Compression for Facial Expression Recognition_20250923|Optimized Learned Image Compression for Facial Expression Recognition]] (81.7% similar)
- [[2025-09-23/Explainable AI for Analyzing Person-Specific Patterns in Facial Recognition Tasks_20250923|Explainable AI for Analyzing Person-Specific Patterns in Facial Recognition Tasks]] (81.6% similar)
- [[2025-09-24/DevFD_ Developmental Face Forgery Detection by Learning Shared and Orthogonal LoRA Subspaces_20250924|DevFD: Developmental Face Forgery Detection by Learning Shared and Orthogonal LoRA Subspaces]] (80.3% similar)
- [[2025-09-23/SynergyNet_ Fusing Generative Priors and State-Space Models for Facial Beauty Prediction_20250923|SynergyNet: Fusing Generative Priors and State-Space Models for Facial Beauty Prediction]] (79.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Margin-based Softmax Losses|Margin-based Softmax Losses]]
**⚡ Unique Technical**: [[keywords/Exponential Angular Margin Loss|Exponential Angular Margin Loss]], [[keywords/Angular Space|Angular Space]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19753v1 Announce Type: cross 
Abstract: Face recognition is an open-set problem requiring high discriminative power to ensure that intra-class distances remain smaller than inter-class distances. Margin-based softmax losses, such as SphereFace, CosFace, and ArcFace, have been widely adopted to enhance intra-class compactness and inter-class separability, yet they overlook the impact of noisy samples. By examining the distribution of samples in the angular space, we observe that clean samples predominantly cluster in the center region, whereas noisy samples tend to shift toward the peripheral region. Motivated by this observation, we propose the Exponential Angular Margin Loss (ExpFace), which introduces an angular exponential term as the margin. This design applies a larger penalty in the center region and a smaller penalty in the peripheral region within the angular space, thereby emphasizing clean samples while suppressing noisy samples. We present a unified analysis of ExpFace and classical margin-based softmax losses in terms of margin embedding forms, similarity curves, and gradient curves, showing that ExpFace not only avoids the training instability of SphereFace and the non-monotonicity of ArcFace, but also exhibits a similarity curve that applies penalties in the same manner as the decision boundary in the angular space. Extensive experiments demonstrate that ExpFace achieves state-of-the-art performance. To facilitate future research, we have released the source code at: https://github.com/dfr-code/ExpFace.

## 📝 요약

이 논문은 얼굴 인식 문제에서 노이즈 샘플의 영향을 고려한 새로운 손실 함수인 Exponential Angular Margin Loss (ExpFace)를 제안합니다. 기존의 마진 기반 소프트맥스 손실 함수들은 노이즈 샘플을 간과했지만, ExpFace는 각도 공간에서 깨끗한 샘플과 노이즈 샘플의 분포 차이를 이용하여 중심 영역에는 더 큰 패널티를, 주변 영역에는 더 작은 패널티를 부여합니다. 이를 통해 깨끗한 샘플을 강조하고 노이즈 샘플을 억제합니다. ExpFace는 SphereFace의 훈련 불안정성과 ArcFace의 비단조성을 피하면서도 각도 공간에서의 결정 경계와 유사한 패널티를 적용합니다. 실험 결과, ExpFace는 최첨단 성능을 달성했으며, 소스 코드는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 얼굴 인식 문제에서 기존의 마진 기반 소프트맥스 손실 함수들은 노이즈 샘플의 영향을 간과하고 있다.
- 2. ExpFace는 각도 공간에서 중심 영역에 더 큰 페널티를 적용하여 깨끗한 샘플을 강조하고, 주변부 영역에서는 노이즈 샘플을 억제한다.
- 3. ExpFace는 SphereFace의 훈련 불안정성과 ArcFace의 비단조성을 피하면서, 각도 공간의 결정 경계와 유사한 방식으로 페널티를 적용한다.
- 4. ExpFace는 다양한 실험을 통해 최첨단 성능을 달성했음을 입증하였다.
- 5. 연구의 재현성을 위해 ExpFace의 소스 코드를 공개하였다.


---

*Generated on 2025-09-25 15:47:05*