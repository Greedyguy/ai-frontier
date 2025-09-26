<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:58:45.090956",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Behavior Cloning",
    "Domain Adaptation",
    "Optimal Transport",
    "Simulation Data",
    "Unbalanced Optimal Transport"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Behavior Cloning": 0.75,
    "Domain Adaptation": 0.79,
    "Optimal Transport": 0.78,
    "Simulation Data": 0.72,
    "Unbalanced Optimal Transport": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Behavior Cloning",
        "canonical": "Behavior Cloning",
        "aliases": [
          "BC"
        ],
        "category": "specific_connectable",
        "rationale": "Behavior Cloning is a key technique in robot manipulation, linking it to machine learning and robotics.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.75
      },
      {
        "surface": "Domain Adaptation",
        "canonical": "Domain Adaptation",
        "aliases": [
          "DA"
        ],
        "category": "specific_connectable",
        "rationale": "Domain Adaptation is crucial for transferring policies from simulation to real-world applications.",
        "novelty_score": 0.58,
        "connectivity_score": 0.83,
        "specificity_score": 0.76,
        "link_intent_score": 0.79
      },
      {
        "surface": "Optimal Transport",
        "canonical": "Optimal Transport",
        "aliases": [
          "OT"
        ],
        "category": "unique_technical",
        "rationale": "Optimal Transport is a mathematical concept applied here to align distributions, enhancing policy transfer.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Simulation Data",
        "canonical": "Simulation Data",
        "aliases": [
          "Sim Data"
        ],
        "category": "broad_technical",
        "rationale": "Simulation Data is fundamental for training policies before real-world application.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.72
      },
      {
        "surface": "Unbalanced Optimal Transport",
        "canonical": "Unbalanced Optimal Transport",
        "aliases": [
          "Unbalanced OT"
        ],
        "category": "unique_technical",
        "rationale": "Unbalanced Optimal Transport addresses data imbalance, a novel approach in this context.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Behavior Cloning",
      "resolved_canonical": "Behavior Cloning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Domain Adaptation",
      "resolved_canonical": "Domain Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.83,
        "specificity": 0.76,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Optimal Transport",
      "resolved_canonical": "Optimal Transport",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Simulation Data",
      "resolved_canonical": "Simulation Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Unbalanced Optimal Transport",
      "resolved_canonical": "Unbalanced Optimal Transport",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18631.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18631](https://arxiv.org/abs/2509.18631)

## 🔗 유사한 논문
- [[2025-09-23/The Sound of Simulation_ Learning Multimodal Sim-to-Real Robot Policies with Generative Audio_20250923|The Sound of Simulation: Learning Multimodal Sim-to-Real Robot Policies with Generative Audio]] (85.9% similar)
- [[2025-09-23/Latent Policy Steering with Embodiment-Agnostic Pretrained World Models_20250923|Latent Policy Steering with Embodiment-Agnostic Pretrained World Models]] (85.1% similar)
- [[2025-09-19/ActivePusher_ Active Learning and Planning with Residual Physics for Nonprehensile Manipulation_20250919|ActivePusher: Active Learning and Planning with Residual Physics for Nonprehensile Manipulation]] (83.7% similar)
- [[2025-09-18/Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning_20250918|Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning]] (83.6% similar)
- [[2025-09-23/End-to-end RL Improves Dexterous Grasping Policies_20250923|End-to-end RL Improves Dexterous Grasping Policies]] (83.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Simulation Data|Simulation Data]]
**🔗 Specific Connectable**: [[keywords/Behavior Cloning|Behavior Cloning]], [[keywords/Domain Adaptation|Domain Adaptation]]
**⚡ Unique Technical**: [[keywords/Optimal Transport|Optimal Transport]], [[keywords/Unbalanced Optimal Transport|Unbalanced Optimal Transport]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18631v1 Announce Type: cross 
Abstract: Behavior cloning has shown promise for robot manipulation, but real-world demonstrations are costly to acquire at scale. While simulated data offers a scalable alternative, particularly with advances in automated demonstration generation, transferring policies to the real world is hampered by various simulation and real domain gaps. In this work, we propose a unified sim-and-real co-training framework for learning generalizable manipulation policies that primarily leverages simulation and only requires a few real-world demonstrations. Central to our approach is learning a domain-invariant, task-relevant feature space. Our key insight is that aligning the joint distributions of observations and their corresponding actions across domains provides a richer signal than aligning observations (marginals) alone. We achieve this by embedding an Optimal Transport (OT)-inspired loss within the co-training framework, and extend this to an Unbalanced OT framework to handle the imbalance between abundant simulation data and limited real-world examples. We validate our method on challenging manipulation tasks, showing it can leverage abundant simulation data to achieve up to a 30% improvement in the real-world success rate and even generalize to scenarios seen only in simulation.

## 📝 요약

이 논문은 로봇 조작을 위한 행동 복제를 다루며, 시뮬레이션 데이터를 활용하여 실제 환경에서의 정책 전이를 개선하는 방법을 제안합니다. 저자들은 시뮬레이션과 실제 환경 간의 도메인 차이를 극복하기 위해, 시뮬레이션과 실제 데이터를 함께 학습하는 통합 프레임워크를 개발했습니다. 이 방법의 핵심은 도메인 불변의 작업 관련 특징 공간을 학습하는 것으로, 관찰과 행동의 공동 분포를 정렬하는 것이 더 풍부한 학습 신호를 제공한다는 점을 발견했습니다. 이를 위해 최적 수송(Optimal Transport) 기반의 손실을 사용하고, 시뮬레이션 데이터와 실제 데이터 간의 불균형을 처리하기 위해 비균형 OT(Unbalanced OT) 프레임워크로 확장했습니다. 실험 결과, 이 방법은 시뮬레이션 데이터를 활용하여 실제 환경에서 최대 30%의 성공률 향상을 이루었으며, 시뮬레이션에서만 본 시나리오에도 일반화할 수 있음을 보여주었습니다.

## 🎯 주요 포인트

- 1. 시뮬레이션과 현실 간의 격차를 줄이기 위해 시뮬레이션과 현실을 통합한 공동 학습 프레임워크를 제안합니다.
- 2. 도메인 불변적이고 작업 관련성이 높은 특징 공간을 학습하여 일반화 가능한 조작 정책을 개발합니다.
- 3. 최적 수송(Optimal Transport) 기반의 손실을 공동 학습 프레임워크에 포함시켜 도메인 간 관측 및 행동의 결합 분포를 정렬합니다.
- 4. 시뮬레이션 데이터와 제한된 현실 세계 예제 간의 불균형을 처리하기 위해 비균형 최적 수송(Unbalanced OT) 프레임워크를 확장합니다.
- 5. 제안된 방법은 시뮬레이션 데이터를 활용하여 현실 세계 성공률을 최대 30% 향상시키고, 시뮬레이션에서만 본 시나리오에도 일반화할 수 있음을 보여줍니다.


---

*Generated on 2025-09-24 13:58:45*