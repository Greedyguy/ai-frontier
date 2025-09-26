---
keywords:
  - PM25Vision Dataset
  - PM2.5 Concentration Estimation
  - Convolutional Neural Network
  - Transformer
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.16519
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:26:20.272156",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "PM25Vision Dataset",
    "PM2.5 Concentration Estimation",
    "Convolutional Neural Network",
    "Transformer"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "PM25Vision Dataset": 0.8,
    "PM2.5 Concentration Estimation": 0.78,
    "Convolutional Neural Network": 0.72,
    "Transformer": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "PM25Vision",
        "canonical": "PM25Vision Dataset",
        "aliases": [
          "PM25V"
        ],
        "category": "unique_technical",
        "rationale": "This dataset is central to the paper and provides a unique resource for air quality estimation research.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "PM2.5 concentrations",
        "canonical": "PM2.5 Concentration Estimation",
        "aliases": [
          "PM2.5 Levels"
        ],
        "category": "specific_connectable",
        "rationale": "This is a specific application area that connects to environmental monitoring and health impact studies.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "CNN",
        "canonical": "Convolutional Neural Network",
        "aliases": [
          "ConvNet"
        ],
        "category": "broad_technical",
        "rationale": "CNNs are a fundamental architecture in computer vision, relevant to the dataset's baseline models.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      },
      {
        "surface": "Transformer architectures",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Transformers are a key architecture used in the paper's baseline models, linking to a wide range of AI research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "dataset",
      "benchmark",
      "model performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "PM25Vision",
      "resolved_canonical": "PM25Vision Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "PM2.5 concentrations",
      "resolved_canonical": "PM2.5 Concentration Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "CNN",
      "resolved_canonical": "Convolutional Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Transformer architectures",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# PM25Vision: A Large-Scale Benchmark Dataset for Visual Estimation of Air Quality

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16519.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.16519](https://arxiv.org/abs/2509.16519)

## 🔗 유사한 논문
- [[2025-09-23/Detecting Urban PM$_{2.5}$ Hotspots with Mobile Sensing and Gaussian Process Regression_20250923|Detecting Urban PM$_{2.5}$ Hotspots with Mobile Sensing and Gaussian Process Regression]] (81.1% similar)
- [[2025-09-19/Forecasting and Visualizing Air Quality from Sky Images with Vision-Language Models_20250919|Forecasting and Visualizing Air Quality from Sky Images with Vision-Language Models]] (80.9% similar)
- [[2025-09-23/DocIQ_ A Benchmark Dataset and Feature Fusion Network for Document Image Quality Assessment_20250923|DocIQ: A Benchmark Dataset and Feature Fusion Network for Document Image Quality Assessment]] (79.2% similar)
- [[2025-09-23/AirQA_ A Comprehensive QA Dataset for AI Research with Instance-Level Evaluation_20250923|AirQA: A Comprehensive QA Dataset for AI Research with Instance-Level Evaluation]] (79.0% similar)
- [[2025-09-18/Do Vision-Language Models See Urban Scenes as People Do? An Urban Perception Benchmark_20250918|Do Vision-Language Models See Urban Scenes as People Do? An Urban Perception Benchmark]] (78.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Convolutional Neural Network|Convolutional Neural Network]], [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/PM2.5 Concentration Estimation|PM2.5 Concentration Estimation]]
**⚡ Unique Technical**: [[keywords/PM25Vision Dataset|PM25Vision Dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16519v1 Announce Type: new 
Abstract: We introduce PM25Vision (PM25V), the largest and most comprehensive dataset to date for estimating air quality - specifically PM2.5 concentrations - from street-level images. The dataset contains over 11,114 images matched with timestamped and geolocated PM2.5 readings across 3,261 AQI monitoring stations and 11 years, significantly exceeding the scale of previous benchmarks. The spatial accuracy of this dataset has reached 5 kilometers, far exceeding the city-level accuracy of many datasets. We describe the data collection, synchronization, and cleaning pipelines, and provide baseline model performances using CNN and transformer architectures. Our dataset is publicly available.

## 📝 요약

PM25Vision(PM25V)은 거리 이미지로부터 대기질, 특히 PM2.5 농도를 추정하기 위한 가장 크고 포괄적인 데이터셋입니다. 이 데이터셋은 11,114개 이상의 이미지와 3,261개의 AQI 모니터링 스테이션에서 11년간 수집된 시간 및 위치 기반 PM2.5 데이터를 포함하며, 기존 데이터셋보다 훨씬 큰 규모입니다. 공간 정확도는 5km에 이르러, 많은 데이터셋의 도시 수준 정확도를 초과합니다. 데이터 수집, 동기화 및 정리 과정을 설명하고, CNN 및 트랜스포머 아키텍처를 사용한 기준 모델 성능을 제공합니다. 데이터셋은 공개적으로 이용 가능합니다.

## 🎯 주요 포인트

- 1. PM25Vision(PM25V)은 거리 수준의 이미지로부터 대기질, 특히 PM2.5 농도를 추정하기 위한 가장 크고 포괄적인 데이터셋입니다.
- 2. 데이터셋은 11,114개 이상의 이미지와 3,261개의 AQI 모니터링 스테이션에서 11년에 걸쳐 수집된 시간 및 위치 기반 PM2.5 데이터를 포함합니다.
- 3. 데이터셋의 공간 정확도는 5킬로미터에 달하며, 이는 많은 기존 데이터셋의 도시 수준 정확도를 훨씬 초과합니다.
- 4. 데이터 수집, 동기화, 정리 파이프라인을 설명하고, CNN 및 트랜스포머 아키텍처를 사용한 기준 모델 성능을 제공합니다.
- 5. 이 데이터셋은 공개적으로 이용 가능합니다.


---

*Generated on 2025-09-24 04:26:20*