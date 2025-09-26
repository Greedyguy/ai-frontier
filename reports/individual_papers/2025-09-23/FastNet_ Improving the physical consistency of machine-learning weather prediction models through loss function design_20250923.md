---
keywords:
  - Graph Neural Network
  - Machine Learning Weather Prediction
  - Modified Spherical Harmonic Loss
  - Physical Consistency
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17601
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:24:14.732588",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Machine Learning Weather Prediction",
    "Modified Spherical Harmonic Loss",
    "Physical Consistency"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.88,
    "Machine Learning Weather Prediction": 0.82,
    "Modified Spherical Harmonic Loss": 0.79,
    "Physical Consistency": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph Neural Network",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Neural Networks are central to the study and provide a strong link to other works in machine learning and weather prediction.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "Machine Learning Weather Prediction",
        "canonical": "Machine Learning Weather Prediction",
        "aliases": [
          "MLWP"
        ],
        "category": "unique_technical",
        "rationale": "This specific application of machine learning is crucial for understanding the paper's focus on improving weather prediction models.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Modified Spherical Harmonic Loss",
        "canonical": "Modified Spherical Harmonic Loss",
        "aliases": [
          "MSH Loss"
        ],
        "category": "unique_technical",
        "rationale": "This novel loss function is a key innovation in the paper, enhancing the physical realism of predictions.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.79
      },
      {
        "surface": "Physical Consistency",
        "canonical": "Physical Consistency",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Ensuring physical consistency is a fundamental challenge addressed in the paper, linking it to broader discussions in model accuracy.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "loss function",
      "model",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph Neural Network",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Machine Learning Weather Prediction",
      "resolved_canonical": "Machine Learning Weather Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Modified Spherical Harmonic Loss",
      "resolved_canonical": "Modified Spherical Harmonic Loss",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Physical Consistency",
      "resolved_canonical": "Physical Consistency",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# FastNet: Improving the physical consistency of machine-learning weather prediction models through loss function design

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17601.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17601](https://arxiv.org/abs/2509.17601)

## 🔗 유사한 논문
- [[2025-09-22/Communications to Circulations_ 3D Wind Field Retrieval and Real-Time Prediction Using 5G GNSS Signals and Deep Learning_20250922|Communications to Circulations: 3D Wind Field Retrieval and Real-Time Prediction Using 5G GNSS Signals and Deep Learning]] (82.5% similar)
- [[2025-09-22/Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets_20250922|Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets]] (81.2% similar)
- [[2025-09-17/Deep Temporal Graph Networks for Real-Time Correction of GNSS Jamming-Induced Deviations_20250917|Deep Temporal Graph Networks for Real-Time Correction of GNSS Jamming-Induced Deviations]] (81.1% similar)
- [[2025-09-17/A Neural Network for the Identical Kuramoto Equation_ Architectural Considerations and Performance Evaluation_20250917|A Neural Network for the Identical Kuramoto Equation: Architectural Considerations and Performance Evaluation]] (81.1% similar)
- [[2025-09-17/An End-to-End Differentiable, Graph Neural Network-Embedded Pore Network Model for Permeability Prediction_20250917|An End-to-End Differentiable, Graph Neural Network-Embedded Pore Network Model for Permeability Prediction]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Physical Consistency|Physical Consistency]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Machine Learning Weather Prediction|Machine Learning Weather Prediction]], [[keywords/Modified Spherical Harmonic Loss|Modified Spherical Harmonic Loss]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17601v1 Announce Type: cross 
Abstract: Machine learning weather prediction (MLWP) models have demonstrated remarkable potential in delivering accurate forecasts at significantly reduced computational cost compared to traditional numerical weather prediction (NWP) systems. However, challenges remain in ensuring the physical consistency of MLWP outputs, particularly in deterministic settings. This study presents FastNet, a graph neural network (GNN)-based global prediction model, and investigates the impact of alternative loss function designs on improving the physical realism of its forecasts. We explore three key modifications to the standard mean squared error (MSE) loss: (1) a modified spherical harmonic (MSH) loss that penalises spectral amplitude errors to reduce blurring and enhance small-scale structure retention; (2) inclusion of horizontal gradient terms in the loss to suppress non-physical artefacts; and (3) an alternative wind representation that decouples speed and direction to better capture extreme wind events. Results show that while the MSH and gradient-based losses \textit{alone} may slightly degrade RMSE scores, when trained in combination the model exhibits very similar MSE performance to an MSE-trained model while at the same time significantly improving spectral fidelity and physical consistency. The alternative wind representation further improves wind speed accuracy and reduces directional bias. Collectively, these findings highlight the importance of loss function design as a mechanism for embedding domain knowledge into MLWP models and advancing their operational readiness.

## 📝 요약

이 연구는 기계 학습 기반의 기상 예측 모델인 FastNet을 소개하며, 그래프 신경망(GNN)을 활용해 전통적인 수치 예보 시스템보다 낮은 계산 비용으로 정확한 예측을 제공합니다. 주요 기여는 물리적 일관성을 개선하기 위한 손실 함수 설계의 대안적 접근입니다. 세 가지 주요 수정 사항을 제안했는데, 이는 (1) 스펙트럼 진폭 오류를 줄여 작은 규모의 구조를 유지하는 수정된 구형 조화(MSH) 손실, (2) 비물리적 인공물을 억제하기 위한 수평 기울기 항목의 포함, (3) 풍속과 방향을 분리하여 극한 바람 사건을 더 잘 포착하는 대체 바람 표현입니다. 연구 결과, MSH와 기울기 기반 손실이 단독으로는 RMSE 점수를 약간 저하시킬 수 있지만, 결합하여 훈련할 경우 MSE 성능을 유지하면서도 스펙트럼 충실도와 물리적 일관성을 크게 개선했습니다. 대체 바람 표현은 풍속 정확성을 높이고 방향 편향을 줄였습니다. 이러한 결과는 손실 함수 설계가 기상 예측 모델에 도메인 지식을 내재화하고 운영 준비성을 향상시키는 중요한 메커니즘임을 강조합니다.

## 🎯 주요 포인트

- 1. FastNet은 그래프 신경망(GNN) 기반의 글로벌 예측 모델로, 물리적 일관성을 개선하기 위해 대체 손실 함수 설계를 탐구합니다.
- 2. 수정된 구면 고조파(MSH) 손실은 스펙트럼 진폭 오류를 줄여 흐림을 감소시키고 소규모 구조 보존을 강화합니다.
- 3. 손실 함수에 수평 기울기 항목을 포함하여 비물리적 인공물을 억제합니다.
- 4. 속도와 방향을 분리한 대체 바람 표현은 극단적인 바람 사건을 더 잘 포착하고 바람 속도 정확성을 향상시킵니다.
- 5. 손실 함수 설계는 MLWP 모델에 도메인 지식을 내재화하고 운영 준비를 향상시키는 데 중요합니다.


---

*Generated on 2025-09-24 02:24:14*