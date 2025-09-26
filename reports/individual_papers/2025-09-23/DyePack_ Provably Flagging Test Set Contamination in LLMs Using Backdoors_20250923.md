---
keywords:
  - Large Language Model
  - Test Set Contamination
  - Backdoor Attack
  - False Positive Rate
  - Open Benchmark
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2505.23001
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:01:18.255331",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Test Set Contamination",
    "Backdoor Attack",
    "False Positive Rate",
    "Open Benchmark"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Test Set Contamination": 0.78,
    "Backdoor Attack": 0.82,
    "False Positive Rate": 0.77,
    "Open Benchmark": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's focus on test set contamination and evaluation.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Test Set Contamination",
        "canonical": "Test Set Contamination",
        "aliases": [
          "Benchmark Contamination"
        ],
        "category": "unique_technical",
        "rationale": "Test Set Contamination is a unique challenge addressed by the DyePack framework.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Backdoor Attacks",
        "canonical": "Backdoor Attack",
        "aliases": [
          "Backdoor Techniques"
        ],
        "category": "specific_connectable",
        "rationale": "Backdoor Attacks are a key method used in DyePack to identify contaminated models.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "False Positive Rate",
        "canonical": "False Positive Rate",
        "aliases": [
          "FPR"
        ],
        "category": "specific_connectable",
        "rationale": "False Positive Rate is crucial for understanding the accuracy of the DyePack framework.",
        "novelty_score": 0.4,
        "connectivity_score": 0.65,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "Open Benchmarks",
        "canonical": "Open Benchmark",
        "aliases": [
          "Public Benchmarks"
        ],
        "category": "specific_connectable",
        "rationale": "Open Benchmarks are essential for evaluating models and are susceptible to contamination.",
        "novelty_score": 0.5,
        "connectivity_score": 0.68,
        "specificity_score": 0.72,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "framework",
      "model",
      "evaluation"
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
      "candidate_surface": "Test Set Contamination",
      "resolved_canonical": "Test Set Contamination",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Backdoor Attacks",
      "resolved_canonical": "Backdoor Attack",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "False Positive Rate",
      "resolved_canonical": "False Positive Rate",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.65,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Open Benchmarks",
      "resolved_canonical": "Open Benchmark",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.68,
        "specificity": 0.72,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# DyePack: Provably Flagging Test Set Contamination in LLMs Using Backdoors

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.23001.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2505.23001](https://arxiv.org/abs/2505.23001)

## 🔗 유사한 논문
- [[2025-09-23/Rethinking Backdoor Detection Evaluation for Language Models_20250923|Rethinking Backdoor Detection Evaluation for Language Models]] (84.7% similar)
- [[2025-09-22/Backdoor Mitigation via Invertible Pruning Masks_20250922|Backdoor Mitigation via Invertible Pruning Masks]] (84.0% similar)
- [[2025-09-23/Both Text and Images Leaked! A Systematic Analysis of Data Contamination in Multimodal LLM_20250923|Both Text and Images Leaked! A Systematic Analysis of Data Contamination in Multimodal LLM]] (83.9% similar)
- [[2025-09-18/LNE-Blocking_ An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models_20250918|LNE-Blocking: An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models]] (83.9% similar)
- [[2025-09-23/Revisiting Backdoor Attacks on LLMs_ A Stealthy and Practical Poisoning Framework via Harmless Inputs_20250923|Revisiting Backdoor Attacks on LLMs: A Stealthy and Practical Poisoning Framework via Harmless Inputs]] (82.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Backdoor Attack|Backdoor Attack]], [[keywords/False Positive Rate|False Positive Rate]], [[keywords/Open Benchmark|Open Benchmark]]
**⚡ Unique Technical**: [[keywords/Test Set Contamination|Test Set Contamination]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.23001v4 Announce Type: replace 
Abstract: Open benchmarks are essential for evaluating and advancing large language models, offering reproducibility and transparency. However, their accessibility makes them likely targets of test set contamination. In this work, we introduce DyePack, a framework that leverages backdoor attacks to identify models that used benchmark test sets during training, without requiring access to the loss, logits, or any internal details of the model. Like how banks mix dye packs with their money to mark robbers, DyePack mixes backdoor samples with the test data to flag models that trained on it. We propose a principled design incorporating multiple backdoors with stochastic targets, enabling exact false positive rate (FPR) computation when flagging every model. This provably prevents false accusations while providing strong evidence for every detected case of contamination. We evaluate DyePack on five models across three datasets, covering both multiple-choice and open-ended generation tasks. For multiple-choice questions, it successfully detects all contaminated models with guaranteed FPRs as low as 0.000073% on MMLU-Pro and 0.000017% on Big-Bench-Hard using eight backdoors. For open-ended generation tasks, it generalizes well and identifies all contaminated models on Alpaca with a guaranteed false positive rate of just 0.127% using six backdoors.

## 📝 요약

이 논문에서는 대형 언어 모델의 평가를 위한 오픈 벤치마크의 테스트 세트 오염 문제를 해결하기 위해 DyePack이라는 프레임워크를 제안합니다. DyePack은 모델의 내부 정보 없이 백도어 공격을 활용하여 벤치마크 테스트 세트를 학습에 사용한 모델을 식별합니다. 이 방법은 여러 백도어와 확률적 목표를 통합하여 모든 모델에 대한 정확한 오탐률(FPR)을 계산할 수 있게 합니다. 이를 통해 잘못된 비난을 방지하면서도 오염된 사례에 대한 강력한 증거를 제공합니다. DyePack은 다양한 데이터셋과 모델에 대해 평가되었으며, 다중 선택 문제에서는 매우 낮은 오탐률로 모든 오염된 모델을 성공적으로 감지했습니다. 또한, 개방형 생성 작업에서도 높은 일반화 성능을 보였습니다.

## 🎯 주요 포인트

- 1. DyePack은 벤치마크 테스트 세트를 훈련에 사용한 모델을 식별하기 위해 백도어 공격을 활용하는 프레임워크입니다.
- 2. DyePack은 손실, 로짓 또는 모델의 내부 세부 정보에 대한 접근 없이도 작동합니다.
- 3. 여러 백도어와 확률적 목표를 포함한 설계를 통해 정확한 오탐률(FPR) 계산이 가능하며, 이는 잘못된 비난을 방지합니다.
- 4. DyePack은 MMLU-Pro와 Big-Bench-Hard에서 매우 낮은 오탐률로 모든 오염된 모델을 성공적으로 탐지합니다.
- 5. Alpaca에서의 개방형 생성 작업에서도 DyePack은 모든 오염된 모델을 식별하며, 오탐률은 0.127%에 불과합니다.


---

*Generated on 2025-09-24 04:01:18*