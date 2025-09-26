<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:07:08.373394",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Wi-Fi Link Quality Prediction",
    "Machine Learning",
    "Channel-Independent Models",
    "Exponential Moving Averages"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Wi-Fi Link Quality Prediction": 0.8,
    "Machine Learning": 0.85,
    "Channel-Independent Models": 0.78,
    "Exponential Moving Averages": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Wi-Fi link quality",
        "canonical": "Wi-Fi Link Quality Prediction",
        "aliases": [
          "Wi-Fi Quality Forecasting",
          "Wireless Link Quality"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus and offers a unique perspective on predicting wireless communication quality.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Machine learning techniques",
        "canonical": "Machine Learning",
        "aliases": [
          "ML Techniques",
          "ML Methods"
        ],
        "category": "broad_technical",
        "rationale": "Machine learning is a core method used in the study, linking it to a broad technical category.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Channel-independent models",
        "canonical": "Channel-Independent Models",
        "aliases": [
          "Generalized Training Models"
        ],
        "category": "unique_technical",
        "rationale": "This concept is highlighted for its competitive performance and generalization capabilities.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Exponential moving averages",
        "canonical": "Exponential Moving Averages",
        "aliases": [
          "EMA"
        ],
        "category": "specific_connectable",
        "rationale": "This technique is crucial for the low-complexity implementation discussed in the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "prediction models",
      "experimental data",
      "real-world Wi-Fi testbed"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Wi-Fi link quality",
      "resolved_canonical": "Wi-Fi Link Quality Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Machine learning techniques",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Channel-independent models",
      "resolved_canonical": "Channel-Independent Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Exponential moving averages",
      "resolved_canonical": "Exponential Moving Averages",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Accurate and Efficient Prediction of Wi-Fi Link Quality Based on Machine Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18933.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18933](https://arxiv.org/abs/2509.18933)

## 🔗 유사한 논문
- [[2025-09-22/Interpretable Network-assisted Random Forest+_20250922|Interpretable Network-assisted Random Forest+]] (81.8% similar)
- [[2025-09-23/Learn to Optimize Resource Allocation under QoS Constraint of AR_20250923|Learn to Optimize Resource Allocation under QoS Constraint of AR]] (81.0% similar)
- [[2025-09-23/BiLCNet _ BiLSTM-Conformer Network for Encrypted Traffic Classification with 5G SA Physical Channel Records_20250923|BiLCNet : BiLSTM-Conformer Network for Encrypted Traffic Classification with 5G SA Physical Channel Records]] (80.0% similar)
- [[2025-09-22/Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets_20250922|Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets]] (79.8% similar)
- [[2025-09-23/Learned Digital Codes for Over-the-Air Federated Learning_20250923|Learned Digital Codes for Over-the-Air Federated Learning]] (79.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**🔗 Specific Connectable**: [[keywords/Exponential Moving Averages|Exponential Moving Averages]]
**⚡ Unique Technical**: [[keywords/Wi-Fi Link Quality Prediction|Wi-Fi Link Quality Prediction]], [[keywords/Channel-Independent Models|Channel-Independent Models]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18933v1 Announce Type: cross 
Abstract: Wireless communications are characterized by their unpredictability, posing challenges for maintaining consistent communication quality. This paper presents a comprehensive analysis of various prediction models, with a focus on achieving accurate and efficient Wi-Fi link quality forecasts using machine learning techniques. Specifically, the paper evaluates the performance of data-driven models based on the linear combination of exponential moving averages, which are designed for low-complexity implementations and are then suitable for hardware platforms with limited processing resources. Accuracy of the proposed approaches was assessed using experimental data from a real-world Wi-Fi testbed, considering both channel-dependent and channel-independent training data. Remarkably, channel-independent models, which allow for generalized training by equipment manufacturers, demonstrated competitive performance. Overall, this study provides insights into the practical deployment of machine learning-based prediction models for enhancing Wi-Fi dependability in industrial environments.

## 📝 요약

이 논문은 무선 통신의 예측 불가능성을 해결하기 위해 다양한 예측 모델을 분석하고, 기계 학습 기법을 활용한 Wi-Fi 링크 품질 예측을 목표로 합니다. 특히, 지수 이동 평균의 선형 결합을 기반으로 한 데이터 기반 모델의 성능을 평가하며, 이는 낮은 복잡도로 제한된 처리 자원을 가진 하드웨어 플랫폼에 적합합니다. 실제 Wi-Fi 테스트베드의 실험 데이터를 통해 제안된 접근법의 정확성을 평가했으며, 채널 독립적인 모델이 장비 제조업체에 의해 일반화된 훈련이 가능하면서도 경쟁력 있는 성능을 보였습니다. 이 연구는 산업 환경에서 Wi-Fi의 신뢰성을 향상시키기 위한 기계 학습 기반 예측 모델의 실질적 배치에 대한 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. 무선 통신의 예측 불가능성 문제를 해결하기 위해 다양한 예측 모델을 분석했습니다.
- 2. 기계 학습 기법을 활용하여 Wi-Fi 링크 품질을 정확하고 효율적으로 예측하는 방법을 제시했습니다.
- 3. 지수 이동 평균의 선형 결합을 기반으로 한 데이터 기반 모델의 성능을 평가했습니다.
- 4. 채널 독립적인 모델이 장비 제조업체의 일반화된 훈련을 가능하게 하면서도 경쟁력 있는 성능을 보였습니다.
- 5. 본 연구는 산업 환경에서 Wi-Fi의 신뢰성을 향상시키기 위한 기계 학습 기반 예측 모델의 실용적 배치에 대한 통찰을 제공합니다.


---

*Generated on 2025-09-24 14:07:08*