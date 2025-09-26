---
keywords:
  - Network-assisted Random Forest
  - Graph Neural Network
  - Feature Importance Measures
  - Sample Influence Measures
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15611
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:50:37.000167",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Network-assisted Random Forest",
    "Graph Neural Network",
    "Feature Importance Measures",
    "Sample Influence Measures"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Network-assisted Random Forest": 0.8,
    "Graph Neural Network": 0.85,
    "Feature Importance Measures": 0.7,
    "Sample Influence Measures": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Network-assisted Random Forest",
        "canonical": "Network-assisted Random Forest",
        "aliases": [
          "Network-assisted RF",
          "RF+"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach that combines network information with random forests, offering a unique perspective on model interpretability.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.8
      },
      {
        "surface": "Graph Neural Networks",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Neural Networks are a key component in leveraging network data for machine learning, providing strong connectivity with existing literature.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Feature Importance Measures",
        "canonical": "Feature Importance Measures",
        "aliases": [
          "Feature Importance",
          "Importance Measures"
        ],
        "category": "broad_technical",
        "rationale": "Understanding feature importance is crucial for model interpretability, connecting well with existing interpretability frameworks.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      },
      {
        "surface": "Sample Influence Measures",
        "canonical": "Sample Influence Measures",
        "aliases": [
          "Sample Influence",
          "Influence Measures"
        ],
        "category": "unique_technical",
        "rationale": "This concept provides insights into the impact of individual samples on model predictions, enhancing interpretability.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "interpretability",
      "transparency",
      "prediction performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Network-assisted Random Forest",
      "resolved_canonical": "Network-assisted Random Forest",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Graph Neural Networks",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Feature Importance Measures",
      "resolved_canonical": "Feature Importance Measures",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Sample Influence Measures",
      "resolved_canonical": "Sample Influence Measures",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Interpretable Network-assisted Random Forest+

**Korean Title:** 해석 가능한 네트워크 지원 랜덤 포레스트+

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15611.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15611](https://arxiv.org/abs/2509.15611)

## 🔗 유사한 논문
- [[2025-09-22/Adversarial generalization of unfolding (model-based) networks_20250922|Adversarial generalization of unfolding (model-based) networks]] (81.5% similar)
- [[2025-09-19/Improving Internet Traffic Matrix Prediction via Time Series Clustering_20250919|Improving Internet Traffic Matrix Prediction via Time Series Clustering]] (80.9% similar)
- [[2025-09-17/A Neural Network for the Identical Kuramoto Equation_ Architectural Considerations and Performance Evaluation_20250917|A Neural Network for the Identical Kuramoto Equation: Architectural Considerations and Performance Evaluation]] (80.0% similar)
- [[2025-09-18/Learning Graph from Smooth Signals under Partial Observation_ A Robustness Analysis_20250918|Learning Graph from Smooth Signals under Partial Observation: A Robustness Analysis]] (79.1% similar)
- [[2025-09-18/Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (79.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Feature Importance Measures|Feature Importance Measures]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Network-assisted Random Forest|Network-assisted Random Forest]], [[keywords/Sample Influence Measures|Sample Influence Measures]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15611v1 Announce Type: cross 
Abstract: Machine learning algorithms often assume that training samples are independent. When data points are connected by a network, the induced dependency between samples is both a challenge, reducing effective sample size, and an opportunity to improve prediction by leveraging information from network neighbors. Multiple methods taking advantage of this opportunity are now available, but many, including graph neural networks, are not easily interpretable, limiting their usefulness for understanding how a model makes its predictions. Others, such as network-assisted linear regression, are interpretable but often yield substantially worse prediction performance. We bridge this gap by proposing a family of flexible network-assisted models built upon a generalization of random forests (RF+), which achieves highly-competitive prediction accuracy and can be interpreted through feature importance measures. In particular, we develop a suite of interpretation tools that enable practitioners to not only identify important features that drive model predictions, but also quantify the importance of the network contribution to prediction. Importantly, we provide both global and local importance measures as well as sample influence measures to assess the impact of a given observation. This suite of tools broadens the scope and applicability of network-assisted machine learning for high-impact problems where interpretability and transparency are essential.

## 🔍 Abstract (한글 번역)

arXiv:2509.15611v1 발표 유형: 교차  
초록: 머신 러닝 알고리즘은 종종 훈련 샘플이 독립적이라고 가정합니다. 데이터 포인트가 네트워크에 의해 연결될 때, 샘플 간에 유도된 종속성은 효과적인 샘플 크기를 줄이는 도전 과제이면서, 네트워크 이웃의 정보를 활용하여 예측을 개선할 수 있는 기회이기도 합니다. 이러한 기회를 활용하는 여러 방법들이 현재 사용 가능하지만, 그래프 신경망을 포함한 많은 방법들은 쉽게 해석할 수 없어 모델이 어떻게 예측을 수행하는지를 이해하는 데 유용성이 제한됩니다. 반면에 네트워크 보조 선형 회귀와 같은 다른 방법들은 해석 가능하지만 종종 예측 성능이 상당히 떨어집니다. 우리는 랜덤 포레스트의 일반화를 기반으로 하는 유연한 네트워크 보조 모델 패밀리(RF+)를 제안하여 이 격차를 해소합니다. 이 모델은 높은 경쟁력을 가진 예측 정확도를 달성하며, 특징 중요도 측정을 통해 해석할 수 있습니다. 특히, 우리는 모델 예측을 이끄는 중요한 특징을 식별할 뿐만 아니라 예측에 대한 네트워크 기여의 중요성을 정량화할 수 있는 해석 도구 모음을 개발했습니다. 중요한 점은, 우리는 주어진 관찰의 영향을 평가하기 위한 전역 및 지역 중요도 측정치뿐만 아니라 샘플 영향 측정치를 제공합니다. 이 도구 모음은 해석 가능성과 투명성이 필수적인 고영향 문제에 대한 네트워크 보조 머신 러닝의 범위와 적용 가능성을 확장합니다.

## 📝 요약

이 논문은 네트워크로 연결된 데이터에서의 예측 성능과 해석 가능성을 동시에 개선하는 새로운 기법을 제안합니다. 기존의 그래프 신경망은 예측 성능은 우수하지만 해석이 어려운 반면, 네트워크 보조 선형 회귀는 해석 가능하지만 예측 성능이 낮습니다. 이를 해결하기 위해, 저자들은 랜덤 포레스트를 일반화한 RF+ 모델을 기반으로 한 유연한 네트워크 보조 모델을 개발했습니다. 이 모델은 높은 예측 정확도를 유지하면서도, 특징 중요도 측정을 통해 해석이 가능합니다. 또한, 네트워크의 기여도를 정량화할 수 있는 해석 도구를 제공하여, 글로벌 및 로컬 중요도와 샘플 영향력을 평가할 수 있습니다. 이 도구들은 해석 가능성과 투명성이 중요한 문제에서 네트워크 보조 머신러닝의 적용 범위를 넓힙니다.

## 🎯 주요 포인트

- 1. 네트워크에 연결된 데이터 포인트 간의 종속성은 샘플 크기를 줄이는 도전이자 네트워크 이웃의 정보를 활용해 예측을 개선할 기회로 작용합니다.
- 2. 기존의 그래프 신경망 등은 해석이 어려워 모델 예측 이해에 한계가 있으며, 네트워크 지원 선형 회귀는 해석 가능하지만 예측 성능이 떨어집니다.
- 3. RF+라는 랜덤 포레스트의 일반화를 기반으로 한 유연한 네트워크 지원 모델을 제안하여 높은 예측 정확도를 유지하면서도 해석 가능성을 제공합니다.
- 4. 모델 예측에 중요한 특징을 식별하고 네트워크 기여도를 정량화할 수 있는 해석 도구 모음을 개발했습니다.
- 5. 이 도구 모음은 해석 가능성과 투명성이 중요한 고영향 문제에 네트워크 지원 머신러닝의 적용 범위를 확장합니다.


---

*Generated on 2025-09-23 10:50:37*