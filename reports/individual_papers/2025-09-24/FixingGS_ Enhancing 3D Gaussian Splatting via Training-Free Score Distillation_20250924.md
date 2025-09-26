<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:08:32.796471",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Gaussian Splatting",
    "Diffusion Model",
    "Multi-view Consistency",
    "Artifact Removal"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Gaussian Splatting": 0.8,
    "Diffusion Model": 0.79,
    "Multi-view Consistency": 0.78,
    "Artifact Removal": 0.75
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
        "rationale": "This is a specific technique central to the paper's contribution, enhancing connectivity within 3D reconstruction discussions.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Diffusion Model",
        "canonical": "Diffusion Model",
        "aliases": [
          "Diffusion Models"
        ],
        "category": "specific_connectable",
        "rationale": "Diffusion models are increasingly relevant in enhancing 3D reconstruction, offering strong connectivity to generative model discussions.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      },
      {
        "surface": "Multi-view Consistency",
        "canonical": "Multi-view Consistency",
        "aliases": [
          "Cross-view Consistency"
        ],
        "category": "specific_connectable",
        "rationale": "Ensuring consistency across multiple views is crucial for 3D reconstruction, linking to broader topics in computer vision.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Artifact Removal",
        "canonical": "Artifact Removal",
        "aliases": [
          "Artifact Reduction"
        ],
        "category": "specific_connectable",
        "rationale": "Artifact removal is a key challenge in 3D reconstruction, connecting to image processing and enhancement techniques.",
        "novelty_score": 0.58,
        "connectivity_score": 0.77,
        "specificity_score": 0.72,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "3D Gaussian Splatting",
      "resolved_canonical": "3D Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Diffusion Model",
      "resolved_canonical": "Diffusion Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Multi-view Consistency",
      "resolved_canonical": "Multi-view Consistency",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Artifact Removal",
      "resolved_canonical": "Artifact Removal",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.77,
        "specificity": 0.72,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# FixingGS: Enhancing 3D Gaussian Splatting via Training-Free Score Distillation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18759.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18759](https://arxiv.org/abs/2509.18759)

## 🔗 유사한 논문
- [[2025-09-23/AD-GS_ Alternating Densification for Sparse-Input 3D Gaussian Splatting_20250923|AD-GS: Alternating Densification for Sparse-Input 3D Gaussian Splatting]] (88.5% similar)
- [[2025-09-23/Accurate and Complete Surface Reconstruction from 3D Gaussians via Direct SDF Learning_20250923|Accurate and Complete Surface Reconstruction from 3D Gaussians via Direct SDF Learning]] (86.0% similar)
- [[2025-09-23/Quantifying and Alleviating Co-Adaptation in Sparse-View 3D Gaussian Splatting_20250923|Quantifying and Alleviating Co-Adaptation in Sparse-View 3D Gaussian Splatting]] (85.6% similar)
- [[2025-09-18/Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images_20250918|Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images]] (85.5% similar)
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (84.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Diffusion Model|Diffusion Model]], [[keywords/Multi-view Consistency|Multi-view Consistency]], [[keywords/Artifact Removal|Artifact Removal]]
**⚡ Unique Technical**: [[keywords/3D Gaussian Splatting|3D Gaussian Splatting]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18759v1 Announce Type: new 
Abstract: Recently, 3D Gaussian Splatting (3DGS) has demonstrated remarkable success in 3D reconstruction and novel view synthesis. However, reconstructing 3D scenes from sparse viewpoints remains highly challenging due to insufficient visual information, which results in noticeable artifacts persisting across the 3D representation. To address this limitation, recent methods have resorted to generative priors to remove artifacts and complete missing content in under-constrained areas. Despite their effectiveness, these approaches struggle to ensure multi-view consistency, resulting in blurred structures and implausible details. In this work, we propose FixingGS, a training-free method that fully exploits the capabilities of the existing diffusion model for sparse-view 3DGS reconstruction enhancement. At the core of FixingGS is our distillation approach, which delivers more accurate and cross-view coherent diffusion priors, thereby enabling effective artifact removal and inpainting. In addition, we propose an adaptive progressive enhancement scheme that further refines reconstructions in under-constrained regions. Extensive experiments demonstrate that FixingGS surpasses existing state-of-the-art methods with superior visual quality and reconstruction performance. Our code will be released publicly.

## 📝 요약

최근 3D 가우시안 스플래팅(3DGS)은 3D 재구성과 새로운 시점 생성에서 큰 성공을 거두었지만, 희소한 시점에서의 3D 장면 재구성은 여전히 어려운 과제입니다. 이는 시각 정보가 부족하여 3D 표현에 눈에 띄는 결함이 남기 때문입니다. 기존 방법들은 생성적 사전 지식을 활용하여 이러한 결함을 제거하고 부족한 부분을 보완하려 했으나, 다중 시점 일관성을 보장하지 못해 흐릿한 구조와 비현실적인 세부사항이 발생했습니다. 본 연구에서는 FixingGS라는 새로운 방법을 제안합니다. 이는 기존 확산 모델을 활용하여 희소 시점 3DGS 재구성을 개선하는 훈련이 필요 없는 방법입니다. FixingGS의 핵심은 보다 정확하고 시점 간 일관된 확산 사전 지식을 제공하는 증류 접근법으로, 효과적인 결함 제거와 보완을 가능하게 합니다. 또한, 적응적 점진적 향상 방식을 제안하여 제약이 적은 영역에서의 재구성을 더욱 정교하게 합니다. 실험 결과, FixingGS는 기존 최첨단 방법들을 뛰어넘는 우수한 시각적 품질과 재구성 성능을 보여주었습니다. 코드는 공개될 예정입니다.

## 🎯 주요 포인트

- 1. 3D Gaussian Splatting(3DGS)은 3D 재구성과 새로운 시점 합성에서 뛰어난 성과를 보였으나, 희소한 시점으로부터의 3D 장면 재구성은 여전히 도전적이다.
- 2. 기존 방법들은 생성적 사전 지식을 활용하여 아티팩트를 제거하고 부족한 콘텐츠를 보완하지만, 다중 시점 일관성을 보장하는 데 어려움을 겪는다.
- 3. FixingGS는 기존 확산 모델의 능력을 활용하여 희소 시점 3DGS 재구성을 향상시키는 훈련이 필요 없는 방법을 제안한다.
- 4. FixingGS의 핵심은 보다 정확하고 시점 간 일관된 확산 사전 지식을 제공하는 증류 접근법으로, 효과적인 아티팩트 제거와 인페인팅을 가능하게 한다.
- 5. FixingGS는 기존 최첨단 방법들을 뛰어넘는 시각적 품질과 재구성 성능을 입증하며, 코드가 공개될 예정이다.


---

*Generated on 2025-09-24 16:08:32*