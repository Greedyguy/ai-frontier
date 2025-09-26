---
keywords:
  - Visual Foundation Models
  - Range-view Segmentation
  - SemanticKITTI
  - Zero-Shot Learning
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15886
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:13:56.694126",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Visual Foundation Models",
    "Range-view Segmentation",
    "SemanticKITTI",
    "Zero-Shot Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Visual Foundation Models": 0.78,
    "Range-view Segmentation": 0.7,
    "SemanticKITTI": 0.75,
    "Zero-Shot Learning": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Visual Foundation Models",
        "canonical": "Visual Foundation Models",
        "aliases": [
          "VFMs"
        ],
        "category": "unique_technical",
        "rationale": "VFMs are central to the paper's approach and represent a novel application in LiDAR segmentation.",
        "novelty_score": 0.85,
        "connectivity_score": 0.72,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Range-view segmentation",
        "canonical": "Range-view Segmentation",
        "aliases": [
          "Range-view LiDAR Segmentation"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific method explored in the paper, linking LiDAR data with segmentation techniques.",
        "novelty_score": 0.78,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.7
      },
      {
        "surface": "SemanticKITTI",
        "canonical": "SemanticKITTI",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "SemanticKITTI is a benchmark dataset mentioned in the paper, crucial for evaluating segmentation methods.",
        "novelty_score": 0.45,
        "connectivity_score": 0.8,
        "specificity_score": 0.9,
        "link_intent_score": 0.75
      },
      {
        "surface": "Zero-shot recognition",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-shot recognition"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-shot capabilities are relevant to the paper's exploration of VFMs and their applications.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
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
      "candidate_surface": "Visual Foundation Models",
      "resolved_canonical": "Visual Foundation Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.72,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Range-view segmentation",
      "resolved_canonical": "Range-view Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "SemanticKITTI",
      "resolved_canonical": "SemanticKITTI",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.8,
        "specificity": 0.9,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Zero-shot recognition",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# RangeSAM: Leveraging Visual Foundation Models for Range-View repesented LiDAR segmentation

**Korean Title:** RangeSAM: 시각적 기초 모델을 활용한 범위 뷰 기반 LiDAR 세분화

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15886.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15886](https://arxiv.org/abs/2509.15886)

## 🔗 유사한 논문
- [[2025-09-22/TASAM_ Terrain-and-Aware Segment Anything Model for Temporal-Scale Remote Sensing Segmentation_20250922|TASAM: Terrain-and-Aware Segment Anything Model for Temporal-Scale Remote Sensing Segmentation]] (82.5% similar)
- [[2025-09-22/FloorSAM_ SAM-Guided Floorplan Reconstruction with Semantic-Geometric Fusion_20250922|FloorSAM: SAM-Guided Floorplan Reconstruction with Semantic-Geometric Fusion]] (82.2% similar)
- [[2025-09-22/pFedSAM_ Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation_20250922|pFedSAM: Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation]] (81.9% similar)
- [[2025-09-22/Enhancing Sa2VA for Referent Video Object Segmentation_ 2nd Solution for 7th LSVOS RVOS Track_20250922|Enhancing Sa2VA for Referent Video Object Segmentation: 2nd Solution for 7th LSVOS RVOS Track]] (81.7% similar)
- [[2025-09-22/Spatial Understanding from Videos_ Structured Prompts Meet Simulation Data_20250922|Spatial Understanding from Videos: Structured Prompts Meet Simulation Data]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/SemanticKITTI|SemanticKITTI]], [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Visual Foundation Models|Visual Foundation Models]], [[keywords/Range-view Segmentation|Range-view Segmentation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15886v1 Announce Type: new 
Abstract: Point cloud segmentation is central to autonomous driving and 3D scene understanding. While voxel- and point-based methods dominate recent research due to their compatibility with deep architectures and ability to capture fine-grained geometry, they often incur high computational cost, irregular memory access, and limited real-time efficiency. In contrast, range-view methods, though relatively underexplored - can leverage mature 2D semantic segmentation techniques for fast and accurate predictions. Motivated by the rapid progress in Visual Foundation Models (VFMs) for captioning, zero-shot recognition, and multimodal tasks, we investigate whether SAM2, the current state-of-the-art VFM for segmentation tasks, can serve as a strong backbone for LiDAR point cloud segmentation in the range view. We present , to our knowledge, the first range-view framework that adapts SAM2 to 3D segmentation, coupling efficient 2D feature extraction with standard projection/back-projection to operate on point clouds. To optimize SAM2 for range-view representations, we implement several architectural modifications to the encoder: (1) a novel module that emphasizes horizontal spatial dependencies inherent in LiDAR range images, (2) a customized configuration of tailored to the geometric properties of spherical projections, and (3) an adapted mechanism in the encoder backbone specifically designed to capture the unique spatial patterns and discontinuities present in range-view pseudo-images. Our approach achieves competitive performance on SemanticKITTI while benefiting from the speed, scalability, and deployment simplicity of 2D-centric pipelines. This work highlights the viability of VFMs as general-purpose backbones for 3D perception and opens a path toward unified, foundation-model-driven LiDAR segmentation. Results lets us conclude that range-view segmentation methods using VFMs leads to promising results.

## 🔍 Abstract (한글 번역)

arXiv:2509.15886v1 발표 유형: 신규  
초록: 포인트 클라우드 분할은 자율 주행 및 3D 장면 이해에 있어 핵심적입니다. 최근 연구에서는 딥 아키텍처와의 호환성 및 세밀한 기하학적 구조를 포착할 수 있는 능력 덕분에 복셀 및 포인트 기반 방법이 주를 이루고 있지만, 이들은 종종 높은 계산 비용, 불규칙한 메모리 접근, 제한된 실시간 효율성을 초래합니다. 반면, 상대적으로 덜 탐구된 범위-뷰 방법은 성숙한 2D 의미 분할 기술을 활용하여 빠르고 정확한 예측을 가능하게 합니다. 캡션 작성, 제로샷 인식, 멀티모달 작업을 위한 비주얼 파운데이션 모델(VFM)의 급속한 발전에 힘입어, 우리는 현재 분할 작업을 위한 최첨단 VFM인 SAM2가 범위 뷰에서 LiDAR 포인트 클라우드 분할을 위한 강력한 백본 역할을 할 수 있는지를 조사합니다. 우리는 SAM2를 3D 분할에 적응시키는 최초의 범위-뷰 프레임워크를 제시하며, 효율적인 2D 특징 추출을 표준 투영/역투영과 결합하여 포인트 클라우드에서 작동합니다. SAM2를 범위-뷰 표현에 최적화하기 위해 인코더에 몇 가지 구조적 수정을 구현합니다: (1) LiDAR 범위 이미지에 내재된 수평 공간 종속성을 강조하는 새로운 모듈, (2) 구형 투영의 기하학적 특성에 맞춘 맞춤형 구성, (3) 범위-뷰 의사 이미지에 존재하는 독특한 공간 패턴과 불연속성을 포착하도록 설계된 인코더 백본의 적응된 메커니즘. 우리의 접근법은 SemanticKITTI에서 경쟁력 있는 성능을 달성하면서 2D 중심 파이프라인의 속도, 확장성, 배포의 단순성의 이점을 누립니다. 이 연구는 3D 인식을 위한 범용 백본으로서의 VFM의 가능성을 강조하며, 통합된 파운데이션 모델 기반 LiDAR 분할로의 길을 엽니다. 결과적으로 VFM을 사용하는 범위-뷰 분할 방법이 유망한 결과를 초래한다는 결론을 내릴 수 있습니다.

## 📝 요약

이 논문은 자율주행과 3D 장면 이해에서 중요한 포인트 클라우드 분할을 다룹니다. 기존의 복셀 및 포인트 기반 방법은 세밀한 기하학적 정보를 포착할 수 있지만, 높은 계산 비용과 실시간 효율성의 한계가 있습니다. 이에 비해, 범위 뷰 방법은 2D 의미 분할 기술을 활용하여 빠르고 정확한 예측이 가능합니다. 본 연구는 최신 시각적 기초 모델(VFM)인 SAM2를 LiDAR 포인트 클라우드 분할에 적용하여, 효율적인 2D 특징 추출과 표준 투영/역투영을 결합한 최초의 범위 뷰 프레임워크를 제안합니다. SAM2를 범위 뷰 표현에 최적화하기 위해, 인코더에 수평 공간 의존성을 강조하는 모듈, 구형 투영의 기하학적 특성에 맞춘 설정, 범위 뷰 이미지의 독특한 공간 패턴을 포착하는 메커니즘을 도입했습니다. 이 접근법은 SemanticKITTI에서 경쟁력 있는 성능을 보이며, 2D 중심 파이프라인의 속도와 확장성, 배포의 간편함을 제공합니다. 연구 결과, VFM을 활용한 범위 뷰 분할 방법이 유망한 결과를 초래함을 확인했습니다.

## 🎯 주요 포인트

- 1. 포인트 클라우드 세분화는 자율 주행과 3D 장면 이해에 중요하지만, 기존 방법들은 높은 계산 비용과 실시간 효율성의 한계를 가집니다.
- 2. 범위 뷰 방법은 2D 의미론적 세분화 기술을 활용하여 빠르고 정확한 예측을 가능하게 합니다.
- 3. SAM2를 3D 세분화에 적응시킨 최초의 범위 뷰 프레임워크를 제시하며, 효율적인 2D 특징 추출과 표준 투영/역투영을 결합하여 포인트 클라우드에 적용합니다.
- 4. LiDAR 범위 이미지의 수평 공간 의존성을 강조하는 모듈 등 몇 가지 구조적 수정이 SAM2의 인코더에 구현되었습니다.
- 5. VFMs를 사용한 범위 뷰 세분화 방법은 유망한 결과를 보여주며, 3D 인식을 위한 범용 백본으로서의 가능성을 강조합니다.


---

*Generated on 2025-09-23 12:13:56*