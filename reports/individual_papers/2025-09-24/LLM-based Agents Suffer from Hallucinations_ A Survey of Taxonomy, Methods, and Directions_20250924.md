<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:31:02.850886",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Agent Hallucinations",
    "Taxonomy of Agent Hallucinations",
    "Hallucination Mitigation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Agent Hallucinations": 0.78,
    "Taxonomy of Agent Hallucinations": 0.77,
    "Hallucination Mitigation": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "LLM-based agents",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM agents"
        ],
        "category": "broad_technical",
        "rationale": "Connects to the broader concept of Large Language Models, which is central to the paper's discussion on hallucinations.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "hallucination issues",
        "canonical": "Agent Hallucinations",
        "aliases": [
          "hallucinations in agents",
          "hallucination problems"
        ],
        "category": "unique_technical",
        "rationale": "Focuses on a specific problem within LLM-based agents, crucial for understanding and addressing system reliability.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "taxonomy of hallucinations",
        "canonical": "Taxonomy of Agent Hallucinations",
        "aliases": [
          "hallucination taxonomy"
        ],
        "category": "unique_technical",
        "rationale": "Provides a structured framework for understanding different types of hallucinations, aiding in systematic study and mitigation.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "hallucination mitigation",
        "canonical": "Hallucination Mitigation",
        "aliases": [
          "mitigation of hallucinations"
        ],
        "category": "specific_connectable",
        "rationale": "Key approach for improving the reliability of LLM-based agents, linking to methods and future research directions.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "workflow",
      "system design",
      "task execution"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "LLM-based agents",
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
      "candidate_surface": "hallucination issues",
      "resolved_canonical": "Agent Hallucinations",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "taxonomy of hallucinations",
      "resolved_canonical": "Taxonomy of Agent Hallucinations",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "hallucination mitigation",
      "resolved_canonical": "Hallucination Mitigation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# LLM-based Agents Suffer from Hallucinations: A Survey of Taxonomy, Methods, and Directions

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18970.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18970](https://arxiv.org/abs/2509.18970)

## 🔗 유사한 논문
- [[2025-09-23/How Large Language Models are Designed to Hallucinate_20250923|How Large Language Models are Designed to Hallucinate]] (88.8% similar)
- [[2025-09-23/Generalizability of Large Language Model-Based Agents_ A Comprehensive Survey_20250923|Generalizability of Large Language Model-Based Agents: A Comprehensive Survey]] (86.9% similar)
- [[2025-09-23/Overhearing LLM Agents_ A Survey, Taxonomy, and Roadmap_20250923|Overhearing LLM Agents: A Survey, Taxonomy, and Roadmap]] (85.1% similar)
- [[2025-09-22/Knowledge-Driven Hallucination in Large Language Models_ An Empirical Study on Process Modeling_20250922|Knowledge-Driven Hallucination in Large Language Models: An Empirical Study on Process Modeling]] (84.5% similar)
- [[2025-09-23/Runaway is Ashamed, But Helpful_ On the Early-Exit Behavior of Large Language Model-based Agents in Embodied Environments_20250923|Runaway is Ashamed, But Helpful: On the Early-Exit Behavior of Large Language Model-based Agents in Embodied Environments]] (84.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Hallucination Mitigation|Hallucination Mitigation]]
**⚡ Unique Technical**: [[keywords/Agent Hallucinations|Agent Hallucinations]], [[keywords/Taxonomy of Agent Hallucinations|Taxonomy of Agent Hallucinations]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18970v1 Announce Type: new 
Abstract: Driven by the rapid advancements of Large Language Models (LLMs), LLM-based agents have emerged as powerful intelligent systems capable of human-like cognition, reasoning, and interaction. These agents are increasingly being deployed across diverse real-world applications, including student education, scientific research, and financial analysis. However, despite their remarkable potential, LLM-based agents remain vulnerable to hallucination issues, which can result in erroneous task execution and undermine the reliability of the overall system design. Addressing this critical challenge requires a deep understanding and a systematic consolidation of recent advances on LLM-based agents. To this end, we present the first comprehensive survey of hallucinations in LLM-based agents. By carefully analyzing the complete workflow of agents, we propose a new taxonomy that identifies different types of agent hallucinations occurring at different stages. Furthermore, we conduct an in-depth examination of eighteen triggering causes underlying the emergence of agent hallucinations. Through a detailed review of a large number of existing studies, we summarize approaches for hallucination mitigation and detection, and highlight promising directions for future research. We hope this survey will inspire further efforts toward addressing hallucinations in LLM-based agents, ultimately contributing to the development of more robust and reliable agent systems.

## 📝 요약

이 논문은 대형 언어 모델(LLM)을 기반으로 한 에이전트의 환각 문제를 다루며, 이러한 문제를 해결하기 위한 체계적인 접근을 제안합니다. LLM 기반 에이전트는 다양한 분야에서 활용되지만, 환각으로 인해 잘못된 작업 수행이 발생할 수 있습니다. 본 연구는 에이전트의 전체 워크플로우를 분석하여 환각의 유형을 분류하고, 환각을 유발하는 18가지 원인을 심층적으로 조사합니다. 또한, 환각 완화 및 탐지를 위한 기존 연구를 검토하고, 향후 연구 방향을 제시합니다. 이를 통해 더 견고하고 신뢰할 수 있는 에이전트 시스템 개발에 기여하고자 합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM) 기반 에이전트는 인간과 유사한 인지, 추론, 상호작용이 가능한 지능형 시스템으로 발전하고 있다.
- 2. LLM 기반 에이전트는 학생 교육, 과학 연구, 금융 분석 등 다양한 실제 응용 분야에 활용되고 있다.
- 3. LLM 기반 에이전트는 환각 문제로 인해 잘못된 작업 수행과 시스템 신뢰성 저하의 위험이 있다.
- 4. 본 논문은 LLM 기반 에이전트의 환각 문제를 체계적으로 분석하고 새로운 분류 체계를 제안한다.
- 5. 환각 문제 해결을 위한 완화 및 탐지 접근법을 요약하고, 향후 연구 방향을 제시한다.


---

*Generated on 2025-09-24 13:31:02*