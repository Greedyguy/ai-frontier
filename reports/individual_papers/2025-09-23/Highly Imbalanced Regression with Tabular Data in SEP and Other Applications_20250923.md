---
keywords:
  - Imbalanced Regression
  - Solar Energetic Particle Events
  - Stratified Sampling
  - Monotonically Decreasing Involution Importance
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16339
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:14:33.659256",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Imbalanced Regression",
    "Solar Energetic Particle Events",
    "Stratified Sampling",
    "Monotonically Decreasing Involution Importance"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Imbalanced Regression": 0.78,
    "Solar Energetic Particle Events": 0.77,
    "Stratified Sampling": 0.72,
    "Monotonically Decreasing Involution Importance": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "imbalanced regression",
        "canonical": "Imbalanced Regression",
        "aliases": [
          "highly imbalanced regression"
        ],
        "category": "unique_technical",
        "rationale": "Addresses a specific challenge in regression tasks that is crucial for accurate predictions in rare event forecasting.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Solar Energetic Particle events",
        "canonical": "Solar Energetic Particle Events",
        "aliases": [
          "SEP events"
        ],
        "category": "unique_technical",
        "rationale": "A specific application domain for the proposed method, linking to research in space weather prediction.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "stratified sampling",
        "canonical": "Stratified Sampling",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "A well-known statistical method that enhances the proposed technique's effectiveness by ensuring representation of rare instances.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      },
      {
        "surface": "Monotonically Decreasing Involution importance",
        "canonical": "Monotonically Decreasing Involution Importance",
        "aliases": [
          "MDI importance"
        ],
        "category": "unique_technical",
        "rationale": "A novel importance function introduced in the paper, enhancing the regression model's performance.",
        "novelty_score": 0.8,
        "connectivity_score": 0.55,
        "specificity_score": 0.88,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "forecasting",
      "mini-batches",
      "recent methods"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "imbalanced regression",
      "resolved_canonical": "Imbalanced Regression",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Solar Energetic Particle events",
      "resolved_canonical": "Solar Energetic Particle Events",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "stratified sampling",
      "resolved_canonical": "Stratified Sampling",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Monotonically Decreasing Involution importance",
      "resolved_canonical": "Monotonically Decreasing Involution Importance",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.55,
        "specificity": 0.88,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Highly Imbalanced Regression with Tabular Data in SEP and Other Applications

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16339.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16339](https://arxiv.org/abs/2509.16339)

## 🔗 유사한 논문
- [[2025-09-22/Improving Monte Carlo Tree Search for Symbolic Regression_20250922|Improving Monte Carlo Tree Search for Symbolic Regression]] (78.5% similar)
- [[2025-09-22/Highly Efficient Direct Analytics on Semantic-aware Time Series Data Compression_20250922|Highly Efficient Direct Analytics on Semantic-aware Time Series Data Compression]] (78.0% similar)
- [[2025-09-22/Neural Networks for Learnable and Scalable Influence Estimation of Instruction Fine-Tuning Data_20250922|Neural Networks for Learnable and Scalable Influence Estimation of Instruction Fine-Tuning Data]] (77.7% similar)
- [[2025-09-18/Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (77.7% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (77.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Stratified Sampling|Stratified Sampling]]
**⚡ Unique Technical**: [[keywords/Imbalanced Regression|Imbalanced Regression]], [[keywords/Solar Energetic Particle Events|Solar Energetic Particle Events]], [[keywords/Monotonically Decreasing Involution Importance|Monotonically Decreasing Involution Importance]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16339v1 Announce Type: cross 
Abstract: We investigate imbalanced regression with tabular data that have an imbalance ratio larger than 1,000 ("highly imbalanced"). Accurately estimating the target values of rare instances is important in applications such as forecasting the intensity of rare harmful Solar Energetic Particle (SEP) events. For regression, the MSE loss does not consider the correlation between predicted and actual values. Typical inverse importance functions allow only convex functions. Uniform sampling might yield mini-batches that do not have rare instances. We propose CISIR that incorporates correlation, Monotonically Decreasing Involution (MDI) importance, and stratified sampling. Based on five datasets, our experimental results indicate that CISIR can achieve lower error and higher correlation than some recent methods. Also, adding our correlation component to other recent methods can improve their performance. Lastly, MDI importance can outperform other importance functions. Our code can be found in https://github.com/Machine-Earning/CISIR.

## 📝 요약

이 논문은 불균형 비율이 1,000 이상인 테이블 데이터의 불균형 회귀 문제를 다룹니다. 드문 사례의 목표 값을 정확히 추정하는 것은 희귀한 해로운 태양 에너지 입자(SEP) 사건의 강도 예측 등에서 중요합니다. 기존의 평균 제곱 오차(MSE) 손실은 예측 값과 실제 값 간의 상관관계를 고려하지 않으며, 일반적인 역중요도 함수는 오직 볼록 함수만을 허용합니다. 또한, 균일 샘플링은 드문 사례를 포함하지 않을 수 있습니다. 이를 해결하기 위해, 상관관계, 단조 감소 변환(MDI) 중요도, 층화 샘플링을 포함한 CISIR을 제안합니다. 다섯 개의 데이터셋을 기반으로 한 실험 결과, CISIR은 최신 방법들보다 낮은 오류와 높은 상관관계를 달성할 수 있음을 보여줍니다. 또한, 상관관계 요소를 다른 최신 방법에 추가하면 성능이 향상될 수 있으며, MDI 중요도는 다른 중요도 함수보다 우수할 수 있습니다. 코드: https://github.com/Machine-Earning/CISIR.

## 🎯 주요 포인트

- 1. 본 연구는 불균형 비율이 1,000 이상인 테이블형 데이터의 불균형 회귀 문제를 조사합니다.
- 2. 희귀 사례의 목표 값을 정확히 추정하는 것은 드문 해로운 태양 에너지 입자(SEP) 사건의 강도 예측과 같은 응용 분야에서 중요합니다.
- 3. 제안된 CISIR 방법은 상관관계, 단조 감소 변환(MDI) 중요도, 계층화된 샘플링을 통합하여 더 낮은 오류와 더 높은 상관관계를 달성할 수 있습니다.
- 4. 상관관계 요소를 다른 최신 방법에 추가하면 성능을 개선할 수 있습니다.
- 5. MDI 중요도는 다른 중요도 함수보다 우수한 성능을 보일 수 있습니다.


---

*Generated on 2025-09-23 23:14:33*