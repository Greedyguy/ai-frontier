---
keywords:
  - Variational Quantum Circuits
  - Particle Swarm Optimization
  - Barren Plateaus Problem
  - Quantum Gates
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15726
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:52:46.543028",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Variational Quantum Circuits",
    "Particle Swarm Optimization",
    "Barren Plateaus Problem",
    "Quantum Gates"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Variational Quantum Circuits": 0.8,
    "Particle Swarm Optimization": 0.78,
    "Barren Plateaus Problem": 0.77,
    "Quantum Gates": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Variational Quantum Circuits",
        "canonical": "Variational Quantum Circuits",
        "aliases": [
          "VQC"
        ],
        "category": "unique_technical",
        "rationale": "Variational Quantum Circuits are central to the paper's methodology and offer unique insights into quantum computing.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Particle Swarm Optimization",
        "canonical": "Particle Swarm Optimization",
        "aliases": [
          "PSO"
        ],
        "category": "unique_technical",
        "rationale": "Particle Swarm Optimization is a key algorithm used in the study, providing a novel approach to training quantum circuits.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "barren plateaus problem",
        "canonical": "Barren Plateaus Problem",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "The barren plateaus problem is a significant challenge in quantum optimization, relevant to the study's context.",
        "novelty_score": 0.75,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "quantum gates",
        "canonical": "Quantum Gates",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Quantum gates are fundamental components of quantum circuits, relevant for understanding the study's technical details.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "algorithm"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Variational Quantum Circuits",
      "resolved_canonical": "Variational Quantum Circuits",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Particle Swarm Optimization",
      "resolved_canonical": "Particle Swarm Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "barren plateaus problem",
      "resolved_canonical": "Barren Plateaus Problem",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "quantum gates",
      "resolved_canonical": "Quantum Gates",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Training Variational Quantum Circuits Using Particle Swarm Optimization

**Korean Title:** 입자 군집 최적화를 이용한 변분 양자 회로 학습

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15726.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15726](https://arxiv.org/abs/2509.15726)

## 🔗 유사한 논문
- [[2025-09-19/Trainability of Quantum Models Beyond Known Classical Simulability_20250919|Trainability of Quantum Models Beyond Known Classical Simulability]] (82.6% similar)
- [[2025-09-22/Triplet Loss Based Quantum Encoding for Class Separability_20250922|Triplet Loss Based Quantum Encoding for Class Separability]] (81.6% similar)
- [[2025-09-17/Quantum Reinforcement Learning-Guided Diffusion Model for Image Synthesis via Hybrid Quantum-Classical Generative Model Architectures_20250917|Quantum Reinforcement Learning-Guided Diffusion Model for Image Synthesis via Hybrid Quantum-Classical Generative Model Architectures]] (80.6% similar)
- [[2025-09-18/Learning AC Power Flow Solutions using a Data-Dependent Variational Quantum Circuit_20250918|Learning AC Power Flow Solutions using a Data-Dependent Variational Quantum Circuit]] (80.5% similar)
- [[2025-09-22/Impact of Single Rotations and Entanglement Topologies in Quantum Neural Networks_20250922|Impact of Single Rotations and Entanglement Topologies in Quantum Neural Networks]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Quantum Gates|Quantum Gates]]
**🔗 Specific Connectable**: [[keywords/Barren Plateaus Problem|Barren Plateaus Problem]]
**⚡ Unique Technical**: [[keywords/Variational Quantum Circuits|Variational Quantum Circuits]], [[keywords/Particle Swarm Optimization|Particle Swarm Optimization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15726v1 Announce Type: cross 
Abstract: In this work, the Particle Swarm Optimization (PSO) algorithm has been used to train various Variational Quantum Circuits (VQCs). This approach is motivated by the fact that commonly used gradient-based optimization methods can suffer from the barren plateaus problem. PSO is a stochastic optimization technique inspired by the collective behavior of a swarm of birds. The dimension of the swarm, the number of iterations of the algorithm, and the number of trainable parameters can be set. In this study, PSO has been used to train the entire structure of VQCs, allowing it to select which quantum gates to apply, the target qubits, and the rotation angle, in case a rotation is chosen. The algorithm is restricted to choosing from four types of gates: Rx, Ry, Rz, and CNOT. The proposed optimization approach has been tested on various datasets of the MedMNIST, which is a collection of biomedical image datasets designed for image classification tasks. Performance has been compared with the results achieved by classical stochastic gradient descent applied to a predefined VQC. The results show that the PSO can achieve comparable or even better classification accuracy across multiple datasets, despite the PSO using a lower number of quantum gates than the VQC used with gradient descent optimization.

## 🔍 Abstract (한글 번역)

arXiv:2509.15726v1 발표 유형: 교차  
초록: 본 연구에서는 입자 군집 최적화(PSO) 알고리즘을 사용하여 다양한 변분 양자 회로(VQC)를 학습시켰습니다. 이 접근법은 일반적으로 사용되는 경사 기반 최적화 방법이 황무지 문제를 겪을 수 있다는 사실에 의해 동기 부여되었습니다. PSO는 새 떼의 집단 행동에서 영감을 받은 확률적 최적화 기법입니다. 군집의 차원, 알고리즘의 반복 횟수, 학습 가능한 매개변수의 수를 설정할 수 있습니다. 본 연구에서는 PSO를 사용하여 VQC의 전체 구조를 학습시켰으며, 이를 통해 어떤 양자 게이트를 적용할지, 대상 큐비트, 회전이 선택된 경우 회전 각도를 선택할 수 있습니다. 알고리즘은 Rx, Ry, Rz, CNOT 네 가지 유형의 게이트 중에서 선택하도록 제한됩니다. 제안된 최적화 접근법은 이미지 분류 작업을 위해 설계된 생의학 이미지 데이터셋 모음인 MedMNIST의 다양한 데이터셋에서 테스트되었습니다. 성능은 사전 정의된 VQC에 적용된 고전적 확률적 경사 하강법으로 달성된 결과와 비교되었습니다. 결과는 PSO가 경사 하강 최적화와 함께 사용된 VQC보다 적은 수의 양자 게이트를 사용함에도 불구하고 여러 데이터셋에서 동등하거나 더 나은 분류 정확도를 달성할 수 있음을 보여줍니다.

## 📝 요약

이 연구에서는 입자 군집 최적화(PSO) 알고리즘을 사용하여 다양한 변분 양자 회로(VQC)를 훈련했습니다. 기존의 경사 기반 최적화 방법이 빈 평원 문제를 겪을 수 있다는 점에서 PSO를 선택했습니다. PSO는 새 떼의 집단 행동에서 영감을 받은 확률적 최적화 기법으로, 군집의 차원, 알고리즘 반복 횟수, 훈련 가능한 매개변수 수를 설정할 수 있습니다. 이 연구에서는 PSO를 통해 VQC의 전체 구조를 훈련하며, 적용할 양자 게이트, 대상 큐비트, 회전 각도를 선택할 수 있습니다. 알고리즘은 Rx, Ry, Rz, CNOT 네 가지 게이트 중에서 선택하도록 제한됩니다. 제안된 최적화 방법은 MedMNIST의 다양한 생의학 이미지 데이터셋에서 테스트되었으며, 기존의 확률적 경사 하강법과 비교하여 유사하거나 더 나은 분류 정확도를 달성했습니다. 이는 PSO가 더 적은 수의 양자 게이트를 사용했음에도 불구하고 얻어진 결과입니다.

## 🎯 주요 포인트

- 1. 입자 군집 최적화(PSO) 알고리즘을 사용하여 다양한 변분 양자 회로(VQC)를 훈련하였다.
- 2. PSO는 일반적인 경사 기반 최적화 방법이 겪는 barren plateaus 문제를 해결하기 위한 대안으로 제안되었다.
- 3. PSO는 네 가지 유형의 양자 게이트(Rx, Ry, Rz, CNOT) 중에서 선택하여 VQC의 전체 구조를 훈련할 수 있다.
- 4. MedMNIST의 다양한 생물 의학 이미지 데이터셋에서 PSO의 성능을 테스트하였으며, 기존의 경사 하강법과 비교하여 유사하거나 더 나은 분류 정확도를 달성하였다.
- 5. PSO는 경사 하강법보다 적은 수의 양자 게이트를 사용하면서도 높은 성능을 보였다.


---

*Generated on 2025-09-23 10:52:46*