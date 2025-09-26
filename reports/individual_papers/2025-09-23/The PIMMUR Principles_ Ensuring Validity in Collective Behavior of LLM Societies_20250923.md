---
keywords:
  - Large Language Model
  - PIMMUR Principles
  - Social Simulation
  - Collective Behavior
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.18052
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:36:46.218004",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "PIMMUR Principles",
    "Social Simulation",
    "Collective Behavior"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "PIMMUR Principles": 0.88,
    "Social Simulation": 0.8,
    "Collective Behavior": 0.82
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
        "rationale": "Central to the study, linking to foundational concepts in AI.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "PIMMUR principles",
        "canonical": "PIMMUR Principles",
        "aliases": [
          "PIMMUR"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel framework for evaluating LLM societies.",
        "novelty_score": 0.95,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "social simulation",
        "canonical": "Social Simulation",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Key application area for LLMs, relevant for interdisciplinary links.",
        "novelty_score": 0.45,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "collective behavior",
        "canonical": "Collective Behavior",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Essential concept for understanding agent interactions in simulations.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "methodological flaws",
      "experimental designs"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "PIMMUR principles",
      "resolved_canonical": "PIMMUR Principles",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "social simulation",
      "resolved_canonical": "Social Simulation",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "collective behavior",
      "resolved_canonical": "Collective Behavior",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# The PIMMUR Principles: Ensuring Validity in Collective Behavior of LLM Societies

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18052.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.18052](https://arxiv.org/abs/2509.18052)

## 🔗 유사한 논문
- [[2025-09-18/Emergent Social Dynamics of LLM Agents in the El Farol Bar Problem_20250918|Emergent Social Dynamics of LLM Agents in the El Farol Bar Problem]] (85.5% similar)
- [[2025-09-17/Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (83.5% similar)
- [[2025-09-23/Generalizability of Large Language Model-Based Agents_ A Comprehensive Survey_20250923|Generalizability of Large Language Model-Based Agents: A Comprehensive Survey]] (83.4% similar)
- [[2025-09-19/Evaluation and Facilitation of Online Discussions in the LLM Era_ A Survey_20250919|Evaluation and Facilitation of Online Discussions in the LLM Era: A Survey]] (83.3% similar)
- [[2025-09-23/Time to Talk_ LLM Agents for Asynchronous Group Communication in Mafia Games_20250923|Time to Talk: LLM Agents for Asynchronous Group Communication in Mafia Games]] (83.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Social Simulation|Social Simulation]], [[keywords/Collective Behavior|Collective Behavior]]
**⚡ Unique Technical**: [[keywords/PIMMUR Principles|PIMMUR Principles]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18052v1 Announce Type: new 
Abstract: Large Language Models (LLMs) are increasingly used for social simulation, where populations of agents are expected to reproduce human-like collective behavior. However, we find that many recent studies adopt experimental designs that systematically undermine the validity of their claims. From a survey of over 40 papers, we identify six recurring methodological flaws: agents are often homogeneous (Profile), interactions are absent or artificially imposed (Interaction), memory is discarded (Memory), prompts tightly control outcomes (Minimal-Control), agents can infer the experimental hypothesis (Unawareness), and validation relies on simplified theoretical models rather than real-world data (Realism). For instance, GPT-4o and Qwen-3 correctly infer the underlying social experiment in 53.1% of cases when given instructions from prior work-violating the Unawareness principle. We formalize these six requirements as the PIMMUR principles and argue they are necessary conditions for credible LLM-based social simulation. To demonstrate their impact, we re-run five representative studies using a framework that enforces PIMMUR and find that the reported social phenomena frequently fail to emerge under more rigorous conditions. Our work establishes methodological standards for LLM-based multi-agent research and provides a foundation for more reliable and reproducible claims about "AI societies."

## 📝 요약

대형 언어 모델(LLM)을 활용한 사회 시뮬레이션 연구에서 자주 발생하는 여섯 가지 방법론적 결함을 지적합니다. 연구는 에이전트의 동질성, 상호작용 부재, 기억 상실, 결과를 엄격히 통제하는 프롬프트, 실험 가설 추론 가능성, 현실 데이터 대신 이론 모델에 의존하는 검증을 문제로 삼습니다. 이러한 결함을 PIMMUR 원칙으로 정리하고, 이를 적용한 재실험에서 기존 연구의 사회적 현상이 자주 나타나지 않음을 확인했습니다. 본 연구는 LLM 기반 다중 에이전트 연구의 방법론적 기준을 확립하고, 신뢰할 수 있는 AI 사회 연구의 기초를 제공합니다.

## 🎯 주요 포인트

- 1. 대규모 언어 모델(LLM)은 사회 시뮬레이션에서 인간과 유사한 집단 행동을 재현하는 데 사용되지만, 많은 연구가 실험 설계에서 체계적인 결함을 가지고 있습니다.
- 2. 조사한 40여 개의 논문에서 발견된 반복적인 방법론적 결함으로는 에이전트의 동질성, 상호작용의 부재, 메모리의 폐기, 결과를 엄격히 통제하는 프롬프트, 실험 가설을 추론할 수 있는 에이전트, 단순화된 이론 모델에 의존한 검증 등이 있습니다.
- 3. PIMMUR 원칙은 신뢰할 수 있는 LLM 기반 사회 시뮬레이션을 위한 필수 조건으로 제안되며, 이를 적용한 연구에서는 기존 연구에서 보고된 사회 현상이 엄격한 조건에서는 자주 나타나지 않음을 발견했습니다.
- 4. 본 연구는 LLM 기반 다중 에이전트 연구를 위한 방법론적 기준을 설정하고, "AI 사회"에 대한 더 신뢰할 수 있고 재현 가능한 주장을 위한 기초를 제공합니다.


---

*Generated on 2025-09-24 03:36:46*