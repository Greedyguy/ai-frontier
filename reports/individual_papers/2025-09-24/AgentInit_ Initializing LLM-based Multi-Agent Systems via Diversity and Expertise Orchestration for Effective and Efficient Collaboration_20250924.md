<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:32:30.104640",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Multi-Agent Systems",
    "Natural Language to Format mechanism",
    "Pareto principles"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Multi-Agent Systems": 0.8,
    "Natural Language to Format mechanism": 0.78,
    "Pareto principles": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus on initializing multi-agent systems using LLMs.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multi-Agent Systems",
        "canonical": "Multi-Agent Systems",
        "aliases": [
          "MAS"
        ],
        "category": "unique_technical",
        "rationale": "Key concept for understanding the system architecture discussed in the paper.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.8
      },
      {
        "surface": "Natural Language to Format mechanism",
        "canonical": "Natural Language to Format mechanism",
        "aliases": [
          "NL2F mechanism"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach for standardizing agent communication.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Pareto principles",
        "canonical": "Pareto principles",
        "aliases": [
          "Pareto efficiency"
        ],
        "category": "specific_connectable",
        "rationale": "Used to balance team diversity and task relevance, crucial for system optimization.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.65,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "system",
      "performance",
      "method"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Multi-Agent Systems",
      "resolved_canonical": "Multi-Agent Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Natural Language to Format mechanism",
      "resolved_canonical": "Natural Language to Format mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Pareto principles",
      "resolved_canonical": "Pareto principles",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.65,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# AgentInit: Initializing LLM-based Multi-Agent Systems via Diversity and Expertise Orchestration for Effective and Efficient Collaboration

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19236.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.19236](https://arxiv.org/abs/2509.19236)

## 🔗 유사한 논문
- [[2025-09-19/Sentinel Agents for Secure and Trustworthy Agentic AI in Multi-Agent Systems_20250919|Sentinel Agents for Secure and Trustworthy Agentic AI in Multi-Agent Systems]] (85.5% similar)
- [[2025-09-23/AgentMaster_ A Multi-Agent Conversational Framework Using A2A and MCP Protocols for Multimodal Information Retrieval and Analysis_20250923|AgentMaster: A Multi-Agent Conversational Framework Using A2A and MCP Protocols for Multimodal Information Retrieval and Analysis]] (84.8% similar)
- [[2025-09-18/$Agent^2$_ An Agent-Generates-Agent Framework for Reinforcement Learning Automation_20250918|$Agent^2$: An Agent-Generates-Agent Framework for Reinforcement Learning Automation]] (83.6% similar)
- [[2025-09-23/Runaway is Ashamed, But Helpful_ On the Early-Exit Behavior of Large Language Model-based Agents in Embodied Environments_20250923|Runaway is Ashamed, But Helpful: On the Early-Exit Behavior of Large Language Model-based Agents in Embodied Environments]] (83.4% similar)
- [[2025-09-23/BlockA2A_ Towards Secure and Verifiable Agent-to-Agent Interoperability_20250923|BlockA2A: Towards Secure and Verifiable Agent-to-Agent Interoperability]] (82.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Pareto principles|Pareto principles]]
**⚡ Unique Technical**: [[keywords/Multi-Agent Systems|Multi-Agent Systems]], [[keywords/Natural Language to Format mechanism|Natural Language to Format mechanism]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19236v1 Announce Type: new 
Abstract: Proper initialization is crucial for any system, particularly in multi-agent systems (MAS), where it plays a pivotal role in determining both the system's efficiency and effectiveness. However, existing MAS initialization methods do not fully account for the collaborative needs of the generated agents in subsequent stages. Inspired by the principles of effective team composition, we propose AgentInit, which aims to optimize the structure of agent teams. Specifically, in addition to multi-round interactions and reflections between agents during agent generation, AgentInit incorporates a Natural Language to Format mechanism to ensure consistency and standardization. Balanced team selection strategies using Pareto principles are subsequently applied to jointly consider agent team diversity and task relevance to promote effective and efficient collaboration and enhance overall system performance. Experiments show that AgentInit consistently outperforms state-of-the-art initialization methods and pre-defined strategies across various frameworks and tasks, achieving an overall performance improvement of up to 1.2 and 1.6, respectively, while also significantly reducing token consumption. Further analysis confirms its strong transferability to similar tasks and verifies the effectiveness of its key components, demonstrating its capability and adaptability as a reliable MAS initialization method. Source code and models are available at https://github.com/1737423697/AgentInit.

## 📝 요약

이 논문은 다중 에이전트 시스템(MAS)의 초기화 문제를 다룹니다. 기존 방법들이 에이전트의 협력 필요성을 충분히 고려하지 않는다는 점을 개선하기 위해, 저자들은 AgentInit을 제안합니다. 이 방법은 에이전트 생성 시 다중 라운드 상호작용과 반영을 포함하며, 자연어를 형식으로 변환하는 메커니즘을 통해 일관성을 유지합니다. 또한, 파레토 원칙을 적용하여 에이전트 팀의 다양성과 과제 관련성을 고려한 균형 잡힌 팀 선택 전략을 사용합니다. 실험 결과, AgentInit은 다양한 프레임워크와 과제에서 기존 초기화 방법보다 뛰어난 성능을 보였으며, 토큰 소비도 크게 줄였습니다. 이 방법의 강력한 전이 가능성과 주요 구성 요소의 효과도 확인되었습니다. 소스 코드와 모델은 GitHub에서 제공됩니다.

## 🎯 주요 포인트

- 1. AgentInit은 다중 에이전트 시스템(MAS)에서 에이전트 팀의 구조를 최적화하여 시스템의 효율성과 효과성을 높이는 초기화 방법을 제안합니다.
- 2. 이 방법은 에이전트 생성 시 다중 라운드 상호작용과 반영을 포함하며, 자연어를 포맷으로 변환하는 메커니즘을 도입하여 일관성과 표준화를 보장합니다.
- 3. 파레토 원칙을 활용한 균형 잡힌 팀 선택 전략을 통해 에이전트 팀의 다양성과 작업 관련성을 고려하여 협업을 촉진하고 시스템 성능을 향상시킵니다.
- 4. 실험 결과, AgentInit은 다양한 프레임워크와 작업에서 기존의 초기화 방법과 사전 정의된 전략을 능가하며, 성능을 최대 1.2 및 1.6까지 향상시키고 토큰 소비를 크게 줄입니다.
- 5. 추가 분석을 통해 유사한 작업에 대한 강력한 전이 가능성과 주요 구성 요소의 효과성을 확인하여 신뢰할 수 있는 MAS 초기화 방법으로서의 적응성과 능력을 입증합니다.


---

*Generated on 2025-09-24 13:32:30*