---
keywords:
  - Neural Algorithmic Reasoning
  - Knapsack Problem
  - Dynamic Programming
  - Combinatorial Optimization
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15239
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T08:43:07.435378",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Algorithmic Reasoning",
    "Knapsack Problem",
    "Dynamic Programming",
    "Combinatorial Optimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Algorithmic Reasoning": 0.78,
    "Knapsack Problem": 0.85,
    "Dynamic Programming": 0.8,
    "Combinatorial Optimization": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural Algorithmic Reasoning",
        "canonical": "Neural Algorithmic Reasoning",
        "aliases": [
          "NAR"
        ],
        "category": "unique_technical",
        "rationale": "This term represents a specialized intersection of neural networks and algorithmic logic, crucial for understanding the paper's contribution.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Knapsack Problem",
        "canonical": "Knapsack Problem",
        "aliases": [
          "Knapsack"
        ],
        "category": "specific_connectable",
        "rationale": "The Knapsack Problem is a central theme of the paper and a well-known problem in combinatorial optimization, facilitating connections to related works.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Dynamic Programming",
        "canonical": "Dynamic Programming",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Dynamic Programming is a fundamental technique used in the paper's approach, relevant for linking to algorithmic strategies.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Combinatorial Optimization",
        "canonical": "Combinatorial Optimization",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "This is a key area of application for the paper's methods, providing a bridge to other optimization problems.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.65,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "pseudo-polynomial",
      "pipeline"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural Algorithmic Reasoning",
      "resolved_canonical": "Neural Algorithmic Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Knapsack Problem",
      "resolved_canonical": "Knapsack Problem",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Dynamic Programming",
      "resolved_canonical": "Dynamic Programming",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Combinatorial Optimization",
      "resolved_canonical": "Combinatorial Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.65,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# KNARsack: Teaching Neural Algorithmic Reasoners to Solve Pseudo-Polynomial Problems

**Korean Title:** KNARsack: 신경 알고리즘 추론자를 가르쳐 의사다항식 문제 해결하기

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15239.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15239](https://arxiv.org/abs/2509.15239)

## 🔗 유사한 논문
- [[2025-09-22/SPaRC_ A Spatial Pathfinding Reasoning Challenge_20250922|SPaRC: A Spatial Pathfinding Reasoning Challenge]] (80.2% similar)
- [[2025-09-22/Neural Architecture Search Algorithms for Quantum Autoencoders_20250922|Neural Architecture Search Algorithms for Quantum Autoencoders]] (78.7% similar)
- [[2025-09-22/Latent learning_ episodic memory complements parametric learning by enabling flexible reuse of experiences_20250922|Latent learning: episodic memory complements parametric learning by enabling flexible reuse of experiences]] (78.5% similar)
- [[2025-09-22/PVPO_ Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning_20250922|PVPO: Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning]] (78.3% similar)
- [[2025-09-22/Walk and Read Less_ Improving the Efficiency of Vision-and-Language Navigation via Tuning-Free Multimodal Token Pruning_20250922|Walk and Read Less: Improving the Efficiency of Vision-and-Language Navigation via Tuning-Free Multimodal Token Pruning]] (77.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Dynamic Programming|Dynamic Programming]], [[keywords/Combinatorial Optimization|Combinatorial Optimization]]
**🔗 Specific Connectable**: [[keywords/Knapsack Problem|Knapsack Problem]]
**⚡ Unique Technical**: [[keywords/Neural Algorithmic Reasoning|Neural Algorithmic Reasoning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15239v1 Announce Type: new 
Abstract: Neural algorithmic reasoning (NAR) is a growing field that aims to embed algorithmic logic into neural networks by imitating classical algorithms. In this extended abstract, we detail our attempt to build a neural algorithmic reasoner that can solve Knapsack, a pseudo-polynomial problem bridging classical algorithms and combinatorial optimisation, but omitted in standard NAR benchmarks. Our neural algorithmic reasoner is designed to closely follow the two-phase pipeline for the Knapsack problem, which involves first constructing the dynamic programming table and then reconstructing the solution from it. The approach, which models intermediate states through dynamic programming supervision, achieves better generalization to larger problem instances than a direct-prediction baseline that attempts to select the optimal subset only from the problem inputs.

## 🔍 Abstract (한글 번역)

arXiv:2509.15239v1 발표 유형: 신규  
초록: 신경 알고리즘적 추론(NAR)은 고전 알고리즘을 모방하여 알고리즘적 논리를 신경망에 내재화하려는 성장하는 분야입니다. 이 확장 초록에서는 고전 알고리즘과 조합 최적화를 연결하는 의사다항식 문제인 배낭 문제를 해결할 수 있는 신경 알고리즘적 추론기를 구축하려는 시도를 자세히 설명합니다. 배낭 문제는 표준 NAR 벤치마크에서 생략되었습니다. 우리의 신경 알고리즘적 추론기는 배낭 문제를 해결하기 위한 2단계 파이프라인을 충실히 따르도록 설계되었습니다. 이 파이프라인은 먼저 동적 프로그래밍 테이블을 구성한 다음 이를 통해 솔루션을 재구성하는 과정을 포함합니다. 동적 프로그래밍 감독을 통해 중간 상태를 모델링하는 이 접근 방식은 문제 입력에서 최적의 부분 집합을 선택하려는 직접 예측 기준선보다 더 큰 문제 인스턴스에 대한 일반화를 더 잘 수행합니다.

## 📝 요약

이 논문은 신경 알고리즘적 추론(NAR)을 활용하여 배낭 문제(Knapsack)를 해결하는 신경 알고리즘 추론기를 개발하는 연구를 다룹니다. 배낭 문제는 고전 알고리즘과 조합 최적화 사이의 가교 역할을 하는 문제로, 기존 NAR 벤치마크에는 포함되지 않았습니다. 연구진은 배낭 문제를 해결하기 위해 동적 프로그래밍 테이블을 구성하고 이를 통해 해를 재구성하는 두 단계 파이프라인을 따르는 신경 알고리즘 추론기를 설계했습니다. 이 방법론은 문제 입력만을 기반으로 최적 부분집합을 선택하려는 직접 예측 방식보다 더 큰 문제 사례에 대한 일반화 성능이 우수한 것으로 나타났습니다.

## 🎯 주요 포인트

- 1. 신경 알고리즘적 추론(NAR)은 고전 알고리즘을 모방하여 알고리즘적 논리를 신경망에 내재화하는 것을 목표로 하는 성장하는 분야이다.
- 2. 본 연구에서는 Knapsack 문제를 해결할 수 있는 신경 알고리즘 추론기를 구축하려는 시도를 상세히 설명한다.
- 3. Knapsack 문제 해결을 위한 신경 알고리즘 추론기는 동적 프로그래밍 테이블을 구성하고 이를 통해 솔루션을 재구성하는 두 단계 파이프라인을 따르도록 설계되었다.
- 4. 동적 프로그래밍 감독을 통해 중간 상태를 모델링하는 접근 방식은 문제 입력에서 최적의 부분 집합을 직접 예측하려는 기준선보다 더 큰 문제 사례에 대한 일반화 성능이 우수하다.


---

*Generated on 2025-09-23 08:43:07*