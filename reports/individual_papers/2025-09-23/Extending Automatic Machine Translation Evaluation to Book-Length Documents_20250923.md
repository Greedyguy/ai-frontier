---
keywords:
  - Large Language Model
  - SEGALE
  - Document-Level Evaluation
  - Sentence Segmentation and Alignment
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.17249
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:22:35.687664",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "SEGALE",
    "Document-Level Evaluation",
    "Sentence Segmentation and Alignment"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "SEGALE": 0.8,
    "Document-Level Evaluation": 0.78,
    "Sentence Segmentation and Alignment": 0.77
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
        "rationale": "Large Language Models are central to the paper's discussion on translation and evaluation, providing a strong link to existing research in NLP.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "SEGALE",
        "canonical": "SEGALE",
        "aliases": [
          "Sentence Segmentation and Alignment Evaluation"
        ],
        "category": "unique_technical",
        "rationale": "SEGALE is a novel evaluation scheme introduced in the paper, offering a unique link to document-level translation evaluation.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "document-level evaluation",
        "canonical": "Document-Level Evaluation",
        "aliases": [
          "long-document evaluation"
        ],
        "category": "specific_connectable",
        "rationale": "Document-level evaluation is a key concept in extending translation assessments beyond sentence-level, crucial for linking to broader translation evaluation methodologies.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "sentence segmentation and alignment",
        "canonical": "Sentence Segmentation and Alignment",
        "aliases": [
          "sentence alignment"
        ],
        "category": "specific_connectable",
        "rationale": "This technique is essential for the proposed evaluation scheme, connecting to methods in text processing and alignment.",
        "novelty_score": 0.5,
        "connectivity_score": 0.72,
        "specificity_score": 0.68,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "evaluation methodologies",
      "translation performance",
      "experiments"
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
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "SEGALE",
      "resolved_canonical": "SEGALE",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "document-level evaluation",
      "resolved_canonical": "Document-Level Evaluation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "sentence segmentation and alignment",
      "resolved_canonical": "Sentence Segmentation and Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.72,
        "specificity": 0.68,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Extending Automatic Machine Translation Evaluation to Book-Length Documents

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17249.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.17249](https://arxiv.org/abs/2509.17249)

## 🔗 유사한 논문
- [[2025-09-23/Breaking the Reviewer_ Assessing the Vulnerability of Large Language Models in Automated Peer Review Under Textual Adversarial Attacks_20250923|Breaking the Reviewer: Assessing the Vulnerability of Large Language Models in Automated Peer Review Under Textual Adversarial Attacks]] (81.4% similar)
- [[2025-09-23/GALLa_ Graph Aligned Large Language Models for Improved Source Code Understanding_20250923|GALLa: Graph Aligned Large Language Models for Improved Source Code Understanding]] (81.4% similar)
- [[2025-09-23/EquiBench_ Benchmarking Large Language Models' Reasoning about Program Semantics via Equivalence Checking_20250923|EquiBench: Benchmarking Large Language Models' Reasoning about Program Semantics via Equivalence Checking]] (81.1% similar)
- [[2025-09-19/CLEAR_ A Comprehensive Linguistic Evaluation of Argument Rewriting by Large Language Models_20250919|CLEAR: A Comprehensive Linguistic Evaluation of Argument Rewriting by Large Language Models]] (80.9% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Document-Level Evaluation|Document-Level Evaluation]], [[keywords/Sentence Segmentation and Alignment|Sentence Segmentation and Alignment]]
**⚡ Unique Technical**: [[keywords/SEGALE|SEGALE]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17249v1 Announce Type: new 
Abstract: Despite Large Language Models (LLMs) demonstrating superior translation performance and long-context capabilities, evaluation methodologies remain constrained to sentence-level assessment due to dataset limitations, token number restrictions in metrics, and rigid sentence boundary requirements. We introduce SEGALE, an evaluation scheme that extends existing automatic metrics to long-document translation by treating documents as continuous text and applying sentence segmentation and alignment methods. Our approach enables previously unattainable document-level evaluation, handling translations of arbitrary length generated with document-level prompts while accounting for under-/over-translations and varied sentence boundaries. Experiments show our scheme significantly outperforms existing long-form document evaluation schemes, while being comparable to evaluations performed with groundtruth sentence alignments. Additionally, we apply our scheme to book-length texts and newly demonstrate that many open-weight LLMs fail to effectively translate documents at their reported maximum context lengths.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 번역 성능 평가를 문서 수준으로 확장하는 SEGALE라는 평가 방식을 제안합니다. 기존의 문장 단위 평가의 한계를 극복하기 위해 문서를 연속적인 텍스트로 처리하고 문장 분할 및 정렬 방법을 적용합니다. 이를 통해 문서 길이에 상관없이 번역 평가가 가능하며, 과소/과대 번역 및 다양한 문장 경계를 고려합니다. 실험 결과, SEGALE는 기존의 장문 문서 평가 방식보다 우수하며, 실제 문장 정렬을 사용한 평가와 유사한 성능을 보입니다. 또한, 책 길이의 텍스트에 적용하여 많은 공개 LLM이 최대 문맥 길이에서 효과적으로 번역하지 못함을 새롭게 입증했습니다.

## 🎯 주요 포인트

- 1. SEGALE는 기존 자동 평가 지표를 확장하여 문서를 연속적인 텍스트로 처리하고 문장 분할 및 정렬 방법을 적용하여 장문 번역 평가를 가능하게 합니다.
- 2. 이 접근법은 문서 수준의 프롬프트로 생성된 임의 길이의 번역을 처리하며, 누락/과잉 번역 및 다양한 문장 경계를 고려합니다.
- 3. 실험 결과, SEGALE는 기존의 장문 문서 평가 방식보다 성능이 뛰어나며, 실제 문장 정렬을 사용한 평가와 비교할 만한 수준입니다.
- 4. SEGALE를 책 길이의 텍스트에 적용한 결과, 많은 오픈 웨이트 LLM이 보고된 최대 문맥 길이에서 문서를 효과적으로 번역하지 못한다는 점을 새롭게 입증했습니다.


---

*Generated on 2025-09-24 03:22:35*