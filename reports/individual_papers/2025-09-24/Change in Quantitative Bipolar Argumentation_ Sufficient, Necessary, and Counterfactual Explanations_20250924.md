<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:22:13.632837",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Quantitative Bipolar Argumentation Framework",
    "Strength Inconsistency",
    "Explanations in Argumentation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Quantitative Bipolar Argumentation Framework": 0.78,
    "Strength Inconsistency": 0.77,
    "Explanations in Argumentation": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Quantitative Bipolar Argumentation Frameworks",
        "canonical": "Quantitative Bipolar Argumentation Framework",
        "aliases": [
          "QBAF"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific framework central to the paper's discussion, offering a unique perspective on argumentation theory.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "strength inconsistencies",
        "canonical": "Strength Inconsistency",
        "aliases": [
          "strength inconsistency"
        ],
        "category": "unique_technical",
        "rationale": "Identifying and explaining strength inconsistencies is a core aspect of the paper's methodology.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "sufficient, necessary, and counterfactual explanations",
        "canonical": "Explanations in Argumentation",
        "aliases": [
          "explanation types",
          "argumentation explanations"
        ],
        "category": "specific_connectable",
        "rationale": "These explanation types are crucial for understanding changes in argumentation frameworks.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "update",
      "approach",
      "implementation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Quantitative Bipolar Argumentation Frameworks",
      "resolved_canonical": "Quantitative Bipolar Argumentation Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "strength inconsistencies",
      "resolved_canonical": "Strength Inconsistency",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "sufficient, necessary, and counterfactual explanations",
      "resolved_canonical": "Explanations in Argumentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Change in Quantitative Bipolar Argumentation: Sufficient, Necessary, and Counterfactual Explanations

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18215.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18215](https://arxiv.org/abs/2509.18215)

## 🔗 유사한 논문
- [[2025-09-18/Set Contribution Functions for Quantitative Bipolar Argumentation and their Principles_20250918|Set Contribution Functions for Quantitative Bipolar Argumentation and their Principles]] (79.2% similar)
- [[2025-09-23/On the Variational Costs of Changing Our Minds_20250923|On the Variational Costs of Changing Our Minds]] (78.9% similar)
- [[2025-09-23/Canonical Representations of Markovian Structural Causal Models_ A Framework for Counterfactual Reasoning_20250923|Canonical Representations of Markovian Structural Causal Models: A Framework for Counterfactual Reasoning]] (78.9% similar)
- [[2025-09-18/Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning_20250918|Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning]] (78.5% similar)
- [[2025-09-22/Decomposing Interventional Causality into Synergistic, Redundant, and Unique Components_20250922|Decomposing Interventional Causality into Synergistic, Redundant, and Unique Components]] (78.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Explanations in Argumentation|Explanations in Argumentation]]
**⚡ Unique Technical**: [[keywords/Quantitative Bipolar Argumentation Framework|Quantitative Bipolar Argumentation Framework]], [[keywords/Strength Inconsistency|Strength Inconsistency]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18215v1 Announce Type: new 
Abstract: This paper presents a formal approach to explaining change of inference in Quantitative Bipolar Argumentation Frameworks (QBAFs). When drawing conclusions from a QBAF and updating the QBAF to then again draw conclusions (and so on), our approach traces changes -- which we call strength inconsistencies -- in the partial order over argument strengths that a semantics establishes on some arguments of interest, called topic arguments. We trace the causes of strength inconsistencies to specific arguments, which then serve as explanations. We identify sufficient, necessary, and counterfactual explanations for strength inconsistencies and show that strength inconsistency explanations exist if and only if an update leads to strength inconsistency. We define a heuristic-based approach to facilitate the search for strength inconsistency explanations, for which we also provide an implementation.

## 📝 요약

이 논문은 정량적 양극화 논증 프레임워크(QBAF)에서 추론 변화의 설명을 위한 형식적 접근법을 제시합니다. QBAF에서 결론을 도출하고 이를 갱신하여 다시 결론을 도출할 때 발생하는 강도 불일치 문제를 추적합니다. 이러한 불일치의 원인을 특정 논증에 연결하여 설명을 제공합니다. 강도 불일치에 대한 충분조건, 필요조건, 반사실적 설명을 식별하고, 갱신이 강도 불일치를 초래할 때만 설명이 존재함을 증명합니다. 또한, 강도 불일치 설명을 찾기 위한 휴리스틱 기반 접근법을 정의하고 구현을 제공합니다.

## 🎯 주요 포인트

- 1. 본 논문은 정량적 양극적 논증 프레임워크(QBAF)에서 추론 변화의 설명을 위한 형식적 접근법을 제시합니다.
- 2. 논문에서는 주제 논증의 강도 불일치의 원인을 특정 논증으로 추적하여 설명으로 사용합니다.
- 3. 강도 불일치에 대한 충분 조건, 필요 조건, 반사실적 설명을 식별하고, 업데이트가 강도 불일치를 초래할 때만 설명이 존재함을 보입니다.
- 4. 강도 불일치 설명을 찾기 위한 휴리스틱 기반 접근법을 정의하고, 이를 위한 구현을 제공합니다.


---

*Generated on 2025-09-24 13:22:13*