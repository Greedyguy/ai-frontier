---
keywords:
  - PruneCD
  - Large Language Model
  - Contrastive Decoding
  - Hallucination Problem
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16598
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:27:48.566631",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "PruneCD",
    "Large Language Model",
    "Contrastive Decoding",
    "Hallucination Problem"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "PruneCD": 0.78,
    "Large Language Model": 0.8,
    "Contrastive Decoding": 0.77,
    "Hallucination Problem": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "PruneCD",
        "canonical": "PruneCD",
        "aliases": [
          "Pruned Contrastive Decoding"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel method for improving factuality in language models, offering a unique approach to contrastive decoding.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus on improving factuality, connecting to a wide range of related research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "Contrastive Decoding",
        "canonical": "Contrastive Decoding",
        "aliases": [
          "Contrastive Prior"
        ],
        "category": "specific_connectable",
        "rationale": "Key technique discussed in the paper, relevant for linking to contrastive learning methods.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "Hallucination Problem",
        "canonical": "Hallucination Problem",
        "aliases": [
          "Model Hallucinations"
        ],
        "category": "specific_connectable",
        "rationale": "Addresses a significant challenge in language models, relevant for discussions on model reliability.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "PruneCD",
      "resolved_canonical": "PruneCD",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
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
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Contrastive Decoding",
      "resolved_canonical": "Contrastive Decoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Hallucination Problem",
      "resolved_canonical": "Hallucination Problem",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# PruneCD: Contrasting Pruned Self Model to Improve Decoding Factuality

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16598.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16598](https://arxiv.org/abs/2509.16598)

## 🔗 유사한 논문
- [[2025-09-17/DSCC-HS_ A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models_20250917|DSCC-HS: A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models]] (85.1% similar)
- [[2025-09-22/Backdoor Mitigation via Invertible Pruning Masks_20250922|Backdoor Mitigation via Invertible Pruning Masks]] (82.3% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (82.2% similar)
- [[2025-09-22/CARD_ A Cache-Assisted Parallel Speculative Decoding Framework via Query-and-Correct Paradigm for Accelerating LLM Inference_20250922|CARD: A Cache-Assisted Parallel Speculative Decoding Framework via Query-and-Correct Paradigm for Accelerating LLM Inference]] (81.7% similar)
- [[2025-09-22/World Modelling Improves Language Model Agents_20250922|World Modelling Improves Language Model Agents]] (81.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Contrastive Decoding|Contrastive Decoding]], [[keywords/Hallucination Problem|Hallucination Problem]]
**⚡ Unique Technical**: [[keywords/PruneCD|PruneCD]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16598v1 Announce Type: cross 
Abstract: To mitigate the hallucination problem in large language models, DoLa exploits early exit logits from the same model as a contrastive prior. However, we found that these early exit logits tend to be flat, low in magnitude, and fail to reflect meaningful contrasts. To address this, we propose PruneCD, a novel contrastive decoding method that constructs the amateur model via layer pruning rather than early exit. This design leads to more informative and well-aligned logits, enabling more effective contrastive decoding. Through qualitative and quantitative analyses, we demonstrate that PruneCD consistently improves factuality with minimal inference overhead, offering a robust and practical approach to mitigating hallucinations in LLMs.

## 📝 요약

이 논문은 대형 언어 모델의 환각 문제를 해결하기 위해 PruneCD라는 새로운 대조적 디코딩 방법을 제안합니다. 기존의 DoLa 방법은 조기 종료 로짓을 대조적 사전으로 사용하지만, 이 로짓은 평탄하고 의미 있는 대조를 제공하지 못합니다. PruneCD는 조기 종료 대신 레이어 프루닝을 통해 아마추어 모델을 구성하여 더 정보가 풍부하고 잘 정렬된 로짓을 생성합니다. 이를 통해 대조적 디코딩이 효과적으로 이루어지며, 질적 및 양적 분석을 통해 PruneCD가 최소한의 추론 오버헤드로 사실성을 지속적으로 개선함을 보여줍니다.

## 🎯 주요 포인트

- 1. DoLa는 대조적 사전으로 초기 종료 로짓을 활용하여 대형 언어 모델의 환각 문제를 완화하려고 시도하였으나, 초기 종료 로짓이 평탄하고 의미 있는 대조를 반영하지 못하는 문제를 발견하였다.
- 2. PruneCD는 초기 종료 대신 레이어 가지치기를 통해 아마추어 모델을 구성하는 새로운 대조적 디코딩 방법을 제안한다.
- 3. PruneCD는 더 정보가 풍부하고 잘 정렬된 로짓을 생성하여 대조적 디코딩을 더 효과적으로 수행할 수 있게 한다.
- 4. 질적 및 양적 분석을 통해 PruneCD가 최소한의 추론 오버헤드로 사실성을 일관되게 향상시키는 것을 입증하였다.
- 5. PruneCD는 대형 언어 모델의 환각 문제를 완화하는 데 있어 견고하고 실용적인 접근 방식을 제공한다.


---

*Generated on 2025-09-23 23:27:48*