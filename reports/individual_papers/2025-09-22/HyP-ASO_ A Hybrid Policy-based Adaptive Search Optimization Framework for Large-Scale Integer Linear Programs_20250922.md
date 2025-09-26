---
keywords:
  - Integer Linear Programs
  - Large Neighborhood Search
  - Reinforcement Learning
  - Adaptive Search Optimization
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15828
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:36:00.684425",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Integer Linear Programs",
    "Large Neighborhood Search",
    "Reinforcement Learning",
    "Adaptive Search Optimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Integer Linear Programs": 0.78,
    "Large Neighborhood Search": 0.77,
    "Reinforcement Learning": 0.82,
    "Adaptive Search Optimization": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Integer Linear Programs",
        "canonical": "Integer Linear Programs",
        "aliases": [
          "ILPs"
        ],
        "category": "unique_technical",
        "rationale": "Key focus of the paper, essential for understanding the optimization context.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Neighborhood Search",
        "canonical": "Large Neighborhood Search",
        "aliases": [
          "LNS"
        ],
        "category": "unique_technical",
        "rationale": "Central to the proposed framework and its comparison with existing methods.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Integral to the framework's policy-based approach, linking to broader AI concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Adaptive Search Optimization",
        "canonical": "Adaptive Search Optimization",
        "aliases": [
          "ASO"
        ],
        "category": "unique_technical",
        "rationale": "Describes the novel approach of the framework, highlighting its adaptive nature.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "formula",
      "experiments",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Integer Linear Programs",
      "resolved_canonical": "Integer Linear Programs",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Neighborhood Search",
      "resolved_canonical": "Large Neighborhood Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Adaptive Search Optimization",
      "resolved_canonical": "Adaptive Search Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# HyP-ASO: A Hybrid Policy-based Adaptive Search Optimization Framework for Large-Scale Integer Linear Programs

**Korean Title:** HyP-ASO: 대규모 정수 선형 프로그램을 위한 하이브리드 정책 기반 적응형 탐색 최적화 프레임워크

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15828.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15828](https://arxiv.org/abs/2509.15828)

## 🔗 유사한 논문
- [[2025-09-22/Momentum-constrained Hybrid Heuristic Trajectory Optimization Framework with Residual-enhanced DRL for Visually Impaired Scenarios_20250922|Momentum-constrained Hybrid Heuristic Trajectory Optimization Framework with Residual-enhanced DRL for Visually Impaired Scenarios]] (79.9% similar)
- [[2025-09-22/PVPO_ Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning_20250922|PVPO: Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning]] (79.9% similar)
- [[2025-09-22/Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning_20250922|Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning]] (79.9% similar)
- [[2025-09-22/Gaussian process policy iteration with additive Schwarz acceleration for forward and inverse HJB and mean field game problems_20250922|Gaussian process policy iteration with additive Schwarz acceleration for forward and inverse HJB and mean field game problems]] (79.9% similar)
- [[2025-09-22/Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization_20250922|Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization]] (79.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Integer Linear Programs|Integer Linear Programs]], [[keywords/Large Neighborhood Search|Large Neighborhood Search]], [[keywords/Adaptive Search Optimization|Adaptive Search Optimization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15828v1 Announce Type: new 
Abstract: Directly solving large-scale Integer Linear Programs (ILPs) using traditional solvers is slow due to their NP-hard nature. While recent frameworks based on Large Neighborhood Search (LNS) can accelerate the solving process, their performance is often constrained by the difficulty in generating sufficiently effective neighborhoods. To address this challenge, we propose HyP-ASO, a hybrid policy-based adaptive search optimization framework that combines a customized formula with deep Reinforcement Learning (RL). The formula leverages feasible solutions to calculate the selection probabilities for each variable in the neighborhood generation process, and the RL policy network predicts the neighborhood size. Extensive experiments demonstrate that HyP-ASO significantly outperforms existing LNS-based approaches for large-scale ILPs. Additional experiments show it is lightweight and highly scalable, making it well-suited for solving large-scale ILPs.

## 🔍 Abstract (한글 번역)

arXiv:2509.15828v1 발표 유형: 신규  
초록: 전통적인 해결기를 사용하여 대규모 정수 선형 계획법(ILP)을 직접 해결하는 것은 NP-난해성 때문에 느립니다. 최근의 대규모 이웃 탐색(LNS)을 기반으로 한 프레임워크는 해결 과정을 가속화할 수 있지만, 충분히 효과적인 이웃을 생성하는 데 어려움이 있어 성능이 종종 제한됩니다. 이 문제를 해결하기 위해, 우리는 맞춤형 수식과 심층 강화 학습(RL)을 결합한 하이브리드 정책 기반 적응 검색 최적화 프레임워크인 HyP-ASO를 제안합니다. 이 수식은 이웃 생성 과정에서 각 변수의 선택 확률을 계산하기 위해 가능한 해를 활용하며, RL 정책 네트워크는 이웃의 크기를 예측합니다. 광범위한 실험을 통해 HyP-ASO가 대규모 ILP에 대해 기존 LNS 기반 접근 방식을 크게 능가함을 보여줍니다. 추가 실험에서는 HyP-ASO가 경량화되어 있고 높은 확장성을 가지고 있어 대규모 ILP 해결에 적합함을 보여줍니다.

## 📝 요약

이 논문은 대규모 정수 선형 계획 문제(ILPs)를 효율적으로 해결하기 위해 HyP-ASO라는 하이브리드 정책 기반 적응 탐색 최적화 프레임워크를 제안합니다. HyP-ASO는 맞춤형 수식과 심층 강화 학습(RL)을 결합하여 이웃 생성 과정에서 각 변수의 선택 확률을 계산하고, RL 정책 네트워크가 이웃 크기를 예측합니다. 실험 결과, HyP-ASO는 기존의 대규모 LNS 기반 접근법보다 뛰어난 성능을 보였으며, 경량성과 확장성이 높아 대규모 ILPs 해결에 적합함을 입증했습니다.

## 🎯 주요 포인트

- 1. 전통적인 솔버로 대규모 정수 선형 계획 문제를 직접 해결하는 것은 NP-hard 특성 때문에 느리다.
- 2. 최근의 대규모 이웃 탐색(LNS) 기반 프레임워크는 해결 과정을 가속화할 수 있지만, 효과적인 이웃 생성의 어려움으로 성능이 제한된다.
- 3. HyP-ASO는 맞춤형 수식과 심층 강화 학습(RL)을 결합한 하이브리드 정책 기반 적응 탐색 최적화 프레임워크로, 이웃 생성 과정에서 각 변수의 선택 확률을 계산한다.
- 4. HyP-ASO는 대규모 정수 선형 계획 문제에서 기존의 LNS 기반 접근 방식을 능가하며, 경량성과 높은 확장성을 보여준다.
- 5. HyP-ASO는 대규모 정수 선형 계획 문제 해결에 적합하다.


---

*Generated on 2025-09-23 10:36:00*