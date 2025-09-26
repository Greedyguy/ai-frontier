<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:21:54.377674",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-agent Systems",
    "EvoAgentX",
    "Large Language Model",
    "TextGrad",
    "GAIA"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multi-agent Systems": 0.8,
    "EvoAgentX": 0.85,
    "Large Language Model": 0.78,
    "TextGrad": 0.7,
    "GAIA": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multi-agent systems",
        "canonical": "Multi-agent Systems",
        "aliases": [
          "MAS"
        ],
        "category": "broad_technical",
        "rationale": "Multi-agent systems are fundamental to orchestrating complex workflows in AI, providing a basis for linking various agentic and optimization concepts.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "EvoAgentX",
        "canonical": "EvoAgentX",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "EvoAgentX is the central framework discussed in the paper, offering unique insights into automated workflow evolution.",
        "novelty_score": 0.95,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are integral to the framework's orchestration capabilities, linking to broader AI concepts.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "TextGrad",
        "canonical": "TextGrad",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "TextGrad is a specific optimization algorithm integrated into EvoAgentX, providing a unique point of discussion for optimization techniques.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "GAIA",
        "canonical": "GAIA",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "GAIA is used for real-world task evaluation, offering a unique context for applied multi-agent systems.",
        "novelty_score": 0.75,
        "connectivity_score": 0.55,
        "specificity_score": 0.8,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "workflow",
      "optimization"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multi-agent systems",
      "resolved_canonical": "Multi-agent Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "EvoAgentX",
      "resolved_canonical": "EvoAgentX",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "TextGrad",
      "resolved_canonical": "TextGrad",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "GAIA",
      "resolved_canonical": "GAIA",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.55,
        "specificity": 0.8,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# EvoAgentX: An Automated Framework for Evolving Agentic Workflows

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2507.03616.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2507.03616](https://arxiv.org/abs/2507.03616)

## 🔗 유사한 논문
- [[2025-09-18/$Agent^2$_ An Agent-Generates-Agent Framework for Reinforcement Learning Automation_20250918|$Agent^2$: An Agent-Generates-Agent Framework for Reinforcement Learning Automation]] (84.8% similar)
- [[2025-09-23/AgentMaster_ A Multi-Agent Conversational Framework Using A2A and MCP Protocols for Multimodal Information Retrieval and Analysis_20250923|AgentMaster: A Multi-Agent Conversational Framework Using A2A and MCP Protocols for Multimodal Information Retrieval and Analysis]] (84.7% similar)
- [[2025-09-23/XAgents_ A Framework for Interpretable Rule-Based Multi-Agents Cooperation_20250923|XAgents: A Framework for Interpretable Rule-Based Multi-Agents Cooperation]] (84.1% similar)
- [[2025-09-18/AppAgent v2_ Advanced Agent for Flexible Mobile Interactions_20250918|AppAgent v2: Advanced Agent for Flexible Mobile Interactions]] (83.7% similar)
- [[2025-09-19/AgentCompass_ Towards Reliable Evaluation of Agentic Workflows in Production_20250919|AgentCompass: Towards Reliable Evaluation of Agentic Workflows in Production]] (83.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Multi-agent Systems|Multi-agent Systems]], [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/EvoAgentX|EvoAgentX]], [[keywords/TextGrad|TextGrad]], [[keywords/GAIA|GAIA]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.03616v2 Announce Type: replace 
Abstract: Multi-agent systems (MAS) have emerged as a powerful paradigm for orchestrating large language models (LLMs) and specialized tools to collaboratively address complex tasks. However, existing MAS frameworks often require manual workflow configuration and lack native support for dynamic evolution and performance optimization. In addition, many MAS optimization algorithms are not integrated into a unified framework. In this paper, we present EvoAgentX, an open-source platform that automates the generation, execution, and evolutionary optimization of multi-agent workflows. EvoAgentX employs a modular architecture consisting of five core layers: the basic components, agent, workflow, evolving, and evaluation layers. Specifically, within the evolving layer, EvoAgentX integrates three MAS optimization algorithms, TextGrad, AFlow, and MIPRO, to iteratively refine agent prompts, tool configurations, and workflow topologies. We evaluate EvoAgentX on HotPotQA, MBPP, and MATH for multi-hop reasoning, code generation, and mathematical problem solving, respectively, and further assess it on real-world tasks using GAIA. Experimental results show that EvoAgentX consistently achieves significant performance improvements, including a 7.44% increase in HotPotQA F1, a 10.00% improvement in MBPP pass@1, a 10.00% gain in MATH solve accuracy, and an overall accuracy improvement of up to 20.00% on GAIA. The source code is available at: https://github.com/EvoAgentX/EvoAgentX

## 📝 요약

EvoAgentX는 대규모 언어 모델(LLM)과 특화 도구를 활용하여 복잡한 작업을 해결하는 다중 에이전트 시스템(MAS)의 자동화 플랫폼입니다. 이 플랫폼은 모듈형 아키텍처를 통해 에이전트 워크플로우의 생성, 실행, 진화적 최적화를 자동화하며, TextGrad, AFlow, MIPRO 등 세 가지 MAS 최적화 알고리즘을 통합하여 에이전트 프롬프트, 도구 구성, 워크플로우 토폴로지를 개선합니다. HotPotQA, MBPP, MATH, GAIA 등의 평가에서 EvoAgentX는 성능을 크게 향상시켰으며, 예를 들어 HotPotQA의 F1 점수를 7.44%, MBPP의 pass@1을 10.00%, MATH의 해결 정확도를 10.00%, GAIA의 전체 정확도를 최대 20.00% 증가시켰습니다. EvoAgentX의 소스 코드는 GitHub에서 확인할 수 있습니다.

## 🎯 주요 포인트

- 1. EvoAgentX는 대규모 언어 모델과 특화된 도구를 조율하여 복잡한 작업을 해결하는 다중 에이전트 시스템(MAS)을 자동화하는 오픈 소스 플랫폼입니다.
- 2. EvoAgentX는 모듈식 아키텍처를 사용하여 에이전트 프롬프트, 도구 구성, 워크플로우 토폴로지를 최적화하는 세 가지 MAS 알고리즘(TextGrad, AFlow, MIPRO)을 통합합니다.
- 3. EvoAgentX는 HotPotQA, MBPP, MATH 및 GAIA를 사용한 실험에서 다중 홉 추론, 코드 생성, 수학 문제 해결에서 성능 향상을 입증했습니다.
- 4. 실험 결과, EvoAgentX는 HotPotQA F1에서 7.44%, MBPP pass@1에서 10.00%, MATH 해결 정확도에서 10.00%, GAIA에서 최대 20.00%의 정확도 향상을 달성했습니다.
- 5. EvoAgentX의 소스 코드는 GitHub에서 제공됩니다: https://github.com/EvoAgentX/EvoAgentX


---

*Generated on 2025-09-24 14:21:54*