---
keywords:
  - Nested Subspace Networks
  - Large Language Model
  - Compute-Performance Frontier
  - Uncertainty-Aware Objective
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17874
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:59:00.778653",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Nested Subspace Networks",
    "Large Language Model",
    "Compute-Performance Frontier",
    "Uncertainty-Aware Objective"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Nested Subspace Networks": 0.88,
    "Large Language Model": 0.85,
    "Compute-Performance Frontier": 0.8,
    "Uncertainty-Aware Objective": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Nested Subspace Networks",
        "canonical": "Nested Subspace Networks",
        "aliases": [
          "NSNs"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel architectural paradigm that enhances model adaptability across compute budgets.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Key component in the application of NSNs, relevant for linking with foundational model discussions.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "compute-performance frontier",
        "canonical": "Compute-Performance Frontier",
        "aliases": [],
        "category": "evolved_concepts",
        "rationale": "Describes the balance between computational efficiency and model performance, crucial for adaptive models.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "uncertainty-aware objective",
        "canonical": "Uncertainty-Aware Objective",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Highlights a method for optimizing models by balancing contributions based on difficulty, relevant for model training.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "efficiency"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Nested Subspace Networks",
      "resolved_canonical": "Nested Subspace Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "compute-performance frontier",
      "resolved_canonical": "Compute-Performance Frontier",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "uncertainty-aware objective",
      "resolved_canonical": "Uncertainty-Aware Objective",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Deep Hierarchical Learning with Nested Subspace Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17874.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17874](https://arxiv.org/abs/2509.17874)

## 🔗 유사한 논문
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (83.1% similar)
- [[2025-09-18/The Energy-Efficient Hierarchical Neural Network with Fast FPGA-Based Incremental Learning_20250918|The Energy-Efficient Hierarchical Neural Network with Fast FPGA-Based Incremental Learning]] (83.1% similar)
- [[2025-09-17/NIRVANA_ Structured pruning reimagined for large language models compression_20250917|NIRVANA: Structured pruning reimagined for large language models compression]] (82.4% similar)
- [[2025-09-19/Hierarchical Federated Learning for Social Network with Mobility_20250919|Hierarchical Federated Learning for Social Network with Mobility]] (82.2% similar)
- [[2025-09-22/Latent Zoning Network_ A Unified Principle for Generative Modeling, Representation Learning, and Classification_20250922|Latent Zoning Network: A Unified Principle for Generative Modeling, Representation Learning, and Classification]] (82.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Uncertainty-Aware Objective|Uncertainty-Aware Objective]]
**⚡ Unique Technical**: [[keywords/Nested Subspace Networks|Nested Subspace Networks]]
**🚀 Evolved Concepts**: [[keywords/Compute-Performance Frontier|Compute-Performance Frontier]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17874v1 Announce Type: new 
Abstract: Large neural networks are typically trained for a fixed computational budget, creating a rigid trade-off between performance and efficiency that is ill-suited for deployment in resource-constrained or dynamic environments. Existing approaches to this problem present a difficult choice: training a discrete collection of specialist models is computationally prohibitive, while dynamic methods like slimmable networks often lack the flexibility to be applied to large, pre-trained foundation models. In this work, we propose Nested Subspace Networks (NSNs), a novel architectural paradigm that enables a single model to be dynamically and granularly adjusted across a continuous spectrum of compute budgets at inference time. The core of our approach is to re-parameterize linear layers to satisfy a nested subspace property, such that the function computed at a given rank is a strict subspace of the function at any higher rank. We show that this entire hierarchy of models can be optimized jointly via an uncertainty-aware objective that learns to balance the contributions of different ranks based on their intrinsic difficulty. We demonstrate empirically that NSNs can be surgically applied to pre-trained LLMs and unlock a smooth and predictable compute-performance frontier. For example, a single NSN-adapted model can achieve a 50% reduction in inference FLOPs with only a 5 percentage point loss in accuracy. Our findings establish NSNs as a powerful framework for creating the next generation of adaptive foundation models.

## 📝 요약

이 논문에서는 자원 제약이나 동적 환경에서의 효율적인 대규모 신경망 활용을 위한 새로운 아키텍처 패러다임인 Nested Subspace Networks(NSNs)를 제안합니다. NSNs는 단일 모델이 추론 시 다양한 계산 예산에 맞춰 동적으로 조정될 수 있도록 합니다. 이를 위해 선형 계층을 재구성하여 특정 랭크에서 계산된 함수가 더 높은 랭크의 함수의 엄격한 부분 공간이 되도록 합니다. 이 방법은 불확실성을 고려한 목표를 통해 다양한 랭크의 기여도를 최적화합니다. 실험 결과, NSNs는 사전 학습된 대규모 언어 모델(LLM)에 적용되어 계산량을 50% 줄이면서도 정확도 손실을 5%로 제한할 수 있음을 보여줍니다. NSNs는 차세대 적응형 모델 개발에 강력한 프레임워크를 제공합니다.

## 🎯 주요 포인트

- 1. 대형 신경망의 고정된 계산 예산 문제를 해결하기 위해 Nested Subspace Networks(NSNs)를 제안합니다.
- 2. NSNs는 단일 모델을 통해 추론 시 다양한 계산 예산에 맞춰 동적이고 세밀하게 조정할 수 있는 새로운 아키텍처 패러다임입니다.
- 3. NSNs는 선형 레이어를 재매개변수화하여 특정 랭크에서 계산된 함수가 더 높은 랭크의 함수의 엄격한 부분 공간이 되도록 합니다.
- 4. NSNs는 사전 학습된 대형 언어 모델(LLM)에 적용되어 매끄럽고 예측 가능한 계산-성능 경계를 제공합니다.
- 5. NSNs를 적용한 모델은 추론 시 FLOPs를 50% 줄이면서도 정확도 손실을 5% 포인트로 제한할 수 있습니다.


---

*Generated on 2025-09-24 01:59:00*