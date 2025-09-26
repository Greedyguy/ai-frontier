---
keywords:
  - Large Language Model
  - Self-supervised Learning
  - Multimodal Learning
  - Data-efficient Learning
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19856
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:40:57.847016",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Self-supervised Learning",
    "Multimodal Learning",
    "Data-efficient Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Self-supervised Learning": 0.8,
    "Multimodal Learning": 0.78,
    "Data-efficient Learning": 0.82
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
        "rationale": "The paper discusses implications for efficient model training in computationally expensive domains, specifically mentioning LLMs.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Self-supervised learning",
        "canonical": "Self-supervised Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "The method's applicability to self-supervised learning scenarios is highlighted, offering potential for significant advancements.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multimodal",
        "canonical": "Multimodal Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "The approach is extendable to multimodal learning, which is a trending area with high connectivity potential.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.78
      },
      {
        "surface": "Data-efficient learning",
        "canonical": "Data-efficient Learning",
        "aliases": [
          "Efficient Data Learning"
        ],
        "category": "unique_technical",
        "rationale": "The paper introduces a novel approach focusing on data efficiency, which is crucial for future AI advancements.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Self-supervised learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multimodal",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Data-efficient learning",
      "resolved_canonical": "Data-efficient Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Oversampling and Downsampling with Core-Boundary Awareness: A Data Quality-Driven Approach

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19856.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19856](https://arxiv.org/abs/2509.19856)

## 🔗 유사한 논문
- [[2025-09-22/Mind the Gap_ Data Rewriting for Stable Off-Policy Supervised Fine-Tuning_20250922|Mind the Gap: Data Rewriting for Stable Off-Policy Supervised Fine-Tuning]] (83.9% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (83.7% similar)
- [[2025-09-23/LASER_ Stratified Selective Sampling for Instruction Tuning with Dedicated Scoring Strategy_20250923|LASER: Stratified Selective Sampling for Instruction Tuning with Dedicated Scoring Strategy]] (83.5% similar)
- [[2025-09-22/Negotiated Representations to Prevent Overfitting in Machine Learning Applications_20250922|Negotiated Representations to Prevent Overfitting in Machine Learning Applications]] (83.0% similar)
- [[2025-09-18/Data coarse graining can improve model performance_20250918|Data coarse graining can improve model performance]] (82.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]], [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Data-efficient Learning|Data-efficient Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19856v1 Announce Type: new 
Abstract: The effectiveness of machine learning models, particularly in unbalanced classification tasks, is often hindered by the failure to differentiate between critical instances near the decision boundary and redundant samples concentrated in the core of the data distribution. In this paper, we propose a method to systematically identify and differentiate between these two types of data. Through extensive experiments on multiple benchmark datasets, we show that the boundary data oversampling method improves the F1 score by up to 10\% on 96\% of the datasets, whereas our core-aware reduction method compresses datasets up to 90\% while preserving their accuracy, making it 10 times more powerful than the original dataset. Beyond imbalanced classification, our method has broader implications for efficient model training, particularly in computationally expensive domains such as Large Language Model (LLM) training. By prioritizing high-quality, decision-relevant data, our approach can be extended to text, multimodal, and self-supervised learning scenarios, offering a pathway to faster convergence, improved generalization, and significant computational savings. This work paves the way for future research in data-efficient learning, where intelligent sampling replaces brute-force expansion, driving the next generation of AI advancements. Our code is available as a Python package at https://pypi.org/project/adaptive-resampling/ .

## 📝 요약

이 논문은 불균형 분류 작업에서 기계 학습 모델의 성능을 저해하는 문제를 해결하기 위해, 결정 경계 근처의 중요한 데이터와 데이터 중심부의 중복 샘플을 구별하는 방법을 제안합니다. 제안된 경계 데이터 오버샘플링 방법은 여러 벤치마크 데이터셋에서 F1 점수를 최대 10%까지 향상시켰으며, 코어 인식 축소 방법은 데이터셋을 최대 90%까지 압축하면서도 정확성을 유지합니다. 이 방법은 대규모 언어 모델(LLM) 훈련과 같은 계산 비용이 높은 분야에서 효율적인 모델 훈련을 가능하게 하며, 텍스트, 멀티모달, 자가 지도 학습 시나리오에서도 빠른 수렴과 일반화 향상, 계산 비용 절감을 제공합니다. 이 연구는 데이터 효율적 학습의 미래 연구를 위한 길을 열며, 지능형 샘플링이 무차별 확장을 대체하여 AI 발전을 이끌어갈 수 있음을 보여줍니다. 코드 패키지는 [여기](https://pypi.org/project/adaptive-resampling/)에서 제공됩니다.

## 🎯 주요 포인트

- 1. 본 논문은 결정 경계 근처의 중요한 데이터와 데이터 분포 중심의 중복 샘플을 구분하는 방법을 제안합니다.
- 2. 경계 데이터 오버샘플링 방법은 F1 점수를 최대 10% 향상시키며, 코어 인식 감소 방법은 데이터셋을 최대 90% 압축하면서 정확성을 유지합니다.
- 3. 제안된 방법은 대규모 언어 모델(LLM) 훈련과 같은 계산 비용이 큰 분야에서 효율적인 모델 훈련을 가능하게 합니다.
- 4. 본 연구는 텍스트, 멀티모달, 자가 지도 학습 시나리오에 적용 가능하며, 빠른 수렴, 개선된 일반화, 상당한 계산 절감을 제공합니다.
- 5. 데이터 효율적 학습에 대한 미래 연구의 길을 열며, 지능형 샘플링이 무차별 확장을 대체하는 AI 발전의 차세대를 이끌 것입니다.


---

*Generated on 2025-09-25 16:40:57*