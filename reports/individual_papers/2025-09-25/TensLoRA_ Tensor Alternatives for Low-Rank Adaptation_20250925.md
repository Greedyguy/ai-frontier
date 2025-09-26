---
keywords:
  - Low-Rank Adaptation
  - Transformer
  - Attention Mechanism
  - Tensor-based Adaptations
  - Vision-Language Model
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19391
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:33:30.538940",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Low-Rank Adaptation",
    "Transformer",
    "Attention Mechanism",
    "Tensor-based Adaptations",
    "Vision-Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Low-Rank Adaptation": 0.8,
    "Transformer": 0.85,
    "Attention Mechanism": 0.82,
    "Tensor-based Adaptations": 0.75,
    "Vision-Language Model": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Low-Rank Adaptation",
        "canonical": "Low-Rank Adaptation",
        "aliases": [
          "LoRA"
        ],
        "category": "unique_technical",
        "rationale": "Low-Rank Adaptation is central to the paper's contribution and is a unique technical concept.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "The paper discusses adaptations for Transformers, a fundamental concept in the field.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Attention Projections",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Attention Projections"
        ],
        "category": "specific_connectable",
        "rationale": "Attention Mechanism is a key component in the discussed adaptations, enhancing connectivity.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Tensor-based Adaptations",
        "canonical": "Tensor-based Adaptations",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The paper introduces a new framework for tensor-based adaptations, which is a novel contribution.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      },
      {
        "surface": "Vision and Language Benchmarks",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision and Language Benchmarks"
        ],
        "category": "evolved_concepts",
        "rationale": "The evaluation on vision and language benchmarks aligns with the concept of Vision-Language Models.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
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
      "candidate_surface": "Low-Rank Adaptation",
      "resolved_canonical": "Low-Rank Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Attention Projections",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Tensor-based Adaptations",
      "resolved_canonical": "Tensor-based Adaptations",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Vision and Language Benchmarks",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# TensLoRA: Tensor Alternatives for Low-Rank Adaptation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19391.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19391](https://arxiv.org/abs/2509.19391)

## 🔗 유사한 논문
- [[2025-09-23/Robust Federated Finetuning of LLMs via Alternating Optimization of LoRA_20250923|Robust Federated Finetuning of LLMs via Alternating Optimization of LoRA]] (88.0% similar)
- [[2025-09-23/RefLoRA_ Refactored Low-Rank Adaptation for Efficient Fine-Tuning of Large Models_20250923|RefLoRA: Refactored Low-Rank Adaptation for Efficient Fine-Tuning of Large Models]] (87.2% similar)
- [[2025-09-23/TASO_ Task-Aligned Sparse Optimization for Parameter-Efficient Model Adaptation_20250923|TASO: Task-Aligned Sparse Optimization for Parameter-Efficient Model Adaptation]] (86.5% similar)
- [[2025-09-23/Accurate and Efficient Low-Rank Model Merging in Core Space_20250923|Accurate and Efficient Low-Rank Model Merging in Core Space]] (85.5% similar)
- [[2025-09-24/TsqLoRA_ Towards Sensitivity and Quality Low-Rank Adaptation for Efficient Fine-Tuning_20250924|TsqLoRA: Towards Sensitivity and Quality Low-Rank Adaptation for Efficient Fine-Tuning]] (85.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Low-Rank Adaptation|Low-Rank Adaptation]], [[keywords/Tensor-based Adaptations|Tensor-based Adaptations]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19391v1 Announce Type: cross 
Abstract: Low-Rank Adaptation (LoRA) is widely used to efficiently adapt Transformers by adding trainable low-rank matrices to attention projections. While effective, these matrices are considered independent for each attention projection (Query, Key, and Value) and each layer. Recent extensions have considered joint, tensor-based adaptations, but only in limited forms and without a systematic framework. We introduce TensLoRA, a unified framework that aggregates LoRA updates into higher-order tensors and models a broad family of tensor-based low-rank adaptations. Our formulation generalizes existing tensor-based methods and enables mode-specific compression rates, allowing parameter budgets to be tailored according to the modality and task. Experiments on vision and language benchmarks reveal that the tensor construction directly impacts performance, sometimes better than standard LoRA under similar parameter counts.

## 📝 요약

이 논문에서는 Transformer 모델의 효율적인 적응을 위해 사용되는 저랭크 적응(LoRA)의 확장을 제안합니다. 기존의 LoRA는 각 주의 프로젝션에 독립적으로 저랭크 행렬을 추가하는 방식이었지만, 이 연구에서는 이를 고차원 텐서로 통합하는 TensLoRA라는 새로운 프레임워크를 소개합니다. TensLoRA는 기존의 텐서 기반 방법들을 일반화하며, 모드별 압축률을 조절할 수 있어 다양한 모달리티와 작업에 맞춘 파라미터 예산 설정이 가능합니다. 실험 결과, TensLoRA는 비슷한 파라미터 수에서도 기존 LoRA보다 더 나은 성능을 보이는 경우가 있음을 확인했습니다.

## 🎯 주요 포인트

- 1. Low-Rank Adaptation (LoRA)는 Transformer의 효율적인 적응을 위해 주로 사용되며, 주의 메커니즘의 각 투영에 독립적인 저랭크 행렬을 추가합니다.
- 2. TensLoRA는 LoRA 업데이트를 고차원 텐서로 집계하여 다양한 텐서 기반 저랭크 적응을 모델링하는 통합 프레임워크를 제안합니다.
- 3. TensLoRA는 기존의 텐서 기반 방법을 일반화하고, 모드별 압축률을 가능하게 하여 모달리티와 작업에 따라 매개변수 예산을 조정할 수 있습니다.
- 4. 실험 결과, 텐서 구성은 성능에 직접적인 영향을 미치며, 때로는 유사한 매개변수 수에서 표준 LoRA보다 더 나은 성능을 보입니다.


---

*Generated on 2025-09-25 15:33:30*