---
keywords:
  - Deep Learning
  - Segmentation-driven Registration
  - Anatomically Adaptive Regularization
  - Image Registration
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15784
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:12:53.376757",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Segmentation-driven Registration",
    "Anatomically Adaptive Regularization",
    "Image Registration"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Segmentation-driven Registration": 0.8,
    "Anatomically Adaptive Regularization": 0.78,
    "Image Registration": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Deep Learning is a fundamental technique used in the proposed framework, connecting it to a wide range of related research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "Segmentation-driven Registration",
        "canonical": "Segmentation-driven Registration",
        "aliases": [
          "SegReg"
        ],
        "category": "unique_technical",
        "rationale": "This is the core innovation of the paper, transforming registration into a segmentation problem, which is a novel approach.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Anatomically Adaptive Regularization",
        "canonical": "Anatomically Adaptive Regularization",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This technique addresses the limitation of uniform smoothness constraints, offering a novel solution for anatomical motion.",
        "novelty_score": 0.75,
        "connectivity_score": 0.55,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Image Registration",
        "canonical": "Image Registration",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Image Registration is a key process in the framework, linking it to extensive research in medical imaging.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "method",
      "approach",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Segmentation-driven Registration",
      "resolved_canonical": "Segmentation-driven Registration",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Anatomically Adaptive Regularization",
      "resolved_canonical": "Anatomically Adaptive Regularization",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.55,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Image Registration",
      "resolved_canonical": "Image Registration",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Ideal Registration? Segmentation is All You Need

**Korean Title:** 이상적인 정합? 세분화가 전부입니다.

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15784.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15784](https://arxiv.org/abs/2509.15784)

## 🔗 유사한 논문
- [[2025-09-22/Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images_20250922|Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images]] (82.1% similar)
- [[2025-09-22/UniMRSeg_ Unified Modality-Relax Segmentation via Hierarchical Self-Supervised Compensation_20250922|UniMRSeg: Unified Modality-Relax Segmentation via Hierarchical Self-Supervised Compensation]] (82.1% similar)
- [[2025-09-22/pFedSAM_ Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation_20250922|pFedSAM: Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation]] (81.9% similar)
- [[2025-09-22/Domain-invariant feature learning in brain MR imaging for content-based image retrieval_20250922|Domain-invariant feature learning in brain MR imaging for content-based image retrieval]] (80.7% similar)
- [[2025-09-22/ENSAM_ an efficient foundation model for interactive segmentation of 3D medical images_20250922|ENSAM: an efficient foundation model for interactive segmentation of 3D medical images]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Image Registration|Image Registration]]
**⚡ Unique Technical**: [[keywords/Segmentation-driven Registration|Segmentation-driven Registration]], [[keywords/Anatomically Adaptive Regularization|Anatomically Adaptive Regularization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15784v1 Announce Type: cross 
Abstract: Deep learning has revolutionized image registration by its ability to handle diverse tasks while achieving significant speed advantages over conventional approaches. Current approaches, however, often employ globally uniform smoothness constraints that fail to accommodate the complex, regionally varying deformations characteristic of anatomical motion. To address this limitation, we propose SegReg, a Segmentation-driven Registration framework that implements anatomically adaptive regularization by exploiting region-specific deformation patterns. Our SegReg first decomposes input moving and fixed images into anatomically coherent subregions through segmentation. These localized domains are then processed by the same registration backbone to compute optimized partial deformation fields, which are subsequently integrated into a global deformation field. SegReg achieves near-perfect structural alignment (98.23% Dice on critical anatomies) using ground-truth segmentation, and outperforms existing methods by 2-12% across three clinical registration scenarios (cardiac, abdominal, and lung images) even with automatic segmentation. Our SegReg demonstrates a near-linear dependence of registration accuracy on segmentation quality, transforming the registration challenge into a segmentation problem. The source code will be released upon manuscript acceptance.

## 🔍 Abstract (한글 번역)

arXiv:2509.15784v1 발표 유형: 교차  
초록: 딥러닝은 다양한 작업을 처리할 수 있는 능력과 기존 방법에 비해 상당한 속도 이점을 제공함으로써 이미지 정합을 혁신적으로 변화시켰습니다. 그러나 현재의 접근 방식은 종종 해부학적 운동의 복잡하고 지역적으로 다양한 변형을 수용하지 못하는 전역적으로 균일한 매끄러움 제약을 사용합니다. 이러한 한계를 해결하기 위해, 우리는 영역별 변형 패턴을 활용하여 해부학적으로 적응적인 정규화를 구현하는 세그먼테이션 기반 정합 프레임워크인 SegReg를 제안합니다. SegReg는 먼저 입력 이동 이미지와 고정 이미지를 세그먼테이션을 통해 해부학적으로 일관된 하위 영역으로 분해합니다. 이러한 지역화된 도메인은 동일한 정합 백본에 의해 처리되어 최적화된 부분 변형 필드를 계산하며, 이는 이후 전역 변형 필드로 통합됩니다. SegReg는 실제 세그먼테이션을 사용하여 거의 완벽한 구조적 정렬(중요 해부학에서 98.23% Dice)을 달성하며, 자동 세그먼테이션을 사용하더라도 세 가지 임상 정합 시나리오(심장, 복부, 폐 이미지)에서 기존 방법보다 2-12% 더 우수한 성능을 보입니다. 우리의 SegReg는 정합 정확도가 세그먼테이션 품질에 거의 선형적으로 의존함을 보여주며, 정합 문제를 세그먼테이션 문제로 변환합니다. 소스 코드는 원고가 승인되면 공개될 예정입니다.

## 📝 요약

이 논문에서는 이미지 등록 분야에서 심층 학습의 한계를 극복하기 위해 SegReg라는 새로운 프레임워크를 제안합니다. 기존 방법들은 전역적으로 균일한 매끄러움 제약을 사용하여 해부학적 움직임의 복잡한 변형을 제대로 반영하지 못하는 문제를 가지고 있습니다. SegReg는 해부학적으로 적응적인 정규화를 통해 이러한 문제를 해결합니다. 이 방법은 입력 이미지를 해부학적으로 일관된 하위 영역으로 분할한 후, 각 영역에 대해 최적화된 변형 필드를 계산하여 전체 변형 필드를 생성합니다. SegReg는 구조적 정렬에서 98.23%의 높은 정확도를 달성하며, 자동 분할을 사용해도 기존 방법보다 2-12% 향상된 성능을 보입니다. 등록 정확도가 분할 품질에 거의 선형적으로 의존함을 보여주며, 등록 문제를 분할 문제로 전환합니다. 코드 공개는 논문 승인 후 이루어질 예정입니다.

## 🎯 주요 포인트

- 1. SegReg는 해부학적으로 적응적인 정규화를 구현하여 복잡하고 지역적으로 다양한 변형을 처리합니다.
- 2. SegReg는 입력 이미지를 해부학적으로 일관된 하위 영역으로 분할하여 부분 변형 필드를 최적화합니다.
- 3. SegReg는 주요 해부학에서 98.23%의 Dice 점수를 기록하며 기존 방법보다 2-12% 더 높은 성능을 보입니다.
- 4. SegReg는 등록 정확도가 분할 품질에 거의 선형적으로 의존함을 보여주며, 등록 문제를 분할 문제로 전환합니다.


---

*Generated on 2025-09-23 09:12:53*