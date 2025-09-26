---
keywords:
  - Collaborative Rational Speech Act
  - Rational Speech Act
  - Multi-Turn Dialog
  - Rate-Distortion Theory
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2507.14063
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:07:52.567422",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Collaborative Rational Speech Act",
    "Rational Speech Act",
    "Multi-Turn Dialog",
    "Rate-Distortion Theory"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Collaborative Rational Speech Act": 0.92,
    "Rational Speech Act": 0.85,
    "Multi-Turn Dialog": 0.8,
    "Rate-Distortion Theory": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Collaborative Rational Speech Act",
        "canonical": "Collaborative Rational Speech Act",
        "aliases": [
          "CRSA"
        ],
        "category": "unique_technical",
        "rationale": "CRSA is a novel extension of RSA specifically designed for multi-turn dialog, making it a unique concept in pragmatic reasoning.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.92
      },
      {
        "surface": "Rational Speech Act",
        "canonical": "Rational Speech Act",
        "aliases": [
          "RSA"
        ],
        "category": "specific_connectable",
        "rationale": "RSA is a foundational framework in pragmatic reasoning, providing a strong link to existing work in language generation.",
        "novelty_score": 0.45,
        "connectivity_score": 0.89,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "multi-turn dialog",
        "canonical": "Multi-Turn Dialog",
        "aliases": [
          "multi-turn conversation"
        ],
        "category": "specific_connectable",
        "rationale": "Multi-turn dialog is crucial for understanding the iterative nature of collaborative AI systems.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "rate-distortion theory",
        "canonical": "Rate-Distortion Theory",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Rate-distortion theory is a key concept in information theory, relevant for optimizing communication strategies in AI.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "shared goals",
      "fluent language",
      "empirical results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Collaborative Rational Speech Act",
      "resolved_canonical": "Collaborative Rational Speech Act",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.92
      }
    },
    {
      "candidate_surface": "Rational Speech Act",
      "resolved_canonical": "Rational Speech Act",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.89,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "multi-turn dialog",
      "resolved_canonical": "Multi-Turn Dialog",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "rate-distortion theory",
      "resolved_canonical": "Rate-Distortion Theory",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Collaborative Rational Speech Act: Pragmatic Reasoning for Multi-Turn Dialog

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2507.14063.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2507.14063](https://arxiv.org/abs/2507.14063)

## 🔗 유사한 논문
- [[2025-09-23/ASTRA_ A Negotiation Agent with Adaptive and Strategic Reasoning via Tool-integrated Action for Dynamic Offer Optimization_20250923|ASTRA: A Negotiation Agent with Adaptive and Strategic Reasoning via Tool-integrated Action for Dynamic Offer Optimization]] (83.6% similar)
- [[2025-09-23/PRINCIPLES_ Synthetic Strategy Memory for Proactive Dialogue Agents_20250923|PRINCIPLES: Synthetic Strategy Memory for Proactive Dialogue Agents]] (82.3% similar)
- [[2025-09-19/Ask-to-Clarify_ Resolving Instruction Ambiguity through Multi-turn Dialogue_20250919|Ask-to-Clarify: Resolving Instruction Ambiguity through Multi-turn Dialogue]] (81.7% similar)
- [[2025-09-23/The STAR-XAI Protocol_ An Interactive Framework for Inducing Second-Order Agency in AI Agents_20250923|The STAR-XAI Protocol: An Interactive Framework for Inducing Second-Order Agency in AI Agents]] (81.6% similar)
- [[2025-09-19/Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents_20250919|Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents]] (81.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Rate-Distortion Theory|Rate-Distortion Theory]]
**🔗 Specific Connectable**: [[keywords/Rational Speech Act|Rational Speech Act]], [[keywords/Multi-Turn Dialog|Multi-Turn Dialog]]
**⚡ Unique Technical**: [[keywords/Collaborative Rational Speech Act|Collaborative Rational Speech Act]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.14063v2 Announce Type: replace 
Abstract: As AI systems take on collaborative roles, they must reason about shared goals and beliefs-not just generate fluent language. The Rational Speech Act (RSA) framework offers a principled approach to pragmatic reasoning, but existing extensions face challenges in scaling to multi-turn, collaborative scenarios. In this paper, we introduce Collaborative Rational Speech Act (CRSA), an information-theoretic (IT) extension of RSA that models multi-turn dialog by optimizing a gain function adapted from rate-distortion theory. This gain is an extension of the gain model that is maximized in the original RSA model but takes into account the scenario in which both agents in a conversation have private information and produce utterances conditioned on the dialog. We demonstrate the effectiveness of CRSA on referential games and template-based doctor-patient dialogs in the medical domain. Empirical results show that CRSA yields more consistent, interpretable, and collaborative behavior than existing baselines-paving the way for more pragmatic and socially aware language agents.

## 📝 요약

이 논문은 AI 시스템이 협력적 역할을 수행할 때 공유된 목표와 신념을 추론해야 한다는 점을 강조하며, 이를 위해 기존의 합리적 발화 행위(RSA) 프레임워크를 확장한 협력적 합리적 발화 행위(CRSA)를 제안합니다. CRSA는 정보 이론적 접근을 통해 다중 턴 대화를 모델링하며, 개인 정보를 가진 두 대화자가 대화에 따라 발화를 생성하는 시나리오를 고려합니다. 이 방법론은 의료 분야의 참조 게임과 템플릿 기반 의사-환자 대화에서 테스트되었으며, 기존 기준보다 일관되고 해석 가능하며 협력적인 행동을 보여주었습니다. CRSA는 보다 실용적이고 사회적으로 인식 있는 언어 에이전트 개발에 기여할 수 있습니다.

## 🎯 주요 포인트

- 1. AI 시스템이 협력적 역할을 수행하기 위해서는 공유된 목표와 신념에 대한 추론이 필요하다.
- 2. 기존의 RSA 프레임워크는 다중 턴 협력 시나리오로 확장하는 데 한계가 있다.
- 3. CRSA는 RSA의 정보 이론적 확장으로, 다중 턴 대화를 모델링하기 위해 이득 함수를 최적화한다.
- 4. CRSA는 의학 분야의 참조 게임과 템플릿 기반 의사-환자 대화에서 효과적임을 입증했다.
- 5. CRSA는 기존 기준선보다 일관되고 해석 가능하며 협력적인 행동을 보여준다.


---

*Generated on 2025-09-24 04:07:52*