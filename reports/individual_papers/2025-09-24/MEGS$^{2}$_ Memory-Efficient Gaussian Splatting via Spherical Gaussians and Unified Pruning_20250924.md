<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:40:51.604371",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Gaussian Splatting",
    "Spherical Gaussians",
    "Unified Pruning",
    "Rendering Memory"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Gaussian Splatting": 0.78,
    "Spherical Gaussians": 0.72,
    "Unified Pruning": 0.75,
    "Rendering Memory": 0.7
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
        "rationale": "This is a specific technique central to the paper's contribution, offering unique insights into memory-efficient rendering.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Spherical Gaussians",
        "canonical": "Spherical Gaussians",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A novel approach in the paper that replaces spherical harmonics, crucial for memory efficiency.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      },
      {
        "surface": "Unified Pruning",
        "canonical": "Unified Pruning",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Represents a key innovation in the paper, addressing both primitive-number and lobe-number pruning.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      },
      {
        "surface": "Rendering Memory",
        "canonical": "Rendering Memory",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A critical bottleneck addressed by the paper, relevant for discussions on memory optimization.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.7
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
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Spherical Gaussians",
      "resolved_canonical": "Spherical Gaussians",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Unified Pruning",
      "resolved_canonical": "Unified Pruning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Rendering Memory",
      "resolved_canonical": "Rendering Memory",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# MEGS$^{2}$: Memory-Efficient Gaussian Splatting via Spherical Gaussians and Unified Pruning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.07021.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.07021](https://arxiv.org/abs/2509.07021)

## 🔗 유사한 논문
- [[2025-09-22/GS-Scale_ Unlocking Large-Scale 3D Gaussian Splatting Training via Host Offloading_20250922|GS-Scale: Unlocking Large-Scale 3D Gaussian Splatting Training via Host Offloading]] (87.4% similar)
- [[2025-09-23/AD-GS_ Alternating Densification for Sparse-Input 3D Gaussian Splatting_20250923|AD-GS: Alternating Densification for Sparse-Input 3D Gaussian Splatting]] (85.6% similar)
- [[2025-09-23/HyRF_ Hybrid Radiance Fields for Memory-efficient and High-quality Novel View Synthesis_20250923|HyRF: Hybrid Radiance Fields for Memory-efficient and High-quality Novel View Synthesis]] (85.2% similar)
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (84.8% similar)
- [[2025-09-23/Neural-MMGS_ Multi-modal Neural Gaussian Splats for Large-Scale Scene Reconstruction_20250923|Neural-MMGS: Multi-modal Neural Gaussian Splats for Large-Scale Scene Reconstruction]] (84.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Rendering Memory|Rendering Memory]]
**⚡ Unique Technical**: [[keywords/3D Gaussian Splatting|3D Gaussian Splatting]], [[keywords/Spherical Gaussians|Spherical Gaussians]], [[keywords/Unified Pruning|Unified Pruning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.07021v2 Announce Type: replace-cross 
Abstract: 3D Gaussian Splatting (3DGS) has emerged as a dominant novel-view synthesis technique, but its high memory consumption severely limits its applicability on edge devices. A growing number of 3DGS compression methods have been proposed to make 3DGS more efficient, yet most only focus on storage compression and fail to address the critical bottleneck of rendering memory. To address this problem, we introduce MEGS$^{2}$, a novel memory-efficient framework that tackles this challenge by jointly optimizing two key factors: the total primitive number and the parameters per primitive, achieving unprecedented memory compression. Specifically, we replace the memory-intensive spherical harmonics with lightweight, arbitrarily oriented spherical Gaussian lobes as our color representations. More importantly, we propose a unified soft pruning framework that models primitive-number and lobe-number pruning as a single constrained optimization problem. Experiments show that MEGS$^{2}$ achieves a 50% static VRAM reduction and a 40% rendering VRAM reduction compared to existing methods, while maintaining comparable rendering quality. Project page: https://megs-2.github.io/

## 📝 요약

3D Gaussian Splatting(3DGS)은 새로운 시각 합성 기술로 주목받고 있으나, 높은 메모리 소모로 인해 엣지 디바이스에서의 활용이 제한적입니다. 이를 해결하기 위해 MEGS$^{2}$라는 메모리 효율적인 프레임워크를 제안합니다. 이 프레임워크는 총 프리미티브 수와 프리미티브 당 파라미터를 최적화하여 메모리 압축을 달성합니다. 특히, 메모리 집약적인 구형 조화를 경량의 구형 가우시안 로브로 대체하고, 프리미티브 수와 로브 수 가지치기를 단일 최적화 문제로 모델링하는 통합 소프트 가지치기 프레임워크를 제안합니다. 실험 결과, MEGS$^{2}$는 기존 방법에 비해 정적 VRAM을 50%, 렌더링 VRAM을 40% 줄이면서도 유사한 렌더링 품질을 유지합니다.

## 🎯 주요 포인트

- 1. 3D Gaussian Splatting(3DGS)의 높은 메모리 소비 문제를 해결하기 위해 MEGS$^{2}$라는 새로운 메모리 효율적 프레임워크를 제안합니다.
- 2. MEGS$^{2}$는 총 프리미티브 수와 프리미티브당 파라미터를 최적화하여 메모리 압축을 달성합니다.
- 3. 메모리 집약적인 구형 조화를 경량의 임의 방향 구형 가우시안 로브로 대체하여 색상 표현을 개선합니다.
- 4. 통합 소프트 프루닝 프레임워크를 통해 프리미티브 수와 로브 수의 프루닝을 단일 제약 최적화 문제로 모델링합니다.
- 5. MEGS$^{2}$는 기존 방법에 비해 정적 VRAM을 50%, 렌더링 VRAM을 40% 감소시키면서도 유사한 렌더링 품질을 유지합니다.


---

*Generated on 2025-09-24 14:40:51*