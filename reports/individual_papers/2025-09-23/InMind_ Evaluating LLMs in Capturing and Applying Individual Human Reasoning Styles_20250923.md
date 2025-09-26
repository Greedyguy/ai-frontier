---
keywords:
  - Large Language Model
  - Social Deduction Games
  - Cognitively Grounded Evaluation Framework
  - Reasoning-Enhanced LLMs
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2508.16072
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:32:04.826361",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Social Deduction Games",
    "Cognitively Grounded Evaluation Framework",
    "Reasoning-Enhanced LLMs"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Social Deduction Games": 0.78,
    "Cognitively Grounded Evaluation Framework": 0.82,
    "Reasoning-Enhanced LLMs": 0.79
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
        "rationale": "This term is central to the paper's focus on evaluating AI models in reasoning tasks.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Social Deduction Games",
        "canonical": "Social Deduction Games",
        "aliases": [
          "SDGs"
        ],
        "category": "unique_technical",
        "rationale": "This concept is crucial for understanding the context in which reasoning styles are evaluated.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Cognitively Grounded Evaluation Framework",
        "canonical": "Cognitively Grounded Evaluation Framework",
        "aliases": [
          "InMind"
        ],
        "category": "unique_technical",
        "rationale": "This framework is a novel approach introduced in the paper for evaluating reasoning styles.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Reasoning-Enhanced LLMs",
        "canonical": "Reasoning-Enhanced LLMs",
        "aliases": [
          "DeepSeek-R1"
        ],
        "category": "evolved_concepts",
        "rationale": "This represents an advancement in LLMs, focusing on style-sensitive reasoning.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "Observer",
      "Participant",
      "Avalon"
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
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Social Deduction Games",
      "resolved_canonical": "Social Deduction Games",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Cognitively Grounded Evaluation Framework",
      "resolved_canonical": "Cognitively Grounded Evaluation Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Reasoning-Enhanced LLMs",
      "resolved_canonical": "Reasoning-Enhanced LLMs",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# InMind: Evaluating LLMs in Capturing and Applying Individual Human Reasoning Styles

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2508.16072.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2508.16072](https://arxiv.org/abs/2508.16072)

## 🔗 유사한 논문
- [[2025-09-23/Evaluating LLM-Generated Versus Human-Authored Responses in Role-Play Dialogues_20250923|Evaluating LLM-Generated Versus Human-Authored Responses in Role-Play Dialogues]] (85.9% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (85.7% similar)
- [[2025-09-23/Evaluating Behavioral Alignment in Conflict Dialogue_ A Multi-Dimensional Comparison of LLM Agents and Humans_20250923|Evaluating Behavioral Alignment in Conflict Dialogue: A Multi-Dimensional Comparison of LLM Agents and Humans]] (85.6% similar)
- [[2025-09-22/Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics_20250922|Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics]] (85.2% similar)
- [[2025-09-22/DivLogicEval_ A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models_20250922|DivLogicEval: A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models]] (85.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Social Deduction Games|Social Deduction Games]], [[keywords/Cognitively Grounded Evaluation Framework|Cognitively Grounded Evaluation Framework]]
**🚀 Evolved Concepts**: [[keywords/Reasoning-Enhanced LLMs|Reasoning-Enhanced LLMs]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.16072v3 Announce Type: replace 
Abstract: LLMs have shown strong performance on human-centric reasoning tasks. While previous evaluations have explored whether LLMs can infer intentions or detect deception, they often overlook the individualized reasoning styles that influence how people interpret and act in social contexts. Social deduction games (SDGs) provide a natural testbed for evaluating individualized reasoning styles, where different players may adopt diverse but contextually valid reasoning strategies under identical conditions. To address this, we introduce InMind, a cognitively grounded evaluation framework designed to assess whether LLMs can capture and apply personalized reasoning styles in SDGs. InMind enhances structured gameplay data with round-level strategy traces and post-game reflections, collected under both Observer and Participant modes. It supports four cognitively motivated tasks that jointly evaluate both static alignment and dynamic adaptation. As a case study, we apply InMind to the game Avalon, evaluating 11 state-of-the-art LLMs. General-purpose LLMs, even GPT-4o frequently rely on lexical cues, struggling to anchor reflections in temporal gameplay or adapt to evolving strategies. In contrast, reasoning-enhanced LLMs like DeepSeek-R1 exhibit early signs of style-sensitive reasoning. These findings reveal key limitations in current LLMs' capacity for individualized, adaptive reasoning, and position InMind as a step toward cognitively aligned human-AI interaction.

## 📝 요약

이 논문은 인간 중심의 추론 과제를 수행하는 대형 언어 모델(LLM)의 성능을 평가합니다. 기존 연구는 LLM이 의도를 추론하거나 속임수를 감지할 수 있는지를 탐구했지만, 개별화된 추론 스타일을 간과했습니다. 이를 해결하기 위해, 저자들은 사회적 추론 게임(SDG)에서 LLM의 개인화된 추론 스타일을 평가하는 InMind라는 평가 프레임워크를 제안합니다. InMind는 게임 데이터와 전략 추적, 게임 후 반성 자료를 활용하여 LLM의 정적 정렬과 동적 적응 능력을 평가합니다. Avalon 게임을 통해 11개의 최신 LLM을 평가한 결과, 일반 LLM은 어휘적 단서에 의존하며, 추론 강화 LLM은 스타일에 민감한 추론을 보여줍니다. 이는 현재 LLM의 개별화된 적응 추론의 한계를 드러내며, InMind가 인간-AI 상호작용의 인지적 정렬을 향한 진전을 제시함을 보여줍니다.

## 🎯 주요 포인트

- 1. LLMs는 인간 중심의 추론 작업에서 강력한 성능을 보여주지만, 개인화된 추론 스타일을 간과하는 경향이 있습니다.
- 2. InMind는 사회적 추론 게임(SDGs)에서 LLMs가 개인화된 추론 스타일을 포착하고 적용할 수 있는지를 평가하기 위한 인지 기반 평가 프레임워크입니다.
- 3. InMind는 관찰자 모드와 참가자 모드에서 수집된 전략 추적과 게임 후 반성을 통해 구조화된 게임 데이터를 강화합니다.
- 4. 일반적인 LLMs는 어휘적 단서에 의존하며, 시간적 게임플레이에 반영하거나 변화하는 전략에 적응하는 데 어려움을 겪습니다.
- 5. DeepSeek-R1과 같은 추론 강화 LLMs는 스타일에 민감한 추론의 초기 징후를 보이며, InMind는 인지적으로 정렬된 인간-AI 상호작용을 위한 진전을 나타냅니다.


---

*Generated on 2025-09-24 00:32:04*