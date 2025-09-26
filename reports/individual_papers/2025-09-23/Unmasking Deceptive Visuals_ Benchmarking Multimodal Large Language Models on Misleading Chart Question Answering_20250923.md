---
keywords:
  - Multimodal Learning
  - Misleading ChartQA
  - Region-aware Reasoning
  - Misleading Visualizations
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2503.18172
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:51:44.480299",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Misleading ChartQA",
    "Region-aware Reasoning",
    "Misleading Visualizations"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.85,
    "Misleading ChartQA": 0.78,
    "Region-aware Reasoning": 0.77,
    "Misleading Visualizations": 0.75
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
        "rationale": "Multimodal Learning is crucial for linking models that integrate multiple types of data, such as text and visuals.",
        "novelty_score": 0.55,
        "connectivity_score": 0.89,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "Misleading ChartQA benchmark",
        "canonical": "Misleading ChartQA",
        "aliases": [
          "Misleading Chart Question Answering"
        ],
        "category": "unique_technical",
        "rationale": "This benchmark is a unique dataset specifically designed for evaluating models on misleading chart reasoning.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Region-aware reasoning pipeline",
        "canonical": "Region-aware Reasoning",
        "aliases": [
          "Region-aware pipeline"
        ],
        "category": "unique_technical",
        "rationale": "This novel approach enhances model accuracy in interpreting charts, offering a specific technique for linking.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.79,
        "link_intent_score": 0.77
      },
      {
        "surface": "Misleading visualizations",
        "canonical": "Misleading Visualizations",
        "aliases": [
          "Deceptive visuals"
        ],
        "category": "unique_technical",
        "rationale": "Understanding misleading visualizations is essential for linking research on visual data integrity.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "chart types",
      "performance",
      "data-driven communication"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal Large Language Models",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.89,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Misleading ChartQA benchmark",
      "resolved_canonical": "Misleading ChartQA",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Region-aware reasoning pipeline",
      "resolved_canonical": "Region-aware Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.79,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Misleading visualizations",
      "resolved_canonical": "Misleading Visualizations",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Unmasking Deceptive Visuals: Benchmarking Multimodal Large Language Models on Misleading Chart Question Answering

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2503.18172.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2503.18172](https://arxiv.org/abs/2503.18172)

## 🔗 유사한 논문
- [[2025-09-23/ChartHal_ A Fine-grained Framework Evaluating Hallucination of Large Vision Language Models in Chart Understanding_20250923|ChartHal: A Fine-grained Framework Evaluating Hallucination of Large Vision Language Models in Chart Understanding]] (86.8% similar)
- [[2025-09-23/Both Text and Images Leaked! A Systematic Analysis of Data Contamination in Multimodal LLM_20250923|Both Text and Images Leaked! A Systematic Analysis of Data Contamination in Multimodal LLM]] (84.0% similar)
- [[2025-09-22/Perception-R1_ Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward_20250922|Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward]] (82.9% similar)
- [[2025-09-19/RAcQUEt_ Unveiling the Dangers of Overlooked Referential Ambiguity in Visual LLMs_20250919|RAcQUEt: Unveiling the Dangers of Overlooked Referential Ambiguity in Visual LLMs]] (82.7% similar)
- [[2025-09-23/When Big Models Train Small Ones_ Label-Free Model Parity Alignment for Efficient Visual Question Answering using Small VLMs_20250923|When Big Models Train Small Ones: Label-Free Model Parity Alignment for Efficient Visual Question Answering using Small VLMs]] (82.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Misleading ChartQA|Misleading ChartQA]], [[keywords/Region-aware Reasoning|Region-aware Reasoning]], [[keywords/Misleading Visualizations|Misleading Visualizations]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.18172v5 Announce Type: replace-cross 
Abstract: Misleading visualizations, which manipulate chart representations to support specific claims, can distort perception and lead to incorrect conclusions. Despite decades of research, they remain a widespread issue, posing risks to public understanding and raising safety concerns for AI systems involved in data-driven communication. While recent multimodal large language models (MLLMs) show strong chart comprehension abilities, their capacity to detect and interpret misleading charts remains unexplored. We introduce Misleading ChartQA benchmark, a large-scale multimodal dataset designed to evaluate MLLMs on misleading chart reasoning. It contains 3,026 curated examples spanning 21 misleader types and 10 chart types, each with standardized chart code, CSV data, multiple-choice questions, and labeled explanations, validated through iterative MLLM checks and expert human review. We benchmark 24 state-of-the-art MLLMs, analyze their performance across misleader types and chart formats, and propose a novel region-aware reasoning pipeline that enhances model accuracy. Our work lays the foundation for developing MLLMs that are robust, trustworthy, and aligned with the demands of responsible visual communication.

## 📝 요약

이 논문은 오해를 불러일으킬 수 있는 시각화 문제를 해결하기 위해 Misleading ChartQA라는 대규모 멀티모달 데이터셋을 소개합니다. 이 데이터셋은 21가지 오해 유형과 10가지 차트 유형을 포함하며, 3,026개의 예시로 구성되어 있습니다. 연구진은 24개의 최신 멀티모달 대형 언어 모델(MLLMs)을 평가하고, 모델의 정확성을 높이기 위한 새로운 지역 인식 추론 파이프라인을 제안합니다. 이 연구는 신뢰할 수 있는 시각적 커뮤니케이션을 위한 MLLMs 개발의 기초를 마련합니다.

## 🎯 주요 포인트

- 1. 오해를 일으키는 시각화는 특정 주장을 지지하기 위해 차트 표현을 조작하며, 이는 인식을 왜곡하고 잘못된 결론을 초래할 수 있다.
- 2. Misleading ChartQA 벤치마크는 오해를 일으키는 차트에 대한 MLLM의 추론 능력을 평가하기 위해 설계된 대규모 멀티모달 데이터셋이다.
- 3. 이 데이터셋은 21가지 오해 유형과 10가지 차트 유형을 포함하여 총 3,026개의 예시를 제공하며, 표준화된 차트 코드, CSV 데이터, 객관식 질문 및 설명을 포함한다.
- 4. 24개의 최신 MLLM을 벤치마크하고, 오해 유형과 차트 형식에 따른 성능을 분석하며, 모델 정확도를 향상시키는 새로운 지역 인식 추론 파이프라인을 제안한다.
- 5. 본 연구는 신뢰할 수 있고 책임 있는 시각적 커뮤니케이션 요구에 부합하는 MLLM 개발의 기초를 마련한다.


---

*Generated on 2025-09-24 00:51:44*