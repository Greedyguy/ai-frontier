---
keywords:
  - DragOSM
  - OpenStreetMap
  - Alignment Token
  - Gaussian Distribution
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17951
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:06:28.949586",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "DragOSM",
    "OpenStreetMap",
    "Alignment Token",
    "Gaussian Distribution"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "DragOSM": 0.8,
    "OpenStreetMap": 0.85,
    "Alignment Token": 0.78,
    "Gaussian Distribution": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "DragOSM",
        "canonical": "DragOSM",
        "aliases": [
          "Drag OpenStreetMap Labels"
        ],
        "category": "unique_technical",
        "rationale": "DragOSM is a novel model specifically designed for aligning historical labels with current aerial images, offering unique insights into geospatial data correction.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "OpenStreetMap",
        "canonical": "OpenStreetMap",
        "aliases": [
          "OSM"
        ],
        "category": "broad_technical",
        "rationale": "OpenStreetMap is a widely used open-source map database, crucial for geospatial analysis and linking historical data with current observations.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "alignment token",
        "canonical": "Alignment Token",
        "aliases": [
          "correction vector"
        ],
        "category": "unique_technical",
        "rationale": "The concept of an alignment token is central to the methodology of correcting positional discrepancies in geospatial data.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Gaussian distribution",
        "canonical": "Gaussian Distribution",
        "aliases": [
          "normal distribution"
        ],
        "category": "specific_connectable",
        "rationale": "Gaussian distribution is used in the model to simulate positional discrepancies, making it a key statistical concept for understanding the model's approach.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "segmentation-based models",
      "remote sensing images"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "DragOSM",
      "resolved_canonical": "DragOSM",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "OpenStreetMap",
      "resolved_canonical": "OpenStreetMap",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "alignment token",
      "resolved_canonical": "Alignment Token",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Gaussian distribution",
      "resolved_canonical": "Gaussian Distribution",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# DragOSM: Extract Building Roofs and Footprints from Aerial Images by Aligning Historical Labels

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17951.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17951](https://arxiv.org/abs/2509.17951)

## 🔗 유사한 논문
- [[2025-09-22/FoBa_ A Foreground-Background co-Guided Method and New Benchmark for Remote Sensing Semantic Change Detection_20250922|FoBa: A Foreground-Background co-Guided Method and New Benchmark for Remote Sensing Semantic Change Detection]] (79.3% similar)
- [[2025-09-23/Depth Edge Alignment Loss_ DEALing with Depth in Weakly Supervised Semantic Segmentation_20250923|Depth Edge Alignment Loss: DEALing with Depth in Weakly Supervised Semantic Segmentation]] (79.3% similar)
- [[2025-09-22/Semantic Change Detection of Roads and Bridges_ A Fine-grained Dataset and Multimodal Frequency-driven Detector_20250922|Semantic Change Detection of Roads and Bridges: A Fine-grained Dataset and Multimodal Frequency-driven Detector]] (79.1% similar)
- [[2025-09-23/L2M-Reg_ Building-level Uncertainty-aware Registration of Outdoor LiDAR Point Clouds and Semantic 3D City Models_20250923|L2M-Reg: Building-level Uncertainty-aware Registration of Outdoor LiDAR Point Clouds and Semantic 3D City Models]] (78.8% similar)
- [[2025-09-22/DC-Mamba_ Bi-temporal deformable alignment and scale-sparse enhancement for remote sensing change detection_20250922|DC-Mamba: Bi-temporal deformable alignment and scale-sparse enhancement for remote sensing change detection]] (78.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/OpenStreetMap|OpenStreetMap]]
**🔗 Specific Connectable**: [[keywords/Gaussian Distribution|Gaussian Distribution]]
**⚡ Unique Technical**: [[keywords/DragOSM|DragOSM]], [[keywords/Alignment Token|Alignment Token]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17951v1 Announce Type: new 
Abstract: Extracting polygonal roofs and footprints from remote sensing images is critical for large-scale urban analysis. Most existing methods rely on segmentation-based models that assume clear semantic boundaries of roofs, but these approaches struggle in off- nadir images, where the roof and footprint are significantly displaced, and facade pixels are fused with the roof boundary. With the increasing availability of open vector map annotations, e.g., OpenStreetMap, utilizing historical labels for off-nadir image annotation has become viable because remote sensing images are georeferenced once captured. However, these historical labels commonly suffer from significant positional discrepancies with new images and only have one annotation (roof or footprint), which fails to describe the correct structures of a building. To address these discrepancies, we first introduce a concept of an alignment token, which encodes the correction vector to guide the label correction. Based on this concept, we then propose Drag OpenStreetMap Labels (DragOSM), a novel model designed to align dislocated historical labels with roofs and footprints. Specifically, DragOSM formulates the label alignment as an interactive denoising process, modeling the positional discrepancy as a Gaussian distribution. During training, it learns to correct these errors by simulating misalignment with random Gaussian perturbations; during inference, it iteratively refines the positions of input labels. To validate our method, we further present a new dataset, Repairing Buildings in OSM (ReBO), comprising 179,265 buildings with both OpenStreetMap and manually corrected annotations across 5,473 images from 41 cities. Experimental results on ReBO demonstrate the effectiveness of DragOSM. Code, dataset, and trained models are publicly available at https://github.com/likaiucas/DragOSM.git.

## 📝 요약

이 논문은 원격 감지 이미지에서 건물의 지붕과 윤곽을 추출하는 새로운 방법론을 제안합니다. 기존 방법들은 지붕의 명확한 경계를 가정하지만, 비직선 이미지에서는 한계가 있습니다. 이를 해결하기 위해, 저자들은 '정렬 토큰' 개념을 도입하여 레이블의 위치 오류를 수정하는 DragOSM 모델을 제안합니다. DragOSM은 레이블 정렬을 상호작용적 잡음 제거 과정으로 모델링하며, Gaussian 분포를 통해 위치 불일치를 처리합니다. 새로운 데이터셋 ReBO를 통해 실험한 결과, DragOSM의 효과가 입증되었습니다. 코드와 데이터셋은 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 원격 감지 이미지에서 다각형 지붕과 건물 윤곽을 추출하는 것은 대규모 도시 분석에 중요하다.
- 2. 기존 방법들은 지붕의 명확한 경계를 가정하는 세그멘테이션 기반 모델에 의존하지만, 오프 나디르 이미지에서는 지붕과 건물 윤곽의 위치가 크게 어긋나고, 외벽 픽셀이 지붕 경계와 혼합되어 어려움을 겪는다.
- 3. DragOSM은 역사적 레이블을 지붕과 건물 윤곽에 정렬시키기 위해 설계된 새로운 모델로, 레이블 정렬을 상호작용적 노이즈 제거 과정으로 공식화한다.
- 4. DragOSM의 효과를 검증하기 위해 41개 도시에서 5,473개의 이미지와 함께 OpenStreetMap 및 수동으로 수정된 주석을 포함하는 ReBO 데이터셋이 제시되었다.
- 5. 실험 결과, ReBO 데이터셋에서 DragOSM의 효과가 입증되었으며, 코드, 데이터셋 및 학습된 모델은 공개적으로 제공된다.


---

*Generated on 2025-09-24 05:06:28*