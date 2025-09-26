---
keywords:
  - Symmetry Discovery
  - Canonical Orientation Normalization
  - Group Invariance
  - Out-of-Distribution Detection
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2505.13289
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:43:54.028740",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Symmetry Discovery",
    "Canonical Orientation Normalization",
    "Group Invariance",
    "Out-of-Distribution Detection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Symmetry Discovery": 0.85,
    "Canonical Orientation Normalization": 0.9,
    "Group Invariance": 0.8,
    "Out-of-Distribution Detection": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "symmetry discovery",
        "canonical": "Symmetry Discovery",
        "aliases": [
          "symmetry detection"
        ],
        "category": "unique_technical",
        "rationale": "Symmetry discovery is central to the paper's contribution and links to advanced geometric analysis.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "canonical orientation normalization",
        "canonical": "Canonical Orientation Normalization",
        "aliases": [
          "orientation normalization"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel technique introduced in the paper, crucial for understanding the proposed method.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.9
      },
      {
        "surface": "group invariance",
        "canonical": "Group Invariance",
        "aliases": [
          "invariance to groups"
        ],
        "category": "specific_connectable",
        "rationale": "Group invariance is a key concept in machine learning, relevant to model robustness.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "out-of-distribution poses",
        "canonical": "Out-of-Distribution Detection",
        "aliases": [
          "OOD poses"
        ],
        "category": "specific_connectable",
        "rationale": "Detecting out-of-distribution poses is critical for model generalization and robustness.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "real world data",
      "test-time canonicalization"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "symmetry discovery",
      "resolved_canonical": "Symmetry Discovery",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "canonical orientation normalization",
      "resolved_canonical": "Canonical Orientation Normalization",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "group invariance",
      "resolved_canonical": "Group Invariance",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "out-of-distribution poses",
      "resolved_canonical": "Out-of-Distribution Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# RECON: Robust symmetry discovery via Explicit Canonical Orientation Normalization

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2505.13289.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2505.13289](https://arxiv.org/abs/2505.13289)

## 🔗 유사한 논문
- [[2025-09-22/Two Is Better Than One_ Aligned Representation Pairs for Anomaly Detection_20250922|Two Is Better Than One: Aligned Representation Pairs for Anomaly Detection]] (83.6% similar)
- [[2025-09-17/Consistent View Alignment Improves Foundation Models for 3D Medical Image Segmentation_20250917|Consistent View Alignment Improves Foundation Models for 3D Medical Image Segmentation]] (81.1% similar)
- [[2025-09-19/Seeing 3D Through 2D Lenses_ 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification_20250919|Seeing 3D Through 2D Lenses: 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (80.6% similar)
- [[2025-09-19/Reconstruction Alignment Improves Unified Multimodal Models_20250919|Reconstruction Alignment Improves Unified Multimodal Models]] (79.8% similar)
- [[2025-09-23/$\boldsymbol{\lambda}$-Orthogonality Regularization for Compatible Representation Learning_20250923|$\boldsymbol{\lambda}$-Orthogonality Regularization for Compatible Representation Learning]] (79.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Group Invariance|Group Invariance]], [[keywords/Out-of-Distribution Detection|Out-of-Distribution Detection]]
**⚡ Unique Technical**: [[keywords/Symmetry Discovery|Symmetry Discovery]], [[keywords/Canonical Orientation Normalization|Canonical Orientation Normalization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.13289v2 Announce Type: replace 
Abstract: Real world data often exhibits unknown, instance-specific symmetries that rarely exactly match a transformation group $G$ fixed a priori. Class-pose decompositions aim to create disentangled representations by factoring inputs into invariant features and a pose $g\in G$ defined relative to a training-dependent, arbitrary canonical representation. We introduce RECON, a class-pose agnostic $\textit{canonical orientation normalization}$ that corrects arbitrary canonicals via a simple right-multiplication, yielding $\textit{natural}$, data-aligned canonicalizations. This enables (i) unsupervised discovery of instance-specific symmetry distributions, (ii) detection of out-of-distribution poses, and (iii) test-time canonicalization, granting group invariance to pre-trained models without retraining and irrespective of model architecture, improving downstream performance. We demonstrate results on 2D image benchmarks and --for the first time-- extend symmetry discovery to 3D groups.

## 📝 요약

이 논문은 데이터의 인스턴스별 대칭성을 효과적으로 처리하기 위한 새로운 방법론인 RECON을 제안합니다. RECON은 클래스-포즈 무관한 정규화 기법으로, 데이터에 맞춘 자연스러운 정규화를 통해 인스턴스별 대칭 분포를 비지도 학습으로 발견하고, 분포 외 포즈를 감지하며, 테스트 시 정규화를 통해 사전 학습된 모델에 군 불변성을 부여합니다. 이를 통해 모델 재학습 없이도 성능을 향상시킬 수 있습니다. 2D 이미지 벤치마크에서의 성능을 입증했으며, 3D 그룹으로 대칭성 발견을 확장한 최초의 사례를 제시합니다.

## 🎯 주요 포인트

- 1. RECON은 임의의 정규화된 표준을 간단한 우측 곱셈으로 수정하여 자연스럽고 데이터에 맞춘 표준화를 제공합니다.
- 2. RECON을 통해 인스턴스별 대칭 분포를 비지도 학습으로 발견할 수 있습니다.
- 3. RECON은 분포 외의 포즈를 감지하고, 테스트 시 표준화를 통해 사전 학습된 모델에 그룹 불변성을 부여합니다.
- 4. RECON은 모델 아키텍처와 상관없이 재학습 없이도 다운스트림 성능을 향상시킵니다.
- 5. 2D 이미지 벤치마크에서의 결과를 시연하고, 처음으로 3D 그룹에 대칭 발견을 확장했습니다.


---

*Generated on 2025-09-24 02:43:54*