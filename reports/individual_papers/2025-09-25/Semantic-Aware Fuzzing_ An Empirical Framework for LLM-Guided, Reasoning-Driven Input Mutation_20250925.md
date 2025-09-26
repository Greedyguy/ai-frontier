---
keywords:
  - Large Language Model
  - Few-Shot Learning
  - Mutation-Based Fuzzing
  - Prompt Engineering
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19533
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:38:12.157699",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Few-Shot Learning",
    "Mutation-Based Fuzzing",
    "Prompt Engineering"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Few-Shot Learning": 0.78,
    "Mutation-Based Fuzzing": 0.8,
    "Prompt Engineering": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "reasoning LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's framework and connect to a wide range of machine learning topics.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Few-Shot Learning",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "few-shot prompts"
        ],
        "category": "specific_connectable",
        "rationale": "Few-Shot Learning is a key technique explored for improving mutation quality, linking to recent trends in machine learning.",
        "novelty_score": 0.58,
        "connectivity_score": 0.79,
        "specificity_score": 0.72,
        "link_intent_score": 0.78
      },
      {
        "surface": "Mutation-Based Fuzzing",
        "canonical": "Mutation-Based Fuzzing",
        "aliases": [
          "fuzzing mutation loop"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique technical process central to the paper's methodology, connecting fuzzing with LLMs.",
        "novelty_score": 0.72,
        "connectivity_score": 0.67,
        "specificity_score": 0.81,
        "link_intent_score": 0.8
      },
      {
        "surface": "Prompt Engineering",
        "canonical": "Prompt Engineering",
        "aliases": [
          "prompt-based learning"
        ],
        "category": "specific_connectable",
        "rationale": "Prompt Engineering is crucial for optimizing LLM performance in the context of fuzzing.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "security vulnerabilities",
      "coverage-guided tools",
      "response latency"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Few-Shot Learning",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.79,
        "specificity": 0.72,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Mutation-Based Fuzzing",
      "resolved_canonical": "Mutation-Based Fuzzing",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.67,
        "specificity": 0.81,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Prompt Engineering",
      "resolved_canonical": "Prompt Engineering",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Semantic-Aware Fuzzing: An Empirical Framework for LLM-Guided, Reasoning-Driven Input Mutation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19533.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19533](https://arxiv.org/abs/2509.19533)

## 🔗 유사한 논문
- [[2025-09-23/Adaptive Distraction_ Probing LLM Contextual Robustness with Automated Tree Search_20250923|Adaptive Distraction: Probing LLM Contextual Robustness with Automated Tree Search]] (84.5% similar)
- [[2025-09-23/Sugar-Coated Poison_ Benign Generation Unlocks LLM Jailbreaking_20250923|Sugar-Coated Poison: Benign Generation Unlocks LLM Jailbreaking]] (84.5% similar)
- [[2025-09-19/A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks_20250919|A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks]] (84.2% similar)
- [[2025-09-23/MIST_ Jailbreaking Black-box Large Language Models via Iterative Semantic Tuning_20250923|MIST: Jailbreaking Black-box Large Language Models via Iterative Semantic Tuning]] (84.1% similar)
- [[2025-09-24/Evaluating Large Language Models for Detecting Antisemitism_20250924|Evaluating Large Language Models for Detecting Antisemitism]] (84.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Few-Shot Learning|Few-Shot Learning]], [[keywords/Prompt Engineering|Prompt Engineering]]
**⚡ Unique Technical**: [[keywords/Mutation-Based Fuzzing|Mutation-Based Fuzzing]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19533v1 Announce Type: cross 
Abstract: Security vulnerabilities in Internet-of-Things devices, mobile platforms, and autonomous systems remain critical. Traditional mutation-based fuzzers -- while effectively explore code paths -- primarily perform byte- or bit-level edits without semantic reasoning. Coverage-guided tools such as AFL++ use dictionaries, grammars, and splicing heuristics to impose shallow structural constraints, leaving deeper protocol logic, inter-field dependencies, and domain-specific semantics unaddressed. Conversely, reasoning-capable large language models (LLMs) can leverage pretraining knowledge to understand input formats, respect complex constraints, and propose targeted mutations, much like an experienced reverse engineer or testing expert. However, lacking ground truth for "correct" mutation reasoning makes supervised fine-tuning impractical, motivating explorations of off-the-shelf LLMs via prompt-based few-shot learning. To bridge this gap, we present an open-source microservices framework that integrates reasoning LLMs with AFL++ on Google's FuzzBench, tackling asynchronous execution and divergent hardware demands (GPU- vs. CPU-intensive) of LLMs and fuzzers. We evaluate four research questions: (R1) How can reasoning LLMs be integrated into the fuzzing mutation loop? (R2) Do few-shot prompts yield higher-quality mutations than zero-shot? (R3) Can prompt engineering with off-the-shelf models improve fuzzing directly? and (R4) Which open-source reasoning LLMs perform best under prompt-only conditions? Experiments with Llama3.3, Deepseek-r1-Distill-Llama-70B, QwQ-32B, and Gemma3 highlight Deepseek as the most promising. Mutation effectiveness depends more on prompt complexity and model choice than shot count. Response latency and throughput bottlenecks remain key obstacles, offering directions for future work.

## 📝 요약

이 논문은 사물인터넷(IoT) 기기, 모바일 플랫폼, 자율 시스템의 보안 취약점을 해결하기 위해 전통적인 퍼징 기법의 한계를 극복하고자 합니다. 기존 퍼저는 주로 바이트나 비트 수준의 편집을 수행하며, 복잡한 프로토콜 논리나 도메인별 의미를 충분히 고려하지 못합니다. 이에 반해, 대형 언어 모델(LLM)은 사전 학습된 지식을 활용하여 입력 형식을 이해하고 복잡한 제약을 준수하며, 목표 지향적인 변이를 제안할 수 있습니다. 그러나 "올바른" 변이에 대한 기준이 없어 지도 학습이 어려운 상황에서, 이 연구는 LLM과 AFL++를 통합한 오픈소스 마이크로서비스 프레임워크를 제안합니다. 이 프레임워크는 비동기 실행과 하드웨어 요구사항을 조율하며, LLM을 퍼징 변이 루프에 통합하는 방법, few-shot 프롬프트의 효과, 프롬프트 엔지니어링의 직접적인 퍼징 개선 가능성, 그리고 최적의 오픈소스 LLM을 평가합니다. 실험 결과, Deepseek 모델이 가장 유망하며, 변이 효과는 프롬프트 복잡성과 모델 선택에 크게 의존합니다. 응답 지연과 처리량 병목이 주요 과제로 남아 있어, 향후 연구 방향을 제시합니다.

## 🎯 주요 포인트

- 1. 전통적인 변이 기반 퍼저는 코드 경로 탐색에 효과적이지만, 의미적 추론 없이 바이트 또는 비트 수준의 편집을 수행합니다.
- 2. 대규모 언어 모델(LLM)은 사전 학습 지식을 활용하여 입력 형식을 이해하고 복잡한 제약을 준수하며 목표 지향적인 변이를 제안할 수 있습니다.
- 3. LLM과 AFL++를 통합한 오픈 소스 마이크로서비스 프레임워크를 제시하여 비동기 실행 및 하드웨어 요구 사항을 해결합니다.
- 4. 실험 결과, Deepseek 모델이 가장 유망하며, 변이 효과는 프롬프트의 복잡성과 모델 선택에 더 의존합니다.
- 5. 응답 지연과 처리량 병목 현상이 주요 장애물로 남아 있으며, 이는 향후 연구 방향을 제시합니다.


---

*Generated on 2025-09-25 15:38:12*