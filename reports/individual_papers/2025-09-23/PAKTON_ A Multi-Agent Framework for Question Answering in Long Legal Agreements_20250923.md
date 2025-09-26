---
keywords:
  - PAKTON Framework
  - Multi-Agent System
  - Retrieval Augmented Generation
  - Contract Analysis
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2506.00608
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:02:13.996360",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "PAKTON Framework",
    "Multi-Agent System",
    "Retrieval Augmented Generation",
    "Contract Analysis"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "PAKTON Framework": 0.8,
    "Multi-Agent System": 0.75,
    "Retrieval Augmented Generation": 0.82,
    "Contract Analysis": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "PAKTON",
        "canonical": "PAKTON Framework",
        "aliases": [
          "PAKTON"
        ],
        "category": "unique_technical",
        "rationale": "PAKTON is a novel framework specifically designed for legal document analysis, providing a unique linking opportunity.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "multi-agent framework",
        "canonical": "Multi-Agent System",
        "aliases": [
          "multi-agent framework"
        ],
        "category": "specific_connectable",
        "rationale": "Multi-agent systems are crucial for collaborative workflows in complex tasks like legal document analysis.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "retrieval-augmented generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "RAG is a trending technique that enhances document retrieval and generation, relevant for legal analysis.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "contract analysis",
        "canonical": "Contract Analysis",
        "aliases": [
          "contract review"
        ],
        "category": "unique_technical",
        "rationale": "Contract analysis is a specialized area of legal document processing, offering unique linking opportunities.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "legal interpretation",
      "subjective assessments"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "PAKTON",
      "resolved_canonical": "PAKTON Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "multi-agent framework",
      "resolved_canonical": "Multi-Agent System",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "retrieval-augmented generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "contract analysis",
      "resolved_canonical": "Contract Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# PAKTON: A Multi-Agent Framework for Question Answering in Long Legal Agreements

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2506.00608.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2506.00608](https://arxiv.org/abs/2506.00608)

## 🔗 유사한 논문
- [[2025-09-23/ACORD_ An Expert-Annotated Retrieval Dataset for Legal Contract Drafting_20250923|ACORD: An Expert-Annotated Retrieval Dataset for Legal Contract Drafting]] (83.3% similar)
- [[2025-09-23/PersonaMatrix_ A Recipe for Persona-Aware Evaluation of Legal Summarization_20250923|PersonaMatrix: A Recipe for Persona-Aware Evaluation of Legal Summarization]] (82.1% similar)
- [[2025-09-23/Medical AI Consensus_ A Multi-Agent Framework for Radiology Report Generation and Evaluation_20250923|Medical AI Consensus: A Multi-Agent Framework for Radiology Report Generation and Evaluation]] (80.1% similar)
- [[2025-09-18/An LLM Agentic Approach for Legal-Critical Software_ A Case Study for Tax Prep Software_20250918|An LLM Agentic Approach for Legal-Critical Software: A Case Study for Tax Prep Software]] (79.8% similar)
- [[2025-09-23/ASTRA_ A Negotiation Agent with Adaptive and Strategic Reasoning via Tool-integrated Action for Dynamic Offer Optimization_20250923|ASTRA: A Negotiation Agent with Adaptive and Strategic Reasoning via Tool-integrated Action for Dynamic Offer Optimization]] (79.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multi-Agent System|Multi-Agent System]], [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]]
**⚡ Unique Technical**: [[keywords/PAKTON Framework|PAKTON Framework]], [[keywords/Contract Analysis|Contract Analysis]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.00608v2 Announce Type: replace 
Abstract: Contract review is a complex and time-intensive task that typically demands specialized legal expertise, rendering it largely inaccessible to non-experts. Moreover, legal interpretation is rarely straightforward-ambiguity is pervasive, and judgments often hinge on subjective assessments. Compounding these challenges, contracts are usually confidential, restricting their use with proprietary models and necessitating reliance on open-source alternatives. To address these challenges, we introduce PAKTON: a fully open-source, end-to-end, multi-agent framework with plug-and-play capabilities. PAKTON is designed to handle the complexities of contract analysis through collaborative agent workflows and a novel retrieval-augmented generation (RAG) component, enabling automated legal document review that is more accessible, adaptable, and privacy-preserving. Experiments demonstrate that PAKTON outperforms both general-purpose and pretrained models in predictive accuracy, retrieval performance, explainability, completeness, and grounded justifications as evaluated through a human study and validated with automated metrics.

## 📝 요약

이 논문은 계약 검토의 복잡성과 시간 소모 문제를 해결하기 위해 PAKTON이라는 오픈 소스 프레임워크를 제안합니다. PAKTON은 다중 에이전트 협업과 새로운 검색 증강 생성(RAG) 구성 요소를 통해 자동화된 법률 문서 검토를 가능하게 합니다. 이 시스템은 예측 정확도, 검색 성능, 설명 가능성, 완전성 및 근거 있는 정당성에서 기존 모델보다 우수한 성능을 보였습니다. 이를 통해 법률 문서 검토가 더 접근 가능하고 적응 가능하며 프라이버시를 보장할 수 있음을 입증했습니다.

## 🎯 주요 포인트

- 1. 계약 검토는 전문적인 법률 지식이 필요한 복잡하고 시간이 많이 소요되는 작업이다.
- 2. 법적 해석은 모호성이 많고 주관적인 평가에 의존하는 경우가 많다.
- 3. PAKTON은 계약 분석의 복잡성을 다루기 위해 설계된 오픈 소스, 엔드 투 엔드, 다중 에이전트 프레임워크이다.
- 4. PAKTON은 협업 에이전트 워크플로우와 새로운 검색-증강 생성(RAG) 구성 요소를 통해 자동화된 법률 문서 검토를 가능하게 한다.
- 5. 실험 결과, PAKTON은 예측 정확도, 검색 성능, 설명 가능성, 완전성 및 근거 있는 정당성에서 일반 모델과 사전 학습된 모델을 능가한다.


---

*Generated on 2025-09-24 04:02:13*