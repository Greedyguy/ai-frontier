---
keywords:
  - Large Language Model
  - Cognitive Bias
  - Adversarial Manipulation
  - Product Recommendation
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2502.01349
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:39:47.351318",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Cognitive Bias",
    "Adversarial Manipulation",
    "Product Recommendation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Cognitive Bias": 0.78,
    "Adversarial Manipulation": 0.77,
    "Product Recommendation": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "As a foundational technology, it connects to various advancements and challenges in AI-driven applications.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Cognitive Biases",
        "canonical": "Cognitive Bias",
        "aliases": [
          "Cognitive Biases"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's exploration of psychological influences on AI behavior.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Adversarial Manipulation",
        "canonical": "Adversarial Manipulation",
        "aliases": [
          "Adversarial Attack"
        ],
        "category": "unique_technical",
        "rationale": "Understanding adversarial techniques is crucial for improving the robustness of AI models.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "Product Recommendations",
        "canonical": "Product Recommendation",
        "aliases": [
          "Product Recommenders"
        ],
        "category": "specific_connectable",
        "rationale": "This is a key application area for LLMs, relevant to commercial AI deployment.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "advent",
      "approach",
      "evaluation"
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
      "candidate_surface": "Cognitive Biases",
      "resolved_canonical": "Cognitive Bias",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Adversarial Manipulation",
      "resolved_canonical": "Adversarial Manipulation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Product Recommendations",
      "resolved_canonical": "Product Recommendation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Bias Beware: The Impact of Cognitive Biases on LLM-Driven Product Recommendations

**Korean Title:** 편향 주의: LLM 기반 제품 추천에 대한 인지 편향의 영향

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2502.01349.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2502.01349](https://arxiv.org/abs/2502.01349)

## 🔗 유사한 논문
- [[2025-09-17/Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (88.2% similar)
- [[2025-09-18/How Does Cognitive Bias Affect Large Language Models? A Case Study on the Anchoring Effect in Price Negotiation Simulations_20250918|How Does Cognitive Bias Affect Large Language Models? A Case Study on the Anchoring Effect in Price Negotiation Simulations]] (87.9% similar)
- [[2025-09-18/Do LLMs Align Human Values Regarding Social Biases? Judging and Explaining Social Biases with LLMs_20250918|Do LLMs Align Human Values Regarding Social Biases? Judging and Explaining Social Biases with LLMs]] (86.4% similar)
- [[2025-09-22/Exploring the Impact of Personality Traits on LLM Bias and Toxicity_20250922|Exploring the Impact of Personality Traits on LLM Bias and Toxicity]] (86.0% similar)
- [[2025-09-22/Benchmarking Debiasing Methods for LLM-based Parameter Estimates_20250922|Benchmarking Debiasing Methods for LLM-based Parameter Estimates]] (85.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Product Recommendation|Product Recommendation]]
**⚡ Unique Technical**: [[keywords/Cognitive Bias|Cognitive Bias]], [[keywords/Adversarial Manipulation|Adversarial Manipulation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.01349v3 Announce Type: replace 
Abstract: The advent of Large Language Models (LLMs) has revolutionized product recommenders, yet their susceptibility to adversarial manipulation poses critical challenges, particularly in real-world commercial applications. Our approach is the first one to tap into human psychological principles, seamlessly modifying product descriptions, making such manipulations hard to detect. In this work, we investigate cognitive biases as black-box adversarial strategies, drawing parallels between their effects on LLMs and human purchasing behavior. Through extensive evaluation across models of varying scale, we find that certain biases, such as social proof, consistently boost product recommendation rate and ranking, while others, like scarcity and exclusivity, surprisingly reduce visibility. Our results demonstrate that cognitive biases are deeply embedded in state-of-the-art LLMs, leading to highly unpredictable behavior in product recommendations and posing significant challenges for effective mitigation.

## 🔍 Abstract (한글 번역)

arXiv:2502.01349v3 발표 유형: 교체  
초록: 대형 언어 모델(LLM)의 등장은 제품 추천 시스템에 혁신을 가져왔으나, 이들의 적대적 조작에 대한 취약성은 특히 실제 상업적 응용에서 중요한 도전 과제를 제기합니다. 우리의 접근법은 인간의 심리적 원칙을 활용하여 제품 설명을 매끄럽게 수정함으로써 이러한 조작을 탐지하기 어렵게 만드는 최초의 방법입니다. 본 연구에서는 인지 편향을 블랙박스 적대적 전략으로 조사하며, LLM과 인간의 구매 행동에 미치는 영향을 비교합니다. 다양한 규모의 모델에 대한 광범위한 평가를 통해, 사회적 증거와 같은 특정 편향이 제품 추천 비율과 순위를 일관되게 향상시키는 반면, 희소성과 독점성 같은 다른 편향은 놀랍게도 가시성을 감소시킨다는 것을 발견했습니다. 우리의 결과는 인지 편향이 최첨단 LLM에 깊이 내재되어 있어 제품 추천에서 매우 예측 불가능한 행동을 초래하고 효과적인 완화를 위한 상당한 도전 과제를 제기함을 보여줍니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 제품 추천 시스템에서 발생할 수 있는 적대적 조작 문제를 다룹니다. 연구진은 인간의 심리적 원칙을 활용하여 제품 설명을 미세하게 조정하는 방법을 제안하였으며, 이를 통해 조작을 탐지하기 어렵게 만들었습니다. 다양한 규모의 모델을 평가한 결과, 사회적 증거와 같은 인지 편향이 제품 추천률과 순위를 높이는 반면, 희소성과 독점성은 오히려 가시성을 감소시켰습니다. 이러한 결과는 최신 LLM에 인지 편향이 깊이 내재되어 있어 제품 추천에서 예측 불가능한 행동을 유발하며, 효과적인 완화에 큰 도전이 된다는 것을 보여줍니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)의 발전은 제품 추천 시스템에 혁신을 가져왔으나, 적대적 조작에 취약하여 상업적 응용에서 중요한 문제를 제기한다.
- 2. 본 연구는 인간의 심리적 원칙을 활용하여 제품 설명을 수정함으로써 조작을 탐지하기 어렵게 만드는 최초의 접근법을 제시한다.
- 3. 인지 편향을 블랙박스 적대적 전략으로 조사하여, LLM과 인간 구매 행동에 미치는 영향을 비교 분석하였다.
- 4. 사회적 증거와 같은 특정 편향은 제품 추천 비율과 순위를 일관되게 높이는 반면, 희소성과 독점성은 가시성을 감소시키는 것으로 나타났다.
- 5. 인지 편향이 최첨단 LLM에 깊이 내재되어 있어 제품 추천에서 예측 불가능한 행동을 초래하며 효과적인 완화에 큰 도전 과제를 제시한다.


---

*Generated on 2025-09-23 11:39:47*