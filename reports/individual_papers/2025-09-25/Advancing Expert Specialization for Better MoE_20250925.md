---
keywords:
  - Mixture-of-Experts
  - Large Language Model
  - Orthogonality Loss
  - Variance Loss
category: cs.CL
publish_date: 2025-09-25
arxiv_id: 2505.22323
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:55:05.224407",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Mixture-of-Experts",
    "Large Language Model",
    "Orthogonality Loss",
    "Variance Loss"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Mixture-of-Experts": 0.78,
    "Large Language Model": 0.72,
    "Orthogonality Loss": 0.7,
    "Variance Loss": 0.68
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
        "rationale": "Mixture-of-Experts is a distinct model architecture that enhances expert specialization, crucial for linking specialized research in neural networks.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are foundational in NLP, providing a broad technical context for the study of expert specialization.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      },
      {
        "surface": "Orthogonality Loss",
        "canonical": "Orthogonality Loss",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Orthogonality Loss is a novel technique proposed to enhance expert specialization, offering a unique technical insight.",
        "novelty_score": 0.82,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Variance Loss",
        "canonical": "Variance Loss",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Variance Loss is introduced as a complementary objective to improve routing decisions, providing a unique technical contribution.",
        "novelty_score": 0.8,
        "connectivity_score": 0.58,
        "specificity_score": 0.78,
        "link_intent_score": 0.68
      }
    ],
    "ban_list_suggestions": [
      "auxiliary loss",
      "load balancing"
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
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Orthogonality Loss",
      "resolved_canonical": "Orthogonality Loss",
      "decision": "linked",
      "scores": {
        "novelty": 0.82,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Variance Loss",
      "resolved_canonical": "Variance Loss",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.58,
        "specificity": 0.78,
        "link_intent": 0.68
      }
    }
  ]
}
-->

# Advancing Expert Specialization for Better MoE

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.22323.pdf)
**Category**: cs.CL
**Published**: 2025-09-25
**ArXiv ID**: [2505.22323](https://arxiv.org/abs/2505.22323)

## 🔗 유사한 논문
- [[2025-09-24/Symphony-MoE_ Harmonizing Disparate Pre-trained Models into a Coherent Mixture-of-Experts_20250924|Symphony-MoE: Harmonizing Disparate Pre-trained Models into a Coherent Mixture-of-Experts]] (91.4% similar)
- [[2025-09-23/MoEs Are Stronger than You Think_ Hyper-Parallel Inference Scaling with RoE_20250923|MoEs Are Stronger than You Think: Hyper-Parallel Inference Scaling with RoE]] (90.2% similar)
- [[2025-09-24/Union of Experts_ Adapting Hierarchical Routing to Equivalently Decomposed Transformer_20250924|Union of Experts: Adapting Hierarchical Routing to Equivalently Decomposed Transformer]] (89.8% similar)
- [[2025-09-22/DiEP_ Adaptive Mixture-of-Experts Compression through Differentiable Expert Pruning_20250922|DiEP: Adaptive Mixture-of-Experts Compression through Differentiable Expert Pruning]] (89.2% similar)
- [[2025-09-23/GuiLoMo_ Allocating Expert Number and Rank for LoRA-MoE via Bilevel Optimization with GuidedSelection Vectors_20250923|GuiLoMo: Allocating Expert Number and Rank for LoRA-MoE via Bilevel Optimization with GuidedSelection Vectors]] (88.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Mixture-of-Experts|Mixture-of-Experts]], [[keywords/Orthogonality Loss|Orthogonality Loss]], [[keywords/Variance Loss|Variance Loss]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.22323v2 Announce Type: replace 
Abstract: Mixture-of-Experts (MoE) models enable efficient scaling of large language models (LLMs) by activating only a subset of experts per input. However, we observe that the commonly used auxiliary load balancing loss often leads to expert overlap and overly uniform routing, which hinders expert specialization and degrades overall performance during post-training. To address this, we propose a simple yet effective solution that introduces two complementary objectives: (1) an orthogonality loss to encourage experts to process distinct types of tokens, and (2) a variance loss to encourage more discriminative routing decisions. Gradient-level analysis demonstrates that these objectives are compatible with the existing auxiliary loss and contribute to optimizing the training process. Experimental results over various model architectures and across multiple benchmarks show that our method significantly enhances expert specialization. Notably, our method improves classic MoE baselines with auxiliary loss by up to 23.79%, while also maintaining load balancing in downstream tasks, without any architectural modifications or additional components. We will release our code to contribute to the community.

## 📝 요약

Mixture-of-Experts (MoE) 모델은 입력당 일부 전문가만 활성화하여 대형 언어 모델의 효율적 확장을 가능하게 합니다. 그러나 기존의 부가적인 부하 균형 손실은 전문가 간의 중복과 지나치게 균일한 라우팅을 초래하여 전문가의 전문화와 성능을 저하시킵니다. 이를 해결하기 위해, 우리는 두 가지 목표를 제안합니다: (1) 전문가들이 서로 다른 유형의 토큰을 처리하도록 유도하는 직교성 손실과 (2) 보다 차별화된 라우팅 결정을 유도하는 분산 손실입니다. 실험 결과, 우리의 방법은 다양한 모델 아키텍처와 벤치마크에서 전문가의 전문화를 크게 향상시켰으며, 기존 MoE 모델 대비 최대 23.79% 성능 향상을 보였습니다. 추가적인 아키텍처 수정 없이도 부하 균형을 유지하며, 코드를 공개하여 연구 커뮤니티에 기여할 예정입니다.

## 🎯 주요 포인트

- 1. Mixture-of-Experts (MoE) 모델은 입력당 일부 전문가만 활성화하여 대형 언어 모델의 효율적 확장을 가능하게 한다.
- 2. 기존의 부가적인 부하 균형 손실은 전문가의 중복과 지나치게 균일한 라우팅을 유발하여 전문가의 전문화를 방해하고 성능을 저하시킨다.
- 3. 제안된 해결책은 전문가가 서로 다른 유형의 토큰을 처리하도록 유도하는 직교 손실과 더 분별력 있는 라우팅 결정을 유도하는 분산 손실을 포함한다.
- 4. 제안된 방법은 다양한 모델 아키텍처와 여러 벤치마크에서 전문가의 전문화를 크게 향상시키며, 부가적인 부하 균형 손실을 사용하는 기존 MoE 기준 모델의 성능을 최대 23.79%까지 개선한다.
- 5. 제안된 방법은 아키텍처 수정이나 추가 구성 요소 없이도 하위 작업에서 부하 균형을 유지하며, 코드가 공개될 예정이다.


---

*Generated on 2025-09-26 08:55:05*