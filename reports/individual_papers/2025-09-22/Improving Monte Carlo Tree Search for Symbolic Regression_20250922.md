---
keywords:
  - Symbolic Regression
  - Monte Carlo Tree Search
  - Genetic Programming
  - Evolution-inspired State-jumping Actions
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15929
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:38:08.004509",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Symbolic Regression",
    "Monte Carlo Tree Search",
    "Genetic Programming",
    "Evolution-inspired State-jumping Actions"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Symbolic Regression": 0.8,
    "Monte Carlo Tree Search": 0.78,
    "Genetic Programming": 0.7,
    "Evolution-inspired State-jumping Actions": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Symbolic Regression",
        "canonical": "Symbolic Regression",
        "aliases": [
          "Symbolic Expression Discovery"
        ],
        "category": "unique_technical",
        "rationale": "This is a central concept in the paper, focusing on discovering mathematical expressions, which is unique and specific to the study.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Monte Carlo Tree Search",
        "canonical": "Monte Carlo Tree Search",
        "aliases": [
          "MCTS"
        ],
        "category": "specific_connectable",
        "rationale": "A key method discussed in the paper, relevant for linking to other works using this search strategy.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "Genetic Programming",
        "canonical": "Genetic Programming",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "A foundational approach in symbolic regression, providing context for the improvements proposed in the paper.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      },
      {
        "surface": "Evolution-inspired State-jumping Actions",
        "canonical": "Evolution-inspired State-jumping Actions",
        "aliases": [
          "State-jumping Actions",
          "Mutation and Crossover"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel technique introduced in the paper to enhance search efficiency, making it a unique contribution.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "efficiency",
      "benchmark",
      "datasets"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Symbolic Regression",
      "resolved_canonical": "Symbolic Regression",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Monte Carlo Tree Search",
      "resolved_canonical": "Monte Carlo Tree Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Genetic Programming",
      "resolved_canonical": "Genetic Programming",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Evolution-inspired State-jumping Actions",
      "resolved_canonical": "Evolution-inspired State-jumping Actions",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Improving Monte Carlo Tree Search for Symbolic Regression

**Korean Title:** 심볼릭 회귀를 위한 몬테카를로 트리 탐색의 개선

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15929.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15929](https://arxiv.org/abs/2509.15929)

## 🔗 유사한 논문
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (81.5% similar)
- [[2025-09-22/Nonconvex Regularization for Feature Selection in Reinforcement Learning_20250922|Nonconvex Regularization for Feature Selection in Reinforcement Learning]] (79.7% similar)
- [[2025-09-22/Deep Reinforcement Learning with Gradient Eligibility Traces_20250922|Deep Reinforcement Learning with Gradient Eligibility Traces]] (79.7% similar)
- [[2025-09-18/Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (79.6% similar)
- [[2025-09-22/Instance Generation for Meta-Black-Box Optimization through Latent Space Reverse Engineering_20250922|Instance Generation for Meta-Black-Box Optimization through Latent Space Reverse Engineering]] (78.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Genetic Programming|Genetic Programming]]
**🔗 Specific Connectable**: [[keywords/Monte Carlo Tree Search|Monte Carlo Tree Search]]
**⚡ Unique Technical**: [[keywords/Symbolic Regression|Symbolic Regression]], [[keywords/Evolution-inspired State-jumping Actions|Evolution-inspired State-jumping Actions]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15929v1 Announce Type: new 
Abstract: Symbolic regression aims to discover concise, interpretable mathematical expressions that satisfy desired objectives, such as fitting data, posing a highly combinatorial optimization problem. While genetic programming has been the dominant approach, recent efforts have explored reinforcement learning methods for improving search efficiency. Monte Carlo Tree Search (MCTS), with its ability to balance exploration and exploitation through guided search, has emerged as a promising technique for symbolic expression discovery. However, its traditional bandit strategies and sequential symbol construction often limit performance. In this work, we propose an improved MCTS framework for symbolic regression that addresses these limitations through two key innovations: (1) an extreme bandit allocation strategy tailored for identifying globally optimal expressions, with finite-time performance guarantees under polynomial reward decay assumptions; and (2) evolution-inspired state-jumping actions such as mutation and crossover, which enable non-local transitions to promising regions of the search space. These state-jumping actions also reshape the reward landscape during the search process, improving both robustness and efficiency. We conduct a thorough numerical study to the impact of these improvements and benchmark our approach against existing symbolic regression methods on a variety of datasets, including both ground-truth and black-box datasets. Our approach achieves competitive performance with state-of-the-art libraries in terms of recovery rate, attains favorable positions on the Pareto frontier of accuracy versus model complexity. Code is available at https://github.com/PKU-CMEGroup/MCTS-4-SR.

## 🔍 Abstract (한글 번역)

arXiv:2509.15929v1 발표 유형: 신규  
초록: 심볼릭 회귀는 데이터 적합과 같은 원하는 목표를 만족하는 간결하고 해석 가능한 수학적 표현을 발견하는 것을 목표로 하며, 이는 매우 조합적인 최적화 문제를 제기합니다. 유전 프로그래밍이 지배적인 접근 방식이었지만, 최근에는 검색 효율성을 향상시키기 위한 강화 학습 방법이 탐구되었습니다. 탐색을 안내하여 탐색과 활용의 균형을 맞출 수 있는 몬테카를로 트리 탐색(MCTS)은 심볼릭 표현 발견을 위한 유망한 기술로 부상했습니다. 그러나 전통적인 밴딧 전략과 순차적 심볼 구성은 종종 성능을 제한합니다. 본 연구에서는 이러한 제한을 해결하기 위해 두 가지 주요 혁신을 통해 심볼릭 회귀를 위한 개선된 MCTS 프레임워크를 제안합니다: (1) 다항 보상 감소 가정 하에서 유한 시간 성능 보장을 갖춘 전역 최적 표현을 식별하기 위한 극단적인 밴딧 할당 전략; (2) 탐색 공간의 유망한 영역으로의 비지역적 전환을 가능하게 하는 돌연변이 및 교차와 같은 진화 영감을 받은 상태 점프 동작. 이러한 상태 점프 동작은 검색 과정에서 보상 지형을 재구성하여 견고성과 효율성을 모두 향상시킵니다. 우리는 이러한 개선의 영향을 철저히 수치적으로 연구하고, 다양한 데이터셋(기준 데이터셋 및 블랙박스 데이터셋 포함)에서 기존 심볼릭 회귀 방법과 우리의 접근 방식을 비교 평가합니다. 우리의 접근 방식은 복구율 측면에서 최첨단 라이브러리와 경쟁력 있는 성능을 달성하며, 정확도 대 모델 복잡성의 파레토 전선에서 유리한 위치를 차지합니다. 코드는 https://github.com/PKU-CMEGroup/MCTS-4-SR에서 이용할 수 있습니다.

## 📝 요약

이 논문은 심볼릭 회귀 문제에서 기존의 유전 프로그래밍 대신 강화 학습을 활용하여 검색 효율성을 개선하는 방법을 제안합니다. 특히, 몬테카를로 트리 탐색(MCTS)의 전통적인 한계를 극복하기 위해 두 가지 혁신적인 방법을 도입했습니다. 첫째, 전역 최적 표현을 식별하기 위한 극단적 밴딧 할당 전략을 사용하여 성능을 보장합니다. 둘째, 진화에서 영감을 받은 상태 점프 액션(변이와 교차)을 도입하여 검색 공간의 유망한 영역으로의 비지역적 전환을 가능하게 합니다. 이러한 방법들은 검색 과정에서 보상 지형을 재구성하여 강건성과 효율성을 향상시킵니다. 다양한 데이터셋에서의 실험 결과, 제안된 방법은 최신 라이브러리와 비교하여 경쟁력 있는 성능을 보이며, 정확도와 모델 복잡성의 파레토 경계에서 유리한 위치를 차지합니다.

## 🎯 주요 포인트

- 1. 본 연구는 심볼릭 회귀 문제 해결을 위한 개선된 몬테카를로 트리 탐색(MCTS) 프레임워크를 제안합니다.
- 2. 제안된 MCTS 프레임워크는 극단적인 밴딧 할당 전략과 진화적 상태 점프 액션을 통해 전통적인 성능 제한을 극복합니다.
- 3. 상태 점프 액션은 탐색 공간의 유망한 영역으로의 비지역적 전환을 가능하게 하여 탐색 과정의 보상 지형을 재구성합니다.
- 4. 다양한 데이터셋에서 기존 심볼릭 회귀 방법과 비교한 결과, 제안된 접근법은 회복률과 모델 복잡성 대비 정확성에서 경쟁력 있는 성능을 보였습니다.
- 5. 연구 결과는 심볼릭 회귀 문제에서 탐색 효율성을 향상시키는 데 있어 강화 학습 방법의 가능성을 시사합니다.


---

*Generated on 2025-09-23 10:38:08*