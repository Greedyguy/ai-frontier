<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:06:01.403676",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Automated Plant Identification",
    "Herbarium Collections",
    "Cross-Domain Classification"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Automated Plant Identification": 0.8,
    "Herbarium Collections": 0.78,
    "Cross-Domain Classification": 0.77
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
        "rationale": "Deep Learning is a core technology enabling automated plant identification, linking to existing research in machine learning.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "Automated Plant Identification",
        "canonical": "Automated Plant Identification",
        "aliases": [
          "Plant Identification"
        ],
        "category": "unique_technical",
        "rationale": "This is the central focus of the paper, offering unique insights into cross-domain identification methods.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Herbarium Collections",
        "canonical": "Herbarium Collections",
        "aliases": [
          "Herbarium Records"
        ],
        "category": "unique_technical",
        "rationale": "Herbarium Collections are crucial for training data in biodiversity-rich regions, linking to botanical data resources.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Cross-Domain Classification",
        "canonical": "Cross-Domain Classification",
        "aliases": [
          "Cross-Domain Learning"
        ],
        "category": "specific_connectable",
        "rationale": "Cross-Domain Classification is a key method used in the challenge, connecting to broader machine learning techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "biodiversity",
      "photos",
      "metadata"
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
      "candidate_surface": "Automated Plant Identification",
      "resolved_canonical": "Automated Plant Identification",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Herbarium Collections",
      "resolved_canonical": "Herbarium Collections",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Cross-Domain Classification",
      "resolved_canonical": "Cross-Domain Classification",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Overview of PlantCLEF 2021: cross-domain plant identification

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18697.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18697](https://arxiv.org/abs/2509.18697)

## 🔗 유사한 논문
- [[2025-09-23/Overview of PlantCLEF 2022_ Image-based plant identification at global scale_20250923|Overview of PlantCLEF 2022: Image-based plant identification at global scale]] (91.5% similar)
- [[2025-09-23/Overview of PlantCLEF 2023_ Image-based Plant Identification at Global Scale_20250923|Overview of PlantCLEF 2023: Image-based Plant Identification at Global Scale]] (90.8% similar)
- [[2025-09-22/Overview of PlantCLEF 2024_ multi-species plant identification in vegetation plot images_20250922|Overview of PlantCLEF 2024: multi-species plant identification in vegetation plot images]] (88.6% similar)
- [[2025-09-23/Overview of PlantCLEF 2025_ Multi-Species Plant Identification in Vegetation Quadrat Images_20250923|Overview of PlantCLEF 2025: Multi-Species Plant Identification in Vegetation Quadrat Images]] (88.4% similar)
- [[2025-09-23/DIVERS-Bench_ Evaluating Language Identification Across Domain Shifts and Code-Switching_20250923|DIVERS-Bench: Evaluating Language Identification Across Domain Shifts and Code-Switching]] (76.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Cross-Domain Classification|Cross-Domain Classification]]
**⚡ Unique Technical**: [[keywords/Automated Plant Identification|Automated Plant Identification]], [[keywords/Herbarium Collections|Herbarium Collections]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18697v1 Announce Type: new 
Abstract: Automated plant identification has improved considerably thanks to recent advances in deep learning and the availability of training data with more and more field photos. However, this profusion of data concerns only a few tens of thousands of species, mainly located in North America and Western Europe, much less in the richest regions in terms of biodiversity such as tropical countries. On the other hand, for several centuries, botanists have systematically collected, catalogued and stored plant specimens in herbaria, especially in tropical regions, and recent efforts by the biodiversity informatics community have made it possible to put millions of digitised records online. The LifeCLEF 2021 plant identification challenge (or "PlantCLEF 2021") was designed to assess the extent to which automated identification of flora in data-poor regions can be improved by using herbarium collections. It is based on a dataset of about 1,000 species mainly focused on the Guiana Shield of South America, a region known to have one of the highest plant diversities in the world. The challenge was evaluated as a cross-domain classification task where the training set consisted of several hundred thousand herbarium sheets and a few thousand photos to allow learning a correspondence between the two domains. In addition to the usual metadata (location, date, author, taxonomy), the training data also includes the values of 5 morphological and functional traits for each species. The test set consisted exclusively of photos taken in the field. This article presents the resources and evaluations of the assessment carried out, summarises the approaches and systems used by the participating research groups and provides an analysis of the main results.

## 📝 요약

자동화된 식물 식별 기술은 심층 학습의 발전과 현장 사진 데이터의 증가로 크게 향상되었습니다. 그러나 이러한 데이터는 주로 북미와 서유럽의 수만 종에 집중되어 있으며, 생물다양성이 풍부한 열대 지역에서는 부족합니다. 반면, 수세기 동안 식물학자들은 열대 지역을 중심으로 식물 표본을 수집하고 분류하여 표본관에 보관해 왔으며, 최근에는 생물다양성 정보학 커뮤니티의 노력으로 수백만 건의 디지털 기록이 온라인에 공개되었습니다. LifeCLEF 2021 식물 식별 챌린지(PlantCLEF 2021)는 이러한 표본관 데이터를 활용하여 데이터가 부족한 지역의 식물 자동 식별을 개선할 수 있는지를 평가하기 위해 설계되었습니다. 이 챌린지는 남아메리카의 Guiana Shield 지역을 중심으로 약 1,000종의 데이터를 기반으로 하며, 훈련 세트는 수십만 장의 표본관 이미지와 수천 장의 사진으로 구성되어 두 도메인 간의 대응을 학습할 수 있도록 했습니다. 테스트 세트는 현장에서 촬영된 사진으로만 구성되었습니다. 이 논문은 평가에 사용된 자원과 평가 결과를 제시하고, 참여 연구 그룹의 접근 방식과 시스템을 요약하며 주요 결과를 분석합니다.

## 🎯 주요 포인트

- 1. 최근 딥러닝의 발전과 현장 사진 데이터의 증가로 자동 식물 식별 기술이 크게 향상되었습니다.
- 2. 현재 데이터는 주로 북미와 서유럽의 수만 종의 식물에 집중되어 있으며, 생물다양성이 풍부한 열대 지역에서는 데이터가 부족합니다.
- 3. 식물 표본은 수 세기 동안 식물학자들에 의해 수집되어 왔으며, 최근에는 수백만 개의 디지털 기록이 온라인에 공개되었습니다.
- 4. LifeCLEF 2021 식물 식별 챌린지는 허바리움 컬렉션을 활용하여 데이터가 부족한 지역의 식물 식별을 개선하는 것을 목표로 합니다.
- 5. 이 챌린지는 남아메리카의 Guiana Shield 지역의 약 1,000종을 대상으로 하며, 교차 도메인 분류 작업으로 평가되었습니다.


---

*Generated on 2025-09-24 16:06:01*