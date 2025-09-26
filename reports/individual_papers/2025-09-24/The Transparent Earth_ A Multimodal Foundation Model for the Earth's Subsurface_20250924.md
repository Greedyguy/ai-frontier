<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:39:40.430303",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transparent Earth Model",
    "Transformer",
    "Multimodal Learning",
    "Attention Mechanism"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transparent Earth Model": 0.78,
    "Transformer": 0.8,
    "Multimodal Learning": 0.82,
    "Attention Mechanism": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transparent Earth",
        "canonical": "Transparent Earth Model",
        "aliases": [
          "Transparent Earth Architecture"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel model specifically designed for subsurface property prediction, enhancing unique technical linkage.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "transformer-based architecture",
        "canonical": "Transformer",
        "aliases": [
          "transformer architecture"
        ],
        "category": "broad_technical",
        "rationale": "Connects to existing transformer-based models, facilitating links to a wide range of machine learning applications.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "multimodal",
        "canonical": "Multimodal Learning",
        "aliases": [
          "multimodal approach"
        ],
        "category": "specific_connectable",
        "rationale": "Links to the growing field of multimodal learning, which is crucial for integrating diverse data types.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "positional encodings",
        "canonical": "Attention Mechanism",
        "aliases": [
          "position encoding"
        ],
        "category": "specific_connectable",
        "rationale": "Enhances connectivity with models utilizing attention mechanisms, particularly in transformer architectures.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "subsurface properties",
      "heterogeneous datasets"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Transparent Earth",
      "resolved_canonical": "Transparent Earth Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "transformer-based architecture",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "multimodal",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "positional encodings",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# The Transparent Earth: A Multimodal Foundation Model for the Earth's Subsurface

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.02783.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.02783](https://arxiv.org/abs/2509.02783)

## 🔗 유사한 논문
- [[2025-09-22/TESSERA_ Precomputed FAIR Global Pixel Embeddings for Earth Representation and Analysis_20250922|TESSERA: Precomputed FAIR Global Pixel Embeddings for Earth Representation and Analysis]] (84.0% similar)
- [[2025-09-22/The Moon's Many Faces_ A Single Unified Transformer for Multimodal Lunar Reconstruction_20250922|The Moon's Many Faces: A Single Unified Transformer for Multimodal Lunar Reconstruction]] (82.6% similar)
- [[2025-09-23/StefaLand_ An Efficient Geoscience Foundation Model That Improves Dynamic Land-Surface Predictions_20250923|StefaLand: An Efficient Geoscience Foundation Model That Improves Dynamic Land-Surface Predictions]] (81.7% similar)
- [[2025-09-17/Towards a Physics Foundation Model_20250917|Towards a Physics Foundation Model]] (81.1% similar)
- [[2025-09-23/EarthGPT-X_ A Spatial MLLM for Multi-level Multi-Source Remote Sensing Imagery Understanding with Visual Prompting_20250923|EarthGPT-X: A Spatial MLLM for Multi-level Multi-Source Remote Sensing Imagery Understanding with Visual Prompting]] (80.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Transparent Earth Model|Transparent Earth Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.02783v2 Announce Type: replace-cross 
Abstract: We present the Transparent Earth, a transformer-based architecture for reconstructing subsurface properties from heterogeneous datasets that vary in sparsity, resolution, and modality, where each modality represents a distinct type of observation (e.g., stress angle, mantle temperature, tectonic plate type). The model incorporates positional encodings of observations together with modality encodings, derived from a text embedding model applied to a description of each modality. This design enables the model to scale to an arbitrary number of modalities, making it straightforward to add new ones not considered in the initial design. We currently include eight modalities spanning directional angles, categorical classes, and continuous properties such as temperature and thickness. These capabilities support in-context learning, enabling the model to generate predictions either with no inputs or with an arbitrary number of additional observations from any subset of modalities. On validation data, this reduces errors in predicting stress angle by more than a factor of three. The proposed architecture is scalable and demonstrates improved performance with increased parameters. Together, these advances make the Transparent Earth an initial foundation model for the Earth's subsurface that ultimately aims to predict any subsurface property anywhere on Earth.

## 📝 요약

논문에서는 다양한 밀도, 해상도, 관측 유형을 가진 이질적인 데이터셋으로부터 지하 특성을 재구성하는 Transformer 기반 아키텍처인 Transparent Earth를 제안합니다. 이 모델은 각 관측 유형에 대한 설명을 텍스트 임베딩 모델로부터 얻은 모달리티 인코딩과 위치 인코딩을 결합하여, 초기 설계에 고려되지 않은 새로운 모달리티도 쉽게 추가할 수 있도록 설계되었습니다. 현재 방향 각도, 범주형 클래스, 온도 및 두께와 같은 연속적 특성을 포함한 8가지 모달리티를 포함하고 있으며, 이는 다양한 모달리티의 추가 관측 없이도 예측을 생성할 수 있는 능력을 제공합니다. 검증 데이터에서 스트레스 각도 예측 오류를 3배 이상 줄였으며, 매개변수 증가에 따라 성능이 향상되는 확장성을 보여줍니다. 이러한 발전은 지구의 지하 특성을 예측하기 위한 초기 기반 모델로서의 가능성을 제시합니다.

## 🎯 주요 포인트

- 1. Transparent Earth는 다양한 희소성, 해상도, 모달리티를 가진 이질적인 데이터셋으로부터 지하 특성을 재구성하기 위한 트랜스포머 기반 아키텍처입니다.
- 2. 모델은 각 모달리티에 대한 설명에 적용된 텍스트 임베딩 모델에서 파생된 모달리티 인코딩과 관측치의 위치 인코딩을 통합합니다.
- 3. 이 설계는 임의의 모달리티 수로 확장할 수 있어 초기 설계에서 고려되지 않은 새로운 모달리티를 추가하기 용이합니다.
- 4. 모델은 방향 각도, 범주형 클래스, 온도 및 두께와 같은 연속적 특성을 포함한 8개의 모달리티를 현재 포함하고 있습니다.
- 5. 검증 데이터에서 스트레스 각도 예측 오류를 3배 이상 줄이며, 지구의 지하 특성을 어디서든 예측할 수 있는 초기 기반 모델로서의 가능성을 보여줍니다.


---

*Generated on 2025-09-24 14:39:40*