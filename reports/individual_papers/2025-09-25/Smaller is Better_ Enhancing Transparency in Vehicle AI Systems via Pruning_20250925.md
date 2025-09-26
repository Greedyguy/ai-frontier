---
keywords:
  - Model Pruning
  - Autonomous Vehicles
  - Post-hoc Explanations
  - Traffic Sign Classification
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.20148
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:13:10.992222",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Model Pruning",
    "Autonomous Vehicles",
    "Post-hoc Explanations",
    "Traffic Sign Classification"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Model Pruning": 0.85,
    "Autonomous Vehicles": 0.78,
    "Post-hoc Explanations": 0.82,
    "Traffic Sign Classification": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "pruning",
        "canonical": "Model Pruning",
        "aliases": [
          "pruning technique",
          "pruning method"
        ],
        "category": "unique_technical",
        "rationale": "Pruning is highlighted as a key strategy for enhancing transparency and efficiency in AI systems, making it a unique and relevant concept for linking.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      },
      {
        "surface": "autonomous vehicles",
        "canonical": "Autonomous Vehicles",
        "aliases": [
          "self-driving cars",
          "driverless vehicles"
        ],
        "category": "specific_connectable",
        "rationale": "Autonomous vehicles are a specific application area for AI systems, providing a strong contextual link.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.79,
        "link_intent_score": 0.78
      },
      {
        "surface": "post-hoc explanations",
        "canonical": "Post-hoc Explanations",
        "aliases": [
          "explanation methods",
          "explanation techniques"
        ],
        "category": "unique_technical",
        "rationale": "Post-hoc explanations are crucial for understanding AI model decisions, offering a unique technical aspect for linking.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.76,
        "link_intent_score": 0.82
      },
      {
        "surface": "traffic sign classifiers",
        "canonical": "Traffic Sign Classification",
        "aliases": [
          "traffic sign recognition",
          "road sign classifiers"
        ],
        "category": "specific_connectable",
        "rationale": "Traffic sign classification is a specific task within computer vision, relevant for autonomous vehicle systems.",
        "novelty_score": 0.58,
        "connectivity_score": 0.79,
        "specificity_score": 0.81,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "AI systems",
      "training approaches",
      "saliency maps"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "pruning",
      "resolved_canonical": "Model Pruning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "autonomous vehicles",
      "resolved_canonical": "Autonomous Vehicles",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.79,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "post-hoc explanations",
      "resolved_canonical": "Post-hoc Explanations",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.76,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "traffic sign classifiers",
      "resolved_canonical": "Traffic Sign Classification",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.79,
        "specificity": 0.81,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Smaller is Better: Enhancing Transparency in Vehicle AI Systems via Pruning

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20148.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.20148](https://arxiv.org/abs/2509.20148)

## 🔗 유사한 논문
- [[2025-09-23/Building Transparency in Deep Learning-Powered Network Traffic Classification_ A Traffic-Explainer Framework_20250923|Building Transparency in Deep Learning-Powered Network Traffic Classification: A Traffic-Explainer Framework]] (83.5% similar)
- [[2025-09-23/Interpretability-Aware Pruning for Efficient Medical Image Analysis_20250923|Interpretability-Aware Pruning for Efficient Medical Image Analysis]] (83.5% similar)
- [[2025-09-22/Training A Neural Network For Partially Occluded Road Sign Identification In The Context Of Autonomous Vehicles_20250922|Training A Neural Network For Partially Occluded Road Sign Identification In The Context Of Autonomous Vehicles]] (82.7% similar)
- [[2025-09-22/Explainable AI for Maritime Autonomous Surface Ships (MASS)_ Adaptive Interfaces and Trustworthy Human-AI Collaboration_20250922|Explainable AI for Maritime Autonomous Surface Ships (MASS): Adaptive Interfaces and Trustworthy Human-AI Collaboration]] (81.7% similar)
- [[2025-09-23/Towards a Transparent and Interpretable AI Model for Medical Image Classifications_20250923|Towards a Transparent and Interpretable AI Model for Medical Image Classifications]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Autonomous Vehicles|Autonomous Vehicles]], [[keywords/Traffic Sign Classification|Traffic Sign Classification]]
**⚡ Unique Technical**: [[keywords/Model Pruning|Model Pruning]], [[keywords/Post-hoc Explanations|Post-hoc Explanations]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20148v1 Announce Type: new 
Abstract: Connected and autonomous vehicles continue to heavily rely on AI systems, where transparency and security are critical for trust and operational safety. Post-hoc explanations provide transparency to these black-box like AI models but the quality and reliability of these explanations is often questioned due to inconsistencies and lack of faithfulness in representing model decisions. This paper systematically examines the impact of three widely used training approaches, namely natural training, adversarial training, and pruning, affect the quality of post-hoc explanations for traffic sign classifiers. Through extensive empirical evaluation, we demonstrate that pruning significantly enhances the comprehensibility and faithfulness of explanations (using saliency maps). Our findings reveal that pruning not only improves model efficiency but also enforces sparsity in learned representation, leading to more interpretable and reliable decisions. Additionally, these insights suggest that pruning is a promising strategy for developing transparent deep learning models, especially in resource-constrained vehicular AI systems.

## 📝 요약

이 논문은 연결 및 자율 주행 차량에서 AI 시스템의 투명성과 보안성을 높이기 위한 연구로, 특히 사후 설명의 품질을 향상시키는 방법을 탐구합니다. 자연 훈련, 적대적 훈련, 가지치기라는 세 가지 훈련 접근법이 교통 표지판 분류기의 사후 설명에 미치는 영향을 체계적으로 분석했습니다. 실험 결과, 가지치기가 설명의 이해도와 충실도를 크게 향상시킴을 보여주었습니다. 가지치기는 모델 효율성을 높이고 학습된 표현의 희소성을 강화하여 더 해석 가능하고 신뢰할 수 있는 결정을 가능하게 합니다. 이러한 결과는 자원 제약이 있는 차량 AI 시스템에서 투명한 딥러닝 모델 개발에 가지치기가 유망한 전략임을 시사합니다.

## 🎯 주요 포인트

- 1. 연결 및 자율 주행 차량의 AI 시스템에서 투명성과 보안은 신뢰와 운영 안전에 필수적입니다.
- 2. 사후 설명은 AI 모델의 투명성을 제공하지만, 설명의 품질과 신뢰성은 종종 일관성 부족과 모델 결정의 충실성 부족으로 의문시됩니다.
- 3. 자연 훈련, 적대적 훈련, 가지치기라는 세 가지 훈련 접근 방식이 교통 표지판 분류기의 사후 설명 품질에 미치는 영향을 체계적으로 조사했습니다.
- 4. 가지치기는 설명의 이해 가능성과 충실성을 크게 향상시키며, 모델 효율성을 개선하고 학습된 표현의 희소성을 강화합니다.
- 5. 가지치기는 특히 자원이 제한된 차량 AI 시스템에서 투명한 딥러닝 모델 개발을 위한 유망한 전략으로 제안됩니다.


---

*Generated on 2025-09-26 09:13:10*