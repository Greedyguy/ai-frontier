---
keywords:
  - Transferable Belief Model
  - Quantum Circuits
  - Belief Functions
  - Quantum Computing
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2410.08949
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:23:02.136485",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transferable Belief Model",
    "Quantum Circuits",
    "Belief Functions",
    "Quantum Computing"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transferable Belief Model": 0.78,
    "Quantum Circuits": 0.8,
    "Belief Functions": 0.77,
    "Quantum Computing": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "transferable belief model",
        "canonical": "Transferable Belief Model",
        "aliases": [
          "TBM"
        ],
        "category": "unique_technical",
        "rationale": "The transferable belief model is central to the paper's approach and offers a unique perspective on belief transfer in quantum computing.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "quantum circuits",
        "canonical": "Quantum Circuits",
        "aliases": [
          "Quantum Circuit"
        ],
        "category": "broad_technical",
        "rationale": "Quantum circuits are a fundamental component of the implementation discussed, linking quantum computing with belief functions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "belief functions",
        "canonical": "Belief Functions",
        "aliases": [
          "Belief Function"
        ],
        "category": "specific_connectable",
        "rationale": "Belief functions are a key element in the paper, providing an alternative to Bayesian approaches in quantum computing.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      },
      {
        "surface": "quantum computing",
        "canonical": "Quantum Computing",
        "aliases": [
          "Quantum Computation"
        ],
        "category": "broad_technical",
        "rationale": "Quantum computing is the broader context within which the transferable belief model is applied, crucial for understanding the paper's scope.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "Dempster-Shafer theory",
      "Bayesian approach"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "transferable belief model",
      "resolved_canonical": "Transferable Belief Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "quantum circuits",
      "resolved_canonical": "Quantum Circuits",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "belief functions",
      "resolved_canonical": "Belief Functions",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "quantum computing",
      "resolved_canonical": "Quantum Computing",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Information Fusion Using Transferable Belief Functions Implemented on Quantum Circuits

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2410.08949.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2410.08949](https://arxiv.org/abs/2410.08949)

## 🔗 유사한 논문
- [[2025-09-23/On the Variational Costs of Changing Our Minds_20250923|On the Variational Costs of Changing Our Minds]] (81.1% similar)
- [[2025-09-23/Quantum Abduction_ A New Paradigm for Reasoning under Uncertainty_20250923|Quantum Abduction: A New Paradigm for Reasoning under Uncertainty]] (81.0% similar)
- [[2025-09-22/Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows_20250922|Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows]] (80.6% similar)
- [[2025-09-19/Trainability of Quantum Models Beyond Known Classical Simulability_20250919|Trainability of Quantum Models Beyond Known Classical Simulability]] (79.4% similar)
- [[2025-09-17/Hybrid Quantum-Classical Neural Networks for Few-Shot Credit Risk Assessment_20250917|Hybrid Quantum-Classical Neural Networks for Few-Shot Credit Risk Assessment]] (79.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Quantum Circuits|Quantum Circuits]], [[keywords/Quantum Computing|Quantum Computing]]
**🔗 Specific Connectable**: [[keywords/Belief Functions|Belief Functions]]
**⚡ Unique Technical**: [[keywords/Transferable Belief Model|Transferable Belief Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2410.08949v4 Announce Type: replace 
Abstract: The transferable belief model, as a semantic interpretation of Dempster-Shafer theory, enables agents to perform reasoning and decision making in imprecise and incomplete environments. The model offers distinct semantics for handling unreliable testimonies, allowing for a more reasonable and general process of belief transfer compared to the Bayesian approach. However, because both the belief masses and the structure of focal sets must be considered when updating belief functions-leading to extra computational complexity during reasoning-the transferable belief model has gradually lost favor among researchers in recent developments. In this paper, we implement the transferable belief model on quantum circuits and demonstrate that belief functions offer a more concise and effective alternative to Bayesian approaches within the quantum computing framework. Furthermore, leveraging the unique characteristics of quantum computing, we propose several novel belief transfer approaches. More broadly, this paper introduces a new perspective on basic information representation for quantum AI models, suggesting that belief functions are more suitable than Bayesian approach for handling uncertainty on quantum circuits.

## 📝 요약

이 논문은 Dempster-Shafer 이론의 의미적 해석인 전이 가능한 신념 모델을 양자 회로에 구현하여, 불확실한 환경에서의 추론과 의사결정을 개선하는 방법을 제안합니다. 기존 베이지안 접근법보다 신뢰할 수 없는 증언을 처리하는 데 있어 더 합리적이고 일반적인 신념 전이 과정을 제공합니다. 그러나 신념 함수 업데이트 시 발생하는 계산 복잡성 때문에 최근 연구에서는 주목받지 못했습니다. 이 논문에서는 양자 컴퓨팅의 특성을 활용하여 새로운 신념 전이 방법을 제안하고, 양자 AI 모델에서 불확실성을 다루는 데 있어 신념 함수가 베이지안 접근법보다 적합하다는 새로운 관점을 제시합니다.

## 🎯 주요 포인트

- 1. 전이 가능한 신념 모델은 Dempster-Shafer 이론의 의미적 해석으로, 불확실하고 불완전한 환경에서의 추론과 의사결정을 가능하게 한다.
- 2. 이 모델은 신뢰할 수 없는 증언을 처리하기 위한 독특한 의미론을 제공하여, 베이지안 접근법보다 더 합리적이고 일반적인 신념 전이 과정을 가능하게 한다.
- 3. 신념 함수의 갱신 시 신념 질량과 초점 집합의 구조를 고려해야 하므로, 전이 가능한 신념 모델은 계산 복잡성으로 인해 최근 연구에서 인기를 잃어가고 있다.
- 4. 본 논문에서는 양자 회로에서 전이 가능한 신념 모델을 구현하고, 양자 컴퓨팅 프레임워크 내에서 신념 함수가 베이지안 접근법보다 더 간결하고 효과적임을 입증한다.
- 5. 양자 컴퓨팅의 고유한 특성을 활용하여 새로운 신념 전이 접근법을 제안하고, 양자 AI 모델의 기본 정보 표현에 대한 새로운 관점을 제시한다.


---

*Generated on 2025-09-24 00:23:02*