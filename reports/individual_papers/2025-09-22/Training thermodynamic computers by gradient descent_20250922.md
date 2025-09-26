---
keywords:
  - Thermodynamic Computer
  - Gradient Descent
  - Neural Network
  - Finite-Time Dynamics
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15324
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:47:35.822950",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Thermodynamic Computer",
    "Gradient Descent",
    "Neural Network",
    "Finite-Time Dynamics"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Thermodynamic Computer": 0.78,
    "Gradient Descent": 0.85,
    "Neural Network": 0.88,
    "Finite-Time Dynamics": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "thermodynamic computer",
        "canonical": "Thermodynamic Computer",
        "aliases": [
          "thermodynamic computing device"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel concept in computing that links thermodynamics with computation.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "gradient descent",
        "canonical": "Gradient Descent",
        "aliases": [
          "gradient optimization"
        ],
        "category": "broad_technical",
        "rationale": "A fundamental optimization technique widely used in machine learning.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "neural network",
        "canonical": "Neural Network",
        "aliases": [
          "NN"
        ],
        "category": "broad_technical",
        "rationale": "Core component of the described computation, linking to machine learning.",
        "novelty_score": 0.2,
        "connectivity_score": 0.95,
        "specificity_score": 0.7,
        "link_intent_score": 0.88
      },
      {
        "surface": "finite-time dynamics",
        "canonical": "Finite-Time Dynamics",
        "aliases": [
          "finite time behavior"
        ],
        "category": "unique_technical",
        "rationale": "Describes a specific behavior of the thermodynamic computer relevant to computation.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "method",
      "computation",
      "probability",
      "parameters"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "thermodynamic computer",
      "resolved_canonical": "Thermodynamic Computer",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "gradient descent",
      "resolved_canonical": "Gradient Descent",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "neural network",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.2,
        "connectivity": 0.95,
        "specificity": 0.7,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "finite-time dynamics",
      "resolved_canonical": "Finite-Time Dynamics",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Training thermodynamic computers by gradient descent

**Korean Title:** 열역학 컴퓨터의 경사 하강법을 통한 훈련

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15324.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15324](https://arxiv.org/abs/2509.15324)

## 🔗 유사한 논문
- [[2025-09-18/Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers_20250918|Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers]] (83.4% similar)
- [[2025-09-22/Analog In-memory Training on General Non-ideal Resistive Elements_ The Impact of Response Functions_20250922|Analog In-memory Training on General Non-ideal Resistive Elements: The Impact of Response Functions]] (81.9% similar)
- [[2025-09-19/Trainability of Quantum Models Beyond Known Classical Simulability_20250919|Trainability of Quantum Models Beyond Known Classical Simulability]] (80.7% similar)
- [[2025-09-22/Double descent in quantum kernel methods_20250922|Double descent in quantum kernel methods]] (80.4% similar)
- [[2025-09-18/Data coarse graining can improve model performance_20250918|Data coarse graining can improve model performance]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Gradient Descent|Gradient Descent]], [[keywords/Neural Network|Neural Network]]
**⚡ Unique Technical**: [[keywords/Thermodynamic Computer|Thermodynamic Computer]], [[keywords/Finite-Time Dynamics|Finite-Time Dynamics]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15324v1 Announce Type: cross 
Abstract: We show how to adjust the parameters of a thermodynamic computer by gradient descent in order to perform a desired computation at a specified observation time. Within a digital simulation of a thermodynamic computer, training proceeds by maximizing the probability with which the computer would generate an idealized dynamical trajectory. The idealized trajectory is designed to reproduce the activations of a neural network trained to perform the desired computation. This teacher-student scheme results in a thermodynamic computer whose finite-time dynamics enacts a computation analogous to that of the neural network. The parameters identified in this way can be implemented in the hardware realization of the thermodynamic computer, which will perform the desired computation automatically, driven by thermal noise. We demonstrate the method on a standard image-classification task, and estimate the thermodynamic advantage -- the ratio of energy costs of the digital and thermodynamic implementations -- to exceed seven orders of magnitude. Our results establish gradient descent as a viable training method for thermodynamic computing, enabling application of the core methodology of machine learning to this emerging field.

## 🔍 Abstract (한글 번역)

arXiv:2509.15324v1 발표 유형: 교차  
초록: 우리는 지정된 관찰 시간에 원하는 계산을 수행하기 위해 열역학적 컴퓨터의 매개변수를 경사 하강법으로 조정하는 방법을 보여줍니다. 열역학적 컴퓨터의 디지털 시뮬레이션 내에서 훈련은 컴퓨터가 이상화된 동적 궤적을 생성할 확률을 최대화함으로써 진행됩니다. 이상화된 궤적은 원하는 계산을 수행하도록 훈련된 신경망의 활성화를 재현하도록 설계되었습니다. 이 교사-학생 방식은 유한 시간 동역학이 신경망의 계산과 유사한 계산을 수행하는 열역학적 컴퓨터를 결과로 가져옵니다. 이와 같이 식별된 매개변수는 열역학적 컴퓨터의 하드웨어 구현에 적용될 수 있으며, 이는 열 잡음에 의해 자동으로 원하는 계산을 수행할 것입니다. 우리는 표준 이미지 분류 작업에 이 방법을 시연하고, 디지털 및 열역학적 구현의 에너지 비용 비율인 열역학적 이점을 7차 이상의 크기로 초과한다고 추정합니다. 우리의 결과는 열역학적 컴퓨팅을 위한 유효한 훈련 방법으로서 경사 하강법을 확립하며, 이 신흥 분야에 기계 학습의 핵심 방법론을 적용할 수 있게 합니다.

## 📝 요약

이 논문은 열역학적 컴퓨터의 매개변수를 경사 하강법을 통해 조정하여 원하는 계산을 수행하는 방법을 제안합니다. 디지털 시뮬레이션 내에서, 이상적인 동적 궤적을 생성할 확률을 최대화하여 컴퓨터를 훈련합니다. 이 궤적은 신경망의 활성화를 재현하도록 설계되었습니다. 이 방법은 열역학적 컴퓨터가 신경망과 유사한 계산을 수행하도록 합니다. 하드웨어 구현 시, 열 잡음에 의해 자동으로 원하는 계산을 수행합니다. 이미지 분류 작업에 이 방법을 적용한 결과, 디지털 구현 대비 에너지 비용이 7자릿수 이상 절감되는 열역학적 이점을 확인했습니다. 이 연구는 열역학적 컴퓨팅에서 경사 하강법이 유효한 훈련 방법임을 입증하며, 기계 학습의 핵심 방법론을 이 분야에 적용할 수 있는 가능성을 열었습니다.

## 🎯 주요 포인트

- 1. 열역학적 컴퓨터의 매개변수를 경사 하강법으로 조정하여 원하는 계산을 수행할 수 있도록 하는 방법을 제시합니다.
- 2. 디지털 시뮬레이션 내에서 이상적인 동적 궤적을 생성할 확률을 최대화하여 훈련을 진행합니다.
- 3. 신경망의 활성화를 재현하도록 설계된 이상적인 궤적을 통해 열역학적 컴퓨터가 유한 시간 내에 신경망과 유사한 계산을 수행하게 합니다.
- 4. 열역학적 구현의 에너지 비용이 디지털 구현보다 7자릿수 이상 우월하다는 열역학적 이점을 추정합니다.
- 5. 경사 하강법이 열역학적 컴퓨팅을 위한 유효한 훈련 방법임을 입증하여 기계 학습의 핵심 방법론을 이 새로운 분야에 적용할 수 있게 합니다.


---

*Generated on 2025-09-23 10:47:35*