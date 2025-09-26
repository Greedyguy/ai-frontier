---
keywords:
  - Channel Imposed Fusion
  - Temporal Convolutional Network
  - Electroencephalogram
  - Electrocardiogram
  - Transformer
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2506.00337
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:09:01.708970",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Channel Imposed Fusion",
    "Temporal Convolutional Network",
    "Electroencephalogram",
    "Electrocardiogram",
    "Transformer"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Channel Imposed Fusion": 0.8,
    "Temporal Convolutional Network": 0.82,
    "Electroencephalogram": 0.78,
    "Electrocardiogram": 0.78,
    "Transformer": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Channel Imposed Fusion",
        "canonical": "Channel Imposed Fusion",
        "aliases": [
          "CIF"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel method specific to the paper, enhancing signal processing in medical time series.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Temporal Convolutional Network",
        "canonical": "Temporal Convolutional Network",
        "aliases": [
          "TCN"
        ],
        "category": "specific_connectable",
        "rationale": "A well-known architecture that is integral to the proposed method, facilitating connections with related neural network models.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Electroencephalogram",
        "canonical": "Electroencephalogram",
        "aliases": [
          "EEG"
        ],
        "category": "specific_connectable",
        "rationale": "A primary data type used in the study, linking to broader medical signal processing research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "Electrocardiogram",
        "canonical": "Electrocardiogram",
        "aliases": [
          "ECG"
        ],
        "category": "specific_connectable",
        "rationale": "Another key data type analyzed, relevant for connections in medical diagnostics.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Provides context on the limitations of existing models, linking to a wide range of machine learning applications.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "classification",
      "performance",
      "method"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Channel Imposed Fusion",
      "resolved_canonical": "Channel Imposed Fusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Temporal Convolutional Network",
      "resolved_canonical": "Temporal Convolutional Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Electroencephalogram",
      "resolved_canonical": "Electroencephalogram",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Electrocardiogram",
      "resolved_canonical": "Electrocardiogram",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Channel-Imposed Fusion: A Simple yet Effective Method for Medical Time Series Classification

**Korean Title:** 채널 부과 융합: 의료 시계열 분류를 위한 간단하면서도 효과적인 방법

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2506.00337.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2506.00337](https://arxiv.org/abs/2506.00337)

## 🔗 유사한 논문
- [[2025-09-22/IEFS-GMB_ Gradient Memory Bank-Guided Feature Selection Based on Information Entropy for EEG Classification of Neurological Disorders_20250922|IEFS-GMB: Gradient Memory Bank-Guided Feature Selection Based on Information Entropy for EEG Classification of Neurological Disorders]] (83.9% similar)
- [[2025-09-18/Explaining deep learning for ECG using time-localized clusters_20250918|Explaining deep learning for ECG using time-localized clusters]] (83.5% similar)
- [[2025-09-18/Multimodal signal fusion for stress detection using deep neural networks_ a novel approach for converting 1D signals to unified 2D images_20250918|Multimodal signal fusion for stress detection using deep neural networks: a novel approach for converting 1D signals to unified 2D images]] (81.8% similar)
- [[2025-09-22/No Black Box Anymore_ Demystifying Clinical Predictive Modeling with Temporal-Feature Cross Attention Mechanism_20250922|No Black Box Anymore: Demystifying Clinical Predictive Modeling with Temporal-Feature Cross Attention Mechanism]] (81.5% similar)
- [[2025-09-22/DAFTED_ Decoupled Asymmetric Fusion of Tabular and Echocardiographic Data for Cardiac Hypertension Diagnosis_20250922|DAFTED: Decoupled Asymmetric Fusion of Tabular and Echocardiographic Data for Cardiac Hypertension Diagnosis]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Temporal Convolutional Network|Temporal Convolutional Network]], [[keywords/Electroencephalogram|Electroencephalogram]], [[keywords/Electrocardiogram|Electrocardiogram]]
**⚡ Unique Technical**: [[keywords/Channel Imposed Fusion|Channel Imposed Fusion]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.00337v2 Announce Type: replace 
Abstract: The automatic classification of medical time series signals, such as electroencephalogram (EEG) and electrocardiogram (ECG), plays a pivotal role in clinical decision support and early detection of diseases. Although Transformer based models have achieved notable performance by implicitly modeling temporal dependencies through self-attention mechanisms, their inherently complex architectures and opaque reasoning processes undermine their trustworthiness in high stakes clinical settings. In response to these limitations, this study shifts focus toward a modeling paradigm that emphasizes structural transparency, aligning more closely with the intrinsic characteristics of medical data. We propose a novel method, Channel Imposed Fusion (CIF), which enhances the signal-to-noise ratio through cross-channel information fusion, effectively reduces redundancy, and improves classification performance. Furthermore, we integrate CIF with the Temporal Convolutional Network (TCN), known for its structural simplicity and controllable receptive field, to construct an efficient and explicit classification framework. Experimental results on multiple publicly available EEG and ECG datasets demonstrate that the proposed method not only outperforms existing state-of-the-art (SOTA) approaches in terms of various classification metrics, but also significantly enhances the transparency of the classification process, offering a novel perspective for medical time series classification.

## 🔍 Abstract (한글 번역)

arXiv:2506.00337v2 발표 유형: 교체  
초록: 뇌전도(EEG) 및 심전도(ECG)와 같은 의료 시계열 신호의 자동 분류는 임상 의사 결정 지원 및 질병의 조기 발견에 중요한 역할을 합니다. Transformer 기반 모델은 자기 주의 메커니즘을 통해 시간적 종속성을 암묵적으로 모델링함으로써 주목할 만한 성과를 거두었지만, 본질적으로 복잡한 아키텍처와 불투명한 추론 과정은 고위험 임상 환경에서 신뢰성을 저해합니다. 이러한 한계에 대응하여, 본 연구는 의료 데이터의 내재적 특성과 더 밀접하게 일치하는 구조적 투명성을 강조하는 모델링 패러다임으로 초점을 전환합니다. 우리는 채널 부가 융합(Channel Imposed Fusion, CIF)이라는 새로운 방법을 제안하여, 교차 채널 정보 융합을 통해 신호 대 잡음 비율을 향상시키고, 중복성을 효과적으로 줄이며, 분류 성능을 개선합니다. 또한, 구조적 단순성과 제어 가능한 수용 영역으로 알려진 시간적 합성곱 네트워크(Temporal Convolutional Network, TCN)와 CIF를 통합하여 효율적이고 명시적인 분류 프레임워크를 구축합니다. 여러 공개 EEG 및 ECG 데이터셋에 대한 실험 결과는 제안된 방법이 다양한 분류 지표 측면에서 기존 최첨단(SOTA) 접근 방식을 능가할 뿐만 아니라, 분류 과정의 투명성을 크게 향상시켜 의료 시계열 분류에 대한 새로운 관점을 제공합니다.

## 📝 요약

이 연구는 의료 시계열 신호인 EEG와 ECG의 자동 분류를 개선하기 위해 새로운 방법론을 제안합니다. 기존의 Transformer 기반 모델은 성능은 뛰어나지만 복잡한 구조와 불투명한 추론 과정으로 인해 임상 환경에서의 신뢰성이 떨어집니다. 이를 해결하기 위해, 연구진은 구조적 투명성을 강조하는 모델링 패러다임으로 전환하였습니다. 제안된 방법인 Channel Imposed Fusion (CIF)은 채널 간 정보 융합을 통해 신호 대 잡음비를 향상시키고 중복성을 줄여 분류 성능을 개선합니다. 또한, CIF를 구조가 간단하고 수용 범위가 조절 가능한 Temporal Convolutional Network (TCN)와 결합하여 효율적이고 명확한 분류 프레임워크를 구축했습니다. 여러 공개 EEG 및 ECG 데이터셋에 대한 실험 결과, 제안된 방법은 기존 최첨단 접근법보다 뛰어난 분류 성능을 보였으며, 분류 과정의 투명성을 크게 향상시켰습니다.

## 🎯 주요 포인트

- 1. 의료 시계열 신호의 자동 분류는 임상 결정 지원과 질병의 조기 발견에 중요한 역할을 합니다.
- 2. Transformer 기반 모델은 성능이 뛰어나지만, 복잡한 구조와 불투명한 추론 과정으로 인해 임상 환경에서의 신뢰성이 떨어집니다.
- 3. 본 연구는 구조적 투명성을 강조하는 모델링 패러다임을 제안하며, 의료 데이터의 특성과 더 잘 맞도록 설계되었습니다.
- 4. 제안된 Channel Imposed Fusion (CIF) 방법은 채널 간 정보 융합을 통해 신호 대 잡음 비율을 개선하고, 중복성을 줄이며 분류 성능을 향상시킵니다.
- 5. CIF와 Temporal Convolutional Network (TCN)를 결합하여 명확하고 효율적인 분류 프레임워크를 구축하였으며, 이는 기존 최첨단 방법보다 뛰어난 성능과 투명성을 제공합니다.


---

*Generated on 2025-09-23 11:09:01*