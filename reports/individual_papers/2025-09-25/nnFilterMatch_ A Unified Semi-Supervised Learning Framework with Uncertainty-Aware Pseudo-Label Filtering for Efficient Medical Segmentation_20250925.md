---
keywords:
  - Semi-supervised Learning
  - Medical Image Segmentation
  - Active Learning
  - Entropy-based Pseudo-label Filtering
  - nnU-Net
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.19746
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:05:22.168160",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Semi-supervised Learning",
    "Medical Image Segmentation",
    "Active Learning",
    "Entropy-based Pseudo-label Filtering",
    "nnU-Net"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Semi-supervised Learning": 0.8,
    "Medical Image Segmentation": 0.85,
    "Active Learning": 0.82,
    "Entropy-based Pseudo-label Filtering": 0.78,
    "nnU-Net": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Semi-supervised learning",
        "canonical": "Semi-supervised Learning",
        "aliases": [
          "SSL"
        ],
        "category": "broad_technical",
        "rationale": "It is a core technique in the paper, linking to broader machine learning discussions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Medical image segmentation",
        "canonical": "Medical Image Segmentation",
        "aliases": [
          "Medical Segmentation"
        ],
        "category": "specific_connectable",
        "rationale": "This is the primary application domain of the study, connecting to specialized medical imaging topics.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      },
      {
        "surface": "Active learning",
        "canonical": "Active Learning",
        "aliases": [
          "AL"
        ],
        "category": "specific_connectable",
        "rationale": "Active Learning is crucial for reducing annotation efforts, linking to efficiency strategies in machine learning.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "Entropy-based pseudo-label filtering",
        "canonical": "Entropy-based Pseudo-label Filtering",
        "aliases": [
          "FilterMatch"
        ],
        "category": "unique_technical",
        "rationale": "This novel method is a key innovation in the paper, offering a unique approach to pseudo-labeling.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "nnU-Net",
        "canonical": "nnU-Net",
        "aliases": [
          "nnU-Net Framework"
        ],
        "category": "unique_technical",
        "rationale": "The framework is central to the study's methodology, linking to specific neural network architectures.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
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
      "candidate_surface": "Semi-supervised learning",
      "resolved_canonical": "Semi-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Medical image segmentation",
      "resolved_canonical": "Medical Image Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Active learning",
      "resolved_canonical": "Active Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Entropy-based pseudo-label filtering",
      "resolved_canonical": "Entropy-based Pseudo-label Filtering",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "nnU-Net",
      "resolved_canonical": "nnU-Net",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# nnFilterMatch: A Unified Semi-Supervised Learning Framework with Uncertainty-Aware Pseudo-Label Filtering for Efficient Medical Segmentation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19746.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.19746](https://arxiv.org/abs/2509.19746)

## 🔗 유사한 논문
- [[2025-09-22/pFedSAM_ Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation_20250922|pFedSAM: Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation]] (86.1% similar)
- [[2025-09-23/An Efficient Dual-Line Decoder Network with Multi-Scale Convolutional Attention for Multi-organ Segmentation_20250923|An Efficient Dual-Line Decoder Network with Multi-Scale Convolutional Attention for Multi-organ Segmentation]] (85.6% similar)
- [[2025-09-18/Semi-Supervised 3D Medical Segmentation from 2D Natural Images Pretrained Model_20250918|Semi-Supervised 3D Medical Segmentation from 2D Natural Images Pretrained Model]] (85.4% similar)
- [[2025-09-24/DiSSECT_ Structuring Transfer-Ready Medical Image Representations through Discrete Self-Supervision_20250924|DiSSECT: Structuring Transfer-Ready Medical Image Representations through Discrete Self-Supervision]] (84.9% similar)
- [[2025-09-25/U-Mamba2-SSL for Semi-Supervised Tooth and Pulp Segmentation in CBCT_20250925|U-Mamba2-SSL for Semi-Supervised Tooth and Pulp Segmentation in CBCT]] (83.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Semi-supervised Learning|Semi-supervised Learning]]
**🔗 Specific Connectable**: [[keywords/Medical Image Segmentation|Medical Image Segmentation]], [[keywords/Active Learning|Active Learning]]
**⚡ Unique Technical**: [[keywords/Entropy-based Pseudo-label Filtering|Entropy-based Pseudo-label Filtering]], [[keywords/nnU-Net|nnU-Net]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19746v1 Announce Type: new 
Abstract: Semi-supervised learning (SSL) has emerged as a promising paradigm in medical image segmentation, offering competitive performance while substantially reducing the need for extensive manual annotation. When combined with active learning (AL), these strategies further minimize annotation burden by selectively incorporating the most informative samples. However, conventional SSL_AL hybrid approaches often rely on iterative and loop-based retraining cycles after each annotation round, incurring significant computational overhead and limiting scalability in clinical applications. In this study, we present a novel, annotation-efficient, and self-adaptive deep segmentation framework that integrates SSL with entropy-based pseudo-label filtering (FilterMatch), an AL-inspired mechanism, within the single-pass nnU-Net training segmentation framework (nnFilterMatch). By selectively excluding high-confidence pseudo-labels during training, our method circumvents the need for retraining loops while preserving the benefits of uncertainty-guided learning. We validate the proposed framework across multiple clinical segmentation benchmarks and demonstrate that it achieves performance comparable to or exceeding fully supervised models, even with only 5\%--20\% labeled data. This work introduces a scalable, end-to-end learning strategy for reducing annotation demands in medical image segmentation without compromising accuracy. Code is available here: https://github.com/Ordi117/nnFilterMatch.git.

## 📝 요약

이 연구는 의료 영상 분할에서 주목받고 있는 반지도 학습(SSL)과 능동 학습(AL)을 결합한 새로운 프레임워크를 제안합니다. 기존의 SSL_AL 접근법은 반복적인 재학습이 필요하여 계산 비용이 높았으나, 본 연구에서는 nnU-Net 기반의 단일 패스 학습을 통해 이러한 문제를 해결합니다. 제안된 nnFilterMatch는 엔트로피 기반의 의사 라벨 필터링을 활용하여 고신뢰도의 의사 라벨을 선택적으로 제외함으로써 재학습의 필요성을 없앴습니다. 다양한 임상 분할 벤치마크에서 검증한 결과, 5%에서 20%의 라벨 데이터만으로도 완전 지도 학습 모델과 동등하거나 더 나은 성능을 보였습니다. 이 연구는 의료 영상 분할에서 주석 부담을 줄이면서도 정확성을 유지하는 확장 가능한 학습 전략을 제시합니다.

## 🎯 주요 포인트

- 1. 본 연구는 의료 영상 분할에서 반지도 학습(SSL)과 능동 학습(AL)을 결합하여 주석 부담을 줄이는 새로운 프레임워크를 제안합니다.
- 2. 제안된 프레임워크는 nnU-Net 훈련 프레임워크 내에서 엔트로피 기반의 가짜 레이블 필터링 메커니즘을 통합하여 반복적인 재훈련 루프 없이 학습을 진행합니다.
- 3. nnFilterMatch는 높은 신뢰도의 가짜 레이블을 선택적으로 제외함으로써 불확실성 기반 학습의 이점을 유지하면서도 주석 효율성을 높입니다.
- 4. 여러 임상 분할 벤치마크에서 제안된 프레임워크를 검증한 결과, 5%--20%의 라벨링 데이터만으로도 완전 지도 학습 모델과 동등하거나 더 나은 성능을 달성했습니다.
- 5. 이 연구는 의료 영상 분할에서 주석 요구를 줄이면서도 정확성을 유지하는 확장 가능한 종단 간 학습 전략을 소개합니다.


---

*Generated on 2025-09-26 09:05:22*