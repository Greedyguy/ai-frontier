---
keywords:
  - Transformer
  - Shifted Position Embedding
  - Attention Mechanism
  - style consistency
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17088
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:45:34.766306",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Shifted Position Embedding",
    "Attention Mechanism",
    "style consistency"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.78,
    "Shifted Position Embedding": 0.81,
    "Attention Mechanism": 0.75,
    "style consistency": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diffusion Transformer",
        "canonical": "Transformer",
        "aliases": [
          "DiT"
        ],
        "category": "broad_technical",
        "rationale": "Diffusion Transformer is a specific application of Transformer models, which are central to many machine learning tasks.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Shifted Position Embedding",
        "canonical": "Shifted Position Embedding",
        "aliases": [
          "ShiftPE"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel technique introduced in the paper, crucial for resolving positional conflicts in the model.",
        "novelty_score": 0.92,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.81
      },
      {
        "surface": "Advanced Attention Sharing",
        "canonical": "Attention Mechanism",
        "aliases": [
          "AAS"
        ],
        "category": "specific_connectable",
        "rationale": "This technique builds on existing attention mechanisms, enhancing their application in diffusion models.",
        "novelty_score": 0.55,
        "connectivity_score": 0.79,
        "specificity_score": 0.72,
        "link_intent_score": 0.75
      },
      {
        "surface": "style consistency",
        "canonical": "style consistency",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Ensuring style consistency is a unique challenge addressed by the paper, relevant for linking to creative workflows.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "training-free",
      "position embeddings",
      "query, key, and value feature extraction"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Diffusion Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Shifted Position Embedding",
      "resolved_canonical": "Shifted Position Embedding",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Advanced Attention Sharing",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.79,
        "specificity": 0.72,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "style consistency",
      "resolved_canonical": "style consistency",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# AlignedGen: Aligning Style Across Generated Images

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17088.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17088](https://arxiv.org/abs/2509.17088)

## 🔗 유사한 논문
- [[2025-09-19/Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation_20250919|Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation]] (84.8% similar)
- [[2025-09-19/TIDE_ Achieving Balanced Subject-Driven Image Generation via Target-Instructed Diffusion Enhancement_20250919|TIDE: Achieving Balanced Subject-Driven Image Generation via Target-Instructed Diffusion Enhancement]] (84.4% similar)
- [[2025-09-22/RespoDiff_ Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation_20250922|RespoDiff: Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation]] (84.2% similar)
- [[2025-09-22/MaskAttn-SDXL_ Controllable Region-Level Text-To-Image Generation_20250922|MaskAttn-SDXL: Controllable Region-Level Text-To-Image Generation]] (83.5% similar)
- [[2025-09-22/Layout Stroke Imitation_ A Layout Guided Handwriting Stroke Generation for Style Imitation with Diffusion Model_20250922|Layout Stroke Imitation: A Layout Guided Handwriting Stroke Generation for Style Imitation with Diffusion Model]] (83.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Shifted Position Embedding|Shifted Position Embedding]], [[keywords/style consistency|style consistency]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17088v1 Announce Type: new 
Abstract: Despite their generative power, diffusion models struggle to maintain style consistency across images conditioned on the same style prompt, hindering their practical deployment in creative workflows. While several training-free methods attempt to solve this, they are constrained to the U-Net architecture, which not only leads to low-quality results and artifacts like object repetition but also renders them incompatible with superior Diffusion Transformer (DiT). To address these issues, we introduce AlignedGen, a novel training-free framework that enhances style consistency across images generated by DiT models. Our work first reveals a critical insight: naive attention sharing fails in DiT due to conflicting positional signals from improper position embeddings. We introduce Shifted Position Embedding (ShiftPE), an effective solution that resolves this conflict by allocating a non-overlapping set of positional indices to each image. Building on this foundation, we develop Advanced Attention Sharing (AAS), a suite of three techniques meticulously designed to fully unleash the potential of attention sharing within the DiT. Furthermore, to broaden the applicability of our method, we present an efficient query, key, and value feature extraction algorithm, enabling our method to seamlessly incorporate external images as style references. Extensive experimental results validate that our method effectively enhances style consistency across generated images while maintaining precise text-to-image alignment.

## 📝 요약

논문은 스타일 프롬프트에 따라 생성된 이미지 간의 스타일 일관성을 유지하는 데 어려움을 겪는 확산 모델의 문제를 해결하기 위해 AlignedGen이라는 새로운 프레임워크를 제안합니다. 기존 방법들은 U-Net 아키텍처에 국한되어 낮은 품질의 결과를 초래했지만, AlignedGen은 Diffusion Transformer(DiT) 모델에서 스타일 일관성을 향상시킵니다. 주요 기여로는 위치 임베딩 문제를 해결하는 Shifted Position Embedding(ShiftPE)과 Advanced Attention Sharing(AAS) 기술이 있습니다. 또한, 외부 이미지를 스타일 참조로 활용할 수 있는 효율적인 특징 추출 알고리즘을 제시합니다. 실험 결과, 제안된 방법이 생성된 이미지의 스타일 일관성을 효과적으로 향상시키면서 텍스트-이미지 정렬을 유지함을 확인했습니다.

## 🎯 주요 포인트

- 1. 확산 모델은 동일한 스타일 프롬프트에 대해 이미지 간 스타일 일관성을 유지하는 데 어려움을 겪습니다.
- 2. AlignedGen은 DiT 모델에서 생성된 이미지의 스타일 일관성을 향상시키는 새로운 훈련 없는 프레임워크입니다.
- 3. Shifted Position Embedding (ShiftPE)은 DiT의 위치 임베딩 문제를 해결하여 주의 공유의 잠재력을 극대화합니다.
- 4. Advanced Attention Sharing (AAS)은 DiT 내에서 주의 공유를 최적화하기 위해 설계된 세 가지 기술로 구성됩니다.
- 5. 제안된 방법은 외부 이미지를 스타일 참조로 통합할 수 있으며, 실험 결과 스타일 일관성을 효과적으로 향상시킵니다.


---

*Generated on 2025-09-24 04:45:34*