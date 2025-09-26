<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:07:18.015444",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Wireless Sensor Networks",
    "Cooperative Localization",
    "Non-Cooperative Localization",
    "Scaled Proximal ADMM"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Wireless Sensor Networks": 0.82,
    "Cooperative Localization": 0.79,
    "Non-Cooperative Localization": 0.77,
    "Scaled Proximal ADMM": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Wireless Sensor Networks",
        "canonical": "Wireless Sensor Networks",
        "aliases": [
          "WSNs"
        ],
        "category": "specific_connectable",
        "rationale": "Wireless Sensor Networks are a key domain for localization techniques, providing strong connectivity to related research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Cooperative Localization",
        "canonical": "Cooperative Localization",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Cooperative Localization is a specialized technique in sensor networks, offering unique insights into network-based localization methods.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.79
      },
      {
        "surface": "Non-Cooperative Localization",
        "canonical": "Non-Cooperative Localization",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Non-Cooperative Localization presents a contrasting approach to cooperative methods, enhancing understanding of independent localization strategies.",
        "novelty_score": 0.72,
        "connectivity_score": 0.7,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      },
      {
        "surface": "Scaled Proximal ADMM",
        "canonical": "Scaled Proximal ADMM",
        "aliases": [
          "SP-ADMM"
        ],
        "category": "unique_technical",
        "rationale": "Scaled Proximal ADMM is a novel algorithmic approach in optimization, relevant for distributed computation in sensor networks.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "Joint Processing",
      "Target Estimation",
      "Variable Coupling"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Wireless Sensor Networks",
      "resolved_canonical": "Wireless Sensor Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Cooperative Localization",
      "resolved_canonical": "Cooperative Localization",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Non-Cooperative Localization",
      "resolved_canonical": "Non-Cooperative Localization",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.7,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Scaled Proximal ADMM",
      "resolved_canonical": "Scaled Proximal ADMM",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Joint Cooperative and Non-Cooperative Localization in WSNs with Distributed Scaled Proximal ADMM Algorithms

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18213.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18213](https://arxiv.org/abs/2509.18213)

## 🔗 유사한 논문
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (83.1% similar)
- [[2025-09-23/KNN-MMD_ Cross Domain Wireless Sensing via Local Distribution Alignment_20250923|KNN-MMD: Cross Domain Wireless Sensing via Local Distribution Alignment]] (81.8% similar)
- [[2025-09-19/Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments_20250919|Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments]] (81.1% similar)
- [[2025-09-19/Nonlinear Cooperative Salvo Guidance with Seeker-Limited Interceptors_20250919|Nonlinear Cooperative Salvo Guidance with Seeker-Limited Interceptors]] (80.3% similar)
- [[2025-09-22/Fully Decentralized Cooperative Multi-Agent Reinforcement Learning is A Context Modeling Problem_20250922|Fully Decentralized Cooperative Multi-Agent Reinforcement Learning is A Context Modeling Problem]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Wireless Sensor Networks|Wireless Sensor Networks]]
**⚡ Unique Technical**: [[keywords/Cooperative Localization|Cooperative Localization]], [[keywords/Non-Cooperative Localization|Non-Cooperative Localization]], [[keywords/Scaled Proximal ADMM|Scaled Proximal ADMM]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18213v1 Announce Type: cross 
Abstract: Cooperative and non-cooperative localization frequently arise together in wireless sensor networks, particularly when sensor positions are uncertain and targets are unable to communicate with the network. While joint processing can eliminate the delay in target estimation found in sequential approaches, it introduces complex variable coupling, posing challenges in both modeling and optimization. This paper presents a joint modeling approach that formulates cooperative and non-cooperative localization as a single optimization problem. To address the resulting coupling, we introduce auxiliary variables that enable structural decoupling and distributed computation. Building on this formulation, we develop the Scaled Proximal Alternating Direction Method of Multipliers for Joint Cooperative and Non-Cooperative Localization (SP-ADMM-JCNL). Leveraging the problem's structured design, we provide theoretical guarantees that the algorithm generates a sequence converging globally to the Karush-Kuhn-Tucker (KKT) point of the reformulated problem and further to a critical point of the original non-convex objective function, with a sublinear rate of O(1/T). Experiments on both synthetic and benchmark datasets demonstrate that SP-ADMM-JCNL achieves accurate and reliable localization performance.

## 📝 요약

이 논문은 무선 센서 네트워크에서 협력적 및 비협력적 위치 추정을 하나의 최적화 문제로 통합하는 모델링 접근법을 제시합니다. 복잡한 변수 결합 문제를 해결하기 위해 보조 변수를 도입하여 구조적 분리와 분산 계산을 가능하게 합니다. 이를 바탕으로 SP-ADMM-JCNL 알고리즘을 개발하였으며, 이 알고리즘은 문제의 구조적 설계를 활용하여 Karush-Kuhn-Tucker (KKT) 점에 전역적으로 수렴함을 이론적으로 보장합니다. 실험 결과, SP-ADMM-JCNL은 정확하고 신뢰할 수 있는 위치 추정 성능을 보여줍니다.

## 🎯 주요 포인트

- 1. 무선 센서 네트워크에서 협력적 및 비협력적 위치 추정 문제를 단일 최적화 문제로 모델링하는 접근법을 제시합니다.
- 2. 구조적 디커플링과 분산 계산을 가능하게 하는 보조 변수를 도입하여 복잡한 변수 결합 문제를 해결합니다.
- 3. SP-ADMM-JCNL 알고리즘을 개발하여 Karush-Kuhn-Tucker (KKT) 점으로의 전역 수렴을 이론적으로 보장합니다.
- 4. SP-ADMM-JCNL은 합성 및 벤치마크 데이터셋 실험에서 정확하고 신뢰할 수 있는 위치 추정 성능을 달성합니다.


---

*Generated on 2025-09-24 15:07:18*