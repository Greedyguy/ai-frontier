<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:29:35.205952",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Federated Learning",
    "Hierarchical Federated Learning",
    "Social Network with Mobility",
    "Dynamic Optimization in Social Network with Mobility"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Federated Learning": 0.78,
    "Hierarchical Federated Learning": 0.82,
    "Social Network with Mobility": 0.79,
    "Dynamic Optimization in Social Network with Mobility": 0.8
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
        "rationale": "Federated Learning is a key concept in decentralized model training, relevant for linking various privacy-preserving techniques.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Hierarchical Federated Learning",
        "canonical": "Hierarchical Federated Learning",
        "aliases": [
          "HFL"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach combining hierarchical structures with federated learning, offering unique insights into multi-layered data privacy.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Social Network with Mobility",
        "canonical": "Social Network with Mobility",
        "aliases": [
          "SNM"
        ],
        "category": "unique_technical",
        "rationale": "The integration of mobility in social networks is a unique aspect that can enhance discussions on dynamic network models.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      },
      {
        "surface": "Dynamic Optimization in Social Network with Mobility",
        "canonical": "Dynamic Optimization in Social Network with Mobility",
        "aliases": [
          "DO-SNM"
        ],
        "category": "unique_technical",
        "rationale": "This algorithm specifically addresses optimization in mobile social networks, providing a distinct point for algorithmic discussions.",
        "novelty_score": 0.72,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "energy consumption",
      "resource allocation"
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
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Hierarchical Federated Learning",
      "resolved_canonical": "Hierarchical Federated Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Social Network with Mobility",
      "resolved_canonical": "Social Network with Mobility",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Dynamic Optimization in Social Network with Mobility",
      "resolved_canonical": "Dynamic Optimization in Social Network with Mobility",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Hierarchical Federated Learning for Social Network with Mobility

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.14938.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.14938](https://arxiv.org/abs/2509.14938)

## 🔗 유사한 논문
- [[2025-09-23/Towards Seamless Hierarchical Federated Learning under Intermittent Client Participation_ A Stagewise Decision-Making Methodology_20250923|Towards Seamless Hierarchical Federated Learning under Intermittent Client Participation: A Stagewise Decision-Making Methodology]] (85.9% similar)
- [[2025-09-23/Asynchronous Federated Learning_ A Scalable Approach for Decentralized Machine Learning_20250923|Asynchronous Federated Learning: A Scalable Approach for Decentralized Machine Learning]] (83.7% similar)
- [[2025-09-23/Zero-Shot Human Mobility Forecasting via Large Language Model with Hierarchical Reasoning_20250923|Zero-Shot Human Mobility Forecasting via Large Language Model with Hierarchical Reasoning]] (82.5% similar)
- [[2025-09-23/Progressive Size-Adaptive Federated Learning_ A Comprehensive Framework for Heterogeneous Multi-Modal Data Systems_20250923|Progressive Size-Adaptive Federated Learning: A Comprehensive Framework for Heterogeneous Multi-Modal Data Systems]] (82.4% similar)
- [[2025-09-22/Towards Communication-efficient Federated Learning via Sparse and Aligned Adaptive Optimization_20250922|Towards Communication-efficient Federated Learning via Sparse and Aligned Adaptive Optimization]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Federated Learning|Federated Learning]]
**⚡ Unique Technical**: [[keywords/Hierarchical Federated Learning|Hierarchical Federated Learning]], [[keywords/Social Network with Mobility|Social Network with Mobility]], [[keywords/Dynamic Optimization in Social Network with Mobility|Dynamic Optimization in Social Network with Mobility]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14938v2 Announce Type: replace 
Abstract: Federated Learning (FL) offers a decentralized solution that allows collaborative local model training and global aggregation, thereby protecting data privacy. In conventional FL frameworks, data privacy is typically preserved under the assumption that local data remains absolutely private, whereas the mobility of clients is frequently neglected in explicit modeling. In this paper, we propose a hierarchical federated learning framework based on the social network with mobility namely HFL-SNM that considers both data sharing among clients and their mobility patterns. Under the constraints of limited resources, we formulate a joint optimization problem of resource allocation and client scheduling, which objective is to minimize the energy consumption of clients during the FL process. In social network, we introduce the concepts of Effective Data Coverage Rate and Redundant Data Coverage Rate. We analyze the impact of effective data and redundant data on the model performance through preliminary experiments. We decouple the optimization problem into multiple sub-problems, analyze them based on preliminary experimental results, and propose Dynamic Optimization in Social Network with Mobility (DO-SNM) algorithm. Experimental results demonstrate that our algorithm achieves superior model performance while significantly reducing energy consumption, compared to traditional baseline algorithms.

## 📝 요약

이 논문은 이동성을 고려한 사회적 네트워크 기반의 계층적 연합 학습(HFL-SNM) 프레임워크를 제안합니다. 기존 연합 학습에서는 데이터 프라이버시를 보장하지만, 클라이언트의 이동성은 충분히 고려되지 않았습니다. 제안된 HFL-SNM은 클라이언트 간 데이터 공유와 이동 패턴을 고려하여, 자원 할당과 클라이언트 스케줄링을 최적화함으로써 에너지 소비를 최소화하는 것을 목표로 합니다. 효과적 데이터 커버리지율과 중복 데이터 커버리지율 개념을 도입하고, 이들이 모델 성능에 미치는 영향을 분석했습니다. 이를 통해 문제를 여러 하위 문제로 분리하고, 이동성을 고려한 동적 최적화 알고리즘(DO-SNM)을 제안했습니다. 실험 결과, 제안된 알고리즘은 전통적인 알고리즘에 비해 모델 성능을 향상시키면서 에너지 소비를 크게 줄였습니다.

## 🎯 주요 포인트

- 1. 본 논문은 클라이언트의 이동성을 고려한 사회 네트워크 기반 계층적 연합 학습 프레임워크(HFL-SNM)를 제안합니다.
- 2. 제한된 자원 하에서 자원 할당과 클라이언트 스케줄링의 공동 최적화 문제를 공식화하여 에너지 소비를 최소화하고자 합니다.
- 3. 효과적인 데이터 커버리지율과 중복 데이터 커버리지율의 개념을 도입하여 모델 성능에 미치는 영향을 분석합니다.
- 4. 제안된 DO-SNM 알고리즘은 전통적인 기준 알고리즘에 비해 에너지 소비를 크게 줄이면서 우수한 모델 성능을 달성합니다.


---

*Generated on 2025-09-24 15:29:35*