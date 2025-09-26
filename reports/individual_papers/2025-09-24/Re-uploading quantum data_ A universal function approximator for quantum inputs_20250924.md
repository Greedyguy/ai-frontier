<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:10:42.355257",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Quantum Data Re-uploading",
    "Universal Function Approximation",
    "Quantum Machine Learning",
    "CPTP Maps"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Quantum Data Re-uploading": 0.92,
    "Universal Function Approximation": 0.68,
    "Quantum Machine Learning": 0.8,
    "CPTP Maps": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "quantum data re-uploading",
        "canonical": "Quantum Data Re-uploading",
        "aliases": [
          "quantum re-uploading"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and represents a novel approach in quantum machine learning, enhancing connectivity with related quantum computing topics.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.92
      },
      {
        "surface": "universal function approximation",
        "canonical": "Universal Function Approximation",
        "aliases": [
          "function approximation"
        ],
        "category": "broad_technical",
        "rationale": "This term is widely applicable in both classical and quantum contexts, facilitating connections to various function approximation studies.",
        "novelty_score": 0.45,
        "connectivity_score": 0.78,
        "specificity_score": 0.52,
        "link_intent_score": 0.68
      },
      {
        "surface": "quantum machine learning models",
        "canonical": "Quantum Machine Learning",
        "aliases": [
          "quantum ML"
        ],
        "category": "specific_connectable",
        "rationale": "Quantum machine learning is a growing field, and linking to it can enhance understanding of quantum data processing techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "completely positive and trace-preserving maps",
        "canonical": "CPTP Maps",
        "aliases": [
          "completely positive maps",
          "trace-preserving maps"
        ],
        "category": "unique_technical",
        "rationale": "This is a fundamental concept in quantum mechanics and quantum information theory, crucial for understanding quantum operations.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
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
      "candidate_surface": "quantum data re-uploading",
      "resolved_canonical": "Quantum Data Re-uploading",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.92
      }
    },
    {
      "candidate_surface": "universal function approximation",
      "resolved_canonical": "Universal Function Approximation",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.78,
        "specificity": 0.52,
        "link_intent": 0.68
      }
    },
    {
      "candidate_surface": "quantum machine learning models",
      "resolved_canonical": "Quantum Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "completely positive and trace-preserving maps",
      "resolved_canonical": "CPTP Maps",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Re-uploading quantum data: A universal function approximator for quantum inputs

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18530.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18530](https://arxiv.org/abs/2509.18530)

## 🔗 유사한 논문
- [[2025-09-22/Quantum Reinforcement Learning with Dynamic-Circuit Qubit Reuse and Grover-Based Trajectory Optimization_20250922|Quantum Reinforcement Learning with Dynamic-Circuit Qubit Reuse and Grover-Based Trajectory Optimization]] (85.4% similar)
- [[2025-09-22/Efficient Learning for Linear Properties of Bounded-Gate Quantum Circuits_20250922|Efficient Learning for Linear Properties of Bounded-Gate Quantum Circuits]] (85.0% similar)
- [[2025-09-17/Learning quantum many-body data locally_ A provably scalable framework_20250917|Learning quantum many-body data locally: A provably scalable framework]] (84.3% similar)
- [[2025-09-22/Double descent in quantum kernel methods_20250922|Double descent in quantum kernel methods]] (84.1% similar)
- [[2025-09-17/Quantum Variational Activation Functions Empower Kolmogorov-Arnold Networks_20250917|Quantum Variational Activation Functions Empower Kolmogorov-Arnold Networks]] (83.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Universal Function Approximation|Universal Function Approximation]]
**🔗 Specific Connectable**: [[keywords/Quantum Machine Learning|Quantum Machine Learning]]
**⚡ Unique Technical**: [[keywords/Quantum Data Re-uploading|Quantum Data Re-uploading]], [[keywords/CPTP Maps|CPTP Maps]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18530v1 Announce Type: cross 
Abstract: Quantum data re-uploading has proved powerful for classical inputs, where repeatedly encoding features into a small circuit yields universal function approximation. Extending this idea to quantum inputs remains underexplored, as the information contained in a quantum state is not directly accessible in classical form. We propose and analyze a quantum data re-uploading architecture in which a qubit interacts sequentially with fresh copies of an arbitrary input state. The circuit can approximate any bounded continuous function using only one ancilla qubit and single-qubit measurements. By alternating entangling unitaries with mid-circuit resets of the input register, the architecture realizes a discrete cascade of completely positive and trace-preserving maps, analogous to collision models in open quantum system dynamics. Our framework provides a qubit-efficient and expressive approach to designing quantum machine learning models that operate directly on quantum data.

## 📝 요약

이 논문은 양자 데이터 재업로드 아키텍처를 제안하고 분석합니다. 이 아키텍처는 하나의 큐비트가 새로운 입력 상태와 순차적으로 상호작용하여, 하나의 앤실라 큐비트와 단일 큐비트 측정만으로 모든 유계 연속 함수를 근사할 수 있습니다. 입력 레지스터의 중간 회로 리셋과 얽힘 유니터리 연산을 번갈아 사용하여, 개방 양자 시스템 동역학의 충돌 모델과 유사한 완전 양의 추적 보존 맵의 이산적 연쇄를 구현합니다. 이 프레임워크는 양자 데이터를 직접 처리하는 양자 기계 학습 모델을 설계하는 데 있어 큐비트를 효율적으로 사용하면서도 표현력이 뛰어난 접근 방식을 제공합니다.

## 🎯 주요 포인트

- 1. 양자 데이터 재업로드는 작은 회로에 특징을 반복적으로 인코딩하여 보편적인 함수 근사를 가능하게 합니다.
- 2. 제안된 양자 데이터 재업로드 아키텍처는 큐비트가 임의의 입력 상태의 새로운 복사본과 순차적으로 상호작용하여 작동합니다.
- 3. 이 회로는 하나의 앤실라 큐비트와 단일 큐비트 측정을 사용하여 모든 유계 연속 함수를 근사할 수 있습니다.
- 4. 입력 레지스터의 중간 회로 리셋과 얽힘 유니터리의 교차를 통해 완전 양의 추적 보존 맵의 이산적 연쇄를 실현합니다.
- 5. 제안된 프레임워크는 양자 데이터를 직접 처리하는 양자 기계 학습 모델을 설계하는 큐비트 효율적이고 표현력 있는 접근 방식을 제공합니다.


---

*Generated on 2025-09-24 15:10:42*