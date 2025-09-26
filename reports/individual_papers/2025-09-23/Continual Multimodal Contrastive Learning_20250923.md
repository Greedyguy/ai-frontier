---
keywords:
  - Continual Multimodal Contrastive Learning
  - Multimodal Learning
  - Stability and Plasticity
  - Self-supervised Learning
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2503.14963
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:40:19.772647",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Continual Multimodal Contrastive Learning",
    "Multimodal Learning",
    "Stability and Plasticity",
    "Self-supervised Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Continual Multimodal Contrastive Learning": 0.88,
    "Multimodal Learning": 0.82,
    "Stability and Plasticity": 0.75,
    "Self-supervised Learning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Continual Multimodal Contrastive Learning",
        "canonical": "Continual Multimodal Contrastive Learning",
        "aliases": [
          "CMCL"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel concept introduced in the paper, crucial for linking multimodal and continual learning research.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "Multimodal Contrastive Learning",
        "canonical": "Multimodal Learning",
        "aliases": [
          "MCL"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to existing multimodal learning frameworks, enhancing cross-modal representation alignment.",
        "novelty_score": 0.55,
        "connectivity_score": 0.87,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Stability and Plasticity",
        "canonical": "Stability and Plasticity",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Key principles in the paper's methodology, relevant for linking to cognitive and learning theories.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "Contrastive Learning",
        "canonical": "Self-supervised Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A core technique in the paper, linking to broader self-supervised learning strategies.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
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
      "candidate_surface": "Continual Multimodal Contrastive Learning",
      "resolved_canonical": "Continual Multimodal Contrastive Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Multimodal Contrastive Learning",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.87,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Stability and Plasticity",
      "resolved_canonical": "Stability and Plasticity",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Contrastive Learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Continual Multimodal Contrastive Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2503.14963.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2503.14963](https://arxiv.org/abs/2503.14963)

## 🔗 유사한 논문
- [[2025-09-22/Towards Robust Visual Continual Learning with Multi-Prototype Supervision_20250922|Towards Robust Visual Continual Learning with Multi-Prototype Supervision]] (86.5% similar)
- [[2025-09-22/Advances in Multimodal Adaptation and Generalization_ From Traditional Approaches to Foundation Models_20250922|Advances in Multimodal Adaptation and Generalization: From Traditional Approaches to Foundation Models]] (85.7% similar)
- [[2025-09-22/Global Pre-fixing, Local Adjusting_ A Simple yet Effective Contrastive Strategy for Continual Learning_20250922|Global Pre-fixing, Local Adjusting: A Simple yet Effective Contrastive Strategy for Continual Learning]] (85.3% similar)
- [[2025-09-22/Perception-R1_ Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward_20250922|Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward]] (85.2% similar)
- [[2025-09-23/Can multimodal representation learning by alignment preserve modality-specific information?_20250923|Can multimodal representation learning by alignment preserve modality-specific information?]] (85.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Continual Multimodal Contrastive Learning|Continual Multimodal Contrastive Learning]], [[keywords/Stability and Plasticity|Stability and Plasticity]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.14963v3 Announce Type: replace 
Abstract: Multimodal Contrastive Learning (MCL) advances in aligning different modalities and generating multimodal representations in a joint space. By leveraging contrastive learning across diverse modalities, large-scale multimodal data enhances representational quality. However, a critical yet often overlooked challenge remains: multimodal data is rarely collected in a single process, and training from scratch is computationally expensive. Instead, emergent multimodal data can be used to optimize existing models gradually, i.e., models are trained on a sequence of modality pair data. We define this problem as Continual Multimodal Contrastive Learning (CMCL), an underexplored yet crucial research direction at the intersection of multimodal and continual learning. In this paper, we formulate CMCL through two specialized principles of stability and plasticity. We theoretically derive a novel optimization-based method, which projects updated gradients from dual sides onto subspaces where any gradient is prevented from interfering with the previously learned knowledge. Two upper bounds provide theoretical insights on both stability and plasticity in our solution. Beyond our theoretical contributions, we conduct experiments on multiple datasets by comparing our method against advanced continual learning baselines. The empirical results further support our claims and demonstrate the efficacy of our method. Our codes are available at https://github.com/Xiaohao-Liu/CMCL.

## 📝 요약

이 논문은 다양한 모달리티를 정렬하고 멀티모달 표현을 생성하는 멀티모달 대조 학습(MCL)의 발전을 다룹니다. 그러나 멀티모달 데이터를 한 번에 수집하기 어려운 점과 초기부터 학습하는 데 드는 높은 계산 비용이 문제로 지적됩니다. 이를 해결하기 위해, 점진적으로 기존 모델을 최적화하는 연속 멀티모달 대조 학습(CMCL)을 제안합니다. CMCL은 안정성과 가소성이라는 두 가지 원칙을 통해 이론적으로 새로운 최적화 방법을 도출하며, 이전에 학습된 지식에 방해가 되지 않도록 업데이트된 기울기를 투영합니다. 이 방법의 안정성과 가소성에 대한 이론적 통찰을 제공하는 두 개의 상한을 제시하고, 여러 데이터셋에서 실험을 통해 기존 연속 학습 기법과 비교하여 제안된 방법의 효율성을 입증합니다.

## 🎯 주요 포인트

- 1. 다중모달 대조 학습(MCL)은 다양한 모달리티를 정렬하고 다중모달 표현을 공동 공간에서 생성하는 데 기여한다.
- 2. 다중모달 데이터를 한 번에 수집하는 것은 드물며, 처음부터 학습하는 것은 계산 비용이 많이 든다.
- 3. 지속적 다중모달 대조 학습(CMCL)은 다중모달 및 지속 학습의 교차점에서 중요한 연구 방향으로 정의된다.
- 4. CMCL은 안정성과 가소성의 두 가지 원칙을 통해 이론적으로 최적화 기반 방법을 도출한다.
- 5. 실험 결과는 이론적 기여를 뒷받침하며, 제안된 방법의 효능을 입증한다.


---

*Generated on 2025-09-24 02:40:19*