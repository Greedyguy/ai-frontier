---
keywords:
  - HDC-X
  - Medical Data Classification
  - Energy Efficiency
  - Hypervectors
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.14617
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:53:48.258808",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "HDC-X",
    "Medical Data Classification",
    "Energy Efficiency",
    "Hypervectors"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "HDC-X": 0.8,
    "Medical Data Classification": 0.78,
    "Energy Efficiency": 0.77,
    "Hypervectors": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "HDC-X",
        "canonical": "HDC-X",
        "aliases": [
          "High-Dimensional Computing X"
        ],
        "category": "unique_technical",
        "rationale": "HDC-X is a novel framework specifically designed for energy-efficient medical data classification on embedded devices.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "medical data classification",
        "canonical": "Medical Data Classification",
        "aliases": [
          "healthcare data classification"
        ],
        "category": "broad_technical",
        "rationale": "This term is central to the paper's focus on classifying medical data efficiently, which is a key application of machine learning.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "energy-efficient",
        "canonical": "Energy Efficiency",
        "aliases": [
          "low-power",
          "power-efficient"
        ],
        "category": "specific_connectable",
        "rationale": "Energy efficiency is crucial for deploying machine learning models on embedded devices, linking to broader discussions on sustainable computing.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.65,
        "link_intent_score": 0.77
      },
      {
        "surface": "hypervectors",
        "canonical": "Hypervectors",
        "aliases": [
          "high-dimensional vectors"
        ],
        "category": "unique_technical",
        "rationale": "Hypervectors are a unique aspect of the HDC-X framework, essential for its classification process.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "framework",
      "device",
      "accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "HDC-X",
      "resolved_canonical": "HDC-X",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "medical data classification",
      "resolved_canonical": "Medical Data Classification",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "energy-efficient",
      "resolved_canonical": "Energy Efficiency",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.65,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "hypervectors",
      "resolved_canonical": "Hypervectors",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# HDC-X: Efficient Medical Data Classification for Embedded Devices

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.14617.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.14617](https://arxiv.org/abs/2509.14617)

## 🔗 유사한 논문
- [[2025-09-18/HD3C_ Efficient Medical Data Classification for Embedded Devices_20250918|HD3C: Efficient Medical Data Classification for Embedded Devices]] (93.8% similar)
- [[2025-09-22/FedHK-MVFC_ Federated Heat Kernel Multi-View Clustering_20250922|FedHK-MVFC: Federated Heat Kernel Multi-View Clustering]] (81.6% similar)
- [[2025-09-23/An Efficient Dual-Line Decoder Network with Multi-Scale Convolutional Attention for Multi-organ Segmentation_20250923|An Efficient Dual-Line Decoder Network with Multi-Scale Convolutional Attention for Multi-organ Segmentation]] (81.6% similar)
- [[2025-09-22/Channel-Imposed Fusion_ A Simple yet Effective Method for Medical Time Series Classification_20250922|Channel-Imposed Fusion: A Simple yet Effective Method for Medical Time Series Classification]] (80.9% similar)
- [[2025-09-23/Interpretability-Aware Pruning for Efficient Medical Image Analysis_20250923|Interpretability-Aware Pruning for Efficient Medical Image Analysis]] (80.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Medical Data Classification|Medical Data Classification]]
**🔗 Specific Connectable**: [[keywords/Energy Efficiency|Energy Efficiency]]
**⚡ Unique Technical**: [[keywords/HDC-X|HDC-X]], [[keywords/Hypervectors|Hypervectors]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14617v2 Announce Type: replace 
Abstract: Energy-efficient medical data classification is essential for modern disease screening, particularly in home and field healthcare where embedded devices are prevalent. While deep learning models achieve state-of-the-art accuracy, their substantial energy consumption and reliance on GPUs limit deployment on such platforms. We present HDC-X, a lightweight classification framework designed for low-power devices. HDC-X encodes data into high-dimensional hypervectors, aggregates them into multiple cluster-specific prototypes, and performs classification through similarity search in hyperspace. We evaluate HDC-X across three medical classification tasks; on heart sound classification, HDC-X is $350\times$ more energy-efficient than Bayesian ResNet with less than 1% accuracy difference. Moreover, HDC-X demonstrates exceptional robustness to noise, limited training data, and hardware error, supported by both theoretical analysis and empirical results, highlighting its potential for reliable deployment in real-world settings. Code is available at https://github.com/jianglanwei/HDC-X.

## 📝 요약

HDC-X는 저전력 장치를 위한 경량 분류 프레임워크로, 고차원 하이퍼벡터를 사용하여 데이터를 인코딩하고, 여러 클러스터별 프로토타입으로 집계한 후, 유사성 검색을 통해 분류를 수행합니다. 이 연구는 세 가지 의료 분류 작업에서 HDC-X를 평가했으며, 특히 심장 소리 분류에서 Bayesian ResNet보다 350배 에너지 효율적이면서도 정확도 차이가 1% 미만입니다. 또한, HDC-X는 소음, 제한된 훈련 데이터, 하드웨어 오류에 대한 뛰어난 강건성을 보여주며, 이론적 분석과 실험 결과로 신뢰할 수 있는 실제 환경 배포 가능성을 강조합니다.

## 🎯 주요 포인트

- 1. HDC-X는 저전력 장치에 적합한 경량 분류 프레임워크로, 고차원 하이퍼벡터로 데이터를 인코딩하여 분류를 수행합니다.
- 2. HDC-X는 심장 소리 분류에서 Bayesian ResNet보다 350배 더 에너지 효율적이며, 정확도 차이는 1% 미만입니다.
- 3. HDC-X는 소음, 제한된 훈련 데이터, 하드웨어 오류에 대한 뛰어난 강건성을 보이며, 이론적 분석과 실험 결과로 이를 뒷받침합니다.
- 4. HDC-X는 가정 및 현장 의료 환경에서의 신뢰할 수 있는 배포 가능성을 강조합니다.


---

*Generated on 2025-09-24 02:53:48*