<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:28:12.541788",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "3D Scene Generation",
    "Identity Embedding",
    "360-Degree Head Synthesis"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diffusion Models": 0.78,
    "3D Scene Generation": 0.75,
    "Identity Embedding": 0.72,
    "360-Degree Head Synthesis": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "diffusion models",
        "canonical": "Diffusion Models",
        "aliases": [
          "diffusion-based models"
        ],
        "category": "broad_technical",
        "rationale": "Diffusion models are a fundamental technique in the paper, linking to broader machine learning contexts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.78
      },
      {
        "surface": "3D scenes",
        "canonical": "3D Scene Generation",
        "aliases": [
          "three-dimensional scenes"
        ],
        "category": "specific_connectable",
        "rationale": "3D scene generation is a key application area for diffusion models, enhancing cross-domain connections.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "identity embedding",
        "canonical": "Identity Embedding",
        "aliases": [
          "identity vector"
        ],
        "category": "unique_technical",
        "rationale": "Identity embedding is a novel approach in the paper, crucial for maintaining subject identity across views.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "360 head synthesis",
        "canonical": "360-Degree Head Synthesis",
        "aliases": [
          "full rotation head synthesis"
        ],
        "category": "unique_technical",
        "rationale": "This technique is a unique contribution of the paper, enabling comprehensive view generation.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "novel viewpoints",
      "significant challenge"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "diffusion models",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "3D scenes",
      "resolved_canonical": "3D Scene Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "identity embedding",
      "resolved_canonical": "Identity Embedding",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "360 head synthesis",
      "resolved_canonical": "360-Degree Head Synthesis",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# SpinMeRound: Consistent Multi-View Identity Generation Using Diffusion Models

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2504.10716.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2504.10716](https://arxiv.org/abs/2504.10716)

## 🔗 유사한 논문
- [[2025-09-23/Stable Video-Driven Portraits_20250923|Stable Video-Driven Portraits]] (84.6% similar)
- [[2025-09-19/Controllable Localized Face Anonymization Via Diffusion Inpainting_20250919|Controllable Localized Face Anonymization Via Diffusion Inpainting]] (84.4% similar)
- [[2025-09-24/Lyra_ Generative 3D Scene Reconstruction via Video Diffusion Model Self-Distillation_20250924|Lyra: Generative 3D Scene Reconstruction via Video Diffusion Model Self-Distillation]] (82.9% similar)
- [[2025-09-22/Kuramoto Orientation Diffusion Models_20250922|Kuramoto Orientation Diffusion Models]] (81.9% similar)
- [[2025-09-23/Beat on Gaze_ Learning Stylized Generation of Gaze and Head Dynamics_20250923|Beat on Gaze: Learning Stylized Generation of Gaze and Head Dynamics]] (81.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Diffusion Models|Diffusion Models]]
**🔗 Specific Connectable**: [[keywords/3D Scene Generation|3D Scene Generation]]
**⚡ Unique Technical**: [[keywords/Identity Embedding|Identity Embedding]], [[keywords/360-Degree Head Synthesis|360-Degree Head Synthesis]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.10716v2 Announce Type: replace 
Abstract: Despite recent progress in diffusion models, generating realistic head portraits from novel viewpoints remains a significant challenge. Most current approaches are constrained to limited angular ranges, predominantly focusing on frontal or near-frontal views. Moreover, although the recent emerging large-scale diffusion models have been proven robust in handling 3D scenes, they underperform on facial data, given their complex structure and the uncanny valley pitfalls. In this paper, we propose SpinMeRound, a diffusion-based approach designed to generate consistent and accurate head portraits from novel viewpoints. By leveraging a number of input views alongside an identity embedding, our method effectively synthesizes diverse viewpoints of a subject whilst robustly maintaining its unique identity features. Through experimentation, we showcase our model's generation capabilities in 360 head synthesis, while beating current state-of-the-art multiview diffusion models.

## 📝 요약

최근 확산 모델의 발전에도 불구하고 새로운 시점에서 현실적인 얼굴 초상화를 생성하는 것은 여전히 어려운 과제입니다. 대부분의 기존 방법은 제한된 각도 범위에 국한되어 있으며, 주로 정면 또는 거의 정면에 초점을 맞추고 있습니다. 본 논문에서는 SpinMeRound라는 확산 기반 접근 방식을 제안하여 새로운 시점에서도 일관되고 정확한 얼굴 초상화를 생성합니다. 여러 입력 뷰와 정체성 임베딩을 활용하여 피사체의 다양한 시점을 합성하면서 고유한 정체성 특징을 견고하게 유지합니다. 실험을 통해 360도 얼굴 합성에서의 생성 능력을 입증하며, 현재 최첨단 다중 뷰 확산 모델들을 능가하는 성과를 보였습니다.

## 🎯 주요 포인트

- 1. 최근 확산 모델의 발전에도 불구하고, 새로운 시점에서 현실적인 얼굴 초상화를 생성하는 것은 여전히 큰 도전 과제입니다.
- 2. 대부분의 현재 접근법은 제한된 각도 범위에 국한되어 있으며, 주로 정면 또는 거의 정면의 뷰에 집중하고 있습니다.
- 3. SpinMeRound라는 새로운 확산 기반 접근법을 제안하여, 새로운 시점에서 일관되고 정확한 얼굴 초상화를 생성합니다.
- 4. 여러 입력 뷰와 정체성 임베딩을 활용하여, 피사체의 다양한 시점을 합성하면서 고유한 정체성 특징을 견고하게 유지합니다.
- 5. 실험을 통해 360도 얼굴 합성에서 모델의 생성 능력을 입증하며, 현재 최첨단 다중 뷰 확산 모델을 능가합니다.


---

*Generated on 2025-09-24 16:28:12*