---
keywords:
  - Neural Network
  - Lateral Connections
  - Recurrent Activation
  - Excitatory-Inhibitory Separation
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15460
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T08:59:47.540821",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Lateral Connections",
    "Recurrent Activation",
    "Excitatory-Inhibitory Separation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.85,
    "Lateral Connections": 0.78,
    "Recurrent Activation": 0.8,
    "Excitatory-Inhibitory Separation": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Convolutional Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "CNN",
          "Convolutional Networks"
        ],
        "category": "broad_technical",
        "rationale": "CNNs are a foundational concept in deep learning and computer vision, linking to a wide range of related research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Visual Cortical Lateral Connections",
        "canonical": "Lateral Connections",
        "aliases": [
          "Horizontal Connections"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's contribution and connects to biological neural network studies.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Recurrent Activation",
        "canonical": "Recurrent Activation",
        "aliases": [
          "Recurrent Processing"
        ],
        "category": "unique_technical",
        "rationale": "Recurrent activation is a specific mechanism explored in the paper, linking to studies on temporal dynamics in neural networks.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Excitatory-Inhibitory Separation",
        "canonical": "Excitatory-Inhibitory Separation",
        "aliases": [
          "E-I Separation"
        ],
        "category": "unique_technical",
        "rationale": "This separation is a novel architectural feature proposed in the paper, relevant to neural computation studies.",
        "novelty_score": 0.72,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
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
      "candidate_surface": "Convolutional Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Visual Cortical Lateral Connections",
      "resolved_canonical": "Lateral Connections",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Recurrent Activation",
      "resolved_canonical": "Recurrent Activation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Excitatory-Inhibitory Separation",
      "resolved_canonical": "Excitatory-Inhibitory Separation",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Incorporating Visual Cortical Lateral Connection Properties into CNN: Recurrent Activation and Excitatory-Inhibitory Separation

**Korean Title:** 시각 피질의 측면 연결 특성을 CNN에 통합하기: 순환 활성화와 흥분-억제 분리

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15460.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15460](https://arxiv.org/abs/2509.15460)

## 🔗 유사한 논문
- [[2025-09-22/Modeling the Human Visual System_ Comparative Insights from Response-Optimized and Task-Optimized Vision Models, Language Models, and different Readout Mechanisms_20250922|Modeling the Human Visual System: Comparative Insights from Response-Optimized and Task-Optimized Vision Models, Language Models, and different Readout Mechanisms]] (80.3% similar)
- [[2025-09-22/Deformable Dynamic Convolution for Accurate yet Efficient Spatio-Temporal Traffic Prediction_20250922|Deformable Dynamic Convolution for Accurate yet Efficient Spatio-Temporal Traffic Prediction]] (79.8% similar)
- [[2025-09-19/Leveraging Geometric Visual Illusions as Perceptual Inductive Biases for Vision Models_20250919|Leveraging Geometric Visual Illusions as Perceptual Inductive Biases for Vision Models]] (79.5% similar)
- [[2025-09-22/Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images_20250922|Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images]] (78.6% similar)
- [[2025-09-22/Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception_20250922|Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception]] (78.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**⚡ Unique Technical**: [[keywords/Lateral Connections|Lateral Connections]], [[keywords/Recurrent Activation|Recurrent Activation]], [[keywords/Excitatory-Inhibitory Separation|Excitatory-Inhibitory Separation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15460v1 Announce Type: cross 
Abstract: The original Convolutional Neural Networks (CNNs) and their modern updates such as the ResNet are heavily inspired by the mammalian visual system. These models include afferent connections (retina and LGN to the visual cortex) and long-range projections (connections across different visual cortical areas). However, in the mammalian visual system, there are connections within each visual cortical area, known as lateral (or horizontal) connections. These would roughly correspond to connections within CNN feature maps, and this important architectural feature is missing in current CNN models. In this paper, we present how such lateral connections can be modeled within the standard CNN framework, and test its benefits and analyze its emergent properties in relation to the biological visual system. We will focus on two main architectural features of lateral connections: (1) recurrent activation and (2) separation of excitatory and inhibitory connections. We show that recurrent CNN using weight sharing is equivalent to lateral connections, and propose a custom loss function to separate excitatory and inhibitory weights. The addition of these two leads to increased classification accuracy, and importantly, the activation properties and connection properties of the resulting model show properties similar to those observed in the biological visual system. We expect our approach to help align CNN closer to its biological counterpart and better understand the principles of visual cortical computation.

## 🔍 Abstract (한글 번역)

arXiv:2509.15460v1 발표 유형: 교차  
초록: 원래의 합성곱 신경망(CNN)과 ResNet과 같은 현대적 업데이트는 포유류의 시각 시스템에서 크게 영감을 받았습니다. 이러한 모델은 구심성 연결(망막과 시상 LGN에서 시각 피질로)과 장거리 투사(다양한 시각 피질 영역 간의 연결)를 포함합니다. 그러나 포유류의 시각 시스템에서는 각 시각 피질 영역 내에 있는 연결, 즉 측면(또는 수평) 연결이 존재합니다. 이러한 연결은 대략적으로 CNN 특징 맵 내의 연결에 해당하며, 이 중요한 구조적 특징은 현재의 CNN 모델에서 누락되어 있습니다. 이 논문에서는 표준 CNN 프레임워크 내에서 이러한 측면 연결을 어떻게 모델링할 수 있는지 제시하고, 그 이점과 생물학적 시각 시스템과의 관계에서 발생하는 특성을 분석합니다. 우리는 측면 연결의 두 가지 주요 구조적 특징에 중점을 둘 것입니다: (1) 재귀적 활성화와 (2) 흥분성 및 억제성 연결의 분리. 우리는 가중치 공유를 사용하는 재귀적 CNN이 측면 연결과 동등하다는 것을 보여주고, 흥분성 및 억제성 가중치를 분리하기 위한 맞춤형 손실 함수를 제안합니다. 이 두 가지를 추가하면 분류 정확도가 증가하고, 결과 모델의 활성화 특성과 연결 특성은 생물학적 시각 시스템에서 관찰되는 특성과 유사한 특성을 나타냅니다. 우리는 우리의 접근 방식이 CNN을 생물학적 대응물에 더 가깝게 정렬하고 시각 피질 계산의 원리를 더 잘 이해하는 데 도움이 되기를 기대합니다.

## 📝 요약

이 논문은 기존의 CNN 모델에 결여된 측면 연결(lateral connections)을 도입하여 생물학적 시각 시스템과의 유사성을 높이고자 합니다. 저자들은 CNN 내에서 측면 연결을 모델링하고, 그 이점을 실험적으로 분석했습니다. 주요 방법론은 (1) 재귀적 활성화와 (2) 흥분성 및 억제성 연결의 분리를 포함합니다. 재귀적 CNN은 가중치 공유를 통해 측면 연결과 동등하게 구현되며, 맞춤형 손실 함수를 사용해 흥분성 및 억제성 가중치를 분리합니다. 이러한 접근은 분류 정확도를 향상시키고, 모델의 활성화 및 연결 특성이 생물학적 시각 시스템과 유사한 특성을 보임을 확인했습니다. 이 연구는 CNN을 생물학적 시각 시스템에 더 가깝게 맞추고, 시각 피질 계산의 원리를 이해하는 데 기여할 것으로 기대됩니다.

## 🎯 주요 포인트

- 1. 기존의 CNN 모델은 포유류의 시각 시스템에서 영감을 받아 설계되었으나, 시각 피질 내의 가로 연결이 부족하다.
- 2. 논문에서는 CNN 프레임워크 내에서 가로 연결을 모델링하는 방법을 제시하고, 그 이점을 테스트하고 분석한다.
- 3. 가로 연결의 주요 특징으로는 재귀적 활성화와 흥분성 및 억제성 연결의 분리가 있다.
- 4. 제안된 모델은 분류 정확도를 높이고, 생물학적 시각 시스템과 유사한 활성화 및 연결 특성을 보인다.
- 5. 이 접근법은 CNN을 생물학적 시각 시스템에 더 가깝게 정렬하고 시각 피질 계산의 원리를 이해하는 데 도움을 줄 것으로 기대된다.


---

*Generated on 2025-09-23 08:59:47*