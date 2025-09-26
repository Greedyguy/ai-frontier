---
keywords:
  - Medical Time Series
  - Continuous-Time Rotary Positional Encoding
  - Neural ODE
  - Zero-Shot Learning
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2506.07584
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:45:37.433110",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Medical Time Series",
    "Continuous-Time Rotary Positional Encoding",
    "Neural ODE",
    "Zero-Shot Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Medical Time Series": 0.78,
    "Continuous-Time Rotary Positional Encoding": 0.77,
    "Neural ODE": 0.82,
    "Zero-Shot Learning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Medical Time Series",
        "canonical": "Medical Time Series",
        "aliases": [
          "Health Time Series",
          "Clinical Time Series"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's focus, enabling connections to health data analysis and forecasting.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Continuous-Time Rotary Positional Encoding",
        "canonical": "Continuous-Time Rotary Positional Encoding",
        "aliases": [
          "CT-RPE"
        ],
        "category": "unique_technical",
        "rationale": "A novel technique introduced in the paper, crucial for handling variable time intervals in medical data.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.77
      },
      {
        "surface": "Neural ODE",
        "canonical": "Neural ODE",
        "aliases": [
          "Neural Ordinary Differential Equations"
        ],
        "category": "specific_connectable",
        "rationale": "A key component in modeling continuous trajectories, linking to advanced neural network methods.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Zero-Shot Learning",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "ZSL"
        ],
        "category": "specific_connectable",
        "rationale": "Relevant for understanding model performance in unseen scenarios, connecting to transfer learning.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "foundation model",
      "forecasting errors",
      "benchmark"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Medical Time Series",
      "resolved_canonical": "Medical Time Series",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Continuous-Time Rotary Positional Encoding",
      "resolved_canonical": "Continuous-Time Rotary Positional Encoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Neural ODE",
      "resolved_canonical": "Neural ODE",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Zero-Shot Learning",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# MIRA: Medical Time Series Foundation Model for Real-World Health Data

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2506.07584.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2506.07584](https://arxiv.org/abs/2506.07584)

## 🔗 유사한 논문
- [[2025-09-23/Multi-View Contrastive Learning for Robust Domain Adaptation in Medical Time Series Analysis_20250923|Multi-View Contrastive Learning for Robust Domain Adaptation in Medical Time Series Analysis]] (83.7% similar)
- [[2025-09-19/Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation_20250919|Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation]] (82.9% similar)
- [[2025-09-22/Multi-modal Adaptive Estimation for Temporal Respiratory Disease Outbreak_20250922|Multi-modal Adaptive Estimation for Temporal Respiratory Disease Outbreak]] (82.6% similar)
- [[2025-09-23/A Unified AI Approach for Continuous Monitoring of Human Health and Diseases from Intensive Care Unit to Home with Physiological Foundation Models (UNIPHY+)_20250923|A Unified AI Approach for Continuous Monitoring of Human Health and Diseases from Intensive Care Unit to Home with Physiological Foundation Models (UNIPHY+)]] (82.2% similar)
- [[2025-09-22/NeuroRAD-FM_ A Foundation Model for Neuro-Oncology with Distributionally Robust Training_20250922|NeuroRAD-FM: A Foundation Model for Neuro-Oncology with Distributionally Robust Training]] (82.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Neural ODE|Neural ODE]], [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Medical Time Series|Medical Time Series]], [[keywords/Continuous-Time Rotary Positional Encoding|Continuous-Time Rotary Positional Encoding]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.07584v4 Announce Type: replace 
Abstract: A unified foundation model for medical time series -- pretrained on open access and ethics board-approved medical corpora -- offers the potential to reduce annotation burdens, minimize model customization, and enable robust transfer across clinical institutions, modalities, and tasks, particularly in data-scarce or privacy-constrained environments. However, existing generalist time series foundation models struggle to handle medical time series data due to their inherent challenges, including irregular intervals, heterogeneous sampling rates, and frequent missing values. To address these challenges, we introduce MIRA, a unified foundation model specifically designed for medical time series forecasting. MIRA incorporates a Continuous-Time Rotary Positional Encoding that enables fine-grained modeling of variable time intervals, a frequency-specific mixture-of-experts layer that routes computation across latent frequency regimes to further promote temporal specialization, and a Continuous Dynamics Extrapolation Block based on Neural ODE that models the continuous trajectory of latent states, enabling accurate forecasting at arbitrary target timestamps. Pretrained on a large-scale and diverse medical corpus comprising over 454 billion time points collect from publicly available datasets, MIRA achieves reductions in forecasting errors by an average of 10% and 7% in out-of-distribution and in-distribution scenarios, respectively, when compared to other zero-shot and fine-tuned baselines. We also introduce a comprehensive benchmark spanning multiple downstream clinical tasks, establishing a foundation for future research in medical time series modeling.

## 📝 요약

이 논문은 의료 시계열 데이터를 위한 통합 기초 모델인 MIRA를 제안합니다. MIRA는 불규칙한 간격, 이질적인 샘플링 속도, 결측치 등 기존 모델이 처리하기 어려운 의료 시계열의 문제를 해결하고자 설계되었습니다. 이를 위해 연속 시간 회전 위치 인코딩, 주파수별 전문가 혼합 레이어, 신경 ODE 기반 연속 동적 외삽 블록을 도입하여 정밀한 시간 간격 모델링과 정확한 예측을 가능하게 합니다. 4540억 개 이상의 시계열 데이터로 사전 학습된 MIRA는 기존 모델 대비 예측 오류를 평균 10% 감소시켰습니다. 이 연구는 다양한 임상 과제를 아우르는 벤치마크를 제시하여 의료 시계열 모델링의 미래 연구 기반을 마련합니다.

## 🎯 주요 포인트

- 1. MIRA는 의료 시계열 예측을 위해 설계된 통합 기초 모델로, 불규칙한 간격, 이질적인 샘플링 속도, 빈번한 결측값 등 의료 시계열 데이터의 고유한 문제를 해결합니다.
- 2. MIRA는 연속 시간 회전 위치 인코딩을 통해 가변 시간 간격의 세밀한 모델링을 가능하게 하며, 주파수별 전문가 혼합 레이어를 통해 시간적 전문화를 촉진합니다.
- 3. Neural ODE 기반의 연속 역학 외삽 블록을 사용하여 잠재 상태의 연속 궤적을 모델링함으로써 임의의 목표 타임스탬프에서 정확한 예측을 가능하게 합니다.
- 4. MIRA는 4540억 개 이상의 시계열 데이터를 포함한 대규모 의료 코퍼스에서 사전 학습되어, 기존의 제로샷 및 미세 조정된 기준 모델 대비 평균 10% 및 7%의 예측 오류 감소를 달성했습니다.
- 5. 다양한 임상 작업을 아우르는 포괄적인 벤치마크를 소개하여, 의료 시계열 모델링 분야의 미래 연구를 위한 기초를 마련했습니다.


---

*Generated on 2025-09-24 02:45:37*