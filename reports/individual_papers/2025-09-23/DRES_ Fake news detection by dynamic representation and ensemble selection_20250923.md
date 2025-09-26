---
keywords:
  - Fake News Detection
  - Dynamic Representation and Ensemble Selection
  - Instance Hardness Measures
  - Textual Feature Representations
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16893
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:44:21.492596",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Fake News Detection",
    "Dynamic Representation and Ensemble Selection",
    "Instance Hardness Measures",
    "Textual Feature Representations"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Fake News Detection": 0.8,
    "Dynamic Representation and Ensemble Selection": 0.85,
    "Instance Hardness Measures": 0.78,
    "Textual Feature Representations": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "fake news detection",
        "canonical": "Fake News Detection",
        "aliases": [
          "misinformation detection",
          "disinformation detection"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application area that connects to broader topics in social media analysis and information integrity.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Dynamic Representation and Ensemble Selection",
        "canonical": "Dynamic Representation and Ensemble Selection",
        "aliases": [
          "DRES"
        ],
        "category": "unique_technical",
        "rationale": "The method is central to the paper and represents a novel approach to improving classification accuracy.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "instance hardness measures",
        "canonical": "Instance Hardness Measures",
        "aliases": [
          "difficulty estimation"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is crucial for understanding the adaptive nature of the proposed method.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "textual feature representations",
        "canonical": "Textual Feature Representations",
        "aliases": [
          "text features"
        ],
        "category": "broad_technical",
        "rationale": "This is a fundamental concept in text analysis and connects to various NLP techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "fake news detection",
      "resolved_canonical": "Fake News Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Dynamic Representation and Ensemble Selection",
      "resolved_canonical": "Dynamic Representation and Ensemble Selection",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "instance hardness measures",
      "resolved_canonical": "Instance Hardness Measures",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "textual feature representations",
      "resolved_canonical": "Textual Feature Representations",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# DRES: Fake news detection by dynamic representation and ensemble selection

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16893.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16893](https://arxiv.org/abs/2509.16893)

## 🔗 유사한 논문
- [[2025-09-22/Multimodal Learning for Fake News Detection in Short Videos Using Linguistically Verified Data and Heterogeneous Modality Fusion_20250922|Multimodal Learning for Fake News Detection in Short Videos Using Linguistically Verified Data and Heterogeneous Modality Fusion]] (82.1% similar)
- [[2025-09-18/An Attention-Based Denoising Framework for Personality Detection in Social Media Texts_20250918|An Attention-Based Denoising Framework for Personality Detection in Social Media Texts]] (79.5% similar)
- [[2025-09-22/RAVE_ Retrieval and Scoring Aware Verifiable Claim Detection_20250922|RAVE: Retrieval and Scoring Aware Verifiable Claim Detection]] (79.5% similar)
- [[2025-09-22/Efficient Extractive Text Summarization for Online News Articles Using Machine Learning_20250922|Efficient Extractive Text Summarization for Online News Articles Using Machine Learning]] (79.0% similar)
- [[2025-09-22/Toward Medical Deepfake Detection_ A Comprehensive Dataset and Novel Method_20250922|Toward Medical Deepfake Detection: A Comprehensive Dataset and Novel Method]] (78.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Textual Feature Representations|Textual Feature Representations]]
**🔗 Specific Connectable**: [[keywords/Instance Hardness Measures|Instance Hardness Measures]]
**⚡ Unique Technical**: [[keywords/Fake News Detection|Fake News Detection]], [[keywords/Dynamic Representation and Ensemble Selection|Dynamic Representation and Ensemble Selection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16893v1 Announce Type: new 
Abstract: The rapid spread of information via social media has made text-based fake news detection critically important due to its societal impact. This paper presents a novel detection method called Dynamic Representation and Ensemble Selection (DRES) for identifying fake news based solely on text. DRES leverages instance hardness measures to estimate the classification difficulty for each news article across multiple textual feature representations. By dynamically selecting the textual representation and the most competent ensemble of classifiers for each instance, DRES significantly enhances prediction accuracy. Extensive experiments show that DRES achieves notable improvements over state-of-the-art methods, confirming the effectiveness of representation selection based on instance hardness and dynamic ensemble selection in boosting performance. Codes and data are available at: https://github.com/FFarhangian/FakeNewsDetection_DRES

## 📝 요약

이 논문은 소셜 미디어를 통한 정보 확산으로 인해 중요해진 텍스트 기반 가짜 뉴스 탐지를 위한 새로운 방법론인 DRES(Dynamic Representation and Ensemble Selection)를 제안합니다. DRES는 인스턴스 난이도 측정을 통해 각 뉴스 기사의 분류 난이도를 평가하고, 이에 따라 최적의 텍스트 표현과 분류기 앙상블을 동적으로 선택하여 예측 정확도를 향상시킵니다. 실험 결과, DRES는 기존 최첨단 방법들보다 성능이 뛰어남을 보여주며, 인스턴스 난이도 기반의 표현 선택과 동적 앙상블 선택이 성능 향상에 효과적임을 확인했습니다. 코드와 데이터는 GitHub에서 제공됩니다.

## 🎯 주요 포인트

- 1. DRES는 텍스트 기반의 가짜 뉴스 탐지를 위한 새로운 방법으로, 인스턴스 난이도 측정을 활용하여 각 뉴스 기사의 분류 난이도를 추정합니다.
- 2. DRES는 각 인스턴스에 대해 텍스트 표현과 가장 적합한 분류기 앙상블을 동적으로 선택하여 예측 정확도를 크게 향상시킵니다.
- 3. 실험 결과, DRES는 최신 방법들에 비해 성능이 크게 개선되었으며, 인스턴스 난이도 기반의 표현 선택과 동적 앙상블 선택의 효과를 입증했습니다.
- 4. 연구의 코드와 데이터는 https://github.com/FFarhangian/FakeNewsDetection_DRES 에서 제공됩니다.


---

*Generated on 2025-09-24 01:44:21*