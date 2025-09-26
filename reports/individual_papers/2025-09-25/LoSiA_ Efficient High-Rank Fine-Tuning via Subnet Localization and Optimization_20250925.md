---
keywords:
  - Parameter-Efficient Fine-Tuning
  - Low-Rank Adaptation
  - Gradient Sparsity Analysis
  - Domain Specialization
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2507.04487
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:30:11.143550",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Parameter-Efficient Fine-Tuning",
    "Low-Rank Adaptation",
    "Gradient Sparsity Analysis",
    "Domain Specialization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Parameter-Efficient Fine-Tuning": 0.78,
    "Low-Rank Adaptation": 0.82,
    "Gradient Sparsity Analysis": 0.77,
    "Domain Specialization": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Parameter-Efficient Fine-Tuning",
        "canonical": "Parameter-Efficient Fine-Tuning",
        "aliases": [
          "PEFT"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's innovation and distinguishes it from traditional fine-tuning methods.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Low-Rank Adaptation",
        "canonical": "Low-Rank Adaptation",
        "aliases": [
          "LoRA"
        ],
        "category": "specific_connectable",
        "rationale": "LoRA is a well-known method in the context of efficient fine-tuning, providing strong connectivity to related works.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Gradient Sparsity Analysis",
        "canonical": "Gradient Sparsity Analysis",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This technique is a novel approach within the paper for optimizing sub-networks, enhancing its specificity.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.77
      },
      {
        "surface": "Domain Specialization",
        "canonical": "Domain Specialization",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Domain specialization is a common application area for fine-tuning methods, linking it to broader technical discussions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "training process"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Parameter-Efficient Fine-Tuning",
      "resolved_canonical": "Parameter-Efficient Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Low-Rank Adaptation",
      "resolved_canonical": "Low-Rank Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Gradient Sparsity Analysis",
      "resolved_canonical": "Gradient Sparsity Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Domain Specialization",
      "resolved_canonical": "Domain Specialization",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# LoSiA: Efficient High-Rank Fine-Tuning via Subnet Localization and Optimization

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2507.04487.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2507.04487](https://arxiv.org/abs/2507.04487)

## 🔗 유사한 논문
- [[2025-09-25/Localized LoRA_ A Structured Low-Rank Approximation for Efficient Fine-Tuning_20250925|Localized LoRA: A Structured Low-Rank Approximation for Efficient Fine-Tuning]] (89.9% similar)
- [[2025-09-23/Robust Federated Finetuning of LLMs via Alternating Optimization of LoRA_20250923|Robust Federated Finetuning of LLMs via Alternating Optimization of LoRA]] (87.7% similar)
- [[2025-09-23/TASO_ Task-Aligned Sparse Optimization for Parameter-Efficient Model Adaptation_20250923|TASO: Task-Aligned Sparse Optimization for Parameter-Efficient Model Adaptation]] (86.6% similar)
- [[2025-09-22/Sparsity May Be All You Need_ Sparse Random Parameter Adaptation_20250922|Sparsity May Be All You Need: Sparse Random Parameter Adaptation]] (86.2% similar)
- [[2025-09-23/RefLoRA_ Refactored Low-Rank Adaptation for Efficient Fine-Tuning of Large Models_20250923|RefLoRA: Refactored Low-Rank Adaptation for Efficient Fine-Tuning of Large Models]] (85.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Domain Specialization|Domain Specialization]]
**🔗 Specific Connectable**: [[keywords/Low-Rank Adaptation|Low-Rank Adaptation]]
**⚡ Unique Technical**: [[keywords/Parameter-Efficient Fine-Tuning|Parameter-Efficient Fine-Tuning]], [[keywords/Gradient Sparsity Analysis|Gradient Sparsity Analysis]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.04487v4 Announce Type: replace-cross 
Abstract: Parameter-Efficient Fine-Tuning (PEFT) methods, such as LoRA, significantly reduce the number of trainable parameters by introducing low-rank decomposition matrices. However, existing methods perform extensive matrix multiplications in domain specialization tasks, resulting in computational inefficiency and sub-optimal fine-tuning performance. Hence, we propose LoSiA(Low-Resources Subnet Integration Adaptation), an innovative method that dynamically localizes and optimizes critical parameters during the training process. Specifically, it identifies a sub-network using gradient sparsity analysis and optimizes it as the trainable target. This design enables effective high-rank adaptation by updating only the sub-network parameters, reducing the additional matrix multiplication. We also present LoSiA-Pro, a faster implementation of LoSiA, which reduces the training latency by about $27\%$ compared to LoRA. Extensive evaluations show that our method achieves minimal performance drop compared to full fine-tuning, while requiring the least training time across domain specialization and common-sense reasoning tasks. Further analysis shows that LoSiA also reduces forgetting during continued training. The source code is available at https://github.com/KlozeWang/LoSiA.

## 📝 요약

이 논문은 매개변수 효율적 미세 조정(PEFT) 방법의 비효율성을 개선하기 위해 LoSiA라는 새로운 방법을 제안합니다. 기존의 PEFT 방법은 행렬 곱셈이 많아 비효율적이었으나, LoSiA는 훈련 과정에서 중요한 매개변수를 동적으로 최적화하여 이를 해결합니다. 구체적으로, 기울기 희소성 분석을 통해 서브 네트워크를 식별하고 이를 최적화 대상으로 삼아 고차원 적응을 효과적으로 수행합니다. LoSiA-Pro는 LoSiA의 빠른 구현 버전으로, LoRA 대비 훈련 시간을 약 27% 단축합니다. 실험 결과, LoSiA는 전체 미세 조정 대비 성능 저하가 거의 없으며, 도메인 특화 및 상식 추론 작업에서 가장 적은 훈련 시간을 요구합니다. 추가 분석에서는 LoSiA가 지속적인 훈련 중 망각을 줄이는 데 효과적임을 보여줍니다. 소스 코드는 GitHub에서 제공됩니다.

## 🎯 주요 포인트

- 1. LoSiA는 훈련 과정에서 중요한 파라미터를 동적으로 지역화하고 최적화하여 고효율의 파라미터 적응을 가능하게 합니다.
- 2. LoSiA-Pro는 LoRA에 비해 약 27%의 훈련 지연 시간을 줄여주는 빠른 구현 방법입니다.
- 3. 제안된 방법은 도메인 특화 및 상식 추론 작업에서 전체 미세 조정과 비교하여 최소한의 성능 저하를 보입니다.
- 4. LoSiA는 훈련 중 망각을 줄이는 데 효과적입니다.
- 5. 소스 코드는 https://github.com/KlozeWang/LoSiA에서 제공됩니다.


---

*Generated on 2025-09-25 16:30:11*