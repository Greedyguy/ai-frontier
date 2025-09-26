---
keywords:
  - Psychological Behavior Model
  - Mere Exposure Effect
  - Hedonic Adaptation
  - Operant Conditioning
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.20304
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T17:02:59.747498",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Psychological Behavior Model",
    "Mere Exposure Effect",
    "Hedonic Adaptation",
    "Operant Conditioning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Psychological Behavior Model": 0.85,
    "Mere Exposure Effect": 0.8,
    "Hedonic Adaptation": 0.78,
    "Operant Conditioning": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "psychological behavior model",
        "canonical": "Psychological Behavior Model",
        "aliases": [
          "behavioral model",
          "psychological model"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's approach in optimizing ad schedules and is not commonly linked in existing vocabularies.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "mere exposure",
        "canonical": "Mere Exposure Effect",
        "aliases": [
          "exposure effect"
        ],
        "category": "specific_connectable",
        "rationale": "This psychological principle is a key factor in the model and can connect to broader discussions on user engagement.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      },
      {
        "surface": "hedonic adaptation",
        "canonical": "Hedonic Adaptation",
        "aliases": [
          "adaptation effect"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding this effect is crucial for optimizing ad frequency and timing, linking to behavioral economics.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "operant conditioning",
        "canonical": "Operant Conditioning",
        "aliases": [
          "conditioning effect"
        ],
        "category": "specific_connectable",
        "rationale": "This principle is used to model user interest decay, connecting to broader psychological and marketing strategies.",
        "novelty_score": 0.58,
        "connectivity_score": 0.82,
        "specificity_score": 0.76,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "ad-schedule",
      "optimal schedule",
      "user interest"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "psychological behavior model",
      "resolved_canonical": "Psychological Behavior Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "mere exposure",
      "resolved_canonical": "Mere Exposure Effect",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "hedonic adaptation",
      "resolved_canonical": "Hedonic Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "operant conditioning",
      "resolved_canonical": "Operant Conditioning",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.82,
        "specificity": 0.76,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Ads that Stick: Near-Optimal Ad Optimization through Psychological Behavior Models

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20304.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.20304](https://arxiv.org/abs/2509.20304)

## 🔗 유사한 논문
- [[2025-09-23/Auto-bidding under Return-on-Spend Constraints with Uncertainty Quantification_20250923|Auto-bidding under Return-on-Spend Constraints with Uncertainty Quantification]] (83.8% similar)
- [[2025-09-24/When Ads Become Profiles_ Large-Scale Audit of Algorithmic Biases and LLM Profiling Risks_20250924|When Ads Become Profiles: Large-Scale Audit of Algorithmic Biases and LLM Profiling Risks]] (81.8% similar)
- [[2025-09-19/JU-NLP at Touch\'e_ Covert Advertisement in Conversational AI-Generation and Detection Strategies_20250919|JU-NLP at Touch\'e: Covert Advertisement in Conversational AI-Generation and Detection Strategies]] (81.2% similar)
- [[2025-09-24/Leveraging Large Models to Evaluate Novel Content_ A Case Study on Advertisement Creativity_20250924|Leveraging Large Models to Evaluate Novel Content: A Case Study on Advertisement Creativity]] (80.9% similar)
- [[2025-09-22/Enhancing Generative Auto-bidding with Offline Reward Evaluation and Policy Search_20250922|Enhancing Generative Auto-bidding with Offline Reward Evaluation and Policy Search]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Mere Exposure Effect|Mere Exposure Effect]], [[keywords/Hedonic Adaptation|Hedonic Adaptation]], [[keywords/Operant Conditioning|Operant Conditioning]]
**⚡ Unique Technical**: [[keywords/Psychological Behavior Model|Psychological Behavior Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20304v1 Announce Type: cross 
Abstract: Optimizing the timing and frequency of ads is a central problem in digital advertising, with significant economic consequences. Existing scheduling policies rely on simple heuristics, such as uniform spacing and frequency caps, that overlook long-term user interest. However, it is well-known that users' long-term interest and engagement result from the interplay of several psychological effects (Curmei, Haupt, Recht, Hadfield-Menell, ACM CRS, 2022).
  In this work, we model change in user interest upon showing ads based on three key psychological principles: mere exposure, hedonic adaptation, and operant conditioning. The first two effects are modeled using a concave function of user interest with repeated exposure, while the third effect is modeled using a temporal decay function, which explains the decline in user interest due to overexposure. Under our psychological behavior model, we ask the following question: Given a continuous time interval $T$, how many ads should be shown, and at what times, to maximize the user interest towards the ads?
  Towards answering this question, we first show that, if the number of displayed ads is fixed, then the optimal ad-schedule only depends on the operant conditioning function. Our main result is a quasi-linear time algorithm that outputs a near-optimal ad-schedule, i.e., the difference in the performance of our schedule and the optimal schedule is exponentially small. Our algorithm leads to significant insights about optimal ad placement and shows that simple heuristics such as uniform spacing are sub-optimal under many natural settings. The optimal number of ads to display, which also depends on the mere exposure and hedonistic adaptation functions, can be found through a simple linear search given the above algorithm. We further support our findings with experimental results, demonstrating that our strategy outperforms various baselines.

## 📝 요약

이 논문은 디지털 광고에서 광고의 타이밍과 빈도를 최적화하는 문제를 다룹니다. 기존의 단순한 휴리스틱 방법은 사용자의 장기적인 관심을 간과합니다. 본 연구에서는 광고 노출이 사용자 관심에 미치는 영향을 세 가지 심리학적 원리인 단순 노출 효과, 쾌락적 적응, 조작적 조건화를 기반으로 모델링했습니다. 연구 결과, 광고 수가 고정된 경우 최적의 광고 일정은 조작적 조건화 함수에 의존하며, 제안된 알고리즘은 준선형 시간 내에 거의 최적의 광고 일정을 제공합니다. 실험 결과, 제안된 방법이 기존의 여러 기준보다 뛰어난 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 디지털 광고에서 광고의 타이밍과 빈도 최적화는 경제적 영향을 미치는 중요한 문제이다.
- 2. 사용자 관심 변화는 단순 노출, 쾌락적 적응, 조작적 조건화라는 세 가지 심리적 원칙에 기반하여 모델링된다.
- 3. 고정된 광고 수에서 최적의 광고 일정은 조작적 조건화 함수에만 의존한다.
- 4. 제안된 알고리즘은 준선형 시간 내에 거의 최적의 광고 일정을 산출하며, 단순한 균등 간격과 같은 기존의 휴리스틱이 비효율적임을 보여준다.
- 5. 실험 결과를 통해 제안된 광고 전략이 다양한 기준선보다 우수함을 입증하였다.


---

*Generated on 2025-09-25 17:02:59*