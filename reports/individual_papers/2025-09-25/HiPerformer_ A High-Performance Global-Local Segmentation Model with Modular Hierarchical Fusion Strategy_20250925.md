---
keywords:
  - Transformer
  - Local-Global Feature Fusion
  - Progressive Pyramid Aggregation
  - Computer Vision
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.20280
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:15:39.624802",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Local-Global Feature Fusion",
    "Progressive Pyramid Aggregation",
    "Computer Vision"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Local-Global Feature Fusion": 0.78,
    "Progressive Pyramid Aggregation": 0.8,
    "Computer Vision": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "CNN-Transformer hybrid architectures",
        "canonical": "Transformer",
        "aliases": [
          "CNN-Transformer",
          "Hybrid Transformer"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a key component in the hybrid architecture, linking to broader technical discussions in neural network design.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Local-Global Feature Fusion",
        "canonical": "Local-Global Feature Fusion",
        "aliases": [
          "LGFF"
        ],
        "category": "unique_technical",
        "rationale": "This module is a novel approach to feature integration, offering a unique perspective in segmentation models.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Progressive Pyramid Aggregation",
        "canonical": "Progressive Pyramid Aggregation",
        "aliases": [
          "PPA"
        ],
        "category": "unique_technical",
        "rationale": "PPA is a distinctive method proposed to enhance feature representation, providing a new angle on multi-scale processing.",
        "novelty_score": 0.78,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "medical image segmentation",
        "canonical": "Computer Vision",
        "aliases": [
          "medical segmentation"
        ],
        "category": "broad_technical",
        "rationale": "Medical image segmentation is a specific application within computer vision, linking to a broad technical field.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "accuracy",
      "robustness"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "CNN-Transformer hybrid architectures",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Local-Global Feature Fusion",
      "resolved_canonical": "Local-Global Feature Fusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Progressive Pyramid Aggregation",
      "resolved_canonical": "Progressive Pyramid Aggregation",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "medical image segmentation",
      "resolved_canonical": "Computer Vision",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# HiPerformer: A High-Performance Global-Local Segmentation Model with Modular Hierarchical Fusion Strategy

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20280.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.20280](https://arxiv.org/abs/2509.20280)

## 🔗 유사한 논문
- [[2025-09-22/pFedSAM_ Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation_20250922|pFedSAM: Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation]] (83.0% similar)
- [[2025-09-23/DCFFSNet_ Deep Connectivity Feature Fusion Separation Network for Medical Image Segmentation_20250923|DCFFSNet: Deep Connectivity Feature Fusion Separation Network for Medical Image Segmentation]] (82.7% similar)
- [[2025-09-22/UniMRSeg_ Unified Modality-Relax Segmentation via Hierarchical Self-Supervised Compensation_20250922|UniMRSeg: Unified Modality-Relax Segmentation via Hierarchical Self-Supervised Compensation]] (81.9% similar)
- [[2025-09-23/A Semantic Segmentation Algorithm for Pleural Effusion Based on DBIF-AUNet_20250923|A Semantic Segmentation Algorithm for Pleural Effusion Based on DBIF-AUNet]] (81.8% similar)
- [[2025-09-23/3D Cell Oversegmentation Correction via Geo-Wasserstein Divergence_20250923|3D Cell Oversegmentation Correction via Geo-Wasserstein Divergence]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]], [[keywords/Computer Vision|Computer Vision]]
**⚡ Unique Technical**: [[keywords/Local-Global Feature Fusion|Local-Global Feature Fusion]], [[keywords/Progressive Pyramid Aggregation|Progressive Pyramid Aggregation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20280v1 Announce Type: new 
Abstract: Both local details and global context are crucial in medical image segmentation, and effectively integrating them is essential for achieving high accuracy. However, existing mainstream methods based on CNN-Transformer hybrid architectures typically employ simple feature fusion techniques such as serial stacking, endpoint concatenation, or pointwise addition, which struggle to address the inconsistencies between features and are prone to information conflict and loss. To address the aforementioned challenges, we innovatively propose HiPerformer. The encoder of HiPerformer employs a novel modular hierarchical architecture that dynamically fuses multi-source features in parallel, enabling layer-wise deep integration of heterogeneous information. The modular hierarchical design not only retains the independent modeling capability of each branch in the encoder, but also ensures sufficient information transfer between layers, effectively avoiding the degradation of features and information loss that come with traditional stacking methods. Furthermore, we design a Local-Global Feature Fusion (LGFF) module to achieve precise and efficient integration of local details and global semantic information, effectively alleviating the feature inconsistency problem and resulting in a more comprehensive feature representation. To further enhance multi-scale feature representation capabilities and suppress noise interference, we also propose a Progressive Pyramid Aggregation (PPA) module to replace traditional skip connections. Experiments on eleven public datasets demonstrate that the proposed method outperforms existing segmentation techniques, demonstrating higher segmentation accuracy and robustness. The code is available at https://github.com/xzphappy/HiPerformer.

## 📝 요약

HiPerformer는 의료 영상 분할에서 지역적 세부사항과 전역적 맥락을 효과적으로 통합하기 위해 제안된 새로운 방법론입니다. 기존 CNN-Transformer 혼합 아키텍처의 단순한 특징 융합 기법의 한계를 극복하기 위해, HiPerformer는 모듈형 계층적 아키텍처를 사용하여 다양한 출처의 특징을 병렬로 융합하고, 계층별로 이질적인 정보를 깊이 있게 통합합니다. 또한, Local-Global Feature Fusion (LGFF) 모듈을 통해 지역적 세부사항과 전역적 의미 정보를 정밀하게 통합하며, Progressive Pyramid Aggregation (PPA) 모듈을 도입하여 다중 스케일 특징 표현을 강화하고 잡음 간섭을 억제합니다. 실험 결과, HiPerformer는 기존 분할 기법보다 높은 정확성과 강건성을 보였습니다.

## 🎯 주요 포인트

- 1. HiPerformer는 의료 이미지 분할에서 지역적 세부 사항과 전역적 문맥을 효과적으로 통합하기 위해 설계된 혁신적인 모듈형 계층적 아키텍처를 제안합니다.
- 2. HiPerformer의 인코더는 병렬로 다중 소스 특징을 동적으로 융합하여 이질적인 정보를 계층적으로 깊이 통합합니다.
- 3. Local-Global Feature Fusion (LGFF) 모듈을 통해 지역적 세부 사항과 전역적 의미 정보를 정밀하고 효율적으로 통합하여 특징 불일치 문제를 완화합니다.
- 4. Progressive Pyramid Aggregation (PPA) 모듈을 도입하여 전통적인 스킵 연결을 대체하고, 다중 스케일 특징 표현 능력을 강화하며 노이즈 간섭을 억제합니다.
- 5. 열한 개의 공개 데이터셋 실험 결과, 제안된 방법이 기존 분할 기술보다 높은 정확성과 강인성을 보입니다.


---

*Generated on 2025-09-26 09:15:39*