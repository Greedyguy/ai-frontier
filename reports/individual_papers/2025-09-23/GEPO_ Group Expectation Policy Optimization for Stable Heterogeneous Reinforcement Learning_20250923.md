---
keywords:
  - Heterogeneous Reinforcement Learning
  - Group Expectation Policy Optimization
  - Decentralized Training
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2508.17850
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:22:41.302361",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Heterogeneous Reinforcement Learning",
    "Group Expectation Policy Optimization",
    "Decentralized Training"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Heterogeneous Reinforcement Learning": 0.78,
    "Group Expectation Policy Optimization": 0.8,
    "Decentralized Training": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Heterogeneous Reinforcement Learning",
        "canonical": "Heterogeneous Reinforcement Learning",
        "aliases": [
          "HeteroRL"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's contribution and represents a novel approach to RL in decentralized environments.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Group Expectation Policy Optimization",
        "canonical": "Group Expectation Policy Optimization",
        "aliases": [
          "GEPO"
        ],
        "category": "unique_technical",
        "rationale": "GEPO is a novel algorithm introduced in the paper, crucial for addressing latency issues in distributed RL.",
        "novelty_score": 0.82,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.8
      },
      {
        "surface": "Decentralized Training",
        "canonical": "Decentralized Training",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Decentralized training is a key context for the paper's methodology, linking it to broader trends in distributed computing.",
        "novelty_score": 0.55,
        "connectivity_score": 0.77,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Heterogeneous Reinforcement Learning",
      "resolved_canonical": "Heterogeneous Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Group Expectation Policy Optimization",
      "resolved_canonical": "Group Expectation Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.82,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Decentralized Training",
      "resolved_canonical": "Decentralized Training",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.77,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# GEPO: Group Expectation Policy Optimization for Stable Heterogeneous Reinforcement Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2508.17850.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2508.17850](https://arxiv.org/abs/2508.17850)

## 🔗 유사한 논문
- [[2025-09-19/Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (83.1% similar)
- [[2025-09-19/Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (82.5% similar)
- [[2025-09-22/PVPO_ Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning_20250922|PVPO: Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning]] (82.2% similar)
- [[2025-09-22/RLinf_ Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation_20250922|RLinf: Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation]] (82.1% similar)
- [[2025-09-23/Sample-Efficient Reinforcement Learning with Symmetry-Guided Demonstrations for Robotic Manipulation_20250923|Sample-Efficient Reinforcement Learning with Symmetry-Guided Demonstrations for Robotic Manipulation]] (82.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Decentralized Training|Decentralized Training]]
**⚡ Unique Technical**: [[keywords/Heterogeneous Reinforcement Learning|Heterogeneous Reinforcement Learning]], [[keywords/Group Expectation Policy Optimization|Group Expectation Policy Optimization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.17850v5 Announce Type: replace-cross 
Abstract: As single-center computing approaches power constraints, decentralized training becomes essential. However, traditional Reinforcement Learning (RL) methods, crucial for enhancing large model post-training, cannot adapt to decentralized distributed training due to the tight coupling between parameter learning and rollout sampling. For this, we propose HeteroRL, a heterogeneous RL architecture that decouples these processes, enabling stable training across geographically distributed nodes connected via the Internet. The core component is Group Expectation Policy Optimization (GEPO), an asynchronous RL algorithm robust to latency caused by network delays or heterogeneity in computational resources. Our study reveals that high latency significantly increases KL divergence, leading to higher variance in importance sampling weights and training instability. GEPO mitigates this issue by using group expectation weighting to exponentially reduce the variance of importance weights, with theoretical guarantees. Experiments show that GEPO achieves superior stability, with only a 3\% performance drop from online to 1800s latency, demonstrating strong potential for decentralized RL in geographically distributed, resource-heterogeneous computing environments.

## 📝 요약

이 논문은 단일 센터 컴퓨팅의 전력 제약을 극복하기 위해 분산형 훈련의 필요성을 강조하며, 전통적인 강화 학습(RL) 방법이 분산형 훈련에 적합하지 않음을 지적합니다. 이를 해결하기 위해 HeteroRL이라는 이질적 RL 아키텍처를 제안합니다. 이 아키텍처는 매개변수 학습과 롤아웃 샘플링을 분리하여 인터넷으로 연결된 지리적으로 분산된 노드에서 안정적인 훈련을 가능하게 합니다. 핵심 요소인 그룹 기대 정책 최적화(GEPO)는 네트워크 지연이나 계산 자원의 이질성에 강한 비동기식 RL 알고리즘입니다. 연구 결과, 높은 지연이 KL 발산을 증가시켜 중요도 샘플링 가중치의 분산을 높이고 훈련의 불안정을 초래함을 밝혔습니다. GEPO는 그룹 기대 가중치를 사용하여 이 문제를 해결하며, 이론적으로 가중치의 분산을 지수적으로 감소시킵니다. 실험 결과, GEPO는 온라인에서 1800초 지연까지 3%의 성능 저하만을 보이며, 지리적으로 분산되고 자원이 이질적인 환경에서의 분산형 RL에 강력한 잠재력을 보여줍니다.

## 🎯 주요 포인트

- 1. HeteroRL은 매개변수 학습과 롤아웃 샘플링을 분리하여 분산된 환경에서 안정적인 훈련을 가능하게 하는 이종 강화 학습 아키텍처입니다.
- 2. Group Expectation Policy Optimization (GEPO)은 네트워크 지연이나 자원 이질성으로 인한 지연에 강한 비동기식 강화 학습 알고리즘입니다.
- 3. 높은 지연은 KL 발산을 증가시켜 중요도 샘플링 가중치의 분산을 높이고 훈련의 불안정을 초래하지만, GEPO는 그룹 기대 가중치를 사용하여 이를 완화합니다.
- 4. GEPO는 이론적 보장을 통해 중요도 가중치의 분산을 기하급수적으로 줄이며, 실험 결과 온라인에서 1800초 지연까지 성능이 3%만 감소하는 안정성을 보여줍니다.
- 5. GEPO는 지리적으로 분산되고 자원이 이질적인 컴퓨팅 환경에서 분산 강화 학습의 강력한 잠재력을 입증합니다.


---

*Generated on 2025-09-24 01:22:41*