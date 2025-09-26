---
keywords:
  - Contract Clause Retrieval
  - ACORD
  - Bi-Encoder Retriever
  - Limitation of Liability Clause
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2501.06582
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:46:38.850141",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Contract Clause Retrieval",
    "ACORD",
    "Bi-Encoder Retriever",
    "Limitation of Liability Clause"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Contract Clause Retrieval": 0.78,
    "ACORD": 0.8,
    "Bi-Encoder Retriever": 0.77,
    "Limitation of Liability Clause": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "contract clause retrieval",
        "canonical": "Contract Clause Retrieval",
        "aliases": [
          "clause retrieval",
          "contract retrieval"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific task within legal document processing, crucial for linking legal and NLP domains.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Atticus Clause Retrieval Dataset",
        "canonical": "ACORD",
        "aliases": [
          "Atticus Dataset",
          "Clause Retrieval Dataset"
        ],
        "category": "unique_technical",
        "rationale": "ACORD is the first expert-annotated dataset for contract drafting, providing a unique resource for legal NLP research.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "bi-encoder retriever",
        "canonical": "Bi-Encoder Retriever",
        "aliases": [
          "bi-encoder",
          "retriever model"
        ],
        "category": "specific_connectable",
        "rationale": "This model type is significant for retrieval tasks, linking to broader NLP model discussions.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "Limitation of Liability",
        "canonical": "Limitation of Liability Clause",
        "aliases": [
          "liability clause",
          "limitation clause"
        ],
        "category": "unique_technical",
        "rationale": "A common and critical clause in contracts, relevant for legal drafting and analysis.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "information retrieval",
      "contract drafting",
      "lawyers"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "contract clause retrieval",
      "resolved_canonical": "Contract Clause Retrieval",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Atticus Clause Retrieval Dataset",
      "resolved_canonical": "ACORD",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "bi-encoder retriever",
      "resolved_canonical": "Bi-Encoder Retriever",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Limitation of Liability",
      "resolved_canonical": "Limitation of Liability Clause",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# ACORD: An Expert-Annotated Retrieval Dataset for Legal Contract Drafting

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2501.06582.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2501.06582](https://arxiv.org/abs/2501.06582)

## 🔗 유사한 논문
- [[2025-09-19/Enhancing Retrieval Augmentation via Adversarial Collaboration_20250919|Enhancing Retrieval Augmentation via Adversarial Collaboration]] (78.9% similar)
- [[2025-09-23/PersonaMatrix_ A Recipe for Persona-Aware Evaluation of Legal Summarization_20250923|PersonaMatrix: A Recipe for Persona-Aware Evaluation of Legal Summarization]] (78.9% similar)
- [[2025-09-22/ConfReady_ A RAG based Assistant and Dataset for Conference Checklist Responses_20250922|ConfReady: A RAG based Assistant and Dataset for Conference Checklist Responses]] (78.0% similar)
- [[2025-09-23/BAGELS_ Benchmarking the Automated Generation and Extraction of Limitations from Scholarly Text_20250923|BAGELS: Benchmarking the Automated Generation and Extraction of Limitations from Scholarly Text]] (77.4% similar)
- [[2025-09-23/KoACD_ The First Korean Adolescent Dataset for Cognitive Distortion Analysis via Role-Switching Multi-LLM Negotiation_20250923|KoACD: The First Korean Adolescent Dataset for Cognitive Distortion Analysis via Role-Switching Multi-LLM Negotiation]] (77.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Bi-Encoder Retriever|Bi-Encoder Retriever]]
**⚡ Unique Technical**: [[keywords/Contract Clause Retrieval|Contract Clause Retrieval]], [[keywords/ACORD|ACORD]], [[keywords/Limitation of Liability Clause|Limitation of Liability Clause]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.06582v4 Announce Type: replace 
Abstract: Information retrieval, specifically contract clause retrieval, is foundational to contract drafting because lawyers rarely draft contracts from scratch; instead, they locate and revise the most relevant precedent. We introduce the Atticus Clause Retrieval Dataset (ACORD), the first retrieval benchmark for contract drafting fully annotated by experts. ACORD focuses on complex contract clauses such as Limitation of Liability, Indemnification, Change of Control, and Most Favored Nation. It includes 114 queries and over 126,000 query-clause pairs, each ranked on a scale from 1 to 5 stars. The task is to find the most relevant precedent clauses to a query. The bi-encoder retriever paired with pointwise LLMs re-rankers shows promising results. However, substantial improvements are still needed to effectively manage the complex legal work typically undertaken by lawyers. As the first retrieval benchmark for contract drafting annotated by experts, ACORD can serve as a valuable IR benchmark for the NLP community.

## 📝 요약

이 논문은 계약서 작성 시 중요한 정보 검색, 특히 계약 조항 검색을 다룹니다. 변호사들은 계약서를 처음부터 작성하기보다는 기존의 관련 사례를 찾아 수정하는 방식을 주로 사용합니다. 이를 위해 전문가가 완전히 주석을 단 최초의 계약 작성 검색 벤치마크인 Atticus Clause Retrieval Dataset (ACORD)을 소개합니다. ACORD는 책임 제한, 보상, 통제 변경, 최혜국 대우와 같은 복잡한 계약 조항에 초점을 맞추고 있으며, 114개의 쿼리와 12만 6천 개 이상의 쿼리-조항 쌍을 포함하고 있습니다. 각 쌍은 1에서 5까지의 별점으로 평가됩니다. 주요 기여는 쿼리에 가장 관련성 높은 선례 조항을 찾는 것입니다. 바이엔코더 검색기와 포인트와이즈 LLM 재랭커가 유망한 결과를 보였지만, 변호사가 수행하는 복잡한 법률 업무를 효과적으로 관리하기 위해서는 여전히 상당한 개선이 필요합니다. ACORD는 전문가가 주석을 단 최초의 계약 작성 검색 벤치마크로서 NLP 커뮤니티에 유용한 정보 검색(IR) 벤치마크가 될 수 있습니다.

## 🎯 주요 포인트

- 1. ACORD는 전문가가 완전히 주석을 단 최초의 계약 초안 작성을 위한 검색 벤치마크 데이터셋입니다.
- 2. 데이터셋은 책임 제한, 보상, 통제 변경, 최혜국 대우와 같은 복잡한 계약 조항에 중점을 둡니다.
- 3. ACORD는 114개의 쿼리와 126,000개 이상의 쿼리-조항 쌍을 포함하며, 각 쌍은 1에서 5까지의 별점으로 평가됩니다.
- 4. 바이 인코더 검색기와 포인트와이즈 LLM 재랭커가 유망한 결과를 보여주지만, 법률 업무를 효과적으로 관리하기 위해서는 상당한 개선이 필요합니다.
- 5. ACORD는 계약 초안 작성을 위한 검색 벤치마크로서 NLP 커뮤니티에 가치 있는 IR 벤치마크로 활용될 수 있습니다.


---

*Generated on 2025-09-24 03:46:38*