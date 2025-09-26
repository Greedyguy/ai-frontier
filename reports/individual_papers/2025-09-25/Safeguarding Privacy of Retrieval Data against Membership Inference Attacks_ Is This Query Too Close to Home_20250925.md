---
keywords:
  - Retrieval Augmented Generation
  - Membership Inference Attack
  - Large Language Model
  - Similarity-based MIA Detection
category: cs.CL
publish_date: 2025-09-25
arxiv_id: 2505.22061
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:54:41.493344",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Retrieval Augmented Generation",
    "Membership Inference Attack",
    "Large Language Model",
    "Similarity-based MIA Detection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Retrieval Augmented Generation": 0.9,
    "Membership Inference Attack": 0.8,
    "Large Language Model": 0.85,
    "Similarity-based MIA Detection": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Retrieval-augmented generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "RAG is a trending concept that directly relates to the paper's focus on enhancing LLMs and is crucial for linking related research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.9
      },
      {
        "surface": "Membership inference attacks",
        "canonical": "Membership Inference Attack",
        "aliases": [
          "MIA"
        ],
        "category": "unique_technical",
        "rationale": "MIAs are a specific threat addressed in the paper, offering a unique technical angle for linking security-related research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large language models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are central to the paper's discussion and are a key concept in current AI research, aiding in broad technical linking.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Similarity-based MIA detection",
        "canonical": "Similarity-based MIA Detection",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This novel method proposed in the paper enhances the understanding of MIA defenses, providing a unique link to security frameworks.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Retrieval-augmented generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Membership inference attacks",
      "resolved_canonical": "Membership Inference Attack",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large language models",
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
      "candidate_surface": "Similarity-based MIA detection",
      "resolved_canonical": "Similarity-based MIA Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Safeguarding Privacy of Retrieval Data against Membership Inference Attacks: Is This Query Too Close to Home?

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.22061.pdf)
**Category**: cs.CL
**Published**: 2025-09-25
**ArXiv ID**: [2505.22061](https://arxiv.org/abs/2505.22061)

## 🔗 유사한 논문
- [[2025-09-25/RAG Security and Privacy_ Formalizing the Threat Model and Attack Surface_20250925|RAG Security and Privacy: Formalizing the Threat Model and Attack Surface]] (88.3% similar)
- [[2025-09-19/AIP_ Subverting Retrieval-Augmented Generation via Adversarial Instructional Prompt_20250919|AIP: Subverting Retrieval-Augmented Generation via Adversarial Instructional Prompt]] (85.7% similar)
- [[2025-09-24/SIRAG_ Towards Stable and Interpretable RAG with A Process-Supervised Multi-Agent Framework_20250924|SIRAG: Towards Stable and Interpretable RAG with A Process-Supervised Multi-Agent Framework]] (85.6% similar)
- [[2025-09-19/Enhancing Retrieval Augmentation via Adversarial Collaboration_20250919|Enhancing Retrieval Augmentation via Adversarial Collaboration]] (85.1% similar)
- [[2025-09-23/GRIL_ Knowledge Graph Retrieval-Integrated Learning with Large Language Models_20250923|GRIL: Knowledge Graph Retrieval-Integrated Learning with Large Language Models]] (84.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]]
**⚡ Unique Technical**: [[keywords/Membership Inference Attack|Membership Inference Attack]], [[keywords/Similarity-based MIA Detection|Similarity-based MIA Detection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.22061v2 Announce Type: replace 
Abstract: Retrieval-augmented generation (RAG) mitigates the hallucination problem in large language models (LLMs) and has proven effective for personalized usages. However, delivering private retrieved documents directly to LLMs introduces vulnerability to membership inference attacks (MIAs), which try to determine whether the target data point exists in the private external database or not. Based on the insight that MIA queries typically exhibit high similarity to only one target document, we introduce a novel similarity-based MIA detection framework designed for the RAG system. With the proposed method, we show that a simple detect-and-hide strategy can successfully obfuscate attackers, maintain data utility, and remain system-agnostic against MIA. We experimentally prove its detection and defense against various state-of-the-art MIA methods and its adaptability to existing RAG systems.

## 📝 요약

이 논문은 대규모 언어 모델(LLM)의 환각 문제를 완화하는 검색 증강 생성(RAG) 시스템의 보안 문제를 다룹니다. RAG 시스템은 개인화된 사용에 효과적이지만, 검색된 문서를 LLM에 직접 전달할 경우 멤버십 추론 공격(MIA)에 취약해질 수 있습니다. MIA는 특정 데이터가 외부 데이터베이스에 존재하는지를 판단하려고 시도합니다. 논문에서는 MIA 쿼리가 주로 하나의 대상 문서와 높은 유사성을 보인다는 점에 착안하여, RAG 시스템을 위한 새로운 유사성 기반 MIA 탐지 프레임워크를 제안합니다. 제안된 방법은 간단한 탐지 및 숨김 전략을 통해 공격자를 혼란시키고, 데이터 유틸리티를 유지하며, 시스템에 구애받지 않고 MIA에 대응할 수 있음을 보여줍니다. 다양한 최신 MIA 방법에 대한 탐지 및 방어 능력과 기존 RAG 시스템에의 적응성을 실험적으로 입증했습니다.

## 🎯 주요 포인트

- 1. 검색 증강 생성(RAG)은 대규모 언어 모델(LLM)의 환각 문제를 완화하고 개인화된 사용에 효과적이다.
- 2. RAG 시스템에서 개인 문서를 직접 LLM에 전달하면 멤버십 추론 공격(MIA)에 취약해진다.
- 3. MIA 쿼리는 일반적으로 하나의 대상 문서와 높은 유사성을 보인다는 점에 착안하여, 유사성 기반 MIA 탐지 프레임워크를 제안한다.
- 4. 제안된 방법은 간단한 탐지 및 숨김 전략을 통해 공격자를 혼란시키고 데이터 유용성을 유지하며, 시스템에 구애받지 않고 MIA에 대응할 수 있다.
- 5. 다양한 최신 MIA 방법에 대한 탐지 및 방어 능력과 기존 RAG 시스템에 대한 적응성을 실험적으로 입증하였다.


---

*Generated on 2025-09-26 08:54:41*