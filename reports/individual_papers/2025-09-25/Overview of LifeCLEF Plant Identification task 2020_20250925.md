---
keywords:
  - Deep Learning
  - Herbarium Collections
  - Biodiversity Informatics
  - Cross-Domain Classification
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.19402
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:59:21.474712",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Herbarium Collections",
    "Biodiversity Informatics",
    "Cross-Domain Classification"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Herbarium Collections": 0.78,
    "Biodiversity Informatics": 0.8,
    "Cross-Domain Classification": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "deep learning",
        "canonical": "Deep Learning",
        "aliases": [
          "DL"
        ],
        "category": "broad_technical",
        "rationale": "Deep Learning is a key technology used in the automated identification of plants, linking it to broader machine learning applications.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "herbarium collections",
        "canonical": "Herbarium Collections",
        "aliases": [
          "herbarium sheets",
          "plant specimens"
        ],
        "category": "unique_technical",
        "rationale": "Herbarium Collections are crucial for training data in biodiversity informatics, linking historical data to modern plant identification tasks.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "biodiversity informatics",
        "canonical": "Biodiversity Informatics",
        "aliases": [
          "bioinformatics",
          "biodiversity data"
        ],
        "category": "specific_connectable",
        "rationale": "Biodiversity Informatics connects the study of biodiversity with informatics, facilitating links to data-driven ecological research.",
        "novelty_score": 0.58,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "cross-domain classification",
        "canonical": "Cross-Domain Classification",
        "aliases": [
          "cross-domain learning",
          "domain adaptation"
        ],
        "category": "specific_connectable",
        "rationale": "Cross-Domain Classification is essential for adapting models trained on herbarium data to field photos, linking domain adaptation techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "automated identification",
      "training data",
      "photos in the field"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "deep learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "herbarium collections",
      "resolved_canonical": "Herbarium Collections",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "biodiversity informatics",
      "resolved_canonical": "Biodiversity Informatics",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "cross-domain classification",
      "resolved_canonical": "Cross-Domain Classification",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Overview of LifeCLEF Plant Identification task 2020

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19402.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.19402](https://arxiv.org/abs/2509.19402)

## 🔗 유사한 논문
- [[2025-09-24/Overview of PlantCLEF 2021_ cross-domain plant identification_20250924|Overview of PlantCLEF 2021: cross-domain plant identification]] (95.4% similar)
- [[2025-09-24/Overview of LifeCLEF Plant Identification task 2019_ diving into data deficient tropical countries_20250924|Overview of LifeCLEF Plant Identification task 2019: diving into data deficient tropical countries]] (92.0% similar)
- [[2025-09-23/Overview of PlantCLEF 2022_ Image-based plant identification at global scale_20250923|Overview of PlantCLEF 2022: Image-based plant identification at global scale]] (89.0% similar)
- [[2025-09-23/Overview of PlantCLEF 2023_ Image-based Plant Identification at Global Scale_20250923|Overview of PlantCLEF 2023: Image-based Plant Identification at Global Scale]] (88.7% similar)
- [[2025-09-22/Overview of PlantCLEF 2024_ multi-species plant identification in vegetation plot images_20250922|Overview of PlantCLEF 2024: multi-species plant identification in vegetation plot images]] (87.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Biodiversity Informatics|Biodiversity Informatics]], [[keywords/Cross-Domain Classification|Cross-Domain Classification]]
**⚡ Unique Technical**: [[keywords/Herbarium Collections|Herbarium Collections]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19402v1 Announce Type: new 
Abstract: Automated identification of plants has improved considerably thanks to the recent progress in deep learning and the availability of training data with more and more photos in the field. However, this profusion of data only concerns a few tens of thousands of species, mostly located in North America and Western Europe, much less in the richest regions in terms of biodiversity such as tropical countries. On the other hand, for several centuries, botanists have collected, catalogued and systematically stored plant specimens in herbaria, particularly in tropical regions, and the recent efforts by the biodiversity informatics community made it possible to put millions of digitized sheets online. The LifeCLEF 2020 Plant Identification challenge (or "PlantCLEF 2020") was designed to evaluate to what extent automated identification on the flora of data deficient regions can be improved by the use of herbarium collections. It is based on a dataset of about 1,000 species mainly focused on the South America's Guiana Shield, an area known to have one of the greatest diversity of plants in the world. The challenge was evaluated as a cross-domain classification task where the training set consist of several hundred thousand herbarium sheets and few thousand of photos to enable learning a mapping between the two domains. The test set was exclusively composed of photos in the field. This paper presents the resources and assessments of the conducted evaluation, summarizes the approaches and systems employed by the participating research groups, and provides an analysis of the main outcomes.

## 📝 요약

이 논문은 LifeCLEF 2020 식물 식별 챌린지를 통해 데이터가 부족한 지역의 식물 자동 식별을 개선하기 위한 연구를 다룹니다. 주로 남아메리카의 기아나 쉴드 지역의 약 1,000종을 대상으로 하며, 수백만 장의 디지털화된 허바리움 시트를 활용하여 사진과의 도메인 간 매핑을 학습합니다. 평가 결과, 허바리움 데이터를 활용한 접근 방식이 식물 식별 정확도를 향상시킬 수 있음을 보여주었습니다. 연구는 참여 그룹의 방법론과 시스템을 요약하고 주요 결과를 분석합니다.

## 🎯 주요 포인트

- 1. 심층 학습의 발전과 풍부한 훈련 데이터 덕분에 식물의 자동 식별이 크게 개선되었지만, 이는 주로 북미와 서유럽에 국한된 수만 종에만 해당됩니다.
- 2. 열대 지역을 포함한 다양한 지역에서 수집된 식물 표본이 허바리움에 보관되어 있으며, 최근 생물다양성 정보학 커뮤니티의 노력으로 수백만 장의 디지털화된 시트가 온라인에 공개되었습니다.
- 3. LifeCLEF 2020 식물 식별 챌린지는 허바리움 컬렉션을 활용하여 데이터가 부족한 지역의 식물 자동 식별을 개선할 수 있는지를 평가하기 위해 설계되었습니다.
- 4. 이 챌린지는 남미의 가이아나 실드 지역의 약 1,000종을 중심으로 한 데이터셋을 기반으로 하며, 훈련 세트는 수십만 장의 허바리움 시트와 수천 장의 사진으로 구성되어 두 도메인 간의 매핑 학습을 가능하게 했습니다.
- 5. 논문은 평가에 사용된 자원과 평가 결과를 제시하고, 참가 연구 그룹이 사용한 접근 방식과 시스템을 요약하며, 주요 결과에 대한 분석을 제공합니다.


---

*Generated on 2025-09-26 08:59:21*