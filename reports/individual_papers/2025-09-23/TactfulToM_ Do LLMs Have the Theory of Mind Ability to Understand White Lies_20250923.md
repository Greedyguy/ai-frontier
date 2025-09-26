---
keywords:
  - Large Language Model
  - Theory of Mind
  - White Lies
  - Human-in-the-Loop
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17054
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:42:42.230860",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Theory of Mind",
    "White Lies",
    "Human-in-the-Loop"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Theory of Mind": 0.8,
    "White Lies": 0.78,
    "Human-in-the-Loop": 0.77
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
        "rationale": "Central to the study, linking it to broader discussions on language models and AI capabilities.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Theory of Mind",
        "canonical": "Theory of Mind",
        "aliases": [
          "ToM"
        ],
        "category": "unique_technical",
        "rationale": "Key concept for understanding cognitive abilities in AI, relevant to psychological and AI research.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.8
      },
      {
        "surface": "white lies",
        "canonical": "White Lies",
        "aliases": [
          "prosocial lies"
        ],
        "category": "unique_technical",
        "rationale": "Specific focus of the paper, relevant for discussions on social reasoning and ethics in AI.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "human-in-the-loop",
        "canonical": "Human-in-the-Loop",
        "aliases": [
          "HITL"
        ],
        "category": "specific_connectable",
        "rationale": "Describes a methodology crucial for training and evaluating AI models with human guidance.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "benchmark",
      "performance",
      "conversation"
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
      "candidate_surface": "Theory of Mind",
      "resolved_canonical": "Theory of Mind",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "white lies",
      "resolved_canonical": "White Lies",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "human-in-the-loop",
      "resolved_canonical": "Human-in-the-Loop",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# TactfulToM: Do LLMs Have the Theory of Mind Ability to Understand White Lies?

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17054.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17054](https://arxiv.org/abs/2509.17054)

## 🔗 유사한 논문
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (84.1% similar)
- [[2025-09-19/Rationality Check! Benchmarking the Rationality of Large Language Models_20250919|Rationality Check! Benchmarking the Rationality of Large Language Models]] (84.0% similar)
- [[2025-09-23/Benchmarking Contextual and Paralinguistic Reasoning in Speech-LLMs_ A Case Study with In-the-Wild Data_20250923|Benchmarking Contextual and Paralinguistic Reasoning in Speech-LLMs: A Case Study with In-the-Wild Data]] (83.6% similar)
- [[2025-09-22/Can Large Language Models Infer Causal Relationships from Real-World Text?_20250922|Can Large Language Models Infer Causal Relationships from Real-World Text?]] (83.2% similar)
- [[2025-09-19/OnlineMate_ An LLM-Based Multi-Agent Companion System for Cognitive Support in Online Learning_20250919|OnlineMate: An LLM-Based Multi-Agent Companion System for Cognitive Support in Online Learning]] (83.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Human-in-the-Loop|Human-in-the-Loop]]
**⚡ Unique Technical**: [[keywords/Theory of Mind|Theory of Mind]], [[keywords/White Lies|White Lies]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17054v1 Announce Type: cross 
Abstract: While recent studies explore Large Language Models' (LLMs) performance on Theory of Mind (ToM) reasoning tasks, research on ToM abilities that require more nuanced social context is limited, such as white lies. We introduce TactfulToM, a novel English benchmark designed to evaluate LLMs' ability to understand white lies within real-life conversations and reason about prosocial motivations behind them, particularly when they are used to spare others' feelings and maintain social harmony. Our benchmark is generated through a multi-stage human-in-the-loop pipeline where LLMs expand manually designed seed stories into conversations to maintain the information asymmetry between participants necessary for authentic white lies. We show that TactfulToM is challenging for state-of-the-art models, which perform substantially below humans, revealing shortcomings in their ability to fully comprehend the ToM reasoning that enables true understanding of white lies.

## 📝 요약

최근 연구에서는 대형 언어 모델(LLM)의 마음 이론(ToM) 추론 과제 수행 능력을 탐구하고 있지만, 보다 미묘한 사회적 맥락이 필요한 ToM 능력, 예를 들어 선의의 거짓말에 대한 연구는 제한적입니다. 우리는 TactfulToM이라는 새로운 영어 벤치마크를 도입하여 LLM이 실제 대화에서 선의의 거짓말을 이해하고, 이를 통해 타인의 감정을 배려하고 사회적 조화를 유지하려는 친사회적 동기를 추론할 수 있는 능력을 평가합니다. 이 벤치마크는 인간 참여자가 수작업으로 설계한 초기 이야기를 LLM이 확장하여 대화로 발전시키는 다단계 프로세스를 통해 생성됩니다. 이를 통해 참가자 간 정보 비대칭을 유지하여 진정한 선의의 거짓말을 평가합니다. TactfulToM은 최신 모델에게 도전 과제를 제시하며, 이 모델들이 인간보다 훨씬 낮은 성과를 보임으로써 선의의 거짓말을 완전히 이해하는 데 필요한 ToM 추론 능력의 한계를 드러냅니다.

## 🎯 주요 포인트

- 1. TactfulToM은 대형 언어 모델(LLMs)이 실제 대화에서 백색 거짓말을 이해하고 그 뒤에 있는 친사회적 동기를 추론하는 능력을 평가하기 위해 설계된 새로운 영어 벤치마크입니다.
- 2. 이 벤치마크는 인간 참여형 다단계 파이프라인을 통해 생성되며, LLM이 수동으로 설계된 시드 스토리를 대화로 확장하여 참가자 간 정보 비대칭을 유지합니다.
- 3. TactfulToM은 최신 모델들에게 도전적인 과제로, 인간보다 현저히 낮은 성능을 보이며 백색 거짓말의 진정한 이해를 가능하게 하는 마음 이론(ToM) 추론 능력의 한계를 드러냅니다.


---

*Generated on 2025-09-23 23:42:42*