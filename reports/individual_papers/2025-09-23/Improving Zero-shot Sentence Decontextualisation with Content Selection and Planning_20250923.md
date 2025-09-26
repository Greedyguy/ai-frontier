---
keywords:
  - Zero-Shot Learning
  - Content Planning
  - Sentence Decontextualisation
  - Discourse Relations
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.17921
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:34:50.783580",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Zero-Shot Learning",
    "Content Planning",
    "Sentence Decontextualisation",
    "Discourse Relations"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Zero-Shot Learning": 0.85,
    "Content Planning": 0.7,
    "Sentence Decontextualisation": 0.72,
    "Discourse Relations": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Zero-shot decontextualisation",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-shot context removal"
        ],
        "category": "specific_connectable",
        "rationale": "Links to the concept of making predictions without prior specific examples, relevant to the paper's focus on decontextualisation.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Content selection and planning",
        "canonical": "Content Planning",
        "aliases": [
          "Content strategy",
          "Content organization"
        ],
        "category": "unique_technical",
        "rationale": "Describes a novel framework for organizing content, central to the paper's methodology.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.7
      },
      {
        "surface": "Sentence decontextualisation",
        "canonical": "Sentence Decontextualisation",
        "aliases": [
          "Sentence context removal"
        ],
        "category": "unique_technical",
        "rationale": "A specific task within NLP that the paper aims to improve, providing a unique technical focus.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.72
      },
      {
        "surface": "Discourse relations",
        "canonical": "Discourse Relations",
        "aliases": [
          "Discourse connections"
        ],
        "category": "specific_connectable",
        "rationale": "Essential for understanding the context and coherence in NLP tasks, relevant to the paper's approach.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "evidence",
      "reasoning steps",
      "experimental results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Zero-shot decontextualisation",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Content selection and planning",
      "resolved_canonical": "Content Planning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Sentence decontextualisation",
      "resolved_canonical": "Sentence Decontextualisation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Discourse relations",
      "resolved_canonical": "Discourse Relations",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Improving Zero-shot Sentence Decontextualisation with Content Selection and Planning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17921.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.17921](https://arxiv.org/abs/2509.17921)

## 🔗 유사한 논문
- [[2025-09-23/MPIC_ Position-Independent Multimodal Context Caching System for Efficient MLLM Serving_20250923|MPIC: Position-Independent Multimodal Context Caching System for Efficient MLLM Serving]] (80.0% similar)
- [[2025-09-23/AttnComp_ Attention-Guided Adaptive Context Compression for Retrieval-Augmented Generation_20250923|AttnComp: Attention-Guided Adaptive Context Compression for Retrieval-Augmented Generation]] (79.8% similar)
- [[2025-09-17/You Are What You Train_ Effects of Data Composition on Training Context-aware Machine Translation Models_20250917|You Are What You Train: Effects of Data Composition on Training Context-aware Machine Translation Models]] (79.2% similar)
- [[2025-09-22/Re-FRAME the Meeting Summarization SCOPE_ Fact-Based Summarization and Personalization via Questions_20250922|Re-FRAME the Meeting Summarization SCOPE: Fact-Based Summarization and Personalization via Questions]] (78.8% similar)
- [[2025-09-22/MMAPG_ A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs_20250922|MMAPG: A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs]] (78.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]], [[keywords/Discourse Relations|Discourse Relations]]
**⚡ Unique Technical**: [[keywords/Content Planning|Content Planning]], [[keywords/Sentence Decontextualisation|Sentence Decontextualisation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17921v1 Announce Type: new 
Abstract: Extracting individual sentences from a document as evidence or reasoning steps is commonly done in many NLP tasks. However, extracted sentences often lack context necessary to make them understood, e.g., coreference and background information. To this end, we propose a content selection and planning framework for zero-shot decontextualisation, which determines what content should be mentioned and in what order for a sentence to be understood out of context. Specifically, given a potentially ambiguous sentence and its context, we first segment it into basic semantically-independent units. We then identify potentially ambiguous units from the given sentence, and extract relevant units from the context based on their discourse relations. Finally, we generate a content plan to rewrite the sentence by enriching each ambiguous unit with its relevant units. Experimental results demonstrate that our approach is competitive for sentence decontextualisation, producing sentences that exhibit better semantic integrity and discourse coherence, outperforming existing methods.

## 📝 요약

이 논문은 문서에서 문장을 추출할 때 발생하는 맥락 부족 문제를 해결하기 위해 제로샷 비맥락화(content selection and planning framework for zero-shot decontextualisation) 프레임워크를 제안합니다. 제안된 방법은 모호한 문장을 기본 의미 단위로 분할하고, 문맥에서 관련 단위를 추출하여 문장을 재작성하는 콘텐츠 계획을 생성합니다. 실험 결과, 이 접근법은 문장의 의미적 완전성과 담화 일관성을 개선하여 기존 방법보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 문서에서 개별 문장을 추출할 때 문맥이 부족하여 이해가 어려운 문제를 해결하기 위해 제로샷 비문맥화(content selection and planning framework for zero-shot decontextualisation) 프레임워크를 제안합니다.
- 2. 제안된 방법은 문장을 기본적인 의미 독립 단위로 분할하고, 모호한 단위를 식별하여 문맥에서 관련 단위를 추출한 후, 이를 바탕으로 문장을 재작성하는 콘텐츠 계획을 생성합니다.
- 3. 실험 결과, 제안된 접근 방식은 문장의 의미적 완전성과 담화의 일관성을 개선하여 기존 방법보다 뛰어난 성능을 보였습니다.


---

*Generated on 2025-09-24 03:34:50*