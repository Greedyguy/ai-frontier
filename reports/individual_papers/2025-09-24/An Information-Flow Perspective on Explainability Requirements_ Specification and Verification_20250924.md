<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:39:25.809628",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Explainability",
    "Privacy",
    "Epistemic Logic",
    "Counterfactual Reasoning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Explainability": 0.82,
    "Privacy": 0.8,
    "Epistemic Logic": 0.78,
    "Counterfactual Reasoning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Explainable systems",
        "canonical": "Explainability",
        "aliases": [
          "Explainable AI",
          "XAI"
        ],
        "category": "specific_connectable",
        "rationale": "Explainability is crucial for understanding system behavior, making it a key concept for linking with other AI and system design topics.",
        "novelty_score": 0.58,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Privacy guarantees",
        "canonical": "Privacy",
        "aliases": [
          "Data Privacy",
          "Privacy Protection"
        ],
        "category": "specific_connectable",
        "rationale": "Privacy is a significant concern in system design, often requiring balancing with explainability, thus providing strong linkage potential.",
        "novelty_score": 0.55,
        "connectivity_score": 0.83,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      },
      {
        "surface": "Epistemic temporal logic",
        "canonical": "Epistemic Logic",
        "aliases": [
          "Knowledge Logic",
          "Temporal Logic"
        ],
        "category": "unique_technical",
        "rationale": "This logic framework is essential for reasoning about knowledge and time, offering unique insights into system behavior.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Counterfactual causes",
        "canonical": "Counterfactual Reasoning",
        "aliases": [
          "Counterfactual Analysis",
          "What-if Analysis"
        ],
        "category": "unique_technical",
        "rationale": "Counterfactual reasoning is pivotal for understanding causality, enhancing system explainability and decision-making processes.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "system-level requirement",
      "finite-state models",
      "prototype implementation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Explainable systems",
      "resolved_canonical": "Explainability",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Privacy guarantees",
      "resolved_canonical": "Privacy",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.83,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Epistemic temporal logic",
      "resolved_canonical": "Epistemic Logic",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Counterfactual causes",
      "resolved_canonical": "Counterfactual Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# An Information-Flow Perspective on Explainability Requirements: Specification and Verification

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.01479.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.01479](https://arxiv.org/abs/2509.01479)

## 🔗 유사한 논문
- [[2025-09-23/Explainability matters_ The effect of liability rules on the healthcare sector_20250923|Explainability matters: The effect of liability rules on the healthcare sector]] (82.7% similar)
- [[2025-09-23/See What I Mean? CUE_ A Cognitive Model of Understanding Explanations_20250923|See What I Mean? CUE: A Cognitive Model of Understanding Explanations]] (81.5% similar)
- [[2025-09-19/The Sum Leaks More Than Its Parts_ Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration_20250919|The Sum Leaks More Than Its Parts: Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration]] (81.2% similar)
- [[2025-09-23/Privacy in Action_ Towards Realistic Privacy Mitigation and Evaluation for LLM-Powered Agents_20250923|Privacy in Action: Towards Realistic Privacy Mitigation and Evaluation for LLM-Powered Agents]] (80.5% similar)
- [[2025-09-22/Shedding Light on Depth_ Explainability Assessment in Monocular Depth Estimation_20250922|Shedding Light on Depth: Explainability Assessment in Monocular Depth Estimation]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Explainability|Explainability]], [[keywords/Privacy|Privacy]]
**⚡ Unique Technical**: [[keywords/Epistemic Logic|Epistemic Logic]], [[keywords/Counterfactual Reasoning|Counterfactual Reasoning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.01479v2 Announce Type: replace-cross 
Abstract: Explainable systems expose information about why certain observed effects are happening to the agents interacting with them. We argue that this constitutes a positive flow of information that needs to be specified, verified, and balanced against negative information flow that may, e.g., violate privacy guarantees. Since both explainability and privacy require reasoning about knowledge, we tackle these tasks with epistemic temporal logic extended with quantification over counterfactual causes. This allows us to specify that a multi-agent system exposes enough information such that agents acquire knowledge on why some effect occurred. We show how this principle can be used to specify explainability as a system-level requirement and provide an algorithm for checking finite-state models against such specifications. We present a prototype implementation of the algorithm and evaluate it on several benchmarks, illustrating how our approach distinguishes between explainable and unexplainable systems, and how it allows to pose additional privacy requirements.

## 📝 요약

이 논문은 설명 가능한 시스템이 상호작용하는 에이전트에게 특정 효과가 발생하는 이유를 설명하는 정보를 제공하는 방법을 제안합니다. 저자들은 설명 가능성과 프라이버시가 모두 지식에 대한 추론을 필요로 한다고 주장하며, 이를 위해 반사실적 원인에 대한 정량화를 포함한 인식적 시제 논리를 사용합니다. 이 접근법은 다중 에이전트 시스템이 충분한 정보를 제공하여 에이전트가 특정 효과의 원인을 이해할 수 있도록 명시합니다. 또한, 설명 가능성을 시스템 수준의 요구사항으로 지정하고, 유한 상태 모델을 이러한 명세에 따라 검증하는 알고리즘을 제안합니다. 프로토타입 구현과 여러 벤치마크 평가를 통해 설명 가능한 시스템과 그렇지 않은 시스템을 구별하고 추가적인 프라이버시 요구사항을 제시할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. 설명 가능한 시스템은 상호작용하는 에이전트에게 특정 효과가 발생하는 이유를 설명하는 정보를 제공한다.
- 2. 설명 가능성과 프라이버시 모두 지식에 대한 추론을 요구하므로, 우리는 반사실적 원인에 대한 양화를 포함한 인식적 시제 논리를 사용하여 이 과제를 해결한다.
- 3. 다중 에이전트 시스템이 충분한 정보를 제공하여 에이전트가 특정 효과가 발생한 이유를 알 수 있도록 명시할 수 있다.
- 4. 설명 가능성을 시스템 수준의 요구 사항으로 명시하고, 이러한 명세에 대해 유한 상태 모델을 검사하는 알고리즘을 제공한다.
- 5. 알고리즘의 프로토타입 구현을 제시하고 여러 벤치마크에서 평가하여 설명 가능한 시스템과 설명 불가능한 시스템을 구별하는 방법을 설명한다.


---

*Generated on 2025-09-24 14:39:25*