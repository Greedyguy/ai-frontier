---
keywords:
  - Multimodal Learning
  - Machine Unlearning
  - Prompt Decouple Loss
  - Safe Answer Refusal Rate
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2502.12520
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:17:07.230138",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Machine Unlearning",
    "Prompt Decouple Loss",
    "Safe Answer Refusal Rate"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.82,
    "Machine Unlearning": 0.79,
    "Prompt Decouple Loss": 0.77,
    "Safe Answer Refusal Rate": 0.75
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
        "rationale": "Multimodal Learning connects language and vision models, crucial for understanding the paper's focus on safety in these models.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Machine Unlearning",
        "canonical": "Machine Unlearning",
        "aliases": [
          "MU"
        ],
        "category": "unique_technical",
        "rationale": "Machine Unlearning is a central theme of the paper, focusing on forgetting specific knowledge, which is a unique technical concept.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.81,
        "link_intent_score": 0.79
      },
      {
        "surface": "Prompt Decouple Loss",
        "canonical": "Prompt Decouple Loss",
        "aliases": [
          "PD Loss"
        ],
        "category": "unique_technical",
        "rationale": "Prompt Decouple Loss is a novel method introduced to mitigate over-forgetting, making it a unique technical contribution.",
        "novelty_score": 0.78,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Safe Answer Refusal Rate",
        "canonical": "Safe Answer Refusal Rate",
        "aliases": [
          "SARR"
        ],
        "category": "unique_technical",
        "rationale": "Safe Answer Refusal Rate is a new metric proposed in the paper, crucial for evaluating the effectiveness of the proposed methods.",
        "novelty_score": 0.75,
        "connectivity_score": 0.58,
        "specificity_score": 0.83,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "forget quality",
      "model utility",
      "over-forgetting"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal Large Language Models",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Machine Unlearning",
      "resolved_canonical": "Machine Unlearning",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.81,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Prompt Decouple Loss",
      "resolved_canonical": "Prompt Decouple Loss",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Safe Answer Refusal Rate",
      "resolved_canonical": "Safe Answer Refusal Rate",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.58,
        "specificity": 0.83,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# SafeEraser: Enhancing Safety in Multimodal Large Language Models through Multimodal Machine Unlearning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2502.12520.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2502.12520](https://arxiv.org/abs/2502.12520)

## 🔗 유사한 논문
- [[2025-09-23/SUA_ Stealthy Multimodal Large Language Model Unlearning Attack_20250923|SUA: Stealthy Multimodal Large Language Model Unlearning Attack]] (88.5% similar)
- [[2025-09-18/Reveal and Release_ Iterative LLM Unlearning with Self-generated Data_20250918|Reveal and Release: Iterative LLM Unlearning with Self-generated Data]] (86.7% similar)
- [[2025-09-22/Sparse-Autoencoder-Guided Internal Representation Unlearning for Large Language Models_20250922|Sparse-Autoencoder-Guided Internal Representation Unlearning for Large Language Models]] (86.3% similar)
- [[2025-09-22/Are Vision-Language Models Safe in the Wild? A Meme-Based Benchmark Study_20250922|Are Vision-Language Models Safe in the Wild? A Meme-Based Benchmark Study]] (85.7% similar)
- [[2025-09-17/Scrub It Out! Erasing Sensitive Memorization in Code Language Models via Machine Unlearning_20250917|Scrub It Out! Erasing Sensitive Memorization in Code Language Models via Machine Unlearning]] (85.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Machine Unlearning|Machine Unlearning]], [[keywords/Prompt Decouple Loss|Prompt Decouple Loss]], [[keywords/Safe Answer Refusal Rate|Safe Answer Refusal Rate]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.12520v3 Announce Type: replace 
Abstract: As Multimodal Large Language Models (MLLMs) develop, their potential security issues have become increasingly prominent. Machine Unlearning (MU), as an effective strategy for forgetting specific knowledge in training data, has been widely used in privacy protection. However, MU for safety in MLLM has yet to be fully explored. To address this issue, we propose SAFEERASER, a safety unlearning benchmark for MLLMs, consisting of 3,000 images and 28.8K VQA pairs. We comprehensively evaluate unlearning methods from two perspectives: forget quality and model utility. Our findings show that existing MU methods struggle to maintain model performance while implementing the forget operation and often suffer from over-forgetting. Hence, we introduce Prompt Decouple (PD) Loss to alleviate over-forgetting through decouple prompt during unlearning process. To quantitatively measure over-forgetting mitigated by PD Loss, we propose a new metric called Safe Answer Refusal Rate (SARR). Experimental results demonstrate that combining PD Loss with existing unlearning methods can effectively prevent over-forgetting and achieve a decrease of 79.5% in the SARR metric of LLaVA-7B and LLaVA-13B, while maintaining forget quality and model utility. Our code and dataset will be released upon acceptance. Warning: This paper contains examples of harmful language and images, and reader discretion is recommended.

## 📝 요약

이 논문은 다중 모달 대형 언어 모델(MLLM)의 안전성 문제를 해결하기 위해 SAFEERASER라는 안전한 학습 제거 벤치마크를 제안합니다. SAFEERASER는 3,000개의 이미지와 28,800개의 VQA 쌍으로 구성되어 있으며, 학습 제거 방법을 망각 품질과 모델 유용성 측면에서 평가합니다. 기존의 학습 제거 방법은 모델 성능을 유지하면서 망각 작업을 수행하는 데 어려움을 겪고, 과도한 망각 문제가 발생합니다. 이를 해결하기 위해 Prompt Decouple (PD) Loss를 도입하여 망각 과정에서 과도한 망각을 완화합니다. Safe Answer Refusal Rate (SARR)라는 새로운 지표를 제안하여 PD Loss가 과도한 망각을 얼마나 완화하는지 측정합니다. 실험 결과, PD Loss를 기존 방법과 결합하면 과도한 망각을 효과적으로 방지하고, LLaVA-7B와 LLaVA-13B의 SARR 지표를 79.5% 감소시키면서 망각 품질과 모델 유용성을 유지할 수 있음을 보여줍니다. 코드와 데이터셋은 승인 후 공개될 예정입니다. 주의: 이 논문에는 유해한 언어와 이미지의 예가 포함되어 있으므로 주의가 필요합니다.

## 🎯 주요 포인트

- 1. 멀티모달 대형 언어 모델(MLLM)의 안전성 문제를 해결하기 위해 SAFEERASER라는 안전성 언러닝 벤치마크를 제안했습니다.
- 2. 기존의 머신 언러닝(MU) 방법은 모델 성능을 유지하면서 특정 지식을 잊게 하는 데 어려움을 겪고 있으며, 과도한 잊음 현상이 발생합니다.
- 3. 과도한 잊음을 완화하기 위해 프롬프트 디커플(PD) 손실을 도입하였으며, 이를 통해 안전한 답변 거부율(SARR)이라는 새로운 지표를 제안했습니다.
- 4. 실험 결과, PD 손실을 기존 언러닝 방법과 결합하면 과도한 잊음을 효과적으로 방지하고, LLaVA-7B 및 LLaVA-13B 모델에서 SARR 지표를 79.5% 감소시킬 수 있음을 보여주었습니다.
- 5. 본 논문은 유해한 언어와 이미지의 예시를 포함하고 있으므로 독자의 주의가 필요합니다.


---

*Generated on 2025-09-24 05:17:07*