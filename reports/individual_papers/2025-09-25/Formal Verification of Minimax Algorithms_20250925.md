---
keywords:
  - Minimax Algorithm
  - Alpha-Beta Pruning
  - Transposition Table
  - Formal Verification
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.20138
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:19:46.746273",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Minimax Algorithm",
    "Alpha-Beta Pruning",
    "Transposition Table",
    "Formal Verification"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Minimax Algorithm": 0.8,
    "Alpha-Beta Pruning": 0.79,
    "Transposition Table": 0.75,
    "Formal Verification": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Minimax Algorithms",
        "canonical": "Minimax Algorithm",
        "aliases": [
          "Minimax Search"
        ],
        "category": "unique_technical",
        "rationale": "Minimax algorithms are central to the paper and provide a unique technical focus for linking.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Alpha-Beta Pruning",
        "canonical": "Alpha-Beta Pruning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Alpha-Beta Pruning is a specific technique within minimax algorithms that enhances connectivity.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "Transposition Tables",
        "canonical": "Transposition Table",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Transposition tables are a specific feature in the algorithms discussed, enhancing specificity.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Formal Verification",
        "canonical": "Formal Verification",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Formal verification is a broad technical concept that underpins the paper's methodology.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "Dafny",
      "Python"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Minimax Algorithms",
      "resolved_canonical": "Minimax Algorithm",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Alpha-Beta Pruning",
      "resolved_canonical": "Alpha-Beta Pruning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Transposition Tables",
      "resolved_canonical": "Transposition Table",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Formal Verification",
      "resolved_canonical": "Formal Verification",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Formal Verification of Minimax Algorithms

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20138.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.20138](https://arxiv.org/abs/2509.20138)

## 🔗 유사한 논문
- [[2025-09-23/Reinforced Generation of Combinatorial Structures_ Applications to Complexity Theory_20250923|Reinforced Generation of Combinatorial Structures: Applications to Complexity Theory]] (80.2% similar)
- [[2025-09-19/Mini-Batch Robustness Verification of Deep Neural Networks_20250919|Mini-Batch Robustness Verification of Deep Neural Networks]] (77.0% similar)
- [[2025-09-19/Optimal Algorithms for Bandit Learning in Matching Markets_20250919|Optimal Algorithms for Bandit Learning in Matching Markets]] (76.7% similar)
- [[2025-09-23/Alpha-GPT_ Human-AI Interactive Alpha Mining for Quantitative Investment_20250923|Alpha-GPT: Human-AI Interactive Alpha Mining for Quantitative Investment]] (76.5% similar)
- [[2025-09-25/Calibrated Reasoning_ An Explanatory Verifier for Dynamic and Efficient Problem-Solving_20250925|Calibrated Reasoning: An Explanatory Verifier for Dynamic and Efficient Problem-Solving]] (76.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Formal Verification|Formal Verification]]
**🔗 Specific Connectable**: [[keywords/Alpha-Beta Pruning|Alpha-Beta Pruning]]
**⚡ Unique Technical**: [[keywords/Minimax Algorithm|Minimax Algorithm]], [[keywords/Transposition Table|Transposition Table]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20138v1 Announce Type: new 
Abstract: Using the Dafny verification system, we formally verify a range of minimax search algorithms, including variations with alpha-beta pruning and transposition tables. For depth-limited search with transposition tables, we introduce a witness-based correctness criterion and apply it to two representative algorithms. All verification artifacts, including proofs and Python implementations, are publicly available.

## 📝 요약

이 논문에서는 Dafny 검증 시스템을 사용하여 다양한 미니맥스 탐색 알고리즘을 형식적으로 검증했습니다. 알파-베타 가지치기와 전이 테이블을 포함한 변형 알고리즘도 검증 대상에 포함되었습니다. 특히, 전이 테이블을 사용하는 깊이 제한 탐색에 대해 증거 기반의 정확성 기준을 도입하고, 이를 두 가지 대표 알고리즘에 적용했습니다. 모든 검증 산출물, 증명 및 Python 구현은 공개되어 있습니다.

## 🎯 주요 포인트

- 1. Dafny 검증 시스템을 사용하여 다양한 미니맥스 검색 알고리즘을 형식적으로 검증했습니다.
- 2. 알파-베타 가지치기와 전이 테이블을 포함한 알고리즘 변형을 검증했습니다.
- 3. 전이 테이블을 사용하는 깊이 제한 검색에 대해 증인 기반의 정확성 기준을 도입했습니다.
- 4. 두 개의 대표 알고리즘에 증인 기반의 정확성 기준을 적용했습니다.
- 5. 모든 검증 산출물, 증명 및 Python 구현을 공개적으로 제공하고 있습니다.


---

*Generated on 2025-09-25 15:19:46*