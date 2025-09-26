---
keywords:
  - Z-Scores for Disfluency Evaluation
  - Large Language Model
  - Disfluency Types
  - Deterministic Alignment Module
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.20319
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:06:20.785818",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Z-Scores for Disfluency Evaluation",
    "Large Language Model",
    "Disfluency Types",
    "Deterministic Alignment Module"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Z-Scores for Disfluency Evaluation": 0.8,
    "Large Language Model": 0.85,
    "Disfluency Types": 0.78,
    "Deterministic Alignment Module": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Z-Scores",
        "canonical": "Z-Scores for Disfluency Evaluation",
        "aliases": [
          "Z-Scores"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel metric specific to disfluency evaluation, enhancing the understanding of system performance.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Connects to a well-established concept in NLP, relevant for understanding model performance in disfluency tasks.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Disfluency Types",
        "canonical": "Disfluency Types",
        "aliases": [
          "EDITED",
          "INTJ",
          "PRN"
        ],
        "category": "specific_connectable",
        "rationale": "Essential for categorizing and understanding the specific challenges in disfluency removal.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Deterministic Alignment Module",
        "canonical": "Deterministic Alignment Module",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A specific tool for mapping text, crucial for the Z-Scores' effectiveness in evaluation.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "precision",
      "recall",
      "F1"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Z-Scores",
      "resolved_canonical": "Z-Scores for Disfluency Evaluation",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
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
      "candidate_surface": "Disfluency Types",
      "resolved_canonical": "Disfluency Types",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Deterministic Alignment Module",
      "resolved_canonical": "Deterministic Alignment Module",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Z-Scores: A Metric for Linguistically Assessing Disfluency Removal

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20319.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.20319](https://arxiv.org/abs/2509.20319)

## 🔗 유사한 논문
- [[2025-09-19/Adding LLMs to the psycholinguistic norming toolbox_ A practical guide to getting the most out of human ratings_20250919|Adding LLMs to the psycholinguistic norming toolbox: A practical guide to getting the most out of human ratings]] (81.6% similar)
- [[2025-09-23/Measuring Scalar Constructs in Social Science with LLMs_20250923|Measuring Scalar Constructs in Social Science with LLMs]] (81.4% similar)
- [[2025-09-23/Cognitive Linguistic Identity Fusion Score (CLIFS)_ A Scalable Cognition-Informed Approach to Quantifying Identity Fusion from Text_20250923|Cognitive Linguistic Identity Fusion Score (CLIFS): A Scalable Cognition-Informed Approach to Quantifying Identity Fusion from Text]] (81.4% similar)
- [[2025-09-23/AIPsychoBench_ Understanding the Psychometric Differences between LLMs and Humans_20250923|AIPsychoBench: Understanding the Psychometric Differences between LLMs and Humans]] (81.3% similar)
- [[2025-09-23/Large Language Models Badly Generalize across Option Length, Problem Types, and Irrelevant Noun Replacements_20250923|Large Language Models Badly Generalize across Option Length, Problem Types, and Irrelevant Noun Replacements]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Disfluency Types|Disfluency Types]]
**⚡ Unique Technical**: [[keywords/Z-Scores for Disfluency Evaluation|Z-Scores for Disfluency Evaluation]], [[keywords/Deterministic Alignment Module|Deterministic Alignment Module]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20319v1 Announce Type: cross 
Abstract: Evaluating disfluency removal in speech requires more than aggregate token-level scores. Traditional word-based metrics such as precision, recall, and F1 (E-Scores) capture overall performance but cannot reveal why models succeed or fail. We introduce Z-Scores, a span-level linguistically-grounded evaluation metric that categorizes system behavior across distinct disfluency types (EDITED, INTJ, PRN). Our deterministic alignment module enables robust mapping between generated text and disfluent transcripts, allowing Z-Scores to expose systematic weaknesses that word-level metrics obscure. By providing category-specific diagnostics, Z-Scores enable researchers to identify model failure modes and design targeted interventions -- such as tailored prompts or data augmentation -- yielding measurable performance improvements. A case study with LLMs shows that Z-Scores uncover challenges with INTJ and PRN disfluencies hidden in aggregate F1, directly informing model refinement strategies.

## 📝 요약

이 논문은 음성의 비유창성 제거 평가에서 전통적인 단어 기반 메트릭의 한계를 지적하며, 새로운 평가 지표인 Z-스코어를 제안합니다. Z-스코어는 비유창성 유형별로 시스템의 행동을 분류하여, 기존의 단어 수준 메트릭이 드러내지 못하는 모델의 체계적 약점을 밝혀냅니다. 이를 통해 연구자들이 모델의 실패 원인을 파악하고, 맞춤형 프롬프트나 데이터 증강과 같은 개입을 설계하여 성능을 향상시킬 수 있도록 돕습니다. 사례 연구에서는 대형 언어 모델(LLM)이 INTJ 및 PRN 비유창성에서의 문제를 드러내며, 이는 모델 개선 전략에 직접적으로 기여합니다.

## 🎯 주요 포인트

- 1. 전통적인 단어 기반 메트릭은 모델의 성공 또는 실패 이유를 드러내지 못한다.
- 2. Z-Scores는 다양한 비유창성 유형에 따라 시스템의 행동을 분류하는 언어학적 기반의 평가 메트릭이다.
- 3. Z-Scores는 생성된 텍스트와 비유창한 전사 간의 강력한 매핑을 통해 단어 수준 메트릭이 가리는 체계적 약점을 드러낸다.
- 4. Z-Scores는 모델의 실패 모드를 식별하고 맞춤형 프롬프트나 데이터 증강과 같은 목표 지향적 개입을 설계하는 데 도움을 준다.
- 5. 사례 연구에서 Z-Scores는 LLMs의 INTJ 및 PRN 비유창성 문제를 밝혀내어 모델 개선 전략에 직접적인 정보를 제공한다.


---

*Generated on 2025-09-25 16:06:20*