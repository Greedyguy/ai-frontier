<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:31:27.029660",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Variational Decision Diagrams",
    "Quantum Machine Learning",
    "Barren Plateaus",
    "Transverse-Field Ising Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Variational Decision Diagrams": 0.78,
    "Quantum Machine Learning": 0.82,
    "Barren Plateaus": 0.75,
    "Transverse-Field Ising Model": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Variational Decision Diagrams",
        "canonical": "Variational Decision Diagrams",
        "aliases": [
          "VDDs"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel graph structure that combines decision diagrams with variational methods, relevant for quantum machine learning.",
        "novelty_score": 0.85,
        "connectivity_score": 0.68,
        "specificity_score": 0.92,
        "link_intent_score": 0.78
      },
      {
        "surface": "Quantum Machine Learning",
        "canonical": "Quantum Machine Learning",
        "aliases": [
          "QML"
        ],
        "category": "broad_technical",
        "rationale": "A key application area for the proposed variational decision diagrams, linking quantum computing with machine learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.89,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Barren Plateaus",
        "canonical": "Barren Plateaus",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A critical concept in quantum machine learning related to the trainability of variational algorithms.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.88,
        "link_intent_score": 0.75
      },
      {
        "surface": "Transverse-Field Ising Model",
        "canonical": "Transverse-Field Ising Model",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Used as a test case for the variational decision diagrams, relevant for quantum state estimation.",
        "novelty_score": 0.6,
        "connectivity_score": 0.72,
        "specificity_score": 0.9,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "Decision Diagrams",
      "Quantum Circuits",
      "Probability Amplitudes"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Variational Decision Diagrams",
      "resolved_canonical": "Variational Decision Diagrams",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.68,
        "specificity": 0.92,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Quantum Machine Learning",
      "resolved_canonical": "Quantum Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.89,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Barren Plateaus",
      "resolved_canonical": "Barren Plateaus",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.88,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Transverse-Field Ising Model",
      "resolved_canonical": "Transverse-Field Ising Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.72,
        "specificity": 0.9,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Variational decision diagrams for quantum-inspired machine learning applications

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2502.04271.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2502.04271](https://arxiv.org/abs/2502.04271)

## 🔗 유사한 논문
- [[2025-09-19/Trainability of Quantum Models Beyond Known Classical Simulability_20250919|Trainability of Quantum Models Beyond Known Classical Simulability]] (84.8% similar)
- [[2025-09-17/Quantum Variational Activation Functions Empower Kolmogorov-Arnold Networks_20250917|Quantum Variational Activation Functions Empower Kolmogorov-Arnold Networks]] (82.0% similar)
- [[2025-09-22/Training Variational Quantum Circuits Using Particle Swarm Optimization_20250922|Training Variational Quantum Circuits Using Particle Swarm Optimization]] (81.6% similar)
- [[2025-09-22/Double descent in quantum kernel methods_20250922|Double descent in quantum kernel methods]] (81.4% similar)
- [[2025-09-23/DiffQ_ Unified Parameter Initialization for Variational Quantum Algorithms via Diffusion Models_20250923|DiffQ: Unified Parameter Initialization for Variational Quantum Algorithms via Diffusion Models]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Quantum Machine Learning|Quantum Machine Learning]]
**🔗 Specific Connectable**: [[keywords/Barren Plateaus|Barren Plateaus]], [[keywords/Transverse-Field Ising Model|Transverse-Field Ising Model]]
**⚡ Unique Technical**: [[keywords/Variational Decision Diagrams|Variational Decision Diagrams]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.04271v2 Announce Type: replace-cross 
Abstract: Decision diagrams (DDs) have emerged as an efficient tool for simulating quantum circuits due to their capacity to exploit data redundancies in quantum states and quantum operations, enabling the efficient computation of probability amplitudes. However, their application in quantum machine learning (QML) has remained unexplored. This paper introduces variational decision diagrams (VDDs), a novel graph structure that combines the structural benefits of DDs with the adaptability of variational methods for efficiently representing quantum states. We investigate the trainability of VDDs by applying them to the ground state estimation problem for transverse-field Ising and Heisenberg Hamiltonians. Analysis of gradient variance suggests that training VDDs is possible, as no signs of vanishing gradients--also known as barren plateaus--are observed. This work provides new insights into the use of decision diagrams in QML as an alternative to design and train variational ans\"atze.

## 📝 요약

이 논문은 양자 회로 시뮬레이션에 효율적인 도구로 사용되는 결정 다이어그램(DDs)을 양자 기계 학습(QML)에 적용한 연구입니다. 저자들은 변분 결정 다이어그램(VDDs)이라는 새로운 그래프 구조를 제안하여, DDs의 구조적 이점과 변분 방법의 적응성을 결합하여 양자 상태를 효율적으로 표현할 수 있도록 했습니다. VDDs를 횡자기장 이징 및 하이젠베르크 해밀토니안의 기저 상태 추정 문제에 적용하여 훈련 가능성을 조사한 결과, 기울기 소멸 문제 없이 훈련이 가능함을 확인했습니다. 이 연구는 QML에서 결정 다이어그램을 활용한 새로운 변분 앙상블 설계 및 훈련 방법을 제시합니다.

## 🎯 주요 포인트

- 1. 결정 다이어그램(DD)은 양자 회로 시뮬레이션에서 데이터 중복성을 활용하여 효율적인 확률 진폭 계산을 가능하게 한다.
- 2. 본 논문은 DD의 구조적 이점과 변분 방법의 적응성을 결합한 새로운 그래프 구조인 변분 결정 다이어그램(VDD)을 소개한다.
- 3. VDD의 훈련 가능성을 조사한 결과, 기울기 소멸 현상이 관찰되지 않아 훈련이 가능함을 시사한다.
- 4. VDD는 횡자기 이징 및 하이젠베르크 해밀토니안의 바닥 상태 추정 문제에 적용되었다.
- 5. 본 연구는 QML에서 결정 다이어그램을 변분 앙상블 설계 및 훈련의 대안으로 사용할 수 있는 새로운 통찰력을 제공한다.


---

*Generated on 2025-09-24 15:31:27*