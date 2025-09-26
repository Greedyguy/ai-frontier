---
keywords:
  - Neural Network
  - Piecewise Linear Activation
  - Extension Complexity
  - Virtual Extension Complexity
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2411.03006
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:56:55.324667",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Piecewise Linear Activation",
    "Extension Complexity",
    "Virtual Extension Complexity"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.85,
    "Piecewise Linear Activation": 0.78,
    "Extension Complexity": 0.82,
    "Virtual Extension Complexity": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "NN",
          "Neural Nets"
        ],
        "category": "broad_technical",
        "rationale": "Neural networks are central to the discussion and connect with a wide range of machine learning topics.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Piecewise Linear Activation Functions",
        "canonical": "Piecewise Linear Activation",
        "aliases": [
          "ReLU",
          "Maxout"
        ],
        "category": "specific_connectable",
        "rationale": "These activation functions are fundamental to the architecture of neural networks discussed in the paper.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Extension Complexity",
        "canonical": "Extension Complexity",
        "aliases": [
          "xc(P)"
        ],
        "category": "unique_technical",
        "rationale": "This concept is crucial for understanding the theoretical limits of neural network size.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      },
      {
        "surface": "Virtual Extension Complexity",
        "canonical": "Virtual Extension Complexity",
        "aliases": [
          "vxc(P)"
        ],
        "category": "unique_technical",
        "rationale": "Introduced in the paper, this concept generalizes extension complexity and is key to the research findings.",
        "novelty_score": 0.9,
        "connectivity_score": 0.55,
        "specificity_score": 0.95,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "linear program",
      "inequalities",
      "polytope"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Piecewise Linear Activation Functions",
      "resolved_canonical": "Piecewise Linear Activation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Extension Complexity",
      "resolved_canonical": "Extension Complexity",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Virtual Extension Complexity",
      "resolved_canonical": "Virtual Extension Complexity",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.55,
        "specificity": 0.95,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Neural Networks and (Virtual) Extended Formulations

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2411.03006.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2411.03006](https://arxiv.org/abs/2411.03006)

## 🔗 유사한 논문
- [[2025-09-23/Virtual Arc Consistency for Linear Constraints inCost Function Networks_20250923|Virtual Arc Consistency for Linear Constraints inCost Function Networks]] (80.3% similar)
- [[2025-09-23/Regularizing Extrapolation in Causal Inference_20250923|Regularizing Extrapolation in Causal Inference]] (79.7% similar)
- [[2025-09-23/Unified Framework for Pre-trained Neural Network Compression via Decomposition and Optimized Rank Selection_20250923|Unified Framework for Pre-trained Neural Network Compression via Decomposition and Optimized Rank Selection]] (79.4% similar)
- [[2025-09-23/Checking extracted rules in Neural Networks_20250923|Checking extracted rules in Neural Networks]] (79.3% similar)
- [[2025-09-23/Deep Hierarchical Learning with Nested Subspace Networks_20250923|Deep Hierarchical Learning with Nested Subspace Networks]] (79.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Piecewise Linear Activation|Piecewise Linear Activation]]
**⚡ Unique Technical**: [[keywords/Extension Complexity|Extension Complexity]], [[keywords/Virtual Extension Complexity|Virtual Extension Complexity]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2411.03006v3 Announce Type: replace-cross 
Abstract: Neural networks with piecewise linear activation functions, such as rectified linear units (ReLU) or maxout, are among the most fundamental models in modern machine learning. We make a step towards proving lower bounds on the size of such neural networks by linking their representative capabilities to the notion of the extension complexity $\mathrm{xc}(P)$ of a polytope $P$. This is a well-studied quantity in combinatorial optimization and polyhedral geometry describing the number of inequalities needed to model $P$ as a linear program. We show that $\mathrm{xc}(P)$ is a lower bound on the size of any monotone or input-convex neural network that solves the linear optimization problem over $P$. This implies exponential lower bounds on such neural networks for a variety of problems, including the polynomially solvable maximum weight matching problem.
  In an attempt to prove similar bounds also for general neural networks, we introduce the notion of virtual extension complexity $\mathrm{vxc}(P)$, which generalizes $\mathrm{xc}(P)$ and describes the number of inequalities needed to represent the linear optimization problem over $P$ as a difference of two linear programs. We prove that $\mathrm{vxc}(P)$ is a lower bound on the size of any neural network that optimizes over $P$. While it remains an open question to derive useful lower bounds on $\mathrm{vxc}(P)$, we argue that this quantity deserves to be studied independently from neural networks by proving that one can efficiently optimize over a polytope $P$ using a small virtual extended formulation.

## 📝 요약

이 논문은 조각별 선형 활성화 함수를 사용하는 신경망(예: ReLU, maxout)의 크기에 대한 하한을 증명하기 위해 다면체 $P$의 확장 복잡성 $\mathrm{xc}(P)$와의 관계를 연구합니다. $\mathrm{xc}(P)$는 선형 프로그램으로 $P$를 모델링하는 데 필요한 부등식의 수를 나타내며, 이는 조합 최적화 및 다면체 기하학에서 잘 연구된 개념입니다. 저자들은 $\mathrm{xc}(P)$가 $P$에 대한 선형 최적화 문제를 해결하는 단조 또는 입력-볼록 신경망의 크기에 대한 하한임을 증명하고, 이를 통해 다양한 문제에 대한 신경망의 크기에 대한 지수적 하한을 도출합니다. 또한, 일반 신경망에 대한 유사한 하한을 증명하기 위해 가상 확장 복잡성 $\mathrm{vxc}(P)$를 도입하고, 이는 $P$에 대한 선형 최적화 문제를 두 개의 선형 프로그램의 차이로 나타내는 데 필요한 부등식의 수를 설명합니다. $\mathrm{vxc}(P)$가 $P$에 대해 최적화하는 신경망의 크기에 대한 하한임을 증명하며, 이 개념이 신경망과 독립적으로 연구될 가치가 있음을 주장합니다.

## 🎯 주요 포인트

- 1. 조각별 선형 활성화 함수(ReLU, maxout 등)를 사용하는 신경망의 크기에 대한 하한을 증명하기 위해 다면체 $P$의 확장 복잡성 $\mathrm{xc}(P)$ 개념과 연결했습니다.
- 2. $\mathrm{xc}(P)$는 $P$를 선형 프로그램으로 모델링하는 데 필요한 부등식의 수를 설명하며, 이는 단조 또는 입력-볼록 신경망의 크기에 대한 하한이 됩니다.
- 3. 다양한 문제에 대해 이러한 신경망에 대한 지수적 하한을 암시하며, 여기에는 다항식적으로 해결 가능한 최대 가중치 매칭 문제도 포함됩니다.
- 4. 일반 신경망에 대한 유사한 하한을 증명하기 위해, 선형 최적화 문제를 두 개의 선형 프로그램의 차이로 표현하는 데 필요한 부등식의 수를 설명하는 가상 확장 복잡성 $\mathrm{vxc}(P)$ 개념을 도입했습니다.
- 5. $\mathrm{vxc}(P)$에 대한 유용한 하한을 도출하는 것은 여전히 미해결 문제이지만, 작은 가상 확장 형식을 사용하여 다면체 $P$에 대해 효율적으로 최적화할 수 있음을 증명했습니다.


---

*Generated on 2025-09-24 02:56:55*