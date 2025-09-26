---
keywords:
  - Handwritten Text Recognition
  - Wasserstein Distance
  - Character Frequency Distribution
  - Guided Decoding
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2506.09846
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:06:40.756020",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Handwritten Text Recognition",
    "Wasserstein Distance",
    "Character Frequency Distribution",
    "Guided Decoding"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Handwritten Text Recognition": 0.78,
    "Wasserstein Distance": 0.82,
    "Character Frequency Distribution": 0.75,
    "Guided Decoding": 0.73
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Handwritten Text Recognition",
        "canonical": "Handwritten Text Recognition",
        "aliases": [
          "HTR"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific domain within computer vision that directly relates to the paper's focus on character frequency distribution shifts.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Wasserstein distance",
        "canonical": "Wasserstein Distance",
        "aliases": [
          "Earth Mover's Distance"
        ],
        "category": "specific_connectable",
        "rationale": "This mathematical concept is central to the proposed method for aligning character frequency distributions.",
        "novelty_score": 0.58,
        "connectivity_score": 0.77,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Character Frequency Distribution",
        "canonical": "Character Frequency Distribution",
        "aliases": [
          "Character Distribution"
        ],
        "category": "unique_technical",
        "rationale": "This term is crucial for understanding the paper's approach to improving model performance.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      },
      {
        "surface": "Guided Decoding Scheme",
        "canonical": "Guided Decoding",
        "aliases": [
          "Decoding Scheme"
        ],
        "category": "unique_technical",
        "rationale": "This technique is a novel contribution of the paper, enhancing model inference without retraining.",
        "novelty_score": 0.66,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.73
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
      "candidate_surface": "Handwritten Text Recognition",
      "resolved_canonical": "Handwritten Text Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Wasserstein distance",
      "resolved_canonical": "Wasserstein Distance",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.77,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Character Frequency Distribution",
      "resolved_canonical": "Character Frequency Distribution",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Guided Decoding Scheme",
      "resolved_canonical": "Guided Decoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.66,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.73
      }
    }
  ]
}
-->

# Learning to Align: Addressing Character Frequency Distribution Shifts in Handwritten Text Recognition

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.09846.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2506.09846](https://arxiv.org/abs/2506.09846)

## 🔗 유사한 논문
- [[2025-09-19/Moment- and Power-Spectrum-Based Gaussianity Regularization for Text-to-Image Models_20250919|Moment- and Power-Spectrum-Based Gaussianity Regularization for Text-to-Image Models]] (82.2% similar)
- [[2025-09-22/DNA-DetectLLM_ Unveiling AI-Generated Text via a DNA-Inspired Mutation-Repair Paradigm_20250922|DNA-DetectLLM: Unveiling AI-Generated Text via a DNA-Inspired Mutation-Repair Paradigm]] (80.4% similar)
- [[2025-09-22/AmpleHate_ Amplifying the Attention for Versatile Implicit Hate Detection_20250922|AmpleHate: Amplifying the Attention for Versatile Implicit Hate Detection]] (80.2% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (80.0% similar)
- [[2025-09-22/VLA-Mark_ A cross modal watermark for large vision-language alignment model_20250922|VLA-Mark: A cross modal watermark for large vision-language alignment model]] (79.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Wasserstein Distance|Wasserstein Distance]]
**⚡ Unique Technical**: [[keywords/Handwritten Text Recognition|Handwritten Text Recognition]], [[keywords/Character Frequency Distribution|Character Frequency Distribution]], [[keywords/Guided Decoding|Guided Decoding]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.09846v2 Announce Type: replace-cross 
Abstract: Handwritten text recognition aims to convert visual input into machine-readable text, and it remains challenging due to the evolving and context-dependent nature of handwriting. Character sets change over time, and character frequency distributions shift across historical periods or regions, often causing models trained on broad, heterogeneous corpora to underperform on specific subsets. To tackle this, we propose a novel loss function that incorporates the Wasserstein distance between the character frequency distribution of the predicted text and a target distribution empirically derived from training data. By penalizing divergence from expected distributions, our approach enhances both accuracy and robustness under temporal and contextual intra-dataset shifts. Furthermore, we demonstrate that character distribution alignment can also improve existing models at inference time without requiring retraining by integrating it as a scoring function in a guided decoding scheme. Experimental results across multiple datasets and architectures confirm the effectiveness of our method in boosting generalization and performance. We open source our code at https://github.com/pkaliosis/fada.

## 📝 요약

이 논문은 필기 인식의 정확성과 강인성을 향상시키기 위해 새로운 손실 함수를 제안합니다. 필기체의 특성상 문자 집합과 빈도 분포가 시간과 지역에 따라 변동하여 기존 모델의 성능이 저하될 수 있습니다. 이를 해결하기 위해, 예측된 텍스트의 문자 빈도 분포와 훈련 데이터에서 경험적으로 도출된 목표 분포 간의 Wasserstein 거리를 활용한 손실 함수를 도입하여, 기대 분포와의 차이를 줄임으로써 성능을 향상시킵니다. 또한, 이 방법은 모델 재훈련 없이도 추론 시 성능을 개선할 수 있습니다. 여러 데이터셋과 아키텍처에서의 실험 결과는 제안된 방법의 일반화 능력과 성능 향상을 확인시켜 줍니다. 코드는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 손글씨 인식에서 문자 빈도 분포의 변화는 모델의 성능 저하를 초래할 수 있으며, 이를 해결하기 위해 새로운 손실 함수를 제안합니다.
- 2. 제안된 손실 함수는 예측된 텍스트의 문자 빈도 분포와 훈련 데이터에서 경험적으로 도출된 목표 분포 간의 Wasserstein 거리를 포함합니다.
- 3. 문자 분포 정렬은 기존 모델의 추론 성능을 향상시킬 수 있으며, 재훈련 없이도 가이드 디코딩 방식으로 통합할 수 있습니다.
- 4. 여러 데이터셋과 아키텍처에 대한 실험 결과, 제안된 방법이 일반화와 성능 향상에 효과적임을 확인했습니다.
- 5. 연구의 코드는 https://github.com/pkaliosis/fada에서 오픈 소스로 제공됩니다.


---

*Generated on 2025-09-24 01:06:40*