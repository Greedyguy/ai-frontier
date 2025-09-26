---
keywords:
  - Variational Quantum Eigensolvers
  - Parameter Initialization
  - Noisy Intermediate-Scale Quantum
  - Optimization Trajectories
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17322
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:52:14.949382",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Variational Quantum Eigensolvers",
    "Parameter Initialization",
    "Noisy Intermediate-Scale Quantum",
    "Optimization Trajectories"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Variational Quantum Eigensolvers": 0.85,
    "Parameter Initialization": 0.68,
    "Noisy Intermediate-Scale Quantum": 0.8,
    "Optimization Trajectories": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Variational Quantum Eigensolvers",
        "canonical": "Variational Quantum Eigensolvers",
        "aliases": [
          "VQE"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper, VQEs are a specific quantum computing algorithm that benefits from dataset connections.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Parameter Initialization",
        "canonical": "Parameter Initialization",
        "aliases": [
          "Initialization"
        ],
        "category": "broad_technical",
        "rationale": "Crucial for VQE performance, linking to broader machine learning concepts.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.6,
        "link_intent_score": 0.68
      },
      {
        "surface": "Noisy Intermediate-Scale Quantum",
        "canonical": "Noisy Intermediate-Scale Quantum",
        "aliases": [
          "NISQ"
        ],
        "category": "unique_technical",
        "rationale": "Describes the current era of quantum computing, relevant for connecting to quantum algorithm discussions.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Optimization Trajectories",
        "canonical": "Optimization Trajectories",
        "aliases": [
          "Optimization Paths"
        ],
        "category": "specific_connectable",
        "rationale": "Key for understanding VQE performance, linking to optimization methods in machine learning.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "dataset",
      "performance",
      "resources"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Variational Quantum Eigensolvers",
      "resolved_canonical": "Variational Quantum Eigensolvers",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Parameter Initialization",
      "resolved_canonical": "Parameter Initialization",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.6,
        "link_intent": 0.68
      }
    },
    {
      "candidate_surface": "Noisy Intermediate-Scale Quantum",
      "resolved_canonical": "Noisy Intermediate-Scale Quantum",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Optimization Trajectories",
      "resolved_canonical": "Optimization Trajectories",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# VQEzy: An Open-Source Dataset for Parameter Initialize in Variational Quantum Eigensolvers

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17322.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17322](https://arxiv.org/abs/2509.17322)

## 🔗 유사한 논문
- [[2025-09-18/TITAN_ A Trajectory-Informed Technique for Adaptive Parameter Freezing in Large-Scale VQE_20250918|TITAN: A Trajectory-Informed Technique for Adaptive Parameter Freezing in Large-Scale VQE]] (83.4% similar)
- [[2025-09-22/Training Variational Quantum Circuits Using Particle Swarm Optimization_20250922|Training Variational Quantum Circuits Using Particle Swarm Optimization]] (79.6% similar)
- [[2025-09-18/Learning AC Power Flow Solutions using a Data-Dependent Variational Quantum Circuit_20250918|Learning AC Power Flow Solutions using a Data-Dependent Variational Quantum Circuit]] (78.9% similar)
- [[2025-09-19/Trainability of Quantum Models Beyond Known Classical Simulability_20250919|Trainability of Quantum Models Beyond Known Classical Simulability]] (77.7% similar)
- [[2025-09-22/Triplet Loss Based Quantum Encoding for Class Separability_20250922|Triplet Loss Based Quantum Encoding for Class Separability]] (77.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Parameter Initialization|Parameter Initialization]]
**🔗 Specific Connectable**: [[keywords/Optimization Trajectories|Optimization Trajectories]]
**⚡ Unique Technical**: [[keywords/Variational Quantum Eigensolvers|Variational Quantum Eigensolvers]], [[keywords/Noisy Intermediate-Scale Quantum|Noisy Intermediate-Scale Quantum]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17322v1 Announce Type: new 
Abstract: Variational Quantum Eigensolvers (VQEs) are a leading class of noisy intermediate-scale quantum (NISQ) algorithms, whose performance is highly sensitive to parameter initialization. Although recent machine learning-based initialization methods have achieved state-of-the-art performance, their progress has been limited by the lack of comprehensive datasets. Existing resources are typically restricted to a single domain, contain only a few hundred instances, and lack complete coverage of Hamiltonians, ansatz circuits, and optimization trajectories. To overcome these limitations, we introduce VQEzy, the first large-scale dataset for VQE parameter initialization. VQEzy spans three major domains and seven representative tasks, comprising 12,110 instances with full VQE specifications and complete optimization trajectories. The dataset is available online, and will be continuously refined and expanded to support future research in VQE optimization.

## 📝 요약

Variational Quantum Eigensolvers (VQEs)는 NISQ 알고리즘의 일종으로, 성능이 매개변수 초기화에 크게 의존합니다. 기존의 머신러닝 기반 초기화 방법은 데이터셋의 부족으로 한계가 있었습니다. 이를 해결하기 위해, 우리는 VQEzy라는 대규모 데이터셋을 소개합니다. VQEzy는 세 가지 주요 도메인과 일곱 가지 대표 과제를 포함하며, 12,110개의 인스턴스를 제공하여 VQE 최적화 연구를 지원합니다. 이 데이터셋은 온라인에서 이용 가능하며, 지속적으로 개선될 예정입니다.

## 🎯 주요 포인트

- 1. VQE는 NISQ 알고리즘의 주요 클래스이며, 성능은 매개변수 초기화에 매우 민감하다.
- 2. 기존의 머신러닝 기반 초기화 방법은 데이터셋의 부족으로 인해 발전이 제한적이었다.
- 3. VQEzy는 VQE 매개변수 초기화를 위한 최초의 대규모 데이터셋으로, 세 가지 주요 도메인과 일곱 가지 대표적인 작업을 포함한다.
- 4. VQEzy는 12,110개의 인스턴스를 포함하며, 완전한 VQE 사양과 최적화 경로를 제공한다.
- 5. 이 데이터셋은 온라인에서 이용 가능하며, VQE 최적화 연구를 지원하기 위해 지속적으로 개선 및 확장될 것이다.


---

*Generated on 2025-09-24 01:52:14*