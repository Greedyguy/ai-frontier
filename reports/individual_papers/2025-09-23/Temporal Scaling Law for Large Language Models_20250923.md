---
keywords:
  - Large Language Model
  - Temporal Scaling Law
  - Dynamic Hyperbolic-Law
  - Hyperparameter Selection
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2404.17785
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:42:33.920101",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Temporal Scaling Law",
    "Dynamic Hyperbolic-Law",
    "Hyperparameter Selection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.9,
    "Temporal Scaling Law": 0.8,
    "Dynamic Hyperbolic-Law": 0.7,
    "Hyperparameter Selection": 0.75
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
        "rationale": "Central to the paper's discussion, linking to a well-established concept in NLP.",
        "novelty_score": 0.2,
        "connectivity_score": 0.95,
        "specificity_score": 0.6,
        "link_intent_score": 0.9
      },
      {
        "surface": "Temporal Scaling Law",
        "canonical": "Temporal Scaling Law",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Introduces a novel concept for understanding LLM training dynamics.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Dynamic Hyperbolic-Law",
        "canonical": "Dynamic Hyperbolic-Law",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Represents a specific mathematical model proposed in the paper.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Hyperparameter Selection",
        "canonical": "Hyperparameter Selection",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Key application of the proposed scaling law, relevant for model optimization.",
        "novelty_score": 0.4,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "test loss",
      "training steps",
      "pre-training process"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.2,
        "connectivity": 0.95,
        "specificity": 0.6,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Temporal Scaling Law",
      "resolved_canonical": "Temporal Scaling Law",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Dynamic Hyperbolic-Law",
      "resolved_canonical": "Dynamic Hyperbolic-Law",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Hyperparameter Selection",
      "resolved_canonical": "Hyperparameter Selection",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Temporal Scaling Law for Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2404.17785.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2404.17785](https://arxiv.org/abs/2404.17785)

## 🔗 유사한 논문
- [[2025-09-23/Mitigating Strategy-Selection Bias in Reasoning for More Effective Test-Time Scaling_20250923|Mitigating Strategy-Selection Bias in Reasoning for More Effective Test-Time Scaling]] (84.4% similar)
- [[2025-09-23/Bayesian scaling laws for in-context learning_20250923|Bayesian scaling laws for in-context learning]] (82.7% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (82.3% similar)
- [[2025-09-17/Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (82.0% similar)
- [[2025-09-23/seqBench_ A Tunable Benchmark to Quantify Sequential Reasoning Limits of LLMs_20250923|seqBench: A Tunable Benchmark to Quantify Sequential Reasoning Limits of LLMs]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Hyperparameter Selection|Hyperparameter Selection]]
**⚡ Unique Technical**: [[keywords/Temporal Scaling Law|Temporal Scaling Law]], [[keywords/Dynamic Hyperbolic-Law|Dynamic Hyperbolic-Law]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2404.17785v4 Announce Type: replace 
Abstract: Recently, Large Language Models (LLMs) have been widely adopted in a wide range of tasks, leading to increasing attention towards the research on how scaling LLMs affects their performance. Existing works, termed Scaling Laws, have discovered that the final test loss of LLMs scales as power-laws with model size, computational budget, and dataset size. However, the temporal change of the test loss of an LLM throughout its pre-training process remains unexplored, though it is valuable in many aspects, such as selecting better hyperparameters \textit{directly} on the target LLM. In this paper, we propose the novel concept of Temporal Scaling Law, studying how the test loss of an LLM evolves as the training steps scale up. In contrast to modeling the test loss as a whole in a coarse-grained manner, we break it down and dive into the fine-grained test loss of each token position, and further develop a dynamic hyperbolic-law. Afterwards, we derive the much more precise temporal scaling law by studying the temporal patterns of the parameters in the dynamic hyperbolic-law. Results on both in-distribution (ID) and out-of-distribution (OOD) validation datasets demonstrate that our temporal scaling law accurately predicts the test loss of LLMs across training steps. Our temporal scaling law has broad practical applications. First, it enables direct and efficient hyperparameter selection on the target LLM, such as data mixture proportions. Secondly, viewing the LLM pre-training dynamics from the token position granularity provides some insights to enhance the understanding of LLM pre-training.

## 📝 요약

최근 대형 언어 모델(LLM)의 성능 향상에 대한 연구가 활발히 진행되고 있습니다. 기존 연구에서는 모델 크기, 계산 예산, 데이터셋 크기에 따른 최종 테스트 손실이 거듭제곱 법칙에 따라 변화한다고 밝혀졌습니다. 그러나 LLM의 사전 학습 과정에서의 테스트 손실의 시간적 변화는 충분히 탐구되지 않았습니다. 본 논문에서는 새로운 개념인 '시간적 스케일링 법칙'을 제안하여, 학습 단계가 증가함에 따라 테스트 손실이 어떻게 변화하는지를 연구합니다. 우리는 각 토큰 위치의 세밀한 테스트 손실을 분석하고, 이를 기반으로 동적 쌍곡선 법칙을 개발하였습니다. 이를 통해 더 정확한 시간적 스케일링 법칙을 도출하였으며, 이는 다양한 검증 데이터셋에서 LLM의 테스트 손실을 정확히 예측합니다. 이 법칙은 LLM의 하이퍼파라미터 선택을 직접적이고 효율적으로 가능하게 하며, LLM 사전 학습의 이해를 높이는 데 기여할 수 있습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 테스트 손실이 훈련 단계에 따라 어떻게 변화하는지를 연구하는 새로운 개념인 '시간적 스케일링 법칙'을 제안합니다.
- 2. 기존의 전체적인 테스트 손실 모델링 대신, 각 토큰 위치의 세밀한 테스트 손실을 분석하여 동적 쌍곡선 법칙을 개발했습니다.
- 3. 동적 쌍곡선 법칙의 시간적 패턴을 연구하여 더 정밀한 시간적 스케일링 법칙을 도출했습니다.
- 4. 제안된 시간적 스케일링 법칙은 훈련 단계 전반에 걸쳐 LLM의 테스트 손실을 정확하게 예측합니다.
- 5. 시간적 스케일링 법칙은 목표 LLM에서의 직접적이고 효율적인 하이퍼파라미터 선택 및 LLM 사전 훈련의 이해를 향상시키는 데 실질적인 응용 가능성을 제공합니다.


---

*Generated on 2025-09-24 03:42:33*