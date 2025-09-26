---
keywords:
  - Control Barrier Functions
  - Hamilton-Jacobi Reachability Analysis
  - Hypernetwork-based Architecture
  - Observation-conditioned Neural Control Barrier Functions
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16614
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:11:47.941369",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Control Barrier Functions",
    "Hamilton-Jacobi Reachability Analysis",
    "Hypernetwork-based Architecture",
    "Observation-conditioned Neural Control Barrier Functions"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Control Barrier Functions": 0.78,
    "Hamilton-Jacobi Reachability Analysis": 0.8,
    "Hypernetwork-based Architecture": 0.77,
    "Observation-conditioned Neural Control Barrier Functions": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Control Barrier Functions",
        "canonical": "Control Barrier Functions",
        "aliases": [
          "CBFs"
        ],
        "category": "unique_technical",
        "rationale": "Control Barrier Functions are central to the paper's methodology and offer a unique approach to safety-critical control, making them a key concept for linking.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Hamilton-Jacobi Reachability Analysis",
        "canonical": "Hamilton-Jacobi Reachability Analysis",
        "aliases": [
          "HJ Reachability"
        ],
        "category": "specific_connectable",
        "rationale": "This analysis method is crucial for understanding the safety guarantees discussed in the paper, providing a strong link to mathematical safety analysis.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "Hypernetwork-based Architecture",
        "canonical": "Hypernetwork-based Architecture",
        "aliases": [
          "Hypernetwork Architecture"
        ],
        "category": "unique_technical",
        "rationale": "The use of hypernetworks is a novel approach in the context of observation-conditioned safety filters, offering a unique technical insight.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      },
      {
        "surface": "Observation-conditioned Neural CBFs",
        "canonical": "Observation-conditioned Neural Control Barrier Functions",
        "aliases": [
          "Observation-conditioned CBFs"
        ],
        "category": "unique_technical",
        "rationale": "This specific type of CBF is a novel contribution of the paper, providing a unique angle on safety-critical control.",
        "novelty_score": 0.8,
        "connectivity_score": 0.68,
        "specificity_score": 0.88,
        "link_intent_score": 0.79
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
      "candidate_surface": "Control Barrier Functions",
      "resolved_canonical": "Control Barrier Functions",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Hamilton-Jacobi Reachability Analysis",
      "resolved_canonical": "Hamilton-Jacobi Reachability Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Hypernetwork-based Architecture",
      "resolved_canonical": "Hypernetwork-based Architecture",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Observation-conditioned Neural CBFs",
      "resolved_canonical": "Observation-conditioned Neural Control Barrier Functions",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.68,
        "specificity": 0.88,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# ORN-CBF: Learning Observation-conditioned Residual Neural Control Barrier Functions via Hypernetworks

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16614.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16614](https://arxiv.org/abs/2509.16614)

## 🔗 유사한 논문
- [[2025-09-18/Designing Latent Safety Filters using Pre-Trained Vision Models_20250918|Designing Latent Safety Filters using Pre-Trained Vision Models]] (83.9% similar)
- [[2025-09-19/Compositional Design of Safety Controllers for Large-scale Stochastic Hybrid Systems_20250919|Compositional Design of Safety Controllers for Large-scale Stochastic Hybrid Systems]] (83.3% similar)
- [[2025-09-23/Distributionally Robust Safety Verification of Neural Networks via Worst-Case CVaR_20250923|Distributionally Robust Safety Verification of Neural Networks via Worst-Case CVaR]] (82.8% similar)
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (81.7% similar)
- [[2025-09-19/Digital Twin-based Cooperative Autonomous Driving in Smart Intersections_ A Multi-Agent Reinforcement Learning Approach_20250919|Digital Twin-based Cooperative Autonomous Driving in Smart Intersections: A Multi-Agent Reinforcement Learning Approach]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Hamilton-Jacobi Reachability Analysis|Hamilton-Jacobi Reachability Analysis]]
**⚡ Unique Technical**: [[keywords/Control Barrier Functions|Control Barrier Functions]], [[keywords/Hypernetwork-based Architecture|Hypernetwork-based Architecture]], [[keywords/Observation-conditioned Neural Control Barrier Functions|Observation-conditioned Neural Control Barrier Functions]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16614v1 Announce Type: cross 
Abstract: Control barrier functions (CBFs) have been demonstrated as an effective method for safety-critical control of autonomous systems. Although CBFs are simple to deploy, their design remains challenging, motivating the development of learning-based approaches. Yet, issues such as suboptimal safe sets, applicability in partially observable environments, and lack of rigorous safety guarantees persist. In this work, we propose observation-conditioned neural CBFs based on Hamilton-Jacobi (HJ) reachability analysis, which approximately recover the maximal safe sets. We exploit certain mathematical properties of the HJ value function, ensuring that the predicted safe set never intersects with the observed failure set. Moreover, we leverage a hypernetwork-based architecture that is particularly suitable for the design of observation-conditioned safety filters. The proposed method is examined both in simulation and hardware experiments for a ground robot and a quadcopter. The results show improved success rates and generalization to out-of-domain environments compared to the baselines.

## 📝 요약

이 논문은 자율 시스템의 안전을 보장하기 위한 제어 장벽 함수(CBF)의 설계 문제를 해결하기 위해 관찰 조건부 신경망 CBF를 제안합니다. 이 방법은 Hamilton-Jacobi 도달 가능성 분석을 기반으로 하며, 최대 안전 집합을 근사적으로 복원합니다. HJ 값 함수의 수학적 특성을 활용하여 예측된 안전 집합이 관찰된 실패 집합과 교차하지 않도록 보장합니다. 또한, 관찰 조건부 안전 필터 설계에 적합한 하이퍼네트워크 기반 아키텍처를 사용합니다. 지상 로봇과 쿼드콥터를 대상으로 한 시뮬레이션 및 하드웨어 실험에서 이 방법은 기존 방법들보다 높은 성공률과 범주 외 환경에 대한 일반화 능력을 보여주었습니다.

## 🎯 주요 포인트

- 1. 본 연구에서는 Hamilton-Jacobi 도달 가능성 분석을 기반으로 한 관찰 조건부 신경망 제어 장벽 함수(Neural CBFs)를 제안하여 최대 안전 집합을 근사적으로 복원합니다.
- 2. HJ 값 함수의 수학적 특성을 활용하여 예측된 안전 집합이 관찰된 실패 집합과 절대 교차하지 않도록 보장합니다.
- 3. 관찰 조건부 안전 필터 설계에 적합한 하이퍼네트워크 기반 아키텍처를 활용합니다.
- 4. 제안된 방법은 지상 로봇과 쿼드콥터에 대한 시뮬레이션 및 하드웨어 실험에서 기존 방법보다 높은 성공률과 범위 외 환경에 대한 일반화를 보여줍니다.


---

*Generated on 2025-09-24 02:11:47*