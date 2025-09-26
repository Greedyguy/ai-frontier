---
keywords:
  - SeqBattNet
  - Neural Network
  - Equivalent Circuit Model
  - HRM-GRU
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17621
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:03:18.986410",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "SeqBattNet",
    "Neural Network",
    "Equivalent Circuit Model",
    "HRM-GRU"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "SeqBattNet": 0.8,
    "Neural Network": 0.75,
    "Equivalent Circuit Model": 0.78,
    "HRM-GRU": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "SeqBattNet",
        "canonical": "SeqBattNet",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "SeqBattNet is a novel discrete-state PINN specifically designed for battery modeling, offering a unique approach with aging adaptation.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Physics-Informed Neural Network",
        "canonical": "Neural Network",
        "aliases": [
          "PINN"
        ],
        "category": "broad_technical",
        "rationale": "Physics-Informed Neural Networks are a subset of neural networks that incorporate physical laws, providing a strong link to existing neural network literature.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Equivalent Circuit Model",
        "canonical": "Equivalent Circuit Model",
        "aliases": [
          "ECM"
        ],
        "category": "specific_connectable",
        "rationale": "The Equivalent Circuit Model is a key component in battery modeling, facilitating connections to other works using ECM in similar contexts.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "HRM-GRU",
        "canonical": "HRM-GRU",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "HRM-GRU is a novel deep learning module proposed in the paper, offering a unique contribution to the field of battery modeling.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "state estimation",
      "benchmark datasets",
      "computational efficiency"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "SeqBattNet",
      "resolved_canonical": "SeqBattNet",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Physics-Informed Neural Network",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Equivalent Circuit Model",
      "resolved_canonical": "Equivalent Circuit Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "HRM-GRU",
      "resolved_canonical": "HRM-GRU",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# SeqBattNet: A Discrete-State Physics-Informed Neural Network with Aging Adaptation for Battery Modeling

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17621.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17621](https://arxiv.org/abs/2509.17621)

## 🔗 유사한 논문
- [[2025-09-22/Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets_20250922|Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets]] (87.0% similar)
- [[2025-09-22/Bayesian Physics Informed Neural Networks for Reliable Transformer Prognostics_20250922|Bayesian Physics Informed Neural Networks for Reliable Transformer Prognostics]] (84.3% similar)
- [[2025-09-22/PBPK-iPINNs_ Inverse Physics-Informed Neural Networks for Physiologically Based Pharmacokinetic Brain Models_20250922|PBPK-iPINNs: Inverse Physics-Informed Neural Networks for Physiologically Based Pharmacokinetic Brain Models]] (81.6% similar)
- [[2025-09-23/ScenGAN_ Attention-Intensive Generative Model for Uncertainty-Aware Renewable Scenario Forecasting_20250923|ScenGAN: Attention-Intensive Generative Model for Uncertainty-Aware Renewable Scenario Forecasting]] (80.8% similar)
- [[2025-09-23/Time Series Forecasting Using a Hybrid Deep Learning Method_ A Bi-LSTM Embedding Denoising Auto Encoder Transformer_20250923|Time Series Forecasting Using a Hybrid Deep Learning Method: A Bi-LSTM Embedding Denoising Auto Encoder Transformer]] (80.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Equivalent Circuit Model|Equivalent Circuit Model]]
**⚡ Unique Technical**: [[keywords/SeqBattNet|SeqBattNet]], [[keywords/HRM-GRU|HRM-GRU]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17621v1 Announce Type: cross 
Abstract: Accurate battery modeling is essential for reliable state estimation in modern applications, such as predicting the remaining discharge time and remaining discharge energy in battery management systems. Existing approaches face several limitations: model-based methods require a large number of parameters; data-driven methods rely heavily on labeled datasets; and current physics-informed neural networks (PINNs) often lack aging adaptation, or still depend on many parameters, or continuously regenerate states. In this work, we propose SeqBattNet, a discrete-state PINN with built-in aging adaptation for battery modeling, to predict terminal voltage during the discharge process. SeqBattNet consists of two components: (i) an encoder, implemented as the proposed HRM-GRU deep learning module, which generates cycle-specific aging adaptation parameters; and (ii) a decoder, based on the equivalent circuit model (ECM) combined with deep learning, which uses these parameters together with the input current to predict voltage. The model requires only three basic battery parameters and, when trained on data from a single cell, still achieves robust performance. Extensive evaluations across three benchmark datasets (TRI, RT-Batt, and NASA) demonstrate that SeqBattNet significantly outperforms classical sequence models and PINN baselines, achieving consistently lower RMSE while maintaining computational efficiency.

## 📝 요약

이 논문에서는 배터리 관리 시스템에서 방전 시간과 에너지를 예측하기 위한 정확한 배터리 모델링을 다룹니다. 기존 방법들은 많은 매개변수나 레이블된 데이터에 의존하거나 노화 적응이 부족한 문제를 가지고 있습니다. 이를 해결하기 위해, 저자들은 노화 적응 기능을 갖춘 이산 상태 물리 정보 신경망(PINN)인 SeqBattNet을 제안합니다. SeqBattNet은 HRM-GRU 모듈을 사용하는 인코더와 등가 회로 모델(ECM) 기반의 디코더로 구성되어 있으며, 세 가지 기본 배터리 매개변수만으로도 강력한 성능을 발휘합니다. TRI, RT-Batt, NASA 데이터셋을 활용한 평가에서 SeqBattNet은 기존 모델들보다 낮은 RMSE를 기록하며 우수한 성능을 입증했습니다.

## 🎯 주요 포인트

- 1. SeqBattNet은 배터리 모델링을 위한 이산 상태의 PINN으로, 내장된 노화 적응 기능을 통해 방전 과정 중 단자 전압을 예측합니다.
- 2. SeqBattNet은 HRM-GRU 딥러닝 모듈로 구현된 인코더와 등가 회로 모델(ECM)과 딥러닝을 결합한 디코더로 구성되어 있습니다.
- 3. 이 모델은 세 가지 기본 배터리 매개변수만 필요로 하며, 단일 셀의 데이터로 훈련되어도 강력한 성능을 발휘합니다.
- 4. TRI, RT-Batt, NASA의 세 가지 벤치마크 데이터셋에서 SeqBattNet은 기존의 시퀀스 모델과 PINN 기반 모델보다 낮은 RMSE를 유지하면서 계산 효율성을 보장합니다.
- 5. SeqBattNet은 사이클별 노화 적응 매개변수를 생성하여, 입력 전류와 함께 전압을 예측하는 데 사용됩니다.


---

*Generated on 2025-09-24 00:03:18*