---
keywords:
  - Federated Learning
  - Internet of Vehicles
  - FairEquityFL
  - Client Selection
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.20193
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:45:52.320603",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Federated Learning",
    "Internet of Vehicles",
    "FairEquityFL",
    "Client Selection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Federated Learning": 0.9,
    "Internet of Vehicles": 0.8,
    "FairEquityFL": 0.85,
    "Client Selection": 0.78
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
        "rationale": "Federated Learning is a central concept in the paper, linking privacy-preserving machine learning with client selection challenges.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.9
      },
      {
        "surface": "Internet of Vehicles",
        "canonical": "Internet of Vehicles",
        "aliases": [
          "IoV"
        ],
        "category": "specific_connectable",
        "rationale": "The Internet of Vehicles is a specific application context for Federated Learning discussed in the paper.",
        "novelty_score": 0.7,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "FairEquityFL",
        "canonical": "FairEquityFL",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "FairEquityFL is a novel framework proposed in the paper for fair client selection in Federated Learning.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "client selection",
        "canonical": "Client Selection",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Client selection is a key challenge addressed by the FairEquityFL framework in the context of Federated Learning.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "model performance",
      "training process"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Federated Learning",
      "resolved_canonical": "Federated Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Internet of Vehicles",
      "resolved_canonical": "Internet of Vehicles",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "FairEquityFL",
      "resolved_canonical": "FairEquityFL",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "client selection",
      "resolved_canonical": "Client Selection",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# FairEquityFL -- A Fair and Equitable Client Selection in Federated Learning for Heterogeneous IoV Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20193.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.20193](https://arxiv.org/abs/2509.20193)

## 🔗 유사한 논문
- [[2025-09-24/FedFiTS_ Fitness-Selected, Slotted Client Scheduling for Trustworthy Federated Learning in Healthcare AI_20250924|FedFiTS: Fitness-Selected, Slotted Client Scheduling for Trustworthy Federated Learning in Healthcare AI]] (88.4% similar)
- [[2025-09-23/Towards Seamless Hierarchical Federated Learning under Intermittent Client Participation_ A Stagewise Decision-Making Methodology_20250923|Towards Seamless Hierarchical Federated Learning under Intermittent Client Participation: A Stagewise Decision-Making Methodology]] (87.6% similar)
- [[2025-09-24/Data Valuation and Selection in a Federated Model Marketplace_20250924|Data Valuation and Selection in a Federated Model Marketplace]] (86.3% similar)
- [[2025-09-24/Communication-Efficient Federated Learning with Adaptive Number of Participants_20250924|Communication-Efficient Federated Learning with Adaptive Number of Participants]] (85.8% similar)
- [[2025-09-23/Asynchronous Federated Learning_ A Scalable Approach for Decentralized Machine Learning_20250923|Asynchronous Federated Learning: A Scalable Approach for Decentralized Machine Learning]] (85.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Federated Learning|Federated Learning]]
**🔗 Specific Connectable**: [[keywords/Internet of Vehicles|Internet of Vehicles]], [[keywords/Client Selection|Client Selection]]
**⚡ Unique Technical**: [[keywords/FairEquityFL|FairEquityFL]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20193v1 Announce Type: new 
Abstract: Federated Learning (FL) has been extensively employed for a number of applications in machine learning, i.e., primarily owing to its privacy preserving nature and efficiency in mitigating the communication overhead. Internet of Vehicles (IoV) is one of the promising applications, wherein FL can be utilized to train a model more efficiently. Since only a subset of the clients can participate in each FL training round, challenges arise pertinent to fairness in the client selection process. Over the years, a number of researchers from both academia and industry have proposed numerous FL frameworks. However, to the best of our knowledge, none of them have employed fairness for FL-based client selection in a dynamic and heterogeneous IoV environment. Accordingly, in this paper, we envisage a FairEquityFL framework to ensure an equitable opportunity for all the clients to participate in the FL training process. In particular, we have introduced a sampling equalizer module within the selector component for ensuring fairness in terms of fair collaboration opportunity for all the clients in the client selection process. The selector is additionally responsible for both monitoring and controlling the clients' participation in each FL training round. Moreover, an outlier detection mechanism is enforced for identifying malicious clients based on the model performance in terms of considerable fluctuation in either accuracy or loss minimization. The selector flags suspicious clients and temporarily suspend such clients from participating in the FL training process. We further evaluate the performance of FairEquityFL on a publicly available dataset, FEMNIST. Our simulation results depict that FairEquityFL outperforms baseline models to a considerable extent.

## 📝 요약

이 논문은 차량 인터넷(IoV) 환경에서 연합 학습(FL)의 공정한 클라이언트 선택을 위한 FairEquityFL 프레임워크를 제안합니다. 기존의 FL 프레임워크는 클라이언트 선택의 공정성을 충분히 고려하지 않았으나, FairEquityFL은 모든 클라이언트에게 공정한 참여 기회를 제공하기 위해 샘플링 평등화 모듈을 도입하였습니다. 또한, 모델 성능의 변동을 기반으로 악의적인 클라이언트를 탐지하고, 이들의 참여를 일시적으로 중단하는 메커니즘을 포함하고 있습니다. FEMNIST 데이터셋을 활용한 실험 결과, FairEquityFL은 기존 모델들보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 연합 학습(Federated Learning, FL)은 사생활 보호와 통신 오버헤드 감소의 효율성 덕분에 다양한 기계 학습 응용 분야에 널리 사용되고 있습니다.
- 2. 차량 인터넷(Internet of Vehicles, IoV) 환경에서 FL 기반 클라이언트 선택의 공정성을 보장하기 위한 FairEquityFL 프레임워크를 제안합니다.
- 3. FairEquityFL은 클라이언트 선택 과정에서 모든 클라이언트에게 공정한 협업 기회를 제공하기 위해 샘플링 평등화 모듈을 도입했습니다.
- 4. 악의적인 클라이언트를 식별하기 위해 모델 성능의 정확도 또는 손실 최소화의 변동성을 기반으로 한 이상치 탐지 메커니즘을 적용합니다.
- 5. FairEquityFL은 공개 데이터셋 FEMNIST를 사용한 시뮬레이션 결과에서 기존 모델보다 성능이 우수함을 보여줍니다.


---

*Generated on 2025-09-25 16:45:52*