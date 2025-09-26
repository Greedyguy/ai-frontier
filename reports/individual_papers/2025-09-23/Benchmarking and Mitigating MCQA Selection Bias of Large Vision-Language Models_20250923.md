---
keywords:
  - Vision-Language Model
  - Multiple-Choice Question Answering
  - Visual Question Answering
  - Selection Bias
  - Logit-Level Debiasing
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.16805
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:34:42.752650",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Multiple-Choice Question Answering",
    "Visual Question Answering",
    "Selection Bias",
    "Logit-Level Debiasing"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "Multiple-Choice Question Answering": 0.78,
    "Visual Question Answering": 0.77,
    "Selection Bias": 0.8,
    "Logit-Level Debiasing": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "LVLM",
          "Vision-Language Models"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are central to the paper's focus on selection bias in MCQA tasks.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multiple-Choice Question Answering",
        "canonical": "Multiple-Choice Question Answering",
        "aliases": [
          "MCQA"
        ],
        "category": "unique_technical",
        "rationale": "MCQA is a specific task where selection bias is being investigated, making it a unique technical focus.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Visual Question Answering",
        "canonical": "Visual Question Answering",
        "aliases": [
          "VQA"
        ],
        "category": "specific_connectable",
        "rationale": "VQA is a related task that provides context for understanding biases in vision-language models.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "selection bias",
        "canonical": "Selection Bias",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Selection Bias is the core issue being addressed in the paper, crucial for linking related research.",
        "novelty_score": 0.6,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "logit-level debiasing method",
        "canonical": "Logit-Level Debiasing",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The debiasing method is a novel approach proposed in the paper, important for understanding the mitigation strategy.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.75
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
      "candidate_surface": "Large Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Multiple-Choice Question Answering",
      "resolved_canonical": "Multiple-Choice Question Answering",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Visual Question Answering",
      "resolved_canonical": "Visual Question Answering",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "selection bias",
      "resolved_canonical": "Selection Bias",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "logit-level debiasing method",
      "resolved_canonical": "Logit-Level Debiasing",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Benchmarking and Mitigating MCQA Selection Bias of Large Vision-Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16805.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.16805](https://arxiv.org/abs/2509.16805)

## 🔗 유사한 논문
- [[2025-09-17/Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (86.9% similar)
- [[2025-09-23/Evaluating Fairness in Large Vision-Language Models Across Diverse Demographic Attributes and Prompts_20250923|Evaluating Fairness in Large Vision-Language Models Across Diverse Demographic Attributes and Prompts]] (86.0% similar)
- [[2025-09-23/Large Language Models Badly Generalize across Option Length, Problem Types, and Irrelevant Noun Replacements_20250923|Large Language Models Badly Generalize across Option Length, Problem Types, and Irrelevant Noun Replacements]] (85.1% similar)
- [[2025-09-22/Benchmarking Debiasing Methods for LLM-based Parameter Estimates_20250922|Benchmarking Debiasing Methods for LLM-based Parameter Estimates]] (85.0% similar)
- [[2025-09-23/Mitigating Hallucinations in Large Vision-Language Models via Entity-Centric Multimodal Preference Optimization_20250923|Mitigating Hallucinations in Large Vision-Language Models via Entity-Centric Multimodal Preference Optimization]] (85.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Visual Question Answering|Visual Question Answering]]
**⚡ Unique Technical**: [[keywords/Multiple-Choice Question Answering|Multiple-Choice Question Answering]], [[keywords/Selection Bias|Selection Bias]], [[keywords/Logit-Level Debiasing|Logit-Level Debiasing]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16805v1 Announce Type: new 
Abstract: Large Vision-Language Models (LVLMs) have achieved strong performance on vision-language tasks, particularly Visual Question Answering (VQA). While prior work has explored unimodal biases in VQA, the problem of selection bias in Multiple-Choice Question Answering (MCQA), where models may favor specific option tokens (e.g., "A") or positions, remains underexplored. In this paper, we investigate both the presence and nature of selection bias in LVLMs through fine-grained MCQA benchmarks spanning easy, medium, and hard difficulty levels, defined by the semantic similarity of the options. We further propose an inference-time logit-level debiasing method that estimates an ensemble bias vector from general and contextual prompts and applies confidence-adaptive corrections to the model's output. Our method mitigates bias without retraining and is compatible with frozen LVLMs. Extensive experiments across several state-of-the-art models reveal consistent selection biases that intensify with task difficulty, and show that our mitigation approach significantly reduces bias while improving accuracy in challenging settings. This work offers new insights into the limitations of LVLMs in MCQA and presents a practical approach to improve their robustness in fine-grained visual reasoning. Datasets and code are available at: https://github.com/Atabuzzaman/Selection-Bias-of-LVLMs

## 📝 요약

이 논문은 대규모 비전-언어 모델(LVLMs)에서 발생하는 선택 편향 문제를 다룹니다. 특히, 다중 선택 질문 답변(MCQA)에서 특정 선택지나 위치에 대한 편향을 조사합니다. 연구진은 난이도에 따라 세분화된 MCQA 벤치마크를 통해 LVLMs의 선택 편향을 분석하고, 추론 시 로그잇 수준에서 편향을 완화하는 방법을 제안합니다. 이 방법은 모델을 재훈련하지 않고도 편향을 줄이며, 고정된 LVLMs와 호환됩니다. 실험 결과, 난이도가 높아질수록 편향이 심화되며, 제안된 방법이 정확도를 개선하는 데 효과적임을 확인했습니다. 이 연구는 LVLMs의 한계를 밝히고, 세밀한 시각적 추론에서의 강건성을 향상시키는 실용적인 접근법을 제시합니다.

## 🎯 주요 포인트

- 1. 대형 비전-언어 모델(LVLMs)은 비전-언어 과제, 특히 시각적 질문 응답(VQA)에서 강력한 성능을 보였으나, 다중 선택 질문 응답(MCQA)에서의 선택 편향 문제는 충분히 탐구되지 않았다.
- 2. 본 연구는 LVLMs의 선택 편향 존재 여부와 특성을 다양한 난이도의 MCQA 벤치마크를 통해 조사하였다.
- 3. 추론 시 로그잇 수준에서 편향을 제거하는 방법을 제안하여, 일반 및 맥락적 프롬프트로부터 편향 벡터를 추정하고 모델 출력에 적응형 보정을 적용하였다.
- 4. 제안된 방법은 모델을 재훈련하지 않고도 편향을 완화하며, 고정된 LVLMs와 호환된다.
- 5. 여러 최신 모델을 대상으로 한 실험 결과, 과제 난이도가 높아질수록 선택 편향이 심화되며, 제안된 편향 완화 방법이 정확도를 개선하면서 편향을 크게 줄이는 것으로 나타났다.


---

*Generated on 2025-09-24 04:34:42*