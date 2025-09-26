---
keywords:
  - LiDAR-to-Model Registration
  - Semantic 3D City Models
  - Plane-based Registration
  - Level of Detail 2 (LoD2)
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.16832
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:35:51.198150",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "LiDAR-to-Model Registration",
    "Semantic 3D City Models",
    "Plane-based Registration",
    "Level of Detail 2 (LoD2)"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "LiDAR-to-Model Registration": 0.78,
    "Semantic 3D City Models": 0.74,
    "Plane-based Registration": 0.77,
    "Level of Detail 2 (LoD2)": 0.73
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "LiDAR-to-Model registration",
        "canonical": "LiDAR-to-Model Registration",
        "aliases": [
          "LiDAR Model Alignment"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's contribution and links to urban digital twinning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "semantic 3D city models",
        "canonical": "Semantic 3D City Models",
        "aliases": [
          "3D City Models"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is crucial for understanding the context of urban digital twinning.",
        "novelty_score": 0.58,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.74
      },
      {
        "surface": "plane-based fine registration",
        "canonical": "Plane-based Registration",
        "aliases": [
          "Fine Registration"
        ],
        "category": "unique_technical",
        "rationale": "This method is a key innovation in the paper, addressing model uncertainty.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      },
      {
        "surface": "Level of Detail 2",
        "canonical": "Level of Detail 2 (LoD2)",
        "aliases": [
          "LoD2"
        ],
        "category": "specific_connectable",
        "rationale": "LoD2 is a specific concept in 3D modeling that affects registration accuracy.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.82,
        "link_intent_score": 0.73
      }
    ],
    "ban_list_suggestions": [
      "digital construction",
      "change detection",
      "model refinement"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "LiDAR-to-Model registration",
      "resolved_canonical": "LiDAR-to-Model Registration",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "semantic 3D city models",
      "resolved_canonical": "Semantic 3D City Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.74
      }
    },
    {
      "candidate_surface": "plane-based fine registration",
      "resolved_canonical": "Plane-based Registration",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Level of Detail 2",
      "resolved_canonical": "Level of Detail 2 (LoD2)",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.82,
        "link_intent": 0.73
      }
    }
  ]
}
-->

# L2M-Reg: Building-level Uncertainty-aware Registration of Outdoor LiDAR Point Clouds and Semantic 3D City Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16832.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.16832](https://arxiv.org/abs/2509.16832)

## 🔗 유사한 논문
- [[2025-09-22/Ideal Registration? Segmentation is All You Need_20250922|Ideal Registration? Segmentation is All You Need]] (81.3% similar)
- [[2025-09-23/Automated Facility Enumeration for Building Compliance Checking using Door Detection and Large Language Models_20250923|Automated Facility Enumeration for Building Compliance Checking using Door Detection and Large Language Models]] (80.9% similar)
- [[2025-09-19/From Pixels to Urban Policy-Intelligence_ Recovering Legacy Effects of Redlining with a Multimodal LLM_20250919|From Pixels to Urban Policy-Intelligence: Recovering Legacy Effects of Redlining with a Multimodal LLM]] (80.4% similar)
- [[2025-09-22/Self-Supervised Cross-Modal Learning for Image-to-Point Cloud Registration_20250922|Self-Supervised Cross-Modal Learning for Image-to-Point Cloud Registration]] (80.3% similar)
- [[2025-09-19/Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments_20250919|Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments]] (79.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Semantic 3D City Models|Semantic 3D City Models]], [[keywords/Level of Detail 2 (LoD2)|Level of Detail 2 (LoD2)]]
**⚡ Unique Technical**: [[keywords/LiDAR-to-Model Registration|LiDAR-to-Model Registration]], [[keywords/Plane-based Registration|Plane-based Registration]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16832v1 Announce Type: new 
Abstract: Accurate registration between LiDAR (Light Detection and Ranging) point clouds and semantic 3D city models is a fundamental topic in urban digital twinning and a prerequisite for downstream tasks, such as digital construction, change detection and model refinement. However, achieving accurate LiDAR-to-Model registration at individual building level remains challenging, particularly due to the generalization uncertainty in semantic 3D city models at the Level of Detail 2 (LoD2). This paper addresses this gap by proposing L2M-Reg, a plane-based fine registration method that explicitly accounts for model uncertainty. L2M-Reg consists of three key steps: establishing reliable plane correspondence, building a pseudo-plane-constrained Gauss-Helmert model, and adaptively estimating vertical translation. Experiments on three real-world datasets demonstrate that L2M-Reg is both more accurate and computationally efficient than existing ICP-based and plane-based methods. Overall, L2M-Reg provides a novel building-level solution regarding LiDAR-to-Model registration when model uncertainty is present.

## 📝 요약

이 논문은 LiDAR 점군과 의미론적 3D 도시 모델 간의 정밀한 정합을 위한 방법론인 L2M-Reg를 제안합니다. 이는 도시 디지털 트윈 및 디지털 건설, 변화 탐지, 모델 개선 등의 작업에 필수적입니다. 특히, LoD2 수준의 일반화 불확실성으로 인해 개별 건물 수준에서의 정합이 어려운 문제를 해결합니다. L2M-Reg는 신뢰할 수 있는 평면 대응 설정, 의사 평면 제약 Gauss-Helmert 모델 구축, 적응적 수직 변환 추정을 통해 모델 불확실성을 명시적으로 고려합니다. 세 가지 실제 데이터셋 실험 결과, L2M-Reg는 기존의 ICP 기반 및 평면 기반 방법보다 더 정확하고 효율적임을 보여줍니다. L2M-Reg는 모델 불확실성이 존재할 때 LiDAR-모델 정합에 대한 새로운 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. LiDAR 점군과 의미론적 3D 도시 모델 간의 정확한 정합은 도시 디지털 트윈 및 디지털 건설, 변화 탐지, 모델 개선과 같은 후속 작업의 필수 조건입니다.
- 2. L2M-Reg는 모델 불확실성을 명시적으로 고려하는 평면 기반의 정밀 정합 방법을 제안하여, LoD2 수준에서의 일반화 불확실성 문제를 해결합니다.
- 3. L2M-Reg는 신뢰할 수 있는 평면 대응 설정, 의사 평면 제약 Gauss-Helmert 모델 구축, 적응형 수직 변위 추정을 포함한 세 가지 주요 단계로 구성됩니다.
- 4. 세 가지 실제 데이터셋에 대한 실험 결과, L2M-Reg는 기존의 ICP 기반 및 평면 기반 방법보다 더 정확하고 계산 효율적임을 보여줍니다.
- 5. L2M-Reg는 모델 불확실성이 존재할 때 LiDAR-to-Model 정합에 대한 새로운 건물 수준 솔루션을 제공합니다.


---

*Generated on 2025-09-24 04:35:51*