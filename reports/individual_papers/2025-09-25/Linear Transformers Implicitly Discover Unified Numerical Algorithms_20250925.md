---
keywords:
  - Transformer
  - Nyström Extrapolation
  - In-Context Learning
  - Matrix Completion
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19702
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:45:36.695458",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Nyström Extrapolation",
    "In-Context Learning",
    "Matrix Completion"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Nyström Extrapolation": 0.7,
    "In-Context Learning": 0.82,
    "Matrix Completion": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "linear attention transformer",
        "canonical": "Transformer",
        "aliases": [
          "linear transformer",
          "attention transformer"
        ],
        "category": "broad_technical",
        "rationale": "Connects to the broader concept of Transformers, a key technology in machine learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Nyström extrapolation",
        "canonical": "Nyström Extrapolation",
        "aliases": [
          "Nyström method"
        ],
        "category": "unique_technical",
        "rationale": "A specialized technique in numerical analysis, relevant for linking to computational methods.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "in-context learning",
        "canonical": "In-Context Learning",
        "aliases": [],
        "category": "evolved_concepts",
        "rationale": "Represents a modern approach in machine learning that is gaining traction.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "masked-block matrix completion",
        "canonical": "Matrix Completion",
        "aliases": [
          "block matrix completion"
        ],
        "category": "specific_connectable",
        "rationale": "A specific task that can be linked to broader matrix operations and algorithms.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "full visibility",
      "distributed computation",
      "rank-limited updates"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "linear attention transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Nyström extrapolation",
      "resolved_canonical": "Nyström Extrapolation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "in-context learning",
      "resolved_canonical": "In-Context Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "masked-block matrix completion",
      "resolved_canonical": "Matrix Completion",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Linear Transformers Implicitly Discover Unified Numerical Algorithms

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19702.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19702](https://arxiv.org/abs/2509.19702)

## 🔗 유사한 논문
- [[2025-09-23/Scaling Efficient LLMs_20250923|Scaling Efficient LLMs]] (84.3% similar)
- [[2025-09-23/Inceptive Transformers_ Enhancing Contextual Representations through Multi-Scale Feature Learning Across Domains and Languages_20250923|Inceptive Transformers: Enhancing Contextual Representations through Multi-Scale Feature Learning Across Domains and Languages]] (83.2% similar)
- [[2025-09-24/Spectraformer_ A Unified Random Feature Framework for Transformer_20250924|Spectraformer: A Unified Random Feature Framework for Transformer]] (83.2% similar)
- [[2025-09-22/Hierarchical Self-Attention_ Generalizing Neural Attention Mechanics to Multi-Scale Problems_20250922|Hierarchical Self-Attention: Generalizing Neural Attention Mechanics to Multi-Scale Problems]] (83.0% similar)
- [[2025-09-23/Measure-to-measure interpolation using Transformers_20250923|Measure-to-measure interpolation using Transformers]] (82.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Matrix Completion|Matrix Completion]]
**⚡ Unique Technical**: [[keywords/Nyström Extrapolation|Nyström Extrapolation]]
**🚀 Evolved Concepts**: [[keywords/In-Context Learning|In-Context Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19702v1 Announce Type: cross 
Abstract: We train a linear attention transformer on millions of masked-block matrix completion tasks: each prompt is masked low-rank matrix whose missing block may be (i) a scalar prediction target or (ii) an unseen kernel slice of Nystr\"om extrapolation. The model sees only input-output pairs and a mean-squared loss; it is given no normal equations, no handcrafted iterations, and no hint that the tasks are related. Surprisingly, after training, algebraic unrolling reveals the same parameter-free update rule across three distinct computational regimes (full visibility, rank-limited updates, and distributed computation). We prove that this rule achieves second-order convergence on full-batch problems, cuts distributed iteration complexity, and remains accurate with rank-limited attention. Thus, a transformer trained solely to patch missing blocks implicitly discovers a unified, resource-adaptive iterative solver spanning prediction, estimation, and Nystr\"om extrapolation, highlighting a powerful capability of in-context learning.

## 📝 요약

이 논문에서는 수백만 개의 마스크된 블록 행렬 완성 작업을 통해 선형 주의 메커니즘을 가진 트랜스포머를 훈련했습니다. 모델은 입력-출력 쌍과 평균 제곱 오차만을 사용하며, 작업 간의 관계에 대한 정보 없이 학습합니다. 훈련 후, 대수적 전개를 통해 세 가지 계산 체제에서 동일한 매개변수 없는 업데이트 규칙이 발견되었습니다. 이 규칙은 전체 배치 문제에서 2차 수렴을 달성하고, 분산 계산의 복잡성을 줄이며, 제한된 랭크의 주의 메커니즘에서도 정확성을 유지합니다. 결과적으로, 이 트랜스포머는 예측, 추정, 그리고 Nyström 외삽을 아우르는 통합적이고 자원 적응적인 반복 솔버를 암묵적으로 발견했음을 보여줍니다.

## 🎯 주요 포인트

- 1. 선형 주의 변환기는 수백만 개의 마스크된 블록 행렬 완성 작업을 통해 훈련되었습니다.
- 2. 모델은 입력-출력 쌍과 평균 제곱 손실만을 사용하여 훈련되며, 관련된 작업에 대한 힌트 없이도 학습합니다.
- 3. 훈련 후, 대수적 전개를 통해 세 가지 계산 체제에서 동일한 매개변수 없는 업데이트 규칙이 발견되었습니다.
- 4. 이 규칙은 전체 배치 문제에서 2차 수렴을 달성하고, 분산 반복 복잡성을 줄이며, 랭크 제한 주의에서도 정확성을 유지합니다.
- 5. 이 연구는 예측, 추정 및 Nystr\"om 외삽을 아우르는 통합된 자원 적응형 반복 솔버를 암시적으로 발견하는 변환기의 강력한 능력을 강조합니다.


---

*Generated on 2025-09-25 15:45:36*