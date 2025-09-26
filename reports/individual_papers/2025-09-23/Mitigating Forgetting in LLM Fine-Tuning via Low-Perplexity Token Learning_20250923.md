---
keywords:
  - Large Language Model
  - Token Perplexity
  - Catastrophic Forgetting
  - Cross-Domain Generalization
  - Fine-Tuning Strategies
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2501.14315
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:47:01.376278",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Token Perplexity",
    "Catastrophic Forgetting",
    "Cross-Domain Generalization",
    "Fine-Tuning Strategies"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Token Perplexity": 0.82,
    "Catastrophic Forgetting": 0.81,
    "Cross-Domain Generalization": 0.78,
    "Fine-Tuning Strategies": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Central to the study, connecting to various aspects of language model fine-tuning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Token Perplexity",
        "canonical": "Token Perplexity",
        "aliases": [
          "Perplexity Reduction"
        ],
        "category": "unique_technical",
        "rationale": "Key concept introduced for mitigating forgetting in fine-tuning.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Catastrophic Forgetting",
        "canonical": "Catastrophic Forgetting",
        "aliases": [
          "Forgetting Mitigation"
        ],
        "category": "specific_connectable",
        "rationale": "Addresses a fundamental issue in model fine-tuning, linking to broader discussions on model stability.",
        "novelty_score": 0.58,
        "connectivity_score": 0.79,
        "specificity_score": 0.82,
        "link_intent_score": 0.81
      },
      {
        "surface": "Cross-Domain Generalization",
        "canonical": "Cross-Domain Generalization",
        "aliases": [
          "Domain Generalization"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the challenge of maintaining performance across different domains, relevant to various ML applications.",
        "novelty_score": 0.6,
        "connectivity_score": 0.77,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Fine-Tuning Strategies",
        "canonical": "Fine-Tuning Strategies",
        "aliases": [
          "Model Fine-Tuning"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's contribution, offering insights into improving model robustness.",
        "novelty_score": 0.55,
        "connectivity_score": 0.83,
        "specificity_score": 0.7,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "model performance",
      "ground truth data"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Model",
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
      "candidate_surface": "Token Perplexity",
      "resolved_canonical": "Token Perplexity",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Catastrophic Forgetting",
      "resolved_canonical": "Catastrophic Forgetting",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.79,
        "specificity": 0.82,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Cross-Domain Generalization",
      "resolved_canonical": "Cross-Domain Generalization",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.77,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Fine-Tuning Strategies",
      "resolved_canonical": "Fine-Tuning Strategies",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.83,
        "specificity": 0.7,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Mitigating Forgetting in LLM Fine-Tuning via Low-Perplexity Token Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2501.14315.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2501.14315](https://arxiv.org/abs/2501.14315)

## 🔗 유사한 논문
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (84.9% similar)
- [[2025-09-23/Large Language Models Badly Generalize across Option Length, Problem Types, and Irrelevant Noun Replacements_20250923|Large Language Models Badly Generalize across Option Length, Problem Types, and Irrelevant Noun Replacements]] (84.6% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (84.6% similar)
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM: Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (84.1% similar)
- [[2025-09-22/IMPQ_ Interaction-Aware Layerwise Mixed Precision Quantization for LLMs_20250922|IMPQ: Interaction-Aware Layerwise Mixed Precision Quantization for LLMs]] (83.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Catastrophic Forgetting|Catastrophic Forgetting]], [[keywords/Cross-Domain Generalization|Cross-Domain Generalization]], [[keywords/Fine-Tuning Strategies|Fine-Tuning Strategies]]
**⚡ Unique Technical**: [[keywords/Token Perplexity|Token Perplexity]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.14315v4 Announce Type: replace 
Abstract: Maintaining consistent model performance across domains is a fundamental challenge in machine learning. While recent work has explored using LLM-generated data for fine-tuning, its impact on cross-domain generalization remains poorly understood. This paper presents a systematic analysis revealing that fine-tuning with LLM-generated data not only improves target task performance but also reduces non-target task degradation compared to fine-tuning with ground truth data. Through analyzing the data sequence in tasks of various domains, we demonstrate that this enhancement of non-target task robustness stems from the reduction of high perplexity tokens found in LLM-generated sequences. Following our findings, we showed that masking high perplexity tokens in ground truth training data achieves similar non-target task performance preservation, comparable to using LLM-generated data. Extensive experiments across different model families and scales, including Gemma 2 IT 2B, Llama 3 8B Instruct, and 3 additional models, agree with our findings. To the best of our knowledge, this is the first work to provide an empirical explanation based on token perplexity reduction to mitigate catastrophic forgetting in LLMs after fine-tuning, offering valuable insights for developing more robust fine-tuning strategies.

## 📝 요약

이 논문은 도메인 간 일관된 모델 성능 유지의 어려움을 다루며, LLM(대규모 언어 모델) 생성 데이터를 활용한 파인튜닝이 교차 도메인 일반화에 미치는 영향을 분석합니다. 연구 결과, LLM 생성 데이터를 사용한 파인튜닝은 목표 작업 성능을 향상시키고, 비목표 작업의 성능 저하를 줄이는 데 효과적임을 밝혔습니다. 이는 LLM 생성 데이터에서 높은 당혹도(perplexity)를 가진 토큰이 줄어들기 때문입니다. 또한, 원본 데이터에서도 높은 당혹도 토큰을 마스킹하면 유사한 비목표 작업 성능을 유지할 수 있음을 보여주었습니다. 다양한 모델과 규모에 걸친 실험은 이러한 결과를 뒷받침하며, 이는 파인튜닝 후 LLM에서의 치명적 망각을 완화하는 데 중요한 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. LLM 생성 데이터로 미세 조정 시, 목표 작업 성능 향상과 비목표 작업 성능 저하 감소를 동시에 달성할 수 있다.
- 2. 다양한 도메인에서 데이터 시퀀스를 분석한 결과, LLM 생성 데이터는 높은 당혹도 토큰을 줄여 비목표 작업의 견고성을 향상시킨다.
- 3. 높은 당혹도 토큰을 마스킹한 실제 데이터로도 LLM 생성 데이터와 유사한 비목표 작업 성능 보존 효과를 얻을 수 있다.
- 4. Gemma 2 IT 2B, Llama 3 8B Instruct 등 다양한 모델에서 실험한 결과, 당혹도 토큰 감소가 미세 조정 후의 망각 문제를 완화할 수 있음을 확인했다.
- 5. 본 연구는 LLM의 미세 조정 후 망각 문제를 해결하기 위한 토큰 당혹도 감소 기반의 경험적 설명을 최초로 제공한다.


---

*Generated on 2025-09-24 03:47:01*