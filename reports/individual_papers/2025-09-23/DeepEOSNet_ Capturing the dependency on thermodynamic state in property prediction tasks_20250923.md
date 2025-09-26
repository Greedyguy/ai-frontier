---
keywords:
  - DeepEOSNet
  - Graph Neural Network
  - Thermodynamic Properties
  - Equation of State
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17018
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:18:41.987637",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "DeepEOSNet",
    "Graph Neural Network",
    "Thermodynamic Properties",
    "Equation of State"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "DeepEOSNet": 0.8,
    "Graph Neural Network": 0.85,
    "Thermodynamic Properties": 0.75,
    "Equation of State": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "DeepEOSNet",
        "canonical": "DeepEOSNet",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "DeepEOSNet is a novel architecture specifically designed for capturing state dependencies in property prediction tasks, offering unique linking opportunities.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Graph Neural Network",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Neural Networks are a key component of the proposed architecture, providing a strong link to existing research in the field.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Thermodynamic Properties",
        "canonical": "Thermodynamic Properties",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Understanding thermodynamic properties is central to the paper's focus, making it a specific technical term for linking.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "Equation of State",
        "canonical": "Equation of State",
        "aliases": [
          "EOS"
        ],
        "category": "unique_technical",
        "rationale": "Equations of state are crucial for predicting thermodynamic properties, offering specific connectivity to related research.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "machine learning",
      "model",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "DeepEOSNet",
      "resolved_canonical": "DeepEOSNet",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Graph Neural Network",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Thermodynamic Properties",
      "resolved_canonical": "Thermodynamic Properties",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Equation of State",
      "resolved_canonical": "Equation of State",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# DeepEOSNet: Capturing the dependency on thermodynamic state in property prediction tasks

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17018.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17018](https://arxiv.org/abs/2509.17018)

## 🔗 유사한 논문
- [[2025-09-22/DeepMech_ A Machine Learning Framework for Chemical Reaction Mechanism Prediction_20250922|DeepMech: A Machine Learning Framework for Chemical Reaction Mechanism Prediction]] (80.3% similar)
- [[2025-09-18/Towards universal property prediction in Cartesian space_ TACE is all you need_20250918|Towards universal property prediction in Cartesian space: TACE is all you need]] (79.0% similar)
- [[2025-09-23/Low-Rank Adaptation of Evolutionary Deep Neural Networks for Efficient Learning of Time-Dependent PDEs_20250923|Low-Rank Adaptation of Evolutionary Deep Neural Networks for Efficient Learning of Time-Dependent PDEs]] (79.0% similar)
- [[2025-09-18/Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (78.8% similar)
- [[2025-09-23/Stabilizing Information Flow Entropy_ Regularization for Safe and Interpretable Autonomous Driving Perception_20250923|Stabilizing Information Flow Entropy: Regularization for Safe and Interpretable Autonomous Driving Perception]] (78.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/DeepEOSNet|DeepEOSNet]], [[keywords/Thermodynamic Properties|Thermodynamic Properties]], [[keywords/Equation of State|Equation of State]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17018v1 Announce Type: cross 
Abstract: We propose a machine learning (ML) architecture to better capture the dependency of thermodynamic properties on the independent states. When predicting state-dependent thermodynamic properties, ML models need to account for both molecular structure and the thermodynamic state, described by independent variables, typically temperature, pressure, and composition. Modern molecular ML models typically include state information by adding it to molecular fingerprint vectors or by embedding explicit (semi-empirical) thermodynamic relations. Here, we propose to rather split the information processing on the molecular structure and the dependency on states into two separate network channels: a graph neural network and a multilayer perceptron, whose output is combined by a dot product. We refer to our approach as DeepEOSNet, as this idea is based on the DeepONet architecture [Lu et al. (2021), Nat. Mach. Intell.]: instead of operators, we learn state dependencies, with the possibility to predict equation of states (EOS). We investigate the predictive performance of DeepEOSNet by means of three case studies, which include the prediction of vapor pressure as a function of temperature, and mixture molar volume as a function of composition, temperature, and pressure. Our results show superior performance of DeepEOSNet for predicting vapor pressure and comparable performance for predicting mixture molar volume compared to state-of-research graph-based thermodynamic prediction models from our earlier works. In fact, we see large potential of DeepEOSNet in cases where data is sparse in the state domain and the output function is structurally similar across different molecules. The concept of DeepEOSNet can easily be transferred to other ML architectures in molecular context, and thus provides a viable option for property prediction.

## 📝 요약

이 논문에서는 독립 상태에 따른 열역학적 특성의 의존성을 효과적으로 포착하기 위한 기계 학습(ML) 아키텍처인 DeepEOSNet을 제안합니다. 이 방법은 분자 구조와 상태 의존성을 각각 그래프 신경망과 다층 퍼셉트론으로 처리한 후, 결과를 내적하여 결합합니다. DeepEOSNet은 온도에 따른 증기압과 혼합물 몰 부피 예측 등에서 우수한 성능을 보였으며, 특히 상태 데이터가 희소한 경우에 유리합니다. 이 접근법은 다른 ML 아키텍처에도 쉽게 적용 가능하여, 열역학적 특성 예측에 유용한 옵션을 제공합니다.

## 🎯 주요 포인트

- 1. DeepEOSNet은 분자 구조와 상태 의존성을 두 개의 네트워크 채널로 분리하여 처리하는 새로운 기계 학습 아키텍처입니다.
- 2. DeepEOSNet은 그래프 신경망과 다층 퍼셉트론을 결합하여 상태 의존성을 학습하고 상태 방정식을 예측할 수 있습니다.
- 3. DeepEOSNet은 온도에 따른 증기압 예측에서 우수한 성능을 보였으며, 혼합물 몰 부피 예측에서는 기존 모델과 유사한 성능을 보였습니다.
- 4. DeepEOSNet은 상태 도메인에서 데이터가 희소한 경우와 출력 함수가 다양한 분자에서 구조적으로 유사한 경우에 큰 잠재력을 가지고 있습니다.
- 5. DeepEOSNet의 개념은 분자 맥락에서 다른 기계 학습 아키텍처로 쉽게 전이될 수 있어 속성 예측에 유용한 옵션을 제공합니다.


---

*Generated on 2025-09-24 02:18:41*