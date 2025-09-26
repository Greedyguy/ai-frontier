---
keywords:
  - Personalized Question Answering
  - Large Language Model
  - LaMP-QA Benchmark
  - Personalized Context
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2506.00137
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:04:39.240939",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Personalized Question Answering",
    "Large Language Model",
    "LaMP-QA Benchmark",
    "Personalized Context"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Personalized Question Answering": 0.78,
    "Large Language Model": 0.82,
    "LaMP-QA Benchmark": 0.85,
    "Personalized Context": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "personalized question answering",
        "canonical": "Personalized Question Answering",
        "aliases": [
          "personalized QA"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's contribution and represents a niche area in question answering systems.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "large language models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large language models are a foundational technology for the paper's methodology and evaluation.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "LaMP-QA benchmark",
        "canonical": "LaMP-QA Benchmark",
        "aliases": [
          "LaMP-QA"
        ],
        "category": "unique_technical",
        "rationale": "The benchmark is a novel contribution of the paper, essential for evaluating personalized long-form answer generation.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "personalized context",
        "canonical": "Personalized Context",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Personalized context is a key factor in the performance improvement reported in the paper.",
        "novelty_score": 0.7,
        "connectivity_score": 0.55,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "answer generation",
      "evaluation strategies",
      "performance improvements",
      "human preferences"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "personalized question answering",
      "resolved_canonical": "Personalized Question Answering",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "large language models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "LaMP-QA benchmark",
      "resolved_canonical": "LaMP-QA Benchmark",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "personalized context",
      "resolved_canonical": "Personalized Context",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.55,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# LaMP-QA: A Benchmark for Personalized Long-form Question Answering

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2506.00137.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2506.00137](https://arxiv.org/abs/2506.00137)

## 🔗 유사한 논문
- [[2025-09-23/Benchmarking Contextual and Paralinguistic Reasoning in Speech-LLMs_ A Case Study with In-the-Wild Data_20250923|Benchmarking Contextual and Paralinguistic Reasoning in Speech-LLMs: A Case Study with In-the-Wild Data]] (84.2% similar)
- [[2025-09-19/SWE-QA_ Can Language Models Answer Repository-level Code Questions?_20250919|SWE-QA: Can Language Models Answer Repository-level Code Questions?]] (82.6% similar)
- [[2025-09-23/Beyond Prompting_ An Efficient Embedding Framework for Open-Domain Question Answering_20250923|Beyond Prompting: An Efficient Embedding Framework for Open-Domain Question Answering]] (81.4% similar)
- [[2025-09-22/MEDAL_ A Framework for Benchmarking LLMs as Multilingual Open-Domain Dialogue Evaluators_20250922|MEDAL: A Framework for Benchmarking LLMs as Multilingual Open-Domain Dialogue Evaluators]] (81.3% similar)
- [[2025-09-19/A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation_20250919|A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Personalized Question Answering|Personalized Question Answering]], [[keywords/LaMP-QA Benchmark|LaMP-QA Benchmark]], [[keywords/Personalized Context|Personalized Context]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.00137v2 Announce Type: replace-cross 
Abstract: Personalization is essential for question answering systems that are user-centric. Despite its importance, personalization in answer generation has been relatively underexplored. This is mainly due to lack of resources for training and evaluating personalized question answering systems. We address this gap by introducing LaMP-QA -- a benchmark designed for evaluating personalized long-form answer generation. The benchmark covers questions from three major categories: (1) Arts & Entertainment, (2) Lifestyle & Personal Development, and (3) Society & Culture, encompassing over 45 subcategories in total. To assess the quality and potential impact of the LaMP-QA benchmark for personalized question answering, we conduct comprehensive human and automatic evaluations, to compare multiple evaluation strategies for evaluating generated personalized responses and measure their alignment with human preferences. Furthermore, we benchmark a number of non-personalized and personalized approaches based on open-source and proprietary large language models. Our results show that incorporating the personalized context provided leads to up to 39% performance improvements. The benchmark is publicly released to support future research in this area.

## 📝 요약

이 논문은 사용자 중심의 질문 응답 시스템에서 개인화의 중요성을 강조하며, 개인화된 답변 생성 연구의 부족을 지적합니다. 이를 해결하기 위해 LaMP-QA라는 벤치마크를 소개하며, 이는 예술 및 엔터테인먼트, 라이프스타일 및 개인 개발, 사회 및 문화의 세 가지 주요 카테고리와 45개 이상의 하위 카테고리를 포함합니다. 연구는 인간과 자동 평가를 통해 개인화된 답변의 질과 영향력을 비교하고, 인간 선호도와의 일치를 측정합니다. 또한, 오픈 소스 및 독점 대형 언어 모델을 기반으로 한 다양한 접근 방식을 벤치마킹하여 개인화된 문맥을 통합했을 때 최대 39%의 성능 향상이 있음을 보여줍니다. 이 벤치마크는 향후 연구를 지원하기 위해 공개되었습니다.

## 🎯 주요 포인트

- 1. LaMP-QA는 개인화된 장문 답변 생성을 평가하기 위한 벤치마크로, 예술 및 엔터테인먼트, 라이프스타일 및 개인 개발, 사회 및 문화의 세 가지 주요 카테고리의 질문을 포함합니다.
- 2. LaMP-QA 벤치마크의 품질과 잠재적 영향을 평가하기 위해 인간 및 자동 평가를 통해 여러 평가 전략을 비교하고 인간 선호도와의 일치를 측정했습니다.
- 3. 개인화된 맥락을 포함하면 성능이 최대 39% 향상된다는 결과를 얻었습니다.
- 4. LaMP-QA 벤치마크는 이 분야의 향후 연구를 지원하기 위해 공개되었습니다.


---

*Generated on 2025-09-24 03:04:39*