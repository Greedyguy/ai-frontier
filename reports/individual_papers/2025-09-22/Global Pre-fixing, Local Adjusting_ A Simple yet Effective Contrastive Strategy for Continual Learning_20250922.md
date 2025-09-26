---
keywords:
  - Continual Learning
  - Contrastive Learning
  - Equiangular Tight Frame
  - Feature Structure
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15347
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:21:03.284716",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Continual Learning",
    "Contrastive Learning",
    "Equiangular Tight Frame",
    "Feature Structure"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Continual Learning": 0.78,
    "Contrastive Learning": 0.8,
    "Equiangular Tight Frame": 0.77,
    "Feature Structure": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Continual Learning",
        "canonical": "Continual Learning",
        "aliases": [
          "CL"
        ],
        "category": "specific_connectable",
        "rationale": "Continual Learning is a key concept in the paper, focusing on knowledge accumulation and reducing forgetting, which is central to the proposed strategy.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Contrastive Learning",
        "canonical": "Contrastive Learning",
        "aliases": [
          "Supervised Contrastive Learning"
        ],
        "category": "specific_connectable",
        "rationale": "The paper introduces a novel contrastive strategy, making this a crucial concept for understanding the proposed method.",
        "novelty_score": 0.6,
        "connectivity_score": 0.88,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "Equiangular Tight Frame",
        "canonical": "Equiangular Tight Frame",
        "aliases": [
          "ETF"
        ],
        "category": "unique_technical",
        "rationale": "This mathematical concept is central to the paper's method for structuring feature representations.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.77
      },
      {
        "surface": "Feature Structure",
        "canonical": "Feature Structure",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Understanding feature structure is essential for grasping the intra-task and inter-task adjustments proposed.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
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
      "candidate_surface": "Continual Learning",
      "resolved_canonical": "Continual Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Contrastive Learning",
      "resolved_canonical": "Contrastive Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.88,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Equiangular Tight Frame",
      "resolved_canonical": "Equiangular Tight Frame",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Feature Structure",
      "resolved_canonical": "Feature Structure",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Global Pre-fixing, Local Adjusting: A Simple yet Effective Contrastive Strategy for Continual Learning

**Korean Title:** 글로벌 사전 고정, 로컬 조정: 연속 학습을 위한 간단하지만 효과적인 대조 전략

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15347.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15347](https://arxiv.org/abs/2509.15347)

## 🔗 유사한 논문
- [[2025-09-22/Towards Robust Visual Continual Learning with Multi-Prototype Supervision_20250922|Towards Robust Visual Continual Learning with Multi-Prototype Supervision]] (84.7% similar)
- [[2025-09-18/HAM_ Hierarchical Adapter Merging for Scalable Continual Learning_20250918|HAM: Hierarchical Adapter Merging for Scalable Continual Learning]] (82.7% similar)
- [[2025-09-22/CLIPTTA_ Robust Contrastive Vision-Language Test-Time Adaptation_20250922|CLIPTTA: Robust Contrastive Vision-Language Test-Time Adaptation]] (82.0% similar)
- [[2025-09-19/Seeing 3D Through 2D Lenses_ 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification_20250919|Seeing 3D Through 2D Lenses: 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (81.7% similar)
- [[2025-09-19/ToolSample_ Dual Dynamic Sampling Methods with Curriculum Learning for RL-based Tool Learning_20250919|ToolSample: Dual Dynamic Sampling Methods with Curriculum Learning for RL-based Tool Learning]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Continual Learning|Continual Learning]], [[keywords/Contrastive Learning|Contrastive Learning]]
**⚡ Unique Technical**: [[keywords/Equiangular Tight Frame|Equiangular Tight Frame]], [[keywords/Feature Structure|Feature Structure]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15347v1 Announce Type: new 
Abstract: Continual learning (CL) involves acquiring and accumulating knowledge from evolving tasks while alleviating catastrophic forgetting. Recently, leveraging contrastive loss to construct more transferable and less forgetful representations has been a promising direction in CL. Despite advancements, their performance is still limited due to confusion arising from both inter-task and intra-task features. To address the problem, we propose a simple yet effective contrastive strategy named \textbf{G}lobal \textbf{P}re-fixing, \textbf{L}ocal \textbf{A}djusting for \textbf{S}upervised \textbf{C}ontrastive learning (GPLASC). Specifically, to avoid task-level confusion, we divide the entire unit hypersphere of representations into non-overlapping regions, with the centers of the regions forming an inter-task pre-fixed \textbf{E}quiangular \textbf{T}ight \textbf{F}rame (ETF). Meanwhile, for individual tasks, our method helps regulate the feature structure and form intra-task adjustable ETFs within their respective allocated regions. As a result, our method \textit{simultaneously} ensures discriminative feature structures both between tasks and within tasks and can be seamlessly integrated into any existing contrastive continual learning framework. Extensive experiments validate its effectiveness.

## 🔍 Abstract (한글 번역)

arXiv:2509.15347v1 발표 유형: 신규  
초록: 지속 학습(CL)은 진화하는 과제로부터 지식을 습득하고 축적하면서도 파국적 망각을 완화하는 것을 포함합니다. 최근에는 대조 손실을 활용하여 보다 전이 가능한 덜 망각적인 표현을 구축하는 것이 CL에서 유망한 방향으로 떠오르고 있습니다. 그러나 발전에도 불구하고, 이들의 성능은 여전히 과제 간 및 과제 내 특징에서 발생하는 혼란으로 인해 제한적입니다. 이 문제를 해결하기 위해, 우리는 \textbf{G}lobal \textbf{P}re-fixing, \textbf{L}ocal \textbf{A}djusting for \textbf{S}upervised \textbf{C}ontrastive learning (GPLASC)라는 간단하면서도 효과적인 대조 전략을 제안합니다. 구체적으로, 과제 수준의 혼란을 피하기 위해, 우리는 표현의 전체 단위 초구를 겹치지 않는 영역으로 나누고, 이 영역의 중심이 과제 간 고정된 \textbf{E}quiangular \textbf{T}ight \textbf{F}rame (ETF)을 형성하도록 합니다. 한편, 개별 과제의 경우, 우리 방법은 특징 구조를 조절하고 할당된 각 영역 내에서 과제 내 조정 가능한 ETF를 형성하는 데 도움을 줍니다. 결과적으로, 우리 방법은 과제 간 및 과제 내에서 동시에 변별적인 특징 구조를 보장하며, 기존의 대조 지속 학습 프레임워크에 매끄럽게 통합될 수 있습니다. 광범위한 실험을 통해 그 효과가 검증되었습니다.

## 📝 요약

이 논문은 연속 학습(CL)에서 발생하는 문제인 망각을 줄이기 위해 대조 손실을 활용하는 새로운 전략인 GPLASC를 제안합니다. 기존 방법들은 과제 간 및 과제 내 특징의 혼란으로 성능이 제한되었습니다. 이를 해결하기 위해, 제안된 방법은 표현의 전체 단위 초구를 비중첩 영역으로 나누고, 영역의 중심을 과제 간 고정된 등각 조밀 프레임(ETF)으로 형성합니다. 또한, 개별 과제에 대해 과제 내 조절 가능한 ETF를 형성하여 특징 구조를 조절합니다. 이 방법은 과제 간 및 과제 내에서 차별적인 특징 구조를 보장하며, 기존의 대조 연속 학습 프레임워크에 통합될 수 있습니다. 실험을 통해 그 효과가 입증되었습니다.

## 🎯 주요 포인트

- 1. 지속 학습에서 대조 손실을 활용하여 전이 가능하고 망각이 적은 표현을 구축하는 것이 유망한 방향으로 주목받고 있습니다.
- 2. 기존 방법들은 과제 간 및 과제 내 특징의 혼란으로 인해 성능이 제한적입니다.
- 3. 본 연구에서는 과제 수준의 혼란을 피하기 위해 표현의 전체 단위 초구를 비겹치는 영역으로 나누는 글로벌 프리픽싱, 로컬 조정 대조 학습 전략인 GPLASC를 제안합니다.
- 4. 제안된 방법은 과제 간 및 과제 내에서 변별적인 특징 구조를 동시에 보장하며, 기존 대조 지속 학습 프레임워크에 원활하게 통합될 수 있습니다.
- 5. 광범위한 실험을 통해 제안된 방법의 효과가 검증되었습니다.


---

*Generated on 2025-09-23 10:21:03*