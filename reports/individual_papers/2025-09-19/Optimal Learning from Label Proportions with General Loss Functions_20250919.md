---
keywords:
  - Sample Complexity
  - Learning from Label Proportions
  - Loss Functions
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.15145
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:30:22.570195",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Sample Complexity",
    "Learning from Label Proportions",
    "Loss Functions"
  ],
  "rejected_keywords": [
    "De-biasing Techniques"
  ],
  "similarity_scores": {
    "Sample Complexity": 0.79,
    "Learning from Label Proportions": 0.78,
    "Loss Functions": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Optimal Learning from Label Proportions with General Loss Functions

**Korean Title:** 라벨 비율로부터의 최적 학습과 일반 손실 함수

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Loss Functions|loss functions]]
**🔗 Specific Connectable**: [[keywords/Sample Complexity|sample complexity guarantees]]
**⚡ Unique Technical**: [[keywords/Learning from Label Proportions|Learning from Label Proportions]]

## 🔗 유사한 논문
- [[Zero-Shot LLMs in Human-in-the-Loop RL Replacing Human Feedback for Reward Shaping]] (81.0% similar)
- [[Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (79.4% similar)
- [[Multi-Fidelity_Hybrid_Reinforcement_Learning_via_Information_Gain_Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (79.3% similar)
- [[SMARTER A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models]] (78.9% similar)
- [[FlowRL Matching Reward Distributions for LLM Reasoning]] (78.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15145v1 Announce Type: new 
Abstract: Motivated by problems in online advertising, we address the task of Learning from Label Proportions (LLP). In this partially-supervised setting, training data consists of groups of examples, termed bags, for which we only observe the average label value. The main goal, however, remains the design of a predictor for the labels of individual examples. We introduce a novel and versatile low-variance de-biasing methodology to learn from aggregate label information, significantly advancing the state of the art in LLP. Our approach exhibits remarkable flexibility, seamlessly accommodating a broad spectrum of practically relevant loss functions across both binary and multi-class classification settings. By carefully combining our estimators with standard techniques, we substantially improve sample complexity guarantees for a large class of losses of practical relevance. We also empirically validate the efficacy of our proposed approach across a diverse array of benchmark datasets, demonstrating compelling empirical advantages over standard baselines.

## 🔍 Abstract (한글 번역)

arXiv:2509.15145v1 발표 유형: 신규  
초록: 온라인 광고 문제에서 동기를 얻어, 우리는 비율에 따른 학습(LLP) 과제를 다룹니다. 이 부분적으로 지도된 환경에서, 훈련 데이터는 '가방'이라고 불리는 예제 그룹으로 구성되며, 우리는 이 그룹의 평균 레이블 값만을 관찰합니다. 그러나 주된 목표는 개별 예제의 레이블에 대한 예측기를 설계하는 것입니다. 우리는 집계된 레이블 정보를 학습하기 위한 새로운 다목적 저분산 편향 제거 방법론을 소개하여 LLP의 최신 기술 수준을 크게 발전시켰습니다. 우리의 접근법은 이진 및 다중 클래스 분류 설정 모두에서 실질적으로 관련 있는 손실 함수의 광범위한 스펙트럼을 원활하게 수용하며 놀라운 유연성을 보여줍니다. 우리의 추정기를 표준 기법과 신중하게 결합함으로써, 실질적으로 관련 있는 손실의 큰 범주에 대해 샘플 복잡성 보장을 상당히 개선했습니다. 또한 다양한 벤치마크 데이터셋에서 제안된 접근법의 효능을 실증적으로 검증하여, 표준 기준보다 설득력 있는 실증적 이점을 입증했습니다.

## 📝 요약

이 논문은 온라인 광고 문제를 해결하기 위해 라벨 비율 학습(LLP) 문제를 다룹니다. LLP는 부분적으로 감독된 학습 설정으로, 훈련 데이터는 평균 라벨 값만 관측되는 그룹(백)으로 구성됩니다. 주요 목표는 개별 예제의 라벨을 예측하는 것입니다. 저자들은 집계된 라벨 정보로부터 학습하기 위한 새로운 저분산 편향 제거 방법론을 제안하여 LLP 분야의 최첨단을 크게 발전시켰습니다. 이 방법론은 이진 및 다중 클래스 분류 설정에서 다양한 손실 함수를 유연하게 수용할 수 있습니다. 제안된 방법은 표준 기법과 결합하여 실질적으로 중요한 손실 클래스에 대한 샘플 복잡성 보장을 향상시킵니다. 다양한 벤치마크 데이터셋을 통해 제안된 방법의 효율성을 실증적으로 검증하였으며, 기존의 기준보다 뛰어난 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 온라인 광고 문제를 해결하기 위해 라벨 비율 학습(LLP) 문제를 다룹니다.

- 2. 집단의 평균 라벨 값만 관찰 가능한 부분적으로 지도된 환경에서 개별 예제의 라벨을 예측하는 것이 주요 목표입니다.

- 3. 집합 라벨 정보로부터 학습하기 위한 새로운 저분산 편향 제거 방법론을 도입하여 LLP의 최신 기술을 크게 발전시켰습니다.

- 4. 제안된 방법은 이진 및 다중 클래스 분류 설정에서 다양한 손실 함수에 유연하게 적용 가능합니다.

- 5. 다양한 벤치마크 데이터셋에서 제안된 접근법의 효능을 실증적으로 검증하여 표준 기준보다 뛰어난 성능을 입증했습니다.

---

*Generated on 2025-09-19 15:31:36*