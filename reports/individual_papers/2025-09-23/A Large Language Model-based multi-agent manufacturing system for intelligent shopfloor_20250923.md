---
keywords:
  - Large Language Model
  - Intelligent Shopfloor Management
  - Multi-Agent System
  - Machine Server Module
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2405.16887
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:22:17.963552",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Intelligent Shopfloor Management",
    "Multi-Agent System",
    "Machine Server Module"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.82,
    "Intelligent Shopfloor Management": 0.78,
    "Multi-Agent System": 0.75,
    "Machine Server Module": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Model-based multi-agent manufacturing system",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM-based system"
        ],
        "category": "broad_technical",
        "rationale": "Connects with existing research on LLM applications in various domains, enhancing cross-disciplinary insights.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.82
      },
      {
        "surface": "intelligent shopfloor management",
        "canonical": "Intelligent Shopfloor Management",
        "aliases": [
          "smart shopfloor",
          "automated shopfloor"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel application of AI in manufacturing, facilitating connections with industry-specific research.",
        "novelty_score": 0.72,
        "connectivity_score": 0.67,
        "specificity_score": 0.79,
        "link_intent_score": 0.78
      },
      {
        "surface": "multi-agent manufacturing system",
        "canonical": "Multi-Agent System",
        "aliases": [
          "MAS",
          "agent-based manufacturing"
        ],
        "category": "specific_connectable",
        "rationale": "Links to existing work on agent-based systems, promoting integration with broader AI research.",
        "novelty_score": 0.58,
        "connectivity_score": 0.83,
        "specificity_score": 0.71,
        "link_intent_score": 0.75
      },
      {
        "surface": "Machine Server Module",
        "canonical": "Machine Server Module",
        "aliases": [
          "MSM"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a specific component of the proposed system, useful for detailed technical discussions.",
        "novelty_score": 0.65,
        "connectivity_score": 0.55,
        "specificity_score": 0.82,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "dynamic disturbances",
      "predefined heuristic rules"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Model-based multi-agent manufacturing system",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "intelligent shopfloor management",
      "resolved_canonical": "Intelligent Shopfloor Management",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.67,
        "specificity": 0.79,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "multi-agent manufacturing system",
      "resolved_canonical": "Multi-Agent System",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.83,
        "specificity": 0.71,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Machine Server Module",
      "resolved_canonical": "Machine Server Module",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.55,
        "specificity": 0.82,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# A Large Language Model-based multi-agent manufacturing system for intelligent shopfloor

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2405.16887.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2405.16887](https://arxiv.org/abs/2405.16887)

## 🔗 유사한 논문
- [[2025-09-19/An LLM-based multi-agent framework for agile effort estimation_20250919|An LLM-based multi-agent framework for agile effort estimation]] (86.8% similar)
- [[2025-09-22/Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context_20250922|Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context]] (84.9% similar)
- [[2025-09-22/Using Natural Language for Human-Robot Collaboration in the Real World_20250922|Using Natural Language for Human-Robot Collaboration in the Real World]] (84.0% similar)
- [[2025-09-19/(P)rior(D)yna(F)low_ A Priori Dynamic Workflow Construction via Multi-Agent Collaboration_20250919|(P)rior(D)yna(F)low: A Priori Dynamic Workflow Construction via Multi-Agent Collaboration]] (84.0% similar)
- [[2025-09-18/Evaluating Classical Software Process Models as Coordination Mechanisms for LLM-Based Software Generation_20250918|Evaluating Classical Software Process Models as Coordination Mechanisms for LLM-Based Software Generation]] (83.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multi-Agent System|Multi-Agent System]]
**⚡ Unique Technical**: [[keywords/Intelligent Shopfloor Management|Intelligent Shopfloor Management]], [[keywords/Machine Server Module|Machine Server Module]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2405.16887v2 Announce Type: replace 
Abstract: As customer demand for multi-variety and small-batch production increases, dynamic disturbances place greater demands on manufacturing systems. To address such challenges, researchers proposed the multi-agent manufacturing system. However, conventional agent negotiation typically relies on pre-defined and fixed heuristic rules, which are ill-suited to managing complex and fluctuating disturbances. In current implementations, mainstream approaches based on reinforcement learning require the development of simulators and training models specific to a given shopfloor, necessitating substantial computational resources and lacking scalability. To overcome this limitation, the present study proposes a Large Language Model-based (LLM-based) multi-agent manufacturing system for intelligent shopfloor management. By defining the diverse modules of agents and their collaborative methods, this system facilitates the processing of all workpieces with minimal human intervention. The agents in this system consist of the Machine Server Module (MSM), Bid Inviter Module (BIM), Bidder Module (BM), Thinking Module (TM), and Decision Module (DM). By harnessing the reasoning capabilities of LLMs, these modules enable agents to dynamically analyze shopfloor information and select appropriate processing machines. The LLM-based modules, predefined by system prompts, provide dynamic functionality for the system without the need for pre-training. Extensive experiments were conducted in physical shopfloor settings. The results demonstrate that the proposed system exhibits strong adaptability, and achieves superior performance (makespan) and stability (as measured by sample standard deviation) compared to other approaches without requiring pre-training.

## 📝 요약

이 연구는 다양한 종류의 소량 생산 수요 증가와 동적 교란에 대응하기 위해 대규모 언어 모델(LLM)을 기반으로 한 다중 에이전트 제조 시스템을 제안합니다. 기존의 강화 학습 기반 접근법은 시뮬레이터 개발과 많은 계산 자원이 필요하며 확장성이 부족한 문제를 해결하고자, 이 시스템은 최소한의 인간 개입으로 작업을 처리할 수 있도록 에이전트의 다양한 모듈과 협력 방법을 정의합니다. 주요 모듈로는 기계 서버 모듈(MSM), 입찰 초청 모듈(BIM), 입찰자 모듈(BM), 사고 모듈(TM), 결정 모듈(DM)이 있으며, LLM의 추론 능력을 활용해 작업장 정보를 동적으로 분석하고 적절한 기계를 선택합니다. 사전 훈련 없이도 시스템 프롬프트로 정의된 LLM 기반 모듈은 동적 기능을 제공합니다. 실험 결과, 제안된 시스템은 높은 적응성과 우수한 성능 및 안정성을 보여줍니다.

## 🎯 주요 포인트

- 1. 다품종 소량 생산에 대한 수요 증가로 인해 제조 시스템에 대한 동적 교란 관리가 중요해졌습니다.
- 2. 기존의 에이전트 협상 방식은 고정된 휴리스틱 규칙에 의존하여 복잡한 교란 관리에 한계가 있습니다.
- 3. 본 연구는 대규모 언어 모델(LLM)을 기반으로 한 다중 에이전트 제조 시스템을 제안하여 지능형 작업장 관리를 가능하게 합니다.
- 4. 제안된 시스템은 사전 훈련 없이 LLM의 추론 능력을 활용하여 작업장 정보를 동적으로 분석하고 적절한 처리 기계를 선택합니다.
- 5. 물리적 작업장 환경에서의 실험 결과, 제안된 시스템은 우수한 적응력과 성능을 보이며, 사전 훈련 없이도 안정성을 유지합니다.


---

*Generated on 2025-09-24 00:22:17*