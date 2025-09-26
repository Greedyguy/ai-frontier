<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:34:55.751250",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Adaptive Layer Reuse",
    "Attention Mechanism",
    "Vision-Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.8,
    "Adaptive Layer Reuse": 0.78,
    "Attention Mechanism": 0.82,
    "Vision-Language Model": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diffusion Transformers",
        "canonical": "Transformer",
        "aliases": [
          "DiT"
        ],
        "category": "broad_technical",
        "rationale": "Connects to existing Transformer models, enhancing understanding of its application in diffusion processes.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "adaptive layer-reuse",
        "canonical": "Adaptive Layer Reuse",
        "aliases": [
          "layer reuse"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel technique specific to the paper, providing a unique concept for linking.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "spatial-temporal attention",
        "canonical": "Attention Mechanism",
        "aliases": [
          "spatial attention",
          "temporal attention"
        ],
        "category": "specific_connectable",
        "rationale": "Links to the broader concept of attention mechanisms, crucial for understanding model efficiency.",
        "novelty_score": 0.55,
        "connectivity_score": 0.83,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "text-to-video generation",
        "canonical": "Vision-Language Model",
        "aliases": [
          "video generation"
        ],
        "category": "evolved_concepts",
        "rationale": "Represents an evolved concept in multimodal learning, connecting text and video data.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "static caching",
      "generation dynamics"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Diffusion Transformers",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "adaptive layer-reuse",
      "resolved_canonical": "Adaptive Layer Reuse",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "spatial-temporal attention",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.83,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "text-to-video generation",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Foresight: Adaptive Layer Reuse for Accelerated and High-Quality Text-to-Video Generation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.00329.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2506.00329](https://arxiv.org/abs/2506.00329)

## 🔗 유사한 논문
- [[2025-09-17/BWCache_ Accelerating Video Diffusion Transformers through Block-Wise Caching_20250917|BWCache: Accelerating Video Diffusion Transformers through Block-Wise Caching]] (86.7% similar)
- [[2025-09-23/LRQ-DiT_ Log-Rotation Post-Training Quantization of Diffusion Transformers for Image and Video Generation_20250923|LRQ-DiT: Log-Rotation Post-Training Quantization of Diffusion Transformers for Image and Video Generation]] (84.9% similar)
- [[2025-09-23/DiCo_ Revitalizing ConvNets for Scalable and Efficient Diffusion Modeling_20250923|DiCo: Revitalizing ConvNets for Scalable and Efficient Diffusion Modeling]] (84.6% similar)
- [[2025-09-19/WorldForge_ Unlocking Emergent 3D/4D Generation in Video Diffusion Model via Training-Free Guidance_20250919|WorldForge: Unlocking Emergent 3D/4D Generation in Video Diffusion Model via Training-Free Guidance]] (83.4% similar)
- [[2025-09-23/ContextFlow_ Training-Free Video Object Editing via Adaptive Context Enrichment_20250923|ContextFlow: Training-Free Video Object Editing via Adaptive Context Enrichment]] (83.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Adaptive Layer Reuse|Adaptive Layer Reuse]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.00329v2 Announce Type: replace-cross 
Abstract: Diffusion Transformers (DiTs) achieve state-of-the-art results in text-to-image, text-to-video generation, and editing. However, their large model size and the quadratic cost of spatial-temporal attention over multiple denoising steps make video generation computationally expensive. Static caching mitigates this by reusing features across fixed steps but fails to adapt to generation dynamics, leading to suboptimal trade-offs between speed and quality.
  We propose Foresight, an adaptive layer-reuse technique that reduces computational redundancy across denoising steps while preserving baseline performance. Foresight dynamically identifies and reuses DiT block outputs for all layers across steps, adapting to generation parameters such as resolution and denoising schedules to optimize efficiency. Applied to OpenSora, Latte, and CogVideoX, Foresight achieves up to \latencyimprv end-to-end speedup, while maintaining video quality. The source code of Foresight is available at \href{https://github.com/STAR-Laboratory/foresight}{https://github.com/STAR-Laboratory/foresight}.

## 📝 요약

Diffusion Transformers (DiTs)는 텍스트-이미지 및 텍스트-비디오 생성에서 최첨단 성능을 보이지만, 큰 모델 크기와 공간-시간적 주의력의 높은 계산 비용으로 인해 비디오 생성이 비싸다. 이를 해결하기 위해 제안된 Foresight는 적응형 레이어 재사용 기법으로, 디노이징 단계 간의 계산 중복을 줄이면서 성능을 유지한다. Foresight는 DiT 블록 출력을 동적으로 식별하고 재사용하여 해상도와 디노이징 일정에 맞춰 효율성을 최적화한다. OpenSora, Latte, CogVideoX에 적용 시 최대 속도 향상을 이루면서도 비디오 품질을 유지한다. Foresight의 소스 코드는 온라인에서 제공된다.

## 🎯 주요 포인트

- 1. Diffusion Transformers(DiTs)는 텍스트-이미지, 텍스트-비디오 생성 및 편집에서 최첨단 결과를 달성하지만, 큰 모델 크기와 공간-시간 주의의 높은 계산 비용으로 인해 비디오 생성이 비싸다.
- 2. 정적 캐싱은 고정된 단계에서 특징을 재사용하여 계산 비용을 줄이지만, 생성 역학에 적응하지 못해 속도와 품질 간의 최적의 균형을 이루지 못한다.
- 3. Foresight는 적응형 레이어 재사용 기술로, 디노이징 단계 간의 계산 중복을 줄이면서 기본 성능을 유지한다.
- 4. Foresight는 해상도와 디노이징 일정과 같은 생성 매개변수에 적응하여 모든 단계에서 DiT 블록 출력을 동적으로 식별하고 재사용한다.
- 5. OpenSora, Latte, CogVideoX에 적용된 Foresight는 비디오 품질을 유지하면서 최대 \latencyimprv의 종단 간 속도 향상을 달성한다.


---

*Generated on 2025-09-24 14:34:55*