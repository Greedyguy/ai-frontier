<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:21:30.943840",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Ridesourcing Mode Choice",
    "Latent Attitudes",
    "Propensity-Score Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.8,
    "Ridesourcing Mode Choice": 0.78,
    "Latent Attitudes": 0.77,
    "Propensity-Score Model": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the SAPA framework, providing a basis for linking with other NLP and AI research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "ridesourcing mode choice",
        "canonical": "Ridesourcing Mode Choice",
        "aliases": [
          "ride-hailing mode choice",
          "ridesharing mode choice"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application area of the SAPA framework, crucial for linking to transportation and urban planning studies.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "latent attitudes",
        "canonical": "Latent Attitudes",
        "aliases": [
          "psychological factors",
          "latent psychological factors"
        ],
        "category": "specific_connectable",
        "rationale": "Latent attitudes are key to understanding user behavior, linking psychological modeling with transportation choices.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "propensity-score model",
        "canonical": "Propensity-Score Model",
        "aliases": [
          "propensity model",
          "score model"
        ],
        "category": "specific_connectable",
        "rationale": "The propensity-score model is a critical component of the SAPA framework, facilitating connections with statistical modeling techniques.",
        "novelty_score": 0.6,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "traffic management policies",
      "multi-year travel survey"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "ridesourcing mode choice",
      "resolved_canonical": "Ridesourcing Mode Choice",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "latent attitudes",
      "resolved_canonical": "Latent Attitudes",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "propensity-score model",
      "resolved_canonical": "Propensity-Score Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# Synthesizing Attitudes, Predicting Actions (SAPA): Behavioral Theory-Guided LLMs for Ridesourcing Mode Choice Modeling

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18181.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18181](https://arxiv.org/abs/2509.18181)

## 🔗 유사한 논문
- [[2025-09-17/ST-LINK_ Spatially-Aware Large Language Models for Spatio-Temporal Forecasting_20250917|ST-LINK: Spatially-Aware Large Language Models for Spatio-Temporal Forecasting]] (81.5% similar)
- [[2025-09-18/CARGO_ A Framework for Confidence-Aware Routing of Large Language Models_20250918|CARGO: A Framework for Confidence-Aware Routing of Large Language Models]] (80.8% similar)
- [[2025-09-23/MSGAT-GRU_ A Multi-Scale Graph Attention and Recurrent Model for Spatiotemporal Road Accident Prediction_20250923|MSGAT-GRU: A Multi-Scale Graph Attention and Recurrent Model for Spatiotemporal Road Accident Prediction]] (80.8% similar)
- [[2025-09-23/STRATA-TS_ Selective Knowledge Transfer for Urban Time Series Forecasting with Retrieval-Guided Reasoning_20250923|STRATA-TS: Selective Knowledge Transfer for Urban Time Series Forecasting with Retrieval-Guided Reasoning]] (80.5% similar)
- [[2025-09-23/Zero-Shot Human Mobility Forecasting via Large Language Model with Hierarchical Reasoning_20250923|Zero-Shot Human Mobility Forecasting via Large Language Model with Hierarchical Reasoning]] (80.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Latent Attitudes|Latent Attitudes]], [[keywords/Propensity-Score Model|Propensity-Score Model]]
**⚡ Unique Technical**: [[keywords/Ridesourcing Mode Choice|Ridesourcing Mode Choice]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18181v1 Announce Type: new 
Abstract: Accurate modeling of ridesourcing mode choices is essential for designing and implementing effective traffic management policies for reducing congestion, improving mobility, and allocating resources more efficiently. Existing models for predicting ridesourcing mode choices often suffer from limited predictive accuracy due to their inability to capture key psychological factors, and are further challenged by severe class imbalance, as ridesourcing trips comprise only a small fraction of individuals' daily travel. To address these limitations, this paper introduces the Synthesizing Attitudes, Predicting Actions (SAPA) framework, a hierarchical approach that uses Large Language Models (LLMs) to synthesize theory-grounded latent attitudes to predict ridesourcing choices. SAPA first uses an LLM to generate qualitative traveler personas from raw travel survey data and then trains a propensity-score model on demographic and behavioral features, enriched by those personas, to produce an individual-level score. Next, the LLM assigns quantitative scores to theory-driven latent variables (e.g., time and cost sensitivity), and a final classifier integrates the propensity score, latent-variable scores (with their interaction terms), and observable trip attributes to predict ridesourcing mode choice. Experiments on a large-scale, multi-year travel survey show that SAPA significantly outperforms state-of-the-art baselines, improving ridesourcing choice predictions by up to 75.9% in terms of PR-AUC on a held-out test set. This study provides a powerful tool for accurately predicting ridesourcing mode choices, and provides a methodology that is readily transferable to various applications.

## 📝 요약

이 논문은 교통 혼잡 완화와 자원 배분 최적화를 위한 효과적인 교통 관리 정책을 설계하는 데 필수적인 라이드소싱 모드 선택의 정확한 모델링을 다룹니다. 기존 모델은 심리적 요인을 충분히 반영하지 못하고 클래스 불균형 문제로 예측 정확도가 제한적입니다. 이를 해결하기 위해, 이 논문은 대형 언어 모델(LLM)을 활용한 SAPA 프레임워크를 제안합니다. SAPA는 여행 설문 데이터를 바탕으로 여행자 페르소나를 생성하고, 인구통계 및 행동 특성을 포함한 성향 점수 모델을 훈련합니다. 그런 다음 이론 기반 잠재 변수에 점수를 부여하고, 최종 분류기는 성향 점수와 잠재 변수 점수, 여행 속성을 통합하여 라이드소싱 모드 선택을 예측합니다. 대규모 여행 설문 실험에서 SAPA는 기존 모델 대비 최대 75.9% 향상된 예측 정확도를 보였습니다. 이 연구는 라이드소싱 모드 선택 예측에 강력한 도구를 제공하며 다양한 응용에 쉽게 적용될 수 있는 방법론을 제시합니다.

## 🎯 주요 포인트

- 1. 효과적인 교통 관리 정책 설계를 위해 승차 공유 모드 선택의 정확한 모델링이 필수적입니다.
- 2. 기존 모델은 심리적 요인을 충분히 반영하지 못하고, 클래스 불균형 문제로 인해 예측 정확도가 제한적입니다.
- 3. SAPA 프레임워크는 대형 언어 모델을 활용하여 이론 기반의 잠재적 태도를 합성하고, 승차 공유 선택을 예측합니다.
- 4. SAPA는 여행 설문 조사 데이터를 바탕으로 여행자 페르소나를 생성하고, 이를 통해 개인 수준의 점수를 산출합니다.
- 5. 대규모 여행 설문 조사 실험에서 SAPA는 기존 최첨단 모델보다 최대 75.9% 향상된 예측 정확도를 보였습니다.


---

*Generated on 2025-09-24 13:21:30*