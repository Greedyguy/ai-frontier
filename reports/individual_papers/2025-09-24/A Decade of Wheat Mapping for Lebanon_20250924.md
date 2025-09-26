<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:28:27.706319",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision Transformer",
    "Parameter-Efficient Fine Tuning",
    "Fields of The World",
    "Crop Rotation Analysis"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision Transformer": 0.82,
    "Parameter-Efficient Fine Tuning": 0.78,
    "Fields of The World": 0.75,
    "Crop Rotation Analysis": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Temporal Spatial Vision Transformer",
        "canonical": "Vision Transformer",
        "aliases": [
          "TSViT"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to advancements in transformer-based models for computer vision tasks.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Parameter-Efficient Fine Tuning",
        "canonical": "Parameter-Efficient Fine Tuning",
        "aliases": [
          "PEFT"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel approach in model optimization, enhancing connectivity to fine-tuning techniques.",
        "novelty_score": 0.72,
        "connectivity_score": 0.68,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Fields of The World framework",
        "canonical": "Fields of The World",
        "aliases": [
          "FTW framework"
        ],
        "category": "unique_technical",
        "rationale": "A specific framework that supports the paper’s methodology, enhancing connectivity to agricultural mapping studies.",
        "novelty_score": 0.7,
        "connectivity_score": 0.7,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      },
      {
        "surface": "crop rotation pattern",
        "canonical": "Crop Rotation Analysis",
        "aliases": [
          "crop rotation"
        ],
        "category": "specific_connectable",
        "rationale": "Links to agricultural practices and their analysis, relevant for historical trend studies.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.76,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "wheat mapping",
      "food security",
      "satellite images"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Temporal Spatial Vision Transformer",
      "resolved_canonical": "Vision Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Parameter-Efficient Fine Tuning",
      "resolved_canonical": "Parameter-Efficient Fine Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.68,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Fields of The World framework",
      "resolved_canonical": "Fields of The World",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.7,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "crop rotation pattern",
      "resolved_canonical": "Crop Rotation Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.76,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# A Decade of Wheat Mapping for Lebanon

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2504.11366.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2504.11366](https://arxiv.org/abs/2504.11366)

## 🔗 유사한 논문
- [[2025-09-22/A multi-temporal multi-spectral attention-augmented deep convolution neural network with contrastive learning for crop yield prediction_20250922|A multi-temporal multi-spectral attention-augmented deep convolution neural network with contrastive learning for crop yield prediction]] (80.1% similar)
- [[2025-09-24/Enabling Plant Phenotyping in Weedy Environments using Multi-Modal Imagery via Synthetic and Generated Training Data_20250924|Enabling Plant Phenotyping in Weedy Environments using Multi-Modal Imagery via Synthetic and Generated Training Data]] (79.4% similar)
- [[2025-09-24/Lightweight Vision Transformer with Window and Spatial Attention for Food Image Classification_20250924|Lightweight Vision Transformer with Window and Spatial Attention for Food Image Classification]] (78.4% similar)
- [[2025-09-24/Semantic-Aware Particle Filter for Reliable Vineyard Robot Localisation_20250924|Semantic-Aware Particle Filter for Reliable Vineyard Robot Localisation]] (77.8% similar)
- [[2025-09-24/SPADE_ A Large Language Model Framework for Soil Moisture Pattern Recognition and Anomaly Detection in Precision Agriculture_20250924|SPADE: A Large Language Model Framework for Soil Moisture Pattern Recognition and Anomaly Detection in Precision Agriculture]] (77.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Vision Transformer|Vision Transformer]], [[keywords/Crop Rotation Analysis|Crop Rotation Analysis]]
**⚡ Unique Technical**: [[keywords/Parameter-Efficient Fine Tuning|Parameter-Efficient Fine Tuning]], [[keywords/Fields of The World|Fields of The World]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.11366v4 Announce Type: replace 
Abstract: Wheat accounts for approximately 20% of the world's caloric intake, making it a vital component of global food security. Given this importance, mapping wheat fields plays a crucial role in enabling various stakeholders, including policy makers, researchers, and agricultural organizations, to make informed decisions regarding food security, supply chain management, and resource allocation. In this paper, we tackle the problem of accurately mapping wheat fields out of satellite images by introducing an improved pipeline for winter wheat segmentation, as well as presenting a case study on a decade-long analysis of wheat mapping in Lebanon. We integrate a Temporal Spatial Vision Transformer (TSViT) with Parameter-Efficient Fine Tuning (PEFT) and a novel post-processing pipeline based on the Fields of The World (FTW) framework. Our proposed pipeline addresses key challenges encountered in existing approaches, such as the clustering of small agricultural parcels in a single large field. By merging wheat segmentation with precise field boundary extraction, our method produces geometrically coherent and semantically rich maps that enable us to perform in-depth analysis such as tracking crop rotation pattern over years. Extensive evaluations demonstrate improved boundary delineation and field-level precision, establishing the potential of the proposed framework in operational agricultural monitoring and historical trend analysis. By allowing for accurate mapping of wheat fields, this work lays the foundation for a range of critical studies and future advances, including crop monitoring and yield estimation.

## 📝 요약

이 논문은 전 세계 칼로리 섭취의 약 20%를 차지하는 밀의 중요성을 강조하며, 위성 이미지를 활용한 밀밭의 정확한 지도를 작성하는 방법을 제안합니다. 연구에서는 겨울 밀 세분화를 위한 개선된 파이프라인을 소개하고, 레바논에서 10년간의 밀 지도 분석 사례를 제시합니다. Temporal Spatial Vision Transformer (TSViT)와 Parameter-Efficient Fine Tuning (PEFT)을 통합하고, Fields of The World (FTW) 프레임워크 기반의 새로운 후처리 파이프라인을 도입하여 기존 방법의 문제점을 해결합니다. 특히 작은 농업 구획의 대규모 필드 내 클러스터링 문제를 해결하여, 기하학적으로 일관되고 의미적으로 풍부한 지도를 생성합니다. 이 방법은 작물 회전 패턴 추적 등 심층 분석을 가능하게 하며, 경계 구분과 필드 수준의 정밀도를 향상시킵니다. 이를 통해 농업 모니터링과 역사적 경향 분석에 기여할 수 있는 잠재력을 입증하며, 미래의 작물 모니터링 및 수확량 추정 연구의 기초를 마련합니다.

## 🎯 주요 포인트

- 1. 밀은 전 세계 칼로리 섭취의 약 20%를 차지하며, 글로벌 식량 안보에 중요한 역할을 한다.
- 2. 본 논문은 위성 이미지를 활용하여 밀밭을 정확하게 매핑하기 위한 개선된 겨울 밀 분할 파이프라인을 제안한다.
- 3. Temporal Spatial Vision Transformer (TSViT)와 Parameter-Efficient Fine Tuning (PEFT)을 통합하여 필드 경계 추출의 정확성을 높인다.
- 4. 제안된 방법은 작은 농업 구획의 클러스터링 문제를 해결하여 기하학적으로 일관되고 의미적으로 풍부한 지도를 생성한다.
- 5. 이 연구는 밀밭의 정확한 매핑을 통해 작물 모니터링 및 수확량 추정과 같은 중요한 연구와 미래 발전의 기초를 마련한다.


---

*Generated on 2025-09-24 16:28:27*