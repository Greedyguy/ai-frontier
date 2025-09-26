<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:10:06.710646",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "End-Cut Preference",
    "Survival Trees",
    "Classification and Regression Trees",
    "Smooth Sigmoid Surrogate"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "End-Cut Preference": 0.78,
    "Survival Trees": 0.77,
    "Classification and Regression Trees": 0.8,
    "Smooth Sigmoid Surrogate": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "End-Cut Preference",
        "canonical": "End-Cut Preference",
        "aliases": [
          "ECP"
        ],
        "category": "unique_technical",
        "rationale": "End-Cut Preference is a specific issue in decision trees, which can be linked to discussions on tree-based models.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Survival Trees",
        "canonical": "Survival Trees",
        "aliases": [
          "Survival Analysis Trees"
        ],
        "category": "specific_connectable",
        "rationale": "Survival Trees are a specialized form of decision trees, relevant for linking to survival analysis topics.",
        "novelty_score": 0.55,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "CART",
        "canonical": "Classification and Regression Trees",
        "aliases": [
          "CART"
        ],
        "category": "broad_technical",
        "rationale": "CART is a foundational algorithm in machine learning, providing strong links to tree-based methods.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Sigmoid Surrogate",
        "canonical": "Smooth Sigmoid Surrogate",
        "aliases": [
          "SSS"
        ],
        "category": "unique_technical",
        "rationale": "The Smooth Sigmoid Surrogate is a novel method proposed to address the End-Cut Preference issue.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "log-rank test statistic",
      "numerical illustrations"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "End-Cut Preference",
      "resolved_canonical": "End-Cut Preference",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Survival Trees",
      "resolved_canonical": "Survival Trees",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "CART",
      "resolved_canonical": "Classification and Regression Trees",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Sigmoid Surrogate",
      "resolved_canonical": "Smooth Sigmoid Surrogate",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# End-Cut Preference in Survival Trees

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18477.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18477](https://arxiv.org/abs/2509.18477)

## 🔗 유사한 논문
- [[2025-09-23/Regularizing Extrapolation in Causal Inference_20250923|Regularizing Extrapolation in Causal Inference]] (77.7% similar)
- [[2025-09-23/Conformal Prediction with Upper and Lower Bound Models_20250923|Conformal Prediction with Upper and Lower Bound Models]] (77.0% similar)
- [[2025-09-22/Improving Monte Carlo Tree Search for Symbolic Regression_20250922|Improving Monte Carlo Tree Search for Symbolic Regression]] (77.0% similar)
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (76.4% similar)
- [[2025-09-23/When Confidence Fails_ Revisiting Pseudo-Label Selection in Semi-supervised Semantic Segmentation_20250923|When Confidence Fails: Revisiting Pseudo-Label Selection in Semi-supervised Semantic Segmentation]] (76.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Classification and Regression Trees|Classification and Regression Trees]]
**🔗 Specific Connectable**: [[keywords/Survival Trees|Survival Trees]]
**⚡ Unique Technical**: [[keywords/End-Cut Preference|End-Cut Preference]], [[keywords/Smooth Sigmoid Surrogate|Smooth Sigmoid Surrogate]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18477v1 Announce Type: cross 
Abstract: The end-cut preference (ECP) problem, referring to the tendency to favor split points near the boundaries of a feature's range, is a well-known issue in CART (Breiman et al., 1984). ECP may induce highly imbalanced and biased splits, obscure weak signals, and lead to tree structures that are both unstable and difficult to interpret. For survival trees, we show that ECP also arises when using greedy search to select the optimal cutoff point by maximizing the log-rank test statistic. To address this issue, we propose a smooth sigmoid surrogate (SSS) approach, in which the hard-threshold indicator function is replaced by a smooth sigmoid function. We further demonstrate, both theoretically and through numerical illustrations, that SSS provides an effective remedy for mitigating or avoiding ECP.

## 📝 요약

이 논문은 CART 알고리즘에서 발생하는 끝점 선호 문제(ECP)를 다룹니다. ECP는 불균형하고 편향된 분할을 유도하며, 약한 신호를 감추고 해석이 어려운 트리 구조를 초래할 수 있습니다. 특히 생존 분석 트리에서 ECP는 로그 순위 검정 통계를 최대화하는 탐욕적 탐색 시 발생할 수 있습니다. 이를 해결하기 위해, 저자들은 하드 임계값 지시 함수 대신 부드러운 시그모이드 함수를 사용하는 SSS(부드러운 시그모이드 대체) 방법을 제안합니다. 이 방법은 이론적 분석과 수치적 예시를 통해 ECP를 완화하거나 피하는 데 효과적임을 보여줍니다.

## 🎯 주요 포인트

- 1. 끝점 선호 문제(ECP)는 CART에서 잘 알려진 문제로, 특징 범위의 경계 근처에서 분할점을 선호하는 경향을 말합니다.
- 2. ECP는 불균형하고 편향된 분할을 유도하고, 약한 신호를 가리며, 불안정하고 해석하기 어려운 트리 구조를 초래할 수 있습니다.
- 3. 생존 트리에서 ECP는 로그 순위 검정 통계를 최대화하여 최적의 절단점을 선택할 때 발생할 수 있습니다.
- 4. 이 문제를 해결하기 위해, 우리는 하드 임계값 지시자 함수를 부드러운 시그모이드 함수로 대체하는 부드러운 시그모이드 대체(SSS) 접근법을 제안합니다.
- 5. SSS는 이론적으로나 수치적 예시를 통해 ECP를 완화하거나 회피하는 데 효과적인 해결책을 제공함을 보여줍니다.


---

*Generated on 2025-09-24 15:10:06*