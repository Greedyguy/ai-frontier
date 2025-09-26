<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:23:12.772665",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Nonlinear Schrödinger Equation",
    "Neural Network",
    "ConvNeXt Architecture",
    "Multivariate Gaussian Negative Log-Likelihood"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Nonlinear Schrödinger Equation": 0.78,
    "Neural Network": 0.85,
    "ConvNeXt Architecture": 0.72,
    "Multivariate Gaussian Negative Log-Likelihood": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "nonlinear Schrödinger equation",
        "canonical": "Nonlinear Schrödinger Equation",
        "aliases": [
          "NLSE"
        ],
        "category": "unique_technical",
        "rationale": "Central to the study, it connects theoretical modeling with experimental data in nonlinear systems.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "neural network",
        "canonical": "Neural Network",
        "aliases": [
          "NN"
        ],
        "category": "broad_technical",
        "rationale": "A core component of the machine learning approach used for parameter estimation.",
        "novelty_score": 0.45,
        "connectivity_score": 0.92,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "ConvNeXt architecture",
        "canonical": "ConvNeXt Architecture",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Specific architecture used in the study, relevant for linking to deep learning advancements.",
        "novelty_score": 0.7,
        "connectivity_score": 0.55,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      },
      {
        "surface": "multivariate Gaussian negative log-likelihood",
        "canonical": "Multivariate Gaussian Negative Log-Likelihood",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Key loss function used in the model, important for understanding the estimation process.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "parameter estimation",
      "wave dynamics",
      "optical fibers"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "nonlinear Schrödinger equation",
      "resolved_canonical": "Nonlinear Schrödinger Equation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "neural network",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.92,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "ConvNeXt architecture",
      "resolved_canonical": "ConvNeXt Architecture",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.55,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "multivariate Gaussian negative log-likelihood",
      "resolved_canonical": "Multivariate Gaussian Negative Log-Likelihood",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Machine learning approach to single-shot multiparameter estimation for the non-linear Schr\"odinger equation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18479.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18479](https://arxiv.org/abs/2509.18479)

## 🔗 유사한 논문
- [[2025-09-17/Learning Minimal Representations of Many-Body Physics from Snapshots of a Quantum Simulator_20250917|Learning Minimal Representations of Many-Body Physics from Snapshots of a Quantum Simulator]] (80.7% similar)
- [[2025-09-22/Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows_20250922|Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows]] (79.7% similar)
- [[2025-09-24/A Kernel Space-based Multidimensional Sparse Model for Dynamic PET Image Denoising_20250924|A Kernel Space-based Multidimensional Sparse Model for Dynamic PET Image Denoising]] (79.6% similar)
- [[2025-09-24/Propagation of Chaos in One-hidden-layer Neural Networks beyond Logarithmic Time_20250924|Propagation of Chaos in One-hidden-layer Neural Networks beyond Logarithmic Time]] (79.6% similar)
- [[2025-09-18/Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (79.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**⚡ Unique Technical**: [[keywords/Nonlinear Schrödinger Equation|Nonlinear Schrödinger Equation]], [[keywords/ConvNeXt Architecture|ConvNeXt Architecture]], [[keywords/Multivariate Gaussian Negative Log-Likelihood|Multivariate Gaussian Negative Log-Likelihood]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18479v1 Announce Type: cross 
Abstract: The nonlinear Schr\"odinger equation (NLSE) is a fundamental model for wave dynamics in nonlinear media ranging from optical fibers to Bose-Einstein condensates. Accurately estimating its parameters, which are often strongly correlated, from a single measurement remains a significant challenge. We address this problem by treating parameter estimation as an inverse problem and training a neural network to invert the NLSE mapping. We combine a fast numerical solver with a machine learning approach based on the ConvNeXt architecture and a multivariate Gaussian negative log-likelihood loss function. From single-shot field (density and phase) images, our model estimates three key parameters: the nonlinear coefficient $n_2$, the saturation intensity $I_{sat}$, and the linear absorption coefficient $\alpha$. Trained on 100,000 simulated images, the model achieves a mean absolute error of $3.22\%$ on 12,500 unseen test samples, demonstrating strong generalization and close agreement with ground-truth values. This approach provides an efficient route for characterizing nonlinear systems and has the potential to bridge theoretical modeling and experimental data when realistic noise is incorporated.

## 📝 요약

이 논문은 비선형 매체의 파동 역학을 설명하는 비선형 슈뢰딩거 방정식(NLSE)의 매개변수 추정을 다룹니다. 단일 측정으로 강하게 상관된 매개변수를 정확히 추정하는 것은 어려운 문제입니다. 이를 해결하기 위해 매개변수 추정을 역문제로 간주하고, NLSE 매핑을 역변환하는 신경망을 훈련시켰습니다. ConvNeXt 아키텍처와 다변량 가우시안 음의 로그 가능도 손실 함수를 기반으로 한 기계 학습 접근법을 빠른 수치 해법과 결합했습니다. 단일 샷 필드 이미지로부터 비선형 계수, 포화 강도, 선형 흡수 계수를 추정하며, 10만 개의 시뮬레이션 이미지로 훈련된 모델은 12,500개의 테스트 샘플에서 평균 절대 오차 3.22%를 달성했습니다. 이 방법은 비선형 시스템 특성화를 위한 효율적인 경로를 제공하며, 현실적인 노이즈가 포함될 때 이론적 모델링과 실험 데이터를 연결할 잠재력을 가집니다.

## 🎯 주요 포인트

- 1. 비선형 슈뢰딩거 방정식(NLSE)은 광섬유에서 보스-아인슈타인 응축체에 이르는 비선형 매체의 파동 역학을 설명하는 기본 모델이다.
- 2. NLSE의 매개변수를 단일 측정으로 정확하게 추정하는 것은 여전히 중요한 과제이다.
- 3. 본 연구는 매개변수 추정을 역문제로 접근하여, NLSE 매핑을 반전시키기 위해 신경망을 훈련시켰다.
- 4. ConvNeXt 아키텍처와 다변량 가우시안 음의 로그 가능도 손실 함수를 기반으로 한 기계 학습 접근법을 사용하여, 단일 샷 필드 이미지로부터 세 가지 주요 매개변수를 추정한다.
- 5. 100,000개의 시뮬레이션 이미지로 훈련된 모델은 12,500개의 테스트 샘플에서 평균 절대 오차 3.22%를 달성하여 강력한 일반화 능력을 보여준다.


---

*Generated on 2025-09-24 16:23:12*