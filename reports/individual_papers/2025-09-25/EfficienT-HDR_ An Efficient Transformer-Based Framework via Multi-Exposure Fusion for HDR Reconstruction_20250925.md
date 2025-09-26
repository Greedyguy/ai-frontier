---
keywords:
  - Transformer
  - High Dynamic Range Imaging
  - Multi-Exposure Fusion
  - Inverted Residual Embedding
  - Dynamic Tanh
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.19779
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:06:51.080299",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "High Dynamic Range Imaging",
    "Multi-Exposure Fusion",
    "Inverted Residual Embedding",
    "Dynamic Tanh"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "High Dynamic Range Imaging": 0.8,
    "Multi-Exposure Fusion": 0.78,
    "Inverted Residual Embedding": 0.77,
    "Dynamic Tanh": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision Transformer",
        "canonical": "Transformer",
        "aliases": [
          "ViT"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational model in deep learning, and linking to them aids in understanding the architectural basis of the proposed framework.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "High Dynamic Range Imaging",
        "canonical": "High Dynamic Range Imaging",
        "aliases": [
          "HDR Imaging"
        ],
        "category": "unique_technical",
        "rationale": "HDR Imaging is a specific application area that benefits from the proposed method, providing a direct link to the paper's focus.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multi-Exposure Fusion",
        "canonical": "Multi-Exposure Fusion",
        "aliases": [
          "MEF"
        ],
        "category": "unique_technical",
        "rationale": "MEF is a key technique discussed in the paper, essential for understanding the proposed HDR reconstruction approach.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Inverted Residual Embedding",
        "canonical": "Inverted Residual Embedding",
        "aliases": [
          "IRE"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel component introduced in the paper, crucial for achieving the lightweight design of the model.",
        "novelty_score": 0.75,
        "connectivity_score": 0.55,
        "specificity_score": 0.88,
        "link_intent_score": 0.77
      },
      {
        "surface": "Dynamic Tanh",
        "canonical": "Dynamic Tanh",
        "aliases": [
          "DyT"
        ],
        "category": "unique_technical",
        "rationale": "Dynamic Tanh is a specific activation function variant proposed in the paper, relevant for its role in reducing computational complexity.",
        "novelty_score": 0.68,
        "connectivity_score": 0.5,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "edge devices",
      "computational efficiency"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "High Dynamic Range Imaging",
      "resolved_canonical": "High Dynamic Range Imaging",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multi-Exposure Fusion",
      "resolved_canonical": "Multi-Exposure Fusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Inverted Residual Embedding",
      "resolved_canonical": "Inverted Residual Embedding",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.55,
        "specificity": 0.88,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Dynamic Tanh",
      "resolved_canonical": "Dynamic Tanh",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.5,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# EfficienT-HDR: An Efficient Transformer-Based Framework via Multi-Exposure Fusion for HDR Reconstruction

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19779.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.19779](https://arxiv.org/abs/2509.19779)

## 🔗 유사한 논문
- [[2025-09-23/PhysHDR_ When Lighting Meets Materials and Scene Geometry in HDR Reconstruction_20250923|PhysHDR: When Lighting Meets Materials and Scene Geometry in HDR Reconstruction]] (86.3% similar)
- [[2025-09-23/DT-NeRF_ A Diffusion and Transformer-Based Optimization Approach for Neural Radiance Fields in 3D Reconstruction_20250923|DT-NeRF: A Diffusion and Transformer-Based Optimization Approach for Neural Radiance Fields in 3D Reconstruction]] (84.1% similar)
- [[2025-09-24/Improving the color accuracy of lighting estimation models_20250924|Improving the color accuracy of lighting estimation models]] (83.8% similar)
- [[2025-09-22/DSDNet_ Raw Domain Demoir\'eing via Dual Color-Space Synergy_20250922|DSDNet: Raw Domain Demoir\'eing via Dual Color-Space Synergy]] (83.8% similar)
- [[2025-09-24/Lightweight Vision Transformer with Window and Spatial Attention for Food Image Classification_20250924|Lightweight Vision Transformer with Window and Spatial Attention for Food Image Classification]] (83.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**⚡ Unique Technical**: [[keywords/High Dynamic Range Imaging|High Dynamic Range Imaging]], [[keywords/Multi-Exposure Fusion|Multi-Exposure Fusion]], [[keywords/Inverted Residual Embedding|Inverted Residual Embedding]], [[keywords/Dynamic Tanh|Dynamic Tanh]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19779v1 Announce Type: new 
Abstract: Achieving high-quality High Dynamic Range (HDR) imaging on resource-constrained edge devices is a critical challenge in computer vision, as its performance directly impacts downstream tasks such as intelligent surveillance and autonomous driving. Multi-Exposure Fusion (MEF) is a mainstream technique to achieve this goal; however, existing methods generally face the dual bottlenecks of high computational costs and ghosting artifacts, hindering their widespread deployment. To this end, this study proposes a light-weight Vision Transformer architecture designed explicitly for HDR reconstruction to overcome these limitations. This study is based on the Context-Aware Vision Transformer and begins by converting input images to the YCbCr color space to separate luminance and chrominance information. It then employs an Intersection-Aware Adaptive Fusion (IAAF) module to suppress ghosting effectively. To further achieve a light-weight design, we introduce Inverted Residual Embedding (IRE), Dynamic Tanh (DyT), and propose Enhanced Multi-Scale Dilated Convolution (E-MSDC) to reduce computational complexity at multiple levels. Our study ultimately contributes two model versions: a main version for high visual quality and a light-weight version with advantages in computational efficiency, both of which achieve an excellent balance between performance and image quality. Experimental results demonstrate that, compared to the baseline, the main version reduces FLOPS by approximately 67% and increases inference speed by more than fivefold on CPU and 2.5 times on an edge device. These results confirm that our method provides an efficient and ghost-free HDR imaging solution for edge devices, demonstrating versatility and practicality across various dynamic scenarios.

## 📝 요약

이 연구는 자원 제약이 있는 엣지 디바이스에서 고품질 HDR 이미징을 구현하기 위한 경량 비전 트랜스포머 아키텍처를 제안합니다. 기존의 다중 노출 융합(MEF) 기법은 높은 계산 비용과 고스트 현상 문제를 겪고 있는데, 이를 해결하기 위해 본 연구는 Context-Aware Vision Transformer를 기반으로 YCbCr 색 공간 변환과 Intersection-Aware Adaptive Fusion(IAAF) 모듈을 활용하여 고스트 현상을 억제합니다. 또한, Inverted Residual Embedding(IRE), Dynamic Tanh(DyT), Enhanced Multi-Scale Dilated Convolution(E-MSDC)을 도입하여 계산 복잡성을 줄였습니다. 연구 결과, 제안된 모델은 성능과 이미지 품질의 균형을 유지하면서도 계산 효율성을 크게 향상시켰으며, 실험 결과 CPU에서 FLOPS를 약 67% 줄이고 추론 속도를 5배 이상, 엣지 디바이스에서는 2.5배 증가시켰습니다. 이로써 다양한 동적 시나리오에서 효율적이고 고스트 없는 HDR 이미징 솔루션을 제공함을 입증했습니다.

## 🎯 주요 포인트

- 1. 본 연구는 자원 제약이 있는 엣지 디바이스에서 고품질 HDR 이미징을 위한 경량 비전 트랜스포머 아키텍처를 제안합니다.
- 2. 입력 이미지를 YCbCr 색상 공간으로 변환하여 휘도와 색차 정보를 분리하고, 교차 인식 적응 융합 모듈(IAAF)을 사용하여 고스트 현상을 효과적으로 억제합니다.
- 3. 경량 설계를 위해 Inverted Residual Embedding (IRE), Dynamic Tanh (DyT), 그리고 Enhanced Multi-Scale Dilated Convolution (E-MSDC)을 도입하여 여러 수준에서 계산 복잡성을 줄입니다.
- 4. 실험 결과, 주 버전은 FLOPS를 약 67% 감소시키고 CPU에서 추론 속도를 5배 이상, 엣지 디바이스에서 2.5배 증가시킵니다.
- 5. 제안된 방법은 엣지 디바이스에서 효율적이고 고스트 없는 HDR 이미징 솔루션을 제공하며, 다양한 동적 시나리오에서 실용성과 범용성을 입증합니다.


---

*Generated on 2025-09-26 09:06:51*