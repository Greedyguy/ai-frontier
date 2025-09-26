---
keywords:
  - Multimodal Learning
  - Information Bottleneck
  - Representation Disentanglement
  - Synergistic Information
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.20225
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:03:19.589522",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Information Bottleneck",
    "Representation Disentanglement",
    "Synergistic Information"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.79,
    "Information Bottleneck": 0.75,
    "Representation Disentanglement": 0.72,
    "Synergistic Information": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal Recommendation",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal Recommender Systems"
        ],
        "category": "specific_connectable",
        "rationale": "Links to the trending concept of integrating multiple data types for improved recommendations.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      },
      {
        "surface": "Information Bottleneck",
        "canonical": "Information Bottleneck",
        "aliases": [
          "IB"
        ],
        "category": "unique_technical",
        "rationale": "A unique approach in the paper that filters noise and preserves semantic information.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      },
      {
        "surface": "Representation-disentangled",
        "canonical": "Representation Disentanglement",
        "aliases": [
          "Disentangled Representation"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's approach in handling multimodal data.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "Synergistic Information",
        "canonical": "Synergistic Information",
        "aliases": [
          "Emergent Information"
        ],
        "category": "unique_technical",
        "rationale": "Describes a novel component of the proposed framework that captures emergent information.",
        "novelty_score": 0.65,
        "connectivity_score": 0.58,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "redundant information",
      "unique information"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal Recommendation",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Information Bottleneck",
      "resolved_canonical": "Information Bottleneck",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Representation-disentangled",
      "resolved_canonical": "Representation Disentanglement",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Synergistic Information",
      "resolved_canonical": "Synergistic Information",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.58,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Multimodal Representation-disentangled Information Bottleneck for Multimodal Recommendation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20225.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.20225](https://arxiv.org/abs/2509.20225)

## 🔗 유사한 논문
- [[2025-09-23/Enhancing Live Broadcast Engagement_ A Multi-modal Approach to Short Video Recommendations Using MMGCN and User Preferences_20250923|Enhancing Live Broadcast Engagement: A Multi-modal Approach to Short Video Recommendations Using MMGCN and User Preferences]] (83.9% similar)
- [[2025-09-22/Beyond Spurious Signals_ Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing_20250922|Beyond Spurious Signals: Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing]] (83.4% similar)
- [[2025-09-22/IGD_ Token Decisiveness Modeling via Information Gain in LLMs for Personalized Recommendation_20250922|IGD: Token Decisiveness Modeling via Information Gain in LLMs for Personalized Recommendation]] (82.6% similar)
- [[2025-09-23/MPIC_ Position-Independent Multimodal Context Caching System for Efficient MLLM Serving_20250923|MPIC: Position-Independent Multimodal Context Caching System for Efficient MLLM Serving]] (82.2% similar)
- [[2025-09-24/Sparse Training Scheme for Multimodal LLM_20250924|Sparse Training Scheme for Multimodal LLM]] (82.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Information Bottleneck|Information Bottleneck]], [[keywords/Representation Disentanglement|Representation Disentanglement]], [[keywords/Synergistic Information|Synergistic Information]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20225v1 Announce Type: cross 
Abstract: Multimodal data has significantly advanced recommendation systems by integrating diverse information sources to model user preferences and item characteristics. However, these systems often struggle with redundant and irrelevant information, which can degrade performance. Most existing methods either fuse multimodal information directly or use rigid architectural separation for disentanglement, failing to adequately filter noise and model the complex interplay between modalities. To address these challenges, we propose a novel framework, the Multimodal Representation-disentangled Information Bottleneck (MRdIB). Concretely, we first employ a Multimodal Information Bottleneck to compress the input representations, effectively filtering out task-irrelevant noise while preserving rich semantic information. Then, we decompose the information based on its relationship with the recommendation target into unique, redundant, and synergistic components. We achieve this decomposition with a series of constraints: a unique information learning objective to preserve modality-unique signals, a redundant information learning objective to minimize overlap, and a synergistic information learning objective to capture emergent information. By optimizing these objectives, MRdIB guides a model to learn more powerful and disentangled representations. Extensive experiments on several competitive models and three benchmark datasets demonstrate the effectiveness and versatility of our MRdIB in enhancing multimodal recommendation.

## 📝 요약

다중 모달 데이터를 활용한 추천 시스템은 사용자 선호도와 아이템 특성을 모델링하는 데 중요한 역할을 하지만, 불필요한 정보로 인해 성능 저하가 발생할 수 있습니다. 이를 해결하기 위해 본 연구는 새로운 프레임워크인 MRdIB(Multimodal Representation-disentangled Information Bottleneck)를 제안합니다. MRdIB는 입력 표현을 압축하여 불필요한 노이즈를 제거하고, 추천 대상과의 관계에 따라 정보를 고유, 중복, 시너지 구성 요소로 분해합니다. 이를 통해 모달리티 고유 신호를 보존하고 중복을 최소화하며, emergent 정보를 포착합니다. 다양한 모델과 데이터셋을 통한 실험 결과, MRdIB는 다중 모달 추천 성능을 효과적으로 향상시킴을 보여줍니다.

## 🎯 주요 포인트

- 1. 멀티모달 데이터는 사용자 선호도와 아이템 특성을 모델링하여 추천 시스템을 크게 발전시켰습니다.
- 2. 기존 방법들은 멀티모달 정보를 직접 융합하거나 분리하는 데 한계가 있어 노이즈 필터링과 모달리티 간 복잡한 상호작용 모델링에 실패합니다.
- 3. MRdIB 프레임워크는 멀티모달 정보 병목을 사용하여 입력 표현을 압축하고, 과제와 무관한 노이즈를 효과적으로 필터링합니다.
- 4. 정보는 추천 목표와의 관계에 따라 고유, 중복, 시너지 구성 요소로 분해되며, 각 구성 요소에 대한 학습 목표를 설정하여 모델이 강력하고 분리된 표현을 학습하도록 유도합니다.
- 5. 다양한 경쟁 모델과 세 가지 벤치마크 데이터셋에서의 실험을 통해 MRdIB의 효과성과 다재다능함이 입증되었습니다.


---

*Generated on 2025-09-25 16:03:19*