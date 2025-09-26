---
keywords:
  - 3D Generative Priors
  - Novel View Synthesis
  - Geometry Completion
  - Scene Reconstruction
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2506.23835
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:26:26.480080",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Generative Priors",
    "Novel View Synthesis",
    "Geometry Completion",
    "Scene Reconstruction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Generative Priors": 0.78,
    "Novel View Synthesis": 0.82,
    "Geometry Completion": 0.8,
    "Scene Reconstruction": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "3D generative priors",
        "canonical": "3D Generative Priors",
        "aliases": [
          "3D generative models",
          "3D priors"
        ],
        "category": "unique_technical",
        "rationale": "This term is crucial for linking to advanced 3D modeling techniques and generative methods in computer vision.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "novel view synthesis",
        "canonical": "Novel View Synthesis",
        "aliases": [
          "view synthesis",
          "new view generation"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is essential for connecting to research on generating new perspectives in 3D environments.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "geometry completion",
        "canonical": "Geometry Completion",
        "aliases": [
          "3D geometry completion",
          "shape completion"
        ],
        "category": "specific_connectable",
        "rationale": "This term links to work on completing missing geometric data in 3D models.",
        "novelty_score": 0.58,
        "connectivity_score": 0.83,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "scene reconstruction",
        "canonical": "Scene Reconstruction",
        "aliases": [
          "3D scene reconstruction",
          "scene modeling"
        ],
        "category": "broad_technical",
        "rationale": "This broad term connects to a wide range of work in reconstructing environments from visual data.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.79
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
      "candidate_surface": "3D generative priors",
      "resolved_canonical": "3D Generative Priors",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "novel view synthesis",
      "resolved_canonical": "Novel View Synthesis",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "geometry completion",
      "resolved_canonical": "Geometry Completion",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.83,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "scene reconstruction",
      "resolved_canonical": "Scene Reconstruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# SCORP: Scene-Consistent Object Refinement via Proxy Generation and Tuning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2506.23835.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2506.23835](https://arxiv.org/abs/2506.23835)

## 🔗 유사한 논문
- [[2025-09-22/SCENEFORGE_ Enhancing 3D-text alignment with Structured Scene Compositions_20250922|SCENEFORGE: Enhancing 3D-text alignment with Structured Scene Compositions]] (83.8% similar)
- [[2025-09-23/MAESTRO_ Task-Relevant Optimization via Adaptive Feature Enhancement and Suppression for Multi-task 3D Perception_20250923|MAESTRO: Task-Relevant Optimization via Adaptive Feature Enhancement and Suppression for Multi-task 3D Perception]] (83.1% similar)
- [[2025-09-23/ProDyG_ Progressive Dynamic Scene Reconstruction via Gaussian Splatting from Monocular Videos_20250923|ProDyG: Progressive Dynamic Scene Reconstruction via Gaussian Splatting from Monocular Videos]] (82.0% similar)
- [[2025-09-23/Emergent 3D Correspondence from Neural Shape Representation_20250923|Emergent 3D Correspondence from Neural Shape Representation]] (81.4% similar)
- [[2025-09-22/SAMPO_Scale-wise Autoregression with Motion PrOmpt for generative world models_20250922|SAMPO:Scale-wise Autoregression with Motion PrOmpt for generative world models]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Scene Reconstruction|Scene Reconstruction]]
**🔗 Specific Connectable**: [[keywords/Novel View Synthesis|Novel View Synthesis]], [[keywords/Geometry Completion|Geometry Completion]]
**⚡ Unique Technical**: [[keywords/3D Generative Priors|3D Generative Priors]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.23835v2 Announce Type: replace 
Abstract: Viewpoint missing of objects is common in scene reconstruction, as camera paths typically prioritize capturing the overall scene structure rather than individual objects. This makes it highly challenging to achieve high-fidelity object-level modeling while maintaining accurate scene-level representation. Addressing this issue is critical for advancing downstream tasks requiring high-fidelity object reconstruction. In this paper, we introduce Scene-Consistent Object Refinement via Proxy Generation and Tuning (SCORP), a novel 3D enhancement framework that leverages 3D generative priors to recover fine-grained object geometry and appearance under missing views. Starting with proxy generation by substituting degraded objects using a 3D generation model, SCORP then progressively refines geometry and texture by aligning each proxy to its degraded counterpart in 7-DoF pose, followed by correcting spatial and appearance inconsistencies through registration-constrained enhancement. This two-stage proxy tuning ensures the high-fidelity geometry and appearance of the original object in unseen views while maintaining consistency in spatial positioning, observed geometry, and appearance. Across challenging benchmarks, SCORP achieves consistent gains over recent state-of-the-art baselines on both novel view synthesis and geometry completion tasks. SCORP is available at https://github.com/PolySummit/SCORP.

## 📝 요약

이 논문은 장면 재구성 시 개별 객체의 시점 누락 문제를 해결하기 위해 SCORP라는 새로운 3D 향상 프레임워크를 제안합니다. SCORP는 3D 생성 모델을 활용하여 손상된 객체를 대체하는 프록시 생성으로 시작하여, 7-DoF 자세 정렬을 통해 기하학과 텍스처를 정교하게 조정합니다. 이후, 등록 제약 기반의 향상을 통해 공간적 및 외관상의 불일치를 수정합니다. 이 두 단계의 프록시 튜닝은 보이지 않는 시점에서도 원래 객체의 고품질 기하학과 외관을 유지하면서 일관성을 보장합니다. SCORP는 새로운 시점 합성과 기하학 완성 작업에서 최신 기법들보다 일관된 성능 향상을 보여주었습니다.

## 🎯 주요 포인트

- 1. SCORP는 3D 생성 프라이어를 활용하여 누락된 뷰에서 객체의 세밀한 기하학과 외관을 복구하는 3D 향상 프레임워크입니다.
- 2. SCORP는 열화된 객체를 3D 생성 모델로 대체하여 프록시를 생성하고, 7-DoF 자세에서 프록시를 정렬하여 기하학과 텍스처를 점진적으로 개선합니다.
- 3. 공간 및 외관 불일치를 등록 제약 강화 기법으로 수정하여 원본 객체의 고충실도 기하학과 외관을 유지합니다.
- 4. SCORP는 새로운 뷰 합성 및 기하학 완성 작업에서 최신 기법 대비 일관된 성능 향상을 달성합니다.


---

*Generated on 2025-09-24 05:26:26*