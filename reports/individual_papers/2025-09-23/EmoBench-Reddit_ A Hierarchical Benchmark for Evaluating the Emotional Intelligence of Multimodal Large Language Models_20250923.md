---
keywords:
  - Multimodal Learning
  - EmoBench-Reddit
  - Vision-Language Model
  - Emotion Understanding
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.11101
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:12:38.431099",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "EmoBench-Reddit",
    "Vision-Language Model",
    "Emotion Understanding"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.88,
    "EmoBench-Reddit": 0.8,
    "Vision-Language Model": 0.82,
    "Emotion Understanding": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal Large Language Models",
        "canonical": "Multimodal Learning",
        "aliases": [
          "MLLMs"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Learning is crucial for linking models that integrate multiple data types, such as text and images.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.88
      },
      {
        "surface": "EmoBench-Reddit",
        "canonical": "EmoBench-Reddit",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "EmoBench-Reddit is a unique benchmark specifically designed for evaluating emotional intelligence in multimodal models.",
        "novelty_score": 0.95,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Vision-Language Tasks",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language Tasks"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are central to understanding tasks that involve both visual and textual data.",
        "novelty_score": 0.4,
        "connectivity_score": 0.78,
        "specificity_score": 0.65,
        "link_intent_score": 0.82
      },
      {
        "surface": "Emotion Understanding",
        "canonical": "Emotion Understanding",
        "aliases": [
          "Emotional Intelligence"
        ],
        "category": "unique_technical",
        "rationale": "Emotion Understanding is a specialized area that evaluates a model's ability to interpret human emotions.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "benchmark",
      "task framework",
      "annotation quality"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal Large Language Models",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "EmoBench-Reddit",
      "resolved_canonical": "EmoBench-Reddit",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Vision-Language Tasks",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.78,
        "specificity": 0.65,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Emotion Understanding",
      "resolved_canonical": "Emotion Understanding",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# EmoBench-Reddit: A Hierarchical Benchmark for Evaluating the Emotional Intelligence of Multimodal Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.11101.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.11101](https://arxiv.org/abs/2509.11101)

## 🔗 유사한 논문
- [[2025-09-23/Benchmarking Contextual and Paralinguistic Reasoning in Speech-LLMs_ A Case Study with In-the-Wild Data_20250923|Benchmarking Contextual and Paralinguistic Reasoning in Speech-LLMs: A Case Study with In-the-Wild Data]] (85.0% similar)
- [[2025-09-23/MOMENTS_ A Comprehensive Multimodal Benchmark for Theory of Mind_20250923|MOMENTS: A Comprehensive Multimodal Benchmark for Theory of Mind]] (83.8% similar)
- [[2025-09-18/Humor in Pixels_ Benchmarking Large Multimodal Models Understanding of Online Comics_20250918|Humor in Pixels: Benchmarking Large Multimodal Models Understanding of Online Comics]] (83.5% similar)
- [[2025-09-22/MEDAL_ A Framework for Benchmarking LLMs as Multilingual Open-Domain Dialogue Evaluators_20250922|MEDAL: A Framework for Benchmarking LLMs as Multilingual Open-Domain Dialogue Evaluators]] (83.5% similar)
- [[2025-09-23/RealBench_ A Chinese Multi-image Understanding Benchmark Close to Real-world Scenarios_20250923|RealBench: A Chinese Multi-image Understanding Benchmark Close to Real-world Scenarios]] (83.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/EmoBench-Reddit|EmoBench-Reddit]], [[keywords/Emotion Understanding|Emotion Understanding]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.11101v2 Announce Type: replace 
Abstract: With the rapid advancement of Multimodal Large Language Models (MLLMs), they have demonstrated exceptional capabilities across a variety of vision-language tasks. However, current evaluation benchmarks predominantly focus on objective visual question answering or captioning, inadequately assessing the models' ability to understand complex and subjective human emotions. To bridge this gap, we introduce EmoBench-Reddit, a novel, hierarchical benchmark for multimodal emotion understanding. The dataset comprises 350 meticulously curated samples from the social media platform Reddit, each containing an image, associated user-provided text, and an emotion category (sad, humor, sarcasm, happy) confirmed by user flairs. We designed a hierarchical task framework that progresses from basic perception to advanced cognition, with each data point featuring six multiple-choice questions and one open-ended question of increasing difficulty. Perception tasks evaluate the model's ability to identify basic visual elements (e.g., colors, objects), while cognition tasks require scene reasoning, intent understanding, and deep empathy integrating textual context. We ensured annotation quality through a combination of AI assistance (Claude 4) and manual verification.

## 📝 요약

이 논문은 멀티모달 대형 언어 모델(MLLMs)의 감정 이해 능력을 평가하기 위해 새로운 벤치마크인 EmoBench-Reddit를 제안합니다. 기존 평가 기준이 주로 객관적인 시각 질문 응답이나 캡셔닝에 치중되어 있어 복잡하고 주관적인 인간 감정을 이해하는 모델의 능력을 충분히 평가하지 못한다는 문제를 해결하고자 합니다. EmoBench-Reddit는 Reddit에서 수집한 350개의 샘플로 구성되며, 각 샘플은 이미지, 사용자 제공 텍스트, 감정 카테고리(슬픔, 유머, 풍자, 행복)를 포함합니다. 계층적 과제 프레임워크는 기본적인 인식에서 고급 인지로 진행되며, 각 데이터 포인트는 난이도가 증가하는 6개의 객관식 질문과 1개의 주관식 질문을 포함합니다. 인식 과제는 기본적인 시각 요소 식별을 평가하고, 인지 과제는 장면 추론, 의도 이해, 텍스트 맥락을 통합한 깊은 공감을 요구합니다. 주석 품질은 AI 보조(Claude 4)와 수동 검증을 통해 보장되었습니다.

## 🎯 주요 포인트

- 1. 멀티모달 대형 언어 모델(MLLMs)은 시각-언어 과제에서 뛰어난 성능을 보이지만, 복잡하고 주관적인 인간 감정을 이해하는 능력을 평가하는 데 한계가 있다.
- 2. EmoBench-Reddit는 멀티모달 감정 이해를 위한 새로운 계층적 벤치마크로, Reddit에서 수집한 350개의 샘플을 포함한다.
- 3. 데이터셋은 이미지, 사용자 제공 텍스트, 감정 카테고리(슬픔, 유머, 풍자, 행복)를 포함하며, 사용자 플레어로 확인된 감정 정보를 제공한다.
- 4. 계층적 과제 프레임워크는 기본적인 지각에서 고급 인지로 진행되며, 각 데이터 포인트는 난이도가 증가하는 여섯 개의 객관식 질문과 하나의 주관식 질문을 포함한다.
- 5. 주석 품질은 AI 지원(Claude 4)과 수작업 검증을 통해 보장된다.


---

*Generated on 2025-09-24 04:12:38*