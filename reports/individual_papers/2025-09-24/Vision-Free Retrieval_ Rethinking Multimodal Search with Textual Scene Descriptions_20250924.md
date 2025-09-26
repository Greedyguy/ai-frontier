<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:18:22.416274",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Zero-Shot Learning",
    "Textual Scene Descriptions",
    "Multimodal Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.88,
    "Zero-Shot Learning": 0.85,
    "Textual Scene Descriptions": 0.7,
    "Multimodal Learning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLMs"
        ],
        "category": "evolved_concepts",
        "rationale": "This concept is central to the paper's discussion on multimodal retrieval and links to evolving trends in AI.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.88
      },
      {
        "surface": "Zero-Shot Performance",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "The paper emphasizes achieving state-of-the-art results in zero-shot settings, highlighting its relevance.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Textual Scene Descriptions",
        "canonical": "Textual Scene Descriptions",
        "aliases": [
          "Structured Image Descriptions"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique approach proposed in the paper, offering a novel method for vision-free retrieval.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.7
      },
      {
        "surface": "Multimodal Search",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal Retrieval"
        ],
        "category": "specific_connectable",
        "rationale": "The paper rethinks traditional multimodal approaches, making this a key concept for linking.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.75,
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
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Zero-Shot Performance",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Textual Scene Descriptions",
      "resolved_canonical": "Textual Scene Descriptions",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Multimodal Search",
      "resolved_canonical": "Multimodal Learning",
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

# Vision-Free Retrieval: Rethinking Multimodal Search with Textual Scene Descriptions

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19203.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.19203](https://arxiv.org/abs/2509.19203)

## 🔗 유사한 논문
- [[2025-09-23/CLIP-IN_ Enhancing Fine-Grained Visual Understanding in CLIP via Instruction Editing Data and Long Captions_20250923|CLIP-IN: Enhancing Fine-Grained Visual Understanding in CLIP via Instruction Editing Data and Long Captions]] (87.7% similar)
- [[2025-09-22/LLMs Can Compensate for Deficiencies in Visual Representations_20250922|LLMs Can Compensate for Deficiencies in Visual Representations]] (86.5% similar)
- [[2025-09-23/Can LLMs Reason Over Non-Text Modalities in a Training-Free Manner? A Case Study with In-Context Representation Learning_20250923|Can LLMs Reason Over Non-Text Modalities in a Training-Free Manner? A Case Study with In-Context Representation Learning]] (85.6% similar)
- [[2025-09-24/Reading Images Like Texts_ Sequential Image Understanding in Vision-Language Models_20250924|Reading Images Like Texts: Sequential Image Understanding in Vision-Language Models]] (85.6% similar)
- [[2025-09-22/Exploring the Capabilities of LLM Encoders for Image-Text Retrieval in Chest X-rays_20250922|Exploring the Capabilities of LLM Encoders for Image-Text Retrieval in Chest X-rays]] (85.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]], [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Textual Scene Descriptions|Textual Scene Descriptions]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19203v1 Announce Type: new 
Abstract: Contrastively-trained Vision-Language Models (VLMs), such as CLIP, have become the standard approach for learning discriminative vision-language representations. However, these models often exhibit shallow language understanding, manifesting bag-of-words behaviour. These limitations are reinforced by their dual-encoder design, which induces a modality gap. Additionally, the reliance on vast web-collected data corpora for training makes the process computationally expensive and introduces significant privacy concerns. To address these limitations, in this work, we challenge the necessity of vision encoders for retrieval tasks by introducing a vision-free, single-encoder retrieval pipeline. Departing from the traditional text-to-image retrieval paradigm, we migrate to a text-to-text paradigm with the assistance of VLLM-generated structured image descriptions. We demonstrate that this paradigm shift has significant advantages, including a substantial reduction of the modality gap, improved compositionality, and better performance on short and long caption queries, all attainable with only a few hours of calibration on two GPUs. Additionally, substituting raw images with textual descriptions introduces a more privacy-friendly alternative for retrieval. To further assess generalisation and address some of the shortcomings of prior compositionality benchmarks, we release two benchmarks derived from Flickr30k and COCO, containing diverse compositional queries made of short captions, which we coin subFlickr and subCOCO. Our vision-free retriever matches and often surpasses traditional multimodal models. Importantly, our approach achieves state-of-the-art zero-shot performance on multiple retrieval and compositionality benchmarks, with models as small as 0.3B parameters. Code is available at: https://github.com/IoannaNti/LexiCLIP

## 📝 요약

이 논문은 기존의 시각-언어 모델(VLM)인 CLIP의 한계를 극복하기 위해 새로운 접근 방식을 제안합니다. 기존 모델은 얕은 언어 이해와 모달리티 격차 문제를 가지고 있으며, 대규모 데이터 사용으로 인해 비용과 개인정보 문제가 발생합니다. 이를 해결하기 위해, 이 연구는 시각 인코더 없이 텍스트 기반의 단일 인코더 검색 파이프라인을 도입합니다. VLLM이 생성한 구조화된 이미지 설명을 활용하여 텍스트 간 검색을 수행하며, 이는 모달리티 격차를 줄이고, 조합성을 개선하며, 짧고 긴 캡션 쿼리에서 더 나은 성능을 보여줍니다. 또한, 텍스트 설명으로 이미지 대체는 개인정보 보호 측면에서도 유리합니다. 연구는 새로운 벤치마크인 subFlickr와 subCOCO를 제시하며, 제안된 방법이 기존 다중 모달 모델을 능가하는 성능을 보임을 입증합니다. 이 접근 방식은 여러 검색 및 조합성 벤치마크에서 최첨단 제로샷 성능을 달성합니다.

## 🎯 주요 포인트

- 1. 기존의 시각-언어 모델은 얕은 언어 이해와 모달리티 격차 문제를 가지고 있으며, 이는 이중 인코더 설계로 인해 강화됩니다.
- 2. 본 연구에서는 시각 인코더 없이 텍스트-텍스트 패러다임을 활용하여 모달리티 격차를 줄이고 성능을 향상시키는 새로운 검색 파이프라인을 제안합니다.
- 3. 텍스트 설명을 사용하여 개인 정보 보호를 강화하고, 짧고 긴 캡션 쿼리에서 더 나은 성능을 달성합니다.
- 4. Flickr30k와 COCO에서 파생된 새로운 벤치마크를 통해 일반화 성능을 평가하며, 제안된 모델은 기존 멀티모달 모델을 능가합니다.
- 5. 제안된 접근 방식은 여러 검색 및 조합성 벤치마크에서 최첨단 제로샷 성능을 달성하며, 코드가 공개되어 있습니다.


---

*Generated on 2025-09-24 16:18:22*