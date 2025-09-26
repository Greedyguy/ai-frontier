---
keywords:
  - Quantum Learning Theory
  - Classical Shadows
  - Variational Quantum Algorithms
  - Hamiltonian Simulation
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2408.12199
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:15:32.460188",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Quantum Learning Theory",
    "Classical Shadows",
    "Variational Quantum Algorithms",
    "Hamiltonian Simulation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Quantum Learning Theory": 0.78,
    "Classical Shadows": 0.79,
    "Variational Quantum Algorithms": 0.81,
    "Hamiltonian Simulation": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "quantum learning theory",
        "canonical": "Quantum Learning Theory",
        "aliases": [
          "quantum learning"
        ],
        "category": "unique_technical",
        "rationale": "Quantum learning theory is a specialized area that connects quantum computing with machine learning, offering unique insights.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "classical shadows",
        "canonical": "Classical Shadows",
        "aliases": [
          "shadow tomography"
        ],
        "category": "unique_technical",
        "rationale": "Classical shadows are a novel technique in quantum computing that can be linked to various quantum measurement methods.",
        "novelty_score": 0.82,
        "connectivity_score": 0.68,
        "specificity_score": 0.88,
        "link_intent_score": 0.79
      },
      {
        "surface": "variational quantum algorithms",
        "canonical": "Variational Quantum Algorithms",
        "aliases": [
          "VQA"
        ],
        "category": "specific_connectable",
        "rationale": "Variational quantum algorithms are a key area in quantum computing with strong connections to optimization and machine learning.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.81
      },
      {
        "surface": "Hamiltonian simulation",
        "canonical": "Hamiltonian Simulation",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Hamiltonian simulation is a fundamental problem in quantum computing, relevant to both theoretical and practical applications.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "large-qubit state space",
      "measurement data",
      "prediction error"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "quantum learning theory",
      "resolved_canonical": "Quantum Learning Theory",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "classical shadows",
      "resolved_canonical": "Classical Shadows",
      "decision": "linked",
      "scores": {
        "novelty": 0.82,
        "connectivity": 0.68,
        "specificity": 0.88,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "variational quantum algorithms",
      "resolved_canonical": "Variational Quantum Algorithms",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Hamiltonian simulation",
      "resolved_canonical": "Hamiltonian Simulation",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Efficient Learning for Linear Properties of Bounded-Gate Quantum Circuits

**Korean Title:** 제한된 게이트 양자 회로의 선형 속성에 대한 효율적인 학습

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2408.12199.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2408.12199](https://arxiv.org/abs/2408.12199)

## 🔗 유사한 논문
- [[2025-09-22/Quantum Reinforcement Learning with Dynamic-Circuit Qubit Reuse and Grover-Based Trajectory Optimization_20250922|Quantum Reinforcement Learning with Dynamic-Circuit Qubit Reuse and Grover-Based Trajectory Optimization]] (85.6% similar)
- [[2025-09-17/Learning quantum many-body data locally_ A provably scalable framework_20250917|Learning quantum many-body data locally: A provably scalable framework]] (84.8% similar)
- [[2025-09-19/Trainability of Quantum Models Beyond Known Classical Simulability_20250919|Trainability of Quantum Models Beyond Known Classical Simulability]] (84.3% similar)
- [[2025-09-17/Efficiently learning depth-3 circuits via quantum agnostic boosting_20250917|Efficiently learning depth-3 circuits via quantum agnostic boosting]] (84.2% similar)
- [[2025-09-22/Double descent in quantum kernel methods_20250922|Double descent in quantum kernel methods]] (82.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Variational Quantum Algorithms|Variational Quantum Algorithms]], [[keywords/Hamiltonian Simulation|Hamiltonian Simulation]]
**⚡ Unique Technical**: [[keywords/Quantum Learning Theory|Quantum Learning Theory]], [[keywords/Classical Shadows|Classical Shadows]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2408.12199v2 Announce Type: replace-cross 
Abstract: The vast and complicated large-qubit state space forbids us to comprehensively capture the dynamics of modern quantum computers via classical simulations or quantum tomography. Recent progress in quantum learning theory prompts a crucial question: can linear properties of a large-qubit circuit with d tunable RZ gates and G-d Clifford gates be efficiently learned from measurement data generated by varying classical inputs? In this work, we prove that the sample complexity scaling linearly in $d$ is required to achieve a small prediction error, while the corresponding computational complexity may scale exponentially in d. To address this challenge, we propose a kernel-based method leveraging classical shadows and truncated trigonometric expansions, enabling a controllable trade-off between prediction accuracy and computational overhead. Our results advance two crucial realms in quantum computation: the exploration of quantum algorithms with practical utilities and learning-based quantum system certification. We conduct numerical simulations to validate our proposals across diverse scenarios, encompassing quantum information processing protocols, Hamiltonian simulation, and variational quantum algorithms up to 60 qubits.

## 🔍 Abstract (한글 번역)

arXiv:2408.12199v2 발표 유형: 교차 교체  
초록: 방대한 복잡성을 지닌 대형 큐비트 상태 공간은 고전적 시뮬레이션이나 양자 단층 촬영을 통해 현대 양자 컴퓨터의 동역학을 포괄적으로 포착하는 것을 금지합니다. 최근 양자 학습 이론의 진전은 중요한 질문을 제기합니다: 조정 가능한 RZ 게이트 d개와 G-d 클리포드 게이트를 가진 대형 큐비트 회로의 선형 속성을 고전적 입력을 변화시켜 생성된 측정 데이터로부터 효율적으로 학습할 수 있는가? 본 연구에서 우리는 작은 예측 오류를 달성하기 위해 d에 선형적으로 비례하는 샘플 복잡성 스케일링이 필요하다는 것을 증명하며, 이에 상응하는 계산 복잡성은 d에 대해 지수적으로 스케일링될 수 있습니다. 이 문제를 해결하기 위해, 우리는 고전적 섀도우와 절단된 삼각 함수 확장을 활용한 커널 기반 방법을 제안하여 예측 정확도와 계산 오버헤드 간의 통제 가능한 균형을 가능하게 합니다. 우리의 결과는 양자 계산의 두 가지 중요한 영역을 발전시킵니다: 실용적 유틸리티를 가진 양자 알고리즘 탐색과 학습 기반 양자 시스템 인증. 우리는 양자 정보 처리 프로토콜, 해밀토니안 시뮬레이션, 최대 60 큐비트의 변분 양자 알고리즘을 포함한 다양한 시나리오에서 우리의 제안을 검증하기 위한 수치 시뮬레이션을 수행합니다.

## 📝 요약

이 논문은 대규모 큐비트 회로의 선형 속성을 효율적으로 학습할 수 있는지에 대한 연구를 다룹니다. 연구 결과, 조정 가능한 RZ 게이트와 Clifford 게이트를 포함한 회로의 경우, 작은 예측 오류를 달성하기 위해 샘플 복잡도는 $d$에 선형적으로 증가하지만, 계산 복잡도는 $d$에 대해 지수적으로 증가할 수 있음을 증명했습니다. 이를 해결하기 위해 고전적 섀도우와 절단된 삼각 함수 확장을 활용한 커널 기반 방법을 제안하여 예측 정확도와 계산 부담 간의 균형을 조절할 수 있게 했습니다. 이 방법은 양자 알고리즘의 실용적 활용과 학습 기반 양자 시스템 인증에 기여하며, 최대 60 큐비트까지의 다양한 시나리오에서 제안된 방법의 유효성을 수치 시뮬레이션을 통해 검증했습니다.

## 🎯 주요 포인트

- 1. 대규모 큐비트 상태 공간의 복잡성으로 인해 고전적 시뮬레이션이나 양자 단층 촬영을 통해 현대 양자 컴퓨터의 동역학을 포괄적으로 파악하기 어렵습니다.
- 2. 본 연구에서는 d개의 조정 가능한 RZ 게이트와 G-d개의 Clifford 게이트를 가진 대규모 큐비트 회로의 선형 특성을 측정 데이터로부터 효율적으로 학습할 수 있는지를 탐구합니다.
- 3. 예측 오류를 줄이기 위해 샘플 복잡성은 d에 선형적으로 비례해야 하며, 계산 복잡성은 d에 대해 지수적으로 증가할 수 있습니다.
- 4. 우리는 고전적 그림자와 절단된 삼각 함수 확장을 활용한 커널 기반 방법을 제안하여 예측 정확도와 계산 오버헤드 간의 균형을 조절할 수 있게 합니다.
- 5. 제안된 방법은 양자 정보 처리 프로토콜, 해밀토니안 시뮬레이션, 변분 양자 알고리즘 등 다양한 시나리오에서 검증되었습니다.


---

*Generated on 2025-09-23 11:15:32*