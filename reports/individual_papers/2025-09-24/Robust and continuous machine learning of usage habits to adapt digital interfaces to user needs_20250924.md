<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:45:38.911645",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Learning",
    "Bayesian Statistics",
    "Incremental Learning",
    "Adaptive Systems",
    "Task Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Learning": 0.85,
    "Bayesian Statistics": 0.8,
    "Incremental Learning": 0.82,
    "Adaptive Systems": 0.78,
    "Task Model": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "machine learning",
        "canonical": "Machine Learning",
        "aliases": [
          "ML"
        ],
        "category": "broad_technical",
        "rationale": "Machine Learning is a foundational concept that connects to various adaptive systems and algorithms.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Bayesian statistics",
        "canonical": "Bayesian Statistics",
        "aliases": [
          "Bayesian methods"
        ],
        "category": "specific_connectable",
        "rationale": "Bayesian Statistics is crucial for modeling user behavior and is a key component of the algorithm described.",
        "novelty_score": 0.7,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "online incremental learning",
        "canonical": "Incremental Learning",
        "aliases": [
          "online learning"
        ],
        "category": "specific_connectable",
        "rationale": "Incremental Learning is essential for adapting to changing environments and user behaviors.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "adaptive systems",
        "canonical": "Adaptive Systems",
        "aliases": [
          "adaptive interfaces"
        ],
        "category": "unique_technical",
        "rationale": "Adaptive Systems represent the overarching goal of the research, linking to user experience improvements.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "task model",
        "canonical": "Task Model",
        "aliases": [
          "task representation"
        ],
        "category": "unique_technical",
        "rationale": "Task Model is a unique aspect of the research, providing a graphical representation of user navigation.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "digital interfaces",
      "user needs"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "machine learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Bayesian statistics",
      "resolved_canonical": "Bayesian Statistics",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "online incremental learning",
      "resolved_canonical": "Incremental Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "adaptive systems",
      "resolved_canonical": "Adaptive Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "task model",
      "resolved_canonical": "Task Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Robust and continuous machine learning of usage habits to adapt digital interfaces to user needs

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18117.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18117](https://arxiv.org/abs/2509.18117)

## 🔗 유사한 논문
- [[2025-09-17/Online Bayesian Risk-Averse Reinforcement Learning_20250917|Online Bayesian Risk-Averse Reinforcement Learning]] (82.6% similar)
- [[2025-09-22/Dynamic Policy Fusion for User Alignment Without Re-Interaction_20250922|Dynamic Policy Fusion for User Alignment Without Re-Interaction]] (81.8% similar)
- [[2025-09-22/AgentA/B_ Automated and Scalable Web A/BTesting with Interactive LLM Agents_20250922|AgentA/B: Automated and Scalable Web A/BTesting with Interactive LLM Agents]] (81.7% similar)
- [[2025-09-23/Statistical Inference for Misspecified Contextual Bandits_20250923|Statistical Inference for Misspecified Contextual Bandits]] (81.4% similar)
- [[2025-09-24/BRAID_ Input-Driven Nonlinear Dynamical Modeling of Neural-Behavioral Data_20250924|BRAID: Input-Driven Nonlinear Dynamical Modeling of Neural-Behavioral Data]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**🔗 Specific Connectable**: [[keywords/Bayesian Statistics|Bayesian Statistics]], [[keywords/Incremental Learning|Incremental Learning]]
**⚡ Unique Technical**: [[keywords/Adaptive Systems|Adaptive Systems]], [[keywords/Task Model|Task Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18117v1 Announce Type: new 
Abstract: The paper presents a machine learning approach to design digital interfaces that can dynamically adapt to different users and usage strategies. The algorithm uses Bayesian statistics to model users' browsing behavior, focusing on their habits rather than group preferences. It is distinguished by its online incremental learning, allowing reliable predictions even with little data and in the case of a changing environment. This inference method generates a task model, providing a graphical representation of navigation with the usage statistics of the current user. The algorithm learns new tasks while preserving prior knowledge. The theoretical framework is described, and simulations show the effectiveness of the approach in stationary and non-stationary environments. In conclusion, this research paves the way for adaptive systems that improve the user experience by helping them to better navigate and act on their interface.

## 📝 요약

이 논문은 사용자와 사용 전략에 따라 동적으로 적응하는 디지털 인터페이스를 설계하기 위한 머신러닝 접근법을 제시합니다. 베이지안 통계를 사용하여 사용자의 브라우징 행동을 모델링하며, 그룹 선호보다는 개인의 습관에 초점을 맞춥니다. 온라인 점진적 학습을 통해 적은 데이터와 변화하는 환경에서도 신뢰할 수 있는 예측이 가능합니다. 이 방법론은 사용자 현재 사용 통계를 그래픽으로 나타내는 작업 모델을 생성합니다. 새로운 작업을 학습하면서도 기존 지식을 유지하며, 이론적 틀과 시뮬레이션을 통해 정적 및 비정적 환경에서의 효과성을 입증합니다. 이 연구는 사용자 경험을 향상시키는 적응형 시스템 개발에 기여합니다.

## 🎯 주요 포인트

- 1. 본 논문은 사용자와 사용 전략에 따라 동적으로 적응하는 디지털 인터페이스 설계를 위한 기계 학습 접근법을 제시합니다.
- 2. 알고리즘은 베이지안 통계를 사용하여 그룹 선호가 아닌 사용자의 브라우징 습관을 모델링합니다.
- 3. 온라인 증분 학습을 통해 적은 데이터와 변화하는 환경에서도 신뢰할 수 있는 예측이 가능합니다.
- 4. 이 추론 방법은 현재 사용자의 사용 통계를 포함한 탐색의 그래픽 표현을 제공하는 작업 모델을 생성합니다.
- 5. 이 연구는 사용자 경험을 개선하는 적응형 시스템 개발의 가능성을 열어줍니다.


---

*Generated on 2025-09-24 14:45:38*