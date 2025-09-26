<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:21:21.978229",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "RAG+",
    "Retrieval Augmented Generation",
    "Large Language Model",
    "Application-Aware Reasoning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "RAG+": 0.92,
    "Retrieval Augmented Generation": 0.89,
    "Large Language Model": 0.85,
    "Application-Aware Reasoning": 0.88
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "RAG+",
        "canonical": "RAG+",
        "aliases": [
          "Enhanced RAG",
          "RAG Plus"
        ],
        "category": "unique_technical",
        "rationale": "RAG+ represents a novel extension to Retrieval-Augmented Generation, enhancing its capability with application-aware reasoning.",
        "novelty_score": 0.85,
        "connectivity_score": 0.68,
        "specificity_score": 0.88,
        "link_intent_score": 0.92
      },
      {
        "surface": "Retrieval-Augmented Generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "RAG is a foundational concept in the paper, crucial for understanding the enhancements proposed by RAG+.",
        "novelty_score": 0.4,
        "connectivity_score": 0.87,
        "specificity_score": 0.78,
        "link_intent_score": 0.89
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the implementation and evaluation of RAG+.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Application-Aware Reasoning",
        "canonical": "Application-Aware Reasoning",
        "aliases": [
          "Task-Specific Reasoning"
        ],
        "category": "unique_technical",
        "rationale": "This concept is key to the novelty of RAG+, enabling it to bridge the gap between retrieval and application.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.88
      }
    ],
    "ban_list_suggestions": [
      "integration",
      "enhancing",
      "paradigms",
      "pipeline",
      "framework"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "RAG+",
      "resolved_canonical": "RAG+",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.68,
        "specificity": 0.88,
        "link_intent": 0.92
      }
    },
    {
      "candidate_surface": "Retrieval-Augmented Generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.87,
        "specificity": 0.78,
        "link_intent": 0.89
      }
    },
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
      "candidate_surface": "Application-Aware Reasoning",
      "resolved_canonical": "Application-Aware Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.88
      }
    }
  ]
}
-->

# RAG+: Enhancing Retrieval-Augmented Generation with Application-Aware Reasoning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.11555.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2506.11555](https://arxiv.org/abs/2506.11555)

## 🔗 유사한 논문
- [[2025-09-19/Enhancing Retrieval Augmentation via Adversarial Collaboration_20250919|Enhancing Retrieval Augmentation via Adversarial Collaboration]] (90.6% similar)
- [[2025-09-23/GRIL_ Knowledge Graph Retrieval-Integrated Learning with Large Language Models_20250923|GRIL: Knowledge Graph Retrieval-Integrated Learning with Large Language Models]] (90.1% similar)
- [[2025-09-19/Causal-Counterfactual RAG_ The Integration of Causal-Counterfactual Reasoning into RAG_20250919|Causal-Counterfactual RAG: The Integration of Causal-Counterfactual Reasoning into RAG]] (89.5% similar)
- [[2025-09-23/Rationale-Guided Retrieval Augmented Generation for Medical Question Answering_20250923|Rationale-Guided Retrieval Augmented Generation for Medical Question Answering]] (89.2% similar)
- [[2025-09-19/ImpRAG_ Retrieval-Augmented Generation with Implicit Queries_20250919|ImpRAG: Retrieval-Augmented Generation with Implicit Queries]] (89.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]]
**⚡ Unique Technical**: [[keywords/RAG+|RAG+]], [[keywords/Application-Aware Reasoning|Application-Aware Reasoning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.11555v4 Announce Type: replace 
Abstract: The integration of external knowledge through Retrieval-Augmented Generation (RAG) has become foundational in enhancing large language models (LLMs) for knowledge-intensive tasks. However, existing RAG paradigms often overlook the cognitive step of applying knowledge, leaving a gap between retrieved facts and task-specific reasoning. In this work, we introduce RAG+, a principled and modular extension that explicitly incorporates application-aware reasoning into the RAG pipeline. RAG+ constructs a dual corpus consisting of knowledge and aligned application examples, created either manually or automatically, and retrieves both jointly during inference. This design enables LLMs not only to access relevant information but also to apply it within structured, goal-oriented reasoning processes. Experiments across mathematical, legal, and medical domains, conducted on multiple models, demonstrate that RAG+ consistently outperforms standard RAG variants, achieving average improvements of 3-5%, and peak gains up to 13.5% in complex scenarios. By bridging retrieval with actionable application, RAG+ advances a more cognitively grounded framework for knowledge integration, representing a step toward more interpretable and capable LLMs.

## 📝 요약

이 논문은 외부 지식을 통합하는 RAG(Retrieval-Augmented Generation) 기법의 한계를 극복하기 위해 RAG+를 제안합니다. RAG+는 지식과 그 적용 예시로 구성된 이중 코퍼스를 통해, 단순한 정보 검색을 넘어 과제에 맞는 추론을 가능하게 합니다. 수학, 법률, 의학 분야에서의 실험 결과, RAG+는 기존 RAG보다 평균 3-5%의 성능 향상을 보였으며, 복잡한 상황에서는 최대 13.5%의 개선을 달성했습니다. 이는 LLMs의 해석 가능성과 능력을 향상시키는 방향으로 나아가는 중요한 기여입니다.

## 🎯 주요 포인트

- 1. RAG+는 기존 RAG 패러다임의 한계를 극복하기 위해 지식 적용을 명시적으로 통합하는 모듈형 확장을 제안합니다.
- 2. RAG+는 지식과 이에 맞는 적용 예시로 구성된 이중 코퍼스를 구축하여 추론 시 함께 검색합니다.
- 3. 실험 결과, RAG+는 수학, 법률, 의료 분야에서 평균 3-5%의 성능 향상과 최대 13.5%의 성능 향상을 달성했습니다.
- 4. RAG+는 검색과 실행 가능한 적용을 연결하여 보다 해석 가능하고 능력 있는 LLMs를 위한 인지적으로 기반이 된 프레임워크를 제공합니다.


---

*Generated on 2025-09-24 14:21:21*