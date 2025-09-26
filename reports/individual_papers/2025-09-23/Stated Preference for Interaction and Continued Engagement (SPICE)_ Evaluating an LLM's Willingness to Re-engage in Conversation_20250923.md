---
keywords:
  - Large Language Model
  - SPICE
  - Abuse Classification
  - Rao-Scott Adjustment
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.09043
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:27:09.253298",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "SPICE",
    "Abuse Classification",
    "Rao-Scott Adjustment"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "SPICE": 0.88,
    "Abuse Classification": 0.78,
    "Rao-Scott Adjustment": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "A fundamental technology discussed in the paper, essential for understanding SPICE's application.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Stated Preference for Interaction and Continued Engagement",
        "canonical": "SPICE",
        "aliases": [
          "SPICE"
        ],
        "category": "unique_technical",
        "rationale": "A unique diagnostic tool introduced in the paper, crucial for linking to studies on model interaction.",
        "novelty_score": 0.95,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "abuse classification",
        "canonical": "Abuse Classification",
        "aliases": [
          "abuse detection"
        ],
        "category": "specific_connectable",
        "rationale": "Relevant for linking to topics on content moderation and model ethics.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Rao-Scott adjustment",
        "canonical": "Rao-Scott Adjustment",
        "aliases": [
          "Rao-Scott test"
        ],
        "category": "specific_connectable",
        "rationale": "A statistical method used in the paper, useful for linking to statistical analysis techniques.",
        "novelty_score": 0.6,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "interaction",
      "study",
      "model"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Model",
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
      "candidate_surface": "Stated Preference for Interaction and Continued Engagement",
      "resolved_canonical": "SPICE",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "abuse classification",
      "resolved_canonical": "Abuse Classification",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Rao-Scott adjustment",
      "resolved_canonical": "Rao-Scott Adjustment",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Stated Preference for Interaction and Continued Engagement (SPICE): Evaluating an LLM's Willingness to Re-engage in Conversation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.09043.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.09043](https://arxiv.org/abs/2509.09043)

## 🔗 유사한 논문
- [[2025-09-19/SPICE_ An Automated SWE-Bench Labeling Pipeline for Issue Clarity, Test Coverage, and Effort Estimation_20250919|SPICE: An Automated SWE-Bench Labeling Pipeline for Issue Clarity, Test Coverage, and Effort Estimation]] (81.9% similar)
- [[2025-09-23/AIPsychoBench_ Understanding the Psychometric Differences between LLMs and Humans_20250923|AIPsychoBench: Understanding the Psychometric Differences between LLMs and Humans]] (81.1% similar)
- [[2025-09-23/MIST_ Jailbreaking Black-box Large Language Models via Iterative Semantic Tuning_20250923|MIST: Jailbreaking Black-box Large Language Models via Iterative Semantic Tuning]] (81.1% similar)
- [[2025-09-22/From Judgment to Interference_ Early Stopping LLM Harmful Outputs via Streaming Content Monitoring_20250922|From Judgment to Interference: Early Stopping LLM Harmful Outputs via Streaming Content Monitoring]] (81.1% similar)
- [[2025-09-22/Fine-Tuning Large Multimodal Models for Automatic Pronunciation Assessment_20250922|Fine-Tuning Large Multimodal Models for Automatic Pronunciation Assessment]] (81.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Abuse Classification|Abuse Classification]], [[keywords/Rao-Scott Adjustment|Rao-Scott Adjustment]]
**⚡ Unique Technical**: [[keywords/SPICE|SPICE]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.09043v2 Announce Type: replace-cross 
Abstract: We introduce and evaluate Stated Preference for Interaction and Continued Engagement (SPICE), a simple diagnostic signal elicited by asking a Large Language Model a YES or NO question about its willingness to re-engage with a user's behavior after reviewing a short transcript. In a study using a 3-tone (friendly, unclear, abusive) by 10-interaction stimulus set, we tested four open-weight chat models across four framing conditions, resulting in 480 trials. Our findings show that SPICE sharply discriminates by user tone. Friendly interactions yielded a near-unanimous preference to continue (97.5% YES), while abusive interactions yielded a strong preference to discontinue (17.9% YES), with unclear interactions falling in between (60.4% YES). This core association remains decisive under multiple dependence-aware statistical tests, including Rao-Scott adjustment and cluster permutation tests. Furthermore, we demonstrate that SPICE provides a distinct signal from abuse classification. In trials where a model failed to identify abuse, it still overwhelmingly stated a preference not to continue the interaction (81% of the time). An exploratory analysis also reveals a significant interaction effect: a preamble describing the study context significantly impacts SPICE under ambiguity, but only when transcripts are presented as a single block of text rather than a multi-turn chat. The results validate SPICE as a robust, low-overhead, and reproducible tool for auditing model dispositions, complementing existing metrics by offering a direct, relational signal of a model's state. All stimuli, code, and analysis scripts are released to support replication.

## 📝 요약

이 논문은 사용자의 행동에 대한 대형 언어 모델의 재참여 의사를 YES 또는 NO로 묻는 SPICE라는 진단 신호를 소개하고 평가합니다. 연구는 세 가지 톤(친근한, 불명확한, 공격적인)과 10번의 상호작용 자극 세트를 사용하여 네 가지 오픈 웨이트 채팅 모델을 테스트하였으며, 총 480번의 실험을 수행했습니다. 결과는 SPICE가 사용자 톤에 따라 명확히 구분됨을 보여줍니다. 친근한 상호작용에서는 97.5%가 재참여를 선호했으며, 공격적인 상호작용에서는 17.9%만이 재참여를 선호했습니다. SPICE는 학대 분류와는 다른 신호를 제공하며, 모델이 학대를 식별하지 못한 경우에도 81%가 상호작용을 지속하지 않겠다고 응답했습니다. 연구 맥락을 설명하는 서문이 모호한 상황에서 SPICE에 영향을 미치는 중요한 상호작용 효과도 발견되었습니다. SPICE는 모델의 상태를 직접적으로 평가할 수 있는 강력하고 재현 가능한 도구로 검증되었습니다. 모든 자극, 코드, 분석 스크립트는 재현성을 지원하기 위해 공개되었습니다.

## 🎯 주요 포인트

- 1. SPICE는 사용자 톤에 따라 명확하게 구별되는 신호를 제공하며, 친근한 상호작용에서는 97.5%의 모델이 재참여를 선호했습니다.
- 2. SPICE는 학대 분류와는 별개의 신호를 제공하며, 모델이 학대를 식별하지 못한 경우에도 81%의 경우 상호작용을 계속하지 않겠다는 의사를 밝혔습니다.
- 3. 연구 맥락을 설명하는 서문이 모호한 상황에서 SPICE에 유의미한 영향을 미치며, 이는 텍스트가 단일 블록으로 제공될 때만 나타났습니다.
- 4. SPICE는 모델의 상태를 직접적으로 나타내는 신호를 제공하여 기존의 메트릭을 보완하는 강력하고 재현 가능한 도구로 검증되었습니다.
- 5. 모든 자극, 코드, 분석 스크립트가 공개되어 연구의 재현성을 지원합니다.


---

*Generated on 2025-09-24 01:27:09*