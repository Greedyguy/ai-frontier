<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:46:10.989455",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Sentiment Analysis",
    "Developer Satisfaction",
    "Conversational AI",
    "Usage Logs"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Sentiment Analysis": 0.82,
    "Developer Satisfaction": 0.74,
    "Conversational AI": 0.71,
    "Usage Logs": 0.73
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "sentiment analysis",
        "canonical": "Sentiment Analysis",
        "aliases": [
          "emotion detection",
          "opinion mining"
        ],
        "category": "specific_connectable",
        "rationale": "Sentiment analysis is a key technique used to infer user satisfaction from developer prompts, linking it to broader NLP applications.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "developer satisfaction",
        "canonical": "Developer Satisfaction",
        "aliases": [
          "programmer satisfaction",
          "coder satisfaction"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's goal of evaluating conversational AI effectiveness, offering a unique angle for user experience research.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.81,
        "link_intent_score": 0.74
      },
      {
        "surface": "conversational AI assistants",
        "canonical": "Conversational AI",
        "aliases": [
          "chatbot",
          "virtual assistant"
        ],
        "category": "broad_technical",
        "rationale": "Conversational AI is a broad technical area relevant to the study of user interactions and satisfaction.",
        "novelty_score": 0.45,
        "connectivity_score": 0.79,
        "specificity_score": 0.64,
        "link_intent_score": 0.71
      },
      {
        "surface": "industrial usage logs",
        "canonical": "Usage Logs",
        "aliases": [
          "interaction logs",
          "activity logs"
        ],
        "category": "unique_technical",
        "rationale": "Usage logs provide empirical data crucial for analyzing developer interactions and satisfaction.",
        "novelty_score": 0.66,
        "connectivity_score": 0.72,
        "specificity_score": 0.77,
        "link_intent_score": 0.73
      }
    ],
    "ban_list_suggestions": [
      "user feedback",
      "developer prompts",
      "feedback channels"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "sentiment analysis",
      "resolved_canonical": "Sentiment Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "developer satisfaction",
      "resolved_canonical": "Developer Satisfaction",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.81,
        "link_intent": 0.74
      }
    },
    {
      "candidate_surface": "conversational AI assistants",
      "resolved_canonical": "Conversational AI",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.79,
        "specificity": 0.64,
        "link_intent": 0.71
      }
    },
    {
      "candidate_surface": "industrial usage logs",
      "resolved_canonical": "Usage Logs",
      "decision": "linked",
      "scores": {
        "novelty": 0.66,
        "connectivity": 0.72,
        "specificity": 0.77,
        "link_intent": 0.73
      }
    }
  ]
}
-->

# Reading Between the Lines: Scalable User Feedback via Implicit Sentiment in Developer Prompts

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18361.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18361](https://arxiv.org/abs/2509.18361)

## 🔗 유사한 논문
- [[2025-09-23/SENSE-7_ Taxonomy and Dataset for Measuring User Perceptions of Empathy in Sustained Human-AI Conversations_20250923|SENSE-7: Taxonomy and Dataset for Measuring User Perceptions of Empathy in Sustained Human-AI Conversations]] (82.3% similar)
- [[2025-09-23/A Similarity Measure for Comparing Conversational Dynamics_20250923|A Similarity Measure for Comparing Conversational Dynamics]] (80.0% similar)
- [[2025-09-18/Calibrated Generative AI as Meta-Reviewer_ A Systemic Functional Linguistics Discourse Analysis of Reviews of Peer Reviews_20250918|Calibrated Generative AI as Meta-Reviewer: A Systemic Functional Linguistics Discourse Analysis of Reviews of Peer Reviews]] (79.0% similar)
- [[2025-09-23/The Good, the Bad and the Constructive_ Automatically Measuring Peer Review's Utility for Authors_20250923|The Good, the Bad and the Constructive: Automatically Measuring Peer Review's Utility for Authors]] (79.0% similar)
- [[2025-09-18/Designing AI-Agents with Personalities_ A Psychometric Approach_20250918|Designing AI-Agents with Personalities: A Psychometric Approach]] (79.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Conversational AI|Conversational AI]]
**🔗 Specific Connectable**: [[keywords/Sentiment Analysis|Sentiment Analysis]]
**⚡ Unique Technical**: [[keywords/Developer Satisfaction|Developer Satisfaction]], [[keywords/Usage Logs|Usage Logs]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18361v1 Announce Type: cross 
Abstract: Evaluating developer satisfaction with conversational AI assistants at scale is critical but challenging. User studies provide rich insights, but are unscalable, while large-scale quantitative signals from logs or in-product ratings are often too shallow or sparse to be reliable. To address this gap, we propose and evaluate a new approach: using sentiment analysis of developer prompts to identify implicit signals of user satisfaction. With an analysis of industrial usage logs of 372 professional developers, we show that this approach can identify a signal in ~8% of all interactions, a rate more than 13 times higher than explicit user feedback, with reasonable accuracy even with an off-the-shelf sentiment analysis approach. This new practical approach to complement existing feedback channels would open up new directions for building a more comprehensive understanding of the developer experience at scale.

## 📝 요약

이 논문은 대규모로 개발자의 대화형 AI 비서에 대한 만족도를 평가하는 새로운 접근법을 제안합니다. 기존의 사용자 연구는 깊이 있는 통찰을 제공하지만 확장성이 부족하고, 로그나 제품 내 평가를 통한 대규모 정량적 신호는 신뢰성이 떨어집니다. 이를 해결하기 위해, 개발자 프롬프트의 감정 분석을 통해 사용자 만족도의 암묵적 신호를 식별하는 방법을 제안하고 평가했습니다. 372명의 전문 개발자 사용 로그 분석 결과, 이 방법은 전체 상호작용의 약 8%에서 신호를 식별할 수 있었으며, 이는 명시적 사용자 피드백보다 13배 이상 높은 비율입니다. 이 접근법은 기존 피드백 채널을 보완하여 대규모로 개발자 경험을 더 잘 이해할 수 있는 새로운 방향을 제시합니다.

## 🎯 주요 포인트

- 1. 대규모로 대화형 AI 비서에 대한 개발자 만족도를 평가하는 것은 중요하지만 도전적인 과제이다.
- 2. 사용자 연구는 깊이 있는 통찰을 제공하지만 확장성이 부족하고, 로그나 제품 내 평가에서 얻는 대규모 정량적 신호는 종종 신뢰하기에 얕거나 드문 경우가 많다.
- 3. 개발자 프롬프트의 감정 분석을 통해 사용자 만족도의 암묵적 신호를 식별하는 새로운 접근 방식을 제안하고 평가하였다.
- 4. 372명의 전문 개발자 사용 로그 분석을 통해 이 접근 방식이 전체 상호작용의 약 8%에서 신호를 식별할 수 있음을 보여주었다.
- 5. 이 새로운 실용적 접근 방식은 기존 피드백 채널을 보완하여 대규모로 개발자 경험을 보다 포괄적으로 이해하는 새로운 방향을 열어줄 것이다.


---

*Generated on 2025-09-24 13:46:10*