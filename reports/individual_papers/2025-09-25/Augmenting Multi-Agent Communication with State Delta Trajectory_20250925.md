---
keywords:
  - Large Language Model
  - State Delta Encoding
  - Multi-Agent Systems
  - Natural Language Processing
category: cs.CL
publish_date: 2025-09-25
arxiv_id: 2506.19209
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:56:13.626882",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "State Delta Encoding",
    "Multi-Agent Systems",
    "Natural Language Processing"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "State Delta Encoding": 0.78,
    "Multi-Agent Systems": 0.82,
    "Natural Language Processing": 0.8
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
        "rationale": "Central to the paper's discussion on multi-agent systems and communication protocols.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "State Delta Encoding",
        "canonical": "State Delta Encoding",
        "aliases": [
          "SDE"
        ],
        "category": "unique_technical",
        "rationale": "A novel method proposed in the paper to enhance communication in multi-agent systems.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Multi-Agent Systems",
        "canonical": "Multi-Agent Systems",
        "aliases": [
          "MAS"
        ],
        "category": "specific_connectable",
        "rationale": "The paper focuses on improving communication within these systems, making it a key concept.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "Natural Language Tokens",
        "canonical": "Natural Language Processing",
        "aliases": [
          "NLP Tokens"
        ],
        "category": "broad_technical",
        "rationale": "Integral to the communication protocol discussed, linking to broader NLP concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experimental results"
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
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "State Delta Encoding",
      "resolved_canonical": "State Delta Encoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Multi-Agent Systems",
      "resolved_canonical": "Multi-Agent Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Natural Language Tokens",
      "resolved_canonical": "Natural Language Processing",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Augmenting Multi-Agent Communication with State Delta Trajectory

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2506.19209.pdf)
**Category**: cs.CL
**Published**: 2025-09-25
**ArXiv ID**: [2506.19209](https://arxiv.org/abs/2506.19209)

## 🔗 유사한 논문
- [[2025-09-23/A State-Update Prompting Strategy for Efficient and Robust Multi-turn Dialogue_20250923|A State-Update Prompting Strategy for Efficient and Robust Multi-turn Dialogue]] (86.3% similar)
- [[2025-09-24/Difficulty-Aware Agent Orchestration in LLM-Powered Workflows_20250924|Difficulty-Aware Agent Orchestration in LLM-Powered Workflows]] (84.6% similar)
- [[2025-09-22/Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context_20250922|Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context]] (83.1% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (83.1% similar)
- [[2025-09-19/Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models: Multi-Agent Consensus Alignment]] (83.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]], [[keywords/Natural Language Processing|Natural Language Processing]]
**🔗 Specific Connectable**: [[keywords/Multi-Agent Systems|Multi-Agent Systems]]
**⚡ Unique Technical**: [[keywords/State Delta Encoding|State Delta Encoding]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.19209v2 Announce Type: replace 
Abstract: Multi-agent techniques such as role playing or multi-turn debates have been shown to be effective in improving the performance of large language models (LLMs) in downstream tasks. Despite their differences in workflows, existing multi-agent systems constructed from a single base LLM mostly use natural language for agent communication. While this is appealing for its simplicity and interpretability, it also introduces inevitable information loss as one model must down sample its continuous state vectors to discrete tokens before transferring them to the other model. Such losses are particularly significant when the information to transfer is not simple facts, but reasoning logics or abstractive thoughts. To tackle this problem, we propose a new communication protocol that transfers both natural language tokens and token-wise state transition trajectory from one agent to another. Particularly, compared to the actual state value, we find that the sequence of state changes in LLMs after generating each token can better reflect the information hidden behind the inference process. We propose a State Delta Encoding (SDE) method to represent state transition trajectories. The experimental results show that multi-agent systems with SDE achieve SOTA performance compared to other communication protocols, particularly in tasks that involve complex reasoning.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 성능을 향상시키기 위한 다중 에이전트 시스템에서의 새로운 통신 프로토콜을 제안합니다. 기존의 다중 에이전트 시스템은 주로 자연어를 사용하여 에이전트 간의 정보를 교환하지만, 이는 정보 손실을 초래할 수 있습니다. 특히, 복잡한 추론 논리나 추상적 사고를 전달할 때 이러한 손실이 두드러집니다. 이를 해결하기 위해, 이 연구는 자연어 토큰과 토큰별 상태 전이 경로를 함께 전송하는 새로운 프로토콜을 제안합니다. 제안된 상태 델타 인코딩(SDE) 방법은 LLM이 각 토큰을 생성한 후의 상태 변화를 나타내며, 이는 추론 과정의 숨겨진 정보를 더 잘 반영합니다. 실험 결과, SDE를 사용하는 다중 에이전트 시스템은 복잡한 추론이 필요한 작업에서 최첨단(SOTA) 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 다중 에이전트 기법은 대형 언어 모델(LLM)의 다운스트림 작업 성능을 향상시키는 데 효과적이다.
- 2. 기존 다중 에이전트 시스템은 주로 자연어를 사용하여 에이전트 간의 의사소통을 하지만, 이는 정보 손실을 초래할 수 있다.
- 3. 정보 손실 문제를 해결하기 위해 자연어 토큰과 토큰별 상태 전이 경로를 함께 전송하는 새로운 통신 프로토콜을 제안한다.
- 4. 상태 전이 경로를 나타내기 위해 제안된 State Delta Encoding(SDE) 방법은 복잡한 추론 작업에서 SOTA 성능을 달성한다.
- 5. 각 토큰 생성 후 LLM의 상태 변화 시퀀스가 추론 과정의 숨겨진 정보를 더 잘 반영할 수 있다.


---

*Generated on 2025-09-26 08:56:13*