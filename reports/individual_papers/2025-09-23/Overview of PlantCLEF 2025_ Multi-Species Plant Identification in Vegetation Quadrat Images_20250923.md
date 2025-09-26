---
keywords:
  - Transformer
  - Multi-Species Plant Identification
  - Quadrat Images
  - Multi-Label Classification
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17602
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:56:14.863114",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Multi-Species Plant Identification",
    "Quadrat Images",
    "Multi-Label Classification"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Multi-Species Plant Identification": 0.79,
    "Quadrat Images": 0.77,
    "Multi-Label Classification": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision Transformer",
        "canonical": "Transformer",
        "aliases": [
          "ViT"
        ],
        "category": "broad_technical",
        "rationale": "Vision Transformers are a key technology in computer vision, linking to broader AI advancements.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multi-Species Plant Identification",
        "canonical": "Multi-Species Plant Identification",
        "aliases": [
          "Plant Identification"
        ],
        "category": "unique_technical",
        "rationale": "This task is central to the paper and connects to ecological and AI research.",
        "novelty_score": 0.78,
        "connectivity_score": 0.67,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "Quadrat Images",
        "canonical": "Quadrat Images",
        "aliases": [
          "Vegetation Quadrat Images"
        ],
        "category": "unique_technical",
        "rationale": "Quadrat images are specific to ecological studies and crucial for biodiversity assessment.",
        "novelty_score": 0.72,
        "connectivity_score": 0.64,
        "specificity_score": 0.81,
        "link_intent_score": 0.77
      },
      {
        "surface": "Multi-Label Classification",
        "canonical": "Multi-Label Classification",
        "aliases": [
          "Multi-Label Task"
        ],
        "category": "specific_connectable",
        "rationale": "This classification task is a key challenge in AI, linking to machine learning techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.79,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "method",
      "evaluation",
      "results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision Transformer",
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
      "candidate_surface": "Multi-Species Plant Identification",
      "resolved_canonical": "Multi-Species Plant Identification",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.67,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Quadrat Images",
      "resolved_canonical": "Quadrat Images",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.64,
        "specificity": 0.81,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Multi-Label Classification",
      "resolved_canonical": "Multi-Label Classification",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.79,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Overview of PlantCLEF 2025: Multi-Species Plant Identification in Vegetation Quadrat Images

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17602.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17602](https://arxiv.org/abs/2509.17602)

## 🔗 유사한 논문
- [[2025-09-22/Overview of PlantCLEF 2024_ multi-species plant identification in vegetation plot images_20250922|Overview of PlantCLEF 2024: multi-species plant identification in vegetation plot images]] (96.2% similar)
- [[2025-09-19/Multi-label Scene Classification for Autonomous Vehicles_ Acquiring and Accumulating Knowledge from Diverse Datasets_20250919|Multi-label Scene Classification for Autonomous Vehicles: Acquiring and Accumulating Knowledge from Diverse Datasets]] (80.3% similar)
- [[2025-09-23/Training the next generation of physicians for artificial intelligence-assisted clinical neuroradiology_ ASNR MICCAI Brain Tumor Segmentation (BraTS) 2025 Lighthouse Challenge education platform_20250923|Training the next generation of physicians for artificial intelligence-assisted clinical neuroradiology: ASNR MICCAI Brain Tumor Segmentation (BraTS) 2025 Lighthouse Challenge education platform]] (79.6% similar)
- [[2025-09-23/Enhancing Scientific Visual Question Answering via Vision-Caption aware Supervised Fine-Tuning_20250923|Enhancing Scientific Visual Question Answering via Vision-Caption aware Supervised Fine-Tuning]] (79.2% similar)
- [[2025-09-23/Search-Optimized Quantization in Biomedical Ontology Alignment_20250923|Search-Optimized Quantization in Biomedical Ontology Alignment]] (79.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Multi-Label Classification|Multi-Label Classification]]
**⚡ Unique Technical**: [[keywords/Multi-Species Plant Identification|Multi-Species Plant Identification]], [[keywords/Quadrat Images|Quadrat Images]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17602v1 Announce Type: new 
Abstract: Quadrat images are essential for ecological studies, as they enable standardized sampling, the assessment of plant biodiversity, long-term monitoring, and large-scale field campaigns. These images typically cover an area of fifty centimetres or one square meter, and botanists carefully identify all the species present. Integrating AI could help specialists accelerate their inventories and expand the spatial coverage of ecological studies. To assess progress in this area, the PlantCLEF 2025 challenge relies on a new test set of 2,105 high-resolution multi-label images annotated by experts and covering around 400 species. It also provides a large training set of 1.4 million individual plant images, along with vision transformer models pre-trained on this data. The task is formulated as a (weakly labelled) multi-label classification problem, where the goal is to predict all species present in a quadrat image using single-label training data. This paper provides a detailed description of the data, the evaluation methodology, the methods and models used by participants, and the results achieved.

## 📝 요약

이 논문은 생태학 연구에서 중요한 방형구 이미지를 AI를 활용하여 분석하는 방법을 제안합니다. PlantCLEF 2025 챌린지를 통해 400여 종의 식물을 포함한 2,105개의 고해상도 다중 라벨 이미지를 사용하여 AI 모델의 성능을 평가합니다. 참가자들은 140만 개의 개별 식물 이미지와 사전 학습된 비전 트랜스포머 모델을 활용하여, 단일 라벨 학습 데이터를 기반으로 방형구 이미지에서 모든 종을 예측하는 다중 라벨 분류 문제를 해결합니다. 이 연구는 데이터, 평가 방법론, 사용된 모델 및 참가자들의 결과를 상세히 설명합니다.

## 🎯 주요 포인트

- 1. 사각형 이미지(quadrat images)는 생태학 연구에서 표준화된 샘플링, 식물 다양성 평가, 장기 모니터링 및 대규모 현장 캠페인에 필수적이다.
- 2. AI 통합은 전문가들이 생태학 연구의 목록 작성 속도를 높이고 공간적 범위를 확장하는 데 도움을 줄 수 있다.
- 3. PlantCLEF 2025 챌린지는 400종의 식물을 포함한 2,105개의 고해상도 다중 라벨 이미지로 구성된 새로운 테스트 세트를 기반으로 한다.
- 4. 이 챌린지는 140만 개의 개별 식물 이미지로 구성된 대규모 훈련 세트와 이 데이터를 사전 학습한 비전 트랜스포머 모델을 제공한다.
- 5. 이 논문은 데이터, 평가 방법론, 참가자들이 사용한 방법 및 모델, 그리고 달성된 결과에 대한 상세한 설명을 제공한다.


---

*Generated on 2025-09-24 04:56:14*