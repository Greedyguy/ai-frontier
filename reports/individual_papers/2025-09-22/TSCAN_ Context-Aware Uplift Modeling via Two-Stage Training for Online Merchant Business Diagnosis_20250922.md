---
keywords:
  - Attention Mechanism
  - Two-Stage Training
  - Uplift Modeling
  - Integral Probability Metrics
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2504.18881
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:07:31.482886",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Attention Mechanism",
    "Two-Stage Training",
    "Uplift Modeling",
    "Integral Probability Metrics"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Attention Mechanism": 0.85,
    "Two-Stage Training": 0.72,
    "Uplift Modeling": 0.78,
    "Integral Probability Metrics": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Context-Aware Attention Layer",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Contextual Attention"
        ],
        "category": "specific_connectable",
        "rationale": "The Context-Aware Attention Layer is a specialized form of attention mechanism, which is a key concept in linking various models and techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.85
      },
      {
        "surface": "Two-Stage Training",
        "canonical": "Two-Stage Training",
        "aliases": [
          "Two-Phase Training"
        ],
        "category": "unique_technical",
        "rationale": "This approach is central to the paper's methodology and offers a unique perspective on training models, enhancing its novelty.",
        "novelty_score": 0.65,
        "connectivity_score": 0.67,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      },
      {
        "surface": "Uplift Modeling",
        "canonical": "Uplift Modeling",
        "aliases": [
          "Uplift Model"
        ],
        "category": "unique_technical",
        "rationale": "Uplift modeling is a specialized technique in causal inference, important for linking to related studies in treatment effect estimation.",
        "novelty_score": 0.61,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Integral Probability Metrics",
        "canonical": "Integral Probability Metrics",
        "aliases": [
          "IPM"
        ],
        "category": "unique_technical",
        "rationale": "IPM is a critical component in the paper's methodology for addressing sample selection bias, making it a unique technical concept.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.82,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "treatment regularization",
      "propensity score modeling"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Context-Aware Attention Layer",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Two-Stage Training",
      "resolved_canonical": "Two-Stage Training",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.67,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Uplift Modeling",
      "resolved_canonical": "Uplift Modeling",
      "decision": "linked",
      "scores": {
        "novelty": 0.61,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Integral Probability Metrics",
      "resolved_canonical": "Integral Probability Metrics",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.82,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# TSCAN: Context-Aware Uplift Modeling via Two-Stage Training for Online Merchant Business Diagnosis

**Korean Title:** TSCAN: 온라인 상거래 비즈니스 진단을 위한 두 단계 학습 기반의 문맥 인식 업리프트 모델링

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2504.18881.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2504.18881](https://arxiv.org/abs/2504.18881)

## 🔗 유사한 논문
- [[2025-09-22/No Black Box Anymore_ Demystifying Clinical Predictive Modeling with Temporal-Feature Cross Attention Mechanism_20250922|No Black Box Anymore: Demystifying Clinical Predictive Modeling with Temporal-Feature Cross Attention Mechanism]] (81.2% similar)
- [[2025-09-22/CIDER_ A Causal Cure for Brand-Obsessed Text-to-Image Models_20250922|CIDER: A Causal Cure for Brand-Obsessed Text-to-Image Models]] (80.3% similar)
- [[2025-09-22/Two Is Better Than One_ Aligned Representation Pairs for Anomaly Detection_20250922|Two Is Better Than One: Aligned Representation Pairs for Anomaly Detection]] (79.9% similar)
- [[2025-09-18/Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients_20250918|Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients]] (78.8% similar)
- [[2025-09-17/Compute as Teacher_ Turning Inference Compute Into Reference-Free Supervision_20250917|Compute as Teacher: Turning Inference Compute Into Reference-Free Supervision]] (78.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Two-Stage Training|Two-Stage Training]], [[keywords/Uplift Modeling|Uplift Modeling]], [[keywords/Integral Probability Metrics|Integral Probability Metrics]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.18881v2 Announce Type: replace 
Abstract: A primary challenge in ITE estimation is sample selection bias. Traditional approaches utilize treatment regularization techniques such as the Integral Probability Metrics (IPM), re-weighting, and propensity score modeling to mitigate this bias. However, these regularizations may introduce undesirable information loss and limit the performance of the model. Furthermore, treatment effects vary across different external contexts, and the existing methods are insufficient in fully interacting with and utilizing these contextual features. To address these issues, we propose a Context-Aware uplift model based on the Two-Stage training approach (TSCAN), comprising CAN-U and CAN-D sub-models. In the first stage, we train an uplift model, called CAN-U, which includes the treatment regularizations of IPM and propensity score prediction, to generate a complete dataset with counterfactual uplift labels. In the second stage, we train a model named CAN-D, which utilizes an isotonic output layer to directly model uplift effects, thereby eliminating the reliance on the regularization components. CAN-D adaptively corrects the errors estimated by CAN-U through reinforcing the factual samples, while avoiding the negative impacts associated with the aforementioned regularizations. Additionally, we introduce a Context-Aware Attention Layer throughout the two-stage process to manage the interactions between treatment, merchant, and contextual features, thereby modeling the varying treatment effect in different contexts. We conduct extensive experiments on two real-world datasets to validate the effectiveness of TSCAN. Ultimately, the deployment of our model for real-world merchant diagnosis on one of China's largest online food ordering platforms validates its practical utility and impact.

## 🔍 Abstract (한글 번역)

arXiv:2504.18881v2 발표 유형: 교체  
초록: ITE(Individual Treatment Effect) 추정에서 주요 과제는 표본 선택 편향입니다. 전통적인 접근법은 이 편향을 완화하기 위해 적분 확률 메트릭(IPM), 재가중치, 성향 점수 모델링과 같은 처치 정규화 기법을 활용합니다. 그러나 이러한 정규화는 바람직하지 않은 정보 손실을 초래할 수 있으며 모델의 성능을 제한할 수 있습니다. 게다가, 처치 효과는 다양한 외부 맥락에 따라 다르며, 기존 방법들은 이러한 맥락적 특징을 충분히 상호작용하고 활용하는 데 부족합니다. 이러한 문제를 해결하기 위해, 우리는 CAN-U와 CAN-D 하위 모델로 구성된 이단계 훈련 접근법(TSCAN)에 기반한 맥락 인식 상승 모델을 제안합니다. 첫 번째 단계에서는 IPM과 성향 점수 예측의 처치 정규화를 포함하는 상승 모델인 CAN-U를 훈련하여 반사실적 상승 레이블이 포함된 완전한 데이터셋을 생성합니다. 두 번째 단계에서는 CAN-D라는 모델을 훈련하여, 등비 출력 층을 활용하여 직접적으로 상승 효과를 모델링함으로써 정규화 구성 요소에 대한 의존성을 제거합니다. CAN-D는 CAN-U가 추정한 오류를 사실 샘플을 강화함으로써 적응적으로 수정하며, 앞서 언급한 정규화와 관련된 부정적 영향을 피합니다. 또한, 우리는 처치, 상인, 맥락적 특징 간의 상호작용을 관리하기 위해 이단계 과정 전반에 걸쳐 맥락 인식 주의 레이어를 도입하여 다양한 맥락에서의 처치 효과를 모델링합니다. 우리는 TSCAN의 효과를 검증하기 위해 두 개의 실제 데이터셋에서 광범위한 실험을 수행합니다. 궁극적으로, 중국 최대의 온라인 음식 주문 플랫폼 중 하나에서 실제 상인 진단을 위한 우리 모델의 배포는 그 실용성과 영향을 입증합니다.

## 📝 요약

본 연구는 ITE(Individual Treatment Effect) 추정에서 발생하는 샘플 선택 편향 문제를 해결하기 위해 TSCAN이라는 새로운 모델을 제안합니다. 기존 방법들은 편향을 완화하기 위해 IPM, 재가중치, 성향 점수 모델링 등의 정규화를 사용하지만, 이는 정보 손실을 초래할 수 있습니다. TSCAN은 두 단계로 구성된 훈련 접근법으로, 첫 번째 단계에서는 CAN-U 모델을 통해 반사실적 상승 라벨을 생성하고, 두 번째 단계에서는 CAN-D 모델을 통해 정규화 없이 상승 효과를 직접 모델링합니다. 또한, 문맥 인식 주의 레이어를 도입하여 다양한 외부 문맥에서의 치료 효과를 모델링합니다. 실험 결과, TSCAN은 실제 데이터셋에서 효과적임을 입증하였으며, 중국의 대형 온라인 음식 주문 플랫폼에서의 실용성을 확인했습니다.

## 🎯 주요 포인트

- 1. ITE 추정에서 샘플 선택 편향 문제를 해결하기 위해 기존 방법들은 IPM, 가중치 조정, 성향 점수 모델링 등의 치료 정규화를 사용하지만, 이는 정보 손실을 초래할 수 있습니다.
- 2. 제안된 TSCAN 모델은 CAN-U와 CAN-D 두 단계로 구성되며, 첫 단계에서는 IPM과 성향 점수 예측을 포함한 CAN-U 모델을 통해 반사실적 상승 레이블을 생성합니다.
- 3. 두 번째 단계에서는 CAN-D 모델이 동형 출력 계층을 사용하여 직접 상승 효과를 모델링하며, 정규화 요소에 대한 의존성을 제거합니다.
- 4. TSCAN은 치료, 상인, 맥락적 특징 간의 상호작용을 관리하기 위해 맥락 인식 주의 계층을 도입하여 다양한 맥락에서의 치료 효과를 모델링합니다.
- 5. TSCAN 모델은 중국의 대형 온라인 음식 주문 플랫폼에서의 실제 상인 진단에 성공적으로 적용되어 실용성과 영향을 입증했습니다.


---

*Generated on 2025-09-23 11:07:31*