<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:21:15.075905",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Operations Research",
    "Automatic Modeling",
    "Semantic Understanding",
    "Optimization Tasks"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Operations Research": 0.78,
    "Automatic Modeling": 0.77,
    "Semantic Understanding": 0.79,
    "Optimization Tasks": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "This term is central to the paper's theme and connects to various applications in operations research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Operations Research",
        "canonical": "Operations Research",
        "aliases": [
          "OR"
        ],
        "category": "unique_technical",
        "rationale": "A key domain discussed in the paper, linking methodologies and applications.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Automatic Modeling",
        "canonical": "Automatic Modeling",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Represents a specific application of LLMs in OR, facilitating connections to modeling techniques.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      },
      {
        "surface": "Semantic Understanding",
        "canonical": "Semantic Understanding",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Highlights the role of LLMs in interpreting natural language, crucial for linking to NLP tasks.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.79
      },
      {
        "surface": "Optimization Tasks",
        "canonical": "Optimization Tasks",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Central to OR, this term connects LLM capabilities with optimization challenges.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "evaluation benchmarks",
      "domain-specific applications"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Operations Research",
      "resolved_canonical": "Operations Research",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Automatic Modeling",
      "resolved_canonical": "Automatic Modeling",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Semantic Understanding",
      "resolved_canonical": "Semantic Understanding",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Optimization Tasks",
      "resolved_canonical": "Optimization Tasks",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Large Language Models and Operations Research: A Structured Survey

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18180.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18180](https://arxiv.org/abs/2509.18180)

## 🔗 유사한 논문
- [[2025-09-18/From Automation to Autonomy_ A Survey on Large Language Models in Scientific Discovery_20250918|From Automation to Autonomy: A Survey on Large Language Models in Scientific Discovery]] (86.3% similar)
- [[2025-09-23/Large Language Models for Security Operations Centers_ A Comprehensive Survey_20250923|Large Language Models for Security Operations Centers: A Comprehensive Survey]] (86.0% similar)
- [[2025-09-22/Are LLMs Better Formalizers than Solvers on Complex Problems?_20250922|Are LLMs Better Formalizers than Solvers on Complex Problems?]] (86.0% similar)
- [[2025-09-23/Reinforcement Learning Meets Large Language Models_ A Survey of Advancements and Applications Across the LLM Lifecycle_20250923|Reinforcement Learning Meets Large Language Models: A Survey of Advancements and Applications Across the LLM Lifecycle]] (85.8% similar)
- [[2025-09-23/Large Language Models as End-to-end Combinatorial Optimization Solvers_20250923|Large Language Models as End-to-end Combinatorial Optimization Solvers]] (85.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Automatic Modeling|Automatic Modeling]], [[keywords/Semantic Understanding|Semantic Understanding]], [[keywords/Optimization Tasks|Optimization Tasks]]
**⚡ Unique Technical**: [[keywords/Operations Research|Operations Research]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18180v1 Announce Type: new 
Abstract: Operations research (OR) provides fundamental methodologies for complex system decision-making, with established applications in transportation, supply chain management, and production scheduling. Traditional approaches, which depend on expert-based modeling and manual parameter adjustment, often face challenges in handling large-scale, dynamic, and multi-constraint problems. Recently, large language models (LLMs) have shown potential to address these limitations through semantic understanding, structured generation, and reasoning control. LLMs can translate natural language descriptions into mathematical models or executable code, generate heuristics, evolve algorithms, and directly tackle optimization tasks. This paper surveys recent progress on the integration of LLMs into OR, organizing methods into three main directions: automatic modeling, auxiliary optimization, and direct solving. It further reviews evaluation benchmarks and domain-specific applications, and summarizes key open issues such as unstable semantic-to-structure mapping, fragmented research progress, limited generalization, and insufficient evaluation systems. Finally, the survey outlines possible research avenues for advancing the role of LLMs in OR.

## 📝 요약

이 논문은 대규모 언어 모델(LLM)을 운영 연구(OR)에 통합하는 최근의 발전을 조사합니다. 전통적인 OR 방법론은 복잡한 시스템의 의사결정에 한계를 보이지만, LLM은 자연어를 수학적 모델이나 실행 가능한 코드로 변환하고, 알고리즘을 발전시키며 최적화 작업을 직접 해결할 수 있는 잠재력을 가지고 있습니다. 논문은 LLM을 활용한 자동 모델링, 보조 최적화, 직접 해결의 세 가지 방향으로 방법론을 정리하고, 평가 기준 및 분야별 응용을 검토합니다. 또한 불안정한 의미-구조 매핑, 단편적인 연구 진행, 일반화의 한계, 평가 시스템의 부족 등 주요 문제를 요약하고, LLM의 OR에서의 역할을 발전시키기 위한 연구 방향을 제시합니다.

## 🎯 주요 포인트

- 1. 운영 연구(OR)는 복잡한 시스템의 의사결정을 위한 기본 방법론을 제공하며, 교통, 공급망 관리, 생산 일정 계획에 널리 응용되고 있다.
- 2. 전통적인 OR 접근 방식은 대규모, 동적, 다중 제약 문제를 다루는 데 어려움을 겪는다.
- 3. 대형 언어 모델(LLM)은 자연어 설명을 수학적 모델이나 실행 가능한 코드로 변환하고, 알고리즘을 발전시키며, 최적화 작업을 직접 처리할 수 있는 잠재력을 보여준다.
- 4. LLM과 OR의 통합은 자동 모델링, 보조 최적화, 직접 해결의 세 가지 주요 방향으로 정리된다.
- 5. 불안정한 의미-구조 매핑, 단편화된 연구 진행, 제한된 일반화, 불충분한 평가 시스템 등이 LLM과 OR 통합의 주요 과제로 지적된다.


---

*Generated on 2025-09-24 13:21:15*