---
keywords:
  - Progressive Multi-Resolution Training
  - Neural Network
  - DrivAerML dataset
  - drag coefficient
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17182
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:49:06.190868",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Progressive Multi-Resolution Training",
    "Neural Network",
    "DrivAerML dataset",
    "drag coefficient"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Progressive Multi-Resolution Training": 0.78,
    "Neural Network": 0.8,
    "DrivAerML dataset": 0.72,
    "drag coefficient": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Progressive Multi-Resolution Training",
        "canonical": "Progressive Multi-Resolution Training",
        "aliases": [
          "PMRT"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel training methodology specific to high-resolution aerodynamic predictions, offering significant improvements in efficiency.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "U-Net",
        "canonical": "Neural Network",
        "aliases": [
          "U-Net architecture"
        ],
        "category": "broad_technical",
        "rationale": "U-Net is a widely used neural network architecture, relevant for connecting concepts in deep learning and image processing.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "DrivAerML dataset",
        "canonical": "DrivAerML dataset",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This dataset is specifically used in the paper for model evaluation, providing a unique link to aerodynamic prediction research.",
        "novelty_score": 0.78,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "drag coefficient",
        "canonical": "drag coefficient",
        "aliases": [
          "c_d"
        ],
        "category": "specific_connectable",
        "rationale": "The drag coefficient is a critical parameter in aerodynamic studies, linking to broader research in fluid dynamics and vehicle design.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "simulation parameters",
      "training cost"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Progressive Multi-Resolution Training",
      "resolved_canonical": "Progressive Multi-Resolution Training",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "U-Net",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "DrivAerML dataset",
      "resolved_canonical": "DrivAerML dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "drag coefficient",
      "resolved_canonical": "drag coefficient",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# PMRT: A Training Recipe for Fast, 3D High-Resolution Aerodynamic Prediction

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17182.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17182](https://arxiv.org/abs/2509.17182)

## 🔗 유사한 논문
- [[2025-09-23/Machine learning-driven conservative-to-primitive conversion in hybrid piecewise polytropic and tabulated equations of state_20250923|Machine learning-driven conservative-to-primitive conversion in hybrid piecewise polytropic and tabulated equations of state]] (83.4% similar)
- [[2025-09-23/Point-RTD_ Replaced Token Denoising for Pretraining Transformer Models on Point Clouds_20250923|Point-RTD: Replaced Token Denoising for Pretraining Transformer Models on Point Clouds]] (81.3% similar)
- [[2025-09-19/MetaTrading_ An Immersion-Aware Model Trading Framework for Vehicular Metaverse Services_20250919|MetaTrading: An Immersion-Aware Model Trading Framework for Vehicular Metaverse Services]] (80.6% similar)
- [[2025-09-23/Comparison of Deterministic and Probabilistic Machine Learning Algorithms for Precise Dimensional Control and Uncertainty Quantification in Additive Manufacturing_20250923|Comparison of Deterministic and Probabilistic Machine Learning Algorithms for Precise Dimensional Control and Uncertainty Quantification in Additive Manufacturing]] (80.5% similar)
- [[2025-09-23/Resolving Turbulent Magnetohydrodynamics_ A Hybrid Operator-Diffusion Framework_20250923|Resolving Turbulent Magnetohydrodynamics: A Hybrid Operator-Diffusion Framework]] (80.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/drag coefficient|drag coefficient]]
**⚡ Unique Technical**: [[keywords/Progressive Multi-Resolution Training|Progressive Multi-Resolution Training]], [[keywords/DrivAerML dataset|DrivAerML dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17182v1 Announce Type: new 
Abstract: The aerodynamic optimization of cars requires close collaboration between aerodynamicists and stylists, while slow, expensive simulations remain a bottleneck. Surrogate models have been shown to accurately predict aerodynamics within the design space for which they were trained. However, many of these models struggle to scale to higher resolutions because of the 3D nature of the problem and data scarcity. We propose Progressive Multi-Resolution Training (PMRT), a probabilistic multi-resolution training schedule that enables training a U-Net to predict the drag coefficient ($c_d$) and high-resolution velocity fields (512 x 128 x 128) in 24 hours on a single NVIDIA H100 GPU, 7x cheaper than the high-resolution-only baseline, with similar accuracy. PMRT samples batches from three resolutions based on probabilities that change during training, starting with an emphasis on lower resolutions and gradually shifting toward higher resolutions. Since this is a training methodology, it can be adapted to other high-resolution-focused backbones. We also show that a single model can be trained across five datasets from different solvers, including a real-world dataset, by conditioning on the simulation parameters. In the DrivAerML dataset, our models achieve a $c_d$ $R^2$ of 0.975, matching literature baselines at a fraction of the training cost.

## 📝 요약

이 논문은 자동차 공기역학 최적화를 위한 새로운 방법론인 Progressive Multi-Resolution Training (PMRT)을 제안합니다. PMRT는 U-Net을 사용하여 항력 계수와 고해상도 속도장을 예측하는데, 단일 NVIDIA H100 GPU에서 24시간 내에 수행할 수 있어 기존 고해상도 모델 대비 7배 저렴한 비용으로 유사한 정확도를 제공합니다. 이 방법론은 낮은 해상도에서 높은 해상도로 점진적으로 전환하는 확률적 훈련 스케줄을 사용하며, 다양한 해상도에서 데이터를 샘플링하여 훈련합니다. 또한, PMRT는 다른 고해상도 모델에도 적용 가능하며, 다양한 시뮬레이션 데이터셋에 대해 단일 모델로 훈련할 수 있습니다. DrivAerML 데이터셋에서 PMRT 모델은 $c_d$ $R^2$ 값 0.975를 달성하여 기존 문헌의 기준을 적은 비용으로 충족합니다.

## 🎯 주요 포인트

- 1. 자동차 공기역학 최적화는 공기역학자와 스타일리스트 간의 긴밀한 협력이 필요하며, 느리고 비용이 많이 드는 시뮬레이션이 병목 현상을 초래합니다.
- 2. 대리 모델은 훈련된 설계 공간 내에서 공기역학을 정확하게 예측할 수 있지만, 3D 문제의 특성과 데이터 부족으로 인해 고해상도로 확장하는 데 어려움을 겪습니다.
- 3. PMRT는 U-Net을 사용하여 단일 NVIDIA H100 GPU에서 24시간 내에 항력 계수와 고해상도 속도 필드를 예측할 수 있게 하는 확률적 다중 해상도 훈련 방법론입니다.
- 4. PMRT는 훈련 중에 해상도를 기반으로 한 확률에 따라 배치를 샘플링하며, 낮은 해상도에서 높은 해상도로 점진적으로 전환합니다.
- 5. 단일 모델이 다양한 솔버의 다섯 가지 데이터셋, 포함하여 실제 데이터셋에서도 훈련될 수 있으며, DrivAerML 데이터셋에서 높은 정확도를 달성합니다.


---

*Generated on 2025-09-24 01:49:06*