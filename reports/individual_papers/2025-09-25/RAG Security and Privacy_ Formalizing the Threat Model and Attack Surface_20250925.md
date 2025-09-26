---
keywords:
  - Retrieval Augmented Generation
  - Large Language Model
  - Document-level Membership Inference
  - Data Poisoning
  - Adversarial Prompts
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.20324
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:06:49.600615",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Retrieval Augmented Generation",
    "Large Language Model",
    "Document-level Membership Inference",
    "Data Poisoning",
    "Adversarial Prompts"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Retrieval Augmented Generation": 0.85,
    "Large Language Model": 0.8,
    "Document-level Membership Inference": 0.78,
    "Data Poisoning": 0.82,
    "Adversarial Prompts": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Retrieval-Augmented Generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "RAG is a trending concept in NLP that combines LLMs with document retrieval, offering strong connectivity potential.",
        "novelty_score": 0.55,
        "connectivity_score": 0.89,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are foundational in NLP and directly relate to the RAG approach, providing broad technical context.",
        "novelty_score": 0.3,
        "connectivity_score": 0.92,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "Document-level Membership Inference",
        "canonical": "Document-level Membership Inference",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a specific threat vector in RAG systems, crucial for understanding privacy risks.",
        "novelty_score": 0.72,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Data Poisoning",
        "canonical": "Data Poisoning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Data poisoning is a well-known attack vector relevant to the security of RAG systems.",
        "novelty_score": 0.5,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Adversarial Prompts",
        "canonical": "Adversarial Prompts",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Adversarial prompts are a unique challenge for RAG systems, impacting security and privacy.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
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
      "candidate_surface": "Retrieval-Augmented Generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.89,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.92,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Document-level Membership Inference",
      "resolved_canonical": "Document-level Membership Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Data Poisoning",
      "resolved_canonical": "Data Poisoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Adversarial Prompts",
      "resolved_canonical": "Adversarial Prompts",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# RAG Security and Privacy: Formalizing the Threat Model and Attack Surface

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20324.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.20324](https://arxiv.org/abs/2509.20324)

## 🔗 유사한 논문
- [[2025-09-19/AIP_ Subverting Retrieval-Augmented Generation via Adversarial Instructional Prompt_20250919|AIP: Subverting Retrieval-Augmented Generation via Adversarial Instructional Prompt]] (85.8% similar)
- [[2025-09-24/SIRAG_ Towards Stable and Interpretable RAG with A Process-Supervised Multi-Agent Framework_20250924|SIRAG: Towards Stable and Interpretable RAG with A Process-Supervised Multi-Agent Framework]] (85.6% similar)
- [[2025-09-19/Engineering RAG Systems for Real-World Applications_ Design, Development, and Evaluation_20250919|Engineering RAG Systems for Real-World Applications: Design, Development, and Evaluation]] (85.5% similar)
- [[2025-09-19/Causal-Counterfactual RAG_ The Integration of Causal-Counterfactual Reasoning into RAG_20250919|Causal-Counterfactual RAG: The Integration of Causal-Counterfactual Reasoning into RAG]] (85.4% similar)
- [[2025-09-23/Rationale-Guided Retrieval Augmented Generation for Medical Question Answering_20250923|Rationale-Guided Retrieval Augmented Generation for Medical Question Answering]] (85.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]], [[keywords/Data Poisoning|Data Poisoning]]
**⚡ Unique Technical**: [[keywords/Document-level Membership Inference|Document-level Membership Inference]], [[keywords/Adversarial Prompts|Adversarial Prompts]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20324v1 Announce Type: cross 
Abstract: Retrieval-Augmented Generation (RAG) is an emerging approach in natural language processing that combines large language models (LLMs) with external document retrieval to produce more accurate and grounded responses. While RAG has shown strong potential in reducing hallucinations and improving factual consistency, it also introduces new privacy and security challenges that differ from those faced by traditional LLMs. Existing research has demonstrated that LLMs can leak sensitive information through training data memorization or adversarial prompts, and RAG systems inherit many of these vulnerabilities. At the same time, reliance of RAG on an external knowledge base opens new attack surfaces, including the potential for leaking information about the presence or content of retrieved documents, or for injecting malicious content to manipulate model behavior. Despite these risks, there is currently no formal framework that defines the threat landscape for RAG systems. In this paper, we address a critical gap in the literature by proposing, to the best of our knowledge, the first formal threat model for retrieval-RAG systems. We introduce a structured taxonomy of adversary types based on their access to model components and data, and we formally define key threat vectors such as document-level membership inference and data poisoning, which pose serious privacy and integrity risks in real-world deployments. By establishing formal definitions and attack models, our work lays the foundation for a more rigorous and principled understanding of privacy and security in RAG systems.

## 📝 요약

이 논문은 정보 검색 기반 생성(RAG) 시스템의 보안 및 프라이버시 위협을 체계적으로 분석한 최초의 연구입니다. RAG는 대형 언어 모델(LLM)과 외부 문서 검색을 결합하여 더 정확한 응답을 생성하지만, 새로운 보안 문제를 야기합니다. 저자들은 RAG 시스템의 위협 모델을 제안하고, 문서 수준의 멤버십 추론 및 데이터 중독과 같은 주요 위협 벡터를 정의하여 실세계에서의 프라이버시와 무결성 위험을 강조합니다. 이 연구는 RAG 시스템의 보안 이해를 위한 기초를 마련합니다.

## 🎯 주요 포인트

- 1. Retrieval-Augmented Generation(RAG)은 대형 언어 모델(LLM)과 외부 문서 검색을 결합하여 보다 정확하고 근거 있는 응답을 생성하는 자연어 처리의 새로운 접근 방식입니다.
- 2. RAG는 환각 감소와 사실적 일관성 향상에 잠재력을 보이지만, 전통적인 LLM과는 다른 새로운 프라이버시 및 보안 문제를 야기합니다.
- 3. RAG 시스템은 외부 지식 기반에 의존하기 때문에 문서의 존재나 내용을 유출하거나 악의적인 콘텐츠를 주입하여 모델의 행동을 조작할 수 있는 새로운 공격 표면을 제공합니다.
- 4. 본 논문은 RAG 시스템에 대한 위협 지형을 정의하는 최초의 공식적인 위협 모델을 제안하여 기존 연구의 중요한 격차를 해결합니다.
- 5. 우리는 모델 구성 요소와 데이터에 대한 접근을 기반으로 한 적대자 유형의 구조화된 분류법을 소개하고, 문서 수준의 멤버십 추론 및 데이터 중독과 같은 주요 위협 벡터를 공식적으로 정의합니다.


---

*Generated on 2025-09-25 16:06:49*