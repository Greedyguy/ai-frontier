---
keywords:
  - Large Language Model
  - Native Language Identification
  - Forensic Linguistics
  - Agentic Decomposition
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.16666
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:16:12.174458",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Native Language Identification",
    "Forensic Linguistics",
    "Agentic Decomposition"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Native Language Identification": 0.8,
    "Forensic Linguistics": 0.78,
    "Agentic Decomposition": 0.82
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
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "This is a foundational technology in NLP and connects with many related concepts.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Native Language Identification",
        "canonical": "Native Language Identification",
        "aliases": [
          "NLI"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's focus, offering a unique angle on language processing.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Forensic Linguistics",
        "canonical": "Forensic Linguistics",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Provides a novel perspective on language analysis techniques.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Agentic Decomposition",
        "canonical": "Agentic Decomposition",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Introduces a novel methodological approach specific to the paper.",
        "novelty_score": 0.8,
        "connectivity_score": 0.55,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "contextual clues",
      "misleading hints"
    ]
  },
  "decisions": [
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
      "candidate_surface": "Native Language Identification",
      "resolved_canonical": "Native Language Identification",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Forensic Linguistics",
      "resolved_canonical": "Forensic Linguistics",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Agentic Decomposition",
      "resolved_canonical": "Agentic Decomposition",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.55,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Robust Native Language Identification through Agentic Decomposition

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16666.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.16666](https://arxiv.org/abs/2509.16666)

## 🔗 유사한 논문
- [[2025-09-23/Evaluating CxG Generalisation in LLMs via Construction-Based NLI Fine Tuning_20250923|Evaluating CxG Generalisation in LLMs via Construction-Based NLI Fine Tuning]] (85.9% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (85.0% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (84.9% similar)
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM: Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (84.6% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (84.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Native Language Identification|Native Language Identification]], [[keywords/Forensic Linguistics|Forensic Linguistics]], [[keywords/Agentic Decomposition|Agentic Decomposition]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16666v1 Announce Type: new 
Abstract: Large language models (LLMs) often achieve high performance in native language identification (NLI) benchmarks by leveraging superficial contextual clues such as names, locations, and cultural stereotypes, rather than the underlying linguistic patterns indicative of native language (L1) influence. To improve robustness, previous work has instructed LLMs to disregard such clues. In this work, we demonstrate that such a strategy is unreliable and model predictions can be easily altered by misleading hints. To address this problem, we introduce an agentic NLI pipeline inspired by forensic linguistics, where specialized agents accumulate and categorize diverse linguistic evidence before an independent final overall assessment. In this final assessment, a goal-aware coordinating agent synthesizes all evidence to make the NLI prediction. On two benchmark datasets, our approach significantly enhances NLI robustness against misleading contextual clues and performance consistency compared to standard prompting methods.

## 📝 요약

이 논문은 대형 언어 모델(LLM)이 표면적인 맥락적 단서에 의존하여 모국어 식별(NLI)에서 높은 성능을 보이지만, 이는 언어적 패턴을 제대로 반영하지 못한다고 지적합니다. 기존 연구에서는 이러한 단서를 무시하도록 LLM을 지시했으나, 이는 신뢰할 수 없고 쉽게 오도될 수 있다는 한계를 가집니다. 이를 해결하기 위해, 이 논문은 법언어학에서 영감을 받은 에이전트 기반 NLI 파이프라인을 제안합니다. 이 파이프라인은 다양한 언어적 증거를 수집하고 분류한 후, 최종적으로 독립적인 에이전트가 이를 종합하여 NLI 예측을 수행합니다. 두 개의 벤치마크 데이터셋에서 이 접근법은 오도되는 맥락적 단서에 대한 NLI의 강건성과 성능 일관성을 크게 향상시켰습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)은 표면적 맥락 단서를 활용하여 높은 성능을 보이지만, 이는 본질적인 언어적 패턴을 반영하지 못합니다.
- 2. 기존 연구에서는 LLMs에게 이러한 단서를 무시하도록 지시했으나, 이는 신뢰할 수 없는 전략임이 드러났습니다.
- 3. 본 연구에서는 법언어학에서 영감을 받은 에이전트 기반 NLI 파이프라인을 도입하여 다양한 언어적 증거를 수집하고 분류합니다.
- 4. 최종 평가에서는 목표 인식 조정 에이전트가 모든 증거를 종합하여 NLI 예측을 수행합니다.
- 5. 제안된 접근법은 두 개의 벤치마크 데이터셋에서 잘못된 맥락 단서에 대한 NLI의 견고성과 성능 일관성을 크게 향상시켰습니다.


---

*Generated on 2025-09-24 03:16:12*