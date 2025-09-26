<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:50:54.275182",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Critical Questions Generation",
    "Large Language Model",
    "Zero-Shot Learning",
    "Automated Reasoning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Critical Questions Generation": 0.8,
    "Large Language Model": 0.85,
    "Zero-Shot Learning": 0.78,
    "Automated Reasoning": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Critical Questions Generation",
        "canonical": "Critical Questions Generation",
        "aliases": [
          "CQs-Gen"
        ],
        "category": "unique_technical",
        "rationale": "This is the central task of the paper, offering a unique approach to enhancing critical thinking in AI systems.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are crucial for understanding the paper's context and benchmarking efforts.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Zero-Shot Evaluation",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-shot evaluation is a trending method that highlights the paper's innovative evaluation approach.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Automated Reasoning",
        "canonical": "Automated Reasoning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Automated reasoning is a key application area for the techniques discussed in the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "dataset",
      "evaluation methods",
      "human judgments"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Critical Questions Generation",
      "resolved_canonical": "Critical Questions Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Zero-Shot Evaluation",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Automated Reasoning",
      "resolved_canonical": "Automated Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Benchmarking Critical Questions Generation: A Challenging Reasoning Task for Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.11341.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2505.11341](https://arxiv.org/abs/2505.11341)

## 🔗 유사한 논문
- [[2025-09-23/EquiBench_ Benchmarking Large Language Models' Reasoning about Program Semantics via Equivalence Checking_20250923|EquiBench: Benchmarking Large Language Models' Reasoning about Program Semantics via Equivalence Checking]] (85.7% similar)
- [[2025-09-23/Does Reasoning Introduce Bias? A Study of Social Bias Evaluation and Mitigation in LLM Reasoning_20250923|Does Reasoning Introduce Bias? A Study of Social Bias Evaluation and Mitigation in LLM Reasoning]] (85.3% similar)
- [[2025-09-24/CCQA_ Generating Question from Solution Can Improve Inference-Time Reasoning in SLMs_20250924|CCQA: Generating Question from Solution Can Improve Inference-Time Reasoning in SLMs]] (85.1% similar)
- [[2025-09-24/CogniLoad_ A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density_20250924|CogniLoad: A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density]] (84.6% similar)
- [[2025-09-23/ESGenius_ Benchmarking LLMs on Environmental, Social, and Governance (ESG) and Sustainability Knowledge_20250923|ESGenius: Benchmarking LLMs on Environmental, Social, and Governance (ESG) and Sustainability Knowledge]] (84.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]], [[keywords/Automated Reasoning|Automated Reasoning]]
**⚡ Unique Technical**: [[keywords/Critical Questions Generation|Critical Questions Generation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.11341v3 Announce Type: replace 
Abstract: The task of Critical Questions Generation (CQs-Gen) aims to foster critical thinking by enabling systems to generate questions that expose underlying assumptions and challenge the validity of argumentative reasoning structures. Despite growing interest in this area, progress has been hindered by the lack of suitable datasets and automatic evaluation standards. This paper presents a comprehensive approach to support the development and benchmarking of systems for this task. We construct the first large-scale dataset including ~5K manually annotated questions. We also investigate automatic evaluation methods and propose reference-based techniques as the strategy that best correlates with human judgments. Our zero-shot evaluation of 11 LLMs establishes a strong baseline while showcasing the difficulty of the task. Data and code plus a public leaderboard are provided to encourage further research, not only in terms of model performance, but also to explore the practical benefits of CQs-Gen for both automated reasoning and human critical thinking.

## 📝 요약

이 논문은 비판적 사고를 촉진하기 위한 '비판적 질문 생성(CQs-Gen)' 과제에 대한 포괄적인 접근법을 제시합니다. 주요 기여로는 약 5천 개의 수작업으로 주석된 질문을 포함한 대규모 데이터셋의 구축과 자동 평가 방법의 탐구가 있습니다. 특히, 인간의 판단과 가장 잘 상관관계를 보이는 참조 기반 평가 기법을 제안합니다. 11개의 대형 언어 모델(LLM)에 대한 제로샷 평가를 통해 강력한 기준선을 설정하며, 이 과제의 어려움을 강조합니다. 데이터와 코드, 공개 리더보드를 제공하여 모델 성능뿐만 아니라 자동화된 추론과 인간의 비판적 사고에 대한 실질적 이점을 탐구하는 추가 연구를 장려합니다.

## 🎯 주요 포인트

- 1. 비판적 질문 생성(CQs-Gen)은 시스템이 숨겨진 가정을 드러내고 논증 구조의 타당성을 도전하는 질문을 생성하도록 하여 비판적 사고를 촉진하는 것을 목표로 한다.
- 2. 적절한 데이터셋과 자동 평가 기준의 부족으로 인해 이 분야의 발전이 저해되고 있다.
- 3. 본 논문은 약 5천 개의 수작업으로 주석이 달린 질문을 포함한 대규모 데이터셋을 구축하여 CQs-Gen 시스템 개발과 벤치마킹을 지원한다.
- 4. 자동 평가 방법을 조사하고 인간 판단과 가장 잘 상관관계를 보이는 참조 기반 기법을 제안한다.
- 5. 11개의 대형 언어 모델(LLM)에 대한 제로샷 평가를 통해 강력한 기준을 설정하고, 데이터와 코드, 공개 리더보드를 제공하여 추가 연구를 장려한다.


---

*Generated on 2025-09-24 15:50:54*