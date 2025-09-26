<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:22:40.034687",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Difficulty-Aware Agentic Orchestration",
    "Variational Autoencoder",
    "Heterogeneous Large Language Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Difficulty-Aware Agentic Orchestration": 0.9,
    "Variational Autoencoder": 0.78,
    "Heterogeneous Large Language Models": 0.8
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
        "rationale": "Central to the paper's framework, linking it to existing LLM discussions enhances understanding.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Difficulty-Aware Agentic Orchestration",
        "canonical": "Difficulty-Aware Agentic Orchestration",
        "aliases": [
          "DAAO"
        ],
        "category": "unique_technical",
        "rationale": "A novel framework introduced in the paper, crucial for understanding its unique contribution.",
        "novelty_score": 0.95,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.9
      },
      {
        "surface": "Variational Autoencoder",
        "canonical": "Variational Autoencoder",
        "aliases": [
          "VAE"
        ],
        "category": "specific_connectable",
        "rationale": "Key component for difficulty estimation, linking to existing VAE literature enhances context.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Heterogeneous LLMs",
        "canonical": "Heterogeneous Large Language Models",
        "aliases": [
          "Heterogeneous LLMs"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the use of diverse LLMs, important for discussions on model diversity and efficiency.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "workflow",
      "operator selection",
      "benchmark"
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
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Difficulty-Aware Agentic Orchestration",
      "resolved_canonical": "Difficulty-Aware Agentic Orchestration",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Variational Autoencoder",
      "resolved_canonical": "Variational Autoencoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Heterogeneous LLMs",
      "resolved_canonical": "Heterogeneous Large Language Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Difficulty-Aware Agent Orchestration in LLM-Powered Workflows

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.11079.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.11079](https://arxiv.org/abs/2509.11079)

## 🔗 유사한 논문
- [[2025-09-19/An LLM-based multi-agent framework for agile effort estimation_20250919|An LLM-based multi-agent framework for agile effort estimation]] (87.0% similar)
- [[2025-09-19/(P)rior(D)yna(F)low_ A Priori Dynamic Workflow Construction via Multi-Agent Collaboration_20250919|(P)rior(D)yna(F)low: A Priori Dynamic Workflow Construction via Multi-Agent Collaboration]] (86.3% similar)
- [[2025-09-18/AppAgent v2_ Advanced Agent for Flexible Mobile Interactions_20250918|AppAgent v2: Advanced Agent for Flexible Mobile Interactions]] (85.7% similar)
- [[2025-09-22/Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context_20250922|Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context]] (85.7% similar)
- [[2025-09-23/A Large Language Model-based multi-agent manufacturing system for intelligent shopfloor_20250923|A Large Language Model-based multi-agent manufacturing system for intelligent shopfloor]] (84.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Variational Autoencoder|Variational Autoencoder]], [[keywords/Heterogeneous Large Language Models|Heterogeneous Large Language Models]]
**⚡ Unique Technical**: [[keywords/Difficulty-Aware Agentic Orchestration|Difficulty-Aware Agentic Orchestration]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.11079v2 Announce Type: replace 
Abstract: Large Language Model (LLM)-based agentic systems have shown strong capabilities across various tasks. However, existing multi-agent frameworks often rely on static or task-level workflows, which either over-process simple queries or underperform on complex ones, while also neglecting the efficiency-performance trade-offs across heterogeneous LLMs. To address these limitations, we propose Difficulty-Aware Agentic Orchestration (DAAO), a dynamic framework that adapts workflow depth, operator selection, and LLM assignment based on the difficulty of each input query. DAAO comprises three interdependent modules: a variational autoencoder (VAE) for difficulty estimation, a modular operator allocator, and a cost- and performance-aware LLM router. By leveraging heterogeneous LLMs and dynamically tailoring workflows, DAAO enables fine-grained, query-specific reasoning strategies. DAAO outperforms prior multi-agent systems in both accuracy and inference efficiency across six benchmarks. We will release our code and implementation details upon publication.

## 📝 요약

이 논문은 대형 언어 모델(LLM) 기반의 에이전트 시스템의 한계를 극복하기 위해 난이도 인식 에이전트 오케스트레이션(DAAO)이라는 동적 프레임워크를 제안합니다. 기존의 다중 에이전트 프레임워크는 고정된 워크플로우로 인해 간단한 쿼리를 과도하게 처리하거나 복잡한 쿼리에서 성능이 저하되는 문제가 있었습니다. DAAO는 입력 쿼리의 난이도에 따라 워크플로우의 깊이, 연산자 선택, LLM 할당을 조정하는 세 가지 모듈로 구성되어 있습니다. 이 시스템은 다양한 LLM을 활용하여 쿼리별로 세밀한 추론 전략을 제공하며, 여섯 개의 벤치마크에서 정확성과 추론 효율성 면에서 기존 시스템을 능가합니다. 코드와 구현 세부사항은 출판 시 공개될 예정입니다.

## 🎯 주요 포인트

- 1. 기존의 다중 에이전트 프레임워크는 정적이거나 작업 수준의 워크플로에 의존하여 간단한 쿼리를 과도하게 처리하거나 복잡한 쿼리에서 성능이 저하되는 문제를 가지고 있습니다.
- 2. DAAO는 입력 쿼리의 난이도에 따라 워크플로 깊이, 운영자 선택 및 LLM 할당을 동적으로 조정하는 프레임워크입니다.
- 3. DAAO는 난이도 추정을 위한 변분 오토인코더(VAE), 모듈형 운영자 할당자, 비용 및 성능을 고려한 LLM 라우터로 구성되어 있습니다.
- 4. 이 프레임워크는 이질적인 LLM을 활용하고 워크플로를 동적으로 조정하여 쿼리별 세밀한 추론 전략을 가능하게 합니다.
- 5. DAAO는 여섯 가지 벤치마크에서 정확도와 추론 효율성 면에서 기존 다중 에이전트 시스템을 능가합니다.


---

*Generated on 2025-09-24 14:22:40*