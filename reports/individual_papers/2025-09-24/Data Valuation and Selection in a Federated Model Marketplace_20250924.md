<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:33:06.389405",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Federated Learning",
    "Wasserstein-based Estimator",
    "Data Marketplaces",
    "Neural Scaling Law"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Federated Learning": 0.85,
    "Wasserstein-based Estimator": 0.78,
    "Data Marketplaces": 0.72,
    "Neural Scaling Law": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Federated Learning",
        "canonical": "Federated Learning",
        "aliases": [
          "FL"
        ],
        "category": "broad_technical",
        "rationale": "Federated Learning is central to the paper's framework and connects well with privacy-preserving data analysis.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Wasserstein-based estimator",
        "canonical": "Wasserstein-based Estimator",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This estimator is a unique technical contribution of the paper, offering a novel approach to data valuation in federated settings.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "data marketplaces",
        "canonical": "Data Marketplaces",
        "aliases": [
          "data exchange platforms"
        ],
        "category": "evolved_concepts",
        "rationale": "Data marketplaces are evolving concepts crucial for understanding the economic context of federated learning applications.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      },
      {
        "surface": "neural scaling law",
        "canonical": "Neural Scaling Law",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "The neural scaling law is a specific concept that links model performance prediction to data selection strategies.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "model performance",
      "data combinations"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Federated Learning",
      "resolved_canonical": "Federated Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Wasserstein-based estimator",
      "resolved_canonical": "Wasserstein-based Estimator",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "data marketplaces",
      "resolved_canonical": "Data Marketplaces",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "neural scaling law",
      "resolved_canonical": "Neural Scaling Law",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Data Valuation and Selection in a Federated Model Marketplace

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18104.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18104](https://arxiv.org/abs/2509.18104)

## 🔗 유사한 논문
- [[2025-09-23/Federated Learning for Financial Forecasting_20250923|Federated Learning for Financial Forecasting]] (85.0% similar)
- [[2025-09-23/Progressive Size-Adaptive Federated Learning_ A Comprehensive Framework for Heterogeneous Multi-Modal Data Systems_20250923|Progressive Size-Adaptive Federated Learning: A Comprehensive Framework for Heterogeneous Multi-Modal Data Systems]] (83.9% similar)
- [[2025-09-19/Who to Trust? Aggregating Client Knowledge in Logit-Based Federated Learning_20250919|Who to Trust? Aggregating Client Knowledge in Logit-Based Federated Learning]] (83.8% similar)
- [[2025-09-19/MetaTrading_ An Immersion-Aware Model Trading Framework for Vehicular Metaverse Services_20250919|MetaTrading: An Immersion-Aware Model Trading Framework for Vehicular Metaverse Services]] (83.3% similar)
- [[2025-09-23/Towards Seamless Hierarchical Federated Learning under Intermittent Client Participation_ A Stagewise Decision-Making Methodology_20250923|Towards Seamless Hierarchical Federated Learning under Intermittent Client Participation: A Stagewise Decision-Making Methodology]] (82.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Federated Learning|Federated Learning]]
**🔗 Specific Connectable**: [[keywords/Neural Scaling Law|Neural Scaling Law]]
**⚡ Unique Technical**: [[keywords/Wasserstein-based Estimator|Wasserstein-based Estimator]]
**🚀 Evolved Concepts**: [[keywords/Data Marketplaces|Data Marketplaces]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18104v1 Announce Type: cross 
Abstract: In the era of Artificial Intelligence (AI), marketplaces have become essential platforms for facilitating the exchange of data products to foster data sharing. Model transactions provide economic solutions in data marketplaces that enhance data reusability and ensure the traceability of data ownership. To establish trustworthy data marketplaces, Federated Learning (FL) has emerged as a promising paradigm to enable collaborative learning across siloed datasets while safeguarding data privacy. However, effective data valuation and selection from heterogeneous sources in the FL setup remain key challenges. This paper introduces a comprehensive framework centered on a Wasserstein-based estimator tailored for FL. The estimator not only predicts model performance across unseen data combinations but also reveals the compatibility between data heterogeneity and FL aggregation algorithms. To ensure privacy, we propose a distributed method to approximate Wasserstein distance without requiring access to raw data. Furthermore, we demonstrate that model performance can be reliably extrapolated under the neural scaling law, enabling effective data selection without full-scale training. Extensive experiments across diverse scenarios, such as label skew, mislabeled, and unlabeled sources, show that our approach consistently identifies high-performing data combinations, paving the way for more reliable FL-based model marketplaces.

## 📝 요약

이 논문은 인공지능 시대의 데이터 마켓플레이스에서 데이터 재사용성과 소유권 추적성을 높이는 모델 거래의 중요성을 강조합니다. 신뢰할 수 있는 데이터 마켓플레이스를 구축하기 위해 연합 학습(FL)이 데이터 프라이버시를 보호하면서 협력적 학습을 가능하게 하는 유망한 패러다임으로 부상했습니다. 그러나 FL 환경에서 이질적인 데이터 소스의 효과적인 데이터 평가와 선택은 여전히 중요한 과제입니다. 본 논문은 FL에 맞춘 Wasserstein 기반 추정기를 중심으로 한 포괄적인 프레임워크를 제안합니다. 이 추정기는 미지의 데이터 조합에서 모델 성능을 예측할 뿐만 아니라 데이터 이질성과 FL 집계 알고리즘 간의 호환성을 드러냅니다. 프라이버시를 보장하기 위해 원시 데이터에 접근하지 않고 Wasserstein 거리를 근사하는 분산 방법을 제안합니다. 또한, 신경 스케일링 법칙에 따라 모델 성능을 신뢰성 있게 추론할 수 있음을 보여주어 전체 훈련 없이도 효과적인 데이터 선택이 가능합니다. 다양한 시나리오에서의 실험을 통해 제안된 접근법이 일관되게 높은 성능의 데이터 조합을 식별함을 입증하였습니다.

## 🎯 주요 포인트

- 1. 인공지능 시대에 데이터 마켓플레이스는 데이터 제품 교환을 촉진하는 필수 플랫폼으로 부상하고 있습니다.
- 2. 신뢰할 수 있는 데이터 마켓플레이스를 구축하기 위해 연합 학습(Federated Learning, FL)이 데이터 프라이버시를 보호하면서 협업 학습을 가능하게 하는 유망한 패러다임으로 떠오르고 있습니다.
- 3. 이 논문은 FL에 맞춘 Wasserstein 기반 추정기를 중심으로 한 종합적인 프레임워크를 소개하며, 이는 데이터 이질성과 FL 집계 알고리즘 간의 호환성을 밝혀냅니다.
- 4. 원시 데이터에 접근하지 않고도 Wasserstein 거리를 근사할 수 있는 분산 방법을 제안하여 프라이버시를 보장합니다.
- 5. 다양한 시나리오에서의 실험을 통해 제안된 접근 방식이 일관되게 고성능 데이터 조합을 식별함을 보여주며, FL 기반 모델 마켓플레이스의 신뢰성을 높입니다.


---

*Generated on 2025-09-24 13:33:06*