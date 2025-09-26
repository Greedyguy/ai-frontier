<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:04:12.706727",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Dynamic PET Image Denoising",
    "Deep Learning",
    "Kernel Space-based Multidimensional Sparse Model",
    "Neural Network"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Dynamic PET Image Denoising": 0.8,
    "Deep Learning": 0.7,
    "Kernel Space-based Multidimensional Sparse Model": 0.85,
    "Neural Network": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "dynamic PET image denoising",
        "canonical": "Dynamic PET Image Denoising",
        "aliases": [
          "PET Denoising",
          "Dynamic PET Denoising"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application of denoising in medical imaging, which is central to the paper's contribution.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "deep learning",
        "canonical": "Deep Learning",
        "aliases": [
          "DL"
        ],
        "category": "broad_technical",
        "rationale": "Deep Learning is a foundational technique used in the proposed model, linking to a broad technical category.",
        "novelty_score": 0.2,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.7
      },
      {
        "surface": "kernel space-based multidimensional sparse model",
        "canonical": "Kernel Space-based Multidimensional Sparse Model",
        "aliases": [
          "KMDS Model"
        ],
        "category": "unique_technical",
        "rationale": "This is the novel model introduced in the paper, crucial for understanding the technical innovation.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "neural network",
        "canonical": "Neural Network",
        "aliases": [
          "NN"
        ],
        "category": "broad_technical",
        "rationale": "Neural Networks are a core component of the proposed model, linking to a broad technical category.",
        "novelty_score": 0.3,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
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
      "candidate_surface": "dynamic PET image denoising",
      "resolved_canonical": "Dynamic PET Image Denoising",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "deep learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.2,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "kernel space-based multidimensional sparse model",
      "resolved_canonical": "Kernel Space-based Multidimensional Sparse Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "neural network",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# A Kernel Space-based Multidimensional Sparse Model for Dynamic PET Image Denoising

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18801.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18801](https://arxiv.org/abs/2509.18801)

## 🔗 유사한 논문
- [[2025-09-23/PPORLD-EDNetLDCT_ A Proximal Policy Optimization-Based Reinforcement Learning Framework for Adaptive Low-Dose CT Denoising_20250923|PPORLD-EDNetLDCT: A Proximal Policy Optimization-Based Reinforcement Learning Framework for Adaptive Low-Dose CT Denoising]] (84.4% similar)
- [[2025-09-23/DT-NeRF_ A Diffusion and Transformer-Based Optimization Approach for Neural Radiance Fields in 3D Reconstruction_20250923|DT-NeRF: A Diffusion and Transformer-Based Optimization Approach for Neural Radiance Fields in 3D Reconstruction]] (83.1% similar)
- [[2025-09-23/An Efficient Dual-Line Decoder Network with Multi-Scale Convolutional Attention for Multi-organ Segmentation_20250923|An Efficient Dual-Line Decoder Network with Multi-Scale Convolutional Attention for Multi-organ Segmentation]] (82.6% similar)
- [[2025-09-22/Blind-Spot Guided Diffusion for Self-supervised Real-World Denoising_20250922|Blind-Spot Guided Diffusion for Self-supervised Real-World Denoising]] (82.4% similar)
- [[2025-09-23/Interpretability-Aware Pruning for Efficient Medical Image Analysis_20250923|Interpretability-Aware Pruning for Efficient Medical Image Analysis]] (82.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]], [[keywords/Neural Network|Neural Network]]
**⚡ Unique Technical**: [[keywords/Dynamic PET Image Denoising|Dynamic PET Image Denoising]], [[keywords/Kernel Space-based Multidimensional Sparse Model|Kernel Space-based Multidimensional Sparse Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18801v1 Announce Type: cross 
Abstract: Achieving high image quality for temporal frames in dynamic positron emission tomography (PET) is challenging due to the limited statistic especially for the short frames. Recent studies have shown that deep learning (DL) is useful in a wide range of medical image denoising tasks. In this paper, we propose a model-based neural network for dynamic PET image denoising. The inter-frame spatial correlation and intra-frame structural consistency in dynamic PET are used to establish the kernel space-based multidimensional sparse (KMDS) model. We then substitute the inherent forms of the parameter estimation with neural networks to enable adaptive parameters optimization, forming the end-to-end neural KMDS-Net. Extensive experimental results from simulated and real data demonstrate that the neural KMDS-Net exhibits strong denoising performance for dynamic PET, outperforming previous baseline methods. The proposed method may be used to effectively achieve high temporal and spatial resolution for dynamic PET. Our source code is available at https://github.com/Kuangxd/Neural-KMDS-Net/tree/main.

## 📝 요약

이 논문은 동적 양전자 방출 단층촬영(PET)에서 짧은 프레임으로 인해 발생하는 이미지 품질 문제를 해결하기 위해 모델 기반 신경망을 제안합니다. 제안된 KMDS-Net은 동적 PET의 프레임 간 공간 상관성과 프레임 내 구조적 일관성을 활용하여 다차원 희소 모델을 구축합니다. 신경망을 통해 매개변수 최적화를 수행하여 적응형 파라미터 최적화를 가능하게 하며, 이를 통해 동적 PET 이미지의 잡음을 효과적으로 제거합니다. 실험 결과, 제안된 방법은 기존 방법들보다 우수한 성능을 보이며, 동적 PET의 높은 시간 및 공간 해상도를 달성할 수 있음을 입증했습니다. 소스 코드는 온라인에서 제공됩니다.

## 🎯 주요 포인트

- 1. 동적 양전자 방출 단층촬영(PET) 이미지의 노이즈 제거를 위해 모델 기반 신경망을 제안했습니다.
- 2. 동적 PET에서 프레임 간 공간 상관성과 프레임 내 구조적 일관성을 활용하여 커널 공간 기반 다차원 희소(KMDS) 모델을 구축했습니다.
- 3. 신경망을 통해 매개변수 추정의 고유 형식을 대체하여 적응형 매개변수 최적화를 가능하게 했습니다.
- 4. 실험 결과, 제안된 신경망 KMDS-Net은 기존 방법보다 우수한 노이즈 제거 성능을 보였습니다.
- 5. 제안된 방법은 동적 PET의 높은 시간적 및 공간적 해상도를 효과적으로 달성할 수 있습니다.


---

*Generated on 2025-09-24 14:04:12*