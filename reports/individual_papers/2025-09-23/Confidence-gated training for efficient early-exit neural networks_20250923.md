---
keywords:
  - Neural Network
  - Confidence-Gated Training
  - Indian Pines Dataset
  - Fashion-MNIST Dataset
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17885
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:11:57.709747",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Confidence-Gated Training",
    "Indian Pines Dataset",
    "Fashion-MNIST Dataset"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.85,
    "Confidence-Gated Training": 0.78,
    "Indian Pines Dataset": 0.72,
    "Fashion-MNIST Dataset": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Early-exit neural networks",
        "canonical": "Neural Network",
        "aliases": [
          "early exit networks",
          "exit networks"
        ],
        "category": "broad_technical",
        "rationale": "Links to the concept of neural networks with a focus on efficiency, relevant to resource-constrained environments.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Confidence-Gated Training",
        "canonical": "Confidence-Gated Training",
        "aliases": [
          "CGT"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel training paradigm that mitigates gradient interference, enhancing early-exit strategies.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Indian Pines",
        "canonical": "Indian Pines Dataset",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A specific dataset used in experiments, relevant for linking to other works using the same dataset.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "Fashion-MNIST",
        "canonical": "Fashion-MNIST Dataset",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A widely used dataset for benchmarking, facilitating connections to other studies using this dataset.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "gradient interference",
      "resource-constrained environments"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Early-exit neural networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Confidence-Gated Training",
      "resolved_canonical": "Confidence-Gated Training",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Indian Pines",
      "resolved_canonical": "Indian Pines Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Fashion-MNIST",
      "resolved_canonical": "Fashion-MNIST Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# Confidence-gated training for efficient early-exit neural networks

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17885.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17885](https://arxiv.org/abs/2509.17885)

## 🔗 유사한 논문
- [[2025-09-22/CBPNet_ A Continual Backpropagation Prompt Network for Alleviating Plasticity Loss on Edge Devices_20250922|CBPNet: A Continual Backpropagation Prompt Network for Alleviating Plasticity Loss on Edge Devices]] (81.8% similar)
- [[2025-09-22/Deep Reinforcement Learning with Gradient Eligibility Traces_20250922|Deep Reinforcement Learning with Gradient Eligibility Traces]] (81.7% similar)
- [[2025-09-23/Gradient Interference-Aware Graph Coloring for Multitask Learning_20250923|Gradient Interference-Aware Graph Coloring for Multitask Learning]] (81.2% similar)
- [[2025-09-22/Neural Networks for Learnable and Scalable Influence Estimation of Instruction Fine-Tuning Data_20250922|Neural Networks for Learnable and Scalable Influence Estimation of Instruction Fine-Tuning Data]] (81.1% similar)
- [[2025-09-22/DIVEBATCH_ Accelerating Model Training Through Gradient-Diversity Aware Batch Size Adaptation_20250922|DIVEBATCH: Accelerating Model Training Through Gradient-Diversity Aware Batch Size Adaptation]] (81.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Indian Pines Dataset|Indian Pines Dataset]], [[keywords/Fashion-MNIST Dataset|Fashion-MNIST Dataset]]
**⚡ Unique Technical**: [[keywords/Confidence-Gated Training|Confidence-Gated Training]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17885v1 Announce Type: cross 
Abstract: Early-exit neural networks reduce inference cost by enabling confident predictions at intermediate layers. However, joint training often leads to gradient interference, with deeper classifiers dominating optimization. We propose Confidence-Gated Training (CGT), a paradigm that conditionally propagates gradients from deeper exits only when preceding exits fail. This encourages shallow classifiers to act as primary decision points while reserving deeper layers for harder inputs. By aligning training with the inference-time policy, CGT mitigates overthinking, improves early-exit accuracy, and preserves efficiency. Experiments on the Indian Pines and Fashion-MNIST benchmarks show that CGT lowers average inference cost while improving overall accuracy, offering a practical solution for deploying deep models in resource-constrained environments.

## 📝 요약

이 논문은 중간 계층에서 자신 있는 예측을 가능하게 하여 추론 비용을 줄이는 조기 종료 신경망에 대해 다룹니다. 그러나 공동 학습 시 깊은 계층의 분류기가 최적화를 지배하는 문제점이 있습니다. 이를 해결하기 위해, 우리는 Confidence-Gated Training (CGT)이라는 방법론을 제안합니다. CGT는 이전 계층이 실패할 경우에만 깊은 계층에서의 기울기를 조건부로 전파하여 얕은 계층이 주요 결정 지점으로 작용하도록 유도합니다. 이는 훈련을 추론 시간 정책과 일치시켜 과도한 계산을 줄이고, 조기 종료 정확도를 개선하며, 효율성을 유지합니다. Indian Pines와 Fashion-MNIST 벤치마크 실험 결과, CGT는 평균 추론 비용을 낮추면서 전체 정확도를 향상시켜, 자원이 제한된 환경에서 심층 모델을 배포하는 실용적인 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. 조기 종료 신경망은 중간 계층에서 자신 있는 예측을 통해 추론 비용을 줄입니다.
- 2. 공동 학습 시 깊은 계층의 분류기가 최적화를 지배하여 그래디언트 간섭이 발생할 수 있습니다.
- 3. Confidence-Gated Training(CGT)은 이전 계층이 실패할 경우에만 깊은 계층의 그래디언트를 전파하여 얕은 분류기가 주요 결정 지점으로 작용하도록 유도합니다.
- 4. CGT는 훈련을 추론 시간 정책과 정렬하여 과도한 연산을 줄이고, 조기 종료 정확도를 개선하며 효율성을 유지합니다.
- 5. Indian Pines와 Fashion-MNIST 벤치마크 실험에서 CGT는 평균 추론 비용을 낮추면서 전체 정확도를 향상시켜, 자원이 제한된 환경에서 심층 모델을 배포하기 위한 실용적인 솔루션을 제공합니다.


---

*Generated on 2025-09-24 00:11:57*