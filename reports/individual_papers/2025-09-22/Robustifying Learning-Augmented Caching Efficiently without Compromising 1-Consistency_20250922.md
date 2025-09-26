---
keywords:
  - Learning-Augmented Caching
  - Guard Framework
  - 1-Consistency
  - Robustification
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2507.16242
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:21:28.697409",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Learning-Augmented Caching",
    "Guard Framework",
    "1-Consistency",
    "Robustification"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Learning-Augmented Caching": 0.78,
    "Guard Framework": 0.82,
    "1-Consistency": 0.7,
    "Robustification": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "learning-augmented caching",
        "canonical": "Learning-Augmented Caching",
        "aliases": [
          "augmented caching"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and represents a novel approach in caching algorithms.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Guard",
        "canonical": "Guard Framework",
        "aliases": [
          "Guard robustification"
        ],
        "category": "unique_technical",
        "rationale": "Guard is the proposed framework in the paper, crucial for understanding the new methodology.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      },
      {
        "surface": "1-consistency",
        "canonical": "1-Consistency",
        "aliases": [
          "consistency level 1"
        ],
        "category": "specific_connectable",
        "rationale": "1-Consistency is a key performance metric in caching algorithms, relevant for linking to algorithmic performance discussions.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.7
      },
      {
        "surface": "robustification",
        "canonical": "Robustification",
        "aliases": [
          "robustness enhancement"
        ],
        "category": "broad_technical",
        "rationale": "Robustification is a critical process in improving algorithm resilience, relevant across various technical domains.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.6,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "cache misses",
      "computational overhead"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "learning-augmented caching",
      "resolved_canonical": "Learning-Augmented Caching",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Guard",
      "resolved_canonical": "Guard Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "1-consistency",
      "resolved_canonical": "1-Consistency",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "robustification",
      "resolved_canonical": "Robustification",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.6,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# Robustifying Learning-Augmented Caching Efficiently without Compromising 1-Consistency

**Korean Title:** 학습 보강 캐싱을 1-일관성을 손상시키지 않고 효율적으로 강화하기

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2507.16242.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2507.16242](https://arxiv.org/abs/2507.16242)

## 🔗 유사한 논문
- [[2025-09-22/LLM Cache Bandit Revisited_ Addressing Query Heterogeneity for Cost-Effective LLM Inference_20250922|LLM Cache Bandit Revisited: Addressing Query Heterogeneity for Cost-Effective LLM Inference]] (82.5% similar)
- [[2025-09-19/Adversarial Distilled Retrieval-Augmented Guarding Model for Online Malicious Intent Detection_20250919|Adversarial Distilled Retrieval-Augmented Guarding Model for Online Malicious Intent Detection]] (81.4% similar)
- [[2025-09-19/Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (79.9% similar)
- [[2025-09-22/Boosting Active Learning with Knowledge Transfer_20250922|Boosting Active Learning with Knowledge Transfer]] (79.0% similar)
- [[2025-09-22/Inference Offloading for Cost-Sensitive Binary Classification at the Edge_20250922|Inference Offloading for Cost-Sensitive Binary Classification at the Edge]] (78.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Robustification|Robustification]]
**🔗 Specific Connectable**: [[keywords/1-Consistency|1-Consistency]]
**⚡ Unique Technical**: [[keywords/Learning-Augmented Caching|Learning-Augmented Caching]], [[keywords/Guard Framework|Guard Framework]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.16242v3 Announce Type: replace-cross 
Abstract: The online caching problem aims to minimize cache misses when serving a sequence of requests under a limited cache size. While naive learning-augmented caching algorithms achieve ideal $1$-consistency, they lack robustness guarantees. Existing robustification methods either sacrifice $1$-consistency or introduce significant computational overhead. In this paper, we introduce Guard, a lightweight robustification framework that enhances the robustness of a broad class of learning-augmented caching algorithms to $2H_k + 2$, while preserving their $1$-consistency. Guard achieves the current best-known trade-off between consistency and robustness, with only $O(1)$ additional per-request overhead, thereby maintaining the original time complexity of the base algorithm. Extensive experiments across multiple real-world datasets and prediction models validate the effectiveness of Guard in practice.

## 🔍 Abstract (한글 번역)

arXiv:2507.16242v3 발표 유형: 교체-교차  
초록: 온라인 캐싱 문제는 제한된 캐시 크기 하에서 요청 시퀀스를 제공할 때 캐시 미스를 최소화하는 것을 목표로 합니다. 단순한 학습 보강 캐싱 알고리즘은 이상적인 $1$-일관성을 달성하지만, 견고성 보장은 부족합니다. 기존의 견고화 방법은 $1$-일관성을 희생하거나 상당한 계산 오버헤드를 도입합니다. 본 논문에서는 Guard라는 경량의 견고화 프레임워크를 소개하여 학습 보강 캐싱 알고리즘의 견고성을 $2H_k + 2$로 향상시키면서도 $1$-일관성을 유지합니다. Guard는 일관성과 견고성 사이의 현재 알려진 최상의 절충점을 달성하며, 요청당 $O(1)$의 추가 오버헤드만을 요구하여 기본 알고리즘의 원래 시간 복잡성을 유지합니다. 다양한 실제 데이터셋과 예측 모델을 통한 광범위한 실험은 실무에서 Guard의 효과성을 입증합니다.

## 📝 요약

이 논문은 온라인 캐싱 문제에서 캐시 미스를 최소화하기 위한 새로운 방법론을 제안합니다. 기존의 학습 기반 캐싱 알고리즘은 이상적인 일관성을 달성하지만, 강건성 보장이 부족합니다. 이를 해결하기 위해, 저자들은 Guard라는 경량화된 강건화 프레임워크를 소개합니다. Guard는 다양한 학습 기반 캐싱 알고리즘의 강건성을 $2H_k + 2$로 향상시키면서도 $1$-일관성을 유지합니다. 이 방법은 일관성과 강건성 간의 최적의 균형을 제공하며, 요청당 $O(1)$의 추가적인 오버헤드만 발생시켜 기존 알고리즘의 시간 복잡성을 유지합니다. 여러 실제 데이터셋과 예측 모델을 통한 실험을 통해 Guard의 실용성을 검증했습니다.

## 🎯 주요 포인트

- 1. 온라인 캐싱 문제는 제한된 캐시 크기에서 요청 시퀀스를 처리할 때 캐시 미스를 최소화하는 것을 목표로 한다.
- 2. 기존의 학습 보강 캐싱 알고리즘은 $1$-일관성을 달성하지만, 견고성 보장이 부족하다.
- 3. Guard는 학습 보강 캐싱 알고리즘의 견고성을 $2H_k + 2$로 향상시키면서 $1$-일관성을 유지하는 경량화된 견고화 프레임워크이다.
- 4. Guard는 일관성과 견고성 간의 최적의 균형을 이루며, 요청당 $O(1)$의 추가 오버헤드만 발생시켜 기본 알고리즘의 시간 복잡성을 유지한다.
- 5. 다양한 실제 데이터셋과 예측 모델을 통한 광범위한 실험에서 Guard의 실효성이 입증되었다.


---

*Generated on 2025-09-23 11:21:28*