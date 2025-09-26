---
keywords:
  - Landmark Relationships
  - Probabilistic Lifted Ordering Graph
  - Automated Planning
  - Planning Domain
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17062
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T22:55:08.203075",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Landmark Relationships",
    "Probabilistic Lifted Ordering Graph",
    "Automated Planning",
    "Planning Domain"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Landmark Relationships": 0.75,
    "Probabilistic Lifted Ordering Graph": 0.8,
    "Automated Planning": 0.7,
    "Planning Domain": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "landmark relationships",
        "canonical": "Landmark Relationships",
        "aliases": [
          "landmark connections",
          "landmark associations"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's approach and offers a unique perspective on planning tasks.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "probabilistic lifted ordering graph",
        "canonical": "Probabilistic Lifted Ordering Graph",
        "aliases": [
          "probabilistic graph",
          "lifted ordering graph"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel graph structure that is key to the proposed methodology.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "automated planning",
        "canonical": "Automated Planning",
        "aliases": [
          "AI planning",
          "automated task planning"
        ],
        "category": "broad_technical",
        "rationale": "A fundamental concept in AI that connects to various planning algorithms and methods.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "planning domain",
        "canonical": "Planning Domain",
        "aliases": [
          "domain planning",
          "task domain"
        ],
        "category": "specific_connectable",
        "rationale": "Critical for understanding the scope and application of the proposed graph generation method.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "landmark extraction",
      "planning tasks"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "landmark relationships",
      "resolved_canonical": "Landmark Relationships",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "probabilistic lifted ordering graph",
      "resolved_canonical": "Probabilistic Lifted Ordering Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "automated planning",
      "resolved_canonical": "Automated Planning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "planning domain",
      "resolved_canonical": "Planning Domain",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# From domain-landmark graph learning to problem-landmark graph generation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17062.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17062](https://arxiv.org/abs/2509.17062)

## 🔗 유사한 논문
- [[2025-09-19/Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring_20250919|Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring]] (80.8% similar)
- [[2025-09-17/MAP_ End-to-End Autonomous Driving with Map-Assisted Planning_20250917|MAP: End-to-End Autonomous Driving with Map-Assisted Planning]] (79.0% similar)
- [[2025-09-22/A Survey of Large Language Models for Data Challenges in Graphs_20250922|A Survey of Large Language Models for Data Challenges in Graphs]] (78.5% similar)
- [[2025-09-22/MMAPG_ A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs_20250922|MMAPG: A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs]] (78.5% similar)
- [[2025-09-18/SPAR_ Scalable LLM-based PDDL Domain Generation for Aerial Robotics_20250918|SPAR: Scalable LLM-based PDDL Domain Generation for Aerial Robotics]] (78.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Automated Planning|Automated Planning]]
**🔗 Specific Connectable**: [[keywords/Planning Domain|Planning Domain]]
**⚡ Unique Technical**: [[keywords/Landmark Relationships|Landmark Relationships]], [[keywords/Probabilistic Lifted Ordering Graph|Probabilistic Lifted Ordering Graph]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17062v1 Announce Type: new 
Abstract: Landmarks have long played a pivotal role in automated planning, serving as crucial elements for improving the planning algorithms. The main limitation of classical landmark extraction methods is their sensitivity to specific planning tasks. This results in landmarks fully tailored to individual instances, thereby limiting their applicability across other instances of the same planning domain. We propose a novel approach that learns landmark relationships from multiple planning tasks of a planning domain. This leads to the creation of a \textit{probabilistic lifted ordering graph}, as a structure that captures weighted abstractions of relationships between parameterized landmarks. Although these orderings are not 100\% true (they are probabilistic), they can still be very useful in planning. Next, given a new planning task for that domain, we instantiate the relationships from that graph to this particular instance. This instantiation operates in two phases. First, it generates two graphs: the former instantiating information from the initial state and the latter from the goal state. Second, it combines these two graphs into one unified graph by searching equivalences to extract landmark orderings. We evaluate the precision and recallof the information found by our approach over well-known planning domains.

## 📝 요약

이 논문은 자동 계획에서 랜드마크의 역할을 개선하기 위한 새로운 접근법을 제안합니다. 기존 랜드마크 추출 방법은 특정 계획 작업에 민감하여 다른 인스턴스에 적용하기 어렵다는 한계가 있습니다. 이를 극복하기 위해 여러 계획 작업에서 랜드마크 관계를 학습하여 가중치가 있는 추상화를 캡처하는 확률적 리프팅 순서 그래프를 생성합니다. 이 그래프는 새로운 계획 작업에 대해 두 단계로 관계를 인스턴스화합니다. 첫째, 초기 상태와 목표 상태에서 정보를 인스턴스화한 두 개의 그래프를 생성하고, 둘째, 이를 통합하여 랜드마크 순서를 추출합니다. 제안된 방법은 잘 알려진 계획 도메인에서 정보의 정밀도와 재현성을 평가합니다.

## 🎯 주요 포인트

- 1. 기존의 랜드마크 추출 방법은 특정 계획 작업에 민감하여 일반화된 적용이 어렵다.
- 2. 여러 계획 작업에서 랜드마크 관계를 학습하여 확률적 상승 순서 그래프를 생성하는 새로운 접근 방식을 제안한다.
- 3. 제안된 방법은 초기 상태와 목표 상태에서 정보를 인스턴스화하여 두 개의 그래프를 생성하고, 이를 통합하여 랜드마크 순서를 추출한다.
- 4. 제안된 접근 방식의 정보 정확도와 재현성을 잘 알려진 계획 도메인에서 평가하였다.


---

*Generated on 2025-09-23 22:55:08*