---
keywords:
  - Deep Learning
  - Neural Network
  - Compound Fault Diagnosis
  - Frequency Domain Representation
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2504.07155
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:06:44.619577",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Neural Network",
    "Compound Fault Diagnosis",
    "Frequency Domain Representation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Neural Network": 0.78,
    "Compound Fault Diagnosis": 0.8,
    "Frequency Domain Representation": 0.77
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
        "rationale": "Deep Learning is a key technique used in the proposed model, linking it to a wide range of related research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "1-dimensional convolutional neural network",
        "canonical": "Neural Network",
        "aliases": [
          "1D CNN"
        ],
        "category": "specific_connectable",
        "rationale": "The use of a 1D CNN is central to the proposed method, offering specific connections to neural network research.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "compound fault diagnosis",
        "canonical": "Compound Fault Diagnosis",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a unique application area of the study, providing a specific link to fault diagnosis research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "frequency domain representation",
        "canonical": "Frequency Domain Representation",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The frequency domain representation is a novel aspect of the method, offering a unique technical perspective.",
        "novelty_score": 0.68,
        "connectivity_score": 0.55,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "train transmission systems",
      "PHM Beijing 2024 dataset"
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
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "1-dimensional convolutional neural network",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "compound fault diagnosis",
      "resolved_canonical": "Compound Fault Diagnosis",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "frequency domain representation",
      "resolved_canonical": "Frequency Domain Representation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.55,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Compound Fault Diagnosis for Train Transmission Systems Using Deep Learning with Fourier-enhanced Representation

**Korean Title:** 기차 전송 시스템의 복합 결함 진단을 위한 푸리에 강화 표현을 활용한 딥러닝 연구

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2504.07155.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2504.07155](https://arxiv.org/abs/2504.07155)

## 🔗 유사한 논문
- [[2025-09-22/Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets_20250922|Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets]] (78.3% similar)
- [[2025-09-18/Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model_20250918|Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model]] (77.6% similar)
- [[2025-09-17/Deep Temporal Graph Networks for Real-Time Correction of GNSS Jamming-Induced Deviations_20250917|Deep Temporal Graph Networks for Real-Time Correction of GNSS Jamming-Induced Deviations]] (77.5% similar)
- [[2025-09-19/Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2_ Atypical Mitosis Classification_20250919|Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2: Atypical Mitosis Classification]] (77.3% similar)
- [[2025-09-22/Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture_20250922|Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture]] (77.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Neural Network|Neural Network]]
**⚡ Unique Technical**: [[keywords/Compound Fault Diagnosis|Compound Fault Diagnosis]], [[keywords/Frequency Domain Representation|Frequency Domain Representation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.07155v3 Announce Type: replace 
Abstract: Fault diagnosis prevents train disruptions by ensuring the stability and reliability of their transmission systems. Data-driven fault diagnosis models have several advantages over traditional methods in terms of dealing with non-linearity, adaptability, scalability, and automation. However, existing data-driven models are trained on separate transmission components and only consider single faults due to the limitations of existing datasets. These models will perform worse in scenarios where components operate with each other at the same time, affecting each component's vibration signals. To address some of these challenges, we propose a frequency domain representation and a 1-dimensional convolutional neural network for compound fault diagnosis and applied it on the PHM Beijing 2024 dataset, which includes 21 sensor channels, 17 single faults, and 42 compound faults from 4 interacting components, that is, motor, gearbox, left axle box, and right axle box. Our proposed model achieved 97.67% and 93.93% accuracies on the test set with 17 single faults and on the test set with 42 compound faults, respectively.

## 🔍 Abstract (한글 번역)

arXiv:2504.07155v3 발표 유형: 교체  
초록: 고장 진단은 전송 시스템의 안정성과 신뢰성을 보장함으로써 열차 중단을 방지합니다. 데이터 기반 고장 진단 모델은 비선형성, 적응성, 확장성 및 자동화 측면에서 전통적인 방법에 비해 여러 가지 이점을 가지고 있습니다. 그러나 기존의 데이터 기반 모델은 개별 전송 구성 요소에 대해 훈련되며, 기존 데이터셋의 한계로 인해 단일 고장만 고려합니다. 이러한 모델은 구성 요소가 동시에 작동하여 각 구성 요소의 진동 신호에 영향을 미치는 시나리오에서 성능이 저하될 것입니다. 이러한 문제를 해결하기 위해 우리는 복합 고장 진단을 위한 주파수 도메인 표현과 1차원 합성곱 신경망을 제안하고, 이를 모터, 기어박스, 왼쪽 차축 상자, 오른쪽 차축 상자라는 4개의 상호작용 구성 요소로부터 21개의 센서 채널, 17개의 단일 고장, 42개의 복합 고장을 포함하는 PHM Beijing 2024 데이터셋에 적용했습니다. 제안된 모델은 17개의 단일 고장이 있는 테스트 세트에서 97.67%의 정확도와 42개의 복합 고장이 있는 테스트 세트에서 93.93%의 정확도를 달성했습니다.

## 📝 요약

이 논문은 열차 전송 시스템의 안정성과 신뢰성을 보장하기 위한 고장 진단에 관한 연구입니다. 기존 데이터 기반 모델들은 개별 전송 부품의 단일 고장만을 고려하여 복합적인 고장 진단에 한계가 있었습니다. 이를 해결하기 위해, 주파수 도메인 표현과 1차원 합성곱 신경망을 활용한 복합 고장 진단 모델을 제안하였습니다. 이 모델은 PHM Beijing 2024 데이터셋을 사용하여 4개의 상호작용 부품에서 발생하는 단일 및 복합 고장을 진단하였으며, 단일 고장 테스트에서 97.67%, 복합 고장 테스트에서 93.93%의 정확도를 달성했습니다.

## 🎯 주요 포인트

- 1. 데이터 기반 고장 진단 모델은 비선형성, 적응성, 확장성 및 자동화 측면에서 전통적인 방법보다 여러 가지 장점을 가지고 있습니다.
- 2. 기존 데이터 기반 모델은 개별 전송 구성 요소에 대해 훈련되며 단일 고장만을 고려하여, 여러 구성 요소가 동시에 작동하는 시나리오에서는 성능이 저하됩니다.
- 3. 복합 고장 진단을 위해 주파수 도메인 표현과 1차원 합성곱 신경망을 제안하였으며, 이를 PHM Beijing 2024 데이터셋에 적용하였습니다.
- 4. 제안된 모델은 17개의 단일 고장에 대해 97.67%, 42개의 복합 고장에 대해 93.93%의 정확도를 기록하였습니다.


---

*Generated on 2025-09-23 11:06:44*