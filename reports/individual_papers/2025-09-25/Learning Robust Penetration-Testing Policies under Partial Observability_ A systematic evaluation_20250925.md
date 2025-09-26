---
keywords:
  - Penetration Testing
  - Partial Observability
  - Proximal Policy Optimization
  - Machine Learning
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.20008
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:44:29.163203",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Penetration Testing",
    "Partial Observability",
    "Proximal Policy Optimization",
    "Machine Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Penetration Testing": 0.78,
    "Partial Observability": 0.77,
    "Proximal Policy Optimization": 0.8,
    "Machine Learning": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Penetration Testing",
        "canonical": "Penetration Testing",
        "aliases": [
          "Pentesting",
          "Security Testing"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus on cybersecurity and is specific to the domain of security assessments.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Partial Observability",
        "canonical": "Partial Observability",
        "aliases": [
          "Partial Observation"
        ],
        "category": "unique_technical",
        "rationale": "Partial observability is a key challenge in the paper, affecting the design of reinforcement learning algorithms.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Proximal Policy Optimization",
        "canonical": "Proximal Policy Optimization",
        "aliases": [
          "PPO"
        ],
        "category": "broad_technical",
        "rationale": "PPO is a widely used reinforcement learning algorithm, relevant for linking discussions on RL techniques.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Reinforcement Learning",
        "canonical": "Machine Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement learning is a core aspect of the study, linking to broader discussions in machine learning.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "sequential decision-making",
      "real-world environments"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Penetration Testing",
      "resolved_canonical": "Penetration Testing",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Partial Observability",
      "resolved_canonical": "Partial Observability",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Proximal Policy Optimization",
      "resolved_canonical": "Proximal Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Learning Robust Penetration-Testing Policies under Partial Observability: A systematic evaluation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20008.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.20008](https://arxiv.org/abs/2509.20008)

## 🔗 유사한 논문
- [[2025-09-22/PVPO_ Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning_20250922|PVPO: Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning]] (83.3% similar)
- [[2025-09-19/Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (82.9% similar)
- [[2025-09-19/Online Learning of Deceptive Policies under Intermittent Observation_20250919|Online Learning of Deceptive Policies under Intermittent Observation]] (82.9% similar)
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (82.3% similar)
- [[2025-09-24/Online Process Reward Leanring for Agentic Reinforcement Learning_20250924|Online Process Reward Leanring for Agentic Reinforcement Learning]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Proximal Policy Optimization|Proximal Policy Optimization]], [[keywords/Machine Learning|Machine Learning]]
**⚡ Unique Technical**: [[keywords/Penetration Testing|Penetration Testing]], [[keywords/Partial Observability|Partial Observability]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20008v1 Announce Type: new 
Abstract: Penetration testing, the simulation of cyberattacks to identify security vulnerabilities, presents a sequential decision-making problem well-suited for reinforcement learning (RL) automation. Like many applications of RL to real-world problems, partial observability presents a major challenge, as it invalidates the Markov property present in Markov Decision Processes (MDPs). Partially Observable MDPs require history aggregation or belief state estimation to learn successful policies. We investigate stochastic, partially observable penetration testing scenarios over host networks of varying size, aiming to better reflect real-world complexity through more challenging and representative benchmarks. This approach leads to the development of more robust and transferable policies, which are crucial for ensuring reliable performance across diverse and unpredictable real-world environments. Using vanilla Proximal Policy Optimization (PPO) as a baseline, we compare a selection of PPO variants designed to mitigate partial observability, including frame-stacking, augmenting observations with historical information, and employing recurrent or transformer-based architectures. We conduct a systematic empirical analysis of these algorithms across different host network sizes. We find that this task greatly benefits from history aggregation. Converging three times faster than other approaches. Manual inspection of the learned policies by the algorithms reveals clear distinctions and provides insights that go beyond quantitative results.

## 📝 요약

이 논문은 침투 테스트에서 강화 학습(RL)을 활용하여 보안 취약점을 식별하는 방법을 연구합니다. 부분 관찰 가능성 문제를 해결하기 위해 다양한 PPO(근접 정책 최적화) 변형을 비교하며, 특히 역사 정보의 집계가 중요한 역할을 한다는 것을 발견했습니다. 실험 결과, 역사 정보 집계를 통한 방법이 다른 방법들보다 세 배 빠르게 수렴하며, 학습된 정책의 수동 검토를 통해 정량적 결과를 넘어선 통찰을 제공합니다. 이 연구는 다양한 네트워크 크기에서의 실험을 통해 현실 세계의 복잡성을 더 잘 반영하는 강력하고 전이 가능한 정책 개발에 기여합니다.

## 🎯 주요 포인트

- 1. 침투 테스트는 강화 학습 자동화에 적합한 순차적 의사 결정 문제를 제시합니다.
- 2. 부분 관찰 가능성은 MDP의 마르코프 속성을 무효화하여 강화 학습에 주요 도전 과제를 제공합니다.
- 3. 다양한 크기의 호스트 네트워크에서 부분 관찰 가능한 침투 테스트 시나리오를 조사하여 현실 세계의 복잡성을 더 잘 반영하려고 합니다.
- 4. 역사 집계 또는 신념 상태 추정은 성공적인 정책 학습에 필수적이며, 이는 다양한 환경에서 신뢰할 수 있는 성능을 보장하는 데 중요합니다.
- 5. Vanilla PPO와 다양한 변형을 비교한 결과, 역사 집계가 학습 속도를 세 배 빠르게 향상시킵니다.


---

*Generated on 2025-09-25 16:44:29*