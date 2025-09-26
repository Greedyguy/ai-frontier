<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:19:34.389872",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Multi-Agent Framework",
    "Decision Rule Optimization",
    "Cross-Domain Validation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.82,
    "Multi-Agent Framework": 0.78,
    "Decision Rule Optimization": 0.8,
    "Cross-Domain Validation": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are central to the framework's approach to cross-domain misinformation detection.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.82
      },
      {
        "surface": "MultiAgent Framework",
        "canonical": "Multi-Agent Framework",
        "aliases": [
          "MultiAgent System",
          "MAS"
        ],
        "category": "unique_technical",
        "rationale": "The framework is a novel approach specific to the paper's methodology.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Automated Decision Rule Optimization",
        "canonical": "Decision Rule Optimization",
        "aliases": [
          "Automated Decision Rules",
          "Decision Rule Tuning"
        ],
        "category": "unique_technical",
        "rationale": "This process is a key innovation in enhancing cross-domain detection capabilities.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Cross-Domain Validation Tasks",
        "canonical": "Cross-Domain Validation",
        "aliases": [
          "Cross-Domain Testing",
          "Domain Transfer Validation"
        ],
        "category": "specific_connectable",
        "rationale": "These tasks are crucial for improving the generalizability of decision rules.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "misinformation detection",
      "expert agents",
      "news analysis"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
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
      "candidate_surface": "MultiAgent Framework",
      "resolved_canonical": "Multi-Agent Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Automated Decision Rule Optimization",
      "resolved_canonical": "Decision Rule Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Cross-Domain Validation Tasks",
      "resolved_canonical": "Cross-Domain Validation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# A Multi-Agent Framework with Automated Decision Rule Optimization for Cross-Domain Misinformation Detection

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2503.23329.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2503.23329](https://arxiv.org/abs/2503.23329)

## 🔗 유사한 논문
- [[2025-09-23/MSCoRe_ A Benchmark for Multi-Stage Collaborative Reasoning in LLM Agents_20250923|MSCoRe: A Benchmark for Multi-Stage Collaborative Reasoning in LLM Agents]] (85.2% similar)
- [[2025-09-23/XAgents_ A Framework for Interpretable Rule-Based Multi-Agents Cooperation_20250923|XAgents: A Framework for Interpretable Rule-Based Multi-Agents Cooperation]] (85.0% similar)
- [[2025-09-23/AgentMaster_ A Multi-Agent Conversational Framework Using A2A and MCP Protocols for Multimodal Information Retrieval and Analysis_20250923|AgentMaster: A Multi-Agent Conversational Framework Using A2A and MCP Protocols for Multimodal Information Retrieval and Analysis]] (84.7% similar)
- [[2025-09-19/Select to Know_ An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering_20250919|Select to Know: An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering]] (84.0% similar)
- [[2025-09-24/Anecdoctoring_ Automated Red-Teaming Across Language and Place_20250924|Anecdoctoring: Automated Red-Teaming Across Language and Place]] (83.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Cross-Domain Validation|Cross-Domain Validation]]
**⚡ Unique Technical**: [[keywords/Multi-Agent Framework|Multi-Agent Framework]], [[keywords/Decision Rule Optimization|Decision Rule Optimization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.23329v2 Announce Type: replace 
Abstract: Misinformation spans various domains, but detection methods trained on specific domains often perform poorly when applied to others. With the rapid development of Large Language Models (LLMs), researchers have begun to utilize LLMs for cross-domain misinformation detection. However, existing LLM-based methods often fail to adequately analyze news in the target domain, limiting their detection capabilities. More importantly, these methods typically rely on manually designed decision rules, which are limited by domain knowledge and expert experience, thus limiting the generalizability of decision rules to different domains. To address these issues, we propose a MultiAgent Framework for cross-domain misinformation detection with Automated Decision Rule Optimization (MARO). Under this framework, we first employs multiple expert agents to analyze target-domain news. Subsequently, we introduce a question-reflection mechanism that guides expert agents to facilitate higherquality analysis. Furthermore, we propose a decision rule optimization approach based on carefully-designed cross-domain validation tasks to iteratively enhance the effectiveness of decision rules in different domains. Experimental results and in-depth analysis on commonlyused datasets demonstrate that MARO achieves significant improvements over existing methods.

## 📝 요약

이 논문은 다양한 분야의 허위 정보를 탐지하는 방법론을 제안합니다. 기존의 대형 언어 모델(LLM) 기반 방법들은 특정 분야에 한정된 규칙에 의존하여 다른 분야에 적용할 때 성능이 저하되는 문제가 있었습니다. 이를 해결하기 위해, 저자들은 자동화된 의사결정 규칙 최적화(MARO)를 통한 다중 에이전트 프레임워크를 제안합니다. 이 프레임워크는 여러 전문가 에이전트를 활용하여 목표 분야의 뉴스를 분석하고, 질문-반성 메커니즘을 도입하여 분석의 질을 높입니다. 또한, 신중하게 설계된 교차 도메인 검증 작업을 통해 의사결정 규칙의 효과성을 향상시킵니다. 실험 결과, MARO는 기존 방법들보다 뛰어난 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 기존의 대규모 언어 모델(LLM) 기반 방법은 대상 도메인 뉴스 분석에 한계가 있어 오탐지 능력이 제한적입니다.
- 2. 수동으로 설계된 결정 규칙에 의존하는 기존 방법은 도메인 지식과 전문가 경험에 의해 제한되어 다양한 도메인에 일반화하기 어렵습니다.
- 3. MARO는 다중 에이전트 프레임워크를 통해 교차 도메인 허위 정보 탐지를 자동화된 결정 규칙 최적화로 개선합니다.
- 4. 전문가 에이전트가 대상 도메인 뉴스를 분석하고, 질문-반성 메커니즘을 도입하여 분석의 질을 높입니다.
- 5. 교차 도메인 검증 작업을 기반으로 결정 규칙을 최적화하여 다양한 도메인에서의 효과성을 향상시킵니다.


---

*Generated on 2025-09-24 14:19:34*