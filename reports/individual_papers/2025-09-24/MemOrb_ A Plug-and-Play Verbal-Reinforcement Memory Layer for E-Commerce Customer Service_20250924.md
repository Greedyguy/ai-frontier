<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:00:41.327742",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Verbal Reinforcement Memory Layer",
    "Multi-turn Interactions",
    "Structured Reflection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Verbal Reinforcement Memory Layer": 0.8,
    "Multi-turn Interactions": 0.78,
    "Structured Reflection": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Model-based agents",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM-based agents"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the discussion of memory and reinforcement in customer service applications.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "verbal reinforcement memory layer",
        "canonical": "Verbal Reinforcement Memory Layer",
        "aliases": [
          "MemOrb"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel concept introduced in the paper, crucial for enhancing LLM reliability.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "multi-turn interactions",
        "canonical": "Multi-turn Interactions",
        "aliases": [
          "multi-turn dialogues"
        ],
        "category": "specific_connectable",
        "rationale": "Multi-turn interactions are key to understanding and improving dialogue systems in customer service.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "structured reflection",
        "canonical": "Structured Reflection",
        "aliases": [
          "reflection mechanism"
        ],
        "category": "unique_technical",
        "rationale": "Structured reflection is a unique mechanism proposed for improving LLM reliability.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "task success rate",
      "consistency metrics",
      "shared memory bank"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Model-based agents",
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
      "candidate_surface": "verbal reinforcement memory layer",
      "resolved_canonical": "Verbal Reinforcement Memory Layer",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "multi-turn interactions",
      "resolved_canonical": "Multi-turn Interactions",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "structured reflection",
      "resolved_canonical": "Structured Reflection",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# MemOrb: A Plug-and-Play Verbal-Reinforcement Memory Layer for E-Commerce Customer Service

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18713.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18713](https://arxiv.org/abs/2509.18713)

## 🔗 유사한 논문
- [[2025-09-24/Memory in Large Language Models_ Mechanisms, Evaluation and Evolution_20250924|Memory in Large Language Models: Mechanisms, Evaluation and Evolution]] (85.2% similar)
- [[2025-09-22/Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context_20250922|Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context]] (84.7% similar)
- [[2025-09-19/WebCoT_ Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback_20250919|WebCoT: Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback]] (84.1% similar)
- [[2025-09-23/A State-Update Prompting Strategy for Efficient and Robust Multi-turn Dialogue_20250923|A State-Update Prompting Strategy for Efficient and Robust Multi-turn Dialogue]] (84.0% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (83.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multi-turn Interactions|Multi-turn Interactions]]
**⚡ Unique Technical**: [[keywords/Verbal Reinforcement Memory Layer|Verbal Reinforcement Memory Layer]], [[keywords/Structured Reflection|Structured Reflection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18713v1 Announce Type: cross 
Abstract: Large Language Model-based agents(LLM-based agents) are increasingly deployed in customer service, yet they often forget across sessions, repeat errors, and lack mechanisms for continual self-improvement. This makes them unreliable in dynamic settings where stability and consistency are critical. To better evaluate these properties, we emphasize two indicators: task success rate as a measure of overall effectiveness, and consistency metrics such as Pass$^k$ to capture reliability across multiple trials. To address the limitations of existing approaches, we propose MemOrb, a lightweight and plug-and-play verbal reinforcement memory layer that distills multi-turn interactions into compact strategy reflections. These reflections are stored in a shared memory bank and retrieved to guide decision-making, without requiring any fine-tuning. Experiments show that MemOrb significantly improves both success rate and stability, achieving up to a 63 percentage-point gain in multi-turn success rate and delivering more consistent performance across repeated trials. Our results demonstrate that structured reflection is a powerful mechanism for enhancing long-term reliability of frozen LLM agents in customer service scenarios.

## 📝 요약

대형 언어 모델 기반 에이전트(LLM-based agents)는 고객 서비스에서 점점 더 많이 사용되지만, 세션 간 망각, 오류 반복, 지속적인 자기 개선 부족 등의 문제로 인해 신뢰성이 떨어집니다. 이를 해결하기 위해 우리는 작업 성공률과 일관성 지표인 Pass$^k$를 강조합니다. 기존 접근 방식의 한계를 극복하기 위해, 우리는 MemOrb라는 경량의 플러그 앤 플레이 언어 강화 메모리 레이어를 제안합니다. MemOrb는 다중 회차 상호작용을 압축된 전략 반영으로 저장하고, 이를 의사결정에 활용합니다. 실험 결과, MemOrb는 성공률과 안정성을 크게 향상시켜, 다중 회차 성공률에서 최대 63% 포인트의 향상을 이루고, 반복 실험에서도 일관된 성능을 제공합니다. 이는 구조화된 반영이 고객 서비스 시나리오에서 LLM 에이전트의 장기 신뢰성을 향상시키는 강력한 메커니즘임을 보여줍니다.

## 🎯 주요 포인트

- 1. LLM 기반 에이전트는 세션 간 망각, 오류 반복, 지속적인 자기 개선 부족으로 인해 고객 서비스에서 신뢰성이 떨어진다.
- 2. 작업 성공률과 일관성 지표는 LLM 에이전트의 안정성과 일관성을 평가하는 중요한 척도이다.
- 3. MemOrb는 멀티턴 상호작용을 전략적 반영으로 압축하여 저장하고 의사결정을 안내하는 경량의 플러그 앤 플레이 메모리 레이어이다.
- 4. MemOrb는 멀티턴 성공률을 최대 63% 포인트 향상시키고 반복 실험에서 일관된 성능을 제공한다.
- 5. 구조화된 반영은 고객 서비스 시나리오에서 LLM 에이전트의 장기적 신뢰성을 향상시키는 강력한 메커니즘이다.


---

*Generated on 2025-09-24 14:00:41*