---
keywords:
  - LLM Cache Bandit
  - Query Heterogeneity
  - Knapsack Problem
  - Cost-Effective LLM Inference
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2509.15515
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:29:44.209350",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "LLM Cache Bandit",
    "Query Heterogeneity",
    "Knapsack Problem",
    "Cost-Effective LLM Inference"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "LLM Cache Bandit": 0.78,
    "Query Heterogeneity": 0.72,
    "Knapsack Problem": 0.68,
    "Cost-Effective LLM Inference": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "LLM Cache Bandit",
        "canonical": "LLM Cache Bandit",
        "aliases": [
          "Large Language Model Cache Bandit"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and introduces a unique approach to optimizing cache strategies for LLMs.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Query Heterogeneity",
        "canonical": "Query Heterogeneity",
        "aliases": [
          "Heterogeneous Queries"
        ],
        "category": "unique_technical",
        "rationale": "Addressing query heterogeneity is a key challenge in the paper, impacting cache selection strategies.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "Knapsack Problem",
        "canonical": "Knapsack Problem",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "The paper frames cache selection as a knapsack problem, which is a well-known optimization problem.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.68
      },
      {
        "surface": "Cost-Effective LLM Inference",
        "canonical": "Cost-Effective LLM Inference",
        "aliases": [
          "Efficient LLM Inference"
        ],
        "category": "unique_technical",
        "rationale": "The focus on cost-effective inference is crucial for practical applications of LLMs.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "cache selection",
      "computational overhead"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "LLM Cache Bandit",
      "resolved_canonical": "LLM Cache Bandit",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Query Heterogeneity",
      "resolved_canonical": "Query Heterogeneity",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Knapsack Problem",
      "resolved_canonical": "Knapsack Problem",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.68
      }
    },
    {
      "candidate_surface": "Cost-Effective LLM Inference",
      "resolved_canonical": "Cost-Effective LLM Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# LLM Cache Bandit Revisited: Addressing Query Heterogeneity for Cost-Effective LLM Inference

**Korean Title:** LLM 캐시 밴딧 재검토: 비용 효율적인 LLM 추론을 위한 쿼리 이질성 해결

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15515.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2509.15515](https://arxiv.org/abs/2509.15515)

## 🔗 유사한 논문
- [[2025-09-22/Robustifying Learning-Augmented Caching Efficiently without Compromising 1-Consistency_20250922|Robustifying Learning-Augmented Caching Efficiently without Compromising 1-Consistency]] (82.5% similar)
- [[2025-09-22/KVCompose_ Efficient Structured KV Cache Compression with Composite Tokens_20250922|KVCompose: Efficient Structured KV Cache Compression with Composite Tokens]] (82.2% similar)
- [[2025-09-22/Cache-of-Thought_ Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning_20250922|Cache-of-Thought: Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning]] (81.4% similar)
- [[2025-09-22/Adaptive Self-improvement LLM Agentic System for ML Library Development_20250922|Adaptive Self-improvement LLM Agentic System for ML Library Development]] (79.7% similar)
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (79.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Knapsack Problem|Knapsack Problem]]
**⚡ Unique Technical**: [[keywords/LLM Cache Bandit|LLM Cache Bandit]], [[keywords/Query Heterogeneity|Query Heterogeneity]], [[keywords/Cost-Effective LLM Inference|Cost-Effective LLM Inference]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15515v1 Announce Type: new 
Abstract: This paper revisits the LLM cache bandit problem, with a special focus on addressing the query heterogeneity for cost-effective LLM inference. Previous works often assume uniform query sizes. Heterogeneous query sizes introduce a combinatorial structure for cache selection, making the cache replacement process more computationally and statistically challenging. We treat optimal cache selection as a knapsack problem and employ an accumulation-based strategy to effectively balance computational overhead and cache updates. In theoretical analysis, we prove that the regret of our algorithm achieves an $O(\sqrt{MNT})$ bound, improving the coefficient of $\sqrt{MN}$ compared to the $O(MN\sqrt{T})$ result in Berkeley, where $N$ is the total number of queries and $M$ is the cache size. Additionally, we also provide a problem-dependent bound, which was absent in previous works. The experiment rely on real-world data show that our algorithm reduces the total cost by approximately 12\%.

## 🔍 Abstract (한글 번역)

arXiv:2509.15515v1 발표 유형: 신규  
초록: 본 논문은 비용 효율적인 대규모 언어 모델(LLM) 추론을 위해 쿼리 이질성을 해결하는 데 중점을 두고 LLM 캐시 밴딧 문제를 재검토합니다. 이전 연구들은 종종 균일한 쿼리 크기를 가정했습니다. 이질적인 쿼리 크기는 캐시 선택에 조합적 구조를 도입하여 캐시 교체 과정을 더 복잡하고 통계적으로 도전적으로 만듭니다. 우리는 최적의 캐시 선택을 배낭 문제로 간주하고, 계산 오버헤드와 캐시 업데이트를 효과적으로 균형 잡기 위해 누적 기반 전략을 사용합니다. 이론적 분석에서, 우리는 우리의 알고리즘의 후회가 $O(\sqrt{MNT})$ 경계를 달성함을 증명하며, 이는 버클리에서의 $O(MN\sqrt{T})$ 결과에 비해 $\sqrt{MN}$ 계수를 개선한 것입니다. 여기서 $N$은 총 쿼리 수이고 $M$은 캐시 크기입니다. 추가적으로, 이전 연구들에서는 없었던 문제 의존적 경계도 제공합니다. 실제 데이터에 기반한 실험은 우리의 알고리즘이 총 비용을 약 12% 절감함을 보여줍니다.

## 📝 요약

이 논문은 LLM 캐시 밴딧 문제를 재검토하며, 특히 비용 효율적인 LLM 추론을 위한 쿼리 이질성 문제를 해결하는 데 중점을 둡니다. 기존 연구는 주로 균일한 쿼리 크기를 가정했으나, 이질적인 쿼리 크기는 캐시 선택에 조합적 구조를 도입하여 캐시 교체 과정을 더 복잡하게 만듭니다. 본 연구는 최적의 캐시 선택을 배낭 문제로 간주하고, 계산 오버헤드와 캐시 업데이트를 효과적으로 균형 잡기 위해 누적 기반 전략을 사용합니다. 이론적 분석을 통해 제안된 알고리즘의 후회(regret)가 $O(\sqrt{MNT})$ 경계를 달성함을 증명하며, 이는 Berkeley의 $O(MN\sqrt{T})$ 결과에 비해 $\sqrt{MN}$ 계수를 개선한 것입니다. 또한, 이전 연구에 없던 문제 의존적 경계도 제공합니다. 실험 결과, 제안된 알고리즘은 총 비용을 약 12% 절감함을 보여줍니다.

## 🎯 주요 포인트

- 1. 이 논문은 LLM 캐시 밴딧 문제를 재검토하며, 비용 효율적인 LLM 추론을 위한 쿼리 이질성 문제를 해결하는 데 중점을 둡니다.
- 2. 이질적인 쿼리 크기는 캐시 선택에 조합적 구조를 도입하여 캐시 교체 과정을 더 복잡하게 만듭니다.
- 3. 최적의 캐시 선택을 배낭 문제로 간주하고, 계산 오버헤드와 캐시 업데이트를 효과적으로 균형 잡기 위해 누적 기반 전략을 사용합니다.
- 4. 제안된 알고리즘의 후회(regret)는 $O(\sqrt{MNT})$ 경계를 달성하며, 이는 기존의 $O(MN\sqrt{T})$ 결과에 비해 개선된 것입니다.
- 5. 실험 결과, 제안된 알고리즘은 총 비용을 약 12% 절감하는 것으로 나타났습니다.


---

*Generated on 2025-09-23 11:29:44*