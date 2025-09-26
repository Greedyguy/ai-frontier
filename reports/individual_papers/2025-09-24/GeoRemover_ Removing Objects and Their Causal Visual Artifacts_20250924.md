<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:01:31.775754",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Object Removal",
    "Causal Visual Artifacts",
    "Geometry-Aware Framework",
    "Appearance Rendering"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Object Removal": 0.75,
    "Causal Visual Artifacts": 0.7,
    "Geometry-Aware Framework": 0.78,
    "Appearance Rendering": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "object removal",
        "canonical": "Object Removal",
        "aliases": [
          "removing objects"
        ],
        "category": "unique_technical",
        "rationale": "This is a core concept of the paper, focusing on removing objects and their visual artifacts, which is crucial for linking to related image editing techniques.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "causal visual artifacts",
        "canonical": "Causal Visual Artifacts",
        "aliases": [
          "visual artifacts",
          "causal effects"
        ],
        "category": "unique_technical",
        "rationale": "Understanding and removing causal visual artifacts is a unique technical challenge addressed by the paper, relevant for linking to causal inference in visual contexts.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "geometry-aware framework",
        "canonical": "Geometry-Aware Framework",
        "aliases": [
          "geometry-based approach"
        ],
        "category": "unique_technical",
        "rationale": "The geometry-aware framework is a novel approach introduced in the paper, providing a new perspective on object removal that can link to geometric methods in computer vision.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "appearance rendering",
        "canonical": "Appearance Rendering",
        "aliases": [
          "rendering appearance"
        ],
        "category": "unique_technical",
        "rationale": "This process is crucial for the second stage of the proposed framework, linking to rendering techniques in image synthesis.",
        "novelty_score": 0.65,
        "connectivity_score": 0.68,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
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
      "candidate_surface": "object removal",
      "resolved_canonical": "Object Removal",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "causal visual artifacts",
      "resolved_canonical": "Causal Visual Artifacts",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "geometry-aware framework",
      "resolved_canonical": "Geometry-Aware Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "appearance rendering",
      "resolved_canonical": "Appearance Rendering",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.68,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# GeoRemover: Removing Objects and Their Causal Visual Artifacts

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18538.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18538](https://arxiv.org/abs/2509.18538)

## 🔗 유사한 논문
- [[2025-09-23/VCE_ Safe Autoregressive Image Generation via Visual Contrast Exploitation_20250923|VCE: Safe Autoregressive Image Generation via Visual Contrast Exploitation]] (80.9% similar)
- [[2025-09-23/Multi-Agent Amodal Completion_ Direct Synthesis with Fine-Grained Semantic Guidance_20250923|Multi-Agent Amodal Completion: Direct Synthesis with Fine-Grained Semantic Guidance]] (80.1% similar)
- [[2025-09-23/SCORP_ Scene-Consistent Object Refinement via Proxy Generation and Tuning_20250923|SCORP: Scene-Consistent Object Refinement via Proxy Generation and Tuning]] (80.0% similar)
- [[2025-09-19/Seeing 3D Through 2D Lenses_ 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification_20250919|Seeing 3D Through 2D Lenses: 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (79.7% similar)
- [[2025-09-23/Penalizing Boundary Activation for Object Completeness in Diffusion Models_20250923|Penalizing Boundary Activation for Object Completeness in Diffusion Models]] (79.5% similar)

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Object Removal|Object Removal]], [[keywords/Causal Visual Artifacts|Causal Visual Artifacts]], [[keywords/Geometry-Aware Framework|Geometry-Aware Framework]], [[keywords/Appearance Rendering|Appearance Rendering]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18538v1 Announce Type: new 
Abstract: Towards intelligent image editing, object removal should eliminate both the target object and its causal visual artifacts, such as shadows and reflections. However, existing image appearance-based methods either follow strictly mask-aligned training and fail to remove these causal effects which are not explicitly masked, or adopt loosely mask-aligned strategies that lack controllability and may unintentionally over-erase other objects. We identify that these limitations stem from ignoring the causal relationship between an object's geometry presence and its visual effects. To address this limitation, we propose a geometry-aware two-stage framework that decouples object removal into (1) geometry removal and (2) appearance rendering. In the first stage, we remove the object directly from the geometry (e.g., depth) using strictly mask-aligned supervision, enabling structure-aware editing with strong geometric constraints. In the second stage, we render a photorealistic RGB image conditioned on the updated geometry, where causal visual effects are considered implicitly as a result of the modified 3D geometry. To guide learning in the geometry removal stage, we introduce a preference-driven objective based on positive and negative sample pairs, encouraging the model to remove objects as well as their causal visual artifacts while avoiding new structural insertions. Extensive experiments demonstrate that our method achieves state-of-the-art performance in removing both objects and their associated artifacts on two popular benchmarks. The code is available at https://github.com/buxiangzhiren/GeoRemover.

## 📝 요약

이 논문은 지능형 이미지 편집을 위한 객체 제거 방법을 제안합니다. 기존 방법들은 객체의 그림자나 반사와 같은 시각적 인과 효과를 제대로 제거하지 못하거나, 다른 객체를 과도하게 제거하는 문제를 가집니다. 이를 해결하기 위해, 객체 제거를 기하학적 제거와 외관 렌더링의 두 단계로 분리하는 기하학 인식 프레임워크를 제안합니다. 첫 번째 단계에서는 객체의 기하학적 정보를 제거하고, 두 번째 단계에서는 수정된 3D 기하학을 바탕으로 사진과 같은 RGB 이미지를 생성합니다. 이 과정에서 인과적 시각 효과를 암묵적으로 고려합니다. 실험 결과, 제안된 방법은 두 가지 주요 벤치마크에서 객체와 관련 아티팩트 제거에 있어 최첨단 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 기존의 이미지 편집 방법은 객체 제거 시 그림자나 반사와 같은 인과적 시각 효과를 제대로 제거하지 못하는 한계가 있다.
- 2. 본 연구는 객체의 기하학적 존재와 시각적 효과 간의 인과 관계를 고려하지 않는 기존 방법의 한계를 지적한다.
- 3. 제안된 기하학 인식 2단계 프레임워크는 객체 제거를 기하학 제거와 외관 렌더링으로 분리하여 처리한다.
- 4. 첫 번째 단계에서는 엄격한 마스크 정렬 감독을 통해 기하학에서 객체를 직접 제거하여 구조 인식 편집을 가능하게 한다.
- 5. 두 번째 단계에서는 수정된 3D 기하학을 기반으로 인과적 시각 효과를 암묵적으로 고려한 사실적인 RGB 이미지를 렌더링한다.


---

*Generated on 2025-09-24 16:01:31*