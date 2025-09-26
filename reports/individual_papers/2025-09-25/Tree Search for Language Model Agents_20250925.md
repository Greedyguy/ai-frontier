---
keywords:
  - Tree Search Algorithm
  - Language Model Agents
  - VisualWebArena Benchmark
  - Web Automation
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2407.01476
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:08:47.367712",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Tree Search Algorithm",
    "Language Model Agents",
    "VisualWebArena Benchmark",
    "Web Automation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Tree Search Algorithm": 0.78,
    "Language Model Agents": 0.81,
    "VisualWebArena Benchmark": 0.72,
    "Web Automation": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Tree Search",
        "canonical": "Tree Search Algorithm",
        "aliases": [
          "Best-First Search",
          "Inference-Time Search"
        ],
        "category": "unique_technical",
        "rationale": "Tree Search is a novel approach in the context of language model agents, providing a unique method for exploration and planning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Language Model Agents",
        "canonical": "Language Model Agents",
        "aliases": [
          "LM Agents",
          "Autonomous Agents"
        ],
        "category": "evolved_concepts",
        "rationale": "Language Model Agents represent an evolving concept in AI, linking language models with autonomous decision-making tasks.",
        "novelty_score": 0.58,
        "connectivity_score": 0.85,
        "specificity_score": 0.77,
        "link_intent_score": 0.81
      },
      {
        "surface": "VisualWebArena",
        "canonical": "VisualWebArena Benchmark",
        "aliases": [
          "Visual Web Arena"
        ],
        "category": "unique_technical",
        "rationale": "VisualWebArena is a specific benchmark used to evaluate the effectiveness of the proposed search algorithm, highlighting its relevance.",
        "novelty_score": 0.72,
        "connectivity_score": 0.64,
        "specificity_score": 0.79,
        "link_intent_score": 0.72
      },
      {
        "surface": "Web Automation",
        "canonical": "Web Automation",
        "aliases": [
          "Web Task Automation"
        ],
        "category": "specific_connectable",
        "rationale": "Web Automation is a key application area for language model agents, facilitating connections with related automation technologies.",
        "novelty_score": 0.55,
        "connectivity_score": 0.83,
        "specificity_score": 0.71,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "success rate"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Tree Search",
      "resolved_canonical": "Tree Search Algorithm",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Language Model Agents",
      "resolved_canonical": "Language Model Agents",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.85,
        "specificity": 0.77,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "VisualWebArena",
      "resolved_canonical": "VisualWebArena Benchmark",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.64,
        "specificity": 0.79,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Web Automation",
      "resolved_canonical": "Web Automation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.83,
        "specificity": 0.71,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Tree Search for Language Model Agents

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2407.01476.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2407.01476](https://arxiv.org/abs/2407.01476)

## 🔗 유사한 논문
- [[2025-09-19/WebCoT_ Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback_20250919|WebCoT: Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback]] (85.1% similar)
- [[2025-09-18/TGPO_ Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning_20250918|TGPO: Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning]] (85.1% similar)
- [[2025-09-17/TGPO_ Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning_20250917|TGPO: Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning]] (84.6% similar)
- [[2025-09-23/WebResearcher_ Unleashing unbounded reasoning capability in Long-Horizon Agents_20250923|WebResearcher: Unleashing unbounded reasoning capability in Long-Horizon Agents]] (84.5% similar)
- [[2025-09-23/Building Coding Agents via Entropy-Enhanced Multi-Turn Preference Optimization_20250923|Building Coding Agents via Entropy-Enhanced Multi-Turn Preference Optimization]] (84.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Web Automation|Web Automation]]
**⚡ Unique Technical**: [[keywords/Tree Search Algorithm|Tree Search Algorithm]], [[keywords/VisualWebArena Benchmark|VisualWebArena Benchmark]]
**🚀 Evolved Concepts**: [[keywords/Language Model Agents|Language Model Agents]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2407.01476v3 Announce Type: replace 
Abstract: Autonomous agents powered by language models (LMs) have demonstrated promise in their ability to perform decision-making tasks such as web automation. However, a key limitation remains: LMs, primarily optimized for natural language understanding and generation, struggle with multi-step reasoning, planning, and using environmental feedback when attempting to solve realistic computer tasks. Towards addressing this, we propose an inference-time search algorithm for LM agents to explicitly perform exploration and multi-step planning in interactive web environments. Our approach is a form of best-first tree search that operates within the actual environment space, and is complementary with most existing state-of-the-art agents. It is the first tree search algorithm for LM agents that shows effectiveness on realistic web tasks. On the challenging VisualWebArena benchmark, applying our search algorithm on top of a GPT-4o agent yields a 39.7% relative increase in success rate compared to the same baseline without search, setting a state-of-the-art success rate of 26.4%. On WebArena, search also yields a 28.0% relative improvement over a baseline agent, setting a competitive success rate of 19.2%. Our experiments highlight the effectiveness of search for web agents, and we demonstrate that performance scales with increased test-time compute. We conduct a thorough analysis of our results to highlight improvements from search, limitations, and promising directions for future work. Our code and models are publicly released at https://jykoh.com/search-agents.

## 📝 요약

이 논문은 언어 모델(LM)을 활용한 자율 에이전트가 웹 자동화와 같은 의사결정 작업에서 가능성을 보였지만, 현실적인 컴퓨터 작업에서는 다단계 추론과 계획, 환경 피드백 활용에 어려움을 겪는다는 문제를 지적합니다. 이를 해결하기 위해, 저자들은 LM 에이전트가 상호작용 웹 환경에서 탐색과 다단계 계획을 수행할 수 있도록 하는 추론 시간 탐색 알고리즘을 제안합니다. 이 알고리즘은 실제 환경 공간에서 작동하는 최우선 탐색(tree search) 방식으로, 기존 최첨단 에이전트와 상호 보완적으로 작용합니다. 특히, VisualWebArena 벤치마크에서 이 알고리즘을 적용한 결과, GPT-4o 에이전트의 성공률이 39.7% 증가하여 26.4%의 최첨단 성공률을 기록했습니다. WebArena에서도 28.0%의 개선을 보여 19.2%의 경쟁력 있는 성공률을 달성했습니다. 실험 결과는 웹 에이전트에 대한 탐색의 효과를 강조하며, 테스트 시간 계산량이 증가할수록 성능이 향상됨을 보여줍니다. 저자들은 결과 분석을 통해 탐색의 개선점과 한계, 그리고 향후 연구 방향을 제시합니다. 코드와 모델은 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 언어 모델 기반 자율 에이전트는 웹 자동화와 같은 의사 결정 작업에서 유망성을 보였으나, 다단계 추론과 계획, 환경 피드백 활용에 어려움을 겪고 있다.
- 2. 이를 해결하기 위해, 우리는 상호작용 웹 환경에서 탐색과 다단계 계획을 명시적으로 수행하는 추론 시간 검색 알고리즘을 제안한다.
- 3. 제안된 알고리즘은 실제 환경 공간에서 작동하는 최선 우선 트리 검색 형태로, 기존 최첨단 에이전트와 상호 보완적이다.
- 4. VisualWebArena 벤치마크에서 제안된 검색 알고리즘을 적용한 결과, GPT-4o 에이전트의 성공률이 39.7% 상대적으로 증가하여 26.4%의 최첨단 성공률을 기록했다.
- 5. 검색 알고리즘은 테스트 시간 계산이 증가함에 따라 성능이 향상되며, 웹 에이전트의 효과를 강조하고 향후 연구 방향을 제시한다.


---

*Generated on 2025-09-25 16:08:47*