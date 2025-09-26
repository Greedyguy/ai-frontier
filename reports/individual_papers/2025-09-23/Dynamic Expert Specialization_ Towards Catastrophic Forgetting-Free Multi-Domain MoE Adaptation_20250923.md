---
keywords:
  - Mixture-of-Experts
  - Catastrophic Forgetting
  - Dynamic Expert Specialization
  - Adaptive Fine-Tuning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16882
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:36:51.276537",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Mixture-of-Experts",
    "Catastrophic Forgetting",
    "Dynamic Expert Specialization",
    "Adaptive Fine-Tuning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Mixture-of-Experts": 0.85,
    "Catastrophic Forgetting": 0.88,
    "Dynamic Expert Specialization": 0.9,
    "Adaptive Fine-Tuning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Mixture-of-Experts",
        "canonical": "Mixture-of-Experts",
        "aliases": [
          "MoE"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's methodology, offering a unique approach to model adaptation.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Catastrophic Forgetting",
        "canonical": "Catastrophic Forgetting",
        "aliases": [
          "Forgetting"
        ],
        "category": "specific_connectable",
        "rationale": "A critical challenge in multi-domain adaptation, relevant for linking to related research.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.88
      },
      {
        "surface": "Dynamic Expert Specialization",
        "canonical": "Dynamic Expert Specialization",
        "aliases": [
          "DES"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel framework that is central to the paper's contribution.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.9
      },
      {
        "surface": "Adaptive Fine-Tuning",
        "canonical": "Adaptive Fine-Tuning",
        "aliases": [
          "Fine-Tuning"
        ],
        "category": "specific_connectable",
        "rationale": "A method for optimizing model performance, relevant to many adaptation strategies.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "model"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Mixture-of-Experts",
      "resolved_canonical": "Mixture-of-Experts",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Catastrophic Forgetting",
      "resolved_canonical": "Catastrophic Forgetting",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Dynamic Expert Specialization",
      "resolved_canonical": "Dynamic Expert Specialization",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Adaptive Fine-Tuning",
      "resolved_canonical": "Adaptive Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Dynamic Expert Specialization: Towards Catastrophic Forgetting-Free Multi-Domain MoE Adaptation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16882.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16882](https://arxiv.org/abs/2509.16882)

## 🔗 유사한 논문
- [[2025-09-22/DiEP_ Adaptive Mixture-of-Experts Compression through Differentiable Expert Pruning_20250922|DiEP: Adaptive Mixture-of-Experts Compression through Differentiable Expert Pruning]] (86.5% similar)
- [[2025-09-22/MoE-CE_ Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework_20250922|MoE-CE: Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework]] (85.6% similar)
- [[2025-09-22/TrueMoE_ Dual-Routing Mixture of Discriminative Experts for Synthetic Image Detection_20250922|TrueMoE: Dual-Routing Mixture of Discriminative Experts for Synthetic Image Detection]] (85.1% similar)
- [[2025-09-23/MoEs Are Stronger than You Think_ Hyper-Parallel Inference Scaling with RoE_20250923|MoEs Are Stronger than You Think: Hyper-Parallel Inference Scaling with RoE]] (84.7% similar)
- [[2025-09-22/Beyond Spurious Signals_ Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing_20250922|Beyond Spurious Signals: Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing]] (83.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Catastrophic Forgetting|Catastrophic Forgetting]], [[keywords/Adaptive Fine-Tuning|Adaptive Fine-Tuning]]
**⚡ Unique Technical**: [[keywords/Mixture-of-Experts|Mixture-of-Experts]], [[keywords/Dynamic Expert Specialization|Dynamic Expert Specialization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16882v1 Announce Type: cross 
Abstract: Mixture-of-Experts (MoE) models offer immense capacity via sparsely gated expert subnetworks, yet adapting them to multiple domains without catastrophic forgetting remains an open challenge. Existing approaches either incur prohibitive computation, suffer cross-domain interference, or require separate runs per domain. We propose DES-MoE, a dynamic expert specialization framework for multi-domain adaptation of Mixture-of-Experts models. DES-MoE addresses catastrophic forgetting through three innovations: (1) an adaptive router balancing pre-trained knowledge retention and task-specific updates via distillation, (2) real-time expert-domain correlation mapping to isolate domain-specific gradients, and (3) a three-phase adaptive fine-tuning schedule that progressively freezes non-specialized parameters. Evaluated on six domains (math, code, law, etc.), DES-MoE matches single-domain ESFT performance while training one unified model, reduces forgetting by 89% compared to full fine-tuning as domains scale from 2 to 6, and achieves 68% faster convergence than conventional methods. Our work establishes dynamic expert isolation as a scalable paradigm for multi-task MoE adaptation.

## 📝 요약

Mixture-of-Experts (MoE) 모델은 전문가 하위 네트워크를 통해 높은 용량을 제공하지만, 여러 도메인에 적응하면서 망각을 방지하는 것은 여전히 어려운 문제입니다. 이를 해결하기 위해 제안된 DES-MoE는 세 가지 혁신을 통해 망각을 방지합니다: (1) 사전 학습된 지식 유지와 과제별 업데이트를 균형 있게 조정하는 적응형 라우터, (2) 실시간 전문가-도메인 상관관계 매핑을 통한 도메인별 그래디언트 분리, (3) 비전문가 매개변수를 점진적으로 고정하는 세 단계의 적응형 미세 조정 일정입니다. DES-MoE는 단일 도메인 성능을 유지하면서도 망각을 89% 줄이고, 기존 방법보다 68% 빠른 수렴 속도를 보입니다. 이 연구는 다중 작업 MoE 적응을 위한 확장 가능한 패러다임을 제시합니다.

## 🎯 주요 포인트

- 1. DES-MoE는 Mixture-of-Experts 모델의 다중 도메인 적응을 위한 동적 전문가 특화 프레임워크를 제안합니다.
- 2. 이 프레임워크는 적응형 라우터를 통해 사전 학습된 지식의 유지와 작업별 업데이트를 균형 있게 조절합니다.
- 3. 실시간 전문가-도메인 상관 매핑을 통해 도메인별 그래디언트를 분리하여 망각을 방지합니다.
- 4. 세 단계의 적응형 미세 조정 스케줄을 통해 비전문가 매개변수를 점진적으로 고정합니다.
- 5. DES-MoE는 단일 도메인 ESFT 성능을 유지하면서도 통합 모델을 훈련하며, 도메인이 증가할수록 망각을 89% 줄이고 기존 방법보다 68% 빠른 수렴을 달성합니다.


---

*Generated on 2025-09-23 23:36:51*