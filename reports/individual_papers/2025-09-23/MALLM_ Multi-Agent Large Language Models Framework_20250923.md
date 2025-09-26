---
keywords:
  - Multi-Agent Large Language Models
  - Multi-agent debate
  - Large Language Model
  - Hugging Face dataset
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.11656
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:29:08.145927",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-Agent Large Language Models",
    "Multi-agent debate",
    "Large Language Model",
    "Hugging Face dataset"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multi-Agent Large Language Models": 0.8,
    "Multi-agent debate": 0.78,
    "Large Language Model": 0.85,
    "Hugging Face dataset": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multi-Agent Large Language Models",
        "canonical": "Multi-Agent Large Language Models",
        "aliases": [
          "MALLM"
        ],
        "category": "unique_technical",
        "rationale": "This framework is central to the paper and represents a novel configuration for multi-agent debates.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multi-agent debate",
        "canonical": "Multi-agent debate",
        "aliases": [
          "MAD"
        ],
        "category": "unique_technical",
        "rationale": "The concept of multi-agent debate is a unique approach to augmenting collective intelligence and is central to the paper.",
        "novelty_score": 0.7,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are a fundamental component of the framework and link to existing research in NLP.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Hugging Face dataset",
        "canonical": "Hugging Face dataset",
        "aliases": [
          "Hugging Face"
        ],
        "category": "specific_connectable",
        "rationale": "Hugging Face datasets are widely used in NLP research and facilitate the evaluation of the proposed framework.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "tool use",
      "evaluation pipeline"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multi-Agent Large Language Models",
      "resolved_canonical": "Multi-Agent Large Language Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multi-agent debate",
      "resolved_canonical": "Multi-agent debate",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Hugging Face dataset",
      "resolved_canonical": "Hugging Face dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# MALLM: Multi-Agent Large Language Models Framework

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.11656.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.11656](https://arxiv.org/abs/2509.11656)

## 🔗 유사한 논문
- [[2025-09-19/Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models: Multi-Agent Consensus Alignment]] (83.3% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning: An Indispensable Path towards New-Generation Large Language Models]] (82.5% similar)
- [[2025-09-23/AgentMaster_ A Multi-Agent Conversational Framework Using A2A and MCP Protocols for Multimodal Information Retrieval and Analysis_20250923|AgentMaster: A Multi-Agent Conversational Framework Using A2A and MCP Protocols for Multimodal Information Retrieval and Analysis]] (81.9% similar)
- [[2025-09-19/A Knowledge-driven Adaptive Collaboration of LLMs for Enhancing Medical Decision-making_20250919|A Knowledge-driven Adaptive Collaboration of LLMs for Enhancing Medical Decision-making]] (81.9% similar)
- [[2025-09-22/MEDAL_ A Framework for Benchmarking LLMs as Multilingual Open-Domain Dialogue Evaluators_20250922|MEDAL: A Framework for Benchmarking LLMs as Multilingual Open-Domain Dialogue Evaluators]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Hugging Face dataset|Hugging Face dataset]]
**⚡ Unique Technical**: [[keywords/Multi-Agent Large Language Models|Multi-Agent Large Language Models]], [[keywords/Multi-agent debate|Multi-agent debate]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.11656v2 Announce Type: replace-cross 
Abstract: Multi-agent debate (MAD) has demonstrated the ability to augment collective intelligence by scaling test-time compute and leveraging expertise. Current frameworks for multi-agent debate are often designed towards tool use, lack integrated evaluation, or provide limited configurability of agent personas, response generators, discussion paradigms, and decision protocols. We introduce MALLM (Multi-Agent Large Language Models), an open-source framework that enables systematic analysis of MAD components. MALLM offers more than 144 unique configurations of MAD, including (1) agent personas (e.g., Expert, Personality), (2) response generators (e.g., Critical, Reasoning), (3) discussion paradigms (e.g., Memory, Relay), and (4) decision protocols (e.g., Voting, Consensus). MALLM uses simple configuration files to define a debate. Furthermore, MALLM can load any textual Hugging Face dataset (e.g., MMLU-Pro, WinoGrande) and provides an evaluation pipeline for easy comparison of MAD configurations. MALLM enables researchers to systematically configure, run, and evaluate debates for their problems, facilitating the understanding of the components and their interplay.

## 📝 요약

이 논문은 다중 에이전트 토론(MAD)의 구성 요소를 체계적으로 분석할 수 있는 오픈 소스 프레임워크인 MALLM을 소개합니다. MALLM은 144가지 이상의 다양한 MAD 구성 옵션을 제공하며, 에이전트 페르소나, 응답 생성기, 토론 패러다임, 의사 결정 프로토콜 등 다양한 요소를 포함합니다. 또한, MALLM은 Hugging Face의 텍스트 데이터셋을 로드하고 MAD 구성의 비교 평가를 위한 파이프라인을 제공합니다. 이를 통해 연구자들은 문제에 맞는 토론을 구성, 실행, 평가할 수 있으며, 구성 요소와 그 상호작용에 대한 이해를 돕습니다.

## 🎯 주요 포인트

- 1. MALLM은 다중 에이전트 토론(MAD)의 구성 요소를 체계적으로 분석할 수 있는 오픈 소스 프레임워크입니다.
- 2. MALLM은 에이전트 페르소나, 응답 생성기, 토론 패러다임, 결정 프로토콜 등 144가지 이상의 고유한 MAD 구성을 제공합니다.
- 3. MALLM은 간단한 구성 파일을 사용하여 토론을 정의하고, 다양한 텍스트 데이터셋을 로드하여 MAD 구성의 비교 평가를 용이하게 합니다.
- 4. 연구자들은 MALLM을 통해 자신들의 문제에 맞는 토론을 구성, 실행, 평가할 수 있으며, 구성 요소와 그 상호작용에 대한 이해를 촉진할 수 있습니다.


---

*Generated on 2025-09-24 01:29:08*