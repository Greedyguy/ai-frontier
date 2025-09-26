---
keywords:
  - Deep Learning
  - Neural Network
  - Human Connectome Project
  - Resting-state and Movie-watching
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16973
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:17:53.336626",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Neural Network",
    "Human Connectome Project",
    "Resting-state and Movie-watching"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Neural Network": 0.9,
    "Human Connectome Project": 0.8,
    "Resting-state and Movie-watching": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [
          "DL"
        ],
        "category": "broad_technical",
        "rationale": "Deep Learning is a central theme of the paper, connecting with various neural network architectures discussed.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "Convolutional Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "CNN",
          "Convolutional Networks"
        ],
        "category": "specific_connectable",
        "rationale": "CNNs are highlighted as the most effective model for the classification task, providing a strong link to neural network discussions.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.9
      },
      {
        "surface": "Human Connectome Project",
        "canonical": "Human Connectome Project",
        "aliases": [
          "HCP"
        ],
        "category": "unique_technical",
        "rationale": "The dataset used is specific to the Human Connectome Project, which is crucial for understanding the study's context.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Resting-state and Movie-watching",
        "canonical": "Resting-state and Movie-watching",
        "aliases": [
          "Resting-state",
          "Movie-watching"
        ],
        "category": "unique_technical",
        "rationale": "These conditions are key experimental settings in the study, relevant for linking to similar fMRI studies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "biological sex classification",
      "functional patterns"
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
      "candidate_surface": "Convolutional Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Human Connectome Project",
      "resolved_canonical": "Human Connectome Project",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Resting-state and Movie-watching",
      "resolved_canonical": "Resting-state and Movie-watching",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Deep Learning Inductive Biases for fMRI Time Series Classification during Resting-state and Movie-watching

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16973.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16973](https://arxiv.org/abs/2509.16973)

## 🔗 유사한 논문
- [[2025-09-17/Exploring the Relationship between Brain Hemisphere States and Frequency Bands through Deep Learning Optimization Techniques_20250917|Exploring the Relationship between Brain Hemisphere States and Frequency Bands through Deep Learning Optimization Techniques]] (85.0% similar)
- [[2025-09-23/Mental Multi-class Classification on Social Media_ Benchmarking Transformer Architectures against LSTM Models_20250923|Mental Multi-class Classification on Social Media: Benchmarking Transformer Architectures against LSTM Models]] (82.3% similar)
- [[2025-09-19/Brain-HGCN_ A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis_20250919|Brain-HGCN: A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis]] (82.2% similar)
- [[2025-09-22/Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images_20250922|Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images]] (81.0% similar)
- [[2025-09-22/Channel-Imposed Fusion_ A Simple yet Effective Method for Medical Time Series Classification_20250922|Channel-Imposed Fusion: A Simple yet Effective Method for Medical Time Series Classification]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Neural Network|Neural Network]]
**⚡ Unique Technical**: [[keywords/Human Connectome Project|Human Connectome Project]], [[keywords/Resting-state and Movie-watching|Resting-state and Movie-watching]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16973v1 Announce Type: cross 
Abstract: Deep learning has advanced fMRI analysis, yet it remains unclear which architectural inductive biases are most effective at capturing functional patterns in human brain activity. This issue is particularly important in small-sample settings, as most datasets fall into this category. We compare models with three major inductive biases in deep learning including convolutional neural networks (CNNs), long short-term memory networks (LSTMs), and Transformers for the task of biological sex classification. These models are evaluated within a unified pipeline using parcellated multivariate fMRI time series from the Human Connectome Project (HCP) 7-Tesla cohort, which includes four resting-state runs and four movie-watching task runs. We assess performance on Whole-brain, subcortex, and 12 functional networks. CNNs consistently achieved the highest discrimination for sex classification in both resting-state and movie-watching, while LSTM and Transformer models underperformed. Network-resolved analyses indicated that the Whole-brain, Default Mode, Cingulo-Opercular, Dorsal Attention, and Frontoparietal networks were the most discriminative. These results were largely similar between resting-state and movie-watching. Our findings indicate that, at this dataset size, discriminative information is carried by local spatial patterns and inter-regional dependencies, favoring convolutional inductive bias. Our study provides insights for selecting deep learning architectures for fMRI time series classification.

## 📝 요약

이 논문은 fMRI 분석에서 효과적인 딥러닝 구조적 편향을 조사하며, 특히 소규모 샘플 환경에서의 성능을 평가합니다. 생물학적 성별 분류 작업을 위해 CNN, LSTM, Transformer 모델을 비교하였으며, Human Connectome Project의 7-Tesla 데이터를 사용했습니다. CNN은 휴식 상태와 영화 감상 모두에서 가장 높은 분류 성능을 보였고, LSTM과 Transformer는 상대적으로 낮은 성능을 보였습니다. 전체 뇌, 기본 모드, Cingulo-Opercular, Dorsal Attention, Frontoparietal 네트워크가 특히 분류에 유리했습니다. 연구 결과, 이 데이터셋 크기에서는 지역적 공간 패턴과 지역 간 의존성이 중요한 정보임을 보여주며, CNN의 구조적 편향이 유리함을 시사합니다. 이 연구는 fMRI 시계열 분류를 위한 딥러닝 아키텍처 선택에 대한 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. 딥러닝 모델 중 CNN이 fMRI 데이터에서 성별 분류에 가장 효과적임을 확인했습니다.
- 2. LSTM과 Transformer 모델은 CNN에 비해 성별 분류 성능이 떨어졌습니다.
- 3. 전체 뇌, 기본 모드, Cingulo-Opercular, Dorsal Attention, Frontoparietal 네트워크가 성별 분류에 가장 유리한 네트워크로 나타났습니다.
- 4. 휴식 상태와 영화 시청 상태 모두에서 유사한 결과가 관찰되었습니다.
- 5. 데이터셋 크기에서는 지역적 공간 패턴과 지역 간 종속성이 중요한 정보임을 시사합니다.


---

*Generated on 2025-09-24 02:17:53*