---
keywords:
  - Large Language Model
  - Cognitive Atom
  - Olympiad-level Mathematical Reasoning
  - Graph Neural Network
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17318
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T22:58:15.338550",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Cognitive Atom",
    "Olympiad-level Mathematical Reasoning",
    "Graph Neural Network"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Cognitive Atom": 0.78,
    "Olympiad-level Mathematical Reasoning": 0.8,
    "Graph Neural Network": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Language Model"
        ],
        "category": "broad_technical",
        "rationale": "This term is central to the paper's focus on mathematical reasoning capabilities in AI.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Cognitive Atoms",
        "canonical": "Cognitive Atom",
        "aliases": [
          "CogAtom"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel concept for problem synthesis in mathematical reasoning.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Olympiad-level Mathematical Reasoning",
        "canonical": "Olympiad-level Mathematical Reasoning",
        "aliases": [
          "Olympiad Math Reasoning"
        ],
        "category": "unique_technical",
        "rationale": "Specifically targets the level of difficulty and reasoning depth the paper addresses.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Graph Structure",
        "canonical": "Graph Neural Network",
        "aliases": [
          "Graph Structure"
        ],
        "category": "specific_connectable",
        "rationale": "The paper's approach involves graph-based exploration, linking to existing graph neural network concepts.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "test-time scaling",
      "problem difficulty",
      "high-quality problems"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Cognitive Atoms",
      "resolved_canonical": "Cognitive Atom",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Olympiad-level Mathematical Reasoning",
      "resolved_canonical": "Olympiad-level Mathematical Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Graph Structure",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# CogAtom: From Cognitive Atoms to Olympiad-level Mathematical Reasoning in Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17318.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17318](https://arxiv.org/abs/2509.17318)

## 🔗 유사한 논문
- [[2025-09-19/Understanding the Thinking Process of Reasoning Models_ A Perspective from Schoenfeld's Episode Theory_20250919|Understanding the Thinking Process of Reasoning Models: A Perspective from Schoenfeld's Episode Theory]] (82.5% similar)
- [[2025-09-17/THOR_ Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning_20250917|THOR: Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning]] (82.2% similar)
- [[2025-09-23/Large Language Models as End-to-end Combinatorial Optimization Solvers_20250923|Large Language Models as End-to-end Combinatorial Optimization Solvers]] (82.1% similar)
- [[2025-09-22/Rethinking Molecule Synthesizability with Chain-of-Reaction_20250922|Rethinking Molecule Synthesizability with Chain-of-Reaction]] (81.0% similar)
- [[2025-09-23/SalaMAnder_ Shapley-based Mathematical Expression Attribution and Metric for Chain-of-Thought Reasoning_20250923|SalaMAnder: Shapley-based Mathematical Expression Attribution and Metric for Chain-of-Thought Reasoning]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Cognitive Atom|Cognitive Atom]], [[keywords/Olympiad-level Mathematical Reasoning|Olympiad-level Mathematical Reasoning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17318v1 Announce Type: new 
Abstract: Mathematical reasoning poses significant challenges for Large Language Models (LLMs) due to its demand for multi-step reasoning and abstract conceptual integration. While recent test-time scaling techniques rely heavily on high-quality, challenging problems, the scarcity of Olympiad-level math problems remains a bottleneck. We introduce CogAtom, a novel cognitive atom-based framework for synthesizing mathematically rigorous and cognitively diverse problems. Unlike prior approaches, CogAtom models problem construction as a process of selecting and recombining fundamental reasoning units, cognitive atoms, extracted from human-authored solutions. A diversity-promoting random walk algorithm enables exploration of the cognitive atom space, while a constraint-based recombination mechanism ensures logical soundness and structural validity. The combinatorial nature of the graph structure provides a near-infinite space of reasoning paths, and the walk algorithm systematically explores this space to achieve large-scale synthesis of high-quality problems; meanwhile, by controlling the number of cognitive atoms, we can precisely adjust problem difficulty, ensuring diversity, scalability, and controllability of the generated problems. Experimental results demonstrate that CogAtom outperforms existing methods in accuracy, reasoning depth, and diversity, generating problems that closely match the difficulty of AIME while exceeding it in structural variation. Our work offers a cognitively grounded pathway toward scalable, high-quality math problem generation.Our code is publicly available at https://github.com/Icarus-1111/CogAtom.

## 📝 요약

이 논문은 수학적 추론 문제를 생성하는 새로운 프레임워크인 CogAtom을 소개합니다. CogAtom은 인간이 작성한 솔루션에서 추출한 인지적 원자(cognitive atoms)를 선택하고 재조합하여 문제를 구성합니다. 이 과정에서 다양성을 촉진하는 랜덤 워크 알고리즘과 제약 기반의 재조합 메커니즘을 사용하여 논리적 일관성과 구조적 타당성을 보장합니다. 이를 통해 거의 무한한 추론 경로를 탐색하며 고품질의 수학 문제를 대규모로 생성할 수 있습니다. 실험 결과, CogAtom은 기존 방법보다 정확성, 추론 깊이, 다양성에서 우수하며, AIME 수준의 난이도를 가진 문제를 생성하면서도 구조적 다양성에서 뛰어납니다. 이 연구는 확장 가능하고 고품질의 수학 문제 생성에 기여합니다.

## 🎯 주요 포인트

- 1. CogAtom은 인간이 작성한 솔루션에서 추출한 인지적 원자들을 선택하고 재조합하여 수학 문제를 생성하는 새로운 프레임워크입니다.
- 2. 다양성을 촉진하는 랜덤 워크 알고리즘을 통해 인지적 원자 공간을 탐색하며, 제약 기반 재조합 메커니즘을 통해 논리적 타당성과 구조적 유효성을 보장합니다.
- 3. CogAtom은 문제의 난이도를 조절할 수 있어 생성된 문제의 다양성, 확장성, 제어 가능성을 보장합니다.
- 4. 실험 결과, CogAtom은 기존 방법들보다 정확성, 추론 깊이, 다양성 면에서 우수하며, AIME 수준의 난이도를 가진 문제를 생성합니다.
- 5. CogAtom의 코드는 공개되어 있으며, 이는 대규모 고품질 수학 문제 생성의 인지적으로 기반을 둔 경로를 제공합니다.


---

*Generated on 2025-09-23 22:58:15*