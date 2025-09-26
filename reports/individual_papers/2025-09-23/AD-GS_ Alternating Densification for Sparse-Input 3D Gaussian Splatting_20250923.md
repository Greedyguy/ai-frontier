---
keywords:
  - 3D Gaussian Splatting
  - Alternating Densification
  - Photometric Loss
  - Opacity Pruning
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.11003
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:37:18.933217",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Gaussian Splatting",
    "Alternating Densification",
    "Photometric Loss",
    "Opacity Pruning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Gaussian Splatting": 0.8,
    "Alternating Densification": 0.82,
    "Photometric Loss": 0.78,
    "Opacity Pruning": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "3D Gaussian Splatting",
        "canonical": "3D Gaussian Splatting",
        "aliases": [
          "3DGS"
        ],
        "category": "unique_technical",
        "rationale": "This technique is central to the paper and represents a unique approach to 3D rendering.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Alternating Densification",
        "canonical": "Alternating Densification",
        "aliases": [
          "AD-GS"
        ],
        "category": "unique_technical",
        "rationale": "The proposed method introduces a novel framework for controlling model capacity and improving rendering.",
        "novelty_score": 0.88,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Photometric Loss",
        "canonical": "Photometric Loss",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This loss function is crucial for refining scene details and is a common concept in computer vision.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Opacity Pruning",
        "canonical": "Opacity Pruning",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This technique is essential for reducing model complexity and improving geometric consistency.",
        "novelty_score": 0.7,
        "connectivity_score": 0.55,
        "specificity_score": 0.8,
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
      "candidate_surface": "3D Gaussian Splatting",
      "resolved_canonical": "3D Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Alternating Densification",
      "resolved_canonical": "Alternating Densification",
      "decision": "linked",
      "scores": {
        "novelty": 0.88,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Photometric Loss",
      "resolved_canonical": "Photometric Loss",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Opacity Pruning",
      "resolved_canonical": "Opacity Pruning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.55,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# AD-GS: Alternating Densification for Sparse-Input 3D Gaussian Splatting

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.11003.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.11003](https://arxiv.org/abs/2509.11003)

## 🔗 유사한 논문
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (88.4% similar)
- [[2025-09-18/Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images_20250918|Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images]] (87.8% similar)
- [[2025-09-23/Accurate and Complete Surface Reconstruction from 3D Gaussians via Direct SDF Learning_20250923|Accurate and Complete Surface Reconstruction from 3D Gaussians via Direct SDF Learning]] (87.7% similar)
- [[2025-09-23/Quantifying and Alleviating Co-Adaptation in Sparse-View 3D Gaussian Splatting_20250923|Quantifying and Alleviating Co-Adaptation in Sparse-View 3D Gaussian Splatting]] (86.2% similar)
- [[2025-09-23/Multi-viewregulated gaussian splatting for novel view synthesis_20250923|Multi-viewregulated gaussian splatting for novel view synthesis]] (86.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Photometric Loss|Photometric Loss]]
**⚡ Unique Technical**: [[keywords/3D Gaussian Splatting|3D Gaussian Splatting]], [[keywords/Alternating Densification|Alternating Densification]], [[keywords/Opacity Pruning|Opacity Pruning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.11003v2 Announce Type: replace-cross 
Abstract: 3D Gaussian Splatting (3DGS) has shown impressive results in real-time novel view synthesis. However, it often struggles under sparse-view settings, producing undesirable artifacts such as floaters, inaccurate geometry, and overfitting due to limited observations. We find that a key contributing factor is uncontrolled densification, where adding Gaussian primitives rapidly without guidance can harm geometry and cause artifacts. We propose AD-GS, a novel alternating densification framework that interleaves high and low densification phases. During high densification, the model densifies aggressively, followed by photometric loss based training to capture fine-grained scene details. Low densification then primarily involves aggressive opacity pruning of Gaussians followed by regularizing their geometry through pseudo-view consistency and edge-aware depth smoothness. This alternating approach helps reduce overfitting by carefully controlling model capacity growth while progressively refining the scene representation. Extensive experiments on challenging datasets demonstrate that AD-GS significantly improves rendering quality and geometric consistency compared to existing methods. The source code for our model can be found on our project page: https://gurutvapatle.github.io/publications/2025/ADGS.html .

## 📝 요약

3D Gaussian Splatting(3DGS)은 실시간 새로운 시점 합성에서 뛰어난 성과를 보였으나, 희소한 시점에서는 부정확한 기하학과 과적합 등의 문제가 발생합니다. 이는 무분별한 밀도 증가가 주원인으로, 이를 해결하기 위해 AD-GS라는 새로운 교차 밀도 증가 프레임워크를 제안합니다. AD-GS는 높은 밀도 증가 단계와 낮은 밀도 증가 단계를 번갈아 수행하며, 높은 밀도 증가 단계에서는 세밀한 장면 세부사항을 포착하고, 낮은 밀도 증가 단계에서는 불필요한 가우시안의 불투명도를 줄이고 기하학을 정규화합니다. 이 방법은 모델 용량의 성장을 조절하여 과적합을 줄이고 장면 표현을 점진적으로 개선합니다. 실험 결과, AD-GS는 기존 방법들보다 렌더링 품질과 기하학적 일관성을 크게 향상시킵니다.

## 🎯 주요 포인트

- 1. 3D Gaussian Splatting(3DGS)는 실시간 새로운 뷰 합성에서 뛰어난 성과를 보이지만, 희소한 뷰 환경에서는 부정확한 기하학과 과적합 등의 문제를 겪습니다.
- 2. 이러한 문제의 주요 원인은 통제되지 않은 밀집화로, 가우시안 프리미티브를 무분별하게 추가하면 기하학에 해를 끼치고 아티팩트를 유발할 수 있습니다.
- 3. AD-GS는 고밀집화와 저밀집화 단계를 교차하여 적용하는 새로운 교대 밀집화 프레임워크로, 장면 표현을 점진적으로 개선합니다.
- 4. AD-GS는 모델 용량의 성장을 신중하게 제어하여 과적합을 줄이며, 기존 방법에 비해 렌더링 품질과 기하학적 일관성을 크게 향상시킵니다.
- 5. AD-GS의 소스 코드는 프로젝트 페이지에서 확인할 수 있습니다.


---

*Generated on 2025-09-24 05:37:18*