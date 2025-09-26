<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:37:29.566680",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Probabilistic Logic Programming",
    "Distribution Semantics",
    "Belief Functions",
    "Interval Probabilities",
    "Computer Vision"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Probabilistic Logic Programming": 0.75,
    "Distribution Semantics": 0.78,
    "Belief Functions": 0.77,
    "Interval Probabilities": 0.72,
    "Computer Vision": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Probabilistic Logic Programming",
        "canonical": "Probabilistic Logic Programming",
        "aliases": [
          "PLP"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific approach to reasoning under uncertainty, which is central to the paper's contribution.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Distribution Semantics",
        "canonical": "Distribution Semantics",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A core concept in the paper, essential for understanding the proposed extensions.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Belief Functions",
        "canonical": "Belief Functions",
        "aliases": [
          "belief measures"
        ],
        "category": "specific_connectable",
        "rationale": "Introduces a way to handle epistemic uncertainty, which is a key innovation in the paper.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Interval Probabilities",
        "canonical": "Interval Probabilities",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A novel concept introduced to address epistemic uncertainty in the framework.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      },
      {
        "surface": "Computer Vision",
        "canonical": "Computer Vision",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Mentioned as an application area, linking the paper to a broader field of study.",
        "novelty_score": 0.3,
        "connectivity_score": 0.85,
        "specificity_score": 0.5,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "Prolog",
      "Python",
      "library",
      "implementation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Probabilistic Logic Programming",
      "resolved_canonical": "Probabilistic Logic Programming",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Distribution Semantics",
      "resolved_canonical": "Distribution Semantics",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Belief Functions",
      "resolved_canonical": "Belief Functions",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Interval Probabilities",
      "resolved_canonical": "Interval Probabilities",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Computer Vision",
      "resolved_canonical": "Computer Vision",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.85,
        "specificity": 0.5,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Integrating Belief Domains into Probabilistic Logic Programs

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2507.17291.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2507.17291](https://arxiv.org/abs/2507.17291)

## 🔗 유사한 논문
- [[2025-09-23/Information Fusion Using Transferable Belief Functions Implemented on Quantum Circuits_20250923|Information Fusion Using Transferable Belief Functions Implemented on Quantum Circuits]] (79.3% similar)
- [[2025-09-22/FSLI_ An Interpretable Formal Semantic System for One-Dimensional Ordering Inference_20250922|FSLI: An Interpretable Formal Semantic System for One-Dimensional Ordering Inference]] (78.1% similar)
- [[2025-09-22/DivLogicEval_ A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models_20250922|DivLogicEval: A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models]] (77.8% similar)
- [[2025-09-22/Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows_20250922|Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows]] (77.8% similar)
- [[2025-09-23/Canonical Representations of Markovian Structural Causal Models_ A Framework for Counterfactual Reasoning_20250923|Canonical Representations of Markovian Structural Causal Models: A Framework for Counterfactual Reasoning]] (77.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Computer Vision|Computer Vision]]
**🔗 Specific Connectable**: [[keywords/Belief Functions|Belief Functions]]
**⚡ Unique Technical**: [[keywords/Probabilistic Logic Programming|Probabilistic Logic Programming]], [[keywords/Distribution Semantics|Distribution Semantics]], [[keywords/Interval Probabilities|Interval Probabilities]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.17291v2 Announce Type: replace-cross 
Abstract: Probabilistic Logic Programming (PLP) under the Distribution Semantics is a leading approach to practical reasoning under uncertainty. An advantage of the Distribution Semantics is its suitability for implementation as a Prolog or Python library, available through two well-maintained implementations, namely ProbLog and cplint/PITA. However, current formulations of the Distribution Semantics use point-probabilities, making it difficult to express epistemic uncertainty, such as arises from, for example, hierarchical classifications from computer vision models. Belief functions generalize probability measures as non-additive capacities, and address epistemic uncertainty via interval probabilities. This paper introduces interval-based Capacity Logic Programs based on an extension of the Distribution Semantics to include belief functions, and describes properties of the new framework that make it amenable to practical applications.

## 📝 요약

이 논문은 불확실성 하에서의 실용적 추론을 위한 확률 논리 프로그래밍(PLP)의 새로운 접근법을 제안합니다. 기존의 분포 의미론은 점 확률을 사용하여 인식론적 불확실성을 표현하는 데 한계가 있었습니다. 이를 해결하기 위해, 이 논문은 신념 함수를 포함한 분포 의미론의 확장을 통해 간격 기반 용량 논리 프로그램을 도입합니다. 이 새로운 프레임워크는 비가산 용량으로 확률 측정을 일반화하여 간격 확률을 통해 인식론적 불확실성을 다룹니다. 이러한 접근법은 실용적 응용에 적합한 특성을 지니고 있습니다.

## 🎯 주요 포인트

- 1. 분포 의미론 하의 확률 논리 프로그래밍(PLP)은 불확실성 하에서의 실용적 추론을 위한 주요 접근 방식이다.
- 2. 분포 의미론은 Prolog 또는 Python 라이브러리로 구현하기에 적합하며, ProbLog와 cplint/PITA라는 두 가지 잘 유지되는 구현을 통해 제공된다.
- 3. 현재의 분포 의미론은 점 확률을 사용하여 인식 불확실성을 표현하기 어렵다.
- 4. 신념 함수는 비가산 용량으로 확률 측정을 일반화하고, 구간 확률을 통해 인식 불확실성을 해결한다.
- 5. 본 논문은 신념 함수를 포함하도록 분포 의미론을 확장한 구간 기반 용량 논리 프로그램을 소개하고, 실용적 응용에 적합한 새로운 프레임워크의 특성을 설명한다.


---

*Generated on 2025-09-24 14:37:29*