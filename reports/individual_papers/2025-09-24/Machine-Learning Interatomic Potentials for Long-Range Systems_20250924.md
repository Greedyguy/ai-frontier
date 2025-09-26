<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:31:41.405477",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Learning Interatomic Potentials",
    "Sum-of-Gaussians Neural Network",
    "Fourier Convolution Layer",
    "Latent-Variable Learning Network"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Learning Interatomic Potentials": 0.8,
    "Sum-of-Gaussians Neural Network": 0.85,
    "Fourier Convolution Layer": 0.8,
    "Latent-Variable Learning Network": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Machine-learning interatomic potentials",
        "canonical": "Machine Learning Interatomic Potentials",
        "aliases": [
          "ML Interatomic Potentials"
        ],
        "category": "unique_technical",
        "rationale": "This term represents a specialized application of machine learning in molecular simulations, highlighting its novelty and specificity.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Sum-of-Gaussians Neural Network",
        "canonical": "Sum-of-Gaussians Neural Network",
        "aliases": [
          "SOG-Net"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific neural network architecture proposed in the paper, offering a unique approach to integrating long-range interactions.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Fourier convolution layer",
        "canonical": "Fourier Convolution Layer",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This component is crucial for incorporating long-range effects, linking it to broader convolutional techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "latent-variable learning network",
        "canonical": "Latent-Variable Learning Network",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This network type is key for bridging short-range and long-range interactions, relevant for linking to latent variable models.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "long-range systems",
      "computational cost"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Machine-learning interatomic potentials",
      "resolved_canonical": "Machine Learning Interatomic Potentials",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Sum-of-Gaussians Neural Network",
      "resolved_canonical": "Sum-of-Gaussians Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Fourier convolution layer",
      "resolved_canonical": "Fourier Convolution Layer",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "latent-variable learning network",
      "resolved_canonical": "Latent-Variable Learning Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Machine-Learning Interatomic Potentials for Long-Range Systems

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2502.04668.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2502.04668](https://arxiv.org/abs/2502.04668)

## 🔗 유사한 논문
- [[2025-09-17/Learning Minimal Representations of Many-Body Physics from Snapshots of a Quantum Simulator_20250917|Learning Minimal Representations of Many-Body Physics from Snapshots of a Quantum Simulator]] (82.6% similar)
- [[2025-09-23/Active Learning for Machine Learning Driven Molecular Dynamics_20250923|Active Learning for Machine Learning Driven Molecular Dynamics]] (82.2% similar)
- [[2025-09-23/Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs_20250923|Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs]] (81.2% similar)
- [[2025-09-18/Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (81.0% similar)
- [[2025-09-22/Merging Memory and Space_ A State Space Neural Operator_20250922|Merging Memory and Space: A State Space Neural Operator]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Fourier Convolution Layer|Fourier Convolution Layer]], [[keywords/Latent-Variable Learning Network|Latent-Variable Learning Network]]
**⚡ Unique Technical**: [[keywords/Machine Learning Interatomic Potentials|Machine Learning Interatomic Potentials]], [[keywords/Sum-of-Gaussians Neural Network|Sum-of-Gaussians Neural Network]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.04668v2 Announce Type: replace-cross 
Abstract: Machine-learning interatomic potentials have emerged as a revolutionary class of force-field models in molecular simulations, delivering quantum-mechanical accuracy at a fraction of the computational cost and enabling the simulation of large-scale systems over extended timescales. However, they often focus on modeling local environments, neglecting crucial long-range interactions. We propose a Sum-of-Gaussians Neural Network (SOG-Net), a lightweight and versatile framework for integrating long-range interactions into machine learning force field. The SOG-Net employs a latent-variable learning network that seamlessly bridges short-range and long-range components, coupled with an efficient Fourier convolution layer that incorporates long-range effects. By learning sum-of-Gaussians multipliers across different convolution layers, the SOG-Net adaptively captures diverse long-range decay behaviors while maintaining close-to-linear computational complexity during training and simulation via non-uniform fast Fourier transforms. The method is demonstrated effective for a broad range of long-range systems.

## 📝 요약

이 논문은 기계 학습 기반 원자간 포텐셜 모델이 주로 국소 환경을 모델링하는 데 집중하여 장거리 상호작용을 간과하는 문제를 해결하고자 합니다. 이를 위해 Sum-of-Gaussians Neural Network (SOG-Net)를 제안합니다. SOG-Net은 짧은 거리와 긴 거리 상호작용을 통합하는 잠재 변수 학습 네트워크와 효율적인 푸리에 컨볼루션 레이어를 사용하여 장거리 효과를 포함합니다. 다양한 컨볼루션 레이어에서 가우시안의 합을 학습함으로써, SOG-Net은 다양한 장거리 감쇠 행동을 적응적으로 포착하며, 비균일한 빠른 푸리에 변환을 통해 훈련 및 시뮬레이션 시 거의 선형의 계산 복잡성을 유지합니다. 이 방법은 다양한 장거리 시스템에 효과적임을 입증하였습니다.

## 🎯 주요 포인트

- 1. 기계 학습 기반의 상호작용 잠재력 모델은 분자 시뮬레이션에서 양자역학적 정확성을 제공하면서도 계산 비용을 줄여 대규모 시스템의 시뮬레이션을 가능하게 한다.
- 2. 기존 모델은 주로 국소 환경을 모델링하며 중요한 장거리 상호작용을 간과하는 경향이 있다.
- 3. SOG-Net은 장거리 상호작용을 기계 학습 포스 필드에 통합하기 위한 경량의 다재다능한 프레임워크로 제안되었다.
- 4. SOG-Net은 단거리와 장거리 성분을 연결하는 잠재 변수 학습 네트워크와 장거리 효과를 포함하는 효율적인 푸리에 컨볼루션 레이어를 사용한다.
- 5. SOG-Net은 다양한 장거리 감쇠 행동을 적응적으로 포착하면서도 비균일 고속 푸리에 변환을 통해 훈련 및 시뮬레이션 시 거의 선형의 계산 복잡성을 유지한다.


---

*Generated on 2025-09-24 15:31:41*