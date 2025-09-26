<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:33:51.358018",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Few-Shot Learning",
    "Vision-Language Model",
    "Subspace Representation Learning",
    "Context Optimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Few-Shot Learning": 0.82,
    "Vision-Language Model": 0.8,
    "Subspace Representation Learning": 0.78,
    "Context Optimization": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Few-shot OOD detection",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "Few-shot Out-of-Distribution Detection"
        ],
        "category": "specific_connectable",
        "rationale": "This connects to the trending topic of Few-Shot Learning, which is crucial for understanding advancements in OOD detection.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLMs"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are a key component in the paper, linking to the broader trend of multimodal AI.",
        "novelty_score": 0.47,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Subspace Representation Learning",
        "canonical": "Subspace Representation Learning",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a novel approach proposed in the paper, offering a unique angle on representation learning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Context Optimization",
        "canonical": "Context Optimization",
        "aliases": [
          "CoOp"
        ],
        "category": "unique_technical",
        "rationale": "The paper introduces this as a novel framework, which is central to its methodology.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "Artificial Intelligence",
      "Open-world Settings",
      "Softmax Probabilities"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Few-shot OOD detection",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.47,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Subspace Representation Learning",
      "resolved_canonical": "Subspace Representation Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Context Optimization",
      "resolved_canonical": "Context Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Prompt Optimization Meets Subspace Representation Learning for Few-shot Out-of-Distribution Detection

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18111.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18111](https://arxiv.org/abs/2509.18111)

## 🔗 유사한 논문
- [[2025-09-22/CoDoL_ Conditional Domain Prompt Learning for Out-of-Distribution Generalization_20250922|CoDoL: Conditional Domain Prompt Learning for Out-of-Distribution Generalization]] (86.4% similar)
- [[2025-09-18/GROOD_ GRadient-Aware Out-of-Distribution Detection_20250918|GROOD: GRadient-Aware Out-of-Distribution Detection]] (83.3% similar)
- [[2025-09-23/Long-Tailed Out-of-Distribution Detection with Refined Separate Class Learning_20250923|Long-Tailed Out-of-Distribution Detection with Refined Separate Class Learning]] (82.5% similar)
- [[2025-09-23/Dual-View Alignment Learning with Hierarchical-Prompt for Class-Imbalance Multi-Label Classification_20250923|Dual-View Alignment Learning with Hierarchical-Prompt for Class-Imbalance Multi-Label Classification]] (82.0% similar)
- [[2025-09-19/An Empirical Study of Federated Prompt Learning for Vision Language Model_20250919|An Empirical Study of Federated Prompt Learning for Vision Language Model]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Subspace Representation Learning|Subspace Representation Learning]], [[keywords/Context Optimization|Context Optimization]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18111v1 Announce Type: cross 
Abstract: The reliability of artificial intelligence (AI) systems in open-world settings depends heavily on their ability to flag out-of-distribution (OOD) inputs unseen during training. Recent advances in large-scale vision-language models (VLMs) have enabled promising few-shot OOD detection frameworks using only a handful of in-distribution (ID) samples. However, existing prompt learning-based OOD methods rely solely on softmax probabilities, overlooking the rich discriminative potential of the feature embeddings learned by VLMs trained on millions of samples. To address this limitation, we propose a novel context optimization (CoOp)-based framework that integrates subspace representation learning with prompt tuning. Our approach improves ID-OOD separability by projecting the ID features into a subspace spanned by prompt vectors, while projecting ID-irrelevant features into an orthogonal null space. To train such OOD detection framework, we design an easy-to-handle end-to-end learning criterion that ensures strong OOD detection performance as well as high ID classification accuracy. Experiments on real-world datasets showcase the effectiveness of our approach.

## 📝 요약

이 논문은 대규모 비전-언어 모델(VLM)을 활용한 소수 샘플 기반의 OOD(분포 외) 탐지 프레임워크를 제안합니다. 기존 방법들이 소프트맥스 확률에만 의존하는 한계를 극복하기 위해, 이 연구는 프롬프트 튜닝과 하위 공간 표현 학습을 결합한 새로운 컨텍스트 최적화(CoOp) 기반 프레임워크를 도입합니다. 제안된 방법은 ID(분포 내) 특징을 프롬프트 벡터로 구성된 하위 공간에 투영하고, ID와 무관한 특징은 직교하는 널 공간에 투영하여 ID-OOD 구분성을 향상시킵니다. 이 프레임워크는 강력한 OOD 탐지 성능과 높은 ID 분류 정확도를 보장하는 학습 기준을 설계하여, 실제 데이터셋 실험에서 그 효과를 입증했습니다.

## 🎯 주요 포인트

- 1. 인공지능 시스템의 신뢰성은 훈련 시 보지 못한 분포 외 입력을 식별하는 능력에 크게 의존합니다.
- 2. 대규모 비전-언어 모델(VLM)의 발전은 소수의 분포 내 샘플만으로도 효과적인 분포 외 탐지 프레임워크를 가능하게 했습니다.
- 3. 기존의 프롬프트 학습 기반 분포 외 탐지 방법은 소프트맥스 확률에만 의존하여 VLM이 학습한 특징 임베딩의 잠재력을 충분히 활용하지 못합니다.
- 4. 제안된 CoOp 기반 프레임워크는 프롬프트 튜닝과 부분 공간 표현 학습을 통합하여 ID-OOD 구분성을 향상시킵니다.
- 5. 실험 결과, 제안된 방법이 실제 데이터셋에서 높은 분포 외 탐지 성능과 분포 내 분류 정확도를 보였습니다.


---

*Generated on 2025-09-24 13:33:51*