<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:30:33.129558",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Gaussian Splatting",
    "Optimal Transport",
    "Gaussian Mixture Reduction",
    "Neural Rendering"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Gaussian Splatting": 0.8,
    "Optimal Transport": 0.85,
    "Gaussian Mixture Reduction": 0.78,
    "Neural Rendering": 0.8
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
        "rationale": "This is a specific technique central to the paper's contribution, offering a unique perspective on radiance field rendering.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Optimal Transport",
        "canonical": "Optimal Transport",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Optimal transport is a mathematical concept that underpins the proposed method, connecting it to broader mathematical and computational fields.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Gaussian Mixture Reduction",
        "canonical": "Gaussian Mixture Reduction",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a novel approach within the paper, crucial for understanding the proposed method's innovation in reducing Gaussian primitives.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Neural Rendering",
        "canonical": "Neural Rendering",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Neural rendering is a key application area for the proposed method, linking it to ongoing research in rendering technologies.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
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
      "candidate_surface": "Optimal Transport",
      "resolved_canonical": "Optimal Transport",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Gaussian Mixture Reduction",
      "resolved_canonical": "Gaussian Mixture Reduction",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Neural Rendering",
      "resolved_canonical": "Neural Rendering",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Gaussian Herding across Pens: An Optimal Transport Perspective on Global Gaussian Reduction for 3DGS

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2506.09534.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2506.09534](https://arxiv.org/abs/2506.09534)

## 🔗 유사한 논문
- [[2025-09-23/AD-GS_ Alternating Densification for Sparse-Input 3D Gaussian Splatting_20250923|AD-GS: Alternating Densification for Sparse-Input 3D Gaussian Splatting]] (89.4% similar)
- [[2025-09-18/Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images_20250918|Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images]] (88.0% similar)
- [[2025-09-22/GS-Scale_ Unlocking Large-Scale 3D Gaussian Splatting Training via Host Offloading_20250922|GS-Scale: Unlocking Large-Scale 3D Gaussian Splatting Training via Host Offloading]] (87.4% similar)
- [[2025-09-24/MEGS$^{2}$_ Memory-Efficient Gaussian Splatting via Spherical Gaussians and Unified Pruning_20250924|MEGS$^{2}$: Memory-Efficient Gaussian Splatting via Spherical Gaussians and Unified Pruning]] (87.3% similar)
- [[2025-09-24/FixingGS_ Enhancing 3D Gaussian Splatting via Training-Free Score Distillation_20250924|FixingGS: Enhancing 3D Gaussian Splatting via Training-Free Score Distillation]] (87.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Optimal Transport|Optimal Transport]]
**🔗 Specific Connectable**: [[keywords/Neural Rendering|Neural Rendering]]
**⚡ Unique Technical**: [[keywords/3D Gaussian Splatting|3D Gaussian Splatting]], [[keywords/Gaussian Mixture Reduction|Gaussian Mixture Reduction]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.09534v2 Announce Type: replace 
Abstract: 3D Gaussian Splatting (3DGS) has emerged as a powerful technique for radiance field rendering, but it typically requires millions of redundant Gaussian primitives, overwhelming memory and rendering budgets. Existing compaction approaches address this by pruning Gaussians based on heuristic importance scores, without global fidelity guarantee. To bridge this gap, we propose a novel optimal transport perspective that casts 3DGS compaction as global Gaussian mixture reduction. Specifically, we first minimize the composite transport divergence over a KD- tree partition to produce a compact geometric representation, and then decouple appearance from geometry by fine-tuning color and opacity attributes with far fewer Gaussian primitives. Experiments on benchmark datasets show that our method (i) yields negligible loss in rendering quality (PSNR, SSIM, LPIPS) compared to vanilla 3DGS with only 10% Gaussians; and (ii) consistently outperforms state- of-the-art 3DGS compaction techniques. Notably, our method is applicable to any stage of vanilla or accelerated 3DGS pipelines, providing an efficient and agnostic pathway to lightweight neural rendering. The code is publicly available at https://github.com/DrunkenPoet/GHAP

## 📝 요약

이 논문은 3D Gaussian Splatting(3DGS)의 효율성을 개선하기 위한 새로운 방법을 제안합니다. 기존의 방법은 수백만 개의 불필요한 Gaussian 프리미티브로 인해 메모리와 렌더링 자원이 과도하게 사용되는 문제를 겪습니다. 이를 해결하기 위해, 저자들은 최적 수송 관점을 도입하여 3DGS를 전역적인 Gaussian 혼합 축소 문제로 재구성했습니다. KD-트리 분할을 활용하여 기하학적 표현을 간소화하고, 색상과 불투명도 속성을 조정하여 훨씬 적은 Gaussian 프리미티브로 높은 렌더링 품질을 유지합니다. 실험 결과, 제안된 방법은 기존 3DGS와 비교해 렌더링 품질의 손실 없이 Gaussian 수를 10%로 줄일 수 있으며, 최신 기법들보다 일관되게 우수한 성능을 보였습니다. 이 방법은 3DGS 파이프라인의 어느 단계에서도 적용 가능하며, 경량화된 신경 렌더링을 위한 효율적인 경로를 제공합니다.

## 🎯 주요 포인트

- 1. 3D Gaussian Splatting(3DGS)의 과도한 메모리 사용 문제를 해결하기 위해 최적 수송 관점을 도입하여 전역적인 Gaussian 혼합물 축소를 제안합니다.
- 2. KD-트리 분할을 통해 복합 수송 발산을 최소화하여 컴팩트한 기하학적 표현을 생성하고, 색상 및 불투명도 속성을 미세 조정하여 적은 수의 Gaussian 원시로 외관을 분리합니다.
- 3. 제안된 방법은 기본 3DGS 대비 10%의 Gaussian만 사용해도 렌더링 품질(PNSR, SSIM, LPIPS) 손실이 거의 없으며, 최신 3DGS 압축 기술보다 일관되게 우수한 성능을 보입니다.
- 4. 본 방법은 기본 또는 가속화된 3DGS 파이프라인의 모든 단계에 적용 가능하며, 경량 신경 렌더링을 위한 효율적이고 독립적인 경로를 제공합니다.


---

*Generated on 2025-09-24 16:30:33*