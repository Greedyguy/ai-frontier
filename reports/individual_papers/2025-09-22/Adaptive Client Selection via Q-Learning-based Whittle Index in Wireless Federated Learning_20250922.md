---
keywords:
  - Federated Learning
  - Whittle Index Learning
  - Restless Multi-Armed Bandit
  - Client Selection in Federated Learning
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.13933
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:12:45.568017",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Federated Learning",
    "Whittle Index Learning",
    "Restless Multi-Armed Bandit",
    "Client Selection in Federated Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Federated Learning": 0.85,
    "Whittle Index Learning": 0.78,
    "Restless Multi-Armed Bandit": 0.82,
    "Client Selection in Federated Learning": 0.8
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
        "rationale": "Federated Learning is a central theme of the paper and connects well with related distributed learning concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.85
      },
      {
        "surface": "Whittle Index Learning in Federated Q-learning",
        "canonical": "Whittle Index Learning",
        "aliases": [
          "WILF-Q"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach introduced in the paper, making it a unique technical contribution.",
        "novelty_score": 0.92,
        "connectivity_score": 0.67,
        "specificity_score": 0.89,
        "link_intent_score": 0.78
      },
      {
        "surface": "Restless Multi-Armed Bandit Problem",
        "canonical": "Restless Multi-Armed Bandit",
        "aliases": [
          "RMAB"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is crucial for understanding the client selection strategy described in the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.79,
        "specificity_score": 0.81,
        "link_intent_score": 0.82
      },
      {
        "surface": "Client Selection",
        "canonical": "Client Selection in Federated Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Client selection is a key challenge in Federated Learning, directly addressed by the paper.",
        "novelty_score": 0.48,
        "connectivity_score": 0.83,
        "specificity_score": 0.76,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "learning accuracy",
      "baseline policies"
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
        "specificity": 0.72,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Whittle Index Learning in Federated Q-learning",
      "resolved_canonical": "Whittle Index Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.67,
        "specificity": 0.89,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Restless Multi-Armed Bandit Problem",
      "resolved_canonical": "Restless Multi-Armed Bandit",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.79,
        "specificity": 0.81,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Client Selection",
      "resolved_canonical": "Client Selection in Federated Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.48,
        "connectivity": 0.83,
        "specificity": 0.76,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Adaptive Client Selection via Q-Learning-based Whittle Index in Wireless Federated Learning

**Korean Title:** 적응형 클라이언트 선택: 무선 연합 학습에서 Q-러닝 기반 Whittle 지수 활용

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.13933.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.13933](https://arxiv.org/abs/2509.13933)

## 🔗 유사한 논문
- [[2025-09-17/Adaptive Client Selection via Q-Learning-based Whittle Index in Wireless Federated Learning_20250917|Adaptive Client Selection via Q-Learning-based Whittle Index in Wireless Federated Learning]] (99.0% similar)
- [[2025-09-19/Who to Trust? Aggregating Client Knowledge in Logit-Based Federated Learning_20250919|Who to Trust? Aggregating Client Knowledge in Logit-Based Federated Learning]] (81.8% similar)
- [[2025-09-19/FedAVOT_ Exact Distribution Alignment in Federated Learning via Masked Optimal Transport_20250919|FedAVOT: Exact Distribution Alignment in Federated Learning via Masked Optimal Transport]] (79.7% similar)
- [[2025-09-19/Hierarchical Federated Learning for Social Network with Mobility_20250919|Hierarchical Federated Learning for Social Network with Mobility]] (78.9% similar)
- [[2025-09-19/Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (78.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Federated Learning|Federated Learning]]
**🔗 Specific Connectable**: [[keywords/Restless Multi-Armed Bandit|Restless Multi-Armed Bandit]], [[keywords/Client Selection in Federated Learning|Client Selection in Federated Learning]]
**⚡ Unique Technical**: [[keywords/Whittle Index Learning|Whittle Index Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13933v2 Announce Type: replace 
Abstract: We consider the client selection problem in wireless Federated Learning (FL), with the objective of reducing the total required time to achieve a certain level of learning accuracy. Since the server cannot observe the clients' dynamic states that can change their computation and communication efficiency, we formulate client selection as a restless multi-armed bandit problem. We propose a scalable and efficient approach called the Whittle Index Learning in Federated Q-learning (WILF-Q), which uses Q-learning to adaptively learn and update an approximated Whittle index associated with each client, and then selects the clients with the highest indices. Compared to existing approaches, WILF-Q does not require explicit knowledge of client state transitions or data distributions, making it well-suited for deployment in practical FL settings. Experiment results demonstrate that WILF-Q significantly outperforms existing baseline policies in terms of learning efficiency, providing a robust and efficient approach to client selection in wireless FL.

## 🔍 Abstract (한글 번역)

arXiv:2509.13933v2 발표 유형: 교체  
초록: 우리는 무선 연합 학습(FL)에서 클라이언트 선택 문제를 고려하며, 특정 수준의 학습 정확도를 달성하기 위한 총 소요 시간을 줄이는 것을 목표로 합니다. 서버는 클라이언트의 계산 및 통신 효율성을 변경할 수 있는 동적 상태를 관찰할 수 없기 때문에, 우리는 클라이언트 선택을 휴리스틱 멀티암드 밴딧 문제로 공식화합니다. 우리는 연합 Q-학습에서 휘틀 지수 학습(WILF-Q)이라는 확장 가능하고 효율적인 접근 방식을 제안하며, 이는 Q-학습을 사용하여 각 클라이언트와 관련된 근사 휘틀 지수를 적응적으로 학습하고 업데이트한 다음 가장 높은 지수를 가진 클라이언트를 선택합니다. 기존 접근 방식과 비교하여, WILF-Q는 클라이언트 상태 전환이나 데이터 분포에 대한 명시적 지식이 필요하지 않으므로 실제 FL 환경에 배포하기에 적합합니다. 실험 결과는 WILF-Q가 학습 효율성 측면에서 기존의 기준 정책을 크게 능가하며, 무선 FL에서 클라이언트 선택에 대한 강력하고 효율적인 접근 방식을 제공함을 보여줍니다.

## 📝 요약

이 논문은 무선 연합 학습(FL)에서 클라이언트 선택 문제를 다루며, 특정 학습 정확도 수준을 달성하는 데 필요한 총 시간을 줄이는 것을 목표로 합니다. 서버가 클라이언트의 동적 상태를 관찰할 수 없기 때문에, 클라이언트 선택 문제를 '휴식 없는 다중 슬롯머신 문제'로 공식화했습니다. 이를 해결하기 위해, 각 클라이언트와 관련된 Whittle 지수를 Q-러닝을 통해 적응적으로 학습하고 업데이트하는 WILF-Q라는 확장 가능하고 효율적인 방법을 제안합니다. WILF-Q는 클라이언트 상태 전이나 데이터 분포에 대한 명시적 지식이 필요하지 않아 실제 FL 환경에 적합합니다. 실험 결과, WILF-Q는 학습 효율성 측면에서 기존의 기준 정책들을 크게 능가하며, 무선 FL에서 클라이언트 선택을 위한 강력하고 효율적인 접근법을 제공합니다.

## 🎯 주요 포인트

- 1. 무선 연합 학습(FL)에서 클라이언트 선택 문제를 해결하기 위해, 학습 정확도를 일정 수준으로 달성하는 데 필요한 총 시간을 줄이는 것을 목표로 합니다.
- 2. 클라이언트의 동적 상태를 관찰할 수 없는 서버 환경에서, 클라이언트 선택 문제를 restless multi-armed bandit 문제로 공식화하였습니다.
- 3. 제안된 WILF-Q(Wittle Index Learning in Federated Q-learning)는 Q-learning을 사용하여 각 클라이언트와 관련된 Whittle 지수를 학습하고 업데이트하며, 가장 높은 지수를 가진 클라이언트를 선택합니다.
- 4. WILF-Q는 클라이언트 상태 전이나 데이터 분포에 대한 명시적 지식이 필요하지 않아 실제 FL 환경에서의 배치에 적합합니다.
- 5. 실험 결과, WILF-Q는 기존의 기준 정책들에 비해 학습 효율성 면에서 크게 우수한 성능을 보였습니다.


---

*Generated on 2025-09-23 11:12:45*