<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:24:39.924458",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Transformer",
    "LongLLaVA",
    "Vision-Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.8,
    "Transformer": 0.85,
    "LongLLaVA": 0.7,
    "Vision-Language Model": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multi-modal Large Language Models",
        "canonical": "Multimodal Learning",
        "aliases": [
          "MLLMs"
        ],
        "category": "specific_connectable",
        "rationale": "Links to ongoing research in integrating multiple data types in AI models.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Transformer blocks",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "A foundational architecture in modern deep learning models.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "LongLLaVA",
        "canonical": "LongLLaVA",
        "aliases": [
          "Long-Context Large Language and Vision Assistant"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel model architecture with specific capabilities in processing large image sets.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "video understanding",
        "canonical": "Vision-Language Model",
        "aliases": [],
        "category": "evolved_concepts",
        "rationale": "Highlights the integration of vision and language for comprehensive media analysis.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "performance degradation",
      "high computational costs"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multi-modal Large Language Models",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Transformer blocks",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "LongLLaVA",
      "resolved_canonical": "LongLLaVA",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "video understanding",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# LongLLaVA: Scaling Multi-modal LLMs to 1000 Images Efficiently via a Hybrid Architecture

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2409.02889.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2409.02889](https://arxiv.org/abs/2409.02889)

## 🔗 유사한 논문
- [[2025-09-19/Unleashing the Potential of Multimodal LLMs for Zero-Shot Spatio-Temporal Video Grounding_20250919|Unleashing the Potential of Multimodal LLMs for Zero-Shot Spatio-Temporal Video Grounding]] (85.9% similar)
- [[2025-09-24/OptMerge_ Unifying Multimodal LLM Capabilities and Modalities via Model Merging_20250924|OptMerge: Unifying Multimodal LLM Capabilities and Modalities via Model Merging]] (85.7% similar)
- [[2025-09-24/LCMF_ Lightweight Cross-Modality Mambaformer for Embodied Robotics VQA_20250924|LCMF: Lightweight Cross-Modality Mambaformer for Embodied Robotics VQA]] (85.7% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I: LLMs are Naturally Interleaved Multimodal Creators]] (85.5% similar)
- [[2025-09-22/MANZANO_ A Simple and Scalable Unified Multimodal Model with a Hybrid Vision Tokenizer_20250922|MANZANO: A Simple and Scalable Unified Multimodal Model with a Hybrid Vision Tokenizer]] (85.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/LongLLaVA|LongLLaVA]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2409.02889v3 Announce Type: replace-cross 
Abstract: Expanding the long-context capabilities of Multi-modal Large Language Models~(MLLMs) is critical for advancing video understanding and high-resolution image analysis. Achieving this requires systematic improvements in model architecture, data construction, and training strategies, particularly to address challenges such as performance degradation with increasing image counts and high computational costs. In this paper, we propose a hybrid architecture that integrates Mamba and Transformer blocks, introduce data construction methods that capture both temporal and spatial dependencies, and employ a progressive training strategy. Our released model, LongLLaVA (\textbf{Long}-Context \textbf{L}arge \textbf{L}anguage \textbf{a}nd \textbf{V}ision \textbf{A}ssistant), demonstrates an effective balance between efficiency and performance. LongLLaVA achieves competitive results across various benchmarks while maintaining high throughput and low memory consumption. Notably, it can process nearly one thousand images on a single A100 80GB GPU, underscoring its potential for a wide range of multi-modal applications.

## 📝 요약

이 논문은 멀티모달 대형 언어 모델(MLLM)의 장기 문맥 처리 능력을 확장하여 비디오 이해와 고해상도 이미지 분석을 개선하는 방법을 제안합니다. 이를 위해 Mamba와 Transformer 블록을 통합한 하이브리드 아키텍처를 설계하고, 시간적 및 공간적 의존성을 포착하는 데이터 구성 방법과 점진적 학습 전략을 도입했습니다. 제안된 모델인 LongLLaVA는 효율성과 성능의 균형을 이루며, 다양한 벤치마크에서 경쟁력 있는 결과를 보여줍니다. 특히, A100 80GB GPU에서 거의 천 장의 이미지를 처리할 수 있어 다양한 멀티모달 응용에 잠재력을 가지고 있습니다.

## 🎯 주요 포인트

- 1. MLLMs의 장기 문맥 처리 능력 확장은 비디오 이해와 고해상도 이미지 분석 발전에 필수적입니다.
- 2. 제안된 하이브리드 아키텍처는 Mamba와 Transformer 블록을 통합하여 성능을 향상시킵니다.
- 3. 데이터 구축 방법은 시간적 및 공간적 의존성을 포착하도록 설계되었습니다.
- 4. LongLLaVA 모델은 높은 처리량과 낮은 메모리 소비를 유지하면서 다양한 벤치마크에서 경쟁력 있는 결과를 달성합니다.
- 5. LongLLaVA는 단일 A100 80GB GPU에서 거의 천 장의 이미지를 처리할 수 있어 다양한 멀티모달 응용 프로그램에 잠재력을 보여줍니다.


---

*Generated on 2025-09-24 14:24:39*