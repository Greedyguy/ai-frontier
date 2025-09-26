---
keywords:
  - Neural Network
  - Engine Ageing Effects
  - Fuel Flow Prediction
  - Airbus A320-214
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15736
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:33:11.114000",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Engine Ageing Effects",
    "Fuel Flow Prediction",
    "Airbus A320-214"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.85,
    "Engine Ageing Effects": 0.78,
    "Fuel Flow Prediction": 0.8,
    "Airbus A320-214": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural Network",
        "canonical": "Neural Network",
        "aliases": [
          "NN",
          "neural nets"
        ],
        "category": "broad_technical",
        "rationale": "Neural networks are a key method used in the paper for modeling fuel flow, providing a strong link to machine learning frameworks.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Engine Ageing Effects",
        "canonical": "Engine Ageing Effects",
        "aliases": [
          "engine deterioration",
          "age-related performance"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's focus on improving fuel flow predictions, offering a unique perspective on aircraft performance modeling.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Fuel Flow Prediction",
        "canonical": "Fuel Flow Prediction",
        "aliases": [
          "fuel consumption modeling",
          "fuel usage estimation"
        ],
        "category": "unique_technical",
        "rationale": "The paper's primary objective is to enhance the accuracy of fuel flow predictions, making it a pivotal concept for linking related research.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Airbus A320-214",
        "canonical": "Airbus A320-214",
        "aliases": [
          "A320",
          "Airbus A320"
        ],
        "category": "specific_connectable",
        "rationale": "The specific aircraft model used in the study provides a concrete example for linking to other aerospace studies.",
        "novelty_score": 0.6,
        "connectivity_score": 0.72,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "operational planning",
      "environmental impact assessment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural Network",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Engine Ageing Effects",
      "resolved_canonical": "Engine Ageing Effects",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Fuel Flow Prediction",
      "resolved_canonical": "Fuel Flow Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Airbus A320-214",
      "resolved_canonical": "Airbus A320-214",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.72,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Aircraft Fuel Flow Modelling with Ageing Effects: From Parametric Corrections to Neural Networks

**Korean Title:** 항공기 연료 흐름 모델링의 노화 효과: 매개변수 보정에서 신경망까지

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15736.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15736](https://arxiv.org/abs/2509.15736)

## 🔗 유사한 논문
- [[2025-09-22/Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets_20250922|Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets]] (79.3% similar)
- [[2025-09-22/Improving the forecast accuracy of wind power by leveraging multiple hierarchical structure_20250922|Improving the forecast accuracy of wind power by leveraging multiple hierarchical structure]] (77.2% similar)
- [[2025-09-22/Bayesian Physics Informed Neural Networks for Reliable Transformer Prognostics_20250922|Bayesian Physics Informed Neural Networks for Reliable Transformer Prognostics]] (76.7% similar)
- [[2025-09-22/Partial Column Generation with Graph Neural Networks for Team Formation and Routing_20250922|Partial Column Generation with Graph Neural Networks for Team Formation and Routing]] (76.7% similar)
- [[2025-09-18/FlowCast-ODE_ Continuous Hourly Weather Forecasting with Dynamic Flow Matching and ODE Integration_20250918|FlowCast-ODE: Continuous Hourly Weather Forecasting with Dynamic Flow Matching and ODE Integration]] (76.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Airbus A320-214|Airbus A320-214]]
**⚡ Unique Technical**: [[keywords/Engine Ageing Effects|Engine Ageing Effects]], [[keywords/Fuel Flow Prediction|Fuel Flow Prediction]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15736v1 Announce Type: new 
Abstract: Accurate modelling of aircraft fuel-flow is crucial for both operational planning and environmental impact assessment, yet standard parametric models often neglect performance deterioration that occurs as aircraft age. This paper investigates multiple approaches to integrate engine ageing effects into fuel-flow prediction for the Airbus A320-214, using a comprehensive dataset of approximately nineteen thousand Quick Access Recorder flights from nine distinct airframes with varying years in service. We systematically evaluate classical physics-based models, empirical correction coefficients, and data-driven neural network architectures that incorporate age either as an input feature or as an explicit multiplicative bias. Results demonstrate that while baseline models consistently underestimate fuel consumption for older aircraft, the use of age-dependent correction factors and neural models substantially reduces bias and improves prediction accuracy. Nevertheless, limitations arise from the small number of airframes and the lack of detailed maintenance event records, which constrain the representativeness and generalization of age-based corrections. This study emphasizes the importance of accounting for the effects of ageing in parametric and machine learning frameworks to improve the reliability of operational and environmental assessments. The study also highlights the need for more diverse datasets that can capture the complexity of real-world engine deterioration.

## 🔍 Abstract (한글 번역)

arXiv:2509.15736v1 발표 유형: 신규  
초록: 항공기 연료 흐름의 정확한 모델링은 운영 계획 및 환경 영향 평가에 필수적이지만, 표준 파라메트릭 모델은 항공기가 노후화됨에 따라 발생하는 성능 저하를 종종 간과합니다. 본 논문은 약 19,000회의 퀵 액세스 레코더 비행 데이터를 사용하여, 서비스 연수가 다양한 9개의 서로 다른 기체에 대해 Airbus A320-214의 연료 흐름 예측에 엔진 노후화 효과를 통합하는 여러 접근 방식을 조사합니다. 우리는 고전적인 물리 기반 모델, 경험적 보정 계수, 그리고 나이를 입력 특징으로 또는 명시적인 곱셈 편향으로 통합하는 데이터 기반 신경망 아키텍처를 체계적으로 평가합니다. 결과는 기본 모델이 오래된 항공기의 연료 소비를 일관되게 과소평가하는 반면, 나이 의존적 보정 계수와 신경망 모델의 사용이 편향을 상당히 줄이고 예측 정확성을 향상시킨다는 것을 보여줍니다. 그럼에도 불구하고, 기체 수의 제한과 상세한 유지보수 이벤트 기록의 부족은 나이 기반 보정의 대표성과 일반화를 제한합니다. 본 연구는 운영 및 환경 평가의 신뢰성을 향상시키기 위해 파라메트릭 및 기계 학습 프레임워크에서 노후화 효과를 고려하는 것의 중요성을 강조합니다. 또한, 실제 엔진 열화의 복잡성을 포착할 수 있는 보다 다양한 데이터 세트의 필요성을 강조합니다.

## 📝 요약

이 논문은 항공기 연료 소모 예측에서 엔진 노후화의 영향을 통합하는 방법을 연구합니다. Airbus A320-214의 약 19,000회 비행 데이터를 활용하여, 물리 기반 모델, 경험적 보정 계수, 나이 정보를 포함한 데이터 기반 신경망 모델을 평가했습니다. 연구 결과, 기존 모델은 노후 항공기의 연료 소모를 과소평가하는 경향이 있지만, 나이 의존 보정 요소와 신경망 모델을 사용하면 예측 정확도가 향상됨을 확인했습니다. 그러나 소수의 항공기 데이터와 유지보수 기록 부족이 한계로 작용했습니다. 이 연구는 노후화 효과를 고려한 모델링의 중요성을 강조하며, 보다 다양한 데이터셋의 필요성을 제기합니다.

## 🎯 주요 포인트

- 1. 항공기 연료 소모 예측 모델에서 노후화에 따른 성능 저하를 고려하는 것이 중요하다.
- 2. Airbus A320-214의 연료 소모 예측을 위해 다양한 방법론을 사용하여 엔진 노후화 효과를 통합하였다.
- 3. 연령에 따른 보정 계수와 신경망 모델을 사용하면 예측 정확성이 크게 향상된다.
- 4. 소수의 기체와 유지보수 이벤트 기록 부족으로 인해 연령 기반 보정의 일반화에 한계가 있다.
- 5. 노후화 효과를 고려한 다양한 데이터셋의 필요성을 강조하였다.


---

*Generated on 2025-09-23 10:33:11*