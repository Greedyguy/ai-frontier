<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:27:28.277844",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "EventVL",
    "Multimodal Learning",
    "Vision-Language Model",
    "Dynamic Semantic Alignment"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "EventVL": 0.8,
    "Multimodal Learning": 0.78,
    "Vision-Language Model": 0.82,
    "Dynamic Semantic Alignment": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "EventVL",
        "canonical": "EventVL",
        "aliases": [
          "Event Vision-Language Model"
        ],
        "category": "unique_technical",
        "rationale": "EventVL is a novel framework specifically designed for event-based multimodal understanding, making it a unique technical concept.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multimodal Large Language Model",
        "canonical": "Multimodal Learning",
        "aliases": [
          "MLLM"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Large Language Models are increasingly relevant for linking vision and language tasks, enhancing connectivity in multimodal research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Vision-Language Model",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLM"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are a key concept in combining visual and textual data, facilitating cross-modal research.",
        "novelty_score": 0.6,
        "connectivity_score": 0.88,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "Dynamic Semantic Alignment",
        "canonical": "Dynamic Semantic Alignment",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This concept is crucial for improving semantic spaces in event streams, providing a unique approach to semantic alignment.",
        "novelty_score": 0.78,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "event-based",
      "scene description",
      "semantic understanding"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "EventVL",
      "resolved_canonical": "EventVL",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multimodal Large Language Model",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Vision-Language Model",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.88,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Dynamic Semantic Alignment",
      "resolved_canonical": "Dynamic Semantic Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# EventVL: Understand Event Streams via Multimodal Large Language Model

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2501.13707.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2501.13707](https://arxiv.org/abs/2501.13707)

## 🔗 유사한 논문
- [[2025-09-19/UnifiedVisual_ A Framework for Constructing Unified Vision-Language Datasets_20250919|UnifiedVisual: A Framework for Constructing Unified Vision-Language Datasets]] (85.5% similar)
- [[2025-09-19/V-SEAM_ Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models_20250919|V-SEAM: Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models]] (83.7% similar)
- [[2025-09-23/CLIP-IN_ Enhancing Fine-Grained Visual Understanding in CLIP via Instruction Editing Data and Long Captions_20250923|CLIP-IN: Enhancing Fine-Grained Visual Understanding in CLIP via Instruction Editing Data and Long Captions]] (83.6% similar)
- [[2025-09-22/LLMs Can Compensate for Deficiencies in Visual Representations_20250922|LLMs Can Compensate for Deficiencies in Visual Representations]] (83.0% similar)
- [[2025-09-23/Open Vision Reasoner_ Transferring Linguistic Cognitive Behavior for Visual Reasoning_20250923|Open Vision Reasoner: Transferring Linguistic Cognitive Behavior for Visual Reasoning]] (82.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/EventVL|EventVL]], [[keywords/Dynamic Semantic Alignment|Dynamic Semantic Alignment]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.13707v2 Announce Type: replace-cross 
Abstract: The event-based Vision-Language Model (VLM) recently has made good progress for practical vision tasks. However, most of these works just utilize CLIP for focusing on traditional perception tasks, which obstruct model understanding explicitly the sufficient semantics and context from event streams. To address the deficiency, we propose EventVL, the first generative event-based MLLM (Multimodal Large Language Model) framework for explicit semantic understanding. Specifically, to bridge the data gap for connecting different modalities semantics, we first annotate a large event-image/video-text dataset, containing almost 1.4 million high-quality pairs of data, which enables effective learning across various scenes, e.g., drive scene or human motion. After that, we design Event Spatiotemporal Representation to fully explore the comprehensive information by diversely aggregating and segmenting the event stream. To further promote a compact semantic space, Dynamic Semantic Alignment is introduced to improve and complete sparse semantic spaces of events. Extensive experiments show that our EventVL can significantly surpass existing MLLM baselines in event captioning and scene description generation tasks. We hope our research could contribute to the development of the event vision community.

## 📝 요약

EventVL은 최초의 생성적 이벤트 기반 다중모달 대형 언어 모델(Multimodal Large Language Model)로, 명시적 의미 이해를 목표로 합니다. 기존의 이벤트 스트림에서 충분한 의미와 맥락을 이해하는 데 한계가 있는 CLIP 기반 모델의 단점을 극복하기 위해, 약 140만 개의 고품질 데이터 쌍을 포함한 대규모 이벤트-이미지/비디오-텍스트 데이터셋을 주석 처리했습니다. 또한, 다양한 이벤트 스트림을 집계하고 분할하여 포괄적인 정보를 탐색하는 이벤트 시공간 표현을 설계했습니다. 더불어, 동적 의미 정렬을 통해 희소한 의미 공간을 개선하고 완성했습니다. 실험 결과, EventVL은 이벤트 캡션 생성 및 장면 설명 생성 작업에서 기존 모델을 뛰어넘는 성능을 보여주었습니다. 이 연구는 이벤트 비전 커뮤니티의 발전에 기여할 것으로 기대됩니다.

## 🎯 주요 포인트

- 1. EventVL은 최초의 생성적 이벤트 기반 다중모달 대형 언어 모델(Multimodal Large Language Model) 프레임워크로, 명시적 의미 이해를 목표로 한다.
- 2. 다양한 장면에서 효과적인 학습을 가능하게 하기 위해 약 140만 개의 고품질 데이터 쌍을 포함한 대규모 이벤트-이미지/비디오-텍스트 데이터셋을 주석 처리하였다.
- 3. 이벤트 스트림의 포괄적인 정보를 탐색하기 위해 이벤트 시공간 표현(Event Spatiotemporal Representation)을 설계하였다.
- 4. 희소한 의미 공간을 개선하고 완성하기 위해 동적 의미 정렬(Dynamic Semantic Alignment)을 도입하였다.
- 5. EventVL은 이벤트 캡션 생성 및 장면 설명 생성 작업에서 기존의 다중모달 대형 언어 모델(Multimodal Large Language Model) 기준을 크게 능가하였다.


---

*Generated on 2025-09-24 14:27:28*