<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:54:42.289051",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "False Assumptions",
    "Fact Verification",
    "External Evidence"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "False Assumptions": 0.7,
    "Fact Verification": 0.8,
    "External Evidence": 0.75
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
        "rationale": "Large Language Models are central to the paper's approach and are a key concept in many related works.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "false assumptions",
        "canonical": "False Assumptions",
        "aliases": [
          "incorrect assumptions"
        ],
        "category": "unique_technical",
        "rationale": "The concept of false assumptions is unique to the paper's problem statement and critical for understanding the research focus.",
        "novelty_score": 0.7,
        "connectivity_score": 0.5,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "fact verification",
        "canonical": "Fact Verification",
        "aliases": [
          "fact-checking"
        ],
        "category": "specific_connectable",
        "rationale": "Fact verification is a specific process discussed in the paper that connects to broader research on information validation.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "external evidence",
        "canonical": "External Evidence",
        "aliases": [
          "retrieved evidence"
        ],
        "category": "specific_connectable",
        "rationale": "Using external evidence is a method to mitigate hallucinations, linking to retrieval-based approaches.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.65,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "hallucinations",
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
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "false assumptions",
      "resolved_canonical": "False Assumptions",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.5,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "fact verification",
      "resolved_canonical": "Fact Verification",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "external evidence",
      "resolved_canonical": "External Evidence",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.65,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Identifying and Answering Questions with False Assumptions: An Interpretable Approach

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2508.15139.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2508.15139](https://arxiv.org/abs/2508.15139)

## 🔗 유사한 논문
- [[2025-09-22/Quantifying Self-Awareness of Knowledge in Large Language Models_20250922|Quantifying Self-Awareness of Knowledge in Large Language Models]] (86.7% similar)
- [[2025-09-22/Do Retrieval Augmented Language Models Know When They Don't Know?_20250922|Do Retrieval Augmented Language Models Know When They Don't Know?]] (85.9% similar)
- [[2025-09-23/No Need for Explanations_ LLMs can implicitly learn from mistakes in-context_20250923|No Need for Explanations: LLMs can implicitly learn from mistakes in-context]] (85.8% similar)
- [[2025-09-24/Unraveling Misinformation Propagation in LLM Reasoning_20250924|Unraveling Misinformation Propagation in LLM Reasoning]] (85.7% similar)
- [[2025-09-23/Question Answering with LLMs and Learning from Answer Sets_20250923|Question Answering with LLMs and Learning from Answer Sets]] (85.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Fact Verification|Fact Verification]], [[keywords/External Evidence|External Evidence]]
**⚡ Unique Technical**: [[keywords/False Assumptions|False Assumptions]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.15139v2 Announce Type: replace 
Abstract: People often ask questions with false assumptions, a type of question that does not have regular answers. Answering such questions requires first identifying the false assumptions. Large Language Models (LLMs) often generate misleading answers to these questions because of hallucinations. In this paper, we focus on identifying and answering questions with false assumptions in several domains. We first investigate whether the problem reduces to fact verification. Then, we present an approach leveraging external evidence to mitigate hallucinations. Experiments with five LLMs demonstrate that (1) incorporating retrieved evidence is beneficial and (2) generating and validating atomic assumptions yields more improvements and provides an interpretable answer by pinpointing the false assumptions.

## 📝 요약

이 논문은 잘못된 가정을 포함한 질문에 대한 답변을 개선하는 방법을 제안합니다. 대형 언어 모델(LLM)은 이러한 질문에 대해 종종 잘못된 답변을 생성하는데, 이는 환각 현상 때문입니다. 연구진은 외부 증거를 활용하여 환각을 줄이는 접근법을 제시하고, 다섯 개의 LLM을 실험하여 증거를 통합하는 것이 유익하며, 원자적 가정을 생성하고 검증하는 것이 더 나은 해답을 제공함을 확인했습니다. 이를 통해 잘못된 가정을 명확히 하여 해석 가능한 답변을 제공합니다.

## 🎯 주요 포인트

- 1. 잘못된 가정을 포함한 질문을 식별하고 답변하는 것이 중요하다.
- 2. 대형 언어 모델(LLM)은 환각으로 인해 잘못된 답변을 생성할 수 있다.
- 3. 외부 증거를 활용하여 환각을 줄이는 접근법을 제시한다.
- 4. 실험 결과, 검색된 증거를 통합하는 것이 유익하며, 원자적 가정을 생성하고 검증하는 것이 더 나은 개선을 가져온다.
- 5. 잘못된 가정을 정확히 지적함으로써 해석 가능한 답변을 제공할 수 있다.


---

*Generated on 2025-09-24 15:54:42*