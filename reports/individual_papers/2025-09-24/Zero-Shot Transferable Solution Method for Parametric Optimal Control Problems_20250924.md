<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:08:44.243910",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Zero-Shot Learning",
    "Neural Network",
    "Function Encoder Policies",
    "Offline-Online Decomposition"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Zero-Shot Learning": 0.82,
    "Neural Network": 0.78,
    "Function Encoder Policies": 0.75,
    "Offline-Online Decomposition": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Zero-Shot Adaptation",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot Transfer"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to the trend of adapting models to new tasks without retraining, enhancing cross-domain applicability.",
        "novelty_score": 0.65,
        "connectivity_score": 0.88,
        "specificity_score": 0.79,
        "link_intent_score": 0.82
      },
      {
        "surface": "Neural Basis Functions",
        "canonical": "Neural Network",
        "aliases": [
          "Neural Basis",
          "Basis Functions"
        ],
        "category": "broad_technical",
        "rationale": "Links to neural network architectures, emphasizing reusable components for control policies.",
        "novelty_score": 0.58,
        "connectivity_score": 0.85,
        "specificity_score": 0.72,
        "link_intent_score": 0.78
      },
      {
        "surface": "Function Encoder Policies",
        "canonical": "Function Encoder Policies",
        "aliases": [
          "FE Policies"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel approach in control problems, enhancing the understanding of policy encoding.",
        "novelty_score": 0.72,
        "connectivity_score": 0.67,
        "specificity_score": 0.81,
        "link_intent_score": 0.75
      },
      {
        "surface": "Offline-Online Decomposition",
        "canonical": "Offline-Online Decomposition",
        "aliases": [
          "Offline-Online Method"
        ],
        "category": "unique_technical",
        "rationale": "Highlights a key methodological innovation for efficient adaptation in control systems.",
        "novelty_score": 0.68,
        "connectivity_score": 0.73,
        "specificity_score": 0.77,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "optimization-based approaches",
      "numerical experiments",
      "real-time deployment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Zero-Shot Adaptation",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.88,
        "specificity": 0.79,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Neural Basis Functions",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.85,
        "specificity": 0.72,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Function Encoder Policies",
      "resolved_canonical": "Function Encoder Policies",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.67,
        "specificity": 0.81,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Offline-Online Decomposition",
      "resolved_canonical": "Offline-Online Decomposition",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.73,
        "specificity": 0.77,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Zero-Shot Transferable Solution Method for Parametric Optimal Control Problems

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18404.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18404](https://arxiv.org/abs/2509.18404)

## 🔗 유사한 논문
- [[2025-09-23/Were Residual Penalty and Neural Operators All We Needed for Solving Optimal Control Problems?_20250923|Were Residual Penalty and Neural Operators All We Needed for Solving Optimal Control Problems?]] (84.1% similar)
- [[2025-09-19/Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (84.0% similar)
- [[2025-09-23/Joint Optimization of Multi-Objective Reinforcement Learning with Policy Gradient Based Algorithm_20250923|Joint Optimization of Multi-Objective Reinforcement Learning with Policy Gradient Based Algorithm]] (83.4% similar)
- [[2025-09-23/ROOT_ Rethinking Offline Optimization as Distributional Translation via Probabilistic Bridge_20250923|ROOT: Rethinking Offline Optimization as Distributional Translation via Probabilistic Bridge]] (83.0% similar)
- [[2025-09-22/Mind the Gap_ Data Rewriting for Stable Off-Policy Supervised Fine-Tuning_20250922|Mind the Gap: Data Rewriting for Stable Off-Policy Supervised Fine-Tuning]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Function Encoder Policies|Function Encoder Policies]], [[keywords/Offline-Online Decomposition|Offline-Online Decomposition]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18404v1 Announce Type: cross 
Abstract: This paper presents a transferable solution method for optimal control problems with varying objectives using function encoder (FE) policies. Traditional optimization-based approaches must be re-solved whenever objectives change, resulting in prohibitive computational costs for applications requiring frequent evaluation and adaptation. The proposed method learns a reusable set of neural basis functions that spans the control policy space, enabling efficient zero-shot adaptation to new tasks through either projection from data or direct mapping from problem specifications. The key idea is an offline-online decomposition: basis functions are learned once during offline imitation learning, while online adaptation requires only lightweight coefficient estimation. Numerical experiments across diverse dynamics, dimensions, and cost structures show our method delivers near-optimal performance with minimal overhead when generalizing across tasks, enabling semi-global feedback policies suitable for real-time deployment.

## 📝 요약

이 논문은 함수 인코더(FE) 정책을 활용하여 목표가 변하는 최적 제어 문제에 대한 전이 가능한 해결 방법을 제시합니다. 기존의 최적화 기반 접근법은 목표가 변경될 때마다 문제를 다시 해결해야 하므로 계산 비용이 많이 듭니다. 제안된 방법은 제어 정책 공간을 아우르는 신경 기저 함수를 학습하여 새로운 작업에 대해 데이터 투영이나 문제 사양으로부터의 직접 매핑을 통해 효율적인 제로샷 적응을 가능하게 합니다. 핵심 아이디어는 오프라인-온라인 분해로, 기저 함수는 오프라인 모방 학습 중에 한 번 학습되고, 온라인 적응은 가벼운 계수 추정만 필요합니다. 다양한 동역학, 차원 및 비용 구조에 대한 수치 실험에서 이 방법이 최소한의 오버헤드로 거의 최적의 성능을 제공하며, 실시간 배포에 적합한 준-글로벌 피드백 정책을 가능하게 함을 보여줍니다.

## 🎯 주요 포인트

- 1. 본 논문은 함수 인코더(FE) 정책을 사용하여 목표가 변하는 최적 제어 문제에 대한 전이 가능한 해결 방법을 제시합니다.
- 2. 제안된 방법은 제어 정책 공간을 아우르는 신경 기저 함수를 학습하여 새로운 작업에 대한 효율적인 제로샷 적응을 가능하게 합니다.
- 3. 오프라인-온라인 분해 접근 방식을 통해 오프라인 모방 학습 시 기저 함수를 학습하고, 온라인 적응 시에는 경량 계수 추정만 필요합니다.
- 4. 다양한 동역학, 차원 및 비용 구조에 대한 수치 실험에서 제안된 방법은 최소한의 오버헤드로 거의 최적의 성능을 제공함을 보여줍니다.
- 5. 본 방법은 실시간 배포에 적합한 준-글로벌 피드백 정책을 가능하게 합니다.


---

*Generated on 2025-09-24 15:08:44*