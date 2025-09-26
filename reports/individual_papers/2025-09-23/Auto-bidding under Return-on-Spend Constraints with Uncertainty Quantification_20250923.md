---
keywords:
  - Auto-bidding
  - Return-on-Spend
  - Conformal Prediction
  - Machine Learning
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16324
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:34:22.756348",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Auto-bidding",
    "Return-on-Spend",
    "Conformal Prediction",
    "Machine Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Auto-bidding": 0.78,
    "Return-on-Spend": 0.77,
    "Conformal Prediction": 0.8,
    "Machine Learning": 0.85
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Auto-bidding",
        "canonical": "Auto-bidding",
        "aliases": [
          "Automated Bidding",
          "Programmatic Bidding"
        ],
        "category": "unique_technical",
        "rationale": "Auto-bidding is a specific technique in advertising that can be linked to discussions on automated decision-making in marketing.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Return-on-Spend",
        "canonical": "Return-on-Spend",
        "aliases": [
          "RoS",
          "Return on Ad Spend"
        ],
        "category": "unique_technical",
        "rationale": "Return-on-Spend is a key metric in advertising that connects to financial performance analysis.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Conformal Prediction",
        "canonical": "Conformal Prediction",
        "aliases": [
          "Conformal Inference"
        ],
        "category": "specific_connectable",
        "rationale": "Conformal Prediction is a statistical technique that is increasingly relevant in uncertainty quantification.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Machine Learning",
        "canonical": "Machine Learning",
        "aliases": [
          "ML"
        ],
        "category": "broad_technical",
        "rationale": "Machine Learning is a foundational technology for the proposed method and connects to a wide range of related topics.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "value"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Auto-bidding",
      "resolved_canonical": "Auto-bidding",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Return-on-Spend",
      "resolved_canonical": "Return-on-Spend",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Conformal Prediction",
      "resolved_canonical": "Conformal Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Machine Learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    }
  ]
}
-->

# Auto-bidding under Return-on-Spend Constraints with Uncertainty Quantification

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16324.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16324](https://arxiv.org/abs/2509.16324)

## 🔗 유사한 논문
- [[2025-09-22/Enhancing Generative Auto-bidding with Offline Reward Evaluation and Policy Search_20250922|Enhancing Generative Auto-bidding with Offline Reward Evaluation and Policy Search]] (83.8% similar)
- [[2025-09-19/Optimal Type-Dependent Liquid Welfare Guarantees for Autobidding Agents with Budgets_20250919|Optimal Type-Dependent Liquid Welfare Guarantees for Autobidding Agents with Budgets]] (82.9% similar)
- [[2025-09-19/JU-NLP at Touch\'e_ Covert Advertisement in Conversational AI-Generation and Detection Strategies_20250919|JU-NLP at Touch\'e: Covert Advertisement in Conversational AI-Generation and Detection Strategies]] (81.3% similar)
- [[2025-09-22/PVPO_ Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning_20250922|PVPO: Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning]] (79.7% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (79.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**🔗 Specific Connectable**: [[keywords/Conformal Prediction|Conformal Prediction]]
**⚡ Unique Technical**: [[keywords/Auto-bidding|Auto-bidding]], [[keywords/Return-on-Spend|Return-on-Spend]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16324v1 Announce Type: new 
Abstract: Auto-bidding systems are widely used in advertising to automatically determine bid values under constraints such as total budget and Return-on-Spend (RoS) targets. Existing works often assume that the value of an ad impression, such as the conversion rate, is known. This paper considers the more realistic scenario where the true value is unknown. We propose a novel method that uses conformal prediction to quantify the uncertainty of these values based on machine learning methods trained on historical bidding data with contextual features, without assuming the data are i.i.d. This approach is compatible with current industry systems that use machine learning to predict values. Building on prediction intervals, we introduce an adjusted value estimator derived from machine learning predictions, and show that it provides performance guarantees without requiring knowledge of the true value. We apply this method to enhance existing auto-bidding algorithms with budget and RoS constraints, and establish theoretical guarantees for achieving high reward while keeping RoS violations low. Empirical results on both simulated and real-world industrial datasets demonstrate that our approach improves performance while maintaining computational efficiency.

## 📝 요약

이 논문은 광고 자동 입찰 시스템에서 실제 광고 가치를 알 수 없는 상황을 다룹니다. 기존 연구는 광고 노출의 가치를 알고 있다고 가정하지만, 본 연구는 이 가치를 알 수 없다는 현실적인 시나리오를 고려합니다. 저자들은 역사적 입찰 데이터와 문맥적 특징을 활용한 기계 학습 방법을 기반으로, 광고 가치의 불확실성을 정량화하는 새로운 방법을 제안합니다. 이 방법은 현재 산업 시스템과 호환되며, 예측 구간을 기반으로 조정된 가치 추정치를 도입하여 실제 가치를 알지 못해도 성능 보장을 제공합니다. 이 방법을 예산 및 RoS 제약이 있는 기존 자동 입찰 알고리즘에 적용하여 높은 보상을 얻으면서 RoS 위반을 최소화하는 이론적 보장을 확립했습니다. 시뮬레이션 및 실제 산업 데이터셋에 대한 실험 결과, 제안된 방법이 성능을 향상시키면서도 계산 효율성을 유지함을 보여줍니다.

## 🎯 주요 포인트

- 1. 기존의 광고 자동 입찰 시스템은 광고 노출의 가치를 알고 있다고 가정하지만, 본 논문은 실제로 그 가치가 알려지지 않은 상황을 고려합니다.
- 2. 본 연구는 과거 입찰 데이터와 문맥적 특징을 기반으로 한 기계 학습 방법을 사용하여 이러한 가치의 불확실성을 정량화하기 위해 적합 예측을 활용하는 새로운 방법을 제안합니다.
- 3. 제안된 방법은 예측 구간을 기반으로 조정된 가치 추정치를 도입하여, 실제 가치를 알 필요 없이 성능 보장을 제공합니다.
- 4. 이 방법은 예산 및 RoS 제약 조건을 가진 기존 자동 입찰 알고리즘을 개선하는 데 적용되며, 높은 보상을 달성하면서 RoS 위반을 낮게 유지하는 이론적 보장을 확립합니다.
- 5. 시뮬레이션 및 실제 산업 데이터셋에 대한 실험 결과, 제안된 접근 방식이 성능을 향상시키면서도 계산 효율성을 유지함을 보여줍니다.


---

*Generated on 2025-09-24 01:34:22*