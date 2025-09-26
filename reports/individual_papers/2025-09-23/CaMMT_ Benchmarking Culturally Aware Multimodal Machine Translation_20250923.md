---
keywords:
  - Culturally-Specific Items
  - Vision-Language Model
  - Multimodal Translation
  - Cultural Context
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2505.24456
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:02:01.946582",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Culturally-Specific Items",
    "Vision-Language Model",
    "Multimodal Translation",
    "Cultural Context"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Culturally-Specific Items": 0.78,
    "Vision-Language Model": 0.82,
    "Multimodal Translation": 0.8,
    "Cultural Context": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Culturally-Specific Items",
        "canonical": "Culturally-Specific Items",
        "aliases": [
          "CSIs"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus on cultural nuances in translation, providing a unique aspect for linking.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Vision Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLMs"
        ],
        "category": "evolved_concepts",
        "rationale": "This concept is crucial for understanding the multimodal approach discussed in the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Multimodal Translation",
        "canonical": "Multimodal Translation",
        "aliases": [
          "Multimodal Machine Translation"
        ],
        "category": "specific_connectable",
        "rationale": "The paper introduces a benchmark specifically for this type of translation, making it a key linking point.",
        "novelty_score": 0.68,
        "connectivity_score": 0.79,
        "specificity_score": 0.77,
        "link_intent_score": 0.8
      },
      {
        "surface": "Cultural Context",
        "canonical": "Cultural Context",
        "aliases": [
          "Cultural Nuance"
        ],
        "category": "unique_technical",
        "rationale": "Understanding cultural context is essential for the paper's exploration of translation challenges.",
        "novelty_score": 0.7,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "benchmark",
      "dataset",
      "evaluation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Culturally-Specific Items",
      "resolved_canonical": "Culturally-Specific Items",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Vision Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Multimodal Translation",
      "resolved_canonical": "Multimodal Translation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.79,
        "specificity": 0.77,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Cultural Context",
      "resolved_canonical": "Cultural Context",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# CaMMT: Benchmarking Culturally Aware Multimodal Machine Translation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.24456.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2505.24456](https://arxiv.org/abs/2505.24456)

## 🔗 유사한 논문
- [[2025-09-23/Seeing Culture_ A Benchmark for Visual Reasoning and Grounding_20250923|Seeing Culture: A Benchmark for Visual Reasoning and Grounding]] (85.5% similar)
- [[2025-09-23/MAKIEval_ A Multilingual Automatic WiKidata-based Framework for Cultural Awareness Evaluation for LLMs_20250923|MAKIEval: A Multilingual Automatic WiKidata-based Framework for Cultural Awareness Evaluation for LLMs]] (83.7% similar)
- [[2025-09-22/CultureScope_ A Dimensional Lens for Probing Cultural Understanding in LLMs_20250922|CultureScope: A Dimensional Lens for Probing Cultural Understanding in LLMs]] (83.2% similar)
- [[2025-09-22/WangchanThaiInstruct_ An instruction-following Dataset for Culture-Aware, Multitask, and Multi-domain Evaluation in Thai_20250922|WangchanThaiInstruct: An instruction-following Dataset for Culture-Aware, Multitask, and Multi-domain Evaluation in Thai]] (82.5% similar)
- [[2025-09-23/RealBench_ A Chinese Multi-image Understanding Benchmark Close to Real-world Scenarios_20250923|RealBench: A Chinese Multi-image Understanding Benchmark Close to Real-world Scenarios]] (81.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Translation|Multimodal Translation]]
**⚡ Unique Technical**: [[keywords/Culturally-Specific Items|Culturally-Specific Items]], [[keywords/Cultural Context|Cultural Context]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.24456v2 Announce Type: replace 
Abstract: Translating cultural content poses challenges for machine translation systems due to the differences in conceptualizations between cultures, where language alone may fail to convey sufficient context to capture region-specific meanings. In this work, we investigate whether images can act as cultural context in multimodal translation. We introduce CaMMT, a human-curated benchmark of over 5,800 triples of images along with parallel captions in English and regional languages. Using this dataset, we evaluate five Vision Language Models (VLMs) in text-only and text+image settings. Through automatic and human evaluations, we find that visual context generally improves translation quality, especially in handling Culturally-Specific Items (CSIs), disambiguation, and correct gender marking. By releasing CaMMT, our objective is to support broader efforts to build and evaluate multimodal translation systems that are better aligned with cultural nuance and regional variations.

## 📝 요약

이 연구는 문화적 콘텐츠 번역에서 이미지가 문화적 맥락을 제공할 수 있는지를 조사합니다. 이를 위해 5,800여 개의 이미지와 영어 및 지역 언어 자막으로 구성된 CaMMT 벤치마크를 소개하고, 다섯 가지 비전 언어 모델(VLM)을 텍스트 전용 및 텍스트+이미지 설정에서 평가했습니다. 자동 및 인간 평가 결과, 시각적 맥락이 번역 품질을 향상시키며, 특히 문화적으로 특정한 항목(CSI) 처리, 모호성 해소, 올바른 성별 표시에 효과적임을 발견했습니다. CaMMT의 공개는 문화적 뉘앙스와 지역적 변화를 더 잘 반영하는 다중 모드 번역 시스템 개발을 지원하는 데 목적이 있습니다.

## 🎯 주요 포인트

- 1. 문화적 내용의 번역은 문화 간 개념 차이로 인해 기계 번역 시스템에 도전 과제를 제시합니다.
- 2. 이미지가 다중 모드 번역에서 문화적 맥락으로 작용할 수 있는지를 조사했습니다.
- 3. CaMMT는 5,800개 이상의 이미지와 영어 및 지역 언어로 된 캡션을 포함한 데이터셋입니다.
- 4. 시각적 맥락은 번역 품질을 향상시키며, 특히 문화적으로 특정한 항목(CSIs), 중의성 해소, 성별 표기에서 효과적입니다.
- 5. CaMMT를 공개하여 문화적 뉘앙스와 지역 변화를 잘 반영하는 다중 모드 번역 시스템 개발을 지원하고자 합니다.


---

*Generated on 2025-09-24 04:02:01*