---
keywords:
  - Attention Mechanism
  - Self-Attention
  - Contract-and-Broadcast Self-Attention
  - Transformer
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16875
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:44:02.677060",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Attention Mechanism",
    "Self-Attention",
    "Contract-and-Broadcast Self-Attention",
    "Transformer"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Attention Mechanism": 0.88,
    "Self-Attention": 0.85,
    "Contract-and-Broadcast Self-Attention": 0.78,
    "Transformer": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Attention Mechanisms",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Attention",
          "Attention Layer"
        ],
        "category": "specific_connectable",
        "rationale": "Attention mechanisms are central to the paper's proposed method and are a key concept in linking related works.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "Self-Attention",
        "canonical": "Self-Attention",
        "aliases": [
          "Self Attention"
        ],
        "category": "specific_connectable",
        "rationale": "Self-attention is a specific type of attention mechanism that the paper aims to optimize, making it highly relevant for linking.",
        "novelty_score": 0.5,
        "connectivity_score": 0.87,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Contract-and-Broadcast Self-Attention",
        "canonical": "Contract-and-Broadcast Self-Attention",
        "aliases": [
          "CBSA"
        ],
        "category": "unique_technical",
        "rationale": "This is the novel mechanism introduced by the paper, crucial for understanding its unique contribution.",
        "novelty_score": 0.95,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Transformers",
        "canonical": "Transformer",
        "aliases": [
          "Transformer Model"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are the foundational architecture for the attention mechanisms discussed, providing broad connectivity.",
        "novelty_score": 0.3,
        "connectivity_score": 0.92,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "optimization objective",
      "quadratic complexity",
      "visual tasks"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Attention Mechanisms",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Self-Attention",
      "resolved_canonical": "Self-Attention",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.87,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Contract-and-Broadcast Self-Attention",
      "resolved_canonical": "Contract-and-Broadcast Self-Attention",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Transformers",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.92,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Towards Interpretable and Efficient Attention: Compressing All by Contracting a Few

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16875.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16875](https://arxiv.org/abs/2509.16875)

## 🔗 유사한 논문
- [[2025-09-22/Hierarchical Self-Attention_ Generalizing Neural Attention Mechanics to Multi-Scale Problems_20250922|Hierarchical Self-Attention: Generalizing Neural Attention Mechanics to Multi-Scale Problems]] (86.3% similar)
- [[2025-09-22/Attention Schema-based Attention Control (ASAC)_ A Cognitive-Inspired Approach for Attention Management in Transformers_20250922|Attention Schema-based Attention Control (ASAC): A Cognitive-Inspired Approach for Attention Management in Transformers]] (83.1% similar)
- [[2025-09-22/AttentionDrop_ A Novel Regularization Method for Transformer Models_20250922|AttentionDrop: A Novel Regularization Method for Transformer Models]] (82.9% similar)
- [[2025-09-18/Stochastic Clock Attention for Aligning Continuous and Ordered Sequences_20250918|Stochastic Clock Attention for Aligning Continuous and Ordered Sequences]] (81.4% similar)
- [[2025-09-18/Attention Beyond Neighborhoods_ Reviving Transformer for Graph Clustering_20250918|Attention Beyond Neighborhoods: Reviving Transformer for Graph Clustering]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]], [[keywords/Self-Attention|Self-Attention]]
**⚡ Unique Technical**: [[keywords/Contract-and-Broadcast Self-Attention|Contract-and-Broadcast Self-Attention]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16875v1 Announce Type: new 
Abstract: Attention mechanisms in Transformers have gained significant empirical success. Nonetheless, the optimization objectives underlying their forward pass are still unclear. Additionally, the quadratic complexity of self-attention is increasingly prohibitive. Unlike the prior work on addressing the interpretability or efficiency issue separately, we propose a unified optimization objective to alleviate both issues simultaneously. By unrolling the optimization over the objective, we derive an inherently interpretable and efficient attention mechanism, which compresses all tokens into low-dimensional structures by contracting a few representative tokens and then broadcasting the contractions back. This Contract-and-Broadcast Self-Attention (CBSA) mechanism can not only scale linearly but also generalize existing attention mechanisms as its special cases. Experiments further demonstrate comparable performance and even superior advantages of CBSA on several visual tasks. Code is available at this https URL.

## 📝 요약

이 논문은 트랜스포머의 주목 메커니즘의 최적화 목표를 명확히 하고, 자가 주목의 복잡성을 줄이기 위한 새로운 접근법을 제안합니다. 기존 연구와 달리, 해석 가능성과 효율성 문제를 동시에 해결하는 통합 최적화 목표를 도입했습니다. 이를 통해 본질적으로 해석 가능하고 효율적인 주목 메커니즘인 'Contract-and-Broadcast Self-Attention (CBSA)'를 개발했습니다. CBSA는 몇 개의 대표 토큰을 압축하여 저차원 구조로 만들고, 이를 다시 확장하여 전달하는 방식으로 작동하며, 선형 확장성을 가집니다. 실험 결과, CBSA는 여러 시각적 과제에서 기존 주목 메커니즘과 비교해 유사하거나 더 나은 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 트랜스포머의 주의 메커니즘은 경험적으로 성공을 거두었으나, 그 최적화 목표는 명확하지 않다.
- 2. 자기 주의 메커니즘의 이차 복잡성은 점점 더 큰 부담이 되고 있다.
- 3. 본 연구는 해석 가능성과 효율성 문제를 동시에 해결하기 위한 통합 최적화 목표를 제안한다.
- 4. 제안된 Contract-and-Broadcast Self-Attention (CBSA) 메커니즘은 선형 확장이 가능하며 기존 주의 메커니즘을 일반화할 수 있다.
- 5. 실험 결과, CBSA는 여러 시각적 과제에서 기존 방법과 비교하여 유사하거나 더 우수한 성능을 보였다.


---

*Generated on 2025-09-24 01:44:02*