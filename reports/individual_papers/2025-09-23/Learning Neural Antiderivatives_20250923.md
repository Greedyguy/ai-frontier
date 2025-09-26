---
keywords:
  - Neural Fields
  - Repeated Antiderivatives
  - Summed-Area Tables
  - Differential and Integral Operators
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17755
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:56:31.424187",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Fields",
    "Repeated Antiderivatives",
    "Summed-Area Tables",
    "Differential and Integral Operators"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Fields": 0.78,
    "Repeated Antiderivatives": 0.79,
    "Summed-Area Tables": 0.75,
    "Differential and Integral Operators": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural Fields",
        "canonical": "Neural Fields",
        "aliases": [
          "Continuous Neural Representations"
        ],
        "category": "unique_technical",
        "rationale": "Neural fields represent a novel approach to continuous data representation, which is crucial for linking advancements in neural network architectures.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Repeated Antiderivatives",
        "canonical": "Repeated Antiderivatives",
        "aliases": [
          "Cumulative Integration"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's contribution and connects to mathematical operations in neural networks.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.79
      },
      {
        "surface": "Summed-Area Tables",
        "canonical": "Summed-Area Tables",
        "aliases": [
          "Integral Image"
        ],
        "category": "specific_connectable",
        "rationale": "Summed-area tables are a well-known technique in computer graphics, providing a bridge to traditional methods.",
        "novelty_score": 0.55,
        "connectivity_score": 0.72,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Differential and Integral Operators",
        "canonical": "Differential and Integral Operators",
        "aliases": [
          "Calculus Operators"
        ],
        "category": "broad_technical",
        "rationale": "These operators are fundamental in mathematical modeling and are relevant to the paper's focus on integration.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "visual computing",
      "grids",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural Fields",
      "resolved_canonical": "Neural Fields",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Repeated Antiderivatives",
      "resolved_canonical": "Repeated Antiderivatives",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Summed-Area Tables",
      "resolved_canonical": "Summed-Area Tables",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.72,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Differential and Integral Operators",
      "resolved_canonical": "Differential and Integral Operators",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Learning Neural Antiderivatives

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17755.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17755](https://arxiv.org/abs/2509.17755)

## 🔗 유사한 논문
- [[2025-09-22/Geometric Integration for Neural Control Variates_20250922|Geometric Integration for Neural Control Variates]] (81.4% similar)
- [[2025-09-17/A Variational Framework for Residual-Based Adaptivity in Neural PDE Solvers and Operator Learning_20250917|A Variational Framework for Residual-Based Adaptivity in Neural PDE Solvers and Operator Learning]] (81.1% similar)
- [[2025-09-22/Stochastic Sample Approximations of (Local) Moduli of Continuity_20250922|Stochastic Sample Approximations of (Local) Moduli of Continuity]] (80.5% similar)
- [[2025-09-22/Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception_20250922|Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception]] (80.3% similar)
- [[2025-09-23/Comprehensive Review of Neural Differential Equations for Time Series Analysis_20250923|Comprehensive Review of Neural Differential Equations for Time Series Analysis]] (79.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Differential and Integral Operators|Differential and Integral Operators]]
**🔗 Specific Connectable**: [[keywords/Summed-Area Tables|Summed-Area Tables]]
**⚡ Unique Technical**: [[keywords/Neural Fields|Neural Fields]], [[keywords/Repeated Antiderivatives|Repeated Antiderivatives]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17755v1 Announce Type: new 
Abstract: Neural fields offer continuous, learnable representations that extend beyond traditional discrete formats in visual computing. We study the problem of learning neural representations of repeated antiderivatives directly from a function, a continuous analogue of summed-area tables. Although widely used in discrete domains, such cumulative schemes rely on grids, which prevents their applicability in continuous neural contexts. We introduce and analyze a range of neural methods for repeated integration, including both adaptations of prior work and novel designs. Our evaluation spans multiple input dimensionalities and integration orders, assessing both reconstruction quality and performance in downstream tasks such as filtering and rendering. These results enable integrating classical cumulative operators into modern neural systems and offer insights into learning tasks involving differential and integral operators.

## 📝 요약

이 논문은 연속적이고 학습 가능한 표현을 제공하는 신경 필드를 연구하여, 함수로부터 반복적인 부정적분을 학습하는 문제를 다룹니다. 이는 전통적인 이산적 누적 영역 테이블의 연속적 유사체입니다. 기존의 누적 방식은 격자에 의존하여 연속적 신경 맥락에서의 적용이 어려웠습니다. 저자들은 반복적 적분을 위한 다양한 신경 방법을 제안하고 분석하였으며, 여러 입력 차원과 적분 차수에 걸쳐 평가를 수행했습니다. 이 연구는 필터링 및 렌더링과 같은 후속 작업에서의 재구성 품질과 성능을 평가하여, 고전적 누적 연산자를 현대 신경 시스템에 통합할 수 있는 가능성을 제시하고, 미분 및 적분 연산자를 포함한 학습 작업에 대한 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. 신경 필드는 전통적인 이산 형식을 넘어서는 연속적이고 학습 가능한 표현을 제공합니다.
- 2. 반복적인 적분의 신경 표현을 함수로부터 직접 학습하는 문제를 연구합니다.
- 3. 기존의 누적 방식은 격자에 의존하여 연속적인 신경 맥락에서의 적용이 어렵습니다.
- 4. 다양한 입력 차원과 적분 차수를 통해 재구성 품질과 필터링 및 렌더링과 같은 다운스트림 작업에서의 성능을 평가합니다.
- 5. 고전적인 누적 연산자를 현대 신경 시스템에 통합할 수 있는 가능성을 제시하고, 미분 및 적분 연산자를 포함하는 학습 작업에 대한 통찰을 제공합니다.


---

*Generated on 2025-09-24 01:56:31*