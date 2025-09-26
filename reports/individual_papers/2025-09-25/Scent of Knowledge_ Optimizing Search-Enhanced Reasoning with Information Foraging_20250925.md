---
keywords:
  - Large Language Model
  - Retrieval-Augmented Reasoning
  - Information Foraging Theory
  - Adaptive Inference-Time Retrieval
category: cs.CL
publish_date: 2025-09-25
arxiv_id: 2505.09316
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:54:07.656289",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Retrieval-Augmented Reasoning",
    "Information Foraging Theory",
    "Adaptive Inference-Time Retrieval"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.8,
    "Retrieval-Augmented Reasoning": 0.78,
    "Information Foraging Theory": 0.77,
    "Adaptive Inference-Time Retrieval": 0.72
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
        "rationale": "Large Language Models are central to the paper's discussion on retrieval-augmented reasoning.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "Retrieval-Augmented Reasoning",
        "canonical": "Retrieval-Augmented Reasoning",
        "aliases": [
          "RAR"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach proposed in the paper, highlighting its unique contribution to adaptive reasoning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Information Foraging Theory",
        "canonical": "Information Foraging Theory",
        "aliases": [
          "IFT"
        ],
        "category": "specific_connectable",
        "rationale": "IFT is a foundational theory that underpins the proposed framework, connecting to broader information-seeking behaviors.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Adaptive Inference-Time Retrieval",
        "canonical": "Adaptive Inference-Time Retrieval",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This concept is key to the paper's innovation, emphasizing dynamic retrieval processes.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
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
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Retrieval-Augmented Reasoning",
      "resolved_canonical": "Retrieval-Augmented Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Information Foraging Theory",
      "resolved_canonical": "Information Foraging Theory",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Adaptive Inference-Time Retrieval",
      "resolved_canonical": "Adaptive Inference-Time Retrieval",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Scent of Knowledge: Optimizing Search-Enhanced Reasoning with Information Foraging

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.09316.pdf)
**Category**: cs.CL
**Published**: 2025-09-25
**ArXiv ID**: [2505.09316](https://arxiv.org/abs/2505.09316)

## 🔗 유사한 논문
- [[2025-09-22/Search and Refine During Think_ Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning_20250922|Search and Refine During Think: Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning]] (87.3% similar)
- [[2025-09-24/ReSearch_ Learning to Reason with Search for LLMs via Reinforcement Learning_20250924|ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning]] (87.0% similar)
- [[2025-09-23/GRIL_ Knowledge Graph Retrieval-Integrated Learning with Large Language Models_20250923|GRIL: Knowledge Graph Retrieval-Integrated Learning with Large Language Models]] (86.5% similar)
- [[2025-09-23/Retrieval Enhanced Feedback via In-context Neural Error-book_20250923|Retrieval Enhanced Feedback via In-context Neural Error-book]] (85.9% similar)
- [[2025-09-22/Query Optimization for Parametric Knowledge Refinement in Retrieval-Augmented Large Language Models_20250922|Query Optimization for Parametric Knowledge Refinement in Retrieval-Augmented Large Language Models]] (85.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Information Foraging Theory|Information Foraging Theory]]
**⚡ Unique Technical**: [[keywords/Retrieval-Augmented Reasoning|Retrieval-Augmented Reasoning]], [[keywords/Adaptive Inference-Time Retrieval|Adaptive Inference-Time Retrieval]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.09316v2 Announce Type: replace 
Abstract: Augmenting large language models (LLMs) with external retrieval has become a standard method to address their inherent knowledge cutoff limitations. However, traditional retrieval-augmented generation methods employ static, pre-inference retrieval strategies, making them inadequate for complex tasks involving ambiguous, multi-step, or evolving information needs. Recent advances in test-time scaling techniques have demonstrated significant potential in enabling LLMs to dynamically interact with external tools, motivating the shift toward adaptive inference-time retrieval. Inspired by Information Foraging Theory (IFT), we propose InForage, a reinforcement learning framework that formalizes retrieval-augmented reasoning as a dynamic information-seeking process. Unlike existing approaches, InForage explicitly rewards intermediate retrieval quality, encouraging LLMs to iteratively gather and integrate information through adaptive search behaviors. To facilitate training, we construct a human-guided dataset capturing iterative search and reasoning trajectories for complex, real-world web tasks. Extensive evaluations across general question answering, multi-hop reasoning tasks, and a newly developed real-time web QA dataset demonstrate InForage's superior performance over baseline methods. These results highlight InForage's effectiveness in building robust, adaptive, and efficient reasoning agents.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 지식 한계를 극복하기 위해 외부 검색을 동적으로 활용하는 InForage라는 강화 학습 프레임워크를 제안합니다. 기존의 정적 검색 방식과 달리, InForage는 정보 탐색 이론(IFT)을 기반으로 하여 검색-강화 추론을 동적 정보 탐색 과정으로 공식화합니다. 이 방법은 중간 검색 품질을 보상하여 LLM이 적응적 검색 행동을 통해 정보를 반복적으로 수집하고 통합하도록 유도합니다. 복잡한 웹 작업을 위한 인간 안내 데이터셋을 구축하여 훈련을 지원하며, 일반 질의응답, 다중 단계 추론, 실시간 웹 QA 데이터셋에서 뛰어난 성능을 보였습니다. InForage는 강력하고 적응적이며 효율적인 추론 에이전트를 구축하는 데 효과적임을 입증했습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 지식 한계 문제를 해결하기 위해 외부 검색을 활용하는 방법이 표준으로 자리 잡고 있습니다.
- 2. 기존의 검색 보강 생성 방법은 정적이며 복잡한 작업에 적합하지 않다는 한계를 가지고 있습니다.
- 3. InForage는 정보 탐색 이론(IFT)에 영감을 받아 강화 학습 프레임워크를 통해 검색 보강 추론을 동적 정보 탐색 과정으로 공식화합니다.
- 4. InForage는 중간 검색 품질을 명시적으로 보상하여 LLM이 적응적 검색 행동을 통해 정보를 반복적으로 수집하고 통합하도록 유도합니다.
- 5. 다양한 평가에서 InForage는 일반 질문 응답, 다중 단계 추론 작업 및 실시간 웹 QA 데이터셋에서 기존 방법보다 뛰어난 성능을 보였습니다.


---

*Generated on 2025-09-26 08:54:07*