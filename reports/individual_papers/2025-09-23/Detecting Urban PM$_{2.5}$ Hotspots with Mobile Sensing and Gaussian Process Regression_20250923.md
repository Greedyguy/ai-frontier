---
keywords:
  - Gaussian Process Regression
  - PM$_{2.5}$ Hotspots
  - Mobile Sensing
  - Urban Air Quality
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17175
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:48:01.989933",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Gaussian Process Regression",
    "PM$_{2.5}$ Hotspots",
    "Mobile Sensing",
    "Urban Air Quality"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Gaussian Process Regression": 0.78,
    "PM$_{2.5}$ Hotspots": 0.77,
    "Mobile Sensing": 0.75,
    "Urban Air Quality": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Gaussian Process Regression",
        "canonical": "Gaussian Process Regression",
        "aliases": [
          "GPR"
        ],
        "category": "unique_technical",
        "rationale": "This method is central to the study's approach for modeling pollution data, offering a unique technical perspective.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "PM$_{2.5}$ Hotspots",
        "canonical": "PM$_{2.5}$ Hotspots",
        "aliases": [
          "Air Pollution Hotspots"
        ],
        "category": "unique_technical",
        "rationale": "Identifying these hotspots is a key objective of the study, providing a unique focus on urban air quality.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.77
      },
      {
        "surface": "Mobile Sensing",
        "canonical": "Mobile Sensing",
        "aliases": [
          "Mobile Sensors",
          "Portable Sensors"
        ],
        "category": "specific_connectable",
        "rationale": "This approach is crucial for data collection in the study, linking to broader themes of sensor networks.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Urban Air Quality",
        "canonical": "Urban Air Quality",
        "aliases": [
          "City Air Quality"
        ],
        "category": "broad_technical",
        "rationale": "This is a fundamental theme of the paper, connecting to broader discussions on environmental health.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "data",
      "results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Gaussian Process Regression",
      "resolved_canonical": "Gaussian Process Regression",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "PM$_{2.5}$ Hotspots",
      "resolved_canonical": "PM$_{2.5}$ Hotspots",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Mobile Sensing",
      "resolved_canonical": "Mobile Sensing",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Urban Air Quality",
      "resolved_canonical": "Urban Air Quality",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Detecting Urban PM$_{2.5}$ Hotspots with Mobile Sensing and Gaussian Process Regression

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17175.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17175](https://arxiv.org/abs/2509.17175)

## 🔗 유사한 논문
- [[2025-09-19/Forecasting and Visualizing Air Quality from Sky Images with Vision-Language Models_20250919|Forecasting and Visualizing Air Quality from Sky Images with Vision-Language Models]] (79.3% similar)
- [[2025-09-23/Detection and Simulation of Urban Heat Islands Using a Fine-Tuned Geospatial Foundation Model_20250923|Detection and Simulation of Urban Heat Islands Using a Fine-Tuned Geospatial Foundation Model]] (78.7% similar)
- [[2025-09-19/From Pixels to Urban Policy-Intelligence_ Recovering Legacy Effects of Redlining with a Multimodal LLM_20250919|From Pixels to Urban Policy-Intelligence: Recovering Legacy Effects of Redlining with a Multimodal LLM]] (75.4% similar)
- [[2025-09-17/Multi-robot Multi-source Localization in Complex Flows with Physics-Preserving Environment Models_20250917|Multi-robot Multi-source Localization in Complex Flows with Physics-Preserving Environment Models]] (75.4% similar)
- [[2025-09-18/Do Vision-Language Models See Urban Scenes as People Do? An Urban Perception Benchmark_20250918|Do Vision-Language Models See Urban Scenes as People Do? An Urban Perception Benchmark]] (75.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Urban Air Quality|Urban Air Quality]]
**🔗 Specific Connectable**: [[keywords/Mobile Sensing|Mobile Sensing]]
**⚡ Unique Technical**: [[keywords/Gaussian Process Regression|Gaussian Process Regression]], [[keywords/PM$_{2.5}$ Hotspots|PM$_{2.5}$ Hotspots]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17175v1 Announce Type: new 
Abstract: Low-cost mobile sensors can be used to collect PM$_{2.5}$ concentration data throughout an entire city. However, identifying air pollution hotspots from the data is challenging due to the uneven spatial sampling, temporal variations in the background air quality, and the dynamism of urban air pollution sources. This study proposes a method to identify urban PM$_{2.5}$ hotspots that addresses these challenges, involving four steps: (1) equip citizen scientists with mobile PM$_{2.5}$ sensors while they travel; (2) normalise the raw data to remove the influence of background ambient pollution levels; (3) fit a Gaussian process regression model to the normalised data and (4) calculate a grid of spatially explicit 'hotspot scores' using the probabilistic framework of Gaussian processes, which conveniently summarise the relative pollution levels throughout the city. We apply our method to create the first ever map of PM$_{2.5}$ pollution in Kigali, Rwanda, at a 200m resolution. Our results suggest that the level of ambient PM$_{2.5}$ pollution in Kigali is dangerously high, and we identify the hotspots in Kigali where pollution consistently exceeds the city-wide average. We also evaluate our method using simulated mobile sensing data for Beijing, China, where we find that the hotspot scores are probabilistically well calibrated and accurately reflect the 'ground truth' spatial profile of PM$_{2.5}$ pollution. Thanks to the use of open-source software, our method can be re-applied in cities throughout the world with a handful of low-cost sensors. The method can help fill the gap in urban air quality information and empower public health officials.

## 📝 요약

이 연구는 저비용 모바일 센서를 활용하여 도시 전역의 PM$_{2.5}$ 농도 데이터를 수집하고, 이를 통해 공기 오염 핫스팟을 식별하는 방법을 제안합니다. 방법론은 시민 과학자들이 이동 중에 센서를 사용하고, 원시 데이터를 정규화하여 배경 오염의 영향을 제거한 후, 가우시안 프로세스 회귀 모델을 적용하여 공간적으로 명확한 '핫스팟 점수'를 계산하는 네 단계로 구성됩니다. 이 방법을 통해 르완다 키갈리의 PM$_{2.5}$ 오염 지도를 200m 해상도로 처음 작성하였으며, 키갈리의 대기 오염 수준이 위험할 정도로 높다는 것을 발견했습니다. 또한, 중국 베이징의 시뮬레이션 데이터를 통해 방법론의 정확성을 검증하였습니다. 이 방법은 전 세계 도시에서 저비용 센서를 사용하여 적용 가능하며, 도시 대기 질 정보의 격차를 메우고 공중 보건 당국에 도움을 줄 수 있습니다.

## 🎯 주요 포인트

- 1. 저비용 모바일 센서를 활용하여 도시 전역의 PM$_{2.5}$ 농도 데이터를 수집할 수 있다.
- 2. 도시의 PM$_{2.5}$ 핫스팟을 식별하기 위한 방법론을 제안하며, 이는 4단계로 구성된다: 시민 과학자들에게 모바일 센서를 장착, 원시 데이터 정규화, 가우시안 프로세스 회귀 모델 적용, 공간적으로 명시적인 '핫스팟 점수' 계산.
- 3. 이 방법론을 통해 르완다의 키갈리에서 200m 해상도의 PM$_{2.5}$ 오염 지도를 최초로 생성하였다.
- 4. 키갈리의 대기 PM$_{2.5}$ 오염 수준이 위험할 정도로 높으며, 도시 평균을 지속적으로 초과하는 핫스팟을 식별하였다.
- 5. 이 방법은 저비용 센서 몇 개만으로 전 세계 도시에서 재적용 가능하며, 도시 대기질 정보의 격차를 메우고 공중 보건 당국을 지원할 수 있다.


---

*Generated on 2025-09-24 01:48:01*