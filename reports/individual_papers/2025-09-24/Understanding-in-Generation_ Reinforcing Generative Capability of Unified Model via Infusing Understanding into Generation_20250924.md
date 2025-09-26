<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:04:56.230091",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Understanding-in-Generation",
    "Text-to-Image Generation",
    "Chain-of-Thought",
    "Image Editing"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Understanding-in-Generation": 0.8,
    "Text-to-Image Generation": 0.85,
    "Chain-of-Thought": 0.78,
    "Image Editing": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Understanding-in-Generation",
        "canonical": "Understanding-in-Generation",
        "aliases": [
          "UiG"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel framework introduced in the paper, crucial for linking to new research on generative models.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "text-to-image generation",
        "canonical": "Text-to-Image Generation",
        "aliases": [
          "T2I Generation"
        ],
        "category": "specific_connectable",
        "rationale": "A key application area that connects with both NLP and computer vision fields.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Chain-of-Thought",
        "canonical": "Chain-of-Thought",
        "aliases": [
          "CoT"
        ],
        "category": "specific_connectable",
        "rationale": "A reasoning method that is gaining traction in AI research, relevant for linking reasoning and generative models.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Image Editing",
        "canonical": "Image Editing",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "A fundamental process in the proposed framework, linking to broader image processing techniques.",
        "novelty_score": 0.3,
        "connectivity_score": 0.7,
        "specificity_score": 0.6,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "enhancing",
      "performance",
      "process"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Understanding-in-Generation",
      "resolved_canonical": "Understanding-in-Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "text-to-image generation",
      "resolved_canonical": "Text-to-Image Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Chain-of-Thought",
      "resolved_canonical": "Chain-of-Thought",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Image Editing",
      "resolved_canonical": "Image Editing",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.7,
        "specificity": 0.6,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# Understanding-in-Generation: Reinforcing Generative Capability of Unified Model via Infusing Understanding into Generation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18639.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18639](https://arxiv.org/abs/2509.18639)

## 🔗 유사한 논문
- [[2025-09-18/Uni-cot_ Towards Unified Chain-of-Thought Reasoning Across Text and Vision_20250918|Uni-cot: Towards Unified Chain-of-Thought Reasoning Across Text and Vision]] (86.4% similar)
- [[2025-09-22/AcT2I_ Evaluating and Improving Action Depiction in Text-to-Image Models_20250922|AcT2I: Evaluating and Improving Action Depiction in Text-to-Image Models]] (84.8% similar)
- [[2025-09-19/TIDE_ Achieving Balanced Subject-Driven Image Generation via Target-Instructed Diffusion Enhancement_20250919|TIDE: Achieving Balanced Subject-Driven Image Generation via Target-Instructed Diffusion Enhancement]] (83.6% similar)
- [[2025-09-19/Reconstruction Alignment Improves Unified Multimodal Models_20250919|Reconstruction Alignment Improves Unified Multimodal Models]] (82.9% similar)
- [[2025-09-23/MEF_ A Systematic Evaluation Framework for Text-to-Image Models_20250923|MEF: A Systematic Evaluation Framework for Text-to-Image Models]] (82.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Image Editing|Image Editing]]
**🔗 Specific Connectable**: [[keywords/Text-to-Image Generation|Text-to-Image Generation]], [[keywords/Chain-of-Thought|Chain-of-Thought]]
**⚡ Unique Technical**: [[keywords/Understanding-in-Generation|Understanding-in-Generation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18639v1 Announce Type: new 
Abstract: Recent works have made notable advancements in enhancing unified models for text-to-image generation through the Chain-of-Thought (CoT). However, these reasoning methods separate the processes of understanding and generation, which limits their ability to guide the reasoning of unified models in addressing the deficiencies of their generative capabilities. To this end, we propose a novel reasoning framework for unified models, Understanding-in-Generation (UiG), which harnesses the robust understanding capabilities of unified models to reinforce their performance in image generation. The core insight of our UiG is to integrate generative guidance by the strong understanding capabilities during the reasoning process, thereby mitigating the limitations of generative abilities. To achieve this, we introduce "Image Editing" as a bridge to infuse understanding into the generation process. Initially, we verify the generated image and incorporate the understanding of unified models into the editing instructions. Subsequently, we enhance the generated image step by step, gradually infusing the understanding into the generation process. Our UiG framework demonstrates a significant performance improvement in text-to-image generation over existing text-to-image reasoning methods, e.g., a 3.92% gain on the long prompt setting of the TIIF benchmark. The project code: https://github.com/QC-LY/UiG

## 📝 요약

최근 연구에서는 Chain-of-Thought(CoT)를 통해 텍스트-이미지 생성 통합 모델을 향상시키는 데 주목할 만한 진전을 이루었습니다. 그러나 기존의 추론 방법은 이해와 생성 과정을 분리하여, 생성 능력의 한계를 극복하는 데 어려움을 겪습니다. 이를 해결하기 위해, 우리는 통합 모델의 강력한 이해 능력을 활용하여 이미지 생성 성능을 강화하는 새로운 추론 프레임워크인 Understanding-in-Generation(UiG)을 제안합니다. UiG의 핵심은 이해 능력을 생성 과정에 통합하여 생성 능력의 한계를 극복하는 것입니다. 이를 위해 "이미지 편집"을 도입하여 생성 과정에 이해를 주입합니다. 초기에는 생성된 이미지를 검증하고, 통합 모델의 이해를 편집 지침에 반영합니다. 이후 단계적으로 이미지를 개선하여 이해를 생성 과정에 점진적으로 통합합니다. UiG 프레임워크는 기존 방법에 비해 텍스트-이미지 생성 성능을 크게 향상시켰으며, TIIF 벤치마크의 긴 프롬프트 설정에서 3.92%의 성능 향상을 보였습니다.

## 🎯 주요 포인트

- 1. 최근 연구들은 Chain-of-Thought(CoT)을 통해 텍스트-이미지 생성 통합 모델을 향상시키는 데 주목할 만한 발전을 이루었다.
- 2. 기존의 추론 방법은 이해와 생성 과정을 분리하여 통합 모델의 생성 능력 결함을 해결하는 데 한계가 있다.
- 3. 새로운 추론 프레임워크인 Understanding-in-Generation(UiG)을 제안하여 통합 모델의 강력한 이해 능력을 활용해 이미지 생성 성능을 강화한다.
- 4. UiG의 핵심은 이해 능력을 생성 과정에 통합하여 생성 능력의 한계를 완화하는 것이다.
- 5. UiG 프레임워크는 기존의 텍스트-이미지 추론 방법에 비해 성능이 크게 향상되었으며, TIIF 벤치마크의 긴 프롬프트 설정에서 3.92%의 성능 향상을 보였다.


---

*Generated on 2025-09-24 16:04:56*