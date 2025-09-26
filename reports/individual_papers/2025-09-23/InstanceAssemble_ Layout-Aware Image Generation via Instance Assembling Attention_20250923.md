---
keywords:
  - InstanceAssemble
  - Layout-to-Image Generation
  - Diffusion Models
  - Layout Grounding Score
  - Multimodal Learning
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.16691
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:32:24.702832",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "InstanceAssemble",
    "Layout-to-Image Generation",
    "Diffusion Models",
    "Layout Grounding Score",
    "Multimodal Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "InstanceAssemble": 0.88,
    "Layout-to-Image Generation": 0.82,
    "Diffusion Models": 0.78,
    "Layout Grounding Score": 0.75,
    "Multimodal Learning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "InstanceAssemble",
        "canonical": "InstanceAssemble",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "InstanceAssemble is a novel architecture that introduces instance-assembling attention, which is central to the paper's contributions.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "Layout-to-Image",
        "canonical": "Layout-to-Image Generation",
        "aliases": [
          "L2I"
        ],
        "category": "specific_connectable",
        "rationale": "Layout-to-Image generation is a key focus of the paper and connects to broader themes in image synthesis.",
        "novelty_score": 0.7,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "Diffusion models",
        "canonical": "Diffusion Models",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Diffusion models are a fundamental technology in image generation, providing a strong link to existing research in the field.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Layout Grounding Score",
        "canonical": "Layout Grounding Score",
        "aliases": [
          "LGS"
        ],
        "category": "unique_technical",
        "rationale": "Layout Grounding Score is a new evaluation metric introduced in the paper, which is significant for assessing L2I accuracy.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "Multimodal content control",
        "canonical": "Multimodal Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Multimodal content control is crucial for the paper's approach, linking it to the trending area of multimodal learning.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
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
      "candidate_surface": "InstanceAssemble",
      "resolved_canonical": "InstanceAssemble",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Layout-to-Image",
      "resolved_canonical": "Layout-to-Image Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Diffusion models",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Layout Grounding Score",
      "resolved_canonical": "Layout Grounding Score",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Multimodal content control",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# InstanceAssemble: Layout-Aware Image Generation via Instance Assembling Attention

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16691.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.16691](https://arxiv.org/abs/2509.16691)

## 🔗 유사한 논문
- [[2025-09-22/OptiScene_ LLM-driven Indoor Scene Layout Generation via Scaled Human-aligned Data Synthesis and Multi-Stage Preference Optimization_20250922|OptiScene: LLM-driven Indoor Scene Layout Generation via Scaled Human-aligned Data Synthesis and Multi-Stage Preference Optimization]] (83.8% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I: LLMs are Naturally Interleaved Multimodal Creators]] (82.5% similar)
- [[2025-09-19/SPATIALGEN_ Layout-guided 3D Indoor Scene Generation_20250919|SPATIALGEN: Layout-guided 3D Indoor Scene Generation]] (80.9% similar)
- [[2025-09-22/AcT2I_ Evaluating and Improving Action Depiction in Text-to-Image Models_20250922|AcT2I: Evaluating and Improving Action Depiction in Text-to-Image Models]] (80.6% similar)
- [[2025-09-23/LLMs as Layout Designers_ A Spatial Reasoning Perspective_20250923|LLMs as Layout Designers: A Spatial Reasoning Perspective]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Diffusion Models|Diffusion Models]]
**🔗 Specific Connectable**: [[keywords/Layout-to-Image Generation|Layout-to-Image Generation]], [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/InstanceAssemble|InstanceAssemble]], [[keywords/Layout Grounding Score|Layout Grounding Score]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16691v1 Announce Type: new 
Abstract: Diffusion models have demonstrated remarkable capabilities in generating high-quality images. Recent advancements in Layout-to-Image (L2I) generation have leveraged positional conditions and textual descriptions to facilitate precise and controllable image synthesis. Despite overall progress, current L2I methods still exhibit suboptimal performance. Therefore, we propose InstanceAssemble, a novel architecture that incorporates layout conditions via instance-assembling attention, enabling position control with bounding boxes (bbox) and multimodal content control including texts and additional visual content. Our method achieves flexible adaption to existing DiT-based T2I models through light-weighted LoRA modules. Additionally, we propose a Layout-to-Image benchmark, Denselayout, a comprehensive benchmark for layout-to-image generation, containing 5k images with 90k instances in total. We further introduce Layout Grounding Score (LGS), an interpretable evaluation metric to more precisely assess the accuracy of L2I generation. Experiments demonstrate that our InstanceAssemble method achieves state-of-the-art performance under complex layout conditions, while exhibiting strong compatibility with diverse style LoRA modules.

## 📝 요약

이 논문에서는 고품질 이미지 생성을 위한 새로운 접근법인 InstanceAssemble을 제안합니다. 이 방법은 인스턴스 조립 주의 메커니즘을 통해 레이아웃 조건을 통합하여, 경계 상자와 텍스트 및 추가 시각적 콘텐츠를 포함한 다중 모달 콘텐츠 제어를 가능하게 합니다. 또한, 경량의 LoRA 모듈을 통해 기존 DiT 기반 T2I 모델에 유연하게 적용할 수 있습니다. 저자들은 5천 개의 이미지와 9만 개의 인스턴스를 포함하는 Denselayout 벤치마크와 L2I 생성 정확성을 평가할 수 있는 해석 가능한 지표인 Layout Grounding Score(LGS)를 제안합니다. 실험 결과, InstanceAssemble은 복잡한 레이아웃 조건에서도 최첨단 성능을 보이며 다양한 스타일의 LoRA 모듈과의 높은 호환성을 나타냅니다.

## 🎯 주요 포인트

- 1. InstanceAssemble는 인스턴스 조립 주의 메커니즘을 통해 레이아웃 조건을 통합하여 위치 제어를 가능하게 합니다.
- 2. 제안된 방법은 경량화된 LoRA 모듈을 통해 기존 DiT 기반 T2I 모델에 유연하게 적응할 수 있습니다.
- 3. Denselayout는 5천 개의 이미지와 총 9만 개의 인스턴스를 포함하는 포괄적인 레이아웃-이미지 생성 벤치마크입니다.
- 4. Layout Grounding Score (LGS)는 L2I 생성의 정확성을 보다 정밀하게 평가할 수 있는 해석 가능한 평가 지표입니다.
- 5. InstanceAssemble 방법은 복잡한 레이아웃 조건에서도 최첨단 성능을 달성하며 다양한 스타일의 LoRA 모듈과 강력한 호환성을 보입니다.


---

*Generated on 2025-09-24 04:32:24*