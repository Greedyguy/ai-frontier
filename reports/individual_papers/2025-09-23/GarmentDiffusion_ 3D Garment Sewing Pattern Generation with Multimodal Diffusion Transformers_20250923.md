---
keywords:
  - Multimodal Learning
  - Diffusion Transformer
  - 3D Sewing Patterns
  - GarmentDiffusion
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2504.21476
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:55:47.945336",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Diffusion Transformer",
    "3D Sewing Patterns",
    "GarmentDiffusion"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.8,
    "Diffusion Transformer": 0.78,
    "3D Sewing Patterns": 0.77,
    "GarmentDiffusion": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal inputs",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal",
          "Multimodal Input"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Learning is a trending concept that enhances connectivity by integrating multiple data types, relevant to the paper's focus on text, image, and pattern inputs.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Diffusion transformer",
        "canonical": "Diffusion Transformer",
        "aliases": [
          "Diffusion Model",
          "Transformer"
        ],
        "category": "unique_technical",
        "rationale": "The Diffusion Transformer is a novel approach within the paper, offering a unique angle on generative modeling that can link to broader transformer discussions.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "3D sewing patterns",
        "canonical": "3D Sewing Patterns",
        "aliases": [
          "3D Patterns",
          "Sewing Patterns"
        ],
        "category": "unique_technical",
        "rationale": "3D Sewing Patterns are central to the paper's contribution, providing a specific technical focus that can connect to discussions on garment design and manufacturing.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "GarmentDiffusion",
        "canonical": "GarmentDiffusion",
        "aliases": [
          "Garment Diffusion"
        ],
        "category": "unique_technical",
        "rationale": "GarmentDiffusion is the core model introduced in the paper, representing a unique technical advancement in garment pattern generation.",
        "novelty_score": 0.8,
        "connectivity_score": 0.55,
        "specificity_score": 0.9,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "approach",
      "model",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal inputs",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Diffusion transformer",
      "resolved_canonical": "Diffusion Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "3D sewing patterns",
      "resolved_canonical": "3D Sewing Patterns",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "GarmentDiffusion",
      "resolved_canonical": "GarmentDiffusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.55,
        "specificity": 0.9,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# GarmentDiffusion: 3D Garment Sewing Pattern Generation with Multimodal Diffusion Transformers

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2504.21476.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2504.21476](https://arxiv.org/abs/2504.21476)

## 🔗 유사한 논문
- [[2025-09-18/DPDEdit_ Detail-Preserved Diffusion Models for Multimodal Fashion Image Editing_20250918|DPDEdit: Detail-Preserved Diffusion Models for Multimodal Fashion Image Editing]] (84.2% similar)
- [[2025-09-22/Kuramoto Orientation Diffusion Models_20250922|Kuramoto Orientation Diffusion Models]] (81.0% similar)
- [[2025-09-22/LowDiff_ Efficient Diffusion Sampling with Low-Resolution Condition_20250922|LowDiff: Efficient Diffusion Sampling with Low-Resolution Condition]] (80.7% similar)
- [[2025-09-22/RespoDiff_ Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation_20250922|RespoDiff: Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation]] (80.6% similar)
- [[2025-09-22/G2D2_ Gradient-Guided Discrete Diffusion for Inverse Problem Solving_20250922|G2D2: Gradient-Guided Discrete Diffusion for Inverse Problem Solving]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Diffusion Transformer|Diffusion Transformer]], [[keywords/3D Sewing Patterns|3D Sewing Patterns]], [[keywords/GarmentDiffusion|GarmentDiffusion]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.21476v4 Announce Type: replace-cross 
Abstract: Garment sewing patterns are fundamental design elements that bridge the gap between design concepts and practical manufacturing. The generative modeling of sewing patterns is crucial for creating diversified garments. However, existing approaches are limited either by reliance on a single input modality or by suboptimal generation efficiency. In this work, we present GarmentDiffusion, a new generative model capable of producing centimeter-precise, vectorized 3D sewing patterns from multimodal inputs (text, image, and incomplete sewing pattern). Our method efficiently encodes 3D sewing pattern parameters into compact edge token representations, achieving a sequence length that is 10 times shorter than that of the autoregressive SewingGPT in DressCode. By employing a diffusion transformer, we simultaneously denoise all edge tokens along the temporal axis, while maintaining a constant number of denoising steps regardless of dataset-specific edge and panel statistics. With all combination of designs of our model, the sewing pattern generation speed is accelerated by 100 times compared to SewingGPT. We achieve new state-of-the-art results on DressCodeData, as well as on the largest sewing pattern dataset, namely GarmentCodeData. The project website is available at https://shenfu-research.github.io/Garment-Diffusion/.

## 📝 요약

GarmentDiffusion은 텍스트, 이미지, 불완전한 패턴 등 다중 입력을 활용하여 정밀한 3D 의류 패턴을 생성하는 새로운 모델입니다. 이 모델은 3D 패턴 파라미터를 효율적으로 인코딩하여 기존의 SewingGPT보다 10배 짧은 시퀀스 길이를 달성하며, 변환기를 통해 모든 엣지 토큰을 동시에 디노이즈합니다. 이를 통해 패턴 생성 속도가 100배 빨라졌으며, DressCodeData와 GarmentCodeData에서 최첨단 성능을 기록했습니다.

## 🎯 주요 포인트

- 1. GarmentDiffusion은 텍스트, 이미지, 불완전한 패턴 등 다중 입력 모달리티로부터 센티미터 단위의 정밀한 벡터화된 3D 봉제 패턴을 생성할 수 있는 새로운 생성 모델입니다.
- 2. 이 모델은 3D 봉제 패턴 파라미터를 컴팩트한 엣지 토큰 표현으로 효율적으로 인코딩하여, DressCode의 SewingGPT보다 시퀀스 길이를 10배 단축시켰습니다.
- 3. GarmentDiffusion은 확산 변환기를 사용하여 모든 엣지 토큰을 동시에 노이즈 제거하며, 데이터셋 특정 엣지 및 패널 통계에 관계없이 일정한 노이즈 제거 단계를 유지합니다.
- 4. 이 모델은 SewingGPT에 비해 봉제 패턴 생성 속도를 100배 가속화하며, DressCodeData 및 GarmentCodeData에서 새로운 최첨단 성능을 달성했습니다.


---

*Generated on 2025-09-24 00:55:47*