---
keywords:
  - Multimodal Learning
  - Long Video Understanding
  - Vision-Language Model
  - Grounding-Based Skills
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2406.19875
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:14:26.216558",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Long Video Understanding",
    "Vision-Language Model",
    "Grounding-Based Skills"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.85,
    "Long Video Understanding": 0.78,
    "Vision-Language Model": 0.82,
    "Grounding-Based Skills": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "multi-modal models",
        "canonical": "Multimodal Learning",
        "aliases": [
          "multi-modal learning",
          "multimodal models"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal learning is crucial for understanding complex video content, linking vision and language processing.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "long video understanding",
        "canonical": "Long Video Understanding",
        "aliases": [
          "long-form video comprehension",
          "extended video analysis"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique challenge in video processing that requires specialized techniques, offering new research opportunities.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "vision-language models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "vision-language systems",
          "VLM"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-language models are at the forefront of integrating visual and textual data, crucial for multimodal tasks.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "grounding-based skills",
        "canonical": "Grounding-Based Skills",
        "aliases": [
          "grounding tasks",
          "scene grounding"
        ],
        "category": "unique_technical",
        "rationale": "These skills are essential for understanding spatial and temporal contexts in videos, linking to cognitive processing.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "benchmark",
      "evaluation",
      "metadata"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "multi-modal models",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "long video understanding",
      "resolved_canonical": "Long Video Understanding",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "vision-language models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "grounding-based skills",
      "resolved_canonical": "Grounding-Based Skills",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# InfiniBench: A Benchmark for Large Multi-Modal Models in Long-Form Movies and TV Shows

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2406.19875.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2406.19875](https://arxiv.org/abs/2406.19875)

## 🔗 유사한 논문
- [[2025-09-23/All-in-one_ Understanding and Generation in Multimodal Reasoning with the MAIA Benchmark_20250923|All-in-one: Understanding and Generation in Multimodal Reasoning with the MAIA Benchmark]] (83.1% similar)
- [[2025-09-17/Dense Video Understanding with Gated Residual Tokenization_20250917|Dense Video Understanding with Gated Residual Tokenization]] (83.0% similar)
- [[2025-09-23/RealBench_ A Chinese Multi-image Understanding Benchmark Close to Real-world Scenarios_20250923|RealBench: A Chinese Multi-image Understanding Benchmark Close to Real-world Scenarios]] (82.1% similar)
- [[2025-09-19/MovieCORE_ COgnitive REasoning in Movies_20250919|MovieCORE: COgnitive REasoning in Movies]] (82.0% similar)
- [[2025-09-23/NUMINA_ A Natural Understanding Benchmark for Multi-dimensional Intelligence and Numerical Reasoning Abilities_20250923|NUMINA: A Natural Understanding Benchmark for Multi-dimensional Intelligence and Numerical Reasoning Abilities]] (81.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Long Video Understanding|Long Video Understanding]], [[keywords/Grounding-Based Skills|Grounding-Based Skills]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2406.19875v4 Announce Type: replace 
Abstract: Understanding long-form videos, such as movies and TV episodes ranging from tens of minutes to two hours, remains a significant challenge for multi-modal models. Existing benchmarks often fail to test the full range of cognitive skills needed to process these temporally rich and narratively complex inputs. Therefore, we introduce InfiniBench, a comprehensive benchmark designed to evaluate the capabilities of models in long video understanding rigorously. InfiniBench offers:(1) Over 1,000 hours of video content, with an average video length of 53 minutes. (2) The largest set of question-answer pairs for long video comprehension, totaling around 87.7 K. (3) Eight diverse skills that span both grounding-based (e.g., scene transitions, character actions) and reasoning-based (e.g., deep context understanding, multi-event linking). (4) Rich annotation formats, including both multiple-choice and open-ended questions. We conducted an in-depth evaluation across both commercial (GPT-4o, Gemini 2.0 Flash) and most recent open-source vision-language models such as Qwen2.5-VL, InternVL3.0). Results reveal that:(1) Models struggle across the board: Even the best model, GPT-4o, achieves only 47.1 % on grounding-based skills, with most models performing near or just above random chance. (2) Strong reliance on world knowledge: Models achieve surprisingly high scores using only metadata (e.g., video titles), highlighting a tendency to rely on pre-trained knowledge rather than actual visual or temporal understanding. (3) Multi-Modal Importance: When provided with full video and subtitle context, however, models show substantial improvements, confirming the critical role of multimodal input in video understanding. InfiniBench is publicly available at https://vision-cair.github.io/Infinibench

## 📝 요약

장편 비디오 이해는 다중 모달 모델에게 여전히 큰 도전 과제입니다. 이를 해결하기 위해 InfiniBench라는 포괄적인 벤치마크를 제안합니다. InfiniBench는 평균 53분 길이의 1,000시간 이상의 비디오 콘텐츠와 약 87,700개의 질문-답변 쌍을 제공합니다. 이 벤치마크는 장면 전환, 캐릭터 행동 등의 기초적 이해와 깊은 문맥 이해, 다중 이벤트 연결 등의 추론 기반 기술을 평가합니다. 평가 결과, 모델들은 전반적으로 어려움을 겪으며, 특히 GPT-4o 모델도 기초적 이해에서 47.1%의 성과만을 보였습니다. 모델들은 사전 학습된 지식에 의존하는 경향이 있으며, 전체 비디오와 자막 맥락이 제공될 때 성능이 크게 향상됩니다. InfiniBench는 공개적으로 이용 가능합니다.

## 🎯 주요 포인트

- 1. InfiniBench는 장시간 비디오 이해를 평가하기 위한 포괄적인 벤치마크로, 평균 53분 길이의 비디오 콘텐츠 1,000시간 이상을 포함합니다.
- 2. 이 벤치마크는 장시간 비디오 이해를 위한 약 87,700개의 질문-답변 쌍을 제공하며, 다양한 인지 기술을 평가합니다.
- 3. InfiniBench는 장면 전환, 캐릭터 행동과 같은 기반 기술과 깊은 맥락 이해, 다중 이벤트 연결과 같은 추론 기술을 포함한 8개의 다양한 기술을 평가합니다.
- 4. 상업적 모델과 최신 오픈 소스 비전-언어 모델을 평가한 결과, 모델들은 전반적으로 어려움을 겪으며, 특히 사전 지식에 의존하는 경향을 보입니다.
- 5. 전체 비디오 및 자막 컨텍스트가 제공될 때 모델의 성능이 크게 향상되며, 멀티모달 입력의 중요성이 확인되었습니다.


---

*Generated on 2025-09-24 05:14:26*