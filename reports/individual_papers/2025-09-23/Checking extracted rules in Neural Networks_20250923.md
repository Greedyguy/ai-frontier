---
keywords:
  - Neural Network
  - ReLU Activation
  - Boolean Network
  - Formal Verification
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16547
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T22:49:54.886865",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "ReLU Activation",
    "Boolean Network",
    "Formal Verification"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.85,
    "ReLU Activation": 0.7,
    "Boolean Network": 0.65,
    "Formal Verification": 0.72
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
        "rationale": "Central topic of the paper, providing a broad technical context for linking.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "ReLU-activation",
        "canonical": "ReLU Activation",
        "aliases": [
          "Rectified Linear Unit"
        ],
        "category": "specific_connectable",
        "rationale": "Specific activation function discussed, relevant for linking to detailed neural network architectures.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Boolean networks",
        "canonical": "Boolean Network",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Distinct type of network analyzed, offering unique technical insights.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.65
      },
      {
        "surface": "formal verification",
        "canonical": "Formal Verification",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Key method used for rule checking, important for linking to verification techniques.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "rule",
      "algorithm",
      "complexity theoretic"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "ReLU-activation",
      "resolved_canonical": "ReLU Activation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Boolean networks",
      "resolved_canonical": "Boolean Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.65
      }
    },
    {
      "candidate_surface": "formal verification",
      "resolved_canonical": "Formal Verification",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Checking extracted rules in Neural Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16547.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16547](https://arxiv.org/abs/2509.16547)

## 🔗 유사한 논문
- [[2025-09-22/Adversarial generalization of unfolding (model-based) networks_20250922|Adversarial generalization of unfolding (model-based) networks]] (80.4% similar)
- [[2025-09-17/A Neural Network for the Identical Kuramoto Equation_ Architectural Considerations and Performance Evaluation_20250917|A Neural Network for the Identical Kuramoto Equation: Architectural Considerations and Performance Evaluation]] (79.5% similar)
- [[2025-09-17/Circuit realization and hardware linearization of monotone operator equilibrium networks_20250917|Circuit realization and hardware linearization of monotone operator equilibrium networks]] (79.2% similar)
- [[2025-09-19/Mini-Batch Robustness Verification of Deep Neural Networks_20250919|Mini-Batch Robustness Verification of Deep Neural Networks]] (79.2% similar)
- [[2025-09-18/Self-Explaining Reinforcement Learning for Mobile Network Resource Allocation_20250918|Self-Explaining Reinforcement Learning for Mobile Network Resource Allocation]] (78.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/ReLU Activation|ReLU Activation]], [[keywords/Formal Verification|Formal Verification]]
**⚡ Unique Technical**: [[keywords/Boolean Network|Boolean Network]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16547v1 Announce Type: new 
Abstract: In this paper we investigate formal verification of extracted rules for Neural Networks under a complexity theoretic point of view. A rule is a global property or a pattern concerning a large portion of the input space of a network. These rules are algorithmically extracted from networks in an effort to better understand their inner way of working. Here, three problems will be in the focus: Does a given set of rules apply to a given network? Is a given set of rules consistent or do the rules contradict themselves? Is a given set of rules exhaustive in the sense that for every input the output is determined? Finding algorithms that extract such rules out of networks has been investigated over the last 30 years, however, to the author's current knowledge, no attempt in verification was made until now. A lot of attempts of extracting rules use heuristics involving randomness and over-approximation, so it might be beneficial to know whether knowledge obtained in that way can actually be trusted.
  We investigate the above questions for neural networks with ReLU-activation as well as for Boolean networks, each for several types of rules. We demonstrate how these problems can be reduced to each other and show that most of them are co-NP-complete.

## 📝 요약

이 논문은 신경망에서 추출된 규칙의 형식적 검증을 복잡도 이론 관점에서 연구합니다. 규칙은 네트워크의 입력 공간의 큰 부분에 대한 전역적 특성이나 패턴을 의미하며, 네트워크의 작동 방식을 이해하기 위해 알고리즘적으로 추출됩니다. 본 연구는 세 가지 문제에 초점을 맞춥니다: 주어진 규칙 세트가 특정 네트워크에 적용되는지, 규칙이 일관성이 있는지, 모든 입력에 대해 출력이 결정되는지 여부입니다. 저자는 ReLU 활성화 함수가 있는 신경망과 불 대수 네트워크에 대해 이러한 문제를 조사하며, 대부분의 문제가 co-NP-완전임을 보입니다. 이 연구는 규칙 추출의 신뢰성을 높이기 위한 검증 시도를 처음으로 제안합니다.

## 🎯 주요 포인트

- 1. 신경망에서 추출된 규칙의 형식적 검증을 복잡도 이론적 관점에서 조사합니다.
- 2. 규칙의 적용 가능성, 일관성, 포괄성을 검증하는 세 가지 문제를 중점적으로 다룹니다.
- 3. 신경망에서 규칙을 추출하는 알고리즘은 30년간 연구되었지만, 검증 시도는 이번이 처음입니다.
- 4. ReLU 활성화 함수와 불 대수 네트워크에 대해 여러 유형의 규칙을 조사합니다.
- 5. 대부분의 문제는 서로 환원 가능하며, co-NP-완전임을 보입니다.


---

*Generated on 2025-09-23 22:49:54*