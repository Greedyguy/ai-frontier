---
keywords:
  - Recommender Systems
  - Fairness in Machine Learning
  - Multi-stakeholder Environments
  - Cross-team Collaboration
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2505.19441
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:59:32.759954",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Recommender Systems",
    "Fairness in Machine Learning",
    "Multi-stakeholder Environments",
    "Cross-team Collaboration"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Recommender Systems": 0.92,
    "Fairness in Machine Learning": 0.89,
    "Multi-stakeholder Environments": 0.81,
    "Cross-team Collaboration": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Recommender Systems",
        "canonical": "Recommender Systems",
        "aliases": [
          "RS"
        ],
        "category": "specific_connectable",
        "rationale": "Recommender systems are central to the paper's discussion and are a key area for fairness considerations.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.85,
        "link_intent_score": 0.92
      },
      {
        "surface": "Fairness",
        "canonical": "Fairness in Machine Learning",
        "aliases": [
          "Bias Mitigation"
        ],
        "category": "evolved_concepts",
        "rationale": "Fairness is a critical concept in the context of machine learning and recommender systems, especially in high-stakes applications.",
        "novelty_score": 0.55,
        "connectivity_score": 0.79,
        "specificity_score": 0.82,
        "link_intent_score": 0.89
      },
      {
        "surface": "Stakeholders",
        "canonical": "Multi-stakeholder Environments",
        "aliases": [
          "Stakeholder Dynamics"
        ],
        "category": "unique_technical",
        "rationale": "Understanding stakeholder dynamics is essential for implementing fairness in recommender systems.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.81
      },
      {
        "surface": "Cross-team Communication",
        "canonical": "Cross-team Collaboration",
        "aliases": [
          "Interdisciplinary Communication"
        ],
        "category": "unique_technical",
        "rationale": "Effective cross-team communication is crucial for integrating fairness into workflows.",
        "novelty_score": 0.61,
        "connectivity_score": 0.7,
        "specificity_score": 0.76,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "workflow",
      "providers",
      "users"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Recommender Systems",
      "resolved_canonical": "Recommender Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.85,
        "link_intent": 0.92
      }
    },
    {
      "candidate_surface": "Fairness",
      "resolved_canonical": "Fairness in Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.79,
        "specificity": 0.82,
        "link_intent": 0.89
      }
    },
    {
      "candidate_surface": "Stakeholders",
      "resolved_canonical": "Multi-stakeholder Environments",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Cross-team Communication",
      "resolved_canonical": "Cross-team Collaboration",
      "decision": "linked",
      "scores": {
        "novelty": 0.61,
        "connectivity": 0.7,
        "specificity": 0.76,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Fairness-in-the-Workflow: How Machine Learning Practitioners at Big Tech Companies Approach Fairness in Recommender Systems

**Korean Title:** 워크플로우에서의 공정성: 대형 기술 기업의 머신러닝 실무자들이 추천 시스템에서 공정성을 접근하는 방법

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.19441.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2505.19441](https://arxiv.org/abs/2505.19441)

## 🔗 유사한 논문
- [[2025-09-22/Algorithmic Fairness_ Not a Purely Technical but Socio-Technical Property_20250922|Algorithmic Fairness: Not a Purely Technical but Socio-Technical Property]] (82.9% similar)
- [[2025-09-19/Let's Grow an Unbiased Community_ Guiding the Fairness of Graphs via New Links_20250919|Let's Grow an Unbiased Community: Guiding the Fairness of Graphs via New Links]] (78.3% similar)
- [[2025-09-22/AI for Scientific Discovery is a Social Problem_20250922|AI for Scientific Discovery is a Social Problem]] (77.5% similar)
- [[2025-09-22/REFER_ Mitigating Bias in Opinion Summarisation via Frequency Framed Prompting_20250922|REFER: Mitigating Bias in Opinion Summarisation via Frequency Framed Prompting]] (77.4% similar)
- [[2025-09-22/Dynamic Policy Fusion for User Alignment Without Re-Interaction_20250922|Dynamic Policy Fusion for User Alignment Without Re-Interaction]] (77.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Recommender Systems|Recommender Systems]]
**⚡ Unique Technical**: [[keywords/Multi-stakeholder Environments|Multi-stakeholder Environments]], [[keywords/Cross-team Collaboration|Cross-team Collaboration]]
**🚀 Evolved Concepts**: [[keywords/Fairness in Machine Learning|Fairness in Machine Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.19441v2 Announce Type: replace-cross 
Abstract: Recommender systems (RS), which are widely deployed across high-stakes domains, are susceptible to biases that can cause large-scale societal impacts. Researchers have proposed methods to measure and mitigate such biases -- but translating academic theory into practice is inherently challenging. RS practitioners must balance the competing interests of diverse stakeholders, including providers and users, and operate in dynamic environments. Through a semi-structured interview study (N=11), we map the RS practitioner workflow within large technology companies, focusing on how technical teams consider fairness internally and in collaboration with other (legal, data, and fairness) teams. We identify key challenges to incorporating fairness into existing RS workflows: defining fairness in RS contexts, particularly when navigating multi-stakeholder and dynamic fairness considerations. We also identify key organization-wide challenges: making time for fairness work and facilitating cross-team communication. Finally, we offer actionable recommendations for the RS community, including HCI researchers and practitioners.

## 🔍 Abstract (한글 번역)

arXiv:2505.19441v2 발표 유형: 교차 교체  
초록: 추천 시스템(RS)은 고위험 분야에서 널리 사용되며, 대규모 사회적 영향을 초래할 수 있는 편향에 취약합니다. 연구자들은 이러한 편향을 측정하고 완화하기 위한 방법을 제안했지만, 학문적 이론을 실제로 적용하는 것은 본질적으로 어려운 일입니다. RS 실무자들은 제공자와 사용자 등 다양한 이해관계자의 상충되는 이익을 균형 있게 고려해야 하며, 역동적인 환경에서 운영해야 합니다. 반구조화된 인터뷰 연구(N=11)를 통해 대형 기술 기업 내 RS 실무자 워크플로를 매핑하고, 기술 팀이 내부적으로 및 다른 팀(법률, 데이터, 공정성)과 협력하여 공정성을 어떻게 고려하는지에 초점을 맞춥니다. 기존 RS 워크플로에 공정성을 통합하는 데 있어 주요 과제로는 특히 다중 이해관계자 및 역동적인 공정성 고려사항을 탐색할 때 RS 맥락에서 공정성을 정의하는 것이 있습니다. 또한, 조직 전체의 주요 과제로는 공정성 작업에 시간을 할애하고 팀 간 커뮤니케이션을 촉진하는 것이 있습니다. 마지막으로, HCI 연구자 및 실무자를 포함한 RS 커뮤니티를 위한 실행 가능한 권장 사항을 제시합니다.

## 📝 요약

이 논문은 추천 시스템(RS)에서 발생할 수 있는 편향 문제를 다루고 있으며, 이러한 편향을 측정하고 완화하는 방법론을 제안합니다. 대형 기술 기업의 RS 실무자들을 대상으로 한 반구조화 인터뷰 연구(N=11)를 통해, 기술 팀이 내부 및 다른 팀(법률, 데이터, 공정성)과 협력하여 공정성을 고려하는 방식을 분석했습니다. 연구는 RS 워크플로우에 공정성을 통합하는 데 있어 공정성 정의의 어려움과 다양한 이해관계자 및 동적인 환경에서의 공정성 고려 문제를 주요 도전 과제로 식별했습니다. 또한, 조직 차원에서 공정성 작업을 위한 시간 확보와 팀 간 소통의 중요성을 강조하며, HCI 연구자 및 실무자를 위한 실질적인 권장 사항을 제시합니다.

## 🎯 주요 포인트

- 1. 추천 시스템(RS)은 고위험 분야에서 널리 사용되며, 대규모 사회적 영향을 미칠 수 있는 편향에 취약하다.
- 2. RS 실무자들은 다양한 이해관계자의 이익을 균형 있게 고려해야 하며, 이는 동적인 환경에서 이루어져야 한다.
- 3. 대형 기술 회사 내에서 RS 실무자들이 공정성을 고려하는 워크플로우를 조사한 결과, 공정성을 정의하고 다중 이해관계자 및 동적 공정성 문제를 해결하는 데 어려움이 있다.
- 4. 조직 전반에서 공정성 작업에 시간을 할애하고 팀 간 의사소통을 촉진하는 것이 주요 과제로 나타났다.
- 5. RS 커뮤니티를 위한 실질적인 권장 사항을 제안하며, 이는 HCI 연구자와 실무자에게도 유용하다.


---

*Generated on 2025-09-23 09:59:32*